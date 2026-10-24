"""A6 (binned, interim): does the RAR acceleration scale evolve with redshift as QI predicts?

Editorial analysis for the Quantized Inertia research archive. Python 3 standard library only.

Inputs are the four binned MUSE-DARK values of the RAR scale a0(z) tabulated by Alcock (2026,
MNRAS 551, Table 1; CC BY 4.0), digitized from Ciocan et al. (2026, A&A 709, L16, Fig. 3). The
per-galaxy MUSE-DARK data release was unreachable when this was written, so this is a binned
first pass, not the planned per-galaxy refit.

MUSE-DARK defines a0 through the McGaugh et al. (2016) function, g = gbar / (1 - exp(-sqrt(gbar/a0))).
McCulloch (2017) predicts g = gbar * sqrt(1 + aQ/gbar) with aQ = 2c^2/Theta and Theta = Theta0/(1+z).
The two scales are not the same number, so every QI prediction is converted into the a0 that the
McGaugh function would return if the data followed QI exactly, over the sample's distribution of
log gbar (a Gaussian with the hyperparameters MUSE-DARK report in their Fig. F.1).

Run:  python3 -I 09-analysis/a6-rar-redshift-evolution/redshift_scale.py
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
ROOT = HERE.parent

C = 2.99792458e8                      # m/s
MPC = 3.0856775814913673e22           # m
THETA0 = 8.8e26                       # McCulloch 2017: present co-moving cosmic diameter (m)
LN10 = math.log(10)

# Alcock 2026, MNRAS 551, Table 1 (units 1e-10 m/s^2): plotted z, a0, lower bar, upper bar.
# Digitized by Alcock from Ciocan et al. 2026b Fig. 3; the two extreme a0 values are printed in that paper's text.
BINS = [(0.503, 1.990, 0.085, 0.086),
        (0.825, 2.200, 0.105, 0.105),
        (1.047, 2.571, 0.114, 0.110),
        (1.276, 2.710, 0.134, 0.138)]
SPARC_A0 = (1.20, 0.26)               # McGaugh et al. 2016, as used by Ciocan et al. and Alcock (total uncertainty)
CIOCAN_LINEAR = (1.00, 1.59)          # Ciocan et al. 2026b Eq. 4: a0(0), a1 (1e-10 m/s^2; 95% CI +-0.04, +-0.10)
# Published global linear fits a0(z) = a0(0) + a1 z (McGaugh function, 1e-10 m/s^2; 95% CIs), Ciocan et al. 2026b.
# Eq. 4: RAR from DC14 disc-halo decompositions. Eq. E.5: RAR from the authors' MOND-framework refit, in which the
# stellar masses are refitted with modified dynamics and no halo (Appendix E, delta-family with delta ~ 1).
GLOBAL_FITS = {
    "dc14_eq4": dict(label="DC14 disc-halo decomposition (Eq. 4)", a0=1.00, a0_ci=0.04, a1=1.59, a1_ci=(0.10, 0.11)),
    "mond_eq_e5": dict(label="MOND-framework refit, no halo (Eq. E.5)", a0=1.03, a0_ci=0.05, a1=1.20, a1_ci=(0.10, 0.10)),
}

# Ciocan et al. 2026b Fig. F.1: Gaussian hyperparameters of the true log10 gbar distribution, read from the figure.
GBAR_MU, GBAR_W = -10.79, 0.63
GBAR_GRID = [(mu, w) for mu in (-11.09, -10.79, -10.49) for w in (0.40, 0.63, 0.90)]

# Cosmologies. Planck 2018 (as used elsewhere in this repository) for QI alternatives;
# Alcock's choice (Planck 2015, as in Ciocan et al. 2026a) only to reproduce his fits.
PLANCK18 = dict(H0=67.4, Om=0.315, Or=9.18e-5)
ALCOCK = dict(H0=67.7, Om=0.307, Or=0.0)


# ---------------------------------------------------------------- physics

def E(z, cos):
    ol = 1 - cos["Om"] - cos["Or"]
    return math.sqrt(cos["Or"] * (1 + z) ** 4 + cos["Om"] * (1 + z) ** 3 + ol)


def comoving_particle_horizon(z, cos, n=20000, umax=30.0):
    """c * integral_z^inf dz'/H(z'), Simpson's rule in u = ln(1+z')."""
    h0 = cos["H0"] * 1e3 / MPC
    u0 = math.log(1 + z)
    step = (umax - u0) / n
    s = 0.0
    for i in range(n + 1):
        u = u0 + i * step
        f = math.exp(u) / E(math.exp(u) - 1, cos)
        s += f * (1 if i in (0, n) else (4 if i % 2 else 2))
    return C / h0 * s * step / 3


def proper_horizon_diameter(z, cos=PLANCK18):
    return 2 * comoving_particle_horizon(z, cos) / (1 + z)


def nu_qi(y):        # McCulloch 2017 Eq. 8
    return math.sqrt(1.0 + 1.0 / y)


def nu_rar(y):       # McGaugh et al. 2016, Ciocan et al. 2026b Eq. 1
    return 1.0 / (1.0 - math.exp(-math.sqrt(y)))


def log_g(nu, la, x):
    return x + math.log10(nu(10 ** (x - la)))


def golden(f, lo, hi, tol=1e-7):
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


def gauss_grid(mu, w, n=81):
    xs = [mu - 4 * w + 8 * w * i / (n - 1) for i in range(n)]
    ws = [math.exp(-0.5 * ((x - mu) / w) ** 2) for x in xs]
    t = sum(ws)
    return xs, [v / t for v in ws]


def a0_equiv(a_q, mu=GBAR_MU, w=GBAR_W, dm=0.0):
    """McGaugh-function a0 (m/s^2) recovered from data that follow QI with scale a_q exactly.

    The analyst's log gbar values follow N(mu, w). dm (dex) is a common-mode mass offset:
    the true baryonic acceleration is 10**dm times the adopted one.
    """
    xs, ws = gauss_grid(mu, w)
    lq = math.log10(a_q)
    ys = [log_g(nu_qi, lq, x + dm) for x in xs]

    def cost(la):
        return sum(wi * (yi - log_g(nu_rar, la, x)) ** 2 for x, yi, wi in zip(xs, ys, ws))
    la, _ = golden(cost, lq - 1.5, lq + 1.0)
    return 10 ** la


# ---------------------------------------------------------------- statistics

def chi2(pred, bins=BINS, reading="c68"):
    """Weighted chi^2 with asymmetric bars; the bar on the side of the model is used.

    reading 'c68': bars are 1 sigma; 'c95': bars are 95% intervals (sigma = bar/1.96).
    """
    f = 1.0 if reading == "c68" else 1.96
    t, pulls = 0.0, []
    for p, (_, a, lo, hi) in zip(pred, bins):
        s = (hi if p > a else lo) / f
        pulls.append((a - p) / s)
        t += pulls[-1] ** 2
    return t, pulls


def gammaincc(s, x):
    """Regularized upper incomplete gamma Q(s, x)."""
    if x <= 0:
        return 1.0
    if x < s + 1:
        term = total = 1.0 / s
        k = s
        while abs(term) > 1e-15 * abs(total):
            k += 1
            term *= x / k
            total += term
        return 1.0 - total * math.exp(-x + s * math.log(x) - math.lgamma(s))
    b, c, d = x + 1 - s, 1e300, 1 / (x + 1 - s)
    h = d
    for i in range(1, 500):
        an = -i * (i - s)
        b += 2
        d = an * d + b
        d = 1 / d if d else 1e300
        c = b + an / c if c else 1e300
        dl = d * c
        h *= dl
        if abs(dl - 1) < 1e-15:
            break
    return math.exp(-x + s * math.log(x) - math.lgamma(s)) * h


def pvalue(x2, dof):
    return gammaincc(dof / 2, x2 / 2) if dof > 0 else float("nan")


def sigma_from_p(p):
    """Nominal Gaussian equivalent; None if p underflowed, not infinite evidence."""
    if p <= 0:
        return None
    lo, hi = 0.0, 40.0
    for _ in range(200):
        m = (lo + hi) / 2
        if math.erfc(m / math.sqrt(2)) > p:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def fit_amplitude(shape_pred, reading, lo=-11.5, hi=-8.5):
    """Best log10 amplitude for a one-parameter family; shape_pred(log_amp) -> list of a0 (1e-10)."""
    best = golden(lambda la: chi2(shape_pred(la), reading=reading)[0], lo, hi)
    la, x2 = best
    # 1-sigma interval from delta chi^2 = 1
    def edge(sign):
        a, b = la, la + sign * 1.0
        for _ in range(60):
            m = (a + b) / 2
            if chi2(shape_pred(m), reading=reading)[0] - x2 < 1:
                a = m
            else:
                b = m
        return (a + b) / 2
    return la, x2, edge(-1), edge(+1)


# ---------------------------------------------------------------- models

def zs():
    return [b[0] for b in BINS]


def published_qi(mu=GBAR_MU, w=GBAR_W):
    """McCulloch 2017: aQ(z) = (2c^2/Theta0)(1+z); converted to MUSE-DARK's a0 convention (1e-10)."""
    return [a0_equiv(2 * C * C * (1 + z) / THETA0, mu, w) * 1e10 for z in zs()]


def scaled_law(a_q0, law, mu=GBAR_MU, w=GBAR_W, horizon=None):
    """aQ(z) = a_q0 * law(z), converted to MUSE-DARK's convention (1e-10)."""
    return [a0_equiv(a_q0 * law(z), mu, w) * 1e10 for z in zs()]


def laws(horizon_ratio):
    return {
        "one_plus_z": ("QI as printed: (1+z)", lambda z: 1 + z),
        "hubble": ("H(z)/H0", lambda z: E(z, PLANCK18)),
        "proper_horizon": ("editorial: proper particle-horizon diameter", lambda z: horizon_ratio[z]),
        "constant": ("constant scale", lambda z: 1.0),
    }


def aq_from_a0(a0_target, mu=GBAR_MU, w=GBAR_W):
    """Inverse of a0_equiv: the QI scale whose McGaugh-function equivalent is a0_target (both m/s^2)."""
    lo, hi = math.log10(a0_target) - 1.0, math.log10(a0_target) + 1.0
    for _ in range(80):
        m = (lo + hi) / 2
        if a0_equiv(10 ** m, mu, w) < a0_target:
            lo = m
        else:
            hi = m
    return 10 ** ((lo + hi) / 2)


def global_fit_in_qi(fit):
    """Evaluate a published linear a0(z) at the bin redshifts and express it in QI's convention.

    Returns per-bin a_Q, ratio to McCulloch's published a_Q(z), and the least-squares slope of
    log a_Q against log(1+z) over the bins (an effective gamma), for the central values and for
    the 95% corners of the slope.
    """
    def evaluate(a0, a1):
        rows = []
        for z in zs():
            a0z = (a0 + a1 * z) * 1e-10
            aq = aq_from_a0(a0z)
            rows.append(dict(z=z, a0_mcg=a0z, a_q=aq, ratio_to_published=aq / (2 * C * C * (1 + z) / THETA0)))
        x = [math.log10(1 + r["z"]) for r in rows]
        y = [math.log10(r["a_q"]) for r in rows]
        mx, my = sum(x) / len(x), sum(y) / len(y)
        g = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
        return rows, g
    rows, g = evaluate(fit["a0"], fit["a1"])
    _, g_lo = evaluate(fit["a0"] + fit["a0_ci"], fit["a1"] - fit["a1_ci"][0])
    _, g_hi = evaluate(fit["a0"] - fit["a0_ci"], fit["a1"] + fit["a1_ci"][1])
    return dict(label=fit["label"], bins=rows, gamma=g, gamma_corners=[g_lo, g_hi],
                a_q_intercept=aq_from_a0(fit["a0"] * 1e-10))


def mass_offset_for(a0_target, a_q, mu=GBAR_MU, w=GBAR_W):
    """Common-mode mass offset dm (dex) under which QI data analysed with adopted masses give a0_target."""
    f = lambda dm: math.log10(a0_equiv(a_q, mu, w, dm)) - math.log10(a0_target)
    lo, hi = -1.5, 1.5
    flo = f(lo)
    for _ in range(60):
        m = (lo + hi) / 2
        fm = f(m)
        if (fm > 0) == (flo > 0):
            lo, flo = m, fm
        else:
            hi = m
    return (lo + hi) / 2


def power_law_fit(values_fn, reading):
    """Two-parameter fit a(z) = A (1+z)^gamma; returns gamma, its 1-sigma half width, A, chi2."""
    def prof(g):
        la, x2, _, _ = fit_amplitude(lambda la: values_fn(la, g), reading)
        return x2, la
    g, _ = golden(lambda g: prof(g)[0], -1.0, 3.0, 1e-5)
    x2, la = prof(g)

    def edge(sign):
        a, b = g, g + sign * 2.0
        for _ in range(50):
            m = (a + b) / 2
            if prof(m)[0] - x2 < 1:
                a = m
            else:
                b = m
        return (a + b) / 2
    lo, hi = edge(-1), edge(+1)
    return dict(gamma=g, gamma_lo=lo, gamma_hi=hi, sigma=(hi - lo) / 2, A=10 ** la, chi2=x2)


# ---------------------------------------------------------------- reporting helpers

def model_row(key, label, pred, k, reading):
    x2, pulls = chi2(pred, reading=reading)
    dof = len(BINS) - k
    p = pvalue(x2, dof)
    return dict(key=key, label=label, k=k, pred=pred, chi2=x2, dof=dof, p=p,
                sigma=sigma_from_p(p), p_underflow=(p == 0), pulls=pulls)


def a1_scales():
    out = {}
    try:
        r = json.loads((ROOT / "a1-sparc-rar-refit/results/results.json").read_text())
        q = r["fits"]["qi_free"]
        out["a1"] = dict(source="A1 qi_free (RAR-level, Υ_disk = 0.5)", a=q["a"],
                         lo=10 ** q["boot"]["log_a_16_50_84"][0], hi=10 ** q["boot"]["log_a_16_50_84"][2])
    except (OSError, KeyError, ValueError):
        pass
    try:
        r = json.loads((ROOT / "a1b-sparc-per-galaxy/results/results.json").read_text())
        q = r["fits"]["qi"]
        out["a1b"] = dict(source="A1b qi (per-galaxy, baseline priors)", a=q["a"],
                          lo=10 ** q["boot_log_a_16_50_84"][0], hi=10 ** q["boot_log_a_16_50_84"][2])
    except (OSError, KeyError, ValueError):
        pass
    return out


# ---------------------------------------------------------------- figures (themed SVG, as in A1)

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

    def band(self, xs, lo, hi, color, op=0.15):
        pts = [(x, y) for x, y in zip(xs, hi)] + [(x, y) for x, y in zip(reversed(xs), reversed(lo))]
        d = " ".join(f"{'M' if i == 0 else 'L'}{self.X(x):.1f},{self.Y(y):.1f}" for i, (x, y) in enumerate(pts)) + " Z"
        self.el.append(f'<path d="{d}" fill="{color}" fill-opacity="{op}" stroke="none"/>')

    def errbar(self, x, y, lo, hi, color, tip):
        self.el.append(f'<line x1="{self.X(x):.1f}" x2="{self.X(x):.1f}" y1="{self.Y(y - lo):.1f}" y2="{self.Y(y + hi):.1f}" '
                       f'stroke="{color}" stroke-width="2"/>')
        self.el.append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="5" fill="{color}" stroke="var(--surface)" '
                       f'stroke-width="2"><title>{tip}</title></circle>')

    def star(self, x, y, color, tip):
        self.el.append(f'<rect x="{self.X(x) - 5:.1f}" y="{self.Y(y) - 5:.1f}" width="10" height="10" fill="{color}" '
                       f'transform="rotate(45 {self.X(x):.1f} {self.Y(y):.1f})"><title>{tip}</title></rect>')

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


def fig_scale(res, path, horizon_ratio_fn):
    p = Plot(760, 520, (0, 1.5), (0.5, 4.5), "RAR acceleration scale versus redshift: binned MUSE-DARK and QI predictions",
             "redshift z", "a₀ in MUSE-DARK's convention (10⁻¹⁰ m s⁻²)")
    p.axes([0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5], [1, 2, 3, 4])
    grid = [i * 1.5 / 60 for i in range(61)]
    mu, w = GBAR_MU, GBAR_W
    pub = [a0_equiv(2 * C * C * (1 + z) / THETA0, mu, w) * 1e10 for z in grid]
    lo_s = [min(a0_equiv(2 * C * C * (1 + z) / THETA0, m, ww) for m, ww in GBAR_GRID) * 1e10 for z in grid]
    hi_s = [max(a0_equiv(2 * C * C * (1 + z) / THETA0, m, ww) for m, ww in GBAR_GRID) * 1e10 for z in grid]
    p.band(grid, lo_s, hi_s, "var(--s2)")
    p.line(grid, pub, "var(--s2)", tip="McCulloch 2017, Θ₀ = 8.8 × 10²⁶ m, (1+z)")
    ph = [a0_equiv(2 * C * C / proper_horizon_diameter(z), mu, w) * 1e10 for z in grid]
    p.line(grid, ph, "var(--s5)", "2 4", tip="editorial: Θ = proper particle-horizon diameter")
    cal = res["calibrated"].get("a1b") or res["calibrated"].get("a1")
    if cal:
        c_mid = [a0_equiv(cal["a_q0"] * (1 + z), mu, w) * 1e10 for z in grid]
        c_lo = [a0_equiv(cal["a_q0_lo"] * (1 + z), mu, w) * 1e10 for z in grid]
        c_hi = [a0_equiv(cal["a_q0_hi"] * (1 + z), mu, w) * 1e10 for z in grid]
        p.band(grid, c_lo, c_hi, "var(--s3)")
        p.line(grid, c_mid, "var(--s3)", tip=f"QI (1+z), scale calibrated on SPARC ({cal['source']})")
    hb = res["shape_fits"]["c68"]["hubble"]
    p.line(grid, [a0_equiv(hb["a_q0"] * E(z, PLANCK18), mu, w) * 1e10 for z in grid], "var(--s1)", "6 3",
           tip="H(z) shape, amplitude fitted")
    p.line(grid, [SPARC_A0[0]] * len(grid), "var(--ink2)", "2 3", tip="constant a₀ = 1.2 (standard MOND reading)")
    p.line(grid, [CIOCAN_LINEAR[0] + CIOCAN_LINEAR[1] * z for z in grid], "var(--pt)", "1 3",
           tip="Ciocan et al. 2026 global linear fit (Eq. 4)")
    for z, a, lo, hi in BINS:
        p.errbar(z, a, lo, hi, "var(--ink)", f"z = {z}: a₀ = {a} (−{lo}/+{hi}), Alcock 2026 Table 1")
    p.star(0.0, SPARC_A0[0], "var(--ink2)", "SPARC a₀ = 1.20 ± 0.26 (McGaugh et al. 2016)")
    lab = f"QI, scale calibrated on SPARC ({'A1b' if 'a1b' in res['calibrated'] else 'A1'}), (1+z)" if cal else None
    items = [("QI published: Θ₀ = 8.8 × 10²⁶ m, (1+z)", "var(--s2)", None)]
    if lab:
        items.append((lab, "var(--s3)", None))
    items += [("editorial: proper particle-horizon Θ(z)", "var(--s5)", "2 4"),
              ("H(z) shape, amplitude fitted", "var(--s1)", "6 3"),
              ("constant a₀ = 1.2", "var(--ink2)", "2 3"),
              ("MUSE-DARK linear fit", "var(--pt)", "1 3")]
    p.legend(items, 80, 62)
    p.save(path)


def fig_mass(res, path):
    rows = res["mass_offset"]["per_bin"]
    p = Plot(620, 400, (0.3, 1.5), (-0.6, 0.6), "Uniform baryonic-mass shift each bin would need to match a QI law",
             "redshift z", "required Δ log M (dex)")
    p.axes([0.4, 0.6, 0.8, 1.0, 1.2, 1.4], [-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6])
    xs = [r["z"] for r in rows]
    p.line(xs, [r["dm_published"] for r in rows], "var(--s2)", tip="published QI")
    for r in rows:
        p.errbar(r["z"], r["dm_published"], 0, 0, "var(--s2)", f"published QI: {r['dm_published']:+.2f} dex")
    if rows and "dm_calibrated" in rows[0]:
        p.line(xs, [r["dm_calibrated"] for r in rows], "var(--s3)", tip="SPARC-calibrated QI")
        for r in rows:
            p.errbar(r["z"], r["dm_calibrated"], 0, 0, "var(--s3)", f"calibrated QI: {r['dm_calibrated']:+.2f} dex")
    p.line([0.3, 1.5], [0, 0], "var(--ink2)", "2 3")
    p.legend([("QI published (Θ₀ = 8.8 × 10²⁶ m)", "var(--s2)", None),
              (f"QI, scale calibrated on SPARC ({res['mass_offset']['calibrated_source']})", "var(--s3)", None)], 80, 62)
    p.save(path)


# ---------------------------------------------------------------- main

def main():
    OUT.mkdir(exist_ok=True)
    horizon0 = proper_horizon_diameter(0.0)
    horizon_ratio = {z: horizon0 / proper_horizon_diameter(z) for z in zs()}
    res = dict(
        inputs=dict(
            bins=[dict(z=z, a0=a, lower=lo, upper=hi) for z, a, lo, hi in BINS],
            bins_source="Alcock 2026, MNRAS 551, Table 1 (doi:10.1093/mnras/stag1485), digitized from Ciocan et al. 2026b Fig. 3",
            units="1e-10 m s^-2",
            gbar_distribution=dict(mu=GBAR_MU, w=GBAR_W, source="Ciocan et al. 2026b Fig. F.1 (mu_gauss, w_gauss), read from the figure"),
            gbar_sensitivity_grid=GBAR_GRID,
            theta0_m=THETA0,
            cosmology_qi=PLANCK18,
            proper_horizon_diameter_z0_m=horizon0,
        ),
        conversion={}, models={}, shape_fits={}, power_law={}, calibrated={}, mass_offset={}, sensitivity={},
    )

    # Conversion factor a0_equiv / aQ at the published scale for each bin.
    for z in zs():
        aq = 2 * C * C * (1 + z) / THETA0
        res["conversion"][str(z)] = dict(a_q=aq, a0_equiv=a0_equiv(aq), ratio=a0_equiv(aq) / aq)

    # Absolute predictions (no parameters fitted to these data).
    cal = a1_scales()
    for key, c in cal.items():
        res["calibrated"][key] = dict(source=c["source"], a_q0=c["a"], a_q0_lo=c["lo"], a_q0_hi=c["hi"],
                                      theta_equiv_m=2 * C * C / c["a"],
                                      pred=scaled_law(c["a"], lambda z: 1 + z),
                                      pred_lo=scaled_law(c["lo"], lambda z: 1 + z),
                                      pred_hi=scaled_law(c["hi"], lambda z: 1 + z))
    abs_models = [("published", "QI published: Θ₀ = 8.8 × 10²⁶ m, Θ = Θ₀/(1+z)", published_qi()),
                  ("proper_horizon_abs", "Editorial: Θ = proper particle-horizon diameter (absolute)",
                   [a0_equiv(2 * C * C / proper_horizon_diameter(z)) * 1e10 for z in zs()])]
    for key, c in res["calibrated"].items():
        abs_models.append((f"calibrated_{key}", f"QI (1+z), scale from {c['source']}", c["pred"]))
    abs_models.append(("constant_sparc", "Constant a₀ = 1.20 (SPARC)", [SPARC_A0[0]] * len(BINS)))
    for reading in ("c68", "c95"):
        res["models"][reading] = {k: model_row(k, lab, pred, 0, reading) for k, lab, pred in abs_models}

    # Shape tests: amplitude aQ(0) free, law fixed, converted per bin.
    for reading in ("c68", "c95"):
        out = {}
        for key, (lab, law) in laws(horizon_ratio).items():
            la, x2, lo, hi = fit_amplitude(lambda la: scaled_law(10 ** la, law), reading)
            row = model_row(key, lab, scaled_law(10 ** la, law), 1, reading)
            row.update(a_q0=10 ** la, a_q0_lo=10 ** lo, a_q0_hi=10 ** hi, theta_equiv_m=2 * C * C / 10 ** la)
            out[key] = row
        res["shape_fits"][reading] = out

    # Power-law exponent: raw a0 (reproduces Alcock) and in QI's aQ convention.
    for reading in ("c68", "c95"):
        raw = power_law_fit(lambda la, g: [10 ** la * 1e10 * (1 + z) ** g for z in zs()], reading)
        qi = power_law_fit(lambda la, g: scaled_law(10 ** la, lambda z: (1 + z) ** g), reading)
        for d in (raw, qi):
            d["pull_gamma_1"] = (d["gamma"] - 1) / (d["gamma_hi"] - d["gamma"] if d["gamma"] < 1 else d["gamma"] - d["gamma_lo"])
        res["power_law"][reading] = dict(raw_a0=raw, qi_scale=qi)

    # Alcock reproduction (his cosmology, raw a0, bins only).
    rep = {}
    for key, law in (("frozen", lambda z: 1.0), ("hubble", lambda z: E(z, ALCOCK)), ("matter", lambda z: (1 + z) ** 1.5)):
        la, x2, _, _ = fit_amplitude(lambda la: [10 ** la * 1e10 * law(z) for z in zs()], "c68")
        rep[key] = dict(A=10 ** la * 1e10, chi2=x2)
    res["alcock_reproduction"] = rep

    # Mass offsets: uniform shift that would make each bin match the published (and calibrated) QI law.
    rows = []
    calkey = "a1b" if "a1b" in cal else ("a1" if "a1" in cal else None)
    for z, a, lo, hi in BINS:
        r = dict(z=z, dm_published=mass_offset_for(a * 1e-10, 2 * C * C * (1 + z) / THETA0))
        if calkey:
            r["dm_calibrated"] = mass_offset_for(a * 1e-10, cal[calkey]["a"] * (1 + z))
        rows.append(r)
    best_dm = golden(lambda dm: chi2([a0_equiv(2 * C * C * (1 + z) / THETA0, dm=dm) * 1e10 for z in zs()])[0], -1.0, 1.0, 1e-5)
    res["mass_offset"] = dict(per_bin=rows, calibrated_source=calkey,
                              common_mode_published=dict(dm=best_dm[0], chi2_c68=best_dm[1], dof=3,
                                                         p=pvalue(best_dm[1], 3)),
                              note="dm > 0: true baryonic masses larger than adopted; dm < 0: smaller.")

    # Sensitivity of the published prediction to the assumed gbar distribution.
    sens = []
    for mu, w in GBAR_GRID:
        pred = published_qi(mu, w)
        x2, _ = chi2(pred)
        sens.append(dict(mu=mu, w=w, pred=pred, chi2_c68=x2, chi2_c95=chi2(pred, reading="c95")[0]))
    res["sensitivity"]["published_vs_gbar"] = sens
    res["global_fits"] = {k: global_fit_in_qi(v) for k, v in GLOBAL_FITS.items()}

    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False, allow_nan=False) + "\n")
    fig_scale(res, OUT / "fig-1-scale-vs-redshift.svg", horizon_ratio)
    fig_mass(res, OUT / "fig-2-mass-offset.svg")
    (OUT / "summary.md").write_text(summary(res))
    print((OUT / "summary.md").read_text())


def f2(v):
    return f"{v:.2f}"


def summary(r):
    L = ["# A6 binned results (generated by redshift_scale.py; do not edit)", "",
         "Editorial approximation: the curve conversion is an equal-weight projection over an assumed acceleration distribution, "
         "not a reproduction of the survey's regression. All χ², p-values and σ equivalents are nominal, conditional on independent "
         "bins and the selected bar convention. Calibration and conversion uncertainty are not included in those statistics.", ""]
    L += ["Units: 10⁻¹⁰ m s⁻². Predictions are in MUSE-DARK's convention (McGaugh-function a₀), converted from QI's a_Q over "
          f"log g_bar ~ N({GBAR_MU}, {GBAR_W}).", ""]
    L += ["## Conversion from a_Q to MUSE-DARK's a₀ (published scale)", "",
          "| z | a_Q = 2c²(1+z)/Θ₀ | equivalent a₀ | ratio |", "|---|---|---|---|"]
    for z, c in r["conversion"].items():
        L.append(f"| {z} | {c['a_q'] * 1e10:.2f} | {c['a0_equiv'] * 1e10:.2f} | {c['ratio']:.3f} |")
    L += ["", "## Absolute predictions (nothing fitted to these bins)", ""]
    zs_ = [b["z"] for b in r["inputs"]["bins"]]
    L.append("| Model | " + " | ".join(f"z = {z}" for z in zs_) + " | χ² (bars = 1σ) | p | χ² (bars = 95%) |")
    L.append("|---|" + "---|" * (len(zs_) + 3))
    L.append("| **Data** (Alcock Table 1) | " + " | ".join(f"{b['a0']:.2f} (−{b['lower']}/+{b['upper']})" for b in r["inputs"]["bins"]) + " | | | |")
    for k, m in r["models"]["c68"].items():
        m95 = r["models"]["c95"][k]
        L.append(f"| {m['label']} | " + " | ".join(f2(v) for v in m["pred"]) +
                 f" | {m['chi2']:.1f} / {m['dof']} | {m['p']:.1e} | {m95['chi2']:.0f} / {m95['dof']} |")
    for key, c in r["calibrated"].items():
        L.append("")
        L.append(f"Calibrated scale {key}: a_Q(0) = {c['a_q0'] * 1e10:.3f} (bootstrap 16–84%: {c['a_q0_lo'] * 1e10:.3f}–"
                 f"{c['a_q0_hi'] * 1e10:.3f}); predictions span " +
                 ", ".join(f"{lo:.2f}–{hi:.2f}" for lo, hi in zip(c["pred_lo"], c["pred_hi"])) + " across that range.")
    L += ["", "## Shape tests (a_Q(0) fitted, law fixed; k = 1, dof = 3)", "",
          "| Law | reading | fitted a_Q(0) | equiv. Θ₀ (m) | χ² | p |", "|---|---|---|---|---|---|"]
    for reading in ("c68", "c95"):
        for k, m in r["shape_fits"][reading].items():
            L.append(f"| {m['label']} | {reading} | {m['a_q0'] * 1e10:.2f} ({m['a_q0_lo'] * 1e10:.2f}–{m['a_q0_hi'] * 1e10:.2f}) | "
                     f"{m['theta_equiv_m']:.3g} | {m['chi2']:.1f} | {m['p']:.1e} |")
    L += ["", "## Power-law exponent, a ∝ (1+z)^γ (k = 2)", "", "| Fitted quantity | reading | γ (1σ) | (γ − 1)/σ |", "|---|---|---|---|"]
    for reading in ("c68", "c95"):
        for name, d in (("MUSE-DARK a₀ directly", r["power_law"][reading]["raw_a0"]),
                        ("QI a_Q after conversion", r["power_law"][reading]["qi_scale"])):
            L.append(f"| {name} | {reading} | {d['gamma']:.2f} (−{d['gamma'] - d['gamma_lo']:.2f}/+{d['gamma_hi'] - d['gamma']:.2f}) | {d['pull_gamma_1']:+.1f} |")
    a = r["alcock_reproduction"]
    L += ["", f"Alcock reproduction (his cosmology, bins only, bars = 1σ): frozen A = {a['frozen']['A']:.2f}, χ² = {a['frozen']['chi2']:.1f}; "
          f"H(z) A = {a['hubble']['A']:.2f}, χ² = {a['hubble']['chi2']:.1f}; (1+z)^1.5 A = {a['matter']['A']:.2f}, χ² = {a['matter']['chi2']:.1f}. "
          "Alcock reports 2.28/28.8, 1.40/5.2 and 0.90/23.2.", ""]
    mo = r["mass_offset"]
    L += ["## Uniform mass shift needed for QI to match each bin", "",
          "| z | published QI (dex) | " + ("SPARC-calibrated QI (dex) |" if mo["calibrated_source"] else ""),
          "|---|---|" + ("---|" if mo["calibrated_source"] else "")]
    for row in mo["per_bin"]:
        L.append(f"| {row['z']} | {row['dm_published']:+.2f} | " + (f"{row['dm_calibrated']:+.2f} |" if "dm_calibrated" in row else ""))
    cm = mo["common_mode_published"]
    L += ["", f"Best single shift for the published law: {cm['dm']:+.3f} dex, leaving χ² = {cm['chi2_c68']:.1f} / 3 (p = {cm['p']:.1e}). "
          "Negative means the adopted baryonic masses would have to be too large.", ""]
    L += ["## Published global fits expressed in QI's convention", "",
          "Ciocan et al. 2026b global linear fits, evaluated at the bin redshifts and converted to a_Q. "
          "γ is the least-squares slope of log a_Q against log(1+z); the corners use the 95% CI ends of the fit.", "",
          "| Fit | a_Q per bin (10⁻¹⁰ m s⁻²) | ÷ published QI | effective γ (95% corners) | intercept a_Q(0) |", "|---|---|---|---|---|"]
    for k, gf in r["global_fits"].items():
        L.append(f"| {gf['label']} | " + ", ".join(f"{b['a_q'] * 1e10:.2f}" for b in gf["bins"]) + " | " +
                 ", ".join(f"{b['ratio_to_published']:.2f}" for b in gf["bins"]) +
                 f" | {gf['gamma']:.2f} ({gf['gamma_corners'][0]:.2f} to {gf['gamma_corners'][1]:.2f}) | {gf['a_q_intercept'] * 1e10:.2f} |")
    L.append("")
    L += ["## Sensitivity of the published prediction to the assumed g_bar distribution", "",
          "| μ | w | predictions | χ² (1σ) | χ² (95%) |", "|---|---|---|---|---|"]
    for s in r["sensitivity"]["published_vs_gbar"]:
        L.append(f"| {s['mu']} | {s['w']} | " + ", ".join(f2(v) for v in s["pred"]) + f" | {s['chi2_c68']:.0f} | {s['chi2_c95']:.0f} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
