"""Run with .venv/bin/python -I 09-analysis/a6c-rc100-qi/test_rc100_qi.py."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rc100_qi as m


class InverseTests(unittest.TestCase):
    def test_qi_inverse_is_exact(self):
        gbar = np.array([1e-30, 1e-12, 1e-11, 1e-10, 1e-9])
        a = 2e-10
        gobs = gbar * np.sqrt(1 + a / gbar)
        np.testing.assert_allclose(m.gbar_qi(gobs, a), gbar, rtol=1e-10, atol=0)

    def test_mcgaugh_inverse(self):
        gbar = np.array([1e-12, 1e-11, 1e-10, 1e-9])
        a = 1.2e-10
        gobs = gbar / (1 - np.exp(-np.sqrt(gbar / a)))
        np.testing.assert_allclose(m.gbar_mcg(gobs, a), gbar, rtol=2e-3)

    def test_fdm_prediction_limits(self):
        # Far above the scale the prediction is Newtonian (no dark matter); far below it approaches 1.
        self.assertAlmostEqual(float(m.fpred("qi", np.array([1e-6]), 1e-10)[0]), 0.0, places=3)
        self.assertGreater(float(m.fpred("qi", np.array([1e-13]), 1e-10)[0]), 0.98)


class DataTests(unittest.TestCase):
    def test_correlated_error_propagation(self):
        # Perfect positive correlation: the two linear errors share one deviate.
        ef, sg, d, tau = 0.1, 0.4, -0.3, 0.05
        self.assertAlmostEqual(m.residual_variance(ef, sg, d, tau, rho=1), (ef - d * sg) ** 2 + tau ** 2)
        self.assertAlmostEqual(m.residual_variance(ef, sg, d, tau, rho=0), ef ** 2 + (d * sg) ** 2 + tau ** 2)

    def test_row87_correction_and_sentina_reproduction(self):
        rows = m.fetch()
        T = m.table(rows)
        i = int(np.where(T["id"] == 87)[0][0])
        self.assertEqual((T["Re"][i], T["fDM"][i], T["Vc"][i]), (3.85, 0.44, 250.0))
        self.assertAlmostEqual(T["sigma_lng"][i] ** 2, (2 * 42 / 250) ** 2 + (2 / 3.85) ** 2)
        Ts = m.table(rows, fix87=False, errors="sentina")
        ii = np.arange(len(Ts["z"]))
        c = m.fit("mcg", Ts, ii, m.LAWS["constant"], gamma=0.0)
        h = m.fit("mcg", Ts, ii, m.LAWS["hubble"], gamma=0.0)
        self.assertAlmostEqual(h[0] - c[0], 8.98, places=1)


if __name__ == "__main__":
    unittest.main()
