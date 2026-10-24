"""Run with python3 -I 09-analysis/a6-rar-redshift-evolution/test_redshift_scale.py."""
import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import redshift_scale as rs


class ConversionTests(unittest.TestCase):
    def test_deep_regime_scales_coincide(self):
        # Both functions reduce to g = sqrt(a * gbar) far below the scale.
        a = 2e-10
        self.assertAlmostEqual(rs.a0_equiv(a, mu=-18.0, w=0.3) / a, 1.0, places=3)

    def test_conversion_is_below_one_in_transition(self):
        # The QI function rises more slowly through the transition, so a smaller McGaugh a0 matches it.
        r = rs.a0_equiv(2e-10) / 2e-10
        self.assertTrue(0.7 < r < 0.95, r)

    def test_mass_offset_round_trip(self):
        a_q = 3e-10
        target = rs.a0_equiv(a_q, dm=-0.1)
        self.assertAlmostEqual(rs.mass_offset_for(target, a_q), -0.1, places=3)


class CosmologyTests(unittest.TestCase):
    def test_proper_horizon_matches_ideas_table(self):
        d0 = rs.proper_horizon_diameter(0.0)
        self.assertAlmostEqual(d0 / 1e26, 8.73, places=1)
        self.assertAlmostEqual(d0 / rs.proper_horizon_diameter(1.0), 2.63, places=2)


class AlcockReproductionTests(unittest.TestCase):
    def test_frozen_and_power_law(self):
        la, x2, _, _ = rs.fit_amplitude(lambda la: [10 ** la * 1e10 for _ in rs.BINS], "c68")
        self.assertAlmostEqual(10 ** la * 1e10, 2.28, places=2)
        self.assertAlmostEqual(x2, 28.8, places=1)
        d = rs.power_law_fit(lambda la, g: [10 ** la * 1e10 * (1 + z) ** g for z in rs.zs()], "c68")
        self.assertAlmostEqual(d["gamma"], 0.78, places=2)
        self.assertAlmostEqual(d["sigma"], 0.15, places=2)

    def test_chi2_uses_bar_on_model_side(self):
        z, a, lo, hi = rs.BINS[2]
        above, _ = rs.chi2([a + hi if i == 2 else b[1] for i, b in enumerate(rs.BINS)])
        below, _ = rs.chi2([a - lo if i == 2 else b[1] for i, b in enumerate(rs.BINS)])
        self.assertAlmostEqual(above, 1.0)
        self.assertAlmostEqual(below, 1.0)
        self.assertAlmostEqual(rs.chi2([b[1] + b[3] for b in rs.BINS], reading="c95")[0], 4 * 1.96 ** 2)

    def test_pvalue(self):
        self.assertAlmostEqual(rs.pvalue(7.815, 3), 0.05, places=3)
        self.assertAlmostEqual(rs.sigma_from_p(math.erfc(2 / math.sqrt(2))), 2.0, places=4)

    def test_underflow_does_not_export_infinite_significance(self):
        row = rs.model_row("extreme", "extreme", [1e6] * 4, 0, "c95")
        self.assertTrue(row["p_underflow"])
        self.assertIsNone(row["sigma"])
        json.dumps(row, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
