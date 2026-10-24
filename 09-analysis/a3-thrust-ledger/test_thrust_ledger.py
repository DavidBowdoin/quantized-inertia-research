"""Run with python3 -I 09-analysis/a3-thrust-ledger/test_thrust_ledger.py."""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import thrust_ledger as m

RES = m.build()


def rows(device):
    return [r for r in RES["controlled"] if r["device"] == device]


class Formulas(unittest.TestCase):
    def test_photon_limit(self):
        self.assertAlmostEqual(m.PHOTON * 1e9, 3.336, places=3)              # nN/W, AGENTS.md gotcha
        self.assertAlmostEqual(m.f_ps(1.0, 1), m.PHOTON, places=20)

    def test_dresden_predictions_reproduce_except_rounding_and_one_q(self):
        for r in RES["controlled"]:
            if r["basis"].startswith("Dresden") and r["printed_pred"]:
                dev = abs(r["recomputed"] / r["printed_pred"] - 1)
                if r["setting"].startswith("1959 MHz"):
                    # N22 Table B2 prints 156 µN; 18 W × Q 2063 / c = 124 µN; Q 2599 reproduces 156 µN.
                    self.assertGreater(dev, 0.2)
                    self.assertAlmostEqual(m.f_ps(18, 2599) / r["printed_pred"], 1, delta=0.01)
                else:
                    self.assertLess(dev, 0.10, (r["device"], r["setting"]))   # N21 truncates to whole nN

    def test_mcculloch_2015_and_2018_tables(self):
        for k, v in RES["checks"]["pip_table1"].items():
            self.assertLess(abs(v["recomputed"] / v["printed"] - 1), 0.02, k)
        for k in ("Shawyer 1", "Shawyer 2", "Cannae", "NASA 2016 (80 W)"):
            v = RES["checks"]["epl_2015_3d"][k]
            self.assertLess(abs(v["recomputed"] / v["printed"] - 1), 0.02, k)
        for p, q, printed in ((145, 60, 29e-6), (145, 190, 92e-6), (63, 60, 12.6e-6), (63, 190, 40e-6)):
            self.assertLess(abs(m.f_met(p, q) / printed - 1), 0.005)

    def test_2017_dielectric_sign(self):
        s1 = next(r for r in RES["claimed"] if r["device"] == "EmDrive: Shawyer 1" and r["model"].startswith("2017"))
        self.assertLess(s1["pred"], 0)                                       # towards the wide end
        self.assertAlmostEqual(s1["pred"] / s1["printed_pred"], 1, delta=0.01)


class Casimir2022(unittest.TestCase):
    def check(self, eq):
        return next(r for r in RES["checks"]["casimir_2022"] if r["eq"] == eq)

    def test_reproduced(self):
        for eq in ("6", "7", "10"):
            self.assertAlmostEqual(self.check(eq)["ratio_printed_to_text"], 1, delta=0.1, msg=eq)

    def test_not_reproduced_from_printed_inputs(self):
        for eq in ("8", "9", "11"):
            c = self.check(eq)
            self.assertGreater(c["ratio_printed_to_text"], 1.8, eq)
            self.assertGreater(abs(c["table_inputs"] / c["printed"] - 1), 0.3, eq)

    def test_madrid_factor(self):
        self.assertAlmostEqual(10000 / 20, 500)                               # the text says 250


class Limits(unittest.TestCase):
    def test_upper_limit_convention(self):
        r = rows("Asymmetric fibre loop, vacuum (S > 3300)")[1]
        self.assertAlmostEqual(r["upper"], (0.08 + 2 * 0.26) * m.NN, places=15)
        neg = rows("EmDrive, spherical end cap (Q = 113–1027)")[1]               # (-7 ± 18) nN
        self.assertAlmostEqual(neg["upper"], 36 * m.NN, places=15)

    def test_capacitor_limit_is_three_sigma_as_given(self):
        for r in rows("Leakage-current capacitor (QI formulas applied by us)"):
            self.assertAlmostEqual(r["upper"], 0.3e-6 * m.G0, places=15)
            self.assertGreater(r["ratio"], 30)

    def test_revised_cavity_prediction_is_at_resolution(self):
        rr = rows("Silver laser cavities: McCulloch 2022 revised prediction")
        self.assertTrue(all(0.3 < r["ratio"] < 3 for r in rr))

    def test_revised_loop_prediction_vacuum_vs_air(self):
        self.assertTrue(all(r["ratio"] > 30 for r in rows("Asymmetric fibre loop, vacuum: McCulloch 2022 revised prediction")))
        self.assertTrue(all(r["ratio"] < 0.2 for r in rows("Asymmetric fibre loop, air: McCulloch 2022 revised prediction")))

    def test_ivo_over_photon(self):
        s = RES["stats"]
        self.assertTrue(1e7 < s["ivo_over_photon_lo"] < s["ivo_over_photon_hi"] < 2e7)

    def test_capacitor_formulas(self):
        self.assertAlmostEqual(m.v_electron(5000) / 2e7, 1, delta=0.06)        # McCulloch 2022 uses 2 × 10⁷ m/s
        self.assertAlmostEqual(m.f_capacitor_2021(10e-6, 10e-6, 1.0) * 1e3, 9.86, delta=0.05)


if __name__ == "__main__":
    unittest.main()
