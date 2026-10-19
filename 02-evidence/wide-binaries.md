---
title: "Wide binary stars (and Proxima Centauri)"
tags: [wide-binaries, gaia, mond, low-acceleration, external-field-effect]
verdict: contested
---

# Wide binary stars

## The phenomenon and the data
- For a pair of solar-mass stars, internal accelerations fall below a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻² at separations beyond about 7000 AU. Wide binaries therefore test gravity at low acceleration in systems where dark matter should be negligible.
- **Hipparcos/SDSS (Hernandez, Jiménez & Allen 2012)** ([2012-hernandez-wide-binaries](../01-papers/2012-hernandez-wide-binaries/README.md)):
  - Samples: 280 Hipparcos pairs and 417 SDSS pairs.
  - Result: a flat upper envelope of projected ΔV at 3 ± 1 km s⁻¹ over three decades in separation, and RMS ΔV₁D ≈ 1 ± 0.5 km s⁻¹, about 10× the Newtonian tidal simulation of Jiang & Tremaine 2010.
  - Data quality: the mean S/N is low (0.5 for SDSS).
- **Gaia DR2 (Hernandez et al. 2019)** ([2019-hernandez-gaia-wide-binaries](../01-papers/2019-hernandez-gaia-wide-binaries/README.md)):
  - Sample: 81 cleaned pairs within 100 pc (83 in arXiv v1).
  - Result: consistent with Newton below 7000 AU and with a velocity floor above it. The authors say this favours MOND variants with a suppressed external field effect (EFE).
- **Gaia DR3, results favouring an anomaly:**
  - Chae 2023 ([2023-chae-wide-binaries](../01-papers/2023-chae-wide-binaries/README.md)) used 26,615 binaries within 200 pc, with a clean subset of 4,077. He finds g_obs/g_pred = 1.43 ± 0.06 at g_N ≈ 10^−10.15 m s⁻², 10σ combined, matching AQUAL *with* the Galactic EFE.
  - Hernandez, Chae & Aguayo-Ortiz 2024 ([2024-hernandez-wide-binary-review](../01-papers/2024-hernandez-wide-binary-review/README.md)) report G → (1.5 ± 0.2)G at 2–20 kau.
- **Gaia DR3, results favouring Newton:**
  - Banik et al. 2024 (MNRAS 527, 4573; [2023-banik-gaia-dr3-wide-binaries](../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md)) used 8,611 binaries within 250 pc at 2–30 kau, forward-modelling close companions and line-of-sight contamination. Newton is preferred over MOND at **19σ**, with α_grav = −0.021 (+0.065/−0.045), which excludes MOND at 16σ.
  - Pittordis & Sutherland 2019 and 2023 reached similar conclusions.

## Mainstream explanation(s)
- Newtonian gravity, plus **contamination and systematics**: unresolved triples and hidden close companions, chance alignments, and loose moving groups.
- Pittordis & Sutherland (2019) found that many Gaia DR2 candidates have velocities too high for any plausible gravity law.
- Banik et al. show that simple population statistics produce an apparent MOND-like signal from contamination. A cut on ṽ uncertainty "completely removes" Chae's signal.
- The pro-anomaly groups reply that these Newtonian-favouring analyses ignore observational noise and omit a deep-Newtonian calibration region (0.2–2 kau). They argue that this pushes hidden-tertiary fractions too high: f_multi = 0.65 vs about 0.4 ([2024-hernandez-wide-binary-review](../01-papers/2024-hernandez-wide-binary-review/README.md)).

## QI's prediction
- **McCulloch & Lucio 2019**, Ap&SS 364, 121, funded by DARPA ([2019-mcculloch-wide-binaries](../01-papers/2019-mcculloch-wide-binaries/README.md)):

  $$ \Delta v_{QI} = \sqrt{\frac{GM}{d} + \sqrt{\frac{G^2M^2}{d^2} + \frac{8GMc^2}{\Theta}}}, \qquad \Theta = 8.8\times10^{26}\ \mathrm{m} $$

  - QI has **no external field effect**, so it predicts an asymptotically flat Δv of about 0.5 km s⁻¹ at large separation.
  - The 83 DR2 bins sit at about 0.8 km s⁻¹, inside the uncertainty band. The paper says "QI alone agrees with the data given the error bars". Newton and MOND+EFE under-predict beyond ~0.3 pc.
  - The authors note that all data points lie *above* QI, and that false binaries "are likely still an issue".
- **Proxima Centauri** ([McCulloch 2024, MNRAS Letters 532, L67](../01-papers/2024-mcculloch-proxima-centauri/README.md)):
  - Observed orbital speed: 0.53 ± 0.14 km s⁻¹ (as cited), at 15,000 ± 700 AU.
  - Predictions: Newton 0.344 ± 0.018, MOND 0.424 ± 0.001, QI **0.483 ± 0.01 km s⁻¹** (from v⁴ = 2GMc²/Θ).
  - QI is claimed to bind Proxima without extra mass.
- **JuMBOs:** see [other-anomalies](other-anomalies.md).

## Independent tests, critiques and null results
- **Banik et al. 2024 on QI.** They state that the absence of the expected peak shift in the ṽ distribution in PS19 "falsifies the quantized inertia proposal (McCulloch & Lucio 2019)". They cite McCulloch & Lucio as an example of reaching "erroneous conclusions" from simple population statistics. The paper does not fit a QI model itself.
  - **Archive inference** (not a calculation in Banik et al.): because QI has no EFE, it predicts a *larger* local boost than MOND+EFE. Any Newtonian-favouring result therefore weighs at least as heavily against QI.
- **Even the pro-anomaly analyses do not support QI directly.** Chae 2023 and the 2024 review find agreement with AQUAL *with* EFE and a boost of about 1.4–1.5 in G. Neither paper mentions QI.
- **Data-version issue.** McCulloch & Lucio used Hernandez et al. v1 (83 binaries). The published v3 has 81 binaries.
- **Model simplifications.** The QI comparison assumes equal-mass circular orbits. It does not forward-model projection, eccentricity or contamination.
- **Proxima Centauri:**
  - Kervella, Thévenin & Lovis 2017 (A&A 598, L7) concluded from HARPS radial velocities that Proxima is **bound under Newtonian gravity** "with a high degree of confidence". They found a period of ~550 kyr, e ≈ 0.50 and apastron ~13 kau. That undercuts the premise of the 2024 letter, which assumes a circular orbit.
  - Banik & Kroupa 2019 propose a decisive astrometric test (~10 yr at 0.5 μas precision).
- **McCulloch's response** (blog, 30 Aug 2026) calls the falsification claim "backwards" and says wide binaries are "the best proof" of QI. The reply does not address the contamination or peak-shift arguments ([2023-banik-gaia-dr3-wide-binaries](../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md)).

## Assessment
Whether Gaia wide binaries show any low-acceleration anomaly is still disputed, mainly over contamination modelling, noise and calibration. Strong statistical claims have been made on both sides: 10σ for an anomaly (Chae) and 19σ for Newton (Banik et al.). QI's own support comes from one comparison with 83 DR2 binaries that sat above even the QI curve, with no forward modelling. The largest Newtonian-favouring analysis states explicitly that QI is falsified. The anomaly-favouring analyses match MOND *with* an external field effect, which QI says it does not have, so neither side of the current debate supports QI's specific prediction. The single-system Proxima Centauri test relies on a circular-orbit assumption that conflicts with the measured eccentric, bound Newtonian orbit. The phenomenon is contested, and the QI-specific claim is weak.

## Sources
- [2012-hernandez-wide-binaries](../01-papers/2012-hernandez-wide-binaries/README.md)
- [2019-hernandez-gaia-wide-binaries](../01-papers/2019-hernandez-gaia-wide-binaries/README.md)
- [2019-mcculloch-wide-binaries](../01-papers/2019-mcculloch-wide-binaries/README.md)
- [2023-chae-wide-binaries](../01-papers/2023-chae-wide-binaries/README.md)
- [2024-hernandez-wide-binary-review](../01-papers/2024-hernandez-wide-binary-review/README.md)
- [2024-mcculloch-proxima-centauri](../01-papers/2024-mcculloch-proxima-centauri/README.md)
- [2025-mcculloch-jupiter-mass-binaries](../01-papers/2025-mcculloch-jupiter-mass-binaries/README.md)
- [2023-banik-gaia-dr3-wide-binaries](../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md)
- Related evidence: [galaxy-rotation](galaxy-rotation.md), [globular-clusters](globular-clusters.md), [other-anomalies](other-anomalies.md)
