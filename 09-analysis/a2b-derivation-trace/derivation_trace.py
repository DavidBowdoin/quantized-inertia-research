#!/usr/bin/env python3
"""A2b: trace McCulloch's later derivations of quantised inertia to the galaxy predictions.

Editorial analysis for the Quantized Inertia research archive. Python 3 standard library only.

Three parts, distinguishing reproduction of printed expressions from checks of their derivation:
1. Derivation routes. The printed mass expressions are reproduced and, where linear, written as
   m_i/m (or dm/m) = P * (1 - kappa c^2 / (a Theta)). A separate check reproduces the sign inconsistency
   between the 2016 conservation equation and its printed mass change (first reported by Haug 2018b). Variants test P and kappa;
   fixed kappa does not make galaxy predictions independent of P without an explicit normalisation.
2. Orbit laws. McCulloch's papers turn Eq. 1 into an orbit law in four different ways. Each is checked against
   the equation it claims to solve, then scored on SPARC with A1's loader and likelihood (A1 data required).
3. Theta(z). McCulloch 2017 Eq. 9 against two literal readings of the derivations' "cosmic horizon" in flat
   LambdaCDM. These readings are our editorial extension, not published QI predictions.

Run from the repository root (fetches SPARC into A1's git-ignored data/ if missing):

    python3 -I 09-analysis/a2b-derivation-trace/derivation_trace.py
"""
import argparse
import json
import math
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
A1_DIR = HERE.parent / "a1-sparc-rar-refit"

C = 2.99792458e8            # m/s
HBAR = 1.054571817e-34      # J s
H_PLANCK = 2 * math.pi * HBAR
KB = 1.380649e-23           # J/K
G = 6.67430e-11             # m^3 kg^-1 s^-2
L_P = math.sqrt(HBAR * G / C ** 3)
MPC = 3.0856775814913673e22  # m
THETA = 8.8e26              # McCulloch 2017 onward (present co-moving diameter)
A_Q = 2 * C * C / THETA     # 2.04e-10 m/s^2


def wien_x5():
    """Root of 5(1 - e^-x) = x; McCulloch's beta = 1/x5 (printed as 0.2)."""
    x = 5.0
    for _ in range(50):
        x = 5 * (1 - math.exp(-x))
    return x


BETA = 1 / wien_x5()

# ---------------------------------------------------------------- 1. derivation routes
# Each route returns the printed m_i/m (or dm/m); reproducing it does not validate every preceding step.


def route_2007(a, theta, beta=BETA):
    """MNRAS 376, 338, Eqs. 3-7: F = 1 - lambda_m / (4 Theta), lambda_m = 4 pi^2 beta c^2 / a."""
    lam = 4 * math.pi ** 2 * beta * C * C / a
    return 1 - lam / (4 * theta)


def route_2013(a, theta):
    """EPL 101, 59001, Eq. 8 bracket (1/4Theta - pi a/16c^2), normalised to its large-a limit."""
    return (1 / (4 * theta) - math.pi * a / (16 * C * C)) / (-math.pi * a / (16 * C * C))


def route_2016(a, theta, dx_r=None, dx_h=None, hbar_factor=1.0, photon="wien"):
    """EPL 115, 69001, printed Eqs. 14-20: dm = (hbar/c)(1/dx2 - 1/dx1), dx2 = c^2/a, dx1 = Theta/2,
    then the a in the prefactor is replaced by the Wien-peak photon energy E = hc/lambda_m (Eq. 18).
    Eq. 13 instead implies the opposite sign for dm = m2 - m1; check_2016_conservation audits this."""
    dx_r = C * C / a if dx_r is None else dx_r(a)
    dx_h = theta / 2 if dx_h is None else dx_h(theta)
    de = hbar_factor * HBAR * C * (1 / dx_r - 1 / dx_h)            # energy, J
    if photon == "wien":
        e_photon = H_PLANCK * C / (4 * math.pi ** 2 * BETA * C * C / a)
    else:                                                        # k_B T_Unruh
        e_photon = HBAR * a / (2 * math.pi * C)
    return de / e_photon


def check_2016_conservation(a, theta=THETA):
    """Editorial check of Eq. 13 against printed Eq. 14 (arXiv:1610.06787v1, p. 5).

    Eq. 13: m1 c^2 + U1 = m2 c^2 + U2, so (m2-m1)c^2 = U1-U2.
    Residuals are final minus initial energy, divided by the Wien-peak energy mc^2 used in Eqs. 18-20.
    The printed route is retained separately; this check supplies no replacement physical model.
    """
    u1 = HBAR * C / (theta / 2)
    u2 = HBAR * C / (C * C / a)
    e_photon = H_PLANCK * C / (4 * math.pi ** 2 * BETA * C * C / a)
    dm_eq13 = (u1 - u2) / e_photon
    dm_printed = route_2016(a, theta)
    return dict(a=a, theta=theta, dm_over_m_from_eq13=dm_eq13,
                dm_over_m_printed=dm_printed,
                printed_eq13_residual=(dm_printed * e_photon + u2 - u1) / e_photon,
                rearranged_eq13_residual=(dm_eq13 * e_photon + u2 - u1) / e_photon)


def route_2020_widths(a, theta, half_circumference=(True, True), hbar_factor=0.5, photon="kT"):
    """Adv. Stud. Theor. Phys. 14, 1, Eqs. 2-12: dE = (hbar c/2)(1/dx2 - 1/dx1) with half-circumferences
    pi c^2/a and pi Theta/2, then E_p = k_B T_Unruh and N = mc^2/E_p photons (Eq. 11)."""
    r_rind, r_cos = C * C / a, theta / 2
    dx_r = math.pi * r_rind if half_circumference[0] else r_rind
    dx_h = math.pi * r_cos if half_circumference[1] else r_cos
    de = hbar_factor * HBAR * C * (1 / dx_r - 1 / dx_h)
    if photon == "kT":
        e_p = HBAR * a / (2 * math.pi * C)
    else:                                                        # Wien peak, as in 2016
        e_p = H_PLANCK * C / (4 * math.pi ** 2 * BETA * C * C / a)
    return de / e_p


def route_2017_area(a, theta, linearised=True):
    """MPLA 32, 1750148, Eqs. 2-13: bits on half the Hubble sphere (2 pi R_U^2/l_P^2) and on a Rindler
    hemisphere (2 pi d^2/l_P^2); E = (3/2) N1 kT = mc^2 (Eq. 9). Exact: dm/m = (2/3) ln2 (1 - d^2/R_U^2).
    The paper linearises about d = R_U (a = 2c^2/Theta) and prints dm = (4/3) m (1 - 2c^2/a Theta) ln 2."""
    d, r_u = C * C / a, theta / 2
    n1 = 2 * math.pi * r_u ** 2 / L_P ** 2
    n2 = 2 * math.pi * d ** 2 / L_P ** 2
    if not linearised:
        return (n1 - n2) * math.log(2) / (1.5 * n1)
    x = d / r_u
    return (4 / 3) * math.log(2) * (1 - x)


def route_2020_info(a, theta, log_base=2.0, cosmic_length=None):
    """Adv. Astrophys. 5, 91, Eqs. 2-9: dE = kT (N1 - N2) log_b 2, N1 = Theta/(2 l_P), N2 = c^2/(a l_P);
    kT = mc^2 per bit (Eq. 8), then divide by the object length Theta/(2 l_P) (Eq. 9)."""
    length = theta / 2 if cosmic_length is None else cosmic_length(theta)
    n1, n2 = length / L_P, C * C / (a * L_P)
    m_bit = 1.0                                                  # kT/c^2 in units of m
    big_m = m_bit * (n1 - n2) * math.log(2) / math.log(log_base)
    return big_m / (theta / (2 * L_P))


def fit_p_kappa(f, theta=THETA):
    """Write f(a) = P (1 - kappa c^2/(a theta)); recover P and kappa from two accelerations and report
    the largest relative departure from that form over 2c^2/theta < a < 1e3 m/s^2."""
    a1, a2 = 1e-9, 1e-8
    f1, f2 = f(a1, theta), f(a2, theta)
    u1, u2 = C * C / (a1 * theta), C * C / (a2 * theta)
    kappa = (f2 - f1) / (f2 * u1 - f1 * u2)
    p = f1 / (1 - kappa * u1)
    dev = 0.0
    for e in range(-100, 31):
        a = 10 ** (e / 10)
        if a <= 2.5 * C * C / theta:
            continue
        lin = p * (1 - kappa * C * C / (a * theta))
        dev = max(dev, abs(f(a, theta) - lin) / abs(lin))
    return dict(P=p, kappa=kappa, a_scale=kappa * C * C / theta, max_rel_departure=dev)


ROUTES = [
    # key, source, variant label, function
    ("2007", "McCulloch 2007, MNRAS 376, 338", "as printed (beta from Wien)", route_2007),
    ("2013", "McCulloch 2013, EPL 101, 59001", "Eq. 8 bracket taken literally", route_2013),
    ("2016", "McCulloch 2016, EPL 115, 69001", "printed Eqs. 14–20 (sign conflicts with Eq. 13); hbar, radii, Wien peak",
     lambda a, t: route_2016(a, t)),
    ("2016_kT", "", "2016 with k_B T instead of the Wien-peak photon",
     lambda a, t: route_2016(a, t, photon="kT")),
    ("2016_halfhbar_halfcirc", "", "2016 with hbar/2 and half-circumferences (still Wien peak)",
     lambda a, t: route_2016(a, t, dx_r=lambda a_: math.pi * C * C / a_, dx_h=lambda t_: math.pi * t_ / 2,
                             hbar_factor=0.5)),
    ("2017_area_lin", "McCulloch & Giné 2017, MPLA 32, 1750148", "as printed (linearised near a = 2c²/Θ)",
     lambda a, t: route_2017_area(a, t, True)),
    ("2017_area_exact", "", "same steps without the linearisation: (2/3) ln 2 (1 − (2c²/aΘ)²)", lambda a, t: route_2017_area(a, t, False)),
    ("2020w", "McCulloch & Giné 2020, ASTP 14, 1", "as printed: hbar/2, both half-circumferences, k_B T",
     lambda a, t: route_2020_widths(a, t)),
    ("2020w_radii", "", "radii instead of half-circumferences for both horizons",
     lambda a, t: route_2020_widths(a, t, (False, False))),
    ("2020w_mixed", "", "half-circumference for the Rindler horizon only",
     lambda a, t: route_2020_widths(a, t, (True, False))),
    ("2020w_wien", "", "Wien-peak photon (as 2016) instead of k_B T",
     lambda a, t: route_2020_widths(a, t, photon="wien")),
    ("2020i", "McCulloch 2020, Adv. Astrophys. 5, 91", "as printed: log₂ 2 = 1, cosmic distance Θ/2",
     lambda a, t: route_2020_info(a, t)),
    ("2020i_ln", "", "natural log (Landauer's kT ln 2)", lambda a, t: route_2020_info(a, t, log_base=math.e)),
    ("2020i_diam", "", "count bits to Θ (the diameter) instead of Θ/2",
     lambda a, t: route_2020_info(a, t, cosmic_length=lambda t_: t_)),
]


def routes():
    out = []
    for key, src, label, f in ROUTES:
        r = fit_p_kappa(f)
        out.append(dict(key=key, source=src, variant=label, **r))
    return out

# ---------------------------------------------------------------- 2. orbit laws
# g = GM/r^2 (Newtonian baryonic acceleration), a = predicted acceleration, aq = 2c^2/Theta.


def law_deep(g, aq):
    """a^2 = g a' with a' = aq (2012 Eq. 7; 2017 Eq. 10; 2017 dwarfs Eq. 9; 2024 Proxima Eq. 5)."""
    return math.sqrt(g * aq)


def law_2017(g, aq):
    """McCulloch 2017 Eq. 8: Eq. 6 with |a| on the right replaced by a_bar (Eq. 7)."""
    return math.sqrt(g * g + g * aq)


def law_selfconsistent(g, aq, prefactor=1.0):
    """Eq. 6, a^2 = g(|a| + aq), solved with |a| = a: MOND's 'simple' function with a0 = aq.
    Same algebra as McCulloch & Lucio 2019 (wide binaries) Eqs. 10-13.
    Optional editorial prefactor P retains m_i/m = P(1-aq/(a+aq)) at fixed G and baryonic masses:
    a^2 = (g/P)(a+aq). All SPARC scores use P=1, as in the published mass law."""
    g = g / prefactor
    return g / 2 + math.sqrt(g * g / 4 + g * aq)


def law_additive(g, aq):
    """Eq. 1 with |a| = a and no local component: (1 - aq/a) a = g, so a = g + aq
    (2010 EPL 90, 29001; 2019 Rindler-horizons Eq. 3; 2025 JuMBOs Eq. 6)."""
    return g + aq


LAWS = [
    ("deep", "Deep limit a² = g·a_Q (v⁴ = 2GMc²/Θ)", law_deep,
     "2012 Eqs. 7-9; 2017 SPARC Eqs. 10-13; 2017 dwarfs Eqs. 9-11; 2024 Proxima Eq. 5"),
    ("eq8", "2017 Eq. 8: a = √(g² + g·a_Q)", law_2017, "2017 SPARC Eqs. 7-8 (used in A1, A1b, A6-A6f)"),
    ("selfcons", "Eq. 6 solved exactly: a = g/2 + √(g²/4 + g·a_Q)", law_selfconsistent,
     "algebra of 2019 wide binaries Eqs. 10-13; not applied to galaxies in the sources read"),
    ("additive", "No split: a = g + a_Q", law_additive, "2010 minimum acceleration; 2019 Rindler horizons Eq. 3; 2025 JuMBOs Eq. 6"),
]
LAW = {k[0]: k for k in LAWS}


def law_checks():
    """Each law against the equation it claims to solve, and 2019 Eq. 13 against the self-consistent law."""
    worst = {}
    for e in range(-130, -79):
        g = 10 ** (e / 10)
        a = law_selfconsistent(g, A_Q)
        worst["selfcons_solves_eq6"] = max(worst.get("selfcons_solves_eq6", 0), abs(a * a - g * (a + A_Q)) / (a * a))
        a = law_2017(g, A_Q)
        worst["eq8_solves_eq7"] = max(worst.get("eq8_solves_eq7", 0), abs(a * a - g * (g + A_Q)) / (a * a))
        a = law_additive(g, A_Q)
        worst["additive_solves_eq1"] = max(worst.get("additive_solves_eq1", 0), abs((1 - A_Q / a) * a - g) / g)
    m, out = 1e30, 0.0                                           # McCulloch & Lucio 2019: M = 1e30 kg
    for e in range(130, 181):
        d = 10 ** (e / 10)                                       # separations 1e13 - 1e18 m
        v2 = (G * m / d + math.sqrt((G * m / d) ** 2 + 8 * G * m * C * C / THETA)) / 4
        a_rel = 2 * v2 / d                                       # their a = 2v^2/d
        out = max(out, abs(a_rel - law_selfconsistent(G * m / d ** 2, A_Q)) / a_rel)
    worst["wide_binary_eq13_equals_selfcons"] = out
    return worst


def law_table():
    rows = []
    for lg in (-12, -11.5, -11, -10.5, -10, -9.5, -9, -8.5, -8):
        g = 10 ** lg
        rows.append(dict(log_g=lg, **{k: math.log10(f(g, A_Q)) for k, _, f, _ in LAWS}))
    return rows


def nu_of(law):
    """Interpolating function nu(y), y = g/a_scale, matching A1's convention g_obs = g_bar nu(g_bar/a)."""
    return lambda y: law(y, 1.0) / y


def sparc_scores(boot, seed):
    sys.path.insert(0, str(A1_DIR))
    import rar_refit as a1
    sums = a1.fetch()
    gal = a1.read_galaxies()
    pts, align = a1.label_rar(a1.read_rar(), gal, a1.read_mass_models(gal))
    n = len(pts)
    nus = {k: nu_of(f) for k, _, f, _ in LAWS if k != "deep"}
    nus["rar_ref"] = a1.nu_rar
    la_q = math.log10(A_Q)

    def score(points, key, la=None):
        if la is None:
            la, _ = a1.golden(lambda v: a1.profile(nus[key], v, points)["m2lnl"], -11.0, -8.5, 2e-4)
            k = 2
        else:
            k = 1
        pr = a1.profile(nus[key], la, points)
        return dict(log_a=la, a=10 ** la, theta=2 * C * C / 10 ** la, k=k, m2lnl=pr["m2lnl"],
                    bic=pr["m2lnl"] + k * math.log(len(points)), sig_int=pr["sig_int"],
                    rms=math.sqrt(sum(r * r for r in pr["res"]) / len(points)), res=pr["res"])

    fits = {}
    for key in ("eq8", "selfcons", "additive"):
        fits[key + "_fixed"] = score(pts, key, la_q)
        fits[key + "_free"] = score(pts, key)
    fits["rar_ref_free"] = score(pts, "rar_ref")
    ref = fits["rar_ref_free"]["bic"]
    for f in fits.values():
        f["dbic_vs_rar_ref"] = f["bic"] - ref

    # binned mean residuals (as A1), fixed Theta, for the low/high-acceleration behaviour
    edges = [-12.0 + 0.25 * i for i in range(17)]
    bins = {}
    for key in ("eq8_fixed", "selfcons_fixed", "additive_fixed"):
        rows = []
        for lo, hi in zip(edges, edges[1:]):
            rs = [r for p, r in zip(pts, fits[key]["res"]) if lo <= p["x"] < hi]
            if len(rs) >= 20:
                mu = sum(rs) / len(rs)
                sd = math.sqrt(sum((r - mu) ** 2 for r in rs) / (len(rs) - 1))
                rows.append(dict(lo=lo, hi=hi, n=len(rs), mean=mu, sem=sd / math.sqrt(len(rs))))
        bins[key] = rows

    # Upsilon sensitivity and galaxy bootstrap for the fixed-Theta comparisons (k = 1 each, so dBIC = d(-2lnL))
    ups = {}
    for ud in (0.4, 0.5, 0.6):
        pu = a1.with_upsilon(pts, ud)
        ups[f"{ud:.1f}"] = {k: score(pu, k, la_q)["m2lnl"] for k in ("eq8", "selfcons", "additive")}
    rng = random.Random(seed)
    by = {}
    for p in pts:
        by.setdefault(p["gal"], []).append(p)
    names = sorted(by)
    diffs = []
    for _ in range(boot):
        sample = [p for _ in names for p in by[rng.choice(names)]]
        e8 = a1.profile(nus["eq8"], la_q, sample)["m2lnl"]
        sc = a1.profile(nus["selfcons"], la_q, sample)["m2lnl"]
        diffs.append(sc - e8)
    diffs.sort()
    bs = None
    if diffs:
        q = lambda f: diffs[min(len(diffs) - 1, int(f * len(diffs)))]
        bs = dict(n=len(diffs), p16=q(0.16), p50=q(0.5), p84=q(0.84),
                  frac_selfcons_better=sum(d < 0 for d in diffs) / len(diffs))
    for f in fits.values():
        del f["res"]
    return dict(n_points=n, n_galaxies=len(names), sha256=sums, alignment=align, fits=fits, binned=bins,
                upsilon_m2lnl=ups, bootstrap_selfcons_minus_eq8=bs), a1

# ---------------------------------------------------------------- 3. Theta(z)
# Flat LambdaCDM, Planck 2018 (paper VI, Table 2, TT,TE,EE+lowE+lensing+BAO): H0 = 67.66, Om = 0.3111.
# Radiation: Omega_gamma h^2 = 2.473e-5 with N_eff = 3.046 massless neutrinos (approximation).
H0 = 67.66
OM = 0.3111
OR = 2.473e-5 * (1 + 0.2271 * 3.046) / (H0 / 100) ** 2
OL = 1 - OM - OR
HUBBLE_LEN = C / (H0 * 1e3 / MPC)                                # c/H0, m


def e_of_z(z):
    return math.sqrt(OR * (1 + z) ** 4 + OM * (1 + z) ** 3 + OL)


def chi_particle(z, n=20000):
    """Comoving particle-horizon radius at redshift z: (c/H0) int_0^{1/(1+z)} da / sqrt(Or + Om a + OL a^4)."""
    top = 1 / (1 + z)
    h = top / n
    f = lambda a: 1 / math.sqrt(OR + OM * a + OL * a ** 4)
    s = f(0) + f(top) + sum((4 if i % 2 else 2) * f(i * h) for i in range(1, n))
    return HUBBLE_LEN * s * h / 3


def theta_readings():
    d0 = 2 * chi_particle(0)
    rows = []
    for z in (0.0, 0.5, 0.9, 1.0, 1.5, 2.0, 2.3, 3.0, 4.5):
        r1 = 1 + z                                               # McCulloch 2017 Eq. 9: Theta0/(1+z)
        r2 = d0 / (2 * chi_particle(z) / (1 + z))                # proper particle-horizon diameter at z
        r3 = e_of_z(z)                                           # Hubble diameter 2c/H(z) (2007-2016 definition)
        g = lambda r: math.log(r) / math.log(1 + z) if z > 0 else None
        rows.append(dict(z=z, ratio_eq9=r1, ratio_particle_horizon=r2, ratio_hubble=r3,
                         gamma_particle_horizon=g(r2), gamma_hubble=g(r3)))
    return dict(cosmology=dict(H0=H0, Om=OM, Or=OR, OL=OL),
                particle_horizon_diameter_today_m=d0, hubble_diameter_today_m=2 * HUBBLE_LEN,
                a_q_particle_today=2 * C * C / d0, a_q_hubble_today=C * H0 * 1e3 / MPC, rows=rows)

# ---------------------------------------------------------------- figures and output


def fig_laws(a1, sp, path):
    rows = a1.read_rar_bins()
    p = a1.Plot(840, 590, (-12.3, -8.4), (-12.3, -8.4),
                "One mass formula, four orbit laws (Θ = 8.8 × 10²⁶ m), with public SPARC bins",
                "log₁₀ g_bar  (m s⁻²)", "log₁₀ g_obs  (m s⁻²)")
    p.axes([-12, -11, -10, -9], [-12, -11, -10, -9])
    for b in rows:
        x, y0, y1 = p.X(b["x"]), p.Y(b["y"] - b["sd"]), p.Y(b["y"] + b["sd"])
        p.el.append(f'<path d="M{x:.1f},{y0:.1f} V{y1:.1f}" stroke="var(--pt)" fill="none"/>')
        p.marker(b["x"], b["y"], "var(--pt)", f"Public bin mean ± within-bin SD; n = {b['n']}")
    xs = [-12.3 + i * 0.02 for i in range(196)]
    p.line(xs, xs, "var(--ink2)", "4 4", "Newton")
    style = {"deep": ("var(--s4)", "2 4"), "eq8": ("var(--s2)", None), "selfcons": ("var(--s1)", "8 4"),
             "additive": ("var(--s5)", None)}
    for k, label, f, _ in LAWS:
        xx = [x for x in xs if k != "deep" or x <= -10.0]
        p.line(xx, [math.log10(f(10 ** x, A_Q)) for x in xx], style[k][0], style[k][1], label)
    p.legend([("Public bin mean ± within-bin SD", "var(--pt)", None)] +
             [(lab, style[k][0], style[k][1]) for k, lab, _, _ in LAWS] +
             [("Newton (baryons only)", "var(--ink2)", "4 4")], 330, 420)
    p.save(path)


def fig_theta(a1, th, path):
    rows = th["rows"]
    p = a1.Plot(760, 440, (0, 4.6), (0, 1.2), "Scale growth a_Q(z)/a_Q(0) under three readings of the cosmic horizon",
                "redshift z", "log₁₀ [a_Q(z) / a_Q(0)]")
    p.axes([0, 1, 2, 3, 4], [0, 0.25, 0.5, 0.75, 1.0])
    zs = [i * 0.05 for i in range(93)]
    d0 = th["particle_horizon_diameter_today_m"]
    curves = [("McCulloch 2017 Eq. 9: Θ₀/(1+z)", "var(--s2)", None, lambda z: 1 + z),
              ("Proper particle-horizon diameter at z (editorial)", "var(--s1)", "8 4",
               lambda z: d0 / (2 * chi_particle(z, 4000) / (1 + z))),
              ("Hubble diameter 2c/H(z) (editorial)", "var(--s3)", "3 3", e_of_z)]
    for label, col, dash, f in curves:
        p.line(zs, [math.log10(f(z)) for z in zs], col, dash, label)
    p.legend([(lab, col, dash) for lab, col, dash, _ in curves], 90, 70)
    p.save(path)


def fmt(x, nd=2):
    return f"{x:.{nd}e}".replace("e-", " × 10^-").replace("e+", " × 10^")


def summary(res):
    L = ["# A2b results (generated by derivation_trace.py; do not edit)", ""]
    L += ["## 1. Printed mass expressions: m_i/m (or dm/m) = P (1 − κ c²/(aΘ))", "",
          "Reproducing a printed expression does not validate its derivation. `a_scale` = κc²/Θ at Θ = 8.8 × 10²⁶ m. "
          "`departure` measures the linear form for a > 2.5c²/Θ; extrapolating the 2017 linearisation here does not "
          "extend its physical domain beyond a ≈ 2c²/Θ.", "",
          "| Route | Variant | P | κ | a_scale (m s⁻²) | departure |", "|---|---|---|---|---|---|"]
    for r in res["routes"]:
        if r["max_rel_departure"] > 1e-6:                            # not of the linear form: P, kappa meaningless
            L.append(f"| {r['source'] or '↳'} | {r['variant']} | — | — | — | {r['max_rel_departure']:.1e} |")
            continue
        L.append(f"| {r['source'] or '↳'} | {r['variant']} | {r['P']:.4f} | {r['kappa']:.4f} | "
                 f"{r['a_scale']:.3e} | {r['max_rel_departure']:.1e} |")
    L += ["", f"β = 1/x₅ = {BETA:.5f}; βπ² = {BETA * math.pi ** 2:.4f}; 2πβ = {2 * math.pi * BETA:.4f}; 4/π = {4 / math.pi:.4f}.", ""]
    ch = res["conservation_2016"]
    L += ["### Editorial check: the 2016 sign inconsistency", "",
          "Eq. 13 implies dm = (ħ/c)(1/Δx₁ − 1/Δx₂), for dm = m₂ − m₁. Printed Eq. 14 reverses that sign. "
          "The route table retains Eqs. 14–20 as printed; it is not a verification of Eq. 13 → Eq. 14.", "",
          f"At a = 2a_Q = {ch['a']:.3e} m s⁻², using the paper's Wien-peak energy mc²:", "",
          f"- dm/m from Eq. 13: {ch['dm_over_m_from_eq13']:+.6f}.",
          f"- dm/m from printed Eqs. 14–20: {ch['dm_over_m_printed']:+.6f}.",
          f"- Eq. 13 energy residual (final − initial)/mc² with the printed mass change: {ch['printed_eq13_residual']:+.6f}.",
          f"- Residual using Eq. 13's own rearrangement: {ch['rearranged_eq13_residual']:.1e}.", "",
          "First reported by Haug (2018b, viXra:1803.0052), who writes that McCulloch confirmed privately that Eq. 13 "
          "should carry minus signs; Eq. 14 then follows. Haug argues the corrected relation is no longer conservation of "
          "mass-energy plus uncertainty energy. This check reproduces the inconsistency; it does not select a revised QI model.", "",
          "### Normalisation and galaxy predictions", "",
          "The listed normalisation variants leave κ = 2, but retain P ≠ 1. At fixed G and baryonic masses, "
          "the split-acceleration equation becomes a² = (g/P)(a+a_Q), so P changes the prediction. "
          "Dividing the mass law by its high-acceleration limit P can remove it only as an explicit normalisation "
          "with a consistent mass/G calibration. All orbit-law scores below use the published P = 1; they do not "
          "test every derivation prefactor.", ""]
    L += ["## 2. Orbit laws (P = 1)", "", "Identity checks (max relative error):", ""]
    for k, v in res["law_checks"].items():
        L.append(f"- `{k}`: {v:.1e}")
    L += ["", "log₁₀ a predicted at log₁₀ g (Θ = 8.8 × 10²⁶ m, a_Q = " + f"{A_Q:.3e} m s⁻²):", "",
          "| log₁₀ g | " + " | ".join(lab for _, lab, _, _ in LAWS) + " |", "|---" * (len(LAWS) + 1) + "|"]
    for r in res["law_table"]:
        L.append(f"| {r['log_g']} | " + " | ".join(f"{r[k]:.3f}" for k, _, _, _ in LAWS) + " |")
    sp = res.get("sparc")
    if sp:
        L += ["", f"### SPARC RAR ({sp['n_points']:,} points, {sp['n_galaxies']} galaxies; A1 loader and likelihood, Υ_disk = 0.5)", "",
              "| Law | Θ | a (m s⁻²) | Θ equiv. (m) | σ_int (dex) | rms (dex) | ΔBIC vs McGaugh fit (a₀ free) |",
              "|---|---|---|---|---|---|---|"]
        names = {"eq8": "2017 Eq. 8", "selfcons": "Eq. 6 exact (MOND simple)", "additive": "a = g + a_Q", "rar_ref": "McGaugh 2016 fit"}
        for k, f in sp["fits"].items():
            base, kind = k.rsplit("_", 1)
            L.append(f"| {names[base]} | {'8.8 × 10²⁶ (fixed)' if kind == 'fixed' else 'free'} | {f['a']:.3e} | "
                     f"{f['theta']:.3e} | {f['sig_int']:.3f} | {f['rms']:.3f} | {f['dbic_vs_rar_ref']:+.0f} |")
        L += ["", "Mean residual (data − law) by log g_bar bin, fixed Θ, dex (± standard error of the mean):", "",
              "| bin | n | 2017 Eq. 8 | Eq. 6 exact | a = g + a_Q |", "|---|---|---|---|---|"]
        b8, bs, ba = sp["binned"]["eq8_fixed"], sp["binned"]["selfcons_fixed"], sp["binned"]["additive_fixed"]
        for x, y, w in zip(b8, bs, ba):
            L.append(f"| {x['lo']:.2f} to {x['hi']:.2f} | {x['n']} | {x['mean']:+.3f} ± {x['sem']:.3f} | "
                     f"{y['mean']:+.3f} ± {y['sem']:.3f} | {w['mean']:+.3f} ± {w['sem']:.3f} |")
        L += ["", "−2 ln L at fixed Θ by Υ_disk (Υ_bul = 1.4 Υ_disk); each law has k = 1, so differences are ΔBIC:", "",
              "| Υ_disk | Eq. 6 exact − Eq. 8 | additive − Eq. 8 |", "|---|---|---|"]
        for u, v in sp["upsilon_m2lnl"].items():
            L.append(f"| {u} | {v['selfcons'] - v['eq8']:+.0f} | {v['additive'] - v['eq8']:+.0f} |")
        bs = sp["bootstrap_selfcons_minus_eq8"]
        if bs:
            L += ["", f"Galaxy bootstrap ({bs['n']} resamples) of Eq. 6 exact − Eq. 8 at fixed Θ: median {bs['p50']:+.0f}, "
                  f"16–84% {bs['p16']:+.0f} to {bs['p84']:+.0f}; Eq. 6 exact better in {bs['frac_selfcons_better']:.0%}."]
    th = res["theta_z"]
    L += ["", "## 3. Θ(z) readings (editorial extension)", "",
          f"Flat ΛCDM, H₀ = {H0}, Ω_m = {OM}, Ω_r = {OR:.2e}. Proper particle-horizon diameter today "
          f"{th['particle_horizon_diameter_today_m']:.3e} m (McCulloch: 8.8 × 10²⁶ m); "
          f"Hubble diameter 2c/H₀ = {th['hubble_diameter_today_m']:.3e} m.", "",
          "| z | Eq. 9: 1+z | particle horizon | γ | Hubble 2c/H(z) | γ |", "|---|---|---|---|---|---|"]
    for r in th["rows"]:
        gp = "—" if r["gamma_particle_horizon"] is None else f"{r['gamma_particle_horizon']:.2f}"
        gh = "—" if r["gamma_hubble"] is None else f"{r['gamma_hubble']:.2f}"
        L.append(f"| {r['z']} | {r['ratio_eq9']:.2f} | {r['ratio_particle_horizon']:.2f} | {gp} | {r['ratio_hubble']:.2f} | {gh} |")
    L += ["", "γ is the equivalent exponent in a_Q ∝ (1+z)^γ at that redshift (Eq. 9 is γ = 1).", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=200, help="galaxy bootstrap replicates for the fixed-Θ comparison")
    ap.add_argument("--seed", type=int, default=20261024)
    ap.add_argument("--no-sparc", action="store_true", help="skip the SPARC scoring (no download)")
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    res = dict(constants=dict(beta=BETA, theta=THETA, a_q=A_Q, l_planck=L_P),
               routes=routes(), conservation_2016=check_2016_conservation(2 * A_Q),
               law_checks=law_checks(), law_table=law_table(),
               laws={k: dict(label=lab, used_in=u) for k, lab, _, u in LAWS}, theta_z=theta_readings())
    a1 = None
    if not args.no_sparc:
        res["sparc"], a1 = sparc_scores(args.boot, args.seed)
        fig_laws(a1, res["sparc"], OUT / "fig-1-orbit-laws.svg")
        fig_theta(a1, res["theta_z"], OUT / "fig-2-theta-z.svg")
    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    (OUT / "summary.md").write_text(summary(res))
    print(summary(res))


if __name__ == "__main__":
    main()
