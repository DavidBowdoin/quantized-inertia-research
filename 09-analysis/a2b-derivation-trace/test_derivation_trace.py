"""Run with python3 -I 09-analysis/a2b-derivation-trace/test_derivation_trace.py."""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import derivation_trace as m


def route(key):
    return next(r for r in m.routes() if r["key"] == key)


class Routes(unittest.TestCase):
    def test_2016_printed_mass_change_violates_its_conservation_equation(self):
        for theta in (2.6e26, m.THETA):
            aq = 2 * m.C ** 2 / theta
            for ratio in (1.0, 2.0, 10.0):
                with self.subTest(theta=theta, a_over_aq=ratio):
                    ch = m.check_2016_conservation(ratio * aq, theta)
                    self.assertAlmostEqual(ch["rearranged_eq13_residual"], 0.0, places=12)
                    self.assertAlmostEqual(ch["dm_over_m_from_eq13"], -ch["dm_over_m_printed"], places=12)
                    if ratio == 1.0:
                        self.assertAlmostEqual(ch["printed_eq13_residual"], 0.0, places=12)
                    else:
                        self.assertLess(ch["dm_over_m_from_eq13"], 0.0)
                        self.assertGreater(ch["dm_over_m_printed"], 0.0)
                        self.assertGreater(ch["printed_eq13_residual"], 1.0)

    def test_printed_coefficients(self):
        self.assertAlmostEqual(route("2007")["kappa"], m.BETA * math.pi ** 2, places=10)
        self.assertAlmostEqual(route("2013")["kappa"], 4 / math.pi, places=10)
        self.assertAlmostEqual(route("2016")["P"], 2 * math.pi * m.BETA, places=10)   # the paper's "26% too large"
        self.assertAlmostEqual(route("2017_area_lin")["P"], 4 / 3 * math.log(2), places=10)
        for k in ("2016", "2017_area_lin", "2020w", "2020i"):
            self.assertAlmostEqual(route(k)["kappa"], 2.0, places=8, msg=k)
        for k in ("2020w", "2020i"):
            self.assertAlmostEqual(route(k)["P"], 1.0, places=10, msg=k)

    def test_normalisation_choices_leave_kappa_alone(self):
        for k in ("2016_kT", "2016_halfhbar_halfcirc", "2020w_radii", "2020w_wien", "2020i_ln"):
            self.assertAlmostEqual(route(k)["kappa"], 2.0, places=8, msg=k)
        self.assertAlmostEqual(route("2020i_ln")["P"], math.log(2), places=10)

    def test_choices_that_move_kappa(self):
        self.assertAlmostEqual(route("2020w_mixed")["kappa"], 2 * math.pi, places=8)
        self.assertAlmostEqual(route("2020i_diam")["kappa"], 1.0, places=8)

    def test_unlinearised_area_route_is_quadratic(self):
        a = 4 * m.C ** 2 / m.THETA                                  # x = 1/2
        self.assertAlmostEqual(m.route_2017_area(a, m.THETA, False), 2 / 3 * math.log(2) * 0.75, places=12)
        self.assertGreater(route("2017_area_exact")["max_rel_departure"], 0.1)


class Laws(unittest.TestCase):
    def test_prefactor_changes_prediction_at_fixed_baryonic_acceleration(self):
        for g in (1e-12, m.A_Q, 1e-8):
            baseline = m.law_selfconsistent(g, m.A_Q)
            for p in (math.log(2), 2 * math.pi * m.BETA):
                a = m.law_selfconsistent(g, m.A_Q, prefactor=p)
                # Check the force balance, independently of the quadratic solution.
                self.assertAlmostEqual(p * (1 - m.A_Q / (a + m.A_Q)) * a / g, 1.0, places=12)
                self.assertGreater(abs(a / baseline - 1), 0.05)
                # Absorbing P into g is an additional calibration, unlike holding g fixed.
                self.assertAlmostEqual(m.law_selfconsistent(p * g, m.A_Q, prefactor=p) / baseline, 1.0, places=12)

    def test_identities(self):
        for k, v in m.law_checks().items():
            self.assertLess(v, 1e-12, k)

    def test_limits(self):
        aq = m.A_Q
        g = 1e-18
        for f in (m.law_2017, m.law_selfconsistent):
            self.assertAlmostEqual(f(g, aq) / m.law_deep(g, aq), 1, places=3)
        g = 1e-6                                                    # Newtonian offsets: Eq. 8 adds aq/2, the others aq
        self.assertAlmostEqual((m.law_2017(g, aq) - g) / aq, 0.5, places=3)
        self.assertAlmostEqual((m.law_selfconsistent(g, aq) - g) / aq, 1.0, places=3)
        self.assertAlmostEqual((m.law_additive(g, aq) - g) / aq, 1.0, places=9)

    def test_nu_matches_a1_conventions(self):
        y = 0.37
        self.assertAlmostEqual(m.nu_of(m.law_2017)(y), math.sqrt(1 + 1 / y), places=12)
        self.assertAlmostEqual(m.nu_of(m.law_selfconsistent)(y), 0.5 + math.sqrt(0.25 + 1 / y), places=12)


class Horizons(unittest.TestCase):
    def test_particle_horizon_matches_published_theta(self):
        d0 = 2 * m.chi_particle(0)
        self.assertLess(abs(d0 / m.THETA - 1), 0.02)

    def test_readings_bracket_eq9_at_high_z(self):
        rows = {r["z"]: r for r in m.theta_readings()["rows"]}
        self.assertGreater(rows[1.0]["ratio_particle_horizon"], rows[1.0]["ratio_eq9"])
        self.assertLess(rows[1.0]["ratio_hubble"], rows[1.0]["ratio_eq9"])


if __name__ == "__main__":
    unittest.main()
