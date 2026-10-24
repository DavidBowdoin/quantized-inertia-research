"""A6c: QI's redshift law against the RC100 dark-matter fractions at z = 0.6-2.5.

Editorial analysis for the Quantized Inertia research archive. Requires numpy and scipy (09-analysis/requirements.txt).

Input: Table B1 of Nestor Shachar et al. 2023 (ApJ 944, 78; CC BY 4.0) as transcribed by Sentina 2026
(Zenodo 10.5281/zenodo.23442383, CC BY 4.0), downloaded into the git-ignored data/ folder. Row 87 (the lensed
galaxy J0901+1814) differs from the journal table in every fitted column; the journal values are used here, and the
transcribed row is kept as a sensitivity case.

Method (following Sentina's fdm_test.py): for each galaxy g_obs = Vc^2/Re. A candidate law a(z) predicts
g_bar by inverting the interpolating function, hence f_DM,pred = 1 - g_bar/g_obs, compared with the published
f_DM(Re) +- error. The main variance propagates the journal's Vc and Re errors,
with a fitted intrinsic scatter tau. The original 20%-Vc-only prescription and
illustrative correlations between f_DM and ln(g_obs) are sensitivity cases.

Run:  .venv/bin/python -I 09-analysis/a6c-rc100-qi/rc100_qi.py [--boot 400]
"""
import argparse
import csv
import hashlib
import io
import json
import math
import urllib.request
import zipfile
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = HERE / "data"
OUT = HERE / "results"
SOURCE = dict(url="https://zenodo.org/records/23442383/files/a0z_zenodo_package_v6.2.zip?download=1",
              sha256="ddef7a04fec10be55c2c2d8ab85109e2e1ec4cba2e9f00e45cedc1a7c3410b9f",
              file="sentina-a0z-package-v6.2.zip", member="a0z_v62_zenodo/data/rc100_table3.csv")
# Nestor Shachar et al. 2023, Table B1, row 87 (J0901+1814): log Mbaryon, Re (kpc), fDM(Re) (error), Vcirc(Re).
ROW87_JOURNAL = dict(logMbar=10.72, Re=3.85, fDM=0.44, e_fDM=0.15, Vc=250.0)

C = 2.99792458e8
THETA0 = 8.8e26
KK_TO_SI = 1e6 / 3.0856775814913673e19
OM, OL = 0.315, 0.685
VC_FRAC = 0.20
JOURNAL_ERRORS = ROOT.parent / "01-papers/2023-nestorshachar-rc100-rotation-curves/table-b1-errors.csv"


def fetch():
    DATA.mkdir(exist_ok=True)
    p = DATA / SOURCE["file"]
    if not p.exists():
        req = urllib.request.Request(SOURCE["url"], headers={"User-Agent": "qi-research-archive/1.0 (python-urllib)"})
        p.write_bytes(urllib.request.urlopen(req, timeout=120).read())
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != SOURCE["sha256"]:
        raise SystemExit(f"checksum mismatch: {h}")
    with zipfile.ZipFile(p) as z:
        rows = list(csv.DictReader(io.StringIO(z.read(SOURCE["member"]).decode("utf-8"))))
    return rows


def table(rows, fix87=True, drop=(), errors="journal", rho=0.0, fixed_weights=False):
    """rho = assumed Corr(f_DM, ln g_obs), not measured by this archive.

    Vc-Re covariance is unavailable; journal mode treats those errors as independent.
    """
    with JOURNAL_ERRORS.open() as f:
        error_rows = {int(r["id"]): r for r in csv.DictReader(l for l in f if not l.startswith("#"))}
    out = []
    for r in rows:
        d = {k: float(v) for k, v in r.items()}
        if fix87 and int(d["id"]) == 87:
            d.update(ROW87_JOURNAL)
        if int(d["id"]) in drop:
            continue
        er = error_rows[int(d["id"])]
        d["sigma_lng"] = (math.hypot(2 * float(er["e_Vc"]) / d["Vc"], float(er["e_Re"]) / d["Re"])
                          if errors == "journal" else 2 * VC_FRAC)
        d["rho_f_lng"] = rho
        out.append(d)
    T = {k: np.array([d[k] for d in out]) for k in out[0]}
    T["gobs"] = T["Vc"] ** 2 / T["Re"] * KK_TO_SI
    if fixed_weights:
        # Data-based derivative of the QI prediction, evaluated at the observed f_DM with x = 1 - f_DM:
        # d f / d ln g_obs = -x (1 - x^2) / (1 + x^2). Same weights for every model, so no fit can shrink its errors.
        x = np.clip(1 - T["fDM"], 1e-3, 1.0)
        T["d_fixed"] = -x * (1 - x * x) / (1 + x * x)
    return T


def E(z):
    return np.sqrt(OM * (1 + z) ** 3 + OL)


# Inverse interpolating functions: g_bar from g_obs at scale a.
def gbar_qi(g, a):
    # Rationalized form avoids cancellation when g << a.
    return 2 * g * g / (np.hypot(a, 2 * g) + a)


_LX = np.linspace(-8, 6, 20001)
_LY = np.log10(10 ** _LX / (1 - np.exp(-np.sqrt(10 ** _LX))))


def gbar_mcg(g, a):
    return 10 ** np.interp(np.log10(g / a), _LY, _LX) * a


INVERSE = {"qi": gbar_qi, "mcg": gbar_mcg}


def fpred(kind, g, a):
    return 1 - INVERSE[kind](g, a) / g


def residual_variance(ef, sigma_lng, derivative, tau, rho=0.0):
    """Var[f_obs - f_pred(g_obs)] to first order, including optional covariance."""
    return ef ** 2 + (sigma_lng * derivative) ** 2 - 2 * derivative * rho * ef * sigma_lng + tau ** 2


def nll(kind, T, idx, a_of_z, tau):
    g, z = T["gobs"][idx], T["z"][idx]
    a = a_of_z(z)
    fp = fpred(kind, g, a)
    d = (fpred(kind, g * 1.05, a) - fpred(kind, g / 1.05, a)) / (2 * math.log(1.05))
    if "d_fixed" in T:
        d = T["d_fixed"][idx]
    v = residual_variance(T["e_fDM"][idx], T["sigma_lng"][idx], d, tau, T["rho_f_lng"][idx])
    return 0.5 * float(np.sum((T["fDM"][idx] - fp) ** 2 / v + np.log(v)))


def fit(kind, T, idx, law, free_amp=True, amp=None, gamma=None):
    """law(z, gamma) -> shape; returns (nll, params)."""
    def obj(p):
        if free_amp and gamma is None:
            la, g_, tau = p
        elif free_amp:
            la, tau = p
            g_ = gamma
        else:
            tau = p[0]
            la, g_ = math.log10(amp), gamma
        return nll(kind, T, idx, lambda z: 10 ** la * law(z, g_), abs(tau))
    best = None
    starts = [-10.4, -10.0, -9.6] if free_amp else [None]
    for la0 in starts:
        for t0 in (0.05, 0.15):
            if free_amp and gamma is None:
                x0 = [la0, 1.0, t0]
            elif free_amp:
                x0 = [la0, t0]
            else:
                x0 = [t0]
            r = minimize(obj, x0, method="Nelder-Mead", options=dict(xatol=1e-6, fatol=1e-8, maxiter=4000))
            if r.success and np.isfinite(r.fun) and (best is None or r.fun < best.fun):
                best = r
    if best is None:
        raise RuntimeError("No converged likelihood fit")
    p = list(best.x)
    if free_amp and gamma is None:
        res = dict(log_A=p[0], gamma=p[1], tau=abs(p[2]))
    elif free_amp:
        res = dict(log_A=p[0], gamma=gamma, tau=abs(p[1]))
    else:
        res = dict(log_A=math.log10(amp), gamma=gamma, tau=abs(p[0]))
    return float(best.fun), res


LAWS = {
    "constant": lambda z, g: np.ones_like(z),
    "one_plus_z": lambda z, g: (1 + z),
    "hubble": lambda z, g: E(z),
    "power": lambda z, g: (1 + z) ** g,
}


def run_models(T, idx, a1, a1b):
    out = {}
    # QI function
    out["qi_published"] = fit("qi", T, idx, LAWS["one_plus_z"], free_amp=False, amp=2 * C * C / THETA0, gamma=1.0)
    if a1:
        out["qi_calibrated_a1"] = fit("qi", T, idx, LAWS["one_plus_z"], free_amp=False, amp=a1, gamma=1.0)
    if a1b:
        out["qi_calibrated_a1b"] = fit("qi", T, idx, LAWS["one_plus_z"], free_amp=False, amp=a1b, gamma=1.0)
    out["qi_one_plus_z"] = fit("qi", T, idx, LAWS["one_plus_z"], gamma=1.0)
    out["qi_constant"] = fit("qi", T, idx, LAWS["constant"], gamma=0.0)
    out["qi_hubble"] = fit("qi", T, idx, LAWS["hubble"], gamma=0.0)
    out["qi_power"] = fit("qi", T, idx, LAWS["power"])
    # McGaugh function (Sentina's convention), for validation
    out["mcg_constant"] = fit("mcg", T, idx, LAWS["constant"], gamma=0.0)
    out["mcg_hubble"] = fit("mcg", T, idx, LAWS["hubble"], gamma=0.0)
    return out


def gamma_profile(T, idx, grid):
    vals = [fit("qi", T, idx, LAWS["power"], gamma=g)[0] for g in grid]
    return np.array(vals)


def binned_scale(T, edges):
    out = []
    for i in range(len(edges) - 1):
        sel = np.where((T["z"] >= edges[i]) & ((T["z"] < edges[i + 1]) if i < len(edges) - 2 else (T["z"] <= edges[i + 1])))[0]
        f_, p = fit("qi", T, sel, LAWS["constant"], gamma=0.0)
        # 1-sigma interval on log A from delta nll = 0.5, profiling tau
        def prof(la):
            return min(nll("qi", T, sel, lambda z: 10 ** la * np.ones_like(z), t) for t in np.linspace(0.0, 0.4, 81))
        base = prof(p["log_A"])
        grid = np.linspace(p["log_A"] - 1.0, p["log_A"] + 1.0, 201)
        pv = np.array([prof(x) for x in grid])
        ok = grid[pv - base <= 0.5]
        out.append(dict(n=int(len(sel)), z_med=float(np.median(T["z"][sel])), log_aq=p["log_A"],
                        lo=float(ok.min()), hi=float(ok.max())))
    return out


def a1_scales():
    a1 = a1b = None
    try:
        a1 = json.loads((ROOT / "a1-sparc-rar-refit/results/results.json").read_text())["fits"]["qi_free"]["a"]
    except (OSError, KeyError, ValueError):
        pass
    try:
        a1b = json.loads((ROOT / "a1b-sparc-per-galaxy/results/results.json").read_text())["fits"]["qi"]["a"]
    except (OSError, KeyError, ValueError):
        pass
    return a1, a1b


# ---------------------------------------------------------------- figure

STYLE = """<style>
svg { --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --grid:#e4e3df; --pt:#8f8d86;
      --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; --s4:#eda100; --s5:#e87ba4; --s6:#008300; --s7:#6250d6; }
@media (prefers-color-scheme: dark) {
  svg { --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --grid:#33322f; --pt:#77756f;
        --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500; --s5:#d55181; --s6:#008300; --s7:#9085e9; } }
text { font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: var(--ink2); font-size: 12px; }
.t { fill: var(--ink); font-size: 14px; font-weight: 600; }
.ax { stroke: var(--ink2); stroke-width: 1; }
.gr { stroke: var(--grid); stroke-width: 1; }
.ln { fill: none; stroke-width: 2; stroke-linejoin: round; }
</style>"""


def fig(res, path):
    w, h, ml, mr, mt, mb = 760, 500, 64, 20, 44, 50
    xr, yr = (0.4, 2.7), (0, 9)
    X = lambda v: ml + (v - xr[0]) / (xr[1] - xr[0]) * (w - mr - ml)
    Y = lambda v: h - mb - (v - yr[0]) / (yr[1] - yr[0]) * (h - mb - mt)
    el = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">',
          "<title>QI scale fitted to RC100 dark-matter fractions, by redshift bin</title>", STYLE,
          f'<rect width="{w}" height="{h}" fill="var(--surface)"/>',
          f'<text class="t" x="{ml}" y="24">QI scale fitted to RC100 dark-matter fractions, by redshift bin</text>',
          f'<text x="{(ml + w - mr) / 2}" y="{h - 12}" text-anchor="middle">redshift z</text>',
          f'<text transform="translate(16,{(mt + h - mb) / 2}) rotate(-90)" text-anchor="middle">a_Q (10⁻¹⁰ m s⁻²)</text>']
    for v in (0.5, 1.0, 1.5, 2.0, 2.5):
        el.append(f'<line class="gr" x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{mt}" y2="{h - mb}"/><text x="{X(v):.1f}" y="{h - mb + 16}" text-anchor="middle">{v:g}</text>')
    for v in (0, 2, 4, 6, 8):
        el.append(f'<line class="gr" x1="{ml}" x2="{w - mr}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/><text x="{ml - 6}" y="{Y(v) + 4:.1f}" text-anchor="end">{v:g}</text>')
    zz = np.linspace(xr[0], xr[1], 60)

    def line(ys, color, dash, tip):
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(a):.1f},{Y(b):.1f}" for i, (a, b) in enumerate(zip(zz, ys)))
        da = f' stroke-dasharray="{dash}"' if dash else ""
        el.append(f'<path class="ln" d="{d}" stroke="{color}"{da}><title>{tip}</title></path>')
    m = res["main"]["models"]
    line(2 * C * C * (1 + zz) / THETA0 * 1e10, "var(--s2)", None, "QI published")
    line(10 ** m["qi_one_plus_z"]["params"]["log_A"] * (1 + zz) * 1e10, "var(--s3)", "6 3", "QI (1+z), amplitude fitted")
    line(np.full_like(zz, 10 ** m["qi_constant"]["params"]["log_A"] * 1e10), "var(--ink2)", "2 3", "constant, amplitude fitted")
    for b in res["main"]["bins"]:
        v, lo, hi = (10 ** b[k] * 1e10 for k in ("log_aq", "lo", "hi"))
        el.append(f'<line x1="{X(b["z_med"]):.1f}" x2="{X(b["z_med"]):.1f}" y1="{Y(lo):.1f}" y2="{Y(min(hi, 9)):.1f}" stroke="var(--ink)" stroke-width="2"/>'
                  f'<circle cx="{X(b["z_med"]):.1f}" cy="{Y(v):.1f}" r="5" fill="var(--ink)" stroke="var(--surface)" stroke-width="2"><title>{b["n"]} galaxies, z̃ = {b["z_med"]:.2f}: a_Q = {v:.2f}</title></circle>')
    for i, (lab, col, da) in enumerate([("QI published: 2c²(1+z)/Θ₀", "var(--s2)", None), ("QI (1+z), amplitude fitted", "var(--s3)", "6 3"),
                                        ("constant scale, amplitude fitted", "var(--ink2)", "2 3")]):
        y = 62 + 18 * i
        dd = f' stroke-dasharray="{da}"' if da else ""
        el.append(f'<line x1="80" x2="104" y1="{y}" y2="{y}" stroke="{col}" stroke-width="2"{dd}/><text x="110" y="{y + 4}">{lab}</text>')
    path.write_text("\n".join(el + ["</svg>"]) + "\n")


# ---------------------------------------------------------------- main

def summarize(models):
    out = {}
    for k, (f_, p) in models.items():
        out[k] = dict(nll=f_, params=p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=400)
    ap.add_argument("--seed", type=int, default=20261023)
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    rows = fetch()
    a1, a1b = a1_scales()
    res = dict(inputs=dict(source=dict(url=SOURCE["url"], sha256=SOURCE["sha256"]), row87_journal=ROW87_JOURNAL,
                           vc_fraction_sentina=VC_FRAC, journal_errors=str(JOURNAL_ERRORS.relative_to(ROOT.parent)),
                           main_errors="published Vc and Re errors; Vc-Re and fDM-ln(gobs) covariance set to zero",
                           cosmology=dict(Om=OM, OL=OL), a1=a1, a1b=a1b))

    # Validation on Sentina's table exactly as transcribed (McGaugh function).
    Ts = table(rows, fix87=False, errors="sentina")
    ii = np.arange(len(Ts["z"]))
    vc = fit("mcg", Ts, ii, LAWS["constant"], gamma=0.0)
    vh = fit("mcg", Ts, ii, LAWS["hubble"], gamma=0.0)
    res["validation_sentina"] = dict(mcg_constant_A=10 ** vc[1]["log_A"] * 1e10, dnll_hubble_minus_constant=vh[0] - vc[0],
                                     sentina_reported=dict(A_const_median=1.264, dnll_hubble=8.98))

    variants = {"main": dict(fix87=True, drop=()),
                "sentina_errors": dict(errors="sentina"),
                "row87_as_transcribed": dict(fix87=False, errors="sentina"),
                "drop_67_83": dict(fix87=True, drop=(67, 83)), "z_below_1p5": None,
                "rho_minus_0p5": dict(rho=-0.5), "rho_plus_0p5": dict(rho=0.5),
                "fixed_weights": dict(fixed_weights=True)}
    for name, v in variants.items():
        if v is None:
            T = table(rows)
            idx = np.where(T["z"] < 1.5)[0]
        else:
            T = table(rows, **v)
            idx = np.arange(len(T["z"]))
        models = summarize(run_models(T, idx, a1, a1b))
        ref = models["qi_constant"]["nll"]
        for k in models:
            models[k]["dnll_vs_qi_constant"] = models[k]["nll"] - ref
        entry = dict(n=int(len(idx)), models=models, error_options=v or dict(errors="journal", rho=0.0))
        if name == "main":
            grid = np.round(np.arange(-1.5, 2.51, 0.05), 3)
            prof = gamma_profile(T, idx, grid)
            ok = grid[prof - prof.min() <= 0.5]
            ok2 = grid[prof - prof.min() <= 2.0]
            entry["gamma_profile"] = dict(grid=grid.tolist(), dnll=(prof - prof.min()).tolist(),
                                          best=float(grid[int(np.argmin(prof))]), one_sigma=[float(ok.min()), float(ok.max())],
                                          two_sigma=[float(ok2.min()), float(ok2.max())])
            entry["bins"] = binned_scale(T, np.quantile(T["z"], [0, 0.25, 0.5, 0.75, 1]).tolist())
            rng = np.random.default_rng(args.seed)
            g_b, d1_b, dp_b = [], [], []
            for _ in range(args.boot):
                bi = rng.integers(0, len(idx), len(idx))
                c0 = fit("qi", T, bi, LAWS["constant"], gamma=0.0)[0]
                c1 = fit("qi", T, bi, LAWS["one_plus_z"], gamma=1.0)[0]
                pw = fit("qi", T, bi, LAWS["power"])
                cp = fit("qi", T, bi, LAWS["one_plus_z"], free_amp=False, amp=2 * C * C / THETA0, gamma=1.0)[0]
                g_b.append(pw[1]["gamma"]); d1_b.append(c1 - c0); dp_b.append(cp - c0)
            g_b, d1_b, dp_b = map(np.array, (g_b, d1_b, dp_b))
            entry["bootstrap"] = dict(n=len(g_b), gamma_16_50_84=np.percentile(g_b, [16, 50, 84]).tolist(),
                                      gamma_2p5_97p5=np.percentile(g_b, [2.5, 97.5]).tolist(),
                                      frac_gamma_ge_1=float(np.mean(g_b >= 1)),
                                      dnll_one_plus_z_minus_constant_16_50_84=np.percentile(d1_b, [16, 50, 84]).tolist(),
                                      frac_one_plus_z_better=float(np.mean(d1_b < 0)),
                                      dnll_published_minus_constant_16_50_84=np.percentile(dp_b, [16, 50, 84]).tolist())
        res[name] = entry
    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    fig(res, OUT / "fig-1-aq-by-redshift.svg")
    (OUT / "summary.md").write_text(summary(res))
    print((OUT / "summary.md").read_text())


LABELS = {
    "qi_published": "QI published: a_Q = 2c²(1+z)/Θ₀ (k = 1, τ only)",
    "qi_calibrated_a1": "QI (1+z), a_Q(0) from A1 SPARC fit (k = 1)",
    "qi_calibrated_a1b": "QI (1+z), a_Q(0) from A1b SPARC fit (k = 1)",
    "qi_one_plus_z": "QI (1+z), amplitude fitted (k = 2)",
    "qi_constant": "QI function, constant scale (k = 2)",
    "qi_hubble": "QI function, scale ∝ H(z) (k = 2)",
    "qi_power": "QI function, (1+z)^γ, γ fitted (k = 3)",
    "mcg_constant": "McGaugh function, constant scale (k = 2)",
    "mcg_hubble": "McGaugh function, scale ∝ H(z) (k = 2)",
}


def summary(r):
    v = r["validation_sentina"]
    L = ["# A6c results (generated by rc100_qi.py; do not edit)", "",
         "Editorial analysis. Main fits propagate the journal Vc and Re errors, assuming zero covariance. "
         "The ±0.5 correlations are illustrative sensitivity choices, not measurements. Likelihood scores and profile intervals "
         "are conditional on this approximate error model; bootstrap fractions are not posterior probabilities or calibrated p-values.", "",
         f"Validation on Sentina's table as transcribed (McGaugh function): constant-scale A = {v['mcg_constant_A']:.3f} × 10⁻¹⁰ m s⁻², "
         f"Δ(−ln L) of H(z) relative to constant = {v['dnll_hubble_minus_constant']:.2f}. Sentina reports 1.26 (bootstrap median) and 8.98.", ""]
    for name in ("main", "sentina_errors", "row87_as_transcribed", "drop_67_83", "z_below_1p5", "rho_minus_0p5", "rho_plus_0p5", "fixed_weights"):
        e = r[name]
        L += [f"## {name} ({e['n']} galaxies)", "", "| Model | Δ(−ln L) vs QI constant | a_Q(0) (10⁻¹⁰ m s⁻²) | γ | τ |", "|---|---|---|---|---|"]
        for k, m in e["models"].items():
            p = m["params"]
            gamma_label = "—" if "hubble" in k else f"{p['gamma']:.2f}"
            L.append(f"| {LABELS[k]} | {m['dnll_vs_qi_constant']:+.2f} | {10 ** p['log_A'] * 1e10:.3f} | {gamma_label} | {p['tau']:.3f} |")
        L.append("")
        if "gamma_profile" in e:
            g = e["gamma_profile"]
            b = e["bootstrap"]
            L += [f"Profile likelihood for γ: best {g['best']:.2f}; Δ(−ln L) ≤ 0.5: {g['one_sigma'][0]:.2f} to {g['one_sigma'][1]:.2f}; "
                  f"≤ 2: {g['two_sigma'][0]:.2f} to {g['two_sigma'][1]:.2f}.", "",
                  f"Galaxy bootstrap ({b['n']}): γ 16/50/84% = " + ", ".join(f"{x:.2f}" for x in b["gamma_16_50_84"]) +
                  f"; 2.5–97.5% = {b['gamma_2p5_97p5'][0]:.2f} to {b['gamma_2p5_97p5'][1]:.2f}; fraction with γ ≥ 1 = {b['frac_gamma_ge_1']:.3f}. "
                  "Δ(−ln L)[(1+z) − constant] 16/50/84% = " + ", ".join(f"{x:+.2f}" for x in b["dnll_one_plus_z_minus_constant_16_50_84"]) +
                  f"; (1+z) better in {b['frac_one_plus_z_better']:.3f}. Published law minus constant: " +
                  ", ".join(f"{x:+.2f}" for x in b["dnll_published_minus_constant_16_50_84"]) + ".", "",
                  "QI scale per redshift quartile (constant within bin; 1σ from Δ(−ln L) = 0.5):", "",
                  "| Bin | N | z̃ | a_Q (10⁻¹⁰ m s⁻²) | published 2c²(1+z̃)/Θ₀ |", "|---|---|---|---|---|"]
            for i, bn in enumerate(e["bins"]):
                L.append(f"| {i + 1} | {bn['n']} | {bn['z_med']:.2f} | {10 ** bn['log_aq'] * 1e10:.2f} ({10 ** bn['lo'] * 1e10:.2f}–{10 ** bn['hi'] * 1e10:.2f}) | "
                         f"{2 * C * C * (1 + bn['z_med']) / THETA0 * 1e10:.2f} |")
            L.append("")
    return "\n".join(L).rstrip() + "\n"


if __name__ == "__main__":
    main()
