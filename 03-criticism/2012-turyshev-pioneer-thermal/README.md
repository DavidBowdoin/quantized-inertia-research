---
title: "Support for the thermal origin of the Pioneer anomaly"
authors: [Slava G. Turyshev, Viktor T. Toth, Gary Kinsella, Siu-Chun Lee, Shing M. Lok, Jordan Ellis]
year: 2012
type: paper
venue: "Physical Review Letters 108:241101"
doi: 10.1103/PhysRevLett.108.241101
arxiv: 1204.2507
url: "https://arxiv.org/abs/1204.2507"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, figures/fig-2-thermal-power.png, figures/fig-3-thermal-vs-anomalous.png]
status: critical
tags: [pioneer-anomaly, indirect, thermal-recoil, spacecraft-navigation, null-result]
---

# Support for the thermal origin of the Pioneer anomaly

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1204.2507](https://arxiv.org/abs/1204.2507) · [doi:10.1103/PhysRevLett.108.241101](https://doi.org/10.1103/PhysRevLett.108.241101).

**Citation:** Turyshev, S. G., Toth, V. T., Kinsella, G., Lee, S.-C., Lok, S. M. & Ellis, J. (2012). *Support for the thermal origin of the Pioneer anomaly*. Physical Review Letters, 108, 241101. https://doi.org/10.1103/PhysRevLett.108.241101. arXiv:[1204.2507](https://arxiv.org/abs/1204.2507). The stored PDF is arXiv v1 (5 pages).

**TL;DR:** A JPL-led team built a finite-element thermal model of Pioneer 10. It has about 3,300 surface elements, uses flight telemetry as boundary conditions, and models the recoil force from anisotropically emitted heat. They also fitted a two-parameter thermal-recoil model directly to the Doppler data. The thermal model gives about 80% of the Doppler-estimated acceleration, and the 1σ error ellipses of the two estimates overlap. The authors conclude that "no statistically significant acceleration anomaly exists". The paper does not mention MiHsC/QI. It matters for QI because the Pioneer anomaly (a_P = 8.74 ± 1.33 × 10⁻¹⁰ m s⁻²) was the first phenomenon McCulloch's 2007 MiHsC paper set out to explain.

## Key claims
- The anomaly, a constant sunward acceleration a_P = (8.74 ± 1.33) × 10⁻¹⁰ m s⁻², is confirmed in the extended Doppler data set. The residuals improve with a *temporally decreasing* acceleration directed towards Earth. That is the signature expected from thermal recoil along the spin axis, decaying with the ²³⁸Pu fuel.
- Finite-element model: about 3,300 surface elements, 3,700 nodes and 8,700 linear conductors in SINDA/3D. Radiative exchange factors come from a Monte Carlo analyser (TSS). Louvers and solar heating are included. The model reproduces RTG thermal power to within 1%, RTG fin-root temperatures to within ±2 K, and platform temperatures with an RMS error of 5.1%.
- The thermal recoil force is well fitted by a two-term model with η_rtg = 0.0104 and η_elec = 0.406 (RMS 0.78 W). An independent Doppler fit gives the lowest residuals at η_rtg = 0.0144 and η_elec = 0.480.
- Error budget: total 26.3% of a_P. The largest single term (25%) is unknown degradation of the RTG zirconia coating in sunlight.
- Conclusion: "once the thermal recoil force is properly accounted for, no anomalous acceleration remains."
- Caveat stated by the authors: Pioneer 11 was not analysed at the same level of detail, although "spot analysis revealed no surprises".

## Key equations
RTG thermal power decay (τ = 87.74 yr, t₀ = 1 July 1972, Q_rtg(t₀) = 2578.179 W):
$$ Q_{\rm rtg}(t) = 2^{-(t-t_0)/\tau}\,Q_{\rm rtg}(t_0) $$
Thermal recoil acceleration and the two-component model (Eq. 1):
$$ a_{\rm th} = \eta\,\frac{Q}{mc}, \qquad a_P = \eta_{\rm rtg}\frac{Q_{\rm rtg}}{mc} + \eta_{\rm elec}\frac{Q_{\rm elec}}{mc} $$
Exponential decay fits:
$$ a = 2^{-(t-t_0)/\tau}\,a_0 $$

## Data used
- The recovered Pioneer 10 flight telemetry (temperatures and electrical power at 11 heliocentric distances, 3–80 AU), project and design documentation, and the extended Pioneer 10 Doppler data set (analysis of Turyshev et al. 2011, ref. [8]).

## Results & predictions
- The thermal estimate is about 80% of the Doppler-estimated magnitude: about 35% from the RTGs and about 45% from electrical heat. The remaining roughly 20% is within the combined 1σ uncertainties (Fig. 4).
- Decay fits with t₀ = 1 Jan 1980:
  - Doppler data: τ = 28.8 ± 2.0 yr, a₀ = (10.1 ± 1.0) × 10⁻¹⁰ m s⁻².
  - Thermal model: τ = 36.9 ± 6.7 yr, a₀ = (7.4 ± 2.5) × 10⁻¹⁰ m s⁻², with an RMS error of 0.1 × 10⁻¹⁰ m s⁻².
- A ~20% change in the overall recoil magnitude nearly doubles the Doppler residual. The Doppler data constrain the total but cannot separate the RTG and electrical contributions.

## Figures
*Figure (local only): Fig. 2 — Pioneer 10 thermal power contributing to sunward acceleration versus time/heliocentric distance: including solar heating and reflected sunlight (hollow circles), solar heating only (hollow squares) and all solar effects removed (filled circles); Fig. 1 (thermal model rendering) and Table I (telemetered power) are on the same page. (Rendered page 2 of the arXiv PDF.)*

*Figure (local only): Fig. 3 & 4 — Fig. 3: thermally induced acceleration (with inner/outer error bars for the subtotal and total budget) compared with the stochastic Doppler-derived anomalous acceleration (step function), with Doppler residuals below. Fig. 4: 1σ error ellipses in the (η_rtg, η_elec) plane for the thermal and Doppler estimates, which overlap. (Rendered page 4 of the arXiv PDF.)*

## Notable quotes
> "We find no statistically significant difference between the two estimates and conclude that once the thermal recoil force is properly accounted for, no anomalous acceleration remains." (p. 1, abstract)

> "at the present level of our knowledge of the Pioneer 10 spacecraft and its trajectory, no statistically significant acceleration anomaly exists." (p. 4)

## Criticisms & responses
- **McCulloch's response (blog, 1 May 2012, "Criticism of the thermal model of the Pioneer anomaly").** He commends the data rescue and then lists six objections ([blog](https://physicsfromtheedge.blogspot.com/2012/05/comment-on-thermal-model-of-pioneer.html)):
  1. Anderson et al. (1998) found a similar anomaly in Ulysses data (and, less conclusively, Galileo data), and different spacecraft are unlikely to share a thermal cause.
  2. Turyshev et al. (2011) themselves said the data are too noisy to prove a decay with time.
  3. The best-fit decay half-lives (28.8 or 36.9 yr) differ from the 87-yr half-life of the plutonium.
  4. The predicted thermal anomaly is largest in the inner Solar System, where none was seen. The proposed cancelling solar push does not exactly cancel in their Fig. 2.
  5. Anderson et al. (2002) estimated that only about 4 W from the RTG fin edges could hit the antenna, giving at most 0.55 × 10⁻¹⁰ m s⁻².
  6. Because radiated power goes as T⁴, he wanted to see the temperature errors.

  He adds a general objection to "a very complex and unrevealed process (over 3000 finite elements, not fully detailed in the paper) and with fitting parameters" used to reach a known answer.
- **Earlier and later blog statements.** On 3 Apr 2012, after a questioner at the UK National Astronomy Meeting said he should stop citing Pioneer as a success, McCulloch wrote that he had not yet read the paper in detail but was concerned about adjustable parameters and the lack of a decay in Anderson et al.'s analysis ([blog](https://physicsfromtheedge.blogspot.com/2012/04/national-astronomy-meeting-talk.html)). On 16 Jan 2016 he again cited the Ulysses result of 12 ± 3 × 10⁻¹⁰ m s⁻² sunward. He described the thermal model as having "1000s of finite elements and two adjustable parameters" ([blog](https://physicsfromtheedge.blogspot.com/2016/01/ulysses-also-showed-pioneer-anomaly.html)).
- **Context (factual):** Two independent thermal analyses reached similar conclusions: Rievers & Lämmerzahl (2011, Ann. Phys. 523, 439, https://doi.org/10.1002/andp.201100081) and Francisco, Bertolami, Gil & Páramos (2012, Phys. Lett. B 711, 337, https://doi.org/10.1016/j.physletb.2012.04.034). Turyshev's paper notes that the η values depend only on the spacecraft geometry and stay constant over time, which answers the "adjustable parameter" objection only in part. *Editorial note:* the half-life point in McCulloch's objection 3 compares decay of the *acceleration*, which mixes RTG and electrical heat whose electrical part falls faster, with the decay of the fuel. Table I of the paper shows electrical power falling faster than RTG output.

## Related
- Evidence: [pioneer-anomaly](../../02-evidence/pioneer-anomaly.md), [other-anomalies](../../02-evidence/other-anomalies.md)
- Sources: [2007-mcculloch-pioneer-anomaly](../../01-papers/2007-mcculloch-pioneer-anomaly/README.md) (the MiHsC Pioneer prediction this removes the target for), [2010-turyshev-pioneer-review](../../01-papers/2010-turyshev-pioneer-review/README.md), [2011-gine-pioneer-holographic](../../01-papers/2011-gine-pioneer-holographic/README.md), [2015-iorio-solar-system-anomalies](../../01-papers/2015-iorio-solar-system-anomalies/README.md), [2008-mcculloch-flyby-anomalies-mnras](../../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md)
