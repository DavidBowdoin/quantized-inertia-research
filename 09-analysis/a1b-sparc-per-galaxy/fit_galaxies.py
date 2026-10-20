#!/usr/bin/env python3
"""A1b: per-galaxy SPARC rotation-curve fits, QI vs MOND, with nuisance parameters.

Needs numpy + scipy (see ../requirements.txt). Run from the repository root:

    uv venv --python 3.13 .venv && uv pip install --python .venv/bin/python -r 09-analysis/requirements.txt
    .venv/bin/python -I 09-analysis/a1b-sparc-per-galaxy/fit_galaxies.py

Each galaxy's rotation curve is fitted with its own disk and bulge mass-to-light ratios,
distance and inclination (all with priors, as in Li et al. 2018), while the acceleration
scale a (QI: a = 2c^2/Theta) is shared by every galaxy. For each model and each value of
log10 a on a grid, every galaxy's best chi^2 + prior penalty is stored; the global profile
is their sum, and a galaxy bootstrap resamples those per-galaxy profiles.
The score Q = chi^2 + prior penalty is descriptive, not BIC or a Bayes factor.
A second full fit enlarges velocity errors while keeping all priors unchanged.
Reuses the SPARC download and parsers of ../a1-sparc-rar-refit/rar_refit.py.
"""
import argparse
import json
import math
import multiprocessing as mp
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "a1-sparc-rar-refit"))
import rar_refit as A1  # noqa: E402

OUT = HERE / "results"
KPC = A1.KPC
C = A1.C

# priors (Li et al. 2018 style): log-normal 0.1 dex on Y_disk (0.5) and Y_bul (0.7);
# Gaussian on distance and inclination with the SPARC Table 1 errors
UD0, UB0, SIG_LOGU = 0.5, 0.7, 0.1

NU = {
    "qi": lambda y: np.sqrt(1.0 + 1.0 / y),
    "mond_simple": lambda y: 0.5 + np.sqrt(0.25 + 1.0 / y),
    "mond_standard": lambda y: np.sqrt(0.5 + np.sqrt(0.25 + 1.0 / y ** 2)),
    "rar_exp": lambda y: 1.0 / (1.0 - np.exp(-np.sqrt(y))),
}
LABEL = {
    "qi": "QI (a = 2c²/Θ)",
    "mond_simple": "MOND simple μ",
    "mond_standard": "MOND standard μ",
    "rar_exp": "McGaugh 2016 RAR fit",
}
LA_EARLY = math.log10(A1.theta_to_a(A1.THETA_EARLY))
LA_LATE = math.log10(A1.theta_to_a(A1.THETA_LATE))
GRID = np.round(np.arange(-11.0, -8.499, 0.01), 3)   # log10 a: 1e-11 .. 3.2e-9
GRID_QI = np.unique(np.concatenate([GRID, [LA_LATE, LA_EARLY]]))   # plus the two fixed-Θ values
KEYS = ["qi_early", "qi_late", "qi", "mond_simple", "mond_standard", "rar_exp"]
DISTANCE_METHODS = {1: "Hubble flow", 2: "TRGB", 3: "Cepheids", 4: "Ursa Major cluster", 5: "Supernovae"}


def galaxies():
    A1.fetch()
    gal = A1.read_galaxies()
    for line in (A1.DATA / "SPARC_Lelli2016c.mrt").read_text().splitlines():
        p = line.split()
        if len(line) > 100 and len(p) >= 18 and p[1].isdigit() and p[0] in gal:
            gal[p[0]].update(eD=float(p[3]), distance_method=int(p[4]), einc=float(p[6]))
    rows = A1.read_mass_models(gal)
    out = []
    for name in sorted(gal):
        g = gal[name]
        if g["Q"] == 3 or g["inc"] < 30:
            continue
        rs = [r for r in rows if r["gal"] == name and r["V"] > 0 and r["eV"] > 0 and r["R"] > 0]
        if len(rs) < 3:
            continue
        arr = {k: np.array([r[k] for r in rs]) for k in ("R", "V", "eV", "Vg", "Vd", "Vb")}
        out.append(dict(name=name, D0=g["D"], eD=max(g["eD"], 0.01 * g["D"]), i0=g["inc"], ei=max(g["einc"], 1.0),
                        distance_method=g["distance_method"], bulge=bool(np.any(arr["Vb"] > 0)), **arr))
    return out


def unpack(g, p):
    """params -> (Y_disk, Y_bul, D, inc)."""
    if g["bulge"]:
        lud, lub, D, inc = p
    else:
        (lud, D, inc), lub = p, math.log10(UB0)
    return 10 ** lud, 10 ** lub, D, inc


def objective_terms(p, g, nu, la):
    """Separate velocity misfit from priors so error sensitivity never rescales priors."""
    ud, ub, D, inc = unpack(g, p)
    if D <= 0 or not (1.0 < inc < 90.0):
        return 1e12, 0.0
    f = D / g["D0"]
    s = math.sin(math.radians(g["i0"])) / math.sin(math.radians(inc))
    R = g["R"] * f
    V, eV = g["V"] * s, g["eV"] * s
    vb2 = (np.abs(g["Vg"]) * g["Vg"] + ud * np.abs(g["Vd"]) * g["Vd"] + ub * np.abs(g["Vb"]) * g["Vb"]) * f  # km^2/s^2
    gbar = np.maximum(vb2, 1e-6) * 1e6 / (R * KPC)
    gpred = gbar * nu(gbar / 10 ** la)
    vpred = np.sqrt(gpred * R * KPC) / 1e3
    chi2 = float(np.sum(((V - vpred) / eV) ** 2))
    pen = ((math.log10(ud) - math.log10(UD0)) / SIG_LOGU) ** 2 + ((D - g["D0"]) / g["eD"]) ** 2 \
        + ((inc - g["i0"]) / g["ei"]) ** 2
    if g["bulge"]:
        pen += ((math.log10(ub) - math.log10(UB0)) / SIG_LOGU) ** 2
    return chi2, pen


def objective(p, g, nu, la):
    return sum(objective_terms(p, g, nu, la))


def with_velocity_errors(gals, factor):
    """Copy each galaxy with enlarged velocity errors; retain all other inputs."""
    if not math.isfinite(factor) or factor <= 0:
        raise ValueError("velocity error factor must be finite and positive")
    return [dict(g, eV=g["eV"] * factor) for g in gals]


def distance_summary(rows):
    """Report both fractional distance shifts and shifts in catalogue-error units."""
    return dict(n=len(rows), median_D_ratio=float(np.median([r["D_ratio"] for r in rows])),
                median_pull_D=float(np.median([r["pull_D"] for r in rows])),
                n_D_ratio_lt_0p8=int(sum(r["D_ratio"] < 0.8 for r in rows)),
                n_pull_D_lt_minus2=int(sum(r["pull_D"] < -2 for r in rows)),
                n_pull_D_lt_minus3=int(sum(r["pull_D"] < -3 for r in rows)))


def fit_one(g, nu, la, x0):
    lo_D = max(0.1 * g["D0"], g["D0"] - 5 * g["eD"])
    bnds = ([(-1.5, 0.7)] + ([(-1.5, 0.7)] if g["bulge"] else []) +
            [(lo_D, g["D0"] + 5 * g["eD"]), (max(1.5, g["i0"] - 5 * g["ei"]), min(89.5, g["i0"] + 5 * g["ei"]))])
    start = x0 if x0 is not None else [math.log10(UD0)] + ([math.log10(UB0)] if g["bulge"] else []) + [g["D0"], g["i0"]]
    return minimize(objective, start, args=(g, nu, la), method="L-BFGS-B", bounds=bnds)


def profile_galaxy(args):
    g, model, grid = args
    nu = NU[model]
    order = np.argsort(np.abs(grid - (-9.95)))  # start near the expected optimum, warm-start outwards
    vals, pars = np.empty(len(grid)), [None] * len(grid)
    x_prev = {}
    for idx in order:
        la = grid[idx]
        near = min(x_prev, key=lambda k: abs(k - la)) if x_prev else None
        r = fit_one(g, nu, la, x_prev.get(near))
        vals[idx], pars[idx] = r.fun, list(map(float, r.x))
        x_prev[la] = r.x
    return g["name"], model, vals.tolist(), pars


COLOR = {"qi_early": "var(--s1)", "qi_late": "var(--s2)", "qi": "var(--s3)", "mond_simple": "var(--s4)",
         "mond_standard": "var(--s5)", "rar_exp": "var(--s7)"}


def figures(fits, grids, total, diag, best_la_gal):
    # 1. global profile of chi^2 + priors against the shared acceleration scale
    lo = min(float(total(m).min()) for m in NU)
    top = math.ceil(math.log10(1 + max(float(total(m).max()) - lo for m in NU)))
    p = A1.Plot(760, 420, (-10.5, -8.9), (0, top), "Per-galaxy fits: total misfit against the shared acceleration scale",
                "log₁₀ a  (m s⁻²);  for QI, Θ = 2c²/a", "Δ(χ² + priors) from the best model")
    p.axes([-10.5, -10.25, -10.0, -9.75, -9.5, -9.25, -9.0], [])
    for dv in [0] + [10 ** i for i in range(top)]:
        y = p.Y(math.log10(1 + dv))
        p.el.append(f'<line class="gr" x1="{p.l}" x2="{p.r}" y1="{y:.1f}" y2="{y:.1f}"/>'
                    f'<text x="{p.l - 6}" y="{y + 4:.1f}" text-anchor="end">{dv:,}</text>')
    for m in ("qi", "mond_simple", "mond_standard", "rar_exp"):
        keep = np.isin(grids[m], GRID) & (grids[m] >= -10.5) & (grids[m] <= -8.9)
        t = total(m)[keep] - lo
        p.line(grids[m][keep].tolist(), np.log10(1 + t).tolist(), COLOR[m], tip=LABEL[m])
    for k in ("qi_late", "qi_early"):
        dv = fits[k]["chi2p"] - lo
        p.marker(fits[k]["log_a"], math.log10(1 + dv), COLOR[k], f"{fits[k]['label']}: Δ = {dv:,.0f}")
        p.text(p.X(fits[k]["log_a"]) - 10, p.Y(math.log10(1 + dv)) - 10, fits[k]["label"].replace(" (fixed)", ""), "end")
    p.legend([(LABEL[m], COLOR[m], None) for m in ("qi", "mond_simple", "mond_standard", "rar_exp")], 90, 70)
    p.save(OUT / "fig-1-global-profile.svg")

    # 2. distance shifts the fits need: cumulative distribution of D / D_catalogue
    p = A1.Plot(760, 420, (0.3, 1.7), (0, 1), "How far each fit moves galaxy distances",
                "fitted distance ÷ catalogue distance", "fraction of galaxies (cumulative)")
    p.axes([0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6], [0, 0.25, 0.5, 0.75, 1.0])
    for k in ("qi_early", "qi_late", "qi", "mond_simple"):
        d = sorted(min(1.7, max(0.3, r["D_ratio"])) for r in diag[k])
        xs, ys = [0.3], [0.0]
        for j, v in enumerate(d):
            xs += [v, v]
            ys += [j / len(d), (j + 1) / len(d)]
        xs.append(1.7)
        ys.append(1.0)
        p.line(xs, ys, COLOR[k], tip=fits[k]["label"] + f": median {np.median([r['D_ratio'] for r in diag[k]]):.2f}")
    p.legend([(fits[k]["label"], COLOR[k], None) for k in ("qi_early", "qi_late", "qi", "mond_simple")], 430, 300)
    p.save(OUT / "fig-2-distance-shift.svg")

    # 3. per-galaxy preferred Theta (QI fitted to each galaxy alone)
    lt = np.log10(2 * C * C / 10 ** np.array(list(best_la_gal.values())))
    edges = np.arange(25.45, 28.25, 0.1)
    h, _ = np.histogram(np.clip(lt, edges[0] + 1e-6, edges[-1] - 1e-6), edges)
    ymax = int(math.ceil(h.max() / 5.0) * 5)
    p = A1.Plot(760, 400, (edges[0], edges[-1]), (0, ymax), "QI fitted to each galaxy alone: preferred Θ",
                "log₁₀ Θ  (m)", "number of galaxies")
    p.axes([25.5, 26.0, 26.5, 27.0, 27.5, 28.0], list(range(0, ymax + 1, 5)))
    for lo_e, hi_e, c in zip(edges, edges[1:], h):
        if c:
            x0, x1 = p.X(lo_e) + 1, p.X(hi_e) - 1
            p.el.append(f'<rect x="{x0:.1f}" y="{p.Y(c):.1f}" width="{x1 - x0:.1f}" height="{p.Y(0) - p.Y(c):.1f}" rx="2" '
                        f'fill="var(--s3)"><title>log Θ {lo_e:.2f}–{hi_e:.2f}: {c} galaxies</title></rect>')
    for th, lab, k in ((A1.THETA_EARLY, "2.6 × 10²⁶ m", "qi_early"), (A1.THETA_LATE, "8.8 × 10²⁶ m", "qi_late"),
                       (fits["qi"]["theta_equiv_m"], f"global best {fits['qi']['theta_equiv_m'] / 1e27:.2f} × 10²⁷ m", "qi")):
        x = p.X(math.log10(th))
        p.el.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{p.t}" y2="{p.b}" stroke="{COLOR[k]}" stroke-width="2" stroke-dasharray="5 4"/>')
        p.text(x - 4 if k == "qi_late" else x + 4, p.t + 14 + 18 * (k == "qi_late"), lab, "end" if k == "qi_late" else "start")
    p.save(OUT / "fig-3-theta-per-galaxy.svg")


def profile_minimum(grid, values):
    """Refine on the regular grid, retaining any better exact fixed-scale point."""
    regular = np.isin(grid, GRID)
    xs, ys = grid[regular], values[regular]
    i = int(np.argmin(ys))
    la, val = float(xs[i]), float(ys[i])
    if 0 < i < len(xs) - 1:
        y0, y1, y2 = ys[i - 1:i + 2]
        den = y0 - 2 * y1 + y2
        dx = 0.5 * (y0 - y2) / den if den > 0 else 0.0
        la += float(dx * (xs[i] - xs[i - 1]))
        val = float(y1 - 0.25 * (y0 - y2) * dx)
    j = int(np.argmin(values))
    if values[j] < val:
        la, val = float(grid[j]), float(values[j])
    return la, val


def run_analysis(gals, boot, seed, procs, make_figures=False):
    npts = int(sum(len(g["R"]) for g in gals))
    grids = {m: (GRID_QI if m == "qi" else GRID) for m in NU}
    jobs = [(g, m, grids[m]) for m in NU for g in gals]
    prof = {m: {} for m in NU}
    pars = {m: {} for m in NU}
    with mp.Pool(procs) as pool:
        for i, (name, m, vals, ps) in enumerate(pool.imap_unordered(profile_galaxy, jobs, chunksize=2), 1):
            prof[m][name], pars[m][name] = np.array(vals), ps
            if i % 100 == 0:
                print(f"  {i}/{len(jobs)} galaxy profiles", flush=True)
    names = [g["name"] for g in gals]
    G = {g["name"]: g for g in gals}

    def total(m, sel=None):
        return np.sum([prof[m][n] for n in (names if sel is None else sel)], axis=0)

    def best(m, sel=None):
        return profile_minimum(grids[m], total(m, sel))

    def at(m, la, sel=None):
        return float(total(m, sel)[int(np.argmin(np.abs(grids[m] - la)))])

    fits = {}
    for m in NU:
        la, v = best(m)
        fits[m] = dict(label=LABEL[m] + ", scale free", log_a=la, a=10 ** la, chi2p=v, kglob=1)
    for key, la, theta in (("qi_late", LA_LATE, "8.8"), ("qi_early", LA_EARLY, "2.6")):
        fits[key] = dict(label=f"QI, Θ = {theta} × 10²⁶ m (fixed)", log_a=la, a=10 ** la,
                         chi2p=at("qi", la), kglob=0)

    # Evaluate nuisance parameters and both objective terms at the refined global scales.
    # Previously these diagnostics were taken from the nearest grid point instead.
    diag = {}
    for key in KEYS:
        m = "qi" if key.startswith("qi") else key
        la = fits[key]["log_a"]
        idx = int(np.argmin(np.abs(grids[m] - la)))
        rows = []
        for name in names:
            g = G[name]
            r = fit_one(g, NU[m], la, pars[m][name][idx])
            if not r.success:
                retry = fit_one(g, NU[m], la, None)
                if retry.success:
                    r = retry
                else:
                    raise RuntimeError(f"Final fit failed for {name}, {key}: {r.message}; {retry.message}")
            ud, ub, D, inc = unpack(g, r.x)
            chi2, pen = objective_terms(r.x, g, NU[m], la)
            rows.append(dict(name=name, n=len(g["R"]), n_nuisance=4 if g["bulge"] else 3,
                             chi2_data=chi2, prior_penalty=pen, chi2p=chi2 + pen,
                             ud=ud, ub=ub if g["bulge"] else None, D_ratio=D / g["D0"],
                             dinc=inc - g["i0"], pull_D=(D - g["D0"]) / g["eD"],
                             pull_i=(inc - g["i0"]) / g["ei"], distance_method=g["distance_method"]))
        diag[key] = rows
        f = fits[key]
        f["chi2_data"] = sum(r["chi2_data"] for r in rows)
        f["prior_penalty"] = sum(r["prior_penalty"] for r in rows)
        f["chi2p"] = f["chi2_data"] + f["prior_penalty"]
        f["theta_equiv_m"] = 2 * C * C / f["a"]
        ud = np.array([r["ud"] for r in rows])
        red = [r["chi2_data"] / (r["n"] - r["n_nuisance"]) for r in rows if r["n"] > r["n_nuisance"]]
        f["nuisance"] = dict(distance_summary(rows), median_ud=float(np.median(ud)),
                             ud_16_84=[float(np.percentile(ud, q)) for q in (16, 84)],
                             median_pull_i=float(np.median([r["pull_i"] for r in rows])),
                             median_chi2_data_per_dof=float(np.median(red)))
        f["distance_by_method"] = {
            str(method): dict(label=label, **distance_summary(subset))
            for method, label in DISTANCE_METHODS.items()
            if (subset := [r for r in rows if r["distance_method"] == method])
        }

    ref = "mond_simple"
    for f in fits.values():
        f["delta_q_vs_mond_simple"] = f["chi2p"] - fits[ref]["chi2p"]
        f["delta_q_vs_qi_free"] = f["chi2p"] - fits["qi"]["chi2p"]

    # Cluster resampling varies the sample, not the error model or the priors.
    # Recomputed profiles are supplied for each error scenario.
    rng = np.random.default_rng(seed)
    boots = {k: [] for k in KEYS}
    boots_qi = {k: [] for k in KEYS}
    la_boot = {m: [] for m in NU}
    for _ in range(boot):
        sel = list(rng.choice(names, size=len(names), replace=True))
        vals = {}
        for m in NU:
            la, vals[m] = best(m, sel)
            la_boot[m].append(la)
        vals["qi_late"] = at("qi", LA_LATE, sel)
        vals["qi_early"] = at("qi", LA_EARLY, sel)
        for k in KEYS:
            boots[k].append(vals[k] - vals[ref])
            boots_qi[k].append(vals[k] - vals["qi"])
    if boot:
        for k in KEYS:
            fits[k]["boot_delta_q_16_50_84"] = [float(np.percentile(boots[k], q)) for q in (16, 50, 84)]
            fits[k]["boot_delta_q_vs_qi_free_16_50_84"] = [float(np.percentile(boots_qi[k], q)) for q in (16, 50, 84)]
        for m in NU:
            fits[m]["boot_log_a_16_50_84"] = [float(np.percentile(la_boot[m], q)) for q in (16, 50, 84)]

    best_la_gal = {n: float(grids["qi"][int(np.argmin(prof["qi"][n]))]) for n in names}
    edge = sum(v <= GRID[0] + 1e-9 or v >= GRID[-1] - 1e-9 for v in best_la_gal.values())
    nnuis = sum(4 if g["bulge"] else 3 for g in gals)
    data_chi2_per_dof = fits[ref]["chi2_data"] / (npts - nnuis - 1)
    win_late = sum(q["chi2p"] < m["chi2p"] for q, m in zip(diag["qi_late"], diag[ref]))
    result = dict(n_galaxies=len(names), n_points=npts, n_nuisance=nnuis,
                  score=dict(name="Q", definition="chi2_data + prior_penalty",
                             interpretation="Descriptive penalized fit loss, not BIC or a Bayes factor; no k log n term."),
                  priors=dict(Y_disk=UD0, Y_bul=UB0, sigma_log_Y=SIG_LOGU,
                              D="Gaussian (SPARC e_D)", inc="Gaussian (SPARC e_Inc, min 1 deg)"),
                  fits=fits, per_galaxy=diag, per_galaxy_best_log_a_qi=best_la_gal,
                  n_gal_best_at_grid_edge=int(edge), n_gal_qi_late_beats_mond_simple=int(win_late),
                  chi2_data_per_dof_reference=data_chi2_per_dof,
                  grids={m: grids[m].tolist() for m in NU},
                  profiles={m: {n: np.round(prof[m][n], 6).tolist() for n in names} for m in NU},
                  bootstrap=dict(replicates=boot, seed=seed, unit="galaxy",
                                 conditional_on="Selected velocity errors and unchanged priors; grid-profile approximation."))
    if make_figures:
        figures(fits, grids, total, diag, best_la_gal)
    return result


def summary_table(result):
    lines = ["| Model | global k | a (m s⁻²) [bootstrap 16–84%] | equiv. Θ (m) | velocity χ² | prior penalty | ΔQ vs MOND simple [bootstrap 16–84%] | median Υ_disk | median D/D₀ | D/D₀ < 0.8 | distance pull < −2 |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for k in KEYS:
        f = result["fits"][k]
        a = f"{f['a'] * 1e10:.3f} × 10⁻¹⁰"
        if "boot_log_a_16_50_84" in f:
            lo, _, hi = f["boot_log_a_16_50_84"]
            a += f" [{10 ** lo * 1e10:.2f}–{10 ** hi * 1e10:.2f}]"
        dq = f"{f['delta_q_vs_mond_simple']:+.0f}"
        if k == "mond_simple":
            dq = "0 (reference)"
        elif "boot_delta_q_16_50_84" in f:
            lo, _, hi = f["boot_delta_q_16_50_84"]
            dq += f" [{lo:+.0f} to {hi:+.0f}]"
        d = f["nuisance"]
        lines.append(f"| {f['label']} | {f['kglob']} | {a} | {f['theta_equiv_m']:.3g} | "
                     f"{f['chi2_data']:.1f} | {f['prior_penalty']:.1f} | {dq} | "
                     f"{d['median_ud']:.2f} | {d['median_D_ratio']:.3f} | {d['n_D_ratio_lt_0p8']}/{d['n']} | "
                     f"{d['n_pull_D_lt_minus2']}/{d['n']} |")
    return lines


def write_summary(result):
    sensitivity = result["velocity_error_sensitivity"]
    lines = ["<!-- generated by fit_galaxies.py; do not edit -->",
             f"{result['n_galaxies']} galaxies, {result['n_points']} rotation-curve points; "
             f"{result['bootstrap']['replicates']} galaxy-bootstrap resamples per scenario.", "",
             "Q = velocity χ² + prior penalty. ΔQ is a descriptive fit comparison, not BIC, a Bayes factor, or a calibrated exclusion significance. "
             "Free-scale QI contains the fixed scales; a lower loss is expected with added freedom. Bootstrap ranges are conditional on each scenario's errors and priors.", "",
             "## Catalogue velocity errors", ""]
    lines += summary_table(result)
    lines += ["", "## Enlarged velocity errors: full refit", "",
              f"Velocity-error multiplier: {sensitivity['velocity_error_factor']:.4f} = "
              f"√max(1, {result['chi2_data_per_dof_reference']:.4f}). The diagnostic ratio uses velocity χ² only, "
              "divided by n_points − n_nuisance − 1 for the baseline MOND simple fit. All priors are unchanged. "
              "Every model and galaxy profile is refitted, then bootstrapped again with this multiplier held fixed. "
              "This is a conditional sensitivity check, not an inferred error model or a conservative evidence bound.", ""]
    lines += summary_table(sensitivity)
    lines += ["", "## Baseline distances by measurement method", "",
              "Distance pull = (D_fit − D_catalogue) / σ_D. Fractional shifts and standardized pulls answer different questions.", "",
              "| Model | Distance method | galaxies | median D/D₀ | median distance pull | D/D₀ < 0.8 | pull < −2 | pull < −3 |",
              "|---|---|---|---|---|---|---|---|"]
    for k in ("qi_late", "mond_simple"):
        for d in result["fits"][k]["distance_by_method"].values():
            lines.append(f"| {result['fits'][k]['label']} | {d['label']} | {d['n']} | {d['median_D_ratio']:.3f} | "
                         f"{d['median_pull_D']:+.2f} | {d['n_D_ratio_lt_0p8']} | "
                         f"{d['n_pull_D_lt_minus2']} | {d['n_pull_D_lt_minus3']} |")
    la = np.array(list(result["per_galaxy_best_log_a_qi"].values()))
    lines += ["", f"QI per-galaxy best Θ: median {2 * C * C / 10 ** np.median(la):.3g} m; "
              f"16–84% {2 * C * C / 10 ** np.percentile(la, 84):.3g}–{2 * C * C / 10 ** np.percentile(la, 16):.3g} m.",
              f"{result['n_gal_best_at_grid_edge']} per-galaxy optima reach the grid edge.",
              f"QI at Θ = 8.8 × 10²⁶ m has lower Q than MOND simple at its global scale in "
              f"{result['n_gal_qi_late_beats_mond_simple']}/{result['n_galaxies']} galaxies."]
    (OUT / "summary.md").write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=20261019)
    ap.add_argument("--procs", type=int, default=max(1, (mp.cpu_count() or 2) - 1))
    args = ap.parse_args()
    if args.boot < 0 or args.procs < 1:
        ap.error("--boot must be nonnegative and --procs must be positive")
    OUT.mkdir(exist_ok=True)
    gals = galaxies()
    print(f"{len(gals)} galaxies; baseline catalogue velocity errors", flush=True)
    result = run_analysis(gals, args.boot, args.seed, args.procs, make_figures=True)
    result["data"] = dict(source=A1.BASE_URL, sha256=A1.fetch())
    factor = math.sqrt(max(1.0, result["chi2_data_per_dof_reference"]))
    print(f"Full sensitivity refit: velocity errors × {factor:.4f}; priors unchanged", flush=True)
    sensitivity = run_analysis(with_velocity_errors(gals, factor), args.boot, args.seed, args.procs)
    sensitivity["velocity_error_factor"] = factor
    sensitivity["factor_selection"] = "sqrt(max(1, baseline MOND simple velocity chi2 / (n_points - n_nuisance - 1)))"
    result["velocity_error_sensitivity"] = sensitivity
    (OUT / "results.json").write_text(json.dumps(result, ensure_ascii=False, allow_nan=False) + "\n")
    write_summary(result)
    print((OUT / "summary.md").read_text())


if __name__ == "__main__":
    main()
