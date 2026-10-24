"""A3: ledger of quantitative QI thrust predictions against measured or claimed thrusts.

Standard library only. Every input is transcribed from the source named in its row (table or
equation number); nothing is downloaded. The script
  - recomputes printed predictions from their printed inputs,
  - forms an upper limit for each null measurement and the ratio prediction / limit,
  - compares the author's fitted predictions with the claimed thrusts they were fitted to,
  - writes results/summary.md, results/ledger.csv, results/results.json and
    results/fig-1-specific-thrust.svg.

Run: python3 -I 09-analysis/a3-thrust-ledger/thrust_ledger.py
"""
import csv
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
A1_DIR = HERE.parent / "a1-sparc-rar-refit"

C = 299_792_458.0
G0 = 9.80665
HBAR = 1.054_571_817e-34
QE = 1.602_176_634e-19
ME = 9.109_383_7015e-31
NN, UN, MN = 1e-9, 1e-6, 1e-3
K_SIGMA = 2.0          # upper limit = max(measured, 0) + K_SIGMA * sigma
PHOTON = 1 / C         # photon-rocket limit, N/W

# Short source keys; README.md maps them to repository folders.
SRC = {
    "N21": "Neunzig, Weikert & Tajmar 2021/22, CEAS Space J. 14, 45",
    "N22": "Neunzig, Weikert & Tajmar 2022, Acta Astronaut. 195, 583",
    "T21": "Tajmar, Neunzig & Weikert 2021/22, CEAS Space J. 14, 31",
    "T20": "Tajmar & Schreiber 2020, J. Electrostat. 107, 103477",
    "M15p": "McCulloch 2015, Prog. Phys. 11, 78",
    "M15e": "McCulloch 2015, EPL 111, 60005",
    "M17": "McCulloch 2017, EPL 118, 34003",
    "M18": "McCulloch 2018, J. Space Explor. 7(3)",
    "M21": "McCulloch 2021, preprint (symmetric capacitors)",
    "M22": "McCulloch 2022, preprint (QI thrust as asymmetric Casimir effect)",
    "blog": "McCulloch, physicsfromtheedge blog",
    "IVO": "IVO Ltd press claims (2022–2023)",
}


# ---------------------------------------------------------------------------
# Prediction formulas, as printed
# ---------------------------------------------------------------------------
def f_ps(p, s):
    """Dresden's worst-case adaptation F = PS/c (S = force amplification, round trips or windings)."""
    return p * s / C


def f_pip(p, q, l, w_big, w_small):
    """McCulloch 2015 Prog. Phys. Eq. 10, magnitude: F = (PQl/c)(1/W_small - 1/W_big)."""
    return p * q * l / C * (1 / w_small - 1 / w_big)


def f_epl(p, q, l, w_big, w_small, n_big=1.0, n_small=1.0):
    """McCulloch 2015 EPL Eq. 14 (n = 1) and 2017 EPL Eq. 13 (dielectrics), sign of the 2015 Eq. 2.

    Positive = towards the narrow end. A2's README for the 2017 paper notes that the printed Eq. 13
    has the opposite overall sign; its Table 1 uses this convention.
    """
    return 6 * p * q * l / C * (1 / (n_small * (l + 4 * w_small)) - 1 / (n_big * (l + 4 * w_big)))


def f_met(p, q):
    """McCulloch 2018 Eq. 9 with dx_left = L/2, dx_right = Theta; reduces to PQ/c (1 - L/2Theta)."""
    return p * q / C


def f_casimir(p, q, v, area, d, c=C):
    """McCulloch 2022 Eq. 5: F = pi^2 P Q c^2 A / (240 c v^2 d^2)."""
    return math.pi ** 2 * p * q * c ** 2 * area / (240 * c * v ** 2 * d ** 2)


def f_capacitor_2021(current, s, n):
    """McCulloch 2021 Eq. 6: F = N_e hbar c / (2 n s^2), with N_e = I/q as in the preprint."""
    return current / QE * HBAR * C / (2 * n * s ** 2)


def v_electron(volts):
    """McCulloch 2022 Sec. 7: mean electron speed with v^2 = (1/4)(2 q V / m_e)."""
    return math.sqrt(QE * volts / (2 * ME))


# ---------------------------------------------------------------------------
# A. Controlled measurements with stated uncertainties (TU Dresden)
# ---------------------------------------------------------------------------
def controlled():
    rows = []

    def add(device, setting, src, p, pred, basis, m, s, unit=NN, lower_bound=False, s_amp=None,
            printed=None, upper=None, note=""):
        rows.append(dict(group="controlled", device=device, setting=setting, src=src, power=p,
                         pred=pred, pred_lower_bound=lower_bound, basis=basis, s_amp=s_amp,
                         printed_pred=printed, obs=None if m is None else m * unit,
                         sigma=None if s is None else s * unit, upper_given=upper, note=note))

    # N21 Table 2: metal cavities, F = PS/c (S = 9 copper, 39 silver).
    t2 = {"concave/convex": [(0.109, 9, 3, 0.39, 0.19), (0.292, 9, 8, 1.02, 0.15), (0.497, 9, 14, 1.67, 0.16),
                             (0.292, 39, 38, 1.08, 0.18), (0.497, 39, 65, 1.73, 0.24)],
          "concave/concave": [(0.109, 9, 3, 0.40, 0.15), (0.292, 9, 8, 1.03, 0.14), (0.497, 9, 14, 1.65, 0.22),
                              (0.292, 39, 38, 1.28, 0.34), (0.497, 39, 65, 1.76, 0.28)],
          "circle": [(0.109, 9, 3, 0.34, 0.28), (0.292, 9, 8, 1.12, 0.25), (0.497, 9, 14, 1.71, 0.27),
                     (0.292, 39, 38, 1.13, 0.27), (0.497, 39, 65, 1.89, 0.24)]}
    for shape, rr in t2.items():
        for p, s_amp, pr, m, s in rr:
            dev = "Copper laser cavities (S = 9)" if s_amp == 9 else "Silver laser cavities (S = 39)"
            add(dev, f"{shape}, {p * 1e3:.0f} mW", "N21 Table 2", p, f_ps(p, s_amp), "Dresden F = PS/c",
                m, s, s_amp=s_amp, printed=pr * NN)
    # N22 Table B3: Ag-plated resonators (S not printed; 60 nN at 467 mW implies S = 39).
    for shape, p, pr, m, s in [("concave/convex", 0.467, 60, 1.52, 0.41), ("concave/concave", 0.279, 36, 1.04, 0.12),
                               ("concave/concave", 0.467, 60, 1.65, 0.14), ("circle", 0.279, 36, 0.89, 0.14),
                               ("circle", 0.467, 60, 1.50, 0.17)]:
        add("Silver-plated cavities, repeat (S = 39)", f"{shape}, {p * 1e3:.0f} mW", "N22 Table B3", p,
            f_ps(p, 39), "Dresden F = PS/c", m, s, s_amp=39, printed=pr * NN)
    # N21 Table 4: Taylor-like resonators. Taylor Classic: only the differential run isolates the device.
    for name, s_amp, rr in [("Light", 500, [(0.292, 487, 1.03, 0.14), (0.497, 828, 1.78, 0.31)]),
                            ("Dual Crystal", 500, [(0.292, 487, 1.14, 0.57), (0.497, 828, 1.62, 0.15)]),
                            ("Halfway Crystal", 908, [(0.292, 885, 0.97, 0.12), (0.497, 1505, 1.75, 0.32)]),
                            ("Classic, differential", 624, [(0.292, 608, 0.43, 0.87), (0.497, 1035, 0.18, 1.53)])]:
        for p, pr, m, s in rr:
            add("Taylor laser resonators (S = 500–908)", f"{name}, {p * 1e3:.0f} mW", "N21 Table 4", p,
                f_ps(p, s_amp), "Dresden F = PS/c", m, s, s_amp=s_amp, printed=pr * NN)
    # N22 Table B4: Taylor-Light inside a tapered metal cavity (McCulloch's requested change).
    for p, pr, m, s in [(0.289, 482, 1.01, 0.30), (0.493, 822, 1.62, 0.26)]:
        add("Taylor-Light in tapered metal cone (S = 500)", f"{p * 1e3:.0f} mW", "N22 Table B4", p, f_ps(p, 500),
            "Dresden F = PS/c", m, s, s_amp=500, printed=pr * NN)
    # N21 Table 5: fibre loops. Windings are minimum counts, so the predictions are lower bounds.
    for p, pr, m, s in [(0.031, 420, 0.02, 1.42), (0.210, 2809, 0.50, 1.44)]:
        add("Symmetric fibre loop + Unruh shield, differential (S > 4000)", f"{p * 1e3:.0f} mW, in air",
            "N21 Table 5", p, f_ps(p, 4000), "Dresden F = PS/c", m, s, lower_bound=True, s_amp=4000, printed=pr * NN)
    for shield, rr in [("no shield", [(0.031, 341, 0.02, 0.23), (0.203, 2234, 0.08, 0.26)]),
                       ("shield at small radius", [(0.031, 341, 0.09, 0.33), (0.203, 2234, 0.02, 0.34)]),
                       ("shield at big radius", [(0.031, 341, 0.09, 0.31), (0.203, 2234, 0.10, 0.39)])]:
        for p, pr, m, s in rr:
            add("Asymmetric fibre loop, vacuum (S > 3300)", f"{shield}, {p * 1e3:.0f} mW", "N21 Table 5", p,
                f_ps(p, 3300), "Dresden F = PS/c", m, s, lower_bound=True, s_amp=3300, printed=pr * NN)
    # N22 Table B5: the same loop outside the vacuum chamber (McCulloch's requested change), µN units.
    for shield, rr in [("no shield", [(0.031, 0.34, 0.02, 0.26), (0.203, 2.23, 0.05, 0.30)]),
                       ("shield at small radius", [(0.031, 0.34, 0.01, 0.19), (0.203, 2.23, 0.09, 0.18)]),
                       ("shield at big radius", [(0.031, 0.34, 0.02, 0.15), (0.203, 2.23, 0.06, 0.16)])]:
        for p, pr, m, s in rr:
            add("Asymmetric fibre loop, air, no metal within 80 m (S = 3300)", f"{shield}, {p * 1e3:.0f} mW",
                "N22 Table B5", p, f_ps(p, 3300), "Dresden F = PS/c", m, s, unit=UN,
                lower_bound=shield != "no shield", s_amp=3300, printed=pr * UN)
    # N22 Table B1 / B2: EmDrives, F = PQ/c with loaded Q.
    for f, q, p, pr, m, s in [(1918, 113, 6, 2261, 13, 31), (1945, 486, 4.2, 6808, -7, 18),
                              (2030, 677, 10, 22582, -4, 38), (2054, 1027, 5.5, 18841, -11, 25)]:
        add("EmDrive, spherical end cap (Q = 113–1027)", f"{f} MHz, {p:g} W", "N22 Table B1", p, f_ps(p, q),
            "Dresden F = PQ/c", m, s, s_amp=q, printed=pr * NN)
    for f, q, p, pr, m, s in [(1819, 2599, 19, 164, 0.14, 0.23), (1959, 2063, 18, 156, -0.33, 0.54)]:
        add("Superconducting EmDrive (Q = 2063–2599)", f"{f} MHz, {p:g} W", "N22 Table B2", p, f_ps(p, q),
            "Dresden F = PQ/c", m, s, unit=UN, s_amp=q, printed=pr * UN)
    # T21 Table 1: White-geometry replica. Tajmar et al. give no QI number; we apply N22's convention.
    for f, q, p, m, s in [(1857, 741, 6, 0.003, 0.02), (1914, 477, 6.5, 0.007, 0.01),
                          (1943, 430, 3, -0.009, 0.01), (1984, 330, 7, 0.004, 0.02)]:
        add("EmDrive, White-geometry replica (Q = 330–741)", f"{f} MHz, {p:g} W", "T21 Table 1", p, f_ps(p, q),
            "editorial: Dresden's F = PQ/c applied", m, s, unit=UN, s_amp=q)
    # N21 Table 3: BART LED cavity. The comparison value is the device's claimed thrust, not QI.
    add("BART LED cavity (claimed 2700 nN; not a QI number)", "1540 mW", "N21 Table 3", 1.54, 2700 * NN,
        "device claim, not QI", 0.22, 4.13)
    # T20 Table 1, Sec. 4.5: leakage-current capacitor. The paper's limit is already 3 sigma.
    lim = 0.3e-6 * G0
    cap = dict(volts=2100, current=10e-6, power=0.021, r=0.020, s=90e-6)
    add("Leakage-current capacitor (Bhatt–Becker extrapolation; not QI)", "2.1 kV, 10 µA", "T20 Table 1", 0.021,
        6.8e-6 * G0, "empirical fit, not QI", None, None, upper=lim)
    for n in (1.0, 1.2):
        add("Leakage-current capacitor (QI formulas applied by us)", f"2021 Eq. 6, n = {n:g}", "T20 Table 1", 0.021,
            f_capacitor_2021(cap["current"], cap["s"], n), "editorial: McCulloch 2021 Eq. 6 applied",
            None, None, upper=lim)
    add("Leakage-current capacitor (QI formulas applied by us)", "2022 Eq. 5, Q = 1", "T20 Table 1", 0.021,
        f_casimir(cap["power"], 1, v_electron(cap["volts"]), math.pi * cap["r"] ** 2, cap["s"]),
        "editorial: McCulloch 2022 Eq. 5 applied", None, None, upper=lim)
    # McCulloch's own 2022 revised (photon) predictions against the Dresden data.
    # Eq. 7 is for 0.203 W; Eq. 5 is linear in P, so we scale it to Dresden's silver-cavity powers.
    for shape, rr in t2.items():
        for p, s_amp, _, m, s in rr:
            if s_amp == 39:
                add("Silver laser cavities: McCulloch 2022 revised prediction", f"{shape}, {p * 1e3:.0f} mW",
                    "N21 Table 2", p, 0.4 * NN * p / 0.203, "McCulloch 2022 Eq. 7, scaled ∝ P (editorial)", m, s,
                    note="anomalous: compared with measured − P/c")
    for shield, rr in [("no shield", (0.08, 0.26)), ("shield at small radius", (0.02, 0.34)),
                       ("shield at big radius", (0.10, 0.39))]:
        add("Asymmetric fibre loop, vacuum: McCulloch 2022 revised prediction", f"{shield}, 203 mW", "N21 Table 5",
            0.203, 40 * NN, "McCulloch 2022 Eq. 9 as printed", *rr)
    for shield, rr in [("no shield", (0.05, 0.30)), ("shield at small radius", (0.09, 0.18)),
                       ("shield at big radius", (0.06, 0.16))]:
        add("Asymmetric fibre loop, air: McCulloch 2022 revised prediction", f"{shield}, 203 mW", "N22 Table B5",
            0.203, 40 * NN, "McCulloch 2022 Eq. 9 as printed", *rr, unit=UN)
    for r in rows:
        r["recomputed"] = r["pred"]
        if r["printed_pred"] is not None:
            r["pred"] = r["printed_pred"]
        anomalous = r["note"].startswith("anomalous")
        if r["upper_given"] is not None:
            r["upper"] = r["upper_given"]
        else:
            base = r["obs"] - (r["power"] / C if anomalous else 0.0)
            r["upper"] = max(base, 0.0) + K_SIGMA * r["sigma"]
        r["ratio"] = r["pred"] / r["upper"]
        r["ratio_central"] = None if r["obs"] is None or anomalous else r["pred"] / abs(r["obs"])
        r["photon"] = r["power"] / C
    return rows


# ---------------------------------------------------------------------------
# B. Author's predictions compared with claimed positive thrusts
# ---------------------------------------------------------------------------
EMDRIVE = {  # (P W, Q, L m, w_big m, w_small m, n_big, n_small) from McCulloch 2017 Table 1
    "Shawyer 1": (850, 5900, 0.156, 0.16, 0.1275, 1.0, 6.16),
    "Shawyer 2": (1000, 45000, 0.345, 0.28, 0.1289, 1.0, 1.0),
    "Cannae": (10.5, 11e6, 0.03, 0.22, 0.2, 1.0, 1.0),
    "NASA 2014 (16.9 W)": (16.9, 7320, 0.2286, 0.2794, 0.1588, 1.0, 1.46),
    "NASA 2014 (16.7 W)": (16.7, 18100, 0.2286, 0.2794, 0.1588, 1.0, 1.46),
    "NASA 2014 (2.6 W)": (2.6, 22000, 0.2286, 0.2794, 0.1588, 1.0, 1.46),
    "NASA 2014 (50 W)": (50, 6730, 0.2286, 0.2794, 0.1588, 1.0, 1.46),
    "Tajmar & Fiedler 2015": (700, 20, 0.1008, 0.1062, 0.075, 1.0, 1.0),
    "NASA 2016 (40 W)": (40, 7123, 0.229, 0.279, 0.159, 1.0, 1.46),
    "NASA 2016 (60 W)": (60, 7123, 0.229, 0.279, 0.159, 1.0, 1.46),
    "NASA 2016 (80 W)": (80, 7123, 0.229, 0.279, 0.159, 1.0, 1.46),
}
# (printed F_-d, printed F_+d, observed lo, observed hi), mN, from the same table
EMDRIVE_PRINTED = {
    "Shawyer 1": (3.8, -15.84, 16, 16), "Shawyer 2": (149, 148.85, 80, 214), "Cannae": (7.3, 7.34, 9, 9),
    "NASA 2014 (16.9 W)": (0.23, 0.03, 0.091, 0.091), "NASA 2014 (16.7 W)": (0.57, 0.07, 0.05, 0.05),
    "NASA 2014 (2.6 W)": (0.11, 0.01, 0.055, 0.055), "NASA 2014 (50 W)": (0.64, 0.08, 0.03, 0.03),
    "Tajmar & Fiedler 2015": (0.02, 0.02, 0.02, 0.11), "NASA 2016 (40 W)": (0.54, 0.06, 0.04, 0.04),
    "NASA 2016 (60 W)": (0.81, 0.09, 0.09, 0.09), "NASA 2016 (80 W)": (1.08, 0.13, 0.09, 0.09),
}
PIP = {  # McCulloch 2015 Prog. Phys. Table 1: (P, Q, l, W_big, W_small, printed mN)
    "Shawyer 1": (850, 5900, 0.156, 0.16, 0.1275, 4.2), "Shawyer 2": (1000, 45000, 0.345, 0.28, 0.1289, 216),
    "NASA B1": (16.9, 7320, 0.332, 0.397, 0.244, 0.22), "NASA B2": (16.7, 18100, 0.332, 0.397, 0.244, 0.53),
    "NASA B3": (2.6, 22000, 0.332, 0.397, 0.244, 0.1),
}


def claimed():
    rows = []

    def add(device, model, src, p, pred, lo, hi, src_obs, printed=None, note=""):
        rows.append(dict(group="claimed", device=device, model=model, src=src, power=p, pred=pred,
                         printed_pred=printed, obs_lo=lo, obs_hi=hi, src_obs=src_obs, note=note))

    for k, (p, q, l, wb, ws, nb, ns) in EMDRIVE.items():
        pd, pdd, lo, hi = EMDRIVE_PRINTED[k]
        f = f_epl(p, q, l, wb, ws, nb, ns)
        add(f"EmDrive: {k}", "2017 Eq. 13 (dielectrics)", "M17 Table 1", p, f, lo * MN, hi * MN,
            "as tabulated by McCulloch", printed=pdd * MN,
            note="wrong sign" if f < 0 else "")
    # Shawyer 1 across model versions.
    s1 = PIP["Shawyer 1"]
    add("EmDrive: Shawyer 1", "2015 Prog. Phys. Eq. 10 (1-D)", "M15p Table 1", 850, f_pip(*s1[:5]), 16 * MN, 16 * MN,
        "Shawyer 2008", printed=4.2 * MN)
    add("EmDrive: Shawyer 1", "2015 EPL Eq. 14 (3-D)", "M15e Table 1", 850, f_epl(*EMDRIVE["Shawyer 1"][:5]),
        16 * MN, 16 * MN, "Shawyer 2008", printed=3.8 * MN)
    add("EmDrive: Shawyer 1", "2018 Eq. 7 (uncertainty principle)", "M18 Eq. 7", 850, None, 16 * MN, 16 * MN,
        "Shawyer 2008", printed=4.2 * MN, note="equation printed as an image; value as printed")
    add("EmDrive: Shawyer 1", "2022 Eq. 6 (wall electrons)", "M22 Eq. 6", 850,
        f_casimir(850, 5900, 3e8 / 6.16, 0.01, 0.1, c=3e8), 16 * MN, 16 * MN, "Shawyer 2008", printed=26 * MN)
    # Mach-effect thrusters (McCulloch 2018 Table 1): Q is a range.
    for name, p, qlo, qhi, obs, plo, phi in [("Mahood 1999", 145, 60, 190, 50, 29, 92),
                                             ("Fearn et al. 2013", 63, 60, 190, 1.5, 12.6, 40)]:
        for q, pr in ((qlo, plo), (qhi, phi)):
            add(f"Mach-effect thruster: {name}", f"2018 Eq. 9, Q = {q}", "M18 Table 1", p, f_met(p, q),
                obs * UN, obs * UN, "as tabulated by McCulloch", printed=pr * UN,
                note="Q estimated, not measured")
    add("Asymmetric capacitor in vacuum (NASA 2004)", "2018 Eq. 14", "M18 Eq. 14", None, None, 14 * MN, 14 * MN,
        "Canning et al. 2004 via Martins & Pinheiro", printed=12 * MN,
        note="power not stated (44 kV, current < 5 mA inferred); thrust direction not reported")
    add("Symmetric capacitor (Becker & Bhatt 2018)", "2022 Eq. 10", "M22 Eq. 10, Table", 0.05,
        f_casimir(0.05, 1, 2e7, 0.025 ** 2, 13e-6, c=3e8), 6 * MN, 6 * MN, "6 ± 2 mN as quoted by McCulloch",
        printed=5.7 * MN, note="plate data from a personal communication; text says 10 µm, formula uses 13 µm")
    add("Symmetric capacitor (Becker & Bhatt 2018)", "2021 Eq. 6, n = 1.2, s = 10 µm", "M21 Eq. 6, Fig. 2", 0.05,
        f_capacitor_2021(10e-6, 10e-6, 1.2), 6 * MN, 6 * MN, "≈ 6 mN at the smallest gap (M21 Fig. 2)")
    add("Photo-injector (Moddel et al. 2021)", "2022 Eq. 11", "M22 Eq. 11", 1.4e-12,
        f_casimir(1.4e-12, 1, 990000, 2e-8, 43e-9, c=3e8), 0.1 * NN, 0.1 * NN, "as quoted by McCulloch",
        printed=0.35 * NN, note="Moddel et al. not in this repository; whether they report a force is unverified")
    return rows


# ---------------------------------------------------------------------------
# C. Informal comparisons (blog-only or unpublished) and claims without a QI number
# ---------------------------------------------------------------------------
def informal():
    return [
        dict(group="informal", device="Dresden EmDrive 2018 (SP2018)", src="blog, 24 May 2018", power=None,
             pred=0.19 * MN, obs=0.004 * MN, note="QI value and test power known only from the blog"),
        dict(group="informal", device="Madrid fibre loop (Pérez-Díaz, unpublished)", src="M22 Eq. 8, Table",
             power=0.129, pred=20 * NN, obs=10000 * NN,
             note="observed ± 6000 nN; McCulloch calls it an artefact; text says '250' times, 10000/20 = 500"),
        dict(group="informal", device="Plymouth capacitor tests", src="blog, Nov 2022", power=None,
             pred=None, obs=10e-6 * G0, note="'only 1/3 of the force predicted'; 14% of 22 tests showed thrust"),
        dict(group="informal", device="IVO Quantum Drive (claim)", src="IVO", power=1.0, pred=None,
             obs=45 * MN, note="company claim, no method or error bars; later up to 52 mN/W; no published QI number"),
        dict(group="informal", device="IVO OTP-2 in orbit (2025)", src="blog / NextBigFuture", power=None,
             pred=None, obs=None, note="~600 m less decay in 3 months per McCulloch; 'not conclusive'; no data"),
    ]


# ---------------------------------------------------------------------------
# Arithmetic checks of printed predictions
# ---------------------------------------------------------------------------
def casimir_checks():
    """McCulloch 2022 Eqs. 6-11 recomputed from the inputs printed in the text and in the Table."""
    c3 = 3e8
    out = []

    def add(eq, label, printed, text_in, table_in=None, note=""):
        t = f_casimir(*text_in, c=c3)
        tb = None if table_in is None else f_casimir(*table_in, c=c3)
        out.append(dict(eq=eq, label=label, printed=printed, text_inputs=t, table_inputs=tb,
                        ratio_printed_to_text=printed / t, note=note))

    add("6", "Shawyer EmDrive", 26 * MN, (850, 5900, c3 / 6.16, 0.01, 0.1))
    add("7", "Silver laser cavity", 0.4 * NN, (0.203, 39, c3, 0.001, 0.05), (0.2, 39, c3, 0.001, 0.05))
    add("8", "Madrid fibre loop", 20 * NN, (0.129, 300, 0.7 * c3, 0.01, 0.1), (0.129, 300, c3, 0.1, 0.1),
        "text A/d² = 0.01/0.01 with v = 0.7c; Table A = 0.1 m², d = 0.1 m, v = c")
    add("9", "Dresden fibre loop", 40 * NN, (0.203, 300, 0.7 * c3, 0.01, 0.1), (0.2, 300, 0.7 * c3, 0.1, 0.1),
        "text A/d² = 0.01/0.01; Table A = 0.1 m², d = 0.1 m")
    add("10", "Becker & Bhatt capacitor", 5.6 * MN, (0.05, 1, 2e7, 0.025 ** 2, 13e-6),
        (0.05, 1, 0.07 * c3, 0.000625, 0.000013), "Table lists 5.7 mN; text gap 10 µm, formula 13 µm")
    add("11", "Moddel photo-injector", 0.35 * NN, (1.4e-12, 1, 990000, 2e-8, 43e-9),
        (1.4e-12, 1, 0.004 * c3, 2e-8, 3.3e-8), "text d = 43 nm; Table d = 33 nm, v = 0.004c")
    return out


def printed_checks(ctl, clm):
    worst = {}
    for r in ctl + clm:
        calc = r.get("recomputed", r.get("pred"))
        if r.get("printed_pred") is None or calc is None:
            continue
        dev = abs(calc / r["printed_pred"] - 1)
        key = (r["src"].split()[0], r.get("basis") or r.get("model"))
        if dev >= worst.get(key, (-1.0,))[0]:
            worst[key] = (dev, f"{r['device']}: {r.get('setting') or r.get('model')}", r["printed_pred"], calc)
    pip = {k: dict(printed=v[5] * MN, recomputed=f_pip(*v[:5])) for k, v in PIP.items()}
    epl = {k: dict(printed=EMDRIVE_PRINTED[k][0] * MN, recomputed=f_epl(*EMDRIVE[k][:5])) for k in EMDRIVE}
    return dict(max_rel_dev=[dict(source=k[0], basis=k[1], max_rel_dev=v[0], row=v[1], printed=v[2], recomputed=v[3])
                             for k, v in sorted(worst.items())],
                pip_table1=pip, epl_2015_3d=epl, casimir_2022=casimir_checks())


# ---------------------------------------------------------------------------
# Summaries
# ---------------------------------------------------------------------------
def by_device(rows):
    out = {}
    for r in rows:
        out.setdefault(r["device"], []).append(r)
    return out


def device_summary(ctl):
    res = []
    for dev, rr in by_device(ctl).items():
        ratios = [r["ratio"] for r in rr]
        res.append(dict(device=dev, src=rr[0]["src"], basis=rr[0]["basis"], n=len(rr),
                        p_min=min(r["power"] for r in rr), p_max=max(r["power"] for r in rr),
                        pred_min=min(r["pred"] for r in rr), pred_max=max(r["pred"] for r in rr),
                        upper_min=min(r["upper"] for r in rr), upper_max=max(r["upper"] for r in rr),
                        ratio_min=min(ratios), ratio_max=max(ratios),
                        lower_bound=any(r["pred_lower_bound"] for r in rr)))
    return res


def fmt_f(v):
    if v is None:
        return "—"
    a = abs(v)
    for unit, scale in (("mN", MN), ("µN", UN), ("nN", NN)):
        if a >= scale or unit == "nN":
            x = v / scale
            return f"{x:.3g} {unit}"


def fmt_rng(a, b, f=fmt_f):
    return f(a) if math.isclose(a, b, rel_tol=1e-9) else f"{f(a)} – {f(b)}"


def fmt_ratio(v):
    return f"{v:.2g}" if v < 10 else f"{v:,.0f}"


def summary(res):
    L = ["# A3 results (generated by thrust_ledger.py; do not edit)", "",
         f"Upper limit for a null measurement: U = max(measured, 0) + {K_SIGMA:g}σ, with σ the reported ± "
         "(N22 states it is the standard deviation of repeated runs). Tajmar & Schreiber's capacitor limit "
         "(0.3 mg) is already 3σ and is used as given. Ratio = predicted / U; ratio > 1 means the prediction "
         "exceeds the limit. Predictions are the values printed in the source; section 4 compares them with "
         "our recomputation from the printed inputs. `ledger.csv` also gives predicted / |measured| "
         "('ratio_central'), which is unstable when the measured value is near zero. Photon-rocket limit "
         f"1/c = {PHOTON * 1e9:.3f} nN/W.", "",
         "## 1. Controlled measurements (TU Dresden) against QI-based predictions", "",
         "| Device | Source | Prediction basis | Power | Predicted | U | Predicted / U (all runs) |",
         "|---|---|---|---|---|---|---|"]
    for d in res["device_summary"]:
        lb = " (lower bound)" if d["lower_bound"] else ""
        L.append(f"| {d['device']} | {d['src']} | {d['basis']}{lb} | "
                 f"{fmt_rng(d['p_min'], d['p_max'], lambda v: f'{v:g} W')} | "
                 f"{fmt_rng(d['pred_min'], d['pred_max'])} | {fmt_rng(d['upper_min'], d['upper_max'])} | "
                 f"{fmt_rng(d['ratio_min'], d['ratio_max'], fmt_ratio)} |")
    L += ["", "Per-run rows are in `ledger.csv`.", "",
          "## 2. The author's predictions against claimed positive thrusts", "",
          "Predicted / claimed uses the printed prediction where there is one.", "",
          "| Device | Model | Source | Power | Predicted (recomputed) | Printed | Claimed | Predicted / claimed | Note |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in res["claimed"]:
        p = "—" if r["power"] is None else f"{r['power']:g} W"
        pred = r["printed_pred"] if r["printed_pred"] is not None else r["pred"]
        ratio = fmt_rng(pred / r["obs_hi"], pred / r["obs_lo"], lambda v: f"{v:.2g}")
        L.append(f"| {r['device']} | {r['model']} | {r['src']} | {p} | {fmt_f(r['pred'])} | "
                 f"{fmt_f(r['printed_pred'])} | {fmt_rng(r['obs_lo'], r['obs_hi'])} | {ratio} | {r['note']} |")
    L += ["", "## 3. Informal comparisons and claims without a QI number", "",
          "| Item | Source | Power | QI value | Reported | Note |", "|---|---|---|---|---|---|"]
    for r in res["informal"]:
        p = "—" if r["power"] is None else f"{r['power']:g} W"
        L.append(f"| {r['device']} | {r['src']} | {p} | {fmt_f(r['pred'])} | {fmt_f(r['obs'])} | {r['note']} |")
    L += ["", "## 4. Arithmetic checks", "",
          "Maximum relative deviation between our recomputation and the printed prediction:", "",
          "| Source | Basis / model | max \\|rel. dev.\\| | Row | Printed | Recomputed |", "|---|---|---|---|---|---|"]
    for r in res["checks"]["max_rel_dev"]:
        L.append(f"| {r['source']} | {r['basis']} | {r['max_rel_dev']:.1%} | {r['row']} | {fmt_f(r['printed'])} | "
                 f"{fmt_f(r['recomputed'])} |")
    L += ["", "McCulloch 2022 Eq. 5 recomputed from the printed inputs (c = 3 × 10⁸ m/s as printed):", "",
          "| Eq. | Device | Printed | From text inputs | From Table inputs | Printed / text | Note |",
          "|---|---|---|---|---|---|---|"]
    for r in res["checks"]["casimir_2022"]:
        L.append(f"| {r['eq']} | {r['label']} | {fmt_f(r['printed'])} | {fmt_f(r['text_inputs'])} | "
                 f"{fmt_f(r['table_inputs'])} | {r['ratio_printed_to_text']:.2f} | {r['note']} |")
    L += ["", "2015 Prog. Phys. Table 1 (1-D) and 2015 EPL Table 1 (3-D) recomputed:", "",
          "| Test | 1-D printed | 1-D recomputed | 3-D printed | 3-D recomputed |", "|---|---|---|---|---|"]
    pip, epl = res["checks"]["pip_table1"], res["checks"]["epl_2015_3d"]
    for k in ("Shawyer 1", "Shawyer 2"):
        L.append(f"| {k} | {fmt_f(pip[k]['printed'])} | {fmt_f(pip[k]['recomputed'])} | "
                 f"{fmt_f(epl[k]['printed'])} | {fmt_f(epl[k]['recomputed'])} |")
    for k in ("NASA B1", "NASA B2", "NASA B3"):
        L.append(f"| {k} (1-D geometry) | {fmt_f(pip[k]['printed'])} | {fmt_f(pip[k]['recomputed'])} | — | — |")
    for k in EMDRIVE:
        if k.startswith(("NASA", "Cannae", "Tajmar")):
            L.append(f"| {k} | — | — | {fmt_f(epl[k]['printed'])} | {fmt_f(epl[k]['recomputed'])} |")
    s = res["stats"]
    L += ["", "## 5. Headline numbers", "",
          f"- Controlled devices with a Dresden-adapted prediction: {s['n_devices_dresden']}. In the most "
          f"constraining run of each, predicted / U ranges from {fmt_ratio(s['dresden_best_min'])} "
          f"({s['dresden_best_min_device']}) to {fmt_ratio(s['dresden_best_max'])} ({s['dresden_best_max_device']}).",
          f"- Devices whose most constraining run exceeds U by ≥ 100×: {s['n_dresden_ge_100']} of "
          f"{s['n_devices_dresden']}; by ≥ 10⁴×: {s['n_dresden_ge_1e4']}.",
          f"- McCulloch's 2022 revised silver-cavity prediction / anomalous U: "
          f"{fmt_rng(s['revised_cavity_min'], s['revised_cavity_max'], fmt_ratio)}.",
          f"- McCulloch's 2022 revised fibre-loop prediction (40 nN) / U: vacuum "
          f"{fmt_rng(s['revised_loop_vac_min'], s['revised_loop_vac_max'], fmt_ratio)}; air "
          f"{fmt_rng(s['revised_loop_air_min'], s['revised_loop_air_max'], fmt_ratio)}.",
          f"- QI formulas applied by us to the Tajmar & Schreiber capacitor: predicted / U = "
          f"{fmt_rng(s['capacitor_min'], s['capacitor_max'], fmt_ratio)}.",
          f"- IVO claim (45–52 mN/W) / photon-rocket limit: {s['ivo_over_photon_lo']:.2g} – "
          f"{s['ivo_over_photon_hi']:.2g}."]
    return "\n".join(L) + "\n"


def stats(ctl):
    dres = [d for d in device_summary(ctl) if d["basis"].startswith("Dresden")]
    pick = lambda name: [r["ratio"] for r in ctl if r["device"] == name]
    rc = pick("Silver laser cavities: McCulloch 2022 revised prediction")
    lv = pick("Asymmetric fibre loop, vacuum: McCulloch 2022 revised prediction")
    la = pick("Asymmetric fibre loop, air: McCulloch 2022 revised prediction")
    cp = pick("Leakage-current capacitor (QI formulas applied by us)")
    lo = min(dres, key=lambda d: d["ratio_max"])
    hi = max(dres, key=lambda d: d["ratio_max"])
    return dict(n_devices_dresden=len(dres), dresden_best_min=lo["ratio_max"], dresden_best_min_device=lo["device"],
                dresden_best_max=hi["ratio_max"], dresden_best_max_device=hi["device"],
                n_dresden_ge_100=sum(d["ratio_max"] >= 100 for d in dres),
                n_dresden_ge_1e4=sum(d["ratio_max"] >= 1e4 for d in dres),
                revised_cavity_min=min(rc), revised_cavity_max=max(rc),
                revised_loop_vac_min=min(lv), revised_loop_vac_max=max(lv),
                revised_loop_air_min=min(la), revised_loop_air_max=max(la),
                capacitor_min=min(cp), capacitor_max=max(cp),
                ivo_over_photon_lo=45e-3 / PHOTON, ivo_over_photon_hi=52e-3 / PHOTON)


# ---------------------------------------------------------------------------
# Figure: specific thrust F/P on a log scale
# ---------------------------------------------------------------------------
def chart_rows(res):
    rows = []
    for d in res["device_summary"]:
        if d["device"].startswith("BART"):
            continue
        rr = [r for r in res["controlled"] if r["device"] == d["device"]]
        rows.append(dict(label=d["device"], kind="controlled",
                         pred=[r["pred"] / r["power"] for r in rr], obs=[r["upper"] / r["power"] for r in rr]))
    for dev, rr in by_device(res["claimed"]).items():
        rr = [r for r in rr if r["power"]]
        if not rr:
            continue
        preds = [abs(r["pred"] if r["pred"] is not None else r["printed_pred"]) / r["power"] for r in rr]
        obs = [v / r["power"] for r in rr for v in (r["obs_lo"], r["obs_hi"])]
        rows.append(dict(label=dev, kind="claimed", pred=preds, obs=obs))
    for r in res["informal"]:
        if r["power"] and r["obs"]:
            rows.append(dict(label=r["device"], kind="informal",
                             pred=[r["pred"] / r["power"]] if r["pred"] else [], obs=[r["obs"] / r["power"]]))
    return rows


def figure(res, path):
    sys.path.insert(0, str(A1_DIR))
    import rar_refit as a1
    rows = chart_rows(res)
    pos, y, last = [], 0.0, None
    for r in rows:
        if r["kind"] != last:
            y += 1.2 if last else 0.6
            last = r["kind"]
        pos.append(y)
        y += 1
    h = 110 + 22 * y + 50
    p = a1.Plot(960, h, (-11.2, 3.2), (y - 0.4, 0), "QI thrust predictions vs measurements, per watt of input power",
                "log₁₀ (force / input power)   (N/W)", "", ml=380, mt=96, mb=50)
    p.axes(list(range(-11, 4)), [])
    xp = math.log10(PHOTON)
    p.el.append(f'<line x1="{p.X(xp):.1f}" x2="{p.X(xp):.1f}" y1="{p.t}" y2="{p.b}" stroke="var(--ink2)" '
                f'stroke-dasharray="4 4"><title>Photon rocket, 1/c = 3.34 nN/W</title></line>')
    p.text(p.X(xp), p.t - 6, "photon rocket, 1/c", anchor="middle")
    col = {"pred": "var(--s1)", "upper": "var(--s2)", "claim": "var(--s3)"}
    heads = {"controlled": "Controlled nulls (TU Dresden): prediction vs measured upper limit",
             "claimed": "The author's fits to claimed thrusts", "informal": "Unpublished and company claims"}

    def upper_mark(x, yy, tip=""):
        return (f'<path d="M{x:.1f},{yy - 6:.1f} V{yy + 6:.1f} M{x:.1f},{yy:.1f} l-7,-4 M{x:.1f},{yy:.1f} l-7,4" '
                f'stroke="{col["upper"]}" stroke-width="2" fill="none">{tip}</path>')

    def claim_mark(x, yy, tip=""):
        return f'<path d="M{x:.1f},{yy - 6:.1f} l6,6 l-6,6 l-6,-6 z" fill="{col["claim"]}">{tip}</path>'

    last = None
    for r, yv in zip(rows, pos):
        yy = p.Y(yv)
        if r["kind"] != last:
            p.text(8, yy - 16, heads[r["kind"]], cls="t")
            last = r["kind"]
        p.text(p.l - 8, yy + 4, r["label"].replace("&", "&amp;"), anchor="end")
        for vals, key in ((r["pred"], "pred"), (r["obs"], "upper" if r["kind"] == "controlled" else "claim")):
            vals = [math.log10(v) for v in vals if v > 0]
            if not vals:
                continue
            lo, hi = min(vals), max(vals)
            if hi - lo > 0.02:
                p.el.append(f'<line x1="{p.X(lo):.1f}" x2="{p.X(hi):.1f}" y1="{yy:.1f}" y2="{yy:.1f}" '
                            f'stroke="{col[key]}" stroke-width="3" stroke-opacity="0.55"/>')
            for v in (lo, hi):
                if key == "upper":
                    p.el.append(upper_mark(p.X(v), yy, f"<title>Measured upper limit, max(m, 0) + 2σ: "
                                                       f"{10 ** v:.3g} N/W</title>"))
                elif key == "claim":
                    p.el.append(claim_mark(p.X(v), yy, f"<title>Claimed thrust: {10 ** v:.3g} N/W</title>"))
                else:
                    p.marker(v, yv, col[key], f"Prediction: {10 ** v:.3g} N/W")
    lx, ly = p.l, 52
    p.el.append(f'<circle cx="{lx}" cy="{ly}" r="5" fill="{col["pred"]}"/>')
    p.text(lx + 10, ly + 4, "QI-based prediction (range over runs)")
    lx += 250
    p.el.append(upper_mark(lx, ly))
    p.text(lx + 8, ly + 4, "measured upper limit, 2σ")
    lx += 185
    p.el.append(claim_mark(lx, ly))
    p.text(lx + 10, ly + 4, "claimed thrust")
    p.save(path)


def write_csv(res, path):
    keys = ["group", "device", "setting", "src", "basis", "power", "pred", "pred_lower_bound", "recomputed",
            "obs", "sigma", "upper", "ratio", "ratio_central", "photon", "note"]
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in res["controlled"]:
            w.writerow({k: (f"{r[k]:.6g}" if isinstance(r.get(k), float) else r.get(k)) for k in keys})


def build():
    ctl, clm, inf = controlled(), claimed(), informal()
    res = dict(constants=dict(c=C, g0=G0, k_sigma=K_SIGMA, photon_limit_N_per_W=PHOTON), sources=SRC,
               controlled=ctl, device_summary=device_summary(ctl), claimed=clm, informal=inf,
               checks=printed_checks(ctl, clm), stats=stats(ctl))
    return res


def main():
    OUT.mkdir(exist_ok=True)
    res = build()
    (OUT / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    write_csv(res, OUT / "ledger.csv")
    (OUT / "summary.md").write_text(summary(res))
    figure(res, OUT / "fig-1-specific-thrust.svg")
    print(summary(res))


if __name__ == "__main__":
    main()
