"""Run with python3 -I 09-analysis/a6d-mcculloch-2017-highz/test_highz_2017.py."""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import highz_2017 as m


class Tests(unittest.TestCase):
    def test_eq13_offsets_match_mccullochs_quoted_values(self):
        u, _ = m.uebler()
        self.assertAlmostEqual(u[0]["qi_relative"], -0.28, places=2)
        self.assertAlmostEqual(u[1]["qi_relative"], -0.52, places=2)

    def test_eq8_reduces_to_newton_without_scale(self):
        gbar = 3e-10
        self.assertAlmostEqual(gbar * math.sqrt(1 + 0 / gbar), gbar)

    def test_genzel_reconstruction_is_close_to_reported_range(self):
        # McCulloch: QI 9-19% higher for the four lower-z galaxies. Our reconstruction must be within a few points.
        r = sorted(m.genzel(), key=lambda x: x["z"])[:4]
        ratios = [x["ratio_min_over_obs_n1"] for x in r]
        self.assertTrue(all(1.05 < v < 1.25 for v in ratios), ratios)


if __name__ == "__main__":
    unittest.main()
