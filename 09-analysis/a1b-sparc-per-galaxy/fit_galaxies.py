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


def galaxies():
    A1.fetch()
    gal = A1.read_galaxies()
    for line in (A1.DATA / "SPARC_Lelli2016c.mrt").read_text().splitlines():
        p = line.split()
        if len(line) > 100 and len(p) >= 18 and p[1].isdigit() and p[0] in gal:
            gal[p[0]].update(eD=float(p[3]), einc=float(p[6]))
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
                        bulge=bool(np.any(arr["Vb"] > 0)), **arr))
    return out


def unpack(g, p):
    """params -> (Y_disk, Y_bul, D, inc)."""
    if g["bulge"]:
        lud, lub, D, inc = p
    else:
        (lud, D, inc), lub = p, math.log10(UB0)
    return 10 ** lud, 10 ** lub, D, inc


def objective(p, g, nu, la):
    ud, ub, D, inc = unpack(g, p)
    if D <= 0 or not (1.0 < inc < 90.0):
        return 1e12
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
    return chi2 + pen


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=20261019)
    ap.add_argument("--procs", type=int, default=max(1, (mp.cpu_count() or 2) - 1))
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    gals = galaxies()
    npts = int(sum(len(g["R"]) for g in gals))
    print(f"{len(gals)} galaxies, {npts} rotation-curve points")

    grids = {m: (GRID_QI if m == "qi" else GRID) for m in NU}
    jobs = [(g, m, grids[m]) for m in NU for g in gals]
    prof = {m: {} for m in NU}
    pars = {m: {} for m in NU}
    with mp.Pool(args.procs) as pool:
        for i, (name, m, vals, ps) in enumerate(pool.imap_unordered(profile_galaxy, jobs, chunksize=2), 1):
            prof[m][name], pars[m][name] = np.array(vals), ps
            if i % 100 == 0:
                print(f"  {i}/{len(jobs)} galaxy profiles")
    names = [g["name"] for g in gals]
    G = {g["name"]: g for g in gals}

    def total(m, sel=None):
        sel = names if sel is None else sel
        return np.sum([prof[m][n] for n in sel], axis=0)

    def best(m, sel=None):
        t, grid = total(m, sel), grids[m]
        keep = np.isin(grid, GRID)          # free fits use the regular grid only
        t, grid = t[keep], grid[keep]
        i = int(np.argmin(t))
        # parabolic refinement
        if 0 < i < len(grid) - 1:
            y0, y1, y2 = t[i - 1], t[i], t[i + 1]
            den = y0 - 2 * y1 + y2
            dx = 0.5 * (y0 - y2) / den if den > 0 else 0.0
            h = grid[i] - grid[i - 1]
            return grid[i] + dx * h, y1 - 0.25 * (y0 - y2) * dx, int(np.argmin(np.abs(grids[m] - grid[i])))
        return grid[i], t[i], int(np.argmin(np.abs(grids[m] - grid[i])))

    def at(m, la, sel=None):
        return float(total(m, sel)[int(np.argmin(np.abs(grids[m] - la)))])

    lnn = math.log(npts)
    fits = {}
    for m in NU:
        la, v, i = best(m)
        fits[m] = dict(label=LABEL[m] + ", scale free", log_a=float(la), a=10 ** float(la), chi2p=float(v), kglob=1, idx=i)
    fits["qi_late"] = dict(label="QI, Θ = 8.8 × 10²⁶ m (fixed)", log_a=LA_LATE, a=10 ** LA_LATE, chi2p=at("qi", LA_LATE), kglob=0)
    fits["qi_early"] = dict(label="QI, Θ = 2.6 × 10²⁶ m (fixed)", log_a=LA_EARLY, a=10 ** LA_EARLY, chi2p=at("qi", LA_EARLY), kglob=0)
    ref = "mond_simple"
    for k, f in fits.items():
        f["bic_rel"] = f["chi2p"] + f["kglob"] * lnn - (fits[ref]["chi2p"] + fits[ref]["kglob"] * lnn)
        f["theta_equiv_m"] = 2 * C * C / f["a"]

    # galaxy bootstrap on the stored profiles
    rng = np.random.default_rng(args.seed)
    keys = ["qi_early", "qi_late", "qi", "mond_simple", "mond_standard", "rar_exp"]
    boots = {k: [] for k in keys}
    la_boot = {m: [] for m in NU}
    for _ in range(args.boot):
        sel = list(rng.choice(names, size=len(names), replace=True))
        vals = {}
        for m in NU:
            la, v, _ = best(m, sel)
            vals[m] = v + lnn
            la_boot[m].append(la)
        vals["qi_late"] = at("qi", LA_LATE, sel)
        vals["qi_early"] = at("qi", LA_EARLY, sel)
        for k in keys:
            boots[k].append(vals[k] - vals[ref])
    for k in keys:
        b = np.array(boots[k])
        fits[k]["boot_dbic_16_50_84"] = [float(np.percentile(b, q)) for q in (16, 50, 84)]
        fits[k]["boot_frac_best"] = float(np.mean([min(keys, key=lambda kk: boots[kk][j]) == k for j in range(len(b))]))
    for m in NU:
        fits[m]["boot_log_a_16_50_84"] = [float(np.percentile(la_boot[m], q)) for q in (16, 50, 84)]

    # per-galaxy diagnostics at each model's global optimum
    def per_gal(m, la):
        i = int(np.argmin(np.abs(grids[m] - la)))
        rows = []
        for n in names:
            g = G[n]
            ud, ub, D, inc = unpack(g, pars[m][n][i])
            rows.append(dict(name=n, n=len(g["R"]), chi2p=float(prof[m][n][i]), ud=ud, ub=ub if g["bulge"] else None,
                             D_ratio=D / g["D0"], dinc=inc - g["i0"], pull_D=(D - g["D0"]) / g["eD"],
                             pull_i=(inc - g["i0"]) / g["ei"]))
        return rows

    diag = {k: per_gal("qi" if k.startswith("qi") else k, fits[k]["log_a"]) for k in keys}
    summ = {}
    for k, rows in diag.items():
        ud = np.array([r["ud"] for r in rows])
        red = np.array([r["chi2p"] / max(1, r["n"] - 3) for r in rows])
        summ[k] = dict(median_ud=float(np.median(ud)), ud_16_84=[float(np.percentile(ud, 16)), float(np.percentile(ud, 84))],
                       median_D_ratio=float(np.median([r["D_ratio"] for r in rows])),
                       median_pull_D=float(np.median([r["pull_D"] for r in rows])),
                       median_pull_i=float(np.median([r["pull_i"] for r in rows])),
                       frac_ud_low=float(np.mean(ud < 0.25)),
                       median_chi2_red=float(np.median(red)), frac_chi2_red_gt2=float(np.mean(red > 2)))
        fits[k]["nuisance"] = summ[k]

    # which galaxies prefer which scale (QI)
    best_la_gal = {n: float(grids["qi"][np.isin(grids["qi"], GRID)][int(np.argmin(prof["qi"][n][np.isin(grids["qi"], GRID)]))]) for n in names}
    edge = sum(v <= GRID[0] + 1e-9 or v >= GRID[-1] - 1e-9 for v in best_la_gal.values())
    # velocity errors are underestimated for every model (median chi2_red ~ 2.7): rescale by the reference fit's
    # chi2 per degree of freedom to get a conservative Delta BIC
    nnuis = sum(4 if g["bulge"] else 3 for g in gals)
    scale = fits[ref]["chi2p"] / (npts - nnuis - 1)
    for k in fits:
        fits[k]["bic_rel_scaled"] = fits[k]["bic_rel"] / scale
        if "boot_dbic_16_50_84" in fits[k]:
            fits[k]["boot_dbic_scaled_16_50_84"] = [v / scale for v in fits[k]["boot_dbic_16_50_84"]]
    win_late = sum(prof["qi"][n][int(np.argmin(np.abs(grids["qi"] - LA_LATE)))] < prof["mond_simple"][n][fits[ref]["idx"]] for n in names)

    result = dict(n_galaxies=len(names), n_points=npts, priors=dict(Y_disk=UD0, Y_bul=UB0, sigma_log_Y=SIG_LOGU, D="Gaussian (SPARC e_D)", inc="Gaussian (SPARC e_Inc, min 1 deg)"),
                  fits={k: {kk: vv for kk, vv in v.items() if kk != "idx"} for k, v in fits.items()},
                  per_galaxy_best_log_a_qi=best_la_gal, n_gal_best_at_grid_edge=int(edge), n_gal_qi_late_beats_mond_simple=int(win_late),
                  chi2_per_dof_reference=scale, n_nuisance=nnuis, per_galaxy={k: [{kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in r.items()} for r in rows] for k, rows in diag.items()},
                  grids={m: grids[m].tolist() for m in NU},
                  profiles={m: {n: np.round(prof[m][n], 2).tolist() for n in names} for m in NU},  # chi2 to 0.01
                  bootstrap=dict(replicates=args.boot, seed=args.seed, unit="galaxy"))
    (OUT / "results.json").write_text(json.dumps(result, ensure_ascii=False) + "\n")

    L = ["<!-- generated by fit_galaxies.py; do not edit -->",
         f"{len(names)} galaxies, {npts} rotation-curve points; {args.boot} galaxy-bootstrap resamples.", "",
         f"χ² per degree of freedom of the reference (MOND simple) fit: {scale:.2f}; \"scaled\" ΔBIC divides by it.", "",
         "| Model | global k | a (m s⁻²) [bootstrap 16–84%] | equiv. Θ (m) | χ² + priors | ΔBIC vs MOND simple | bootstrap ΔBIC 16–84% | scaled ΔBIC [bootstrap 16–84%] | best in bootstrap | median Υ_disk [16–84%] | median D/D₀ | median χ²_red | galaxies with χ²_red > 2 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for k in keys:
        f = fits[k]
        a = f"{f['a'] * 1e10:.3f} × 10⁻¹⁰"
        if "boot_log_a_16_50_84" in f:
            b = f["boot_log_a_16_50_84"]
            a += f" [{10 ** b[0] * 1e10:.2f}–{10 ** b[2] * 1e10:.2f}]"
        bd = f["boot_dbic_16_50_84"]
        nz = f["nuisance"]
        L.append(f"| {f['label']} | {f['kglob']} | {a} | {f['theta_equiv_m']:.3g} | {f['chi2p']:.0f} | {f['bic_rel']:+.0f} | "
                 + (f"{bd[0]:+.0f} to {bd[2]:+.0f}" if k != ref else "(reference)")
                 + f" | {f['bic_rel_scaled']:+.0f}" + (f" [{f['boot_dbic_scaled_16_50_84'][0]:+.0f} to {f['boot_dbic_scaled_16_50_84'][2]:+.0f}]" if k != ref else "")
                 + f" | {100 * f['boot_frac_best']:.0f}% | {nz['median_ud']:.2f} [{nz['ud_16_84'][0]:.2f}–{nz['ud_16_84'][1]:.2f}] | "
                 f"{nz['median_D_ratio']:.3f} | {nz['median_chi2_red']:.2f} | {100 * nz['frac_chi2_red_gt2']:.0f}% |")
    la_q = np.array(list(best_la_gal.values()))
    L += ["", f"QI, per-galaxy best Θ (each galaxy alone): median {2 * C * C / 10 ** np.median(la_q):.3g} m; "
          f"16–84% {2 * C * C / 10 ** np.percentile(la_q, 84):.3g} – {2 * C * C / 10 ** np.percentile(la_q, 16):.3g} m.",
          f"({edge} galaxies have their best value at the edge of the grid, a = {10 ** GRID[0]:.2g}–{10 ** GRID[-1]:.2g} m s⁻², so the spread is a lower limit.)",
          f"Galaxies where QI at Θ = 8.8 × 10²⁶ m fits better than MOND simple at its global a₀: {win_late} of {len(names)}."]
    (OUT / "summary.md").write_text("\n".join(L) + "\n")
    figures(fits, grids, total, diag, best_la_gal)
    print((OUT / "summary.md").read_text())


if __name__ == "__main__":
    main()
