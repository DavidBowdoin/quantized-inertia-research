"""A6e: QI's redshift law against 263 discs at 0.6 <= z < 2.5 with halo-independent baryonic accelerations.

Editorial analysis for the Quantized Inertia research archive. Requires numpy and scipy (09-analysis/requirements.txt).

Input: the catalogues of Sharma et al. 2025 (A&A 699, A164; Zenodo 10.5281/zenodo.15458539, CC BY 4.0) for the
KMOS3D, KGES and KROSS surveys. For each galaxy they give the circular velocity (pressure corrected) at
R_e, R_opt = 1.89 R_e and R_out = 2.95 R_e, and the baryonic mass enclosed within each radius from SED stellar
masses plus molecular and atomic gas from scaling relations. Their dynamical mass is exactly V^2 R / G, so
    g_obs = V^2 / R,    g_bar = G M_bar(<R) / R^2,
in the same spherical convention, with no dark-matter halo fitted. This is the QI-consistent form of the data.

Residuals are taken in ln g_obs against McCulloch 2017 Eq. 8, g = g_bar sqrt(1 + a/g_bar), with first-order
propagation of the velocity, baryonic-mass and radius errors (radius enters both accelerations) plus a fitted
intrinsic scatter. The propagation slope is evaluated at each observed point, where for Eq. 8 it depends only on the
observed ratio: s = (1 + (g_bar/g_obs)^2)/2. Weights are therefore the same for every model; letting them follow the
model would let a fit shrink its own error bars (with baryonic-mass errors of ~0.55 dex, that artefact dominated).

Run:  .venv/bin/python -I 09-analysis/a6e-sharma-qi/sharma_qi.py [--boot 400]
"""
import argparse
import csv
import hashlib
import json
import math
import urllib.request
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = HERE / "data"
OUT = HERE / "results"
BASE = "https://zenodo.org/records/15458539/files/{}_FDM_CATALOG_GS.csv?download=1"
FILES = {"KMOS3D": "0159ca6843515607cc6d95007d106ff1d991be78c1af01aea6188d3e0d406e82",
         "KGES": "555be2bd99b38af772200a8ce6ce3957e86ae032343adf117aeb7b7aeb0c4cd2",
         "KROSS": "baad935078610826825506463bf3f296408e07974ef2a6f7f94b85328061b342"}

G = 4.30091e-6
KK = 1e6 / 3.0856775814913673e19
C = 2.99792458e8
THETA0 = 8.8e26
A_PUB = 2 * C * C / THETA0
OM, OL = 0.315, 0.685
RADII = ("Re", "Ropt", "Rout")


def fetch():
    DATA.mkdir(exist_ok=True)
    rows = []
    for survey, sha in FILES.items():
        p = DATA / f"{survey}_FDM_CATALOG_GS.csv"
        if not p.exists():
            req = urllib.request.Request(BASE.format(survey), headers={"User-Agent": "qi-research-archive/1.0 (python-urllib)"})
            p.write_bytes(urllib.request.urlopen(req, timeout=120).read())
        if hashlib.sha256(p.read_bytes()).hexdigest() != sha:
            raise SystemExit(f"checksum mismatch: {p.name}")
        for r in csv.DictReader(p.open()):
            r["survey"] = survey
            rows.append(r)
    return rows


def ln_sigma(val, err):
    """Log-normal width matching a linear value and its 1-sigma error."""
    return math.sqrt(math.log(1 + (err / val) ** 2))


def points(rows):
    """One record per galaxy and radius."""
    P = []
    for gi, r in enumerate(rows):
        z = float(r["Redshift"])
        re_, re_err = float(r["Re"]), float(r["Re_err"])
        for t in RADII:
            R, V, Ve = float(r[t]), float(r["V" + t]), float(r["V" + t + "_err"])
            M, Me = float(r["Mbar_" + t]), float(r["Mbar_" + t + "_err"])
            if not (R > 0 and V > 0 and M > 0):
                continue
            P.append(dict(gal=gi, survey=r["survey"], z=z, radius=t, logmstar=math.log10(float(r["Mstar"])),
                          ln_gobs=math.log(V * V / R * KK), ln_gbar=math.log(G * M / R ** 2 * KK),
                          s_v=Ve / V, s_m=ln_sigma(M, Me), s_r=re_err / re_,
                          re_gt_psf=re_ > float(r["PSF"]), mbar_gt_mdyn=M > float(r["Mdyn_" + t])))
    return P


def arrays(P):
    keys = ("gal", "z", "ln_gobs", "ln_gbar", "s_v", "s_m", "s_r", "logmstar")
    A = {k: np.array([p[k] for p in P]) for k in keys}
    # Eq. 8 slope d ln g / d ln g_bar at the observed point; clipped where g_bar > g_obs (no QI solution).
    A["slope"] = np.clip(0.5 * (1 + np.exp(2 * (A["ln_gbar"] - A["ln_gobs"]))), 0.5, 1.0)
    return A


def E(z):
    return np.sqrt(OM * (1 + z) ** 3 + OL)


LAWS = {"constant": lambda z, g: np.ones_like(z), "one_plus_z": lambda z, g: 1 + z,
        "hubble": lambda z, g: E(z), "power": lambda z, g: (1 + z) ** g}


def nll(A, a_of_z, tau, shift=0.0):
    """Negative log likelihood in ln g_obs. shift: common change of ln M_bar."""
    gb = np.exp(A["ln_gbar"] + shift)
    a = a_of_z(A["z"])
    y = 0.5 * np.log(gb * gb + a * gb)
    s = A["slope"]
    v = (2 * A["s_v"]) ** 2 + (s * A["s_m"]) ** 2 + ((2 * s - 1) * A["s_r"]) ** 2 + tau ** 2
    r = A["ln_gobs"] - y
    return 0.5 * float(np.sum(r * r / v + np.log(v)))


def fit(A, law, amp=None, gamma=None, shift=False):
    """Free: log10 amplitude unless amp given; gamma if law is power and gamma None; tau always; mass shift if asked."""
    def unpack(p):
        i = 0
        la = math.log10(amp) if amp is not None else p[i]
        i += amp is None
        g = gamma if (gamma is not None or law != "power") else p[i]
        i += (gamma is None and law == "power")
        sh = p[i] if shift else 0.0
        i += shift
        return la, g, sh, abs(p[i])

    def obj(p):
        la, g, sh, tau = unpack(p)
        return nll(A, lambda z: 10 ** la * LAWS[law](z, g), tau, sh)
    best = None
    for la0 in ([-10.0, -9.6] if amp is None else [None]):
        x0 = ([la0] if amp is None else []) + ([1.0] if (gamma is None and law == "power") else []) + ([0.0] if shift else []) + [0.2]
        r = minimize(obj, x0, method="Nelder-Mead", options=dict(xatol=1e-6, fatol=1e-8, maxiter=6000))
        if best is None or r.fun < best.fun:
            best = r
    la, g, sh, tau = unpack(best.x)
    return float(best.fun), dict(log_A=la, gamma=g if law == "power" else None, shift_ln=sh, tau=tau)


def models(A, a1, a1b):
    out = {"published": fit(A, "one_plus_z", amp=A_PUB),
           "published_mass_shift": fit(A, "one_plus_z", amp=A_PUB, shift=True)}
    if a1:
        out["calibrated_a1"] = fit(A, "one_plus_z", amp=a1)
    if a1b:
        out["calibrated_a1b"] = fit(A, "one_plus_z", amp=a1b)
    out.update(one_plus_z=fit(A, "one_plus_z"), constant=fit(A, "constant"), hubble=fit(A, "hubble"), power=fit(A, "power"))
    ref = out["constant"][0]
    return {k: dict(nll=v[0], dnll_vs_constant=v[0] - ref, **v[1]) for k, v in out.items()}


def scale_interval(A):
    """Constant QI scale with a 1-sigma profile interval (delta nll = 0.5, tau profiled)."""
    f0, p = fit(A, "constant")
    grid = np.linspace(p["log_A"] - 1.2, p["log_A"] + 1.2, 121)
    prof = []
    for la in grid:
        prof.append(min(nll(A, lambda z, la=la: 10 ** la * np.ones_like(z), t) for t in np.linspace(0, 1.0, 51)))
    prof = np.array(prof)
    ok = grid[prof - prof.min() <= 0.5]
    return dict(log_A=p["log_A"], lo=float(ok.min()), hi=float(ok.max()), n=int(len(A["z"])), z_med=float(np.median(A["z"])))


def subset(A, mask):
    return {k: v[mask] for k, v in A.items()}


def boot(A, nb, rng):
    gal = np.unique(A["gal"])
    idx = {g: np.where(A["gal"] == g)[0] for g in gal}
    gs, d1 = [], []
    for _ in range(nb):
        pick = rng.choice(gal, len(gal), replace=True)
        ii = np.concatenate([idx[g] for g in pick])
        B = subset(A, ii)
        gs.append(fit(B, "power")[1]["gamma"])
        d1.append(fit(B, "one_plus_z")[0] - fit(B, "constant")[0])
    gs, d1 = np.array(gs), np.array(d1)
    return dict(n=nb, gamma_16_50_84=np.percentile(gs, [16, 50, 84]).tolist(), gamma_2p5_97p5=np.percentile(gs, [2.5, 97.5]).tolist(),
                frac_gamma_ge_1=float(np.mean(gs >= 1)), dnll_one_plus_z_16_50_84=np.percentile(d1, [16, 50, 84]).tolist(),
                frac_one_plus_z_better=float(np.mean(d1 < 0)))


def tf_offsets(rows):
    """McCulloch 2017 Eq. 13: M = v^4 Theta_now / (2 G c^2 (1+z)) with v = V(R_out). Offset = log M_obs - log M_QI."""
    out = []
    for r in rows:
        z, V = float(r["Redshift"]), float(r["VRout"])
        m_qi = (V * 1e3) ** 4 * THETA0 / (2 * 6.674e-11 * C * C * (1 + z)) / 1.989e30
        out.append(dict(survey=r["survey"], z=z, total=math.log10(float(r["Mbar"])) - math.log10(m_qi),
                        within_rout=math.log10(float(r["Mbar_Rout"])) - math.log10(m_qi)))
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


STYLE = """<style>
svg { --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --grid:#e4e3df; --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; --s4:#eda100; }
@media (prefers-color-scheme: dark) { svg { --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --grid:#33322f; --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500; } }
text { font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: var(--ink2); font-size: 12px; }
.t { fill: var(--ink); font-size: 14px; font-weight: 600; }
</style>"""
SURVEY_COLOR = {"KROSS": "var(--s1)", "KMOS3D": "var(--s3)", "KGES": "var(--s4)"}


def fig(res, path):
    w, h, ml, mr, mt, mb = 760, 500, 64, 20, 44, 50
    xr, yr = (0.5, 2.6), (0, 7)
    X = lambda v: ml + (v - xr[0]) / (xr[1] - xr[0]) * (w - ml - mr)
    Y = lambda v: h - mb - (v - yr[0]) / (yr[1] - yr[0]) * (h - mt - mb)
    el = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">',
          "<title>QI scale fitted to Sharma et al. 2025 discs at the outer radius</title>", STYLE,
          f'<rect width="{w}" height="{h}" fill="var(--surface)"/>',
          f'<text class="t" x="{ml}" y="24">QI scale at R_out, halo-independent baryons (Sharma et al. 2025)</text>',
          f'<text x="{(ml + w - mr) / 2}" y="{h - 12}" text-anchor="middle">redshift z</text>',
          f'<text transform="translate(16,{(mt + h - mb) / 2}) rotate(-90)" text-anchor="middle">a_Q (10⁻¹⁰ m s⁻²)</text>']
    for v in (0.5, 1.0, 1.5, 2.0, 2.5):
        el.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{mt}" y2="{h - mb}" stroke="var(--grid)"/><text x="{X(v):.1f}" y="{h - mb + 16}" text-anchor="middle">{v}</text>')
    for v in range(0, 8):
        el.append(f'<line x1="{ml}" x2="{w - mr}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="var(--grid)"/><text x="{ml - 6}" y="{Y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    zz = np.linspace(xr[0], xr[1], 50)
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(a):.1f},{Y(A_PUB * (1 + a) * 1e10):.1f}" for i, a in enumerate(zz))
    el.append(f'<path d="{d}" fill="none" stroke="var(--s2)" stroke-width="2"><title>QI published 2c²(1+z)/Θ₀</title></path>')
    for b in res["bins_by_survey"]:
        v, lo, hi = (10 ** b[k] * 1e10 for k in ("log_A", "lo", "hi"))
        col = SURVEY_COLOR[b["survey"]]
        el.append(f'<line x1="{X(b["z_med"]):.1f}" x2="{X(b["z_med"]):.1f}" y1="{Y(lo):.1f}" y2="{Y(min(hi, 7)):.1f}" stroke="{col}" stroke-width="2"/>'
                  f'<circle cx="{X(b["z_med"]):.1f}" cy="{Y(v):.1f}" r="5" fill="{col}" stroke="var(--surface)" stroke-width="2">'
                  f'<title>{b["survey"]}, {b["n"]} galaxies, z̃ = {b["z_med"]:.2f}: a_Q = {v:.2f}</title></circle>')
    items = [("QI published: 2c²(1+z)/Θ₀", "var(--s2)")] + [(s, c) for s, c in SURVEY_COLOR.items()]
    for i, (lab, col) in enumerate(items):
        y = 62 + 18 * i
        el.append(f'<line x1="80" x2="104" y1="{y}" y2="{y}" stroke="{col}" stroke-width="3"/><text x="110" y="{y + 4}">{lab}</text>')
    path.write_text("\n".join(el + ["</svg>"]) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=400)
    ap.add_argument("--seed", type=int, default=20261023)
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    rows = fetch()
    P = points(rows)
    a1, a1b = a1_scales()
    rng = np.random.default_rng(args.seed)
    sel = {
        "rout_all": lambda p: p["radius"] == "Rout",
        "rout_kmos3d": lambda p: p["radius"] == "Rout" and p["survey"] == "KMOS3D",
        "ropt_all": lambda p: p["radius"] == "Ropt",
        "re_resolved": lambda p: p["radius"] == "Re" and p["re_gt_psf"],
        "all_radii": lambda p: True,
        "rout_mbar_le_mdyn": lambda p: p["radius"] == "Rout" and not p["mbar_gt_mdyn"],
    }
    labels = {"rout_all": "R_out, all surveys (main)", "rout_kmos3d": "R_out, KMOS3D only (single survey, z = 0.7–2.4)",
              "ropt_all": "R_opt, all surveys", "re_resolved": "R_e, galaxies with R_e > PSF",
              "all_radii": "all three radii (galaxy bootstrap keeps radii together)",
              "rout_mbar_le_mdyn": "R_out, excluding galaxies with M_bar > M_dyn (biased; illustration only)"}
    res = dict(inputs=dict(zenodo="10.5281/zenodo.15458539", sha256=FILES, n_galaxies=len(rows), a1=a1, a1b=a1b,
                           frac_mbar_gt_mdyn={t: float(np.mean([p["mbar_gt_mdyn"] for p in P if p["radius"] == t])) for t in RADII}),
               samples={})
    for name, f in sel.items():
        Psub = [p for p in P if f(p)]
        A = arrays(Psub)
        e = dict(label=labels[name], n_points=len(Psub), n_galaxies=int(len(np.unique(A["gal"]))), models=models(A, a1, a1b))
        if name in ("rout_all", "rout_kmos3d", "all_radii"):
            e["bootstrap"] = boot(A, args.boot, rng)
        res["samples"][name] = e
    # Redshift bins (R_out) per survey; KMOS3D split into three redshift bins.
    bins = []
    for survey in ("KROSS", "KGES", "KMOS3D"):
        Ps = [p for p in P if p["radius"] == "Rout" and p["survey"] == survey]
        zs = np.array([p["z"] for p in Ps])
        edges = np.quantile(zs, [0, 1 / 3, 2 / 3, 1]) if survey == "KMOS3D" else np.array([zs.min(), zs.max()])
        for i in range(len(edges) - 1):
            m = (zs >= edges[i]) & ((zs < edges[i + 1]) if i < len(edges) - 2 else (zs <= edges[i + 1]))
            b = scale_interval(arrays([p for p, k in zip(Ps, m) if k]))
            b.update(survey=survey, published=A_PUB * (1 + b["z_med"]))
            bins.append(b)
    res["bins_by_survey"] = bins
    # Stellar-mass dependence within each survey (QI predicts none).
    mass = []
    for survey in ("KROSS", "KMOS3D"):
        Ps = [p for p in P if p["radius"] == "Rout" and p["survey"] == survey]
        med = float(np.median([p["logmstar"] for p in Ps]))
        lo = scale_interval(arrays([p for p in Ps if p["logmstar"] < med]))
        hi = scale_interval(arrays([p for p in Ps if p["logmstar"] >= med]))
        mass.append(dict(survey=survey, split_logmstar=med, low=lo, high=hi))
    res["mass_dependence"] = mass
    tf = tf_offsets(rows)
    res["tully_fisher_eq13"] = {s: dict(n=len([t for t in tf if t["survey"] == s]),
                                        median_total=float(np.median([t["total"] for t in tf if t["survey"] == s])),
                                        median_within_rout=float(np.median([t["within_rout"] for t in tf if t["survey"] == s])),
                                        median_z=float(np.median([t["z"] for t in tf if t["survey"] == s])))
                                for s in ("KROSS", "KGES", "KMOS3D")}
    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False, allow_nan=False) + "\n")
    fig(res, OUT / "fig-1-aq-by-survey.svg")
    (OUT / "summary.md").write_text(summary(res))
    print((OUT / "summary.md").read_text())


NAMES = {"published": "QI published, a_Q = 2c²(1+z)/Θ₀ (τ)", "published_mass_shift": "QI published + common M_bar shift (shift, τ)",
         "calibrated_a1": "QI (1+z), A1 SPARC amplitude (τ)", "calibrated_a1b": "QI (1+z), A1b SPARC amplitude (τ)",
         "one_plus_z": "QI (1+z), amplitude fitted (A, τ)", "constant": "QI, constant scale (A, τ)",
         "hubble": "QI, scale ∝ H(z) (A, τ)", "power": "QI, (1+z)^γ (A, γ, τ)"}


def summary(r):
    i = r["inputs"]
    L = ["# A6e results (generated by sharma_qi.py; do not edit)", "",
         "Editorial analysis. Residuals in ln g_obs against McCulloch 2017 Eq. 8 with first-order error propagation. "
         "Δ(−ln L) values are conditional on this approximate likelihood; bootstrap fractions are not p-values.", "",
         f"{i['n_galaxies']} galaxies. Fraction with M_bar(<R) > M_dyn(<R), which no QI scale can fit: " +
         ", ".join(f"{k} {v:.2f}" for k, v in i["frac_mbar_gt_mdyn"].items()) + ".", ""]
    for name, e in r["samples"].items():
        L += [f"## {e['label']} ({e['n_galaxies']} galaxies, {e['n_points']} points)", "",
              "| Model | Δ(−ln L) vs constant | a_Q(0) (10⁻¹⁰ m s⁻²) | γ | M_bar shift (dex) | τ (ln) |", "|---|---|---|---|---|---|"]
        for k, m in e["models"].items():
            g = "—" if m["gamma"] is None else f"{m['gamma']:.2f}"
            L.append(f"| {NAMES[k]} | {m['dnll_vs_constant']:+.2f} | {10 ** m['log_A'] * 1e10:.3f} | {g} | "
                     f"{m['shift_ln'] / math.log(10):+.2f} | {m['tau']:.3f} |")
        if "bootstrap" in e:
            b = e["bootstrap"]
            L += ["", f"Galaxy bootstrap ({b['n']}): γ 16/50/84% = " + ", ".join(f"{x:.2f}" for x in b["gamma_16_50_84"]) +
                  f"; 2.5–97.5% = {b['gamma_2p5_97p5'][0]:.2f} to {b['gamma_2p5_97p5'][1]:.2f}; fraction γ ≥ 1 = {b['frac_gamma_ge_1']:.3f}. "
                  "Δ(−ln L)[(1+z) − constant] 16/50/84% = " + ", ".join(f"{x:+.2f}" for x in b["dnll_one_plus_z_16_50_84"]) +
                  f"; (1+z) better in {b['frac_one_plus_z_better']:.3f}."]
        L.append("")
    L += ["## Constant QI scale by survey and redshift (R_out; 1σ profile interval)", "",
          "| Survey | N | z̃ | a_Q (10⁻¹⁰ m s⁻²) | published 2c²(1+z̃)/Θ₀ |", "|---|---|---|---|---|"]
    for b in r["bins_by_survey"]:
        L.append(f"| {b['survey']} | {b['n']} | {b['z_med']:.2f} | {10 ** b['log_A'] * 1e10:.2f} ({10 ** b['lo'] * 1e10:.2f}–{10 ** b['hi'] * 1e10:.2f}) | {b['published'] * 1e10:.2f} |")
    L += ["", "## Stellar-mass dependence within a survey (R_out; QI predicts none)", "",
          "| Survey | split log M★ | a_Q, lower half | a_Q, upper half |", "|---|---|---|---|"]
    for m in r["mass_dependence"]:
        lo, hi = m["low"], m["high"]
        L.append(f"| {m['survey']} | {m['split_logmstar']:.2f} | {10 ** lo['log_A'] * 1e10:.2f} ({10 ** lo['lo'] * 1e10:.2f}–{10 ** lo['hi'] * 1e10:.2f}) | "
                 f"{10 ** hi['log_A'] * 1e10:.2f} ({10 ** hi['lo'] * 1e10:.2f}–{10 ** hi['hi'] * 1e10:.2f}) |")
    L += ["", "## McCulloch 2017 Eq. 13 Tully–Fisher offsets: log M_bar(observed) − log M(QI from V_out) (QI predicts 0 in the deep limit)", "",
          "| Survey | N | z̃ | median, total M_bar | median, M_bar within R_out |", "|---|---|---|---|---|"]
    for s, t in r["tully_fisher_eq13"].items():
        L.append(f"| {s} | {t['n']} | {t['median_z']:.2f} | {t['median_total']:+.2f} | {t['median_within_rout']:+.2f} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
