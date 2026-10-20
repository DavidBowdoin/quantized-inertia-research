"""Run with python3 -I 09-analysis/a1-sparc-rar-refit/test_rar_refit.py."""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rar_refit as fit


class PublicBinsTests(unittest.TestCase):
    def test_fixed_prediction_is_compared_to_scatter_not_error_of_mean(self):
        # Choose gbar = a_Q: Eq. 8 gives gobs = sqrt(2) * a_Q.
        a = fit.theta_to_a(fit.THETA_LATE)
        x = math.log10(a)
        y = math.log10(math.sqrt(2) * a)
        rows = [dict(x=x, y=y + .15, sd=.2, n=100),
                dict(x=x, y=y - .3, sd=.2, n=400)]
        r = fit.public_bin_comparison(rows)
        q = r["comparisons"]["qi_late"]
        self.assertEqual(r["n_points"], 500)
        self.assertEqual(q["n_bins_within_one_scatter"], 1)
        self.assertAlmostEqual(q["bins"][0]["residual_over_scatter"], .75)
        self.assertAlmostEqual(q["bins"][1]["residual_over_scatter"], -1.5)
        # Changing bin counts cannot change a comparison with within-bin scatter.
        rows[0]["n"] = 10000
        self.assertEqual(fit.public_bin_comparison(rows)["comparisons"], r["comparisons"])
        self.assertEqual(r["comparisons"]["rar_reference"]["a"], 1.2e-10)


if __name__ == "__main__":
    unittest.main()
