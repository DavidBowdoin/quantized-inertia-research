"""Run with .venv/bin/python -I 09-analysis/a6b-musedark-per-galaxy/test_musedark_qi.py."""
import math
import sys
import unittest
from pathlib import Path

import numpy as np
from scipy.special import i0, i1, k0, k1

sys.path.insert(0, str(Path(__file__).resolve().parent))
import musedark_qi as m


class MassModelTests(unittest.TestCase):
    def test_sed_budget_conserves_total_stellar_mass_with_bulge(self):
        # Unit responses let the summed velocity contributions measure total mass.
        g = dict(m_dyn=10.0, m_bulge=1e10, m_sed=10.0, z=1.0,
                 vd1=np.ones(2), vb=np.full(2, 1e10), vh=np.zeros(2))
        np.testing.assert_allclose(m.baryonic_vc2(g, "sed"), 1e10)
        np.testing.assert_allclose(m.baryonic_vc2(g, "sed_h2"), 1e10 * (1 + m.mu_h2(1.0, 10.0)))
        # Original bookkeeping is retained only to reproduce the source.
        np.testing.assert_allclose(m.baryonic_vc2(g, "sed", source_budget=True), 2e10)

    def test_thin_exponential_disc_matches_freeman(self):
        Re = 5.0
        Rd = Re / 1.678
        r = np.array([1.0, 2.0, 4.0, 8.0])
        y = r / (2 * Rd)
        freeman = 4 * np.pi * m.G / (2 * np.pi * Rd ** 2) * Rd * y ** 2 * (i0(y) * k0(y) - i1(y) * k1(y))
        np.testing.assert_allclose(m.vc2_disc(r, Re, 1.0, aspect=0.001), freeman, rtol=0.015)

    def test_disc_is_keplerian_far_out(self):
        r = np.array([200.0])
        self.assertAlmostEqual(float(m.vc2_disc(r, 5.0, 1.5)[0] * r[0] / m.G), 1.0, places=2)

    def test_dc14_reduces_to_nfw_mass(self):
        r = np.array([1.0, 10.0, 50.0])
        rs, rhos = 10.0, 1e7
        nfw = 4 * np.pi * rhos * rs ** 3 * (np.log(1 + r / rs) - r / (r + rs))
        np.testing.assert_allclose(m.dc14_mass(r, rhos, rs, 1.0, 3.0, 1.0), nfw, rtol=2e-3)


class FitTests(unittest.TestCase):
    def test_scale_and_exponent_are_recovered(self):
        x = np.linspace(-12, -10, 400)
        z = np.repeat([0.5, 0.8, 1.1, 1.4], 100)
        la_true, g_true = -9.85, 1.0
        y = m.model("qi", x, la_true + g_true * np.log10(1 + z))
        la, g, rms = m.fit_law(x, y, z)
        self.assertAlmostEqual(la, la_true, places=3)
        self.assertAlmostEqual(g, g_true, places=2)
        lq, edge = m.fit_scale("qi", x[:100], y[:100])
        self.assertAlmostEqual(lq, la_true + np.log10(1.5), delta=0.003)
        self.assertFalse(edge)

    def test_h2_scaling_matches_karpov_form(self):
        # At the Tacconi pivot, log(1+z) = 0.63 and log M = 10.7, mu = 10^0.07 on the main sequence.
        z = 10 ** 0.63 - 1
        self.assertAlmostEqual(m.mu_h2(z, 10.7), 10 ** 0.07, places=6)


if __name__ == "__main__":
    unittest.main()
