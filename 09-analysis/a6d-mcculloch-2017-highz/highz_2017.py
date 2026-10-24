"""A6d: reproduce McCulloch's 2017 high-redshift comparisons, then apply his own equations to the same data.

Editorial analysis for the Quantized Inertia research archive. Python 3 standard library only.

McCulloch 2017 (Ap&SS 362, 149; arXiv:1709.04918), Sect. 4, makes two high-z comparisons:
1. Tully-Fisher: Eq. 13 gives M = v^4 Theta_now / (2 G c^2 (1+z)), so at fixed v the mass falls by log10(1+z).
   He compares -0.28 and -0.52 dex with Uebler et al. 2017 at z = 0.9 and 2.3.
2. Genzel et al. 2017: the observed acceleration of six galaxies against the QI "minimum acceleration"
   2c^2/Theta(z), Theta(z) = Theta_now/(1+z). He reports QI 9-19% higher for the four lower-z galaxies.

Inputs are typed from the source tables (numbers only), with locations given below.

Run:  python3 -I 09-analysis/a6d-mcculloch-2017-highz/highz_2017.py
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
C = 2.99792458e8
THETA0 = 8.8e26            # McCulloch 2017
KK_TO_SI = 1e6 / 3.0856775814913673e19
A_Q0 = 2 * C * C / THETA0  # 2.04e-10 m/s^2

# Genzel et al. 2017, Nature 543, 397, Table 1 (arXiv:1703.04310v1 p. 4):
# name, z, H-band R1/2 (kpc), R1/2 of the n=1 fit (kpc), vc(R1/2) (km/s), fDM(R1/2), its +-2 rms or upper limit
GENZEL = [
    ("COS4 01351", 0.854, 8.6, 7.3, 276, 0.21, "±0.1"),
    ("D3a 6397", 1.500, 5.9, 7.4, 310, 0.17, "<0.38"),
    ("GS4 43501", 1.613, 4.9, 4.9, 257, 0.19, "±0.09"),
    ("zC 406690", 2.196, 5.5, 5.5, 301, 0.00, "<0.08"),
    ("zC 400569", 2.242, 4.0, 3.3, 364, 0.00, "<0.07"),
    ("D3a 15504", 2.383, 6.3, 6.0, 299, 0.12, "<0.26"),
]
# Uebler et al. 2017, ApJ 842, 121 (arXiv:1703.04321v2), Sect. 3.3 and Fig. 5: baryonic TFR, local slope a = 3.75
# (Lelli et al. 2016), v_ref = 242 km/s. Zero points b and offsets from the local relation.
UEBLER = dict(
    btfr=dict(z=[0.9, 2.3], b=[10.68, 10.85], b_err=[0.04, 0.05], offset_from_local=[-0.44, -0.27]),
    stfr=dict(z=[0.9, 2.3], offset_from_local=[-0.44, -0.42]),
    evolution_first_order_sample=0.28, evolution_w16_sample=0.20,
)
# McCulloch 2017's quoted ranges for the observed mass reduction (Sect. 4).
MCCULLOCH_QUOTED = {"0.9": [-0.38, -0.47], "2.3": [-0.2, -0.47]}
SPARC_A0 = 1.2e-10   # local deep-MOND BTFR normalisation (McGaugh et al. 2016), for the absolute zero-point check


def genzel():
    rows = []
    for name, z, rh, r1, vc, f, ferr in GENZEL:
        a_min = 2 * C * C * (1 + z) / THETA0
        g_n1 = vc ** 2 / r1 * KK_TO_SI
        g_h = vc ** 2 / rh * KK_TO_SI
        gbar = (1 - f) * g_n1
        g_qi = gbar * math.sqrt(1 + a_min / gbar)          # McCulloch 2017 Eq. 8 with Theta(z)
        rows.append(dict(name=name, z=z, a_min=a_min, g_obs_n1=g_n1, g_obs_hband=g_h,
                         ratio_min_over_obs_n1=a_min / g_n1, ratio_min_over_obs_hband=a_min / g_h,
                         gbar=gbar, g_qi_eq8=g_qi, ratio_eq8_over_obs=g_qi / g_n1,
                         fdm_obs=f, fdm_obs_err=ferr, fdm_qi_eq8=1 - gbar / g_qi,
                         below_minimum=g_n1 < a_min))
    return rows


def uebler():
    out = []
    for i, z in enumerate(UEBLER["btfr"]["z"]):
        rel = -math.log10(1 + z)                                        # Eq. 13 relative to QI at z = 0
        absolute = rel - math.log10(A_Q0 / SPARC_A0)                    # also shift QI's z = 0 scale against SPARC's
        out.append(dict(z=z, qi_relative=rel, qi_absolute_vs_local=absolute,
                        observed_btfr=UEBLER["btfr"]["offset_from_local"][i],
                        observed_stfr=UEBLER["stfr"]["offset_from_local"][i],
                        mcculloch_quoted=MCCULLOCH_QUOTED[str(z)]))
    b, e = UEBLER["btfr"]["b"], UEBLER["btfr"]["b_err"]
    obs = b[1] - b[0]
    err = math.hypot(*e)
    pred = -math.log10((1 + 2.3) / (1 + 0.9))
    within = dict(observed=obs, observed_err=err, qi_predicted=pred, difference_in_sigma=(obs - pred) / err,
                  alternative_samples=dict(first_order=UEBLER["evolution_first_order_sample"], w16=UEBLER["evolution_w16_sample"]))
    return out, within


STYLE = """<style>
svg { --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --grid:#e4e3df; --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; }
@media (prefers-color-scheme: dark) { svg { --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --grid:#33322f; --s1:#3987e5; --s2:#d95926; --s3:#199e70; } }
text { font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: var(--ink2); font-size: 12px; }
.t { fill: var(--ink); font-size: 14px; font-weight: 600; }
</style>"""


def fig(rows, path):
    w, h, ml, mr, mt, mb = 620, 560, 64, 20, 44, 50
    lo, hi = 2.0, 17.0
    X = lambda v: ml + (v - lo) / (hi - lo) * (w - ml - mr)
    Y = lambda v: h - mb - (v - lo) / (hi - lo) * (h - mt - mb)
    el = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">',
          "<title>Genzel et al. 2017 galaxies: observed acceleration against QI predictions</title>", STYLE,
          f'<rect width="{w}" height="{h}" fill="var(--surface)"/>',
          f'<text class="t" x="{ml}" y="24">Six Genzel et al. 2017 galaxies: observed vs QI (10⁻¹⁰ m s⁻²)</text>',
          f'<text x="{(ml + w - mr) / 2}" y="{h - 12}" text-anchor="middle">observed v_c²/R₁/₂</text>',
          f'<text transform="translate(16,{(mt + h - mb) / 2}) rotate(-90)" text-anchor="middle">QI value</text>']
    for v in (2, 5, 8, 11, 14, 17):
        el.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{mt}" y2="{h - mb}" stroke="var(--grid)"/>'
                  f'<text x="{X(v):.1f}" y="{h - mb + 16}" text-anchor="middle">{v}</text>'
                  f'<line x1="{ml}" x2="{w - mr}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="var(--grid)"/>'
                  f'<text x="{ml - 6}" y="{Y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    el.append(f'<line x1="{X(lo):.1f}" y1="{Y(lo):.1f}" x2="{X(hi):.1f}" y2="{Y(hi):.1f}" stroke="var(--ink2)" stroke-dasharray="3 3"/>')
    for r in rows:
        x = r["g_obs_n1"] * 1e10
        for key, col, lab in (("a_min", "var(--s2)", "2017 Fig. 2: minimum acceleration 2c²(1+z)/Θ₀"),
                              ("g_qi_eq8", "var(--s1)", "2017 Eq. 8 with Genzel's baryonic acceleration")):
            y = r[key] * 1e10
            el.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="5" fill="{col}" stroke="var(--surface)" stroke-width="2">'
                      f'<title>{r["name"]} (z = {r["z"]}): {lab} = {y:.2f}; observed {x:.2f}</title></circle>')
        el.append(f'<text x="{X(x) + 7:.1f}" y="{Y(r["a_min"] * 1e10) - 6:.1f}">{r["z"]}</text>')
    for i, (lab, col) in enumerate((("McCulloch 2017 Fig. 2: minimum acceleration", "var(--s2)"),
                                    ("2017 Eq. 8 applied to Genzel's baryons", "var(--s1)"))):
        y = 64 + 18 * i
        el.append(f'<circle cx="{ml + 22}" cy="{y}" r="5" fill="{col}"/><text x="{ml + 34}" y="{y + 4}">{lab}</text>')
    el.append(f'<text x="{X(11):.1f}" y="{Y(10.2):.1f}">line of agreement</text>')
    path.write_text("\n".join(el + ["</svg>"]) + "\n")


def main():
    OUT.mkdir(exist_ok=True)
    g = genzel()
    u, within = uebler()
    res = dict(theta0_m=THETA0, a_q0=A_Q0, genzel=g, uebler=dict(per_redshift=u, within_sample=within, inputs=UEBLER))
    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False, allow_nan=False) + "\n")
    fig(g, OUT / "fig-1-genzel-comparison.svg")
    L = ["# A6d results (generated by highz_2017.py; do not edit)", "",
         f"QI scale today a_Q(0) = 2c²/Θ₀ = {A_Q0 * 1e10:.3f} × 10⁻¹⁰ m s⁻² (Θ₀ = 8.8 × 10²⁶ m).", "",
         "## Genzel et al. 2017 (accelerations in 10⁻¹⁰ m s⁻²)", "",
         "| Galaxy | z | observed v_c²/R₁/₂ (n=1 radius) | QI minimum 2c²(1+z)/Θ₀ | minimum ÷ observed | same, H-band radius | Eq. 8 prediction | Eq. 8 ÷ observed | f_DM observed | f_DM from Eq. 8 |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in g:
        L.append(f"| {r['name']} | {r['z']} | {r['g_obs_n1'] * 1e10:.2f} | {r['a_min'] * 1e10:.2f} | {r['ratio_min_over_obs_n1']:.2f} | "
                 f"{r['ratio_min_over_obs_hband']:.2f} | {r['g_qi_eq8'] * 1e10:.2f} | {r['ratio_eq8_over_obs']:.2f} | "
                 f"{r['fdm_obs']:.2f} ({r['fdm_obs_err']}) | {r['fdm_qi_eq8']:.2f} |")
    nb = sum(r["below_minimum"] for r in g)
    L += ["", f"Observed acceleration below the QI minimum in {nb} of {len(g)} galaxies (n=1 radius).", "",
          "## Übler et al. 2017 baryonic Tully–Fisher relation (dex of mass at fixed velocity)", "",
          "| z | observed bTFR offset from local | observed sTFR offset | McCulloch's quoted range | QI Eq. 13, relative to QI at z = 0 | QI absolute, relative to the SPARC normalisation |",
          "|---|---|---|---|---|---|"]
    for r in u:
        L.append(f"| {r['z']} | {r['observed_btfr']:+.2f} | {r['observed_stfr']:+.2f} | {r['mcculloch_quoted'][0]:+.2f} to {r['mcculloch_quoted'][1]:+.2f} | "
                 f"{r['qi_relative']:+.2f} | {r['qi_absolute_vs_local']:+.2f} |")
    L += ["", f"Within Übler's sample, z ≈ 0.9 → 2.3: observed bTFR zero point changes by {within['observed']:+.2f} ± {within['observed_err']:.2f} dex; "
          f"QI predicts {within['qi_predicted']:+.2f} dex (difference {within['difference_in_sigma']:.1f} σ, statistical errors only). "
          f"Übler's alternative samples give +{UEBLER['evolution_first_order_sample']:.2f} and +{UEBLER['evolution_w16_sample']:.2f} dex."]
    (OUT / "summary.md").write_text("\n".join(L) + "\n")
    print((OUT / "summary.md").read_text())


if __name__ == "__main__":
    main()
