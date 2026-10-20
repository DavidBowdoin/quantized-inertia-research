#!/usr/bin/env python3
"""A1: fixed-Θ refit of the SPARC radial acceleration relation (QI vs MOND).

Stdlib only. Run from the repository root:

    python3 -I 09-analysis/a1-sparc-rar-refit/rar_refit.py            # full run (bootstrap 200)
    python3 -I 09-analysis/a1-sparc-rar-refit/rar_refit.py --boot 0   # no bootstrap (fast)

Downloads the SPARC tables into ./data/ (git-ignored; no redistribution licence),
labels each of the 2693 RAR points of Lelli et al. (2017) with its galaxy, fits every
model by maximum likelihood with errors on both axes plus a free intrinsic scatter,
bootstraps over galaxies, and writes results/results.json, results/summary.md and
results/fig-*.svg.
"""
import argparse
import hashlib
import json
import math
import multiprocessing as mp
import random
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE / "results"
BASE_URL = "https://astroweb.case.edu/SPARC/"
FILES = ["RAR.mrt", "RARbins.mrt", "SPARC_Lelli2016c.mrt", "MassModels_Lelli2016c.mrt"]

C = 2.99792458e8          # m/s
KPC = 3.085677581e19      # m
LN10 = math.log(10)

# ---------------------------------------------------------------- data


def fetch():
    DATA.mkdir(exist_ok=True)
    sums = {}
    for f in FILES:
        p = DATA / f
        if not p.exists():
            req = urllib.request.Request(BASE_URL + f, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                p.write_bytes(r.read())
        sums[f] = hashlib.sha256(p.read_bytes()).hexdigest()
    return sums


def read_galaxies():
    gal = {}
    for line in (DATA / "SPARC_Lelli2016c.mrt").read_text().splitlines():
        p = line.split()
        if len(line) > 100 and len(p) >= 18 and p[1].isdigit():
            gal[p[0]] = dict(D=float(p[2]), inc=float(p[5]), Q=int(p[17]))
    return gal


def read_mass_models(gal):
    rows = []
    for line in (DATA / "MassModels_Lelli2016c.mrt").read_text().splitlines():
        p = line.split()
        if len(p) == 10 and p[0] in gal:
            try:
                D, R, V, eV, Vg, Vd, Vb = map(float, p[1:8])
            except ValueError:
                continue
            rows.append(dict(gal=p[0], R=R, V=V, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb))
    return rows


def gbar_of(r, ud=0.5, ub=0.7):
    """Baryonic acceleration (m/s^2) for disk/bulge mass-to-light ratios ud, ub at 3.6 um."""
    v2 = abs(r["Vg"]) * r["Vg"] + ud * abs(r["Vd"]) * r["Vd"] + ub * abs(r["Vb"]) * r["Vb"]
    return v2 * 1e6 / (r["R"] * KPC)


def read_rar():
    pts = []
    for line in (DATA / "RAR.mrt").read_text().splitlines():
        p = line.split()
        if len(p) == 4 and line.strip()[0] in "-0123456789":
            try:
                pts.append(tuple(map(float, p)))
            except ValueError:
                pass
    return pts


def label_rar(rar, gal, mm):
    """Attach galaxy name + mass-model components to each RAR.mrt row.

    RAR.mrt has no galaxy column. Rebuilding it from the mass models with the cuts of
    Lelli et al. 2017 (Q < 3, i >= 30 deg, dV/V <= 10%, Y_disk 0.5, Y_bul 0.7) gives
    2700 points; RAR.mrt lists galaxies in reverse name order, so a banded DP alignment
    recovers the mapping (unmatched rebuilt points are dropped).
    """
    seq = []
    for r in mm:
        g = gal[r["gal"]]
        if g["Q"] == 3 or g["inc"] < 30 or r["R"] <= 0 or r["V"] <= 0 or r["eV"] / r["V"] > 0.1:
            continue
        gb = gbar_of(r)
        if gb <= 0:
            continue
        r = dict(r, x=round(math.log10(gb), 2), y=round(math.log10((r["V"] * 1e3) ** 2 / (r["R"] * KPC)), 2))
        seq.append(r)
    order = {n: i for i, n in enumerate(sorted({r["gal"] for r in seq}, reverse=True))}
    seq.sort(key=lambda r: order[r["gal"]])  # stable: keeps radius order within a galaxy
    n, m, band, gap, inf = len(seq), len(rar), 40, 1.5, float("inf")

    def cost(i, j):
        d = max(abs(seq[i]["x"] - rar[j][0]), abs(seq[i]["y"] - rar[j][2]))
        return 0.0 if d <= 0.011 else 1.0 + d

    dp = [dict() for _ in range(n + 1)]
    dp[0][0] = (0.0, None)
    for i in range(n):
        for j, (c, _) in list(dp[i].items()):
            if c + gap < dp[i + 1].get(j, (inf,))[0]:
                dp[i + 1][j] = (c + gap, "skip")
            if j < m and abs(i - j) <= band and c + cost(i, j) < dp[i + 1].get(j + 1, (inf,))[0]:
                dp[i + 1][j + 1] = (c + cost(i, j), "match")
    if m not in dp[n]:
        raise SystemExit("alignment failed: RAR.mrt does not match the rebuilt sample")
    i, j, out, stats = n, m, [None] * m, {"exact": 0, "approx": 0, "dropped": 0, "max_dex": 0.0}
    while i > 0:
        if dp[i][j][1] == "match":
            i, j = i - 1, j - 1
            d = max(abs(seq[i]["x"] - rar[j][0]), abs(seq[i]["y"] - rar[j][2]))
            stats["exact" if d <= 0.011 else "approx"] += 1
            stats["max_dex"] = max(stats["max_dex"], round(d, 3))
            out[j] = dict(seq[i], x=rar[j][0], ex=rar[j][1], y=rar[j][2], ey=rar[j][3])
        else:
            i -= 1
            stats["dropped"] += 1
    stats["rebuilt"] = n
    return out, stats

# ---------------------------------------------------------------- models
# Each model gives g_obs = g_bar * nu(g_bar / a). y = g_bar / a.


def nu_newton(y):
    return 1.0


def nu_qi(y):            # McCulloch 2017 Eq. 8, a = 2c^2/Theta
    return math.sqrt(1.0 + 1.0 / y)


def nu_simple(y):        # MOND "simple" interpolation, mu = x/(1+x)
    return 0.5 + math.sqrt(0.25 + 1.0 / y)


def nu_standard(y):      # MOND "standard" interpolation, mu = x/sqrt(1+x^2)
    return math.sqrt(0.5 + math.sqrt(0.25 + 1.0 / (y * y)))


def nu_rar(y):           # McGaugh et al. 2016 empirical RAR fit
    return 1.0 / (1.0 - math.exp(-math.sqrt(y)))


def theta_to_a(theta):
    return 2 * C * C / theta


THETA_EARLY = 2.6e26     # 2007-2013 papers ("2.6 x 10^26 m" as quoted in McCulloch 2017)
THETA_LATE = 8.8e26      # 2017 onward (present co-moving diameter)

# key, label, nu, fixed log10(a) or None (free), colour slot
MODELS = [
    ("newton", "Newton (baryons only)", nu_newton, 0.0, None),
    ("qi_early", "QI, Θ = 2.6 × 10²⁶ m (fixed)", nu_qi, math.log10(theta_to_a(THETA_EARLY)), 1),
    ("qi_late", "QI, Θ = 8.8 × 10²⁶ m (fixed)", nu_qi, math.log10(theta_to_a(THETA_LATE)), 2),
    ("qi_free", "QI, Θ free", nu_qi, None, 3),
    ("mond_simple", "MOND simple μ, a₀ free", nu_simple, None, 4),
    ("mond_standard", "MOND standard μ, a₀ free", nu_standard, None, 5),
    ("rar_exp", "McGaugh 2016 RAR fit, a₀ free (reference)", nu_rar, None, 7),
]
MODEL = {m[0]: m for m in MODELS}


def predict(nu, la, x):
    """log10 g_obs predicted at log10 g_bar = x, and its slope d/dx (numerical)."""
    def f(xx):
        return xx + math.log10(nu(10 ** (xx - la)))
    h = 1e-4
    return f(x), (f(x + h) - f(x - h)) / (2 * h)

# ---------------------------------------------------------------- likelihood


def m2lnl(res, var0, s2):
    """-2 ln L for residuals res with base variances var0 and intrinsic variance s2."""
    t = 0.0
    for r, v in zip(res, var0):
        v += s2
        t += r * r / v + math.log(v)
    return t + len(res) * math.log(2 * math.pi)


def golden(f, lo, hi, tol=1e-4):
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = f(c), f(d)
    while b - a > tol:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a)
            fd = f(d)
    x = (a + b) / 2
    return x, f(x)


def profile(nu, la, pts):
    """For fixed log a: best intrinsic scatter and -2lnL. Also chi2 with no intrinsic scatter."""
    res, var0 = [], []
    for p in pts:
        yp, s = predict(nu, la, p["x"])
        res.append(p["y"] - yp)
        var0.append(p["ey"] ** 2 + (s * p["ex"]) ** 2)
    sig, val = golden(lambda s: m2lnl(res, var0, s * s), 0.0, 1.5, 1e-4)
    chi2 = sum(r * r / v for r, v in zip(res, var0))
    return dict(m2lnl=val, sig_int=sig, chi2=chi2, res=res)


def fit(key, pts, la_range=(-11.0, -8.5)):
    _, _, nu, fixed, _ = MODEL[key]
    if fixed is not None or key == "newton":
        la, pr = fixed, profile(nu, fixed, pts)
        k = 1
    else:
        la, _ = golden(lambda v: profile(nu, v, pts)["m2lnl"], *la_range, tol=2e-4)
        pr = profile(nu, la, pts)
        k = 2
    n = len(pts)
    return dict(model=key, log_a=la, a=10 ** la, k=k, n=n, m2lnl=pr["m2lnl"], sig_int=pr["sig_int"],
                chi2=pr["chi2"], chi2_red=pr["chi2"] / (n - (k - 1)),
                rms=math.sqrt(sum(r * r for r in pr["res"]) / n),
                aic=pr["m2lnl"] + 2 * k, bic=pr["m2lnl"] + k * math.log(n), res=pr["res"])


def fit_all(pts, keys=None):
    out = {}
    for key in keys or MODEL:
        out[key] = fit(key, pts)
    return out


def with_upsilon(pts, ud):
    return [dict(p, x=math.log10(gbar_of(p, ud, 1.4 * ud))) for p in pts]


def fit_upsilon(key, pts, lo=0.15, hi=1.0):
    """Same model with one global disk mass-to-light ratio fitted too (flat prior, Y_bul = 1.4 Y_disk)."""
    ud, _ = golden(lambda u: fit(key, with_upsilon(pts, u))["m2lnl"], lo, hi, tol=2e-3)
    f = fit(key, with_upsilon(pts, ud))
    f["k"] += 1
    f["aic"] = f["m2lnl"] + 2 * f["k"]
    f["bic"] = f["m2lnl"] + f["k"] * math.log(f["n"])
    f["upsilon_disk"] = ud
    return f


def boot_rep(args):
    seed, pts, keys = args
    rng = random.Random(seed)
    by = {}
    for p in pts:
        by.setdefault(p["gal"], []).append(p)
    names = sorted(by)
    sample = [p for _ in names for p in by[rng.choice(names)]]
    fits = fit_all(sample, keys)
    return {k: dict(log_a=v["log_a"], m2lnl=v["m2lnl"], sig_int=v["sig_int"], bic=v["bic"]) for k, v in fits.items()}

# ---------------------------------------------------------------- SVG figures


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


class Plot:
    def __init__(self, w, h, xr, yr, title, xlabel, ylabel, ml=64, mr=20, mt=44, mb=50):
        self.w, self.h, self.xr, self.yr = w, h, xr, yr
        self.l, self.r, self.t, self.b = ml, w - mr, mt, h - mb
        self.el = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">',
                   f"<title>{title}</title>", STYLE, f'<rect width="{w}" height="{h}" fill="var(--surface)"/>',
                   f'<text class="t" x="{ml}" y="24">{title}</text>',
                   f'<text x="{(self.l + self.r) / 2}" y="{h - 12}" text-anchor="middle">{xlabel}</text>',
                   f'<text transform="translate(16,{(self.t + self.b) / 2}) rotate(-90)" text-anchor="middle">{ylabel}</text>']

    def X(self, v):
        return self.l + (v - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.r - self.l)

    def Y(self, v):
        return self.b - (v - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.b - self.t)

    def axes(self, xt, yt, fmt=lambda v: f"{v:g}"):
        for v in xt:
            self.el.append(f'<line class="gr" x1="{self.X(v):.1f}" x2="{self.X(v):.1f}" y1="{self.t}" y2="{self.b}"/>'
                           f'<text x="{self.X(v):.1f}" y="{self.b + 16}" text-anchor="middle">{fmt(v)}</text>')
        for v in yt:
            self.el.append(f'<line class="gr" x1="{self.l}" x2="{self.r}" y1="{self.Y(v):.1f}" y2="{self.Y(v):.1f}"/>'
                           f'<text x="{self.l - 6}" y="{self.Y(v) + 4:.1f}" text-anchor="end">{fmt(v)}</text>')
        self.el.append(f'<line class="ax" x1="{self.l}" x2="{self.r}" y1="{self.b}" y2="{self.b}"/>'
                       f'<line class="ax" x1="{self.l}" x2="{self.l}" y1="{self.t}" y2="{self.b}"/>')

    def line(self, xs, ys, color, dash=None, tip=None):
        d = " ".join(f"{'M' if i == 0 else 'L'}{self.X(x):.1f},{self.Y(y):.1f}" for i, (x, y) in enumerate(zip(xs, ys)))
        da = f' stroke-dasharray="{dash}"' if dash else ""
        tt = f"<title>{tip}</title>" if tip else ""
        self.el.append(f'<path class="ln" d="{d}" stroke="{color}"{da}>{tt}</path>')

    def points(self, xs, ys, color, r=1.6, op=0.35):
        self.el.append(f'<g fill="{color}" fill-opacity="{op}">' + "".join(
            f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="{r}"/>' for x, y in zip(xs, ys)) + "</g>")

    def marker(self, x, y, color, tip):
        self.el.append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="5" fill="{color}" stroke="var(--surface)" '
                       f'stroke-width="2"><title>{tip}</title></circle>')

    def text(self, x, y, s, anchor="start", cls=""):
        c = f' class="{cls}"' if cls else ""
        self.el.append(f'<text{c} x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}">{s}</text>')

    def legend(self, items, x, y):
        for i, (label, color, dash) in enumerate(items):
            yy = y + i * 18
            da = f' stroke-dasharray="{dash}"' if dash else ""
            self.el.append(f'<line x1="{x}" x2="{x + 24}" y1="{yy}" y2="{yy}" stroke="{color}" stroke-width="2"{da}/>')
            self.text(x + 30, yy + 4, label)

    def save(self, path):
        path.write_text("\n".join(self.el + ["</svg>"]) + "\n")


def curve(key, la, xs):
    return [predict(MODEL[key][2], la, x)[0] for x in xs]


def color(key):
    slot = MODEL[key][4]
    return f"var(--s{slot})" if slot else "var(--ink2)"


def fig_rar(pts, fits, path):
    p = Plot(760, 560, (-12.3, -8.4), (-12.3, -8.4), f"SPARC radial acceleration relation: {len(pts):,} points, {len({q['gal'] for q in pts})} galaxies",
             "log₁₀ g_bar  (m s⁻²)", "log₁₀ g_obs  (m s⁻²)")
    p.axes([-12, -11, -10, -9], [-12, -11, -10, -9])
    p.points([q["x"] for q in pts], [q["y"] for q in pts], "var(--pt)")
    xs = [-12.3 + i * 0.02 for i in range(196)]
    p.line(xs, xs, "var(--ink2)", "4 4", "Newton: g_obs = g_bar")
    for k in ("qi_early", "qi_late", "mond_simple"):
        p.line(xs, curve(k, fits[k]["log_a"], xs), color(k), tip=MODEL[k][1])
    p.legend([("Newton (baryons only)", "var(--ink2)", "4 4")] +
             [(MODEL[k][1] if k != "mond_simple" else f"MOND simple μ, best fit a₀ = {fits[k]['a'] * 1e10:.2f} × 10⁻¹⁰", color(k), None)
              for k in ("qi_early", "qi_late", "mond_simple")], 360, 440)
    p.save(path)


def binned(pts, res, edges):
    out = []
    for lo, hi in zip(edges, edges[1:]):
        rs = [r for q, r in zip(pts, res) if lo <= q["x"] < hi]
        if len(rs) >= 20:
            mu = sum(rs) / len(rs)
            sd = math.sqrt(sum((r - mu) ** 2 for r in rs) / (len(rs) - 1))
            out.append(((lo + hi) / 2, mu, sd / math.sqrt(len(rs)), len(rs)))
    return out


def fig_residuals(pts, fits, path, keys, title):
    edges = [-12.4 + 0.2 * i for i in range(20)]
    p = Plot(760, 400, (-12.2, -8.6), (-0.45, 0.25), title, "log₁₀ g_bar  (m s⁻²)",
             "mean residual, log₁₀ (g_obs / g_model)  (dex)")
    p.axes([-12, -11, -10, -9], [-0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2], fmt=lambda v: f"{v:+.1f}" if v else "0")
    p.el.append(f'<line class="ax" x1="{p.l}" x2="{p.r}" y1="{p.Y(0):.1f}" y2="{p.Y(0):.1f}"/>')
    for k in keys:
        b = binned(pts, fits[k]["res"], edges)
        p.line([v[0] for v in b], [v[1] for v in b], color(k), tip=MODEL[k][1])
        for xb, mu, se, nb in b:
            p.marker(xb, mu, color(k), f"{MODEL[k][1]}: {mu:+.3f} ± {se:.3f} dex (n = {nb})")
    p.legend([(MODEL[k][1], color(k), None) for k in keys], 440, 340 - 18 * (len(keys) - 1))
    p.save(path)


def fig_theta(pts, best, path):
    lt = sorted({round(26.0 + 0.02 * i, 3) for i in range(76)} |
          {round(math.log10(2 * C * C / best['a']) + 0.002 * i, 4) for i in range(-40, 41)})
    lo = best["m2lnl"]
    d = [profile(nu_qi, math.log10(theta_to_a(10 ** v)), pts)["m2lnl"] - lo for v in lt]
    top = math.ceil(math.log10(1 + max(d)))
    p = Plot(760, 400, (26.0, 27.5), (0, top), "QI: how the fit depends on Θ",
             "log₁₀ Θ  (m)", "Δ(−2 ln L) from the best-fit Θ")
    p.axes([26.0, 26.25, 26.5, 26.75, 27.0, 27.25, 27.5], [])
    for dv in [0] + [10 ** i for i in range(top)]:
        y = p.Y(math.log10(1 + dv))
        p.el.append(f'<line class="gr" x1="{p.l}" x2="{p.r}" y1="{y:.1f}" y2="{y:.1f}"/>'
                    f'<text x="{p.l - 6}" y="{y + 4:.1f}" text-anchor="end">{dv:,}</text>')
    p.line(lt, [math.log10(1 + v) for v in d], "var(--s3)", tip="profile likelihood, QI with Θ free")
    for th, k in ((THETA_EARLY, "qi_early"), (THETA_LATE, "qi_late")):
        v = math.log10(th)
        dv = profile(nu_qi, math.log10(theta_to_a(th)), pts)["m2lnl"] - lo
        p.marker(v, math.log10(1 + dv), color(k), f"{MODEL[k][1]}: Δ(−2 ln L) = {dv:.0f}")
        p.text(p.X(v) + 10, p.Y(math.log10(1 + dv)) + 4, f"Θ = {th / 1e26:.1f} × 10²⁶ m: +{dv:,.0f}")
    bt = 2 * C * C / best["a"]
    p.marker(math.log10(bt), 0, color("qi_free"), f"best fit Θ = {bt:.3g} m")
    p.text(p.X(math.log10(bt)), p.Y(0) - 12, f"best Θ = {bt / 1e27:.2f} × 10²⁷ m", "middle")
    p.save(path)


# ---------------------------------------------------------------- main


def fmt_a(a):
    return f"{a * 1e10:.3f} × 10⁻¹⁰"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=200, help="galaxy bootstrap replicates (0 to skip)")
    ap.add_argument("--seed", type=int, default=20261019)
    ap.add_argument("--procs", type=int, default=max(1, (mp.cpu_count() or 2) - 1))
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)

    sums = fetch()
    gal = read_galaxies()
    mm = read_mass_models(gal)
    rar = read_rar()
    pts, align = label_rar(rar, gal, mm)
    ngal = len({p["gal"] for p in pts})
    print(f"RAR points {len(pts)}, galaxies {ngal}; alignment {align}")

    fits = fit_all(pts)
    for k, f in fits.items():
        print(f"{k:14s} a={fmt_a(f['a'])} sig={f['sig_int']:.4f} -2lnL={f['m2lnl']:9.2f} BIC={f['bic']:9.2f} "
              f"chi2/dof={f['chi2_red']:.3f} rms={f['rms']:.4f}")

    # stellar mass-to-light systematics: rebuild g_bar from the components
    upsilon = {}
    for ud in (0.4, 0.5, 0.6):
        fv = fit_all(with_upsilon(pts, ud))
        upsilon[f"{ud:.1f}"] = {k: dict(log_a=v["log_a"], a=v["a"], sig_int=v["sig_int"], m2lnl=v["m2lnl"], bic=v["bic"])
                                for k, v in fv.items()}
        print("Y_disk", ud, {k: round(v["bic"] - fv["mond_simple"]["bic"], 1) for k, v in fv.items()})

    # global Y_disk fitted alongside every model (Newton excluded: it runs to the bound)
    ufree = {}
    for k in MODEL:
        if k == "newton":
            continue
        f = fit_upsilon(k, pts)
        ufree[k] = {kk: f[kk] for kk in ("upsilon_disk", "log_a", "a", "k", "m2lnl", "sig_int", "rms", "aic", "bic")}
        print(f"Y free {k:14s} Y_disk={f['upsilon_disk']:.3f} a={fmt_a(f['a'])} sig={f['sig_int']:.4f} BIC={f['bic']:.1f}")

    boot = []
    if args.boot:
        rng = random.Random(args.seed)
        jobs = [(rng.randrange(2 ** 31), pts, None) for _ in range(args.boot)]
        with mp.Pool(args.procs) as pool:
            for i, r in enumerate(pool.imap(boot_rep, jobs), 1):
                boot.append(r)
                if i % 20 == 0:
                    print(f"bootstrap {i}/{args.boot}")

    def pct(vals, q):
        s = sorted(vals)
        return s[min(len(s) - 1, max(0, int(round(q * (len(s) - 1)))))]

    ref = "mond_simple"
    summary = {}
    for k, f in fits.items():
        e = {kk: f[kk] for kk in ("log_a", "a", "k", "n", "m2lnl", "sig_int", "chi2", "chi2_red", "rms", "aic", "bic")}
        e["label"] = MODEL[k][1]
        e["theta_equiv_m"] = 2 * C * C / f["a"] if k != "newton" else None
        e["dbic_vs_mond_simple"] = f["bic"] - fits[ref]["bic"]
        e["dbic_vs_qi_free"] = f["bic"] - fits["qi_free"]["bic"]
        if boot:
            la = [b[k]["log_a"] for b in boot]
            db = [b[k]["bic"] - b[ref]["bic"] for b in boot]
            dq = [b[k]["bic"] - b["qi_free"]["bic"] for b in boot]
            e["boot"] = dict(n=len(boot), log_a_16_50_84=[pct(la, q) for q in (0.16, 0.5, 0.84)],
                             dbic_16_50_84=[pct(db, q) for q in (0.16, 0.5, 0.84)],
                             dbic_vs_qi_free_16_50_84=[pct(dq, q) for q in (0.16, 0.5, 0.84)],
                             frac_best_bic=sum(min(b, key=lambda kk: b[kk]["bic"]) == k for b in boot) / len(boot))
        summary[k] = e

    bins = {k: binned(pts, fits[k]["res"], [-12.4 + 0.2 * i for i in range(20)]) for k in fits}
    result = dict(data=dict(source=BASE_URL, sha256=sums, n_points=len(pts), n_galaxies=ngal, alignment=align),
                  constants=dict(c=C, theta_early=THETA_EARLY, theta_late=THETA_LATE,
                                 a_early=theta_to_a(THETA_EARLY), a_late=theta_to_a(THETA_LATE)),
                  fits=summary, upsilon_disk=upsilon, upsilon_free=ufree, binned_residuals=bins,
                  bootstrap=dict(replicates=len(boot), seed=args.seed, unit="galaxy"),
                  interpretation="Point-level BIC uses an independence approximation. Galaxy bootstrap ranges "
                  "describe sampling variation conditional on the error model and baryonic assumptions; "
                  "they do not calibrate BIC evidence thresholds or establish model-independent exclusion.")
    (OUT / "results.json").write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n")

    # summary table
    L = ["<!-- generated by rar_refit.py; do not edit -->",
         f"Data: {len(pts)} points in {ngal} galaxies (Lelli et al. 2017 RAR). Bootstrap: {len(boot)} galaxy resamples.", "",
         result["interpretation"], "",
         "| Model | k | a (m s⁻²) | equiv. Θ (m) | σ_int (dex) | χ²/dof (σ_int = 0) | rms (dex) | −2 ln L | ΔBIC vs MOND simple | bootstrap ΔBIC 16–84% | best in bootstrap |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for k, e in summary.items():
        th = f"{e['theta_equiv_m']:.3g}" if e["theta_equiv_m"] else "—"
        a = fmt_a(e["a"]) if k != "newton" else "—"
        if e.get("boot") and k != "newton":
            la = e["boot"]["log_a_16_50_84"]
            if MODEL[k][3] is None:
                a += f" ({fmt_a(10 ** la[0])} – {fmt_a(10 ** la[2])})"
            bd = e["boot"]["dbic_16_50_84"]
            bs = f"{bd[0]:+.0f} to {bd[2]:+.0f}" if k != ref else "(reference)"
            fb = f"{100 * e['boot']['frac_best_bic']:.0f}%"
        else:
            bs = fb = "—"
        L.append(f"| {e['label']} | {e['k']} | {a} | {th} | {e['sig_int']:.3f} | {e['chi2_red']:.2f} | {e['rms']:.3f} | "
                 f"{e['m2lnl']:.1f} | {e['dbic_vs_mond_simple']:+.1f} | {bs} | {fb} |")
    L += ["", "Within QI: ΔBIC of each fixed Θ relative to QI with Θ free (bootstrap 16–84% in brackets):", ""]
    for k in ("qi_early", "qi_late"):
        e = summary[k]
        bq = e.get("boot", {}).get("dbic_vs_qi_free_16_50_84")
        L.append(f"- {e['label']}: {e['dbic_vs_qi_free']:+.1f}" + (f" ({bq[0]:+.0f} to {bq[2]:+.0f})" if bq else ""))
    L += ["", "Stellar mass-to-light systematics (Υ_bulge = 1.4 Υ_disk). ΔBIC vs MOND simple at the same Υ; fitted a in 10⁻¹⁰ m s⁻²:", "",
          "| Model | " + " | ".join(f"Υ_disk = {u}" for u in upsilon) + " |", "|---|" + "---|" * len(upsilon)]
    for k in MODEL:
        cells = []
        for u, fv in upsilon.items():
            s = f"{fv[k]['bic'] - fv[ref]['bic']:+.0f}"
            if MODEL[k][3] is None:
                s += f" (a = {fv[k]['a'] * 1e10:.2f})"
            cells.append(s)
        L.append(f"| {MODEL[k][1]} | " + " | ".join(cells) + " |")
    L += ["", "Global Υ_disk fitted as an extra free parameter (flat prior 0.15–1.0, Υ_bulge = 1.4 Υ_disk). ΔBIC vs MOND simple in this table:", "",
          "| Model | k | best Υ_disk | a (m s⁻²) | equiv. Θ (m) | σ_int (dex) | rms (dex) | ΔBIC |", "|---|---|---|---|---|---|---|---|"]
    for k, f in ufree.items():
        L.append(f"| {MODEL[k][1]} | {f['k']} | {f['upsilon_disk']:.2f} | {fmt_a(f['a'])} | {2 * C * C / f['a']:.3g} | "
                 f"{f['sig_int']:.3f} | {f['rms']:.3f} | {f['bic'] - ufree[ref]['bic']:+.1f} |")
    (OUT / "summary.md").write_text("\n".join(L) + "\n")

    fig_rar(pts, fits, OUT / "fig-1-rar-models.svg")
    fig_residuals(pts, fits, OUT / "fig-2-residuals-qi.svg", ["qi_early", "qi_late", "qi_free"],
                  "Binned residuals: QI with three choices of Θ")
    fig_residuals(pts, fits, OUT / "fig-3-residuals-free.svg", ["qi_free", "mond_simple", "mond_standard", "rar_exp"],
                  "Binned residuals: one-parameter fits")
    fig_theta(pts, fits["qi_free"], OUT / "fig-4-theta-profile.svg")
    print((OUT / "summary.md").read_text())


if __name__ == "__main__":
    main()
