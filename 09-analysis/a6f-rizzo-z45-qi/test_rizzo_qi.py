"""Run with .venv/bin/python -I 09-analysis/a6f-rizzo-z45-qi/test_rizzo_qi.py."""
import math
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rizzo_qi as m


class Tests(unittest.TestCase):
    def test_sersic_encloses_all_mass_far_out(self):
        r = 500.0
        self.assertAlmostEqual(float(m.v2_star(r, 1e10, 1.0, 2.0)) * r / (m.G * 1e10), 1.0, places=3)

    def test_sersic_half_mass_near_three_quarters_re(self):
        # Projected half-light radius R_e corresponds to a 3D half-mass radius of roughly 1.3 R_e for n ~ 1-4.
        Re, n = 1.0, 2.0
        frac = float(m.v2_star(1.33 * Re, 1.0, Re, n)) * 1.33 * Re / m.G
        self.assertTrue(0.45 < frac < 0.55, frac)

    def test_nfw_at_virial_radius(self):
        M, z = 1e12, 4.5
        R = m.r_vir(M, z, "bryan_norman")
        self.assertAlmostEqual(float(m.v2_dm(R, M, 3.0, z, "bryan_norman")) * R / (m.G * M), 1.0, places=6)

    def test_eq8_inversion(self):
        gbar, a = 3e-10, 1e-9
        gobs = math.sqrt(gbar * gbar + a * gbar)
        self.assertAlmostEqual(gbar * ((gobs / gbar) ** 2 - 1), a, delta=1e-20)


if __name__ == "__main__":
    unittest.main()
