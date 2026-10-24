"""A6b: QI's redshift law against MUSE-DARK galaxies rebuilt from their public decomposition parameters.

Editorial analysis for the Quantized Inertia research archive. Requires numpy and scipy (09-analysis/requirements.txt).

Inputs (downloaded into the git-ignored data/ folder and checked by SHA-256):
- Karpov 2026, Zenodo 10.5281/zenodo.22278304: galpak_params_all.csv, the GalPaK3D DC14 parameters of the
  126 galaxies of the MUSE-DARK release, parsed by Karpov. Terms: those of the MUSE-DARK release (not stated).
- Sentina 2026, Zenodo 10.5281/zenodo.23442383 (CC BY 4.0): per-galaxy redshift, SED stellar mass, SFR and
  radial extent of the kinematic data for the 89-galaxy subsample; model-evidence extract for the quality cut.

Each galaxy's model rotation curve is rebuilt (Sersic disc as oblate Gaussians, constant-density HI with
v^2 = pi G Sigma r, DC14 halo, Hernquist bulge) and sampled from 2 kpc to the data extent. g_obs is the model
circular acceleration, which is fixed. SED budgets conserve the total stellar mass,
retaining the dynamical bulge-to-total ratio; added molecular gas follows the disc.

Run:  .venv/bin/python -I 09-analysis/a6b-musedark-per-galaxy/musedark_qi.py [--boot 500]
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
from scipy.optimize import minimize, nnls
from scipy.special import gammaincinv

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE / "results"

SOURCES = {
    "karpov": dict(url="https://zenodo.org/records/22278304/files/musedark-a0z-audit-v1.zip?download=1",
                   sha256="6aac9a9cfdcee5b19553598b24dfe3a1bb41240f7c4afdc4b1c982ae1ba5029d", file="karpov-musedark-a0z-audit-v1.zip"),
    "sentina": dict(url="https://zenodo.org/records/23442383/files/a0z_zenodo_package_v6.2.zip?download=1",
                    sha256="ddef7a04fec10be55c2c2d8ab85109e2e1ec4cba2e9f00e45cedc1a7c3410b9f", file="sentina-a0z-package-v6.2.zip"),
}
MEMBERS = {
    "params": ("karpov", "musedark-a0z-audit/data/musedark/galpak/galpak_params_all.csv"),
    "galaxies": ("sentina", "a0z_v62_zenodo/results/a0post_summary_k1.0.csv"),
    "logz": ("sentina", "a0z_v62_zenodo/data/musedark_logZ_extract.csv"),
}

G = 4.30091e-6                 # kpc (km/s)^2 / Msun
KK_TO_SI = 1e6 / 3.0856775814913673e19   # (km/s)^2/kpc -> m/s^2
C = 2.99792458e8
THETA0 = 8.8e26
PUBLISHED_BINS = [(0.503, 1.990), (0.825, 2.200), (1.047, 2.571), (1.276, 2.710)]   # Alcock 2026 Table 1
KARPOV_BINS_A = {"dyn": [2.31, 2.38, 3.64, 3.65], "sed": [1.95, 1.96, 2.17, 1.69], "sed_h2": [1.23, 0.96, 0.88, 0.56]}
LG = np.arange(-11.5, -8.5 + 1e-9, 0.0025)   # log10 scale grid (m/s^2)


# ---------------------------------------------------------------- data

def fetch():
    DATA.mkdir(exist_ok=True)
    out = {}
    for key, s in SOURCES.items():
        p = DATA / s["file"]
        if not p.exists():
            req = urllib.request.Request(s["url"], headers={"User-Agent": "qi-research-archive/1.0 (python-urllib)"})
            p.write_bytes(urllib.request.urlopen(req, timeout=120).read())
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h != s["sha256"]:
            raise SystemExit(f"checksum mismatch for {p.name}: {h}")
        out[key] = p
    return out


# Halo-fit catalogue of the MUSE-DARK release as captured by the Internet Archive on 7 January 2026. Used only as a
# cross-check of Karpov's parsed table (retrieved by him on 2 September 2026), not as an input to the fits.
WAYBACK = dict(url="https://web.archive.org/web/20260107002101id_/https://dark-matter.osu-lyon.fr/data/catalogues/DC14_bestfit.txt",
               sha256="20cf806591dc83eb1ab098fcca5d6d5b62b53055d2e84515352403ac4e1a2554", file="wayback-20260107-DC14_bestfit.txt")


def wayback_check(params):
    """Compare halo parameters in Karpov's table with the archived January 2026 catalogue. None if unavailable."""
    p = DATA / WAYBACK["file"]
    try:
        if not p.exists():
            req = urllib.request.Request(WAYBACK["url"], headers={"User-Agent": "qi-research-archive/1.0 (python-urllib)"})
            p.write_bytes(urllib.request.urlopen(req, timeout=120).read())
    except OSError as e:
        return dict(available=False, reason=str(e))
    if hashlib.sha256(p.read_bytes()).hexdigest() != WAYBACK["sha256"]:
        return dict(available=False, reason="checksum mismatch")
    lines = [l.split() for l in p.read_text().splitlines() if l.strip()]
    head, arch = lines[0], {l[0]: dict(zip(lines[0], l)) for l in lines[1:]}
    kar = {r["muse_id"]: r for r in params}
    common = sorted(set(arch) & set(kar), key=int)
    out = dict(available=True, url=WAYBACK["url"], sha256=WAYBACK["sha256"], n_archive=len(arch), n_karpov=len(kar),
               n_common=len(common), columns={})
    for col in ("virial_velocity", "log_Mvir", "concentration", "rs_kpc", "log_X"):
        d, ids = [], []
        for i in common:
            a, b = num(kar[i].get(col)), num(arch[i].get(col))
            if math.isnan(a) or math.isnan(b) or (not col.startswith("log") and b == 0):
                continue
            d.append(a - b if col.startswith("log") else a / b)
            ids.append(i)
        d = np.array(d)
        ref = 0.0 if col.startswith("log") else 1.0
        dev = np.abs(d - ref) if not col.startswith("log") else np.abs(10 ** d - 1)
        out["columns"][col] = dict(kind="difference" if col.startswith("log") else "ratio", n=int(len(d)),
                                   median=float(np.median(d)), p16_84=pct(d, (16, 84)),
                                   n_off_10pct=int(np.sum(dev > 0.10)),
                                   ids_off_10pct=[i for i, x in zip(ids, dev) if x > 0.10])
    return out


def read_member(zips, key):
    src, name = MEMBERS[key]
    with zipfile.ZipFile(zips[src]) as z:
        text = z.read(name).decode("utf-8")
    return [r for r in csv.DictReader(io.StringIO("\n".join(l for l in text.splitlines() if not l.startswith("#"))))]


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return float("nan")


# ---------------------------------------------------------------- mass model

_MGE = {}


def sersic_mge(n, ng=24):
    """Gaussian amplitudes w_j and widths s_j (units of Re) fitting a Sersic profile; normalised to unit mass."""
    key = round(n, 3)
    if key not in _MGE:
        bn = gammaincinv(2 * n, 0.5)
        R = np.logspace(-2.5, math.log10(12), 300)
        S = np.exp(-bn * (R ** (1 / n) - 1))
        s = np.logspace(-2.7, math.log10(8), ng)
        A = np.exp(-R[:, None] ** 2 / (2 * s[None, :] ** 2))
        w, _ = nnls(A / S[:, None], np.ones_like(S))
        w = w / np.sum(2 * np.pi * s ** 2 * w)
        _MGE[key] = (w, s)
    return _MGE[key]


_U = np.linspace(0, 1, 401)


def vc2_disc(r, Re, n, aspect=0.15):
    """Circular velocity^2 (km/s)^2 of a unit-mass Sersic disc of scale height aspect*Re (oblate Gaussians)."""
    w, s = sersic_mge(n)
    sig = s * Re
    Mj = 2 * np.pi * s ** 2 * w
    q = np.clip(aspect * Re / sig, 0.02, 1.0)
    e2 = 1 - q ** 2
    x = r[:, None, None] / sig[None, :, None]
    u = _U[None, None, :]
    integ = np.trapezoid(u ** 2 * np.exp(-0.5 * x ** 2 * u ** 2) / np.sqrt(1 - e2[None, :, None] * u ** 2), _U, axis=2)
    return np.sum(2 * G * Mj[None, :] * r[:, None] ** 2 / (math.sqrt(2 * math.pi) * sig[None, :] ** 3) * integ, axis=1)


def dc14_mass(r, rhos, rs, a, b, g):
    rr = np.geomspace(1e-4, max(r.max(), rs) * 1.001, 20000)
    rho = rhos / ((rr / rs) ** g * (1 + (rr / rs) ** a) ** ((b - g) / a))
    m = np.concatenate([[0], np.cumsum(0.5 * (4 * np.pi * rr[1:] ** 2 * rho[1:] + 4 * np.pi * rr[:-1] ** 2 * rho[:-1]) * np.diff(rr))])
    return np.interp(r, rr, m)


def build(params, gals, logz, hi_factor=math.pi, grid="data"):
    """Rebuild each galaxy. grid "data": r = 2 kpc .. data extent (0.2 kpc steps);
    grid "karpov": 25 radii from max(0.3 kpc, 0.2 Re) to 3 Re, as in Karpov 2026. Returns list of dicts."""
    P = {r["muse_id"]: r for r in params}
    Z = {}
    for r in logz:
        Z.setdefault(r["muse_id"], []).append(num(r["log_Z_DC14"]))
    out = []
    for gr in gals:
        gid = gr["id"]
        p = P.get(gid)
        if p is None:
            continue
        Re, n = num(p["rad_kpc"]), num(p["sersic_n"])
        need = [num(p[k]) for k in ("rhos", "rs_kpc", "alpha", "beta", "gamma", "log_Mdisk", "gas_density")]
        if any(math.isnan(v) for v in need + [Re, n]) or not (0.3 <= n <= 8):
            continue
        rhos, rs, a, b, g, lmd, sig_hi = need
        rext = num(gr["rext"])
        if grid == "karpov":
            r = np.linspace(max(0.3, 0.2 * Re), 3.0 * Re, 25)
        else:
            r = np.arange(2.0, rext + 1e-9, 0.2) if rext >= 2.2 else None
        rfull = np.unique(np.concatenate([[2.0], np.geomspace(0.3, max(rext, 3.0 * Re, 3.0), 40)] + ([r] if r is not None else [])))
        vd1 = vc2_disc(rfull, Re, n)                       # per unit mass
        vh = hi_factor * G * sig_hi * 1e6 * rfull
        vdm = G * dc14_mass(rfull, rhos, rs, a, b, g) / rfull
        vb = np.zeros_like(rfull)
        lmb = num(p.get("log_Mbulge"))
        if not math.isnan(lmb) and num(p.get("radius")) > 0:
            rb = num(p["bulge_radius"]) * Re / num(p["radius"]) / 1.8153    # Hernquist scale from effective radius
            vb = G * 10 ** lmb * rfull / (rfull + rb) ** 2
        vc2 = 10 ** lmd * vd1 + vh + vdm + vb
        i2 = int(np.argmin(np.abs(rfull - 2.0)))
        sd = num(p.get("velocity_dispersion"))
        vperp2 = vc2[i2] - 0.92 * sd ** 2 * (2.0 / (Re / 1.678)) if not math.isnan(sd) else float("nan")
        gal = dict(id=gid, z=num(gr["z"]), m_sed=num(gr["Mstar"]), sfr=num(gr["SFR"]), m_dyn=lmd, Re=Re, rext=rext,
                   logz=min(Z.get(gid, [float("nan")])), v22_sigma=num(p.get("v22")) / sd if sd > 0 else float("nan"),
                   v2kpc_model=math.sqrt(vperp2) if vperp2 > 0 else float("nan"), v2kpc_release=num(p.get("v2kpc")),
                   has_bulge=not math.isnan(lmb), m_bulge=10 ** lmb if not math.isnan(lmb) else 0.0)
        if r is not None:
            ix = np.searchsorted(rfull, r)
            gal.update(r=r, vd1=vd1[ix], vh=vh[ix], vdm=vdm[ix], vb=vb[ix], vc2=vc2[ix])
        out.append(gal)
    return out


# ---------------------------------------------------------------- budgets

def age_gyr(z, H0=70.0, Om=0.3):
    zz = np.geomspace(1e-6, 1e4, 20000) + z
    f = 1 / ((1 + zz) * H0 * np.sqrt(Om * (1 + zz) ** 3 + 1 - Om))
    return float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(zz))) * 977.8


def mu_h2(z, logm, dms=1.0):
    """Molecular-to-stellar ratio, Tacconi et al. 2018 scaling as used by Karpov 2026."""
    return 10 ** (0.07 - 3.8 * (math.log10(1 + z) - 0.63) ** 2 + 0.53 * math.log10(dms) - 0.33 * (logm - 10.7))


def dms_speagle(z, logm, logsfr):
    t = age_gyr(z)
    return 10 ** (logsfr - ((0.84 - 0.026 * t) * logm - (6.51 - 0.11 * t)))


BUDGETS = {
    "dyn": ("dynamical disc mass (MUSE-DARK fit)", lambda g: 10 ** g["m_dyn"]),
    "sed": ("SED stellar mass", lambda g: 10 ** g["m_sed"]),
    "sed_h2": ("SED mass + H₂ (Tacconi, on the main sequence)", lambda g: 10 ** g["m_sed"] * (1 + mu_h2(g["z"], g["m_sed"]))),
    "sed_h2_sfr": ("SED mass + H₂ (Tacconi, offset from SFR)",
                   lambda g: 10 ** g["m_sed"] * (1 + mu_h2(g["z"], g["m_sed"], dms_speagle(g["z"], g["m_sed"], g["sfr"])))),
}


def baryonic_vc2(g, budget, source_budget=False):
    """Keep SED stellar mass TOTAL, partitioned at the released stellar B/T.

    source_budget=True reproduces Karpov's whole-SED-mass disc plus fixed bulge
    for validation only. Molecular gas is assigned entirely to the disc.
    """
    mass = BUDGETS[budget][1](g)
    if budget == "dyn" or source_budget:
        return mass * g["vd1"] + g["vh"] + g["vb"]
    stars = 10 ** g["m_sed"]
    dyn_disc = 10 ** g["m_dyn"]
    dyn_total = dyn_disc + g["m_bulge"]
    disc_mass = stars * dyn_disc / dyn_total + (mass - stars)
    return disc_mass * g["vd1"] + g["vh"] + g["vb"] * stars / dyn_total


def points(sample, budget, source_budget=False):
    """Concatenated log gbar, log gobs (m/s^2), point redshift and galaxy index for one budget."""
    xs, ys, zs, gi = [], [], [], []
    for k, g in enumerate(sample):
        gbar = baryonic_vc2(g, budget, source_budget) / g["r"] * KK_TO_SI
        gobs = g["vc2"] / g["r"] * KK_TO_SI
        ok = (gbar > 0) & (gobs > 0)
        xs.append(np.log10(gbar[ok])); ys.append(np.log10(gobs[ok]))
        zs.append(np.full(ok.sum(), g["z"])); gi.append(np.full(ok.sum(), k))
    return np.concatenate(xs), np.concatenate(ys), np.concatenate(zs), np.concatenate(gi)


# ---------------------------------------------------------------- fits

def model(kind, x, la):
    gb = 10 ** x
    a = 10 ** la
    if kind == "qi":
        return np.log10(gb * np.sqrt(1 + a / gb))
    return np.log10(gb / (1 - np.exp(-np.sqrt(gb / a))))


def fit_scale(kind, x, y):
    ss = np.sum((y[None, :] - model(kind, x[None, :], LG[:, None])) ** 2, axis=1)
    k = int(np.argmin(ss))
    return float(LG[k]), bool(k in (0, len(LG) - 1))


def fit_law(x, y, z, gamma=None):
    """QI function with aQ(z) = A (1+z)^gamma. gamma None: fit both. Returns log10 A, gamma, rms."""
    def ss(p):
        la, gm = (p[0], p[1]) if gamma is None else (p[0], gamma)
        return float(np.mean((y - model("qi", x, la + gm * np.log10(1 + z))) ** 2))
    if gamma is None:
        r = minimize(ss, [-9.9, 1.0], method="Nelder-Mead", options=dict(xatol=1e-5, fatol=1e-10, maxiter=2000))
        return float(r.x[0]), float(r.x[1]), math.sqrt(r.fun)
    grid = LG
    vals = [ss([la]) for la in grid[::8]]
    la0 = grid[::8][int(np.argmin(vals))]
    r = minimize(lambda p: ss(p), [la0], method="Nelder-Mead", options=dict(xatol=1e-6, fatol=1e-12))
    return float(r.x[0]), gamma, math.sqrt(r.fun)


def analyse(sample, budget, edges, source_budget=False):
    x, y, z, gi = points(sample, budget, source_budget)
    gz = np.array([g["z"] for g in sample])
    bins = []
    for i in range(4):
        sel_g = (gz >= edges[i]) & ((gz < edges[i + 1]) if i < 3 else (gz <= edges[i + 1]))
        sel = sel_g[gi]
        lq, eq = fit_scale("qi", x[sel], y[sel])
        lm, em = fit_scale("mcg", x[sel], y[sel])
        bins.append(dict(n_gal=int(sel_g.sum()), z_med=float(np.median(gz[sel_g])), log_aq=lq, log_a0_mcg=lm, edge=eq or em,
                         median_log_gbar=float(np.median(x[sel]))))
    la, gm, rms = fit_law(x, y, z)
    la1, _, rms1 = fit_law(x, y, z, gamma=1.0)
    la0, _, rms0 = fit_law(x, y, z, gamma=0.0)
    return dict(bins=bins, power_law=dict(log_A=la, gamma=gm, rms=rms), one_plus_z=dict(log_A=la1, rms=rms1),
                constant=dict(log_A=la0, rms=rms0), n_points=int(len(x)), n_gal=len(sample))


# ---------------------------------------------------------------- figures

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
        self.xr, self.yr = xr, yr
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

    def axes(self, xt, yt):
        for v in xt:
            self.el.append(f'<line class="gr" x1="{self.X(v):.1f}" x2="{self.X(v):.1f}" y1="{self.t}" y2="{self.b}"/>'
                           f'<text x="{self.X(v):.1f}" y="{self.b + 16}" text-anchor="middle">{v:g}</text>')
        for v in yt:
            self.el.append(f'<line class="gr" x1="{self.l}" x2="{self.r}" y1="{self.Y(v):.1f}" y2="{self.Y(v):.1f}"/>'
                           f'<text x="{self.l - 6}" y="{self.Y(v) + 4:.1f}" text-anchor="end">{v:g}</text>')
        self.el.append(f'<line class="ax" x1="{self.l}" x2="{self.r}" y1="{self.b}" y2="{self.b}"/>'
                       f'<line class="ax" x1="{self.l}" x2="{self.l}" y1="{self.t}" y2="{self.b}"/>')

    def line(self, xs, ys, color, dash=None, tip=None):
        d = " ".join(f"{'M' if i == 0 else 'L'}{self.X(a):.1f},{self.Y(b):.1f}" for i, (a, b) in enumerate(zip(xs, ys)))
        da = f' stroke-dasharray="{dash}"' if dash else ""
        tt = f"<title>{tip}</title>" if tip else ""
        self.el.append(f'<path class="ln" d="{d}" stroke="{color}"{da}>{tt}</path>')

    def errbar(self, x, y, lo, hi, color, tip):
        self.el.append(f'<line x1="{self.X(x):.1f}" x2="{self.X(x):.1f}" y1="{self.Y(lo):.1f}" y2="{self.Y(hi):.1f}" stroke="{color}" stroke-width="2"/>'
                       f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="5" fill="{color}" stroke="var(--surface)" stroke-width="2"><title>{tip}</title></circle>')

    def text(self, x, y, s):
        self.el.append(f'<text x="{x:.1f}" y="{y:.1f}">{s}</text>')

    def legend(self, items, x, y):
        for i, (label, color, dash) in enumerate(items):
            yy = y + i * 18
            da = f' stroke-dasharray="{dash}"' if dash else ""
            self.el.append(f'<line x1="{x}" x2="{x + 24}" y1="{yy}" y2="{yy}" stroke="{color}" stroke-width="2"{da}/>')
            self.text(x + 30, yy + 4, label)

    def save(self, path):
        path.write_text("\n".join(self.el + ["</svg>"]) + "\n")


SAMPLE_LABELS = {
    "data_letter": "data-extent grid, Letter-like cuts",
    "data_all": "data-extent grid, all galaxies",
    "karpov_letter": "Karpov grid (0.2–3 Re), Letter-like cuts",
    "karpov_all": "Karpov grid (0.2–3 Re), all galaxies",
}
SHORT_SAMPLE = {"data_letter": "data grid, Letter-like", "data_all": "data grid, all",
                "karpov_letter": "Karpov grid, Letter-like", "karpov_all": "Karpov grid, all"}
SHORT_BUDGET = {"dyn": "dynamical mass", "sed": "SED mass", "sed_h2": "SED + H₂ (main seq.)", "sed_h2_sfr": "SED + H₂ (from SFR)"}
COLORS = {"dyn": "var(--s1)", "sed": "var(--s3)", "sed_h2": "var(--s4)", "sed_h2_sfr": "var(--s5)"}


def fig_bins(res, path):
    base = res["samples"]["data_letter"]
    p = Plot(760, 520, (0.3, 1.5), (0, 9), "QI scale a_Q fitted per redshift bin, MUSE-DARK rebuilt from public parameters",
             "redshift z", "a_Q (10⁻¹⁰ m s⁻²)")
    p.axes([0.4, 0.6, 0.8, 1.0, 1.2, 1.4], [0, 2, 4, 6, 8])  # noqa
    zz = [0.3 + i * 0.02 for i in range(61)]
    p.line(zz, [2 * C * C * (1 + z) / THETA0 * 1e10 for z in zz], "var(--s2)", tip="published QI, Θ₀ = 8.8 × 10²⁶ m")
    off = {"dyn": -0.02, "sed": 0.0, "sed_h2": 0.02}
    items = [("QI published: 2c²(1+z)/Θ₀", "var(--s2)", None)]
    for b in ("dyn", "sed", "sed_h2"):
        r = base["budgets"][b]
        for i, bn in enumerate(r["bins"]):
            v = 10 ** bn["log_aq"] * 1e10
            lo, hi = r["boot"]["bin_log_aq_16_84"][i]
            p.errbar(bn["z_med"] + off[b], v, 10 ** lo * 1e10, 10 ** hi * 1e10, COLORS[b], f"{BUDGETS[b][0]}: {v:.2f}")
        items.append((BUDGETS[b][0], COLORS[b], None))
    p.legend(items, 80, 62)
    p.save(path)


def fig_gamma(res, path):
    limits = [v for s in res["samples"].values() for b in s["budgets"].values() for v in b["boot"]["gamma_16_84"]]
    p = Plot(1000, 620, (min(-2.0, math.floor(min(limits))), max(6.0, math.ceil(max(limits)))), (0, 17), "Fitted exponent γ in a_Q ∝ (1+z)^γ, with galaxy-bootstrap 16–84% ranges",
             "γ (QI as printed: γ = 1; constant scale: γ = 0)", "", ml=40, mr=300)
    p.axes([-2, -1, 0, 1, 2, 3, 4, 5, 6], [])
    rows = [(s, b) for s in res["samples"] for b in BUDGETS]
    for j, (s, b) in enumerate(rows):
        r = res["samples"][s]["budgets"][b]
        y = 16.3 - j
        lo, hi = r["boot"]["gamma_16_84"]
        p.el.append(f'<line x1="{p.X(lo):.1f}" x2="{p.X(hi):.1f}" y1="{p.Y(y):.1f}" y2="{p.Y(y):.1f}" stroke="{COLORS[b]}" stroke-width="3"/>')
        p.el.append(f'<circle cx="{p.X(r["power_law"]["gamma"]):.1f}" cy="{p.Y(y):.1f}" r="5" fill="{COLORS[b]}"><title>{s}, {BUDGETS[b][0]}: γ = {r["power_law"]["gamma"]:.2f}</title></circle>')
        p.text(p.r + 10, p.Y(y) + 4, f"{SHORT_SAMPLE[s]}: {SHORT_BUDGET[b]}")
    for v in (0, 1):
        p.line([v, v], [0, 17], "var(--ink2)", "3 3")
    p.save(path)


# ---------------------------------------------------------------- main

def pct(a, q):
    return [float(np.percentile(a, v)) for v in q]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=500)
    ap.add_argument("--seed", type=int, default=20261023)
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    zips = fetch()
    params, gals, logz = read_member(zips, "params"), read_member(zips, "galaxies"), read_member(zips, "logz")
    allg = build(params, gals, logz)

    # Anchor: release v2kpc (rotation before pressure correction) against the rebuilt curve.
    rat = np.array([g["v2kpc_model"] / g["v2kpc_release"] for g in allg
                    if g["v2kpc_release"] > 0 and not math.isnan(g["v2kpc_model"])])
    usable = [g for g in allg if "r" in g and 0.33 < g["z"] < 1.44 and g["m_sed"] > 8.8]
    # Pipeline check against Karpov 2026 (his radial grid, his base sample, bins only).
    kg = [g for g in build(params, gals, logz, grid="karpov") if 0.33 < g["z"] < 1.44 and g["m_sed"] > 8.8]
    kedges = np.quantile([g["z"] for g in kg], [0, 0.25, 0.5, 0.75, 1]).tolist()
    karpov_check = dict(n_gal=len(kg), edges=kedges, source_budget=True,
                       ours={b: [10 ** x["log_a0_mcg"] * 1e10 for x in analyse(kg, b, kedges, source_budget=True)["bins"]]
                                                    for b in ("dyn", "sed", "sed_h2")}, karpov_published=KARPOV_BINS_A)
    def letter(sample):
        return [g for g in sample if not (g["logz"] >= 15000) and g["v22_sigma"] > 1]
    samples = {"data_letter": letter(usable), "data_all": usable, "karpov_letter": letter(kg), "karpov_all": kg}
    rng = np.random.default_rng(args.seed)
    res = dict(inputs=dict(sources={k: dict(url=v["url"], sha256=v["sha256"]) for k, v in SOURCES.items()},
                           n_rebuilt=len(allg), n_usable=len(usable), hi_factor="pi", radial_grid="2 kpc to data extent, 0.2 kpc steps"),
               anchors=dict(v2kpc_ratio_median=float(np.median(rat)), v2kpc_ratio_16_84=pct(rat, (16, 84)), n=int(len(rat))),
               karpov_check=karpov_check, wayback_check=wayback_check(params), samples={})
    for sname, sample in samples.items():
        gz = np.array([g["z"] for g in sample])
        edges = np.quantile(gz, [0, 0.25, 0.5, 0.75, 1]).tolist()
        sres = dict(label=SAMPLE_LABELS[sname], n_gal=len(sample), edges=edges, budgets={},
                    n_bulge=sum(g["has_bulge"] for g in sample), source_budget_gamma={})
        for b in BUDGETS:
            sres["source_budget_gamma"][b] = analyse(sample, b, edges, source_budget=True)["power_law"]["gamma"]
            r = analyse(sample, b, edges)
            boots = []
            for _ in range(args.boot):
                bs = [sample[i] for i in rng.integers(0, len(sample), len(sample))]
                try:
                    boots.append(analyse(bs, b, edges))
                except (ValueError, IndexError):
                    pass
            g_b = np.array([x["power_law"]["gamma"] for x in boots])
            a1_b = np.array([x["one_plus_z"]["log_A"] for x in boots])
            r["boot"] = dict(n=len(boots),
                             gamma_16_84=pct(g_b, (16, 84)), gamma_2p5_97p5=pct(g_b, (2.5, 97.5)),
                             frac_gamma_ge_1=float(np.mean(g_b >= 1)), frac_gamma_le_0=float(np.mean(g_b <= 0)),
                             one_plus_z_log_A_16_84=pct(a1_b, (16, 84)),
                             bin_log_aq_16_84=[pct([x["bins"][i]["log_aq"] for x in boots], (16, 84)) for i in range(4)],
                             bin_log_a0_mcg_16_84=[pct([x["bins"][i]["log_a0_mcg"] for x in boots], (16, 84)) for i in range(4)])
            for i, bn in enumerate(r["bins"]):
                bn["aq_published"] = 2 * C * C * (1 + bn["z_med"]) / THETA0
                bn["ratio_fit_over_published"] = 10 ** bn["log_aq"] / bn["aq_published"]
            r["one_plus_z"]["theta0_equiv_m"] = 2 * C * C / 10 ** r["one_plus_z"]["log_A"]
            sres["budgets"][b] = r
        res["samples"][sname] = sres
    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    fig_bins(res, OUT / "fig-1-aq-per-bin.svg")
    fig_gamma(res, OUT / "fig-2-gamma.svg")
    (OUT / "summary.md").write_text(summary(res))
    print((OUT / "summary.md").read_text())


def summary(r):
    L = ["# A6b results (generated by musedark_qi.py; do not edit)", "",
         "Editorial analysis. SED budgets partition the total stellar mass at the released stellar B/T; molecular gas follows the disc. "
         "Bootstrap fractions describe resampled fits, not posterior probabilities or calibrated rejection probabilities.", ""]
    a = r["anchors"]
    L += [f"Rebuilt galaxies: {r['inputs']['n_rebuilt']}; usable (0.33 < z < 1.44, SED log M★ > 8.8, data beyond 2.2 kpc): {r['inputs']['n_usable']}.",
          f"Anchor: rebuilt v_⊥(2 kpc) / release v2kpc = {a['v2kpc_ratio_median']:.3f} (16–84%: {a['v2kpc_ratio_16_84'][0]:.3f}–{a['v2kpc_ratio_16_84'][1]:.3f}, N = {a['n']}).", ""]
    k = r["karpov_check"]
    L += [f"Pipeline check on Karpov's grid and base sample ({k['n_gal']} galaxies), using his original mass bookkeeping (whole SED mass in disc plus fixed bulge), McGaugh a₀ per bin, ours / Karpov 2026:", "",
          "| Budget | bin 1 | bin 2 | bin 3 | bin 4 |", "|---|---|---|---|---|"]
    for b, v in k["ours"].items():
        L.append(f"| {BUDGETS[b][0]} | " + " | ".join(f"{x:.2f} / {y:.2f}" for x, y in zip(v, k["karpov_published"][b])) + " |")
    L.append("")
    w = r["wayback_check"]
    if w.get("available"):
        L += [f"Cross-check of Karpov's halo parameters against the Internet Archive copy of DC14_bestfit.txt (7 January 2026; "
              f"{w['n_common']} galaxies in common, {w['n_archive']} in the archive, {w['n_karpov']} in Karpov's table). "
              "Not an input to the fits.", "",
              "| Parameter | Karpov vs archive | median | 16–84% | galaxies off by > 10% |", "|---|---|---|---|---|"]
        for col, c in w["columns"].items():
            L.append(f"| {col} | {c['kind']} | {c['median']:.3f} | {c['p16_84'][0]:.3f} to {c['p16_84'][1]:.3f} | {c['n_off_10pct']} of {c['n']} |")
        L.append("")
    else:
        L += [f"Archive cross-check unavailable: {w.get('reason')}.", ""]
    for sname, s in r["samples"].items():
        L += [f"## {s['label']} ({s['n_gal']} galaxies; z edges " + ", ".join(f"{e:.3f}" for e in s["edges"]) + ")", ""]
        L += [f"{s['n_bulge']} galaxies have a bulge. Exponents before correcting the SED mass bookkeeping: " +
              ", ".join(f"{b}: {g:.2f}" for b, g in s["source_budget_gamma"].items()) + ".", ""]
        L += ["McGaugh-function a₀ per bin (10⁻¹⁰ m s⁻²), against the published bins 1.99 / 2.20 / 2.57 / 2.71:", "",
              "| Budget | bin 1 | bin 2 | bin 3 | bin 4 |", "|---|---|---|---|---|"]
        for b, br in s["budgets"].items():
            L.append(f"| {BUDGETS[b][0]} | " + " | ".join(f"{10 ** x['log_a0_mcg'] * 1e10:.2f}" for x in br["bins"]) + " |")
        L += ["", "QI scale a_Q per bin (10⁻¹⁰ m s⁻²; bootstrap 16–84%) and ratio to the published 2c²(1+z)/Θ₀:", "",
              "| Budget | " + " | ".join(f"bin {i + 1} (z̃ = {s['budgets']['dyn']['bins'][i]['z_med']:.2f})" for i in range(4)) + " |",
              "|---|---|---|---|---|"]
        for b, br in s["budgets"].items():
            cells = []
            for i, x in enumerate(br["bins"]):
                lo, hi = br["boot"]["bin_log_aq_16_84"][i]
                cells.append(f"{10 ** x['log_aq'] * 1e10:.2f} ({10 ** lo * 1e10:.2f}–{10 ** hi * 1e10:.2f}); ×{x['ratio_fit_over_published']:.2f}")
            L.append(f"| {BUDGETS[b][0]} | " + " | ".join(cells) + " |")
        L += ["", "Redshift law for a_Q, fitted to all points (rms in dex):", "",
              "| Budget | γ (bootstrap 16–84%; 2.5–97.5%) | bootstrap fraction γ ≥ 1 | bootstrap fraction γ ≤ 0 | (1+z) law: a_Q(0), equiv. Θ₀ | rms (1+z) | rms constant | rms free γ |",
              "|---|---|---|---|---|---|---|---|"]
        for b, br in s["budgets"].items():
            bt = br["boot"]
            L.append(f"| {BUDGETS[b][0]} | {br['power_law']['gamma']:.2f} ({bt['gamma_16_84'][0]:.2f} to {bt['gamma_16_84'][1]:.2f}; "
                     f"{bt['gamma_2p5_97p5'][0]:.2f} to {bt['gamma_2p5_97p5'][1]:.2f}) | {bt['frac_gamma_ge_1']:.2f} | {bt['frac_gamma_le_0']:.2f} | "
                     f"{10 ** br['one_plus_z']['log_A'] * 1e10:.2f}, {br['one_plus_z']['theta0_equiv_m']:.3g} m | "
                     f"{br['one_plus_z']['rms']:.4f} | {br['constant']['rms']:.4f} | {br['power_law']['rms']:.4f} |")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


if __name__ == "__main__":
    main()
