"""Regression checks for the review fixes. Run with .venv/bin/python -I <this file>."""
import json
import math
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fit_galaxies as fit


class FitDiagnosticsTests(unittest.TestCase):
    def test_velocity_error_change_preserves_priors_and_original_data(self):
        # Gas-only Newtonian prediction is 100 km/s at each radius.
        # Residuals 10 and -10 with errors 5 and 2 give chi2 = 4 + 25.
        g = dict(bulge=False, R=np.array([1., 2.]), V=np.array([110., 90.]),
                 eV=np.array([5., 2.]), Vg=np.array([100., 100.]),
                 Vd=np.zeros(2), Vb=np.zeros(2), D0=10., eD=2., i0=60., ei=5.)
        p = [math.log10(fit.UD0) + fit.SIG_LOGU, 10., 60.]
        new = fit.with_velocity_errors([g], 3.)[0]
        chi2, penalty = fit.objective_terms(p, g, np.ones_like, -10.)
        new_chi2, new_penalty = fit.objective_terms(p, new, np.ones_like, -10.)
        self.assertAlmostEqual(chi2, 29.)
        self.assertAlmostEqual(penalty, 1.)
        self.assertAlmostEqual(new_chi2, 29. / 9.)
        self.assertAlmostEqual(new_penalty, 1.)
        np.testing.assert_array_equal(g["eV"], [5., 2.])
        for key in ("eD", "ei", "D0", "i0"):
            self.assertEqual(new[key], g[key])

    def test_fractional_distance_shifts_are_not_standardized_pulls(self):
        rows = [dict(D_ratio=np.float64(.75), pull_D=np.float64(-5.)), dict(D_ratio=.75, pull_D=-1.),
                dict(D_ratio=1.1, pull_D=.5)]
        result = fit.distance_summary(rows)
        self.assertEqual(result["n_D_ratio_lt_0p8"], 2)
        self.assertEqual(result["n_pull_D_lt_minus2"], 1)
        self.assertEqual(result["n_pull_D_lt_minus3"], 1)
        self.assertEqual(result["median_pull_D"], -1.)
        self.assertEqual(json.loads(json.dumps(result)), result)

    def test_free_qi_profile_contains_exact_fixed_scale(self):
        grid = np.array([-9.96, -9.95, -9.94, fit.LA_LATE])
        la, loss = fit.profile_minimum(grid, np.array([100., 99., 100., 0.]))
        self.assertEqual(la, fit.LA_LATE)
        self.assertEqual(loss, 0.)


if __name__ == "__main__":
    unittest.main()
