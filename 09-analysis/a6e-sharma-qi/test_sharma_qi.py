"""Run with .venv/bin/python -I 09-analysis/a6e-sharma-qi/test_sharma_qi.py."""
import math
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sharma_qi as m


class Tests(unittest.TestCase):
    def test_observed_slope_matches_eq8_derivative(self):
        # For g = sqrt(gb^2 + a gb), d ln g / d ln gb = (2 gb + a) / (2 (gb + a)) = (1 + (gb/g)^2) / 2.
        gb, a = 3e-11, 2e-10
        g = math.sqrt(gb * gb + a * gb)
        self.assertAlmostEqual((2 * gb + a) / (2 * (gb + a)), 0.5 * (1 + (gb / g) ** 2), places=12)

    def test_weights_do_not_depend_on_the_model(self):
        A = dict(z=np.array([1.0]), ln_gobs=np.array([math.log(3e-10)]), ln_gbar=np.array([math.log(1e-10)]),
                 s_v=np.array([0.1]), s_m=np.array([0.5]), s_r=np.array([0.2]))
        A["slope"] = np.clip(0.5 * (1 + np.exp(2 * (A["ln_gbar"] - A["ln_gobs"]))), 0.5, 1.0)
        # With zero residual for a matching scale, nll differences come only from residuals, not variances.
        a_true = (3e-10 ** 2 - 1e-10 ** 2) / 1e-10
        n0 = m.nll(A, lambda z: np.full_like(z, a_true), 0.0)
        n1 = m.nll(A, lambda z: np.full_like(z, 2 * a_true), 0.0)
        self.assertGreater(n1, n0)

    def test_eq13_mass(self):
        # v = 200 km/s at z = 0: M = v^4 Theta / (2 G c^2) ~ 7.7e10 Msun with Theta = 8.8e26 m.
        rows = [dict(Redshift="0", VRout="200", Mbar="1e10", Mbar_Rout="1e10", survey="X")]
        t = m.tf_offsets(rows)[0]
        m_qi = (2e5) ** 4 * m.THETA0 / (2 * 6.674e-11 * m.C ** 2) / 1.989e30
        self.assertAlmostEqual(t["total"], 10 - math.log10(m_qi), places=6)


if __name__ == "__main__":
    unittest.main()
