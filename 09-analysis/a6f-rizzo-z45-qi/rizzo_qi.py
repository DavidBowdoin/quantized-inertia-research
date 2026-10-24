"""A6f: QI's scale at z ~ 4.2-4.8 from six ALMA discs (Rizzo et al. 2020, 2021).

Editorial analysis for the Quantized Inertia research archive. Requires numpy and scipy (09-analysis/requirements.txt).

At z = 4.5 McCulloch's 2017 law predicts a_Q = 2c^2(1+z)/Theta_0 = 5.5 times its present value, a change of
0.74 dex: larger than typical baryonic-mass systematics. Rizzo et al. decompose [CII] rotation curves of five lensed
dusty star-forming galaxies (2021, MNRAS 507, 3952) and SPT0418-47 (2020, Nature 584, 201) into a spherical
deprojected Sersic stellar component, an exponential gas disc and an NFW halo. From their posteriors we rebuild
g_bar and g_obs at the outermost measured radius and invert McCulloch 2017 Eq. 8:
    g_obs^2 = g_bar^2 + a g_bar   =>   a = g_bar ((g_obs/g_bar)^2 - 1).

Parameters are typed from the papers (see PARAMS). The outermost radii were read from the rotation-curve figures by
Sentina 2026 (Zenodo 10.5281/zenodo.23442383); they are approximate and varied by +-15% below.

Run:  .venv/bin/python -I 09-analysis/a6f-rizzo-z45-qi/rizzo_qi.py [--draws 20000]
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import gammainc, gammaincinv, i0, i1, k0, k1

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
G = 4.30091e-6
KK = 1e6 / 3.0856775814913673e19
C = 2.99792458e8
THETA0 = 8.8e26
H0, OM, OL = 67.8, 0.308, 0.691    # Rizzo et al. 2021 cosmology (Planck 2015)

# name, z, then (value, +err, -err) for M_star [1e10], R_e [kpc], n, M_gas [1e10], M_DM [1e11];
# R_gas [kpc], concentration c, R_out [kpc].
# Rizzo 2021 Tables 4, 5, C1 (arXiv:2102.05671); SPT0418-47 from Rizzo 2020 Extended Data Table 5 and Methods
# (arXiv:2009.01251). R_out read from Rizzo 2021 Fig. 4 / Rizzo 2020 Fig. 2c by Sentina 2026.
PARAMS = [
    ("SPT0113-46", 4.23, (6.0, 2.0, 1.0), (1.4, 0.6, 0.5), (6.0, 0.5, 0.6), (4.3, 1.0, 0.9), (12, 6, 6), 1.5, 3.04, 3.4),
    ("SPT0345-47", 4.29, (2.3, 0.4, 0.3), (0.30, 0.06, 0.04), (1.5, 0.5, 0.3), (1.7, 0.4, 0.4), (2, 2, 1), 0.76, 2.97, 3.1),
    ("SPT0441-46", 4.48, (1.8, 0.2, 0.2), (0.11, 0.02, 0.02), (2.0, 0.9, 0.6), (1.4, 0.2, 0.2), (72, 8, 8), 0.63, 2.77, 2.05),
    ("SPT2146-55", 4.57, (1.0, 0.2, 0.1), (0.39, 0.08, 0.05), (1.6, 0.3, 0.2), (1.2, 0.3, 0.2), (1.2, 0.5, 0.5), 1.4, 2.67, 2.75),
    ("SPT2132-58", 4.77, (1.9, 0.3, 0.3), (1.4, 0.1, 0.1), (0.94, 0.05, 0.04), (1.9, 0.3, 0.3), (0.32, 0.23, 0.09), 2.1, 2.45, 4.15),
    ("SPT0418-47", 4.225, (1.2, 0.2, 0.1), (0.22, 0.04, 0.02), (2.2, 0.3, 0.2), (1.3, 0.2, 0.2), (17, 3, 3), 0.9, 3.06, 3.6),
]
# Rizzo 2021 Sect. 4: baryon-to-total mass ratio at the outermost radius, quoted for two galaxies.
RIZZO_FBAR = {"SPT0441-46": (0.66, 0.02), "SPT0345-47": (0.90, 0.03)}


def E(z):
    return math.sqrt(OM * (1 + z) ** 3 + OL)


def delta_vir(z, kind):
    if kind == "200c":
        return 200.0
    x = OM * (1 + z) ** 3 / E(z) ** 2 - 1
    return 18 * math.pi ** 2 + 82 * x - 39 * x * x


def r_vir(M, z, kind):
    rho_c = 3 * (H0 * 1e-3 * E(z)) ** 2 / (8 * math.pi * G)       # Msun / kpc^3 with H in km/s/kpc
    return (3 * M / (4 * math.pi * delta_vir(z, kind) * rho_c)) ** (1 / 3)


def v2_star(r, M, Re, n):
    """Deprojected spherical Sersic (Lima Neto et al. 1999; Terzic & Graham 2005): enclosed mass."""
    b = gammaincinv(2 * n, 0.5)
    p = 1 - 0.6097 / n + 0.05463 / n ** 2
    return G * M * gammainc(n * (3 - p), b * (r / Re) ** (1 / n)) / r


def v2_gas(r, M, Rd):
    y = r / (2 * Rd)
    return 4 * math.pi * G * (M / (2 * math.pi * Rd ** 2)) * Rd * y ** 2 * (i0(y) * k0(y) - i1(y) * k1(y))


def v2_dm(r, M, c, z, kind):
    R = r_vir(M, z, kind)
    x = r / R
    m = lambda u: np.log(1 + u) - u / (1 + u)
    return G * M / R * m(c * x) / (x * m(c))


def split_normal(rng, v, up, lo, n):
    s = rng.standard_normal(n)
    return np.where(s >= 0, v + s * up, v + s * lo)


def evaluate(par, rng, n, kind="bryan_norman", rout_scale=1.0):
    name, z, ms, re_, nn, mg, mdm, rg, c, rout = par
    r = rout * rout_scale
    Ms = np.clip(split_normal(rng, *ms, n), 1e-3, None) * 1e10
    Re = np.clip(split_normal(rng, *re_, n), 1e-3, None)
    N = np.clip(split_normal(rng, *nn, n), 0.5, 10)
    Mg = np.clip(split_normal(rng, *mg, n), 1e-3, None) * 1e10
    Md = np.clip(split_normal(rng, *mdm, n), 1e-3, None) * 1e11
    vb = v2_star(r, Ms, Re, N) + v2_gas(r, Mg, rg)
    vt = vb + v2_dm(r, Md, c, z, kind)
    gbar, gobs = vb / r * KK, vt / r * KK
    a = gbar * ((gobs / gbar) ** 2 - 1)
    pub = 2 * C * C * (1 + z) / THETA0
    q = lambda arr: [float(np.percentile(arr, v)) for v in (16, 50, 84)]
    return dict(name=name, z=z, r_out=r, a_q_16_50_84=q(a), ratio_to_published_16_50_84=q(a / pub),
                log_ratio_median=float(np.median(np.log10(a / pub))), log_ratio_sigma=float(np.std(np.log10(a / pub))),
                fbar_16_50_84=q(gbar / gobs), gbar_median=float(np.median(gbar)), published=pub,
                ratio_to_constant_today_16_50_84=q(a / (2 * C * C / THETA0)))


def combine(rows):
    """Random-effects mean of log10(a/published): x_i ~ N(m, s_i^2 + tau^2), maximum likelihood for m and tau.

    QI predicts one scale at a given redshift, so tau > 0 beyond the measurement errors is itself informative.
    An inverse-variance mean without tau would be dominated by the most precise galaxy.
    """
    x = np.array([r["log_ratio_median"] for r in rows])
    s = np.array([r["log_ratio_sigma"] for r in rows])
    best = None
    for tau in np.linspace(0, 1.5, 3001):
        w = 1 / (s ** 2 + tau ** 2)
        m = float(np.sum(w * x) / np.sum(w))
        ll = -0.5 * float(np.sum((x - m) ** 2 * w - np.log(w)))
        if best is None or ll > best[0]:
            best = (ll, m, tau, float(1 / math.sqrt(np.sum(w))))
    ll, m, tau, err = best
    w0 = 1 / s ** 2
    m0 = float(np.sum(w0 * x) / np.sum(w0))
    chi2_single = float(np.sum((x - m0) ** 2 * w0))
    return dict(mean_log_ratio=m, mean_ratio=10 ** m, error=err, tau_dex=tau, median_ratio=float(10 ** np.median(x)),
                chi2_single_scale=chi2_single, dof=len(x) - 1, n=len(rows),
                mean_ratio_to_qi_today=float(10 ** m * np.mean([1 + r["z"] for r in rows])))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=20261023)
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    res = dict(theta0_m=THETA0, cosmology=dict(H0=H0, Om=OM, OL=OL), variants={})
    for vname, kw in (("main", {}), ("delta_200c", dict(kind="200c")),
                      ("r_out_minus_15pct", dict(rout_scale=0.85)), ("r_out_plus_15pct", dict(rout_scale=1.15))):
        rng = np.random.default_rng(args.seed)
        rows = [evaluate(p, rng, args.draws, **kw) for p in PARAMS]
        res["variants"][vname] = dict(galaxies=rows, combined=combine(rows))
    res["rizzo_fbar_check"] = {k: dict(rizzo=v, ours=next(r["fbar_16_50_84"] for r in res["variants"]["main"]["galaxies"] if r["name"] == k))
                               for k, v in RIZZO_FBAR.items()}
    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False, allow_nan=False) + "\n")
    L = ["# A6f results (generated by rizzo_qi.py; do not edit)", "",
         "Editorial analysis. Parameter posteriors are sampled independently as split normals; their correlations are not published. "
         "Outermost radii are read from figures.", "",
         "## Main (Bryan–Norman virial overdensity)", "",
         "| Galaxy | z | R_out (kpc) | g_bar/g_obs (16/50/84) | a_Q (10⁻¹⁰ m s⁻², 16/50/84) | published 2c²(1+z)/Θ₀ | a_Q ÷ published (16/50/84) |",
         "|---|---|---|---|---|---|---|"]
    for r in res["variants"]["main"]["galaxies"]:
        L.append(f"| {r['name']} | {r['z']} | {r['r_out']:.2f} | " + " / ".join(f"{x:.2f}" for x in r["fbar_16_50_84"]) + " | " +
                 " / ".join(f"{x * 1e10:.2f}" for x in r["a_q_16_50_84"]) + f" | {r['published'] * 1e10:.2f} | " +
                 " / ".join(f"{x:.2f}" for x in r["ratio_to_published_16_50_84"]) + " |")
    L += ["", "Check against Rizzo 2021's quoted baryon-to-total ratios at the outermost radius: " +
          "; ".join(f"{k}: Rizzo {v['rizzo'][0]:.2f} ± {v['rizzo'][1]:.2f}, ours {v['ours'][1]:.2f}" for k, v in res["rizzo_fbar_check"].items()) + ".", "",
          "## Combined ratio a_Q ÷ published, by variant", "",
          "Random-effects mean of log(a_Q ÷ published) with fitted intrinsic scatter τ. χ² tests whether one common scale fits all six.", "",
          "| Variant | mean ratio (log ± error) | τ (dex) | median | χ² for one common scale / dof | mean ratio to QI's z = 0 scale |", "|---|---|---|---|---|---|"]
    for vname, v in res["variants"].items():
        cmb = v["combined"]
        L.append(f"| {vname} | {cmb['mean_ratio']:.2f} (log {cmb['mean_log_ratio']:+.2f} ± {cmb['error']:.2f}) | {cmb['tau_dex']:.2f} | "
                 f"{cmb['median_ratio']:.2f} | {cmb['chi2_single_scale']:.0f} / {cmb['dof']} | {cmb['mean_ratio_to_qi_today']:.2f} |")
    (OUT / "summary.md").write_text("\n".join(L) + "\n")
    print((OUT / "summary.md").read_text())


if __name__ == "__main__":
    main()
