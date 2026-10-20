---
title: "Put strong limits on all proposed theories so far assessing electrostatic propulsion: Does a charged high-voltage capacitor produce thrust?"
authors: [Martin Tajmar, Tom Schreiber]
year: 2020
type: experiment-report
venue: "Journal of Electrostatics 107:103477"
doi: 10.1016/j.elstat.2020.103477
arxiv:
url: "https://doi.org/10.1016/j.elstat.2020.103477"
open_access: false
license: all-rights-reserved
files: [paper.pdf, figures/fig-1-setup.png, figures/fig-2-calibration-null.png, figures/fig-3-leakage-capacitor.png]
status: critical
tags: [capacitor, electrostatic, tu-dresden, indirect, null-result, biefeld-brown, lab-test]
---

# Put strong limits on all proposed theories so far assessing electrostatic propulsion: Does a charged high-voltage capacitor produce thrust?

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.1016/j.elstat.2020.103477](https://doi.org/10.1016/j.elstat.2020.103477).

**Citation:** Tajmar, M. & Schreiber, T. (2020). *Put strong limits on all proposed theories so far assessing electrostatic propulsion: Does a charged high-voltage capacitor produce thrust?* Journal of Electrostatics, 107, 103477 (8 pp.). https://doi.org/10.1016/j.elstat.2020.103477. Received 21 Feb 2020, accepted 11 May 2020.

**Stored version:** the typeset Elsevier journal version (8 pp., "© 2020 Elsevier B.V. All rights reserved"), supplied by the archive owner and kept local only. Page numbers below are journal pages 1–8 (= PDF pages 1–8). An earlier version of this entry was written from the authors' 23-page manuscript on the TU Dresden site; the numbers below have been re-checked against the published text.

**TL;DR:** TU Dresden built a capacitor weight-change rig designed to remove high-voltage artefacts: a Sartorius balance (0.1 mg digital resolution) with a hanging mu-metal/Faraday box holding an on-board 10 kV supply and a rotation rig, powered only by low-voltage Galinstan liquid-metal contacts. Accuracy is ±0.3 mg (3σ). Five capacitor types were tested against four models: Ivanov, Porcelli & dos Santos Filho, Minotti, and the field-emission ("leakage current") claim of **Bhatt & Becker** that QI was invoked for. No weight change above 0.3 mg was seen in any configuration. The Bhatt & Becker prediction used (6.8 mg in the text, "≈ 7 mg" in Table 1) is **not a QI prediction**: it is the authors' own empirical fit to Bhatt & Becker's measured force-versus-power data. The authors say the null result "may not completely rule out the claim" because their replica differs from the original.

## Key claims
- **Context (p. 1):** the Biefeld-Brown effect in air is corona/ion wind (Tajmar 2004). Later claims of a residual, purely electrostatic force linked to the dielectric "lack a proper setup to definitely rule out conventional explanations".
- **Models tested (Sect. 2, pp. 2–3):**
  - Ivanov (and the related Musha and Zhu models), Eq. 1: forces "up to 10 μN (or an equivalent of 1 mg ...)" for standard high-voltage capacitors.
  - Porcelli & dos Santos Filho, Eqs. 2–3: "up to several 1000s of μN (or equivalent several 100s of mg)".
  - Minotti's version of the Mbelek–Lachièze-Rey scalar-tensor theory, Eqs. 4–5. The authors say Minotti omitted the relative permittivity (Eq. 4 should be multiplied by ε_r⁻²), and treat Minotti's revised coupling constant as giving a lower bound.
  - Bhatt & Becker's "discharge through a thin dielectric sheet": "The authors say that their effect can by predicted by a modified inertia model based on Unruh radiation forming a so-called Rindler horizon", citing McCulloch 2010 (EPL 90, 29001). "However, no actual force model is shown", so the authors digitised Bhatt & Becker's force-versus-power plot and fitted Eq. 6 (R² = 0.9996) (p. 2–3).
- **Artefacts (Sect. 3, pp. 3–4):** corona wind from thin or poorly insulated cables and sharp solder joints; high-voltage bending of wires and the resulting centre-of-mass shifts; buoyancy from supply heating ("A change of 1 °C in that volume [10 × 10 × 10 cm³] causes a buoyancy force equivalent to 4 mg"); and electromagnetic interaction with the surroundings. A null measurement is essential.
- **Overall answer (Conclusion, p. 8):** "No – within our measurement accuracy." Ivanov's model and the Bhatt claim are "worth to be pursued with better setups in the future".

## Key equations
Ivanov, parallel-plate capacitor (Eq. 1; m = dielectric mass, d = thickness, V = voltage):
$$ F_{\rm Ivanov} = \sqrt{G\varepsilon_0\varepsilon_r}\cdot\frac{m}{d}\cdot V $$
Porcelli & dos Santos Filho, symmetric (Eq. 2) and asymmetric (Eq. 3, A₁ the larger and A₂ the smaller electrode area):
$$ F_{\rm Porcelli} = \frac{0.102}{16\pi^2}\,\frac{\varepsilon_r - 1}{\varepsilon_r + 2}\,\varepsilon_0 A E^2, \qquad F_{\rm Porcelli} = \frac{0.102}{16\pi^2}\,\frac{\varepsilon_r - 1}{\varepsilon_r + 2}\,\frac{A_1^2}{A_2}\,\varepsilon_0 E^2 $$
Minotti, parallel-plate form with the ε_r correction (Eq. 5; ρ = dielectric density, Γ = 3.35 × 10⁻¹² in the paper's units):
$$ F_{\rm Minotti} = \frac{\Gamma A \rho V^2}{2\varepsilon_r^2} $$
Empirical fit to Bhatt & Becker's data (Eq. 6; P = discharge power in mW, d = dielectric thickness in µm, F in µN):
$$ F_{\rm Bhatt} = P\cdot\left(2.7 + 114.8\,e^{-d/16.9} + 2679\,e^{-d/3.6}\right) $$

## Data used
- **Balance:** Sartorius MSE1203S-100-DE, 1200 g capacity, custom resolution 0.1 mg. The experiment hangs from a single hook below the balance (to limit centre-of-mass effects) inside a Faraday cage on an isolated granite table (p. 4).
- **Experiment box:** 150 × 150 mm base, 100 mm high; 0.5 mm mu-metal base plate and 100 µm mu-metal foil sides. Inside: an EMCO CB101 supply (10 kV, 100 µA) in thermal-insulation foam with an LM35 temperature sensor, and a 3D-printed rotation rig with stepper motor and absolute encoder. All connections pass through a 16-pin Galinstan liquid-metal feedthrough carrying low-voltage signals only (p. 4).
- **Calibration:** voice coil (0.758 µN/µA), linear from 0.1 to 10 mg (tested to 100 mg). The balance registered 92% of the commanded force, which the authors put down to coil alignment (p. 4).
- **Null test:** an EMCO V1G high-voltage resistor instead of a capacitor, 2–10 kV, 20 averaged profiles of 60 s on / 60 s off at 1 Hz. Most profiles stayed within ±0.1 mg. The 10 kV profile peaked at 0.3 mg at the end of the profile. Hence "Our accuracy is therefore ± 0.3 mg" (3σ) (p. 4).
- Profiles were averaged (10–20 per configuration; 5 for the leakage capacitor) with linear drift removal from the off-periods.

## Results & predictions
Table 1 (p. 6), Δm = F/g₀. "Experiment (3σ)" is Δm < 0.3 mg for every row.

| Test item (all at 10 kV unless stated) | Model predictions (Table 1) | Measured |
|---|---|---|
| Symmetric ceramic: 2 × Murata DHRB34A102MF1B, 2 × 1000 pF, m = 2 × 5.8 g, ε_r = 4500, r = 7.5 mm, d = 7 mm; 0°, 90°, 180°, 270° | Ivanov 2.4 mg; Porcelli 0.4 mg; Minotti 8.6 × 10⁻⁶ mg | < 0.3 mg |
| Symmetric Teflon: m = 4.1 g, ε_r = 2.1, r = 20 mm, d = 1.5 mm | Ivanov 0.1 mg; **Porcelli 118.8 mg; Minotti 11.8 mg** | < 0.3 mg |
| Asymmetric Teflon: r₁ = 20 mm, r₂ = 0.04 mm (wire electrode), d = 1.5 mm; 0°, 90° | **Porcelli 29.7 kg** | < 0.3 mg |
| Spherical, half-filled with bee wax: ε_r = 1.8, ρ = 0.9 g/cm³, a = 15 mm, b = 28 mm; total 315 g | **Minotti 24.4 mg** (7.5 mg with ε_r⁻² correction) | < 0.3 mg |
| Leakage-current capacitor: 90 µm Al-foil anode and needle-perforated Al-foil cathode (r = 20 mm), 90 µm PE dielectric; discharge 2100 V, about 10 µA, P = 21 mW; anode up, down and sideways | **Bhatt ≈ 7 mg (extrapolation)**; text: 6.8 mg | < 0.3 mg |

- The 3σ limit is 0.3 mg ≈ 2.9 µN of force (editorial check: 0.3 × 10⁻⁶ kg × 9.81 m/s²).
- Margins stated: Porcelli ruled out by "nearly three orders of magnitude", Minotti by two, Ivanov's ceramic case by one ("quite close to our resolution"), Bhatt & Becker by one order of magnitude (pp. 5–8).
- **Leakage test details (Sect. 4.5, p. 7):** the first discharge needed up to 4 kV, later ones 2.1 kV, "indicating that the first discharge probably increased the leakage of the dielectric through conduction paths". To avoid further damage the on/off period was cut to 30 s and only 5 profiles were averaged. A 100 MΩ series resistor limited the current to Bhatt & Becker's maximum of about 10 µA.
- **Stated differences from Bhatt & Becker (pp. 7–8):** discharge at 2.1 kV instead of 5 kV; the 90 µm dielectric is thicker than Bhatt & Becker's thickest (80 µm; range 13–80 µm); and the distance to conductive surroundings may differ, which matters because Bhatt & Becker reported "force blocking" by nearby conductors.
- **What the "prediction" is:** Eq. 6 fits Bhatt & Becker's own data. It is not McCulloch's QI capacitor formula, which was published later (see Criticisms). Editorial check: Eq. 6 at P = 21 mW and d = 90 µm gives 21 × (2.7 + 114.8 e^(−5.33) + ≈ 0) ≈ 21 × 3.26 ≈ 68 µN ≈ 7.0 mg. That matches Table 1's "≈ 7 mg"; the text's 6.8 mg is slightly lower, perhaps from rounding or slightly different inputs, which the paper does not show.

## Figures
*Figure (local only): Fig. 2 — Balance set-up: Faraday cage on granite table, Sartorius balance with hanging mu-metal experiment box, on-board high-voltage supply in insulation foam, rotation rig, and the Galinstan liquid-metal feedthrough. (PDF p. 3.)*

*Figure (local only): Figs. 3–4 — Voice-coil calibration (linearity 0.1–10 mg; 10 µN step) and the high-voltage-resistor null test at 2–10 kV defining the ±0.3 mg accuracy. Also shows Sect. 4.2 text on the Teflon capacitor. (PDF p. 5.)*

*Figure (local only): Fig. 12 — Weight change of the leakage-current capacitor at 2100 V for three anode orientations, with the emitted current; no signal above 0.3 mg. The page also carries the Conclusion. (PDF p. 8.)*

## Notable quotes
> "No force was detected for a variety of configurations ruling out most theories by many orders of magnitude." (abstract, p. 1)

> "Still, our null result is important for comparison with a clean setup although it may not completely rule out the claim due to the exact replica uncertainties." (Sect. 4.5, p. 8)

> "Can we answer the question if a charged high-voltage capacitor produces thrust? So far, our answer must be: No – within our measurement accuracy." (Conclusion, p. 8)

## Criticisms & responses
- **The Bhatt & Becker comparison is with an empirical fit, not a QI prediction.** The paper says outright that Bhatt & Becker give no force model (p. 2). McCulloch's QI capacitor formulas came later: the 2021 preprint ([2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md), which depends on current and plate separation) and the area-dependent F = 0.00014 IA/d² from the 2022 preprint and blog ([2022-mcculloch-qi-thrust-casimir](../../01-papers/2022-mcculloch-qi-thrust-casimir/README.md)). No published QI-formula value for this rig was found.
  - Editorial check, on stated assumptions (SI units; d = the 90 µm dielectric thickness; I = 10 µA; A = π × (20 mm)²): F = 0.00014 × 10⁻⁵ × 1.26 × 10⁻³ / (9 × 10⁻⁵)² ≈ 2.2 × 10⁻⁴ N ≈ 22 mg, about 70 times the 0.3 mg limit. This is our arithmetic, not a number in either paper.
  > [!UNVERIFIED] Whether McCulloch would accept those inputs (in particular the units of the 0.00014 coefficient and which length d stands for) for the Dresden capacitor.
- **Replication caveats raised by the authors themselves:** lower discharge voltage, thicker dielectric, possible degradation after the first 4 kV discharge, a shortened 30 s / 5-profile protocol, and unknown sensitivity to nearby conductors (pp. 7–8). A Bhatt & Becker supporter could argue the field-emission regime was not reproduced. This argument was not found in print.
- **McCulloch's position (blog):** no post directly addressing this paper was found (searches for "Schreiber" and "Tajmar" in Oct 2026). McCulloch continued to cite the Becker & Bhatt capacitor results as QI's strongest laboratory support:
  - 23 Jan 2022: "QI predicts the capacitor results perfectly (top right): results now seen in two labs" ([blog](https://physicsfromtheedge.blogspot.com/2022/01/learning-from-experiments.html)).
  - 2 Nov 2021: Richard Mansell of IVO Ltd "tried it with an analogue method and agreed with them" ([blog](https://physicsfromtheedge.blogspot.com/2021/11/a-thrust-from-nothing.html)).
  - 4 Aug 2022: describes his own capacitor tests with R. Arundal ([blog](https://physicsfromtheedge.blogspot.com/2022/08/glimpses-of-qi-in-lab.html)).

  These are McCulloch's claims. The IVO and Plymouth measurements were not located as peer-reviewed publications for this entry.
- **Subsequent space test:** IVO Ltd's QI-capacitor thruster flight in 2023–24. See [2023-debrief-ivo-launch](../../07-media/2023-debrief-ivo-launch/README.md), [2024-debrief-ivo-failure](../../07-media/2024-debrief-ivo-failure/README.md) and [2024-futurism-ivo-contact-lost](../../07-media/2024-futurism-ivo-contact-lost/README.md).

## Related
- Evidence: [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md), [2010-mcculloch-minimum-accelerations](../../01-papers/2010-mcculloch-minimum-accelerations/README.md), [2018-mcculloch-propellantless-propulsion](../../01-papers/2018-mcculloch-propellantless-propulsion/README.md), [2018-tajmar-spacedrive](../../04-experiments/2018-tajmar-spacedrive/README.md) (cited as ref. [20]), [2022-neunzig-laser-resonators](../2022-neunzig-laser-resonators/README.md)
