---
title: "Thrust from Symmetric Capacitors using Quantised Inertia"
authors: [Michael Edward McCulloch]
year: 2021
type: preprint
venue: "ResearchGate preprint (not peer-reviewed)"
doi:
arxiv:
url: "https://www.researchgate.net/publication/353481953_Thrust_from_Symmetric_Capacitors_using_Quantised_Inertia"
open_access: true
license: unknown
files: [paper.pdf, citation.bib, figures/fig-1-schematic.png, figures/fig-2-thrust-vs-separation.png]
status: supports
tags: [propulsion, capacitor-thrust, preprint, field-emission]
---

# Thrust from Symmetric Capacitors using Quantised Inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`unknown`) does not permit redistribution. Read the paper at [source](https://www.researchgate.net/publication/353481953_Thrust_from_Symmetric_Capacitors_using_Quantised_Inertia).

**Citation:** McCulloch, M. E. (2021). *Thrust from Symmetric Capacitors using Quantised Inertia*. ResearchGate preprint 353481953 (not peer-reviewed). https://www.researchgate.net/publication/353481953_Thrust_from_Symmetric_Capacitors_using_Quantised_Inertia

**About the stored PDF:** `paper.pdf` is a 7-page LaTeX preprint dated **July 27, 2021** on its title page (the PDF metadata gives the same creation date). It gives a Plymouth University affiliation and acknowledges DARPA grant HR001118C0125 (p. 5). It is a **non-peer-reviewed preprint**: no journal, DOI or arXiv identifier appears in it. Page numbers below are the PDF's own page numbers (pp. 1–7).
> [!UNVERIFIED] McCulloch's blog says the preprint was submitted to a journal (JPC) and that a "Version 2" exists on ResearchGate. Whether the stored July 2021 copy is that version, or an earlier one, cannot be told from the PDF. No published journal version was found as of 2026-10.

**TL;DR:** McCulloch applies QI to the anode-directed thrust that Becker & Bhatt (2018) reported from symmetric field-emission capacitors. An electron leaving the cathode sees a Rindler horizon behind it. The capacitor plates in front of it damp ("deselect") the Unruh waves between them, so the usual QI gradient is reversed and the electron gets an extra forward push, which it passes to the anode. From the uncertainty principle he derives a force per electron of ħc/(2ns²), multiplies by the number of electrons, and compares the result with Becker & Bhatt's thrust-versus-separation data, which he says it fits within the error bars. He says Becker & Bhatt's own QI derivation was flawed, and calls the device "a potential launch system" at a claimed 120 N/kW.

## Key claims
- Capacitors undergoing highly accelerated discharges or field emission thrust towards their anodes, as reported by Canning et al., Musha (2008) and Becker & Bhatt (2018). The thrust is "many orders of magnitude larger" than ion drift allows, and no plate ablation was seen (p. 1).
- Becker & Bhatt's earlier QI derivation was "finally flawed": it used an uncertainty relation with h instead of ħ/2 (12.5 times too large) and an erroneous assumption, and the two errors cancelled (p. 2).
- **Mechanism (Fig. 1, pp. 2–3):** the electron sees Unruh waves damped between the plates in front of it and undamped behind it, so "in a sense the electrons' inertial mass reverses". The deceleration at the anode is said, if anything, to add further thrust to the right (pp. 3–4).
- QI predicts the thrust and its dependence on plate separation "very well". Some aspects remain unmodelled, such as the drop in thrust when the cathode was thickened (p. 2; p. 4).
- Becker & Bhatt found that a metal plate placed on one side of the calculated Rindler-horizon position reversed the force, and on the other side had no effect. McCulloch says "this test by Becker and Bhatt (2018) may be the first direct observation of a horizon" (p. 5).
- The thruster is "potentially a launch system", and thrust should increase sharply for closer plates (pp. 4–5).

## Key equations
Uncertainty principle used as the starting point (Eqs. 1–2, p. 2):
$$ \Delta p\,\Delta x \ge \frac{\hbar}{2}, \qquad \Delta p \ge \frac{\hbar}{2\Delta x} $$
Momentum available between the plates (separation s) and between the cathode and the Rindler horizon (distance R = c²/a) (Eqs. 3–4, p. 3):
$$ \Delta p = \frac{\hbar}{2s}, \qquad \Delta p = \frac{\hbar}{2R} $$
Extra force on one electron, with n the refractive index of the dielectric (Eq. 5, p. 3):
$$ F = \frac{\hbar c}{2ns}\left(\frac{1}{R} - \frac{1}{s}\right) $$
The 1/R term is dropped because R (about 2 cm) is much larger than s; McCulloch says including it changes the result by at most 1% (p. 3). The force is multiplied by N_e = I/q, which for I = 10 µA is 6.25 × 10¹³ (Eq. 6, p. 3):
$$ F = \frac{N_e\,\hbar c}{2ns^2} $$

**The blog formula F = 0.00014 IA/d² is not in this version.** Eq. 6 contains no plate area A and no numerical coefficient of that kind. The force depends on current, refractive index and separation, and not on voltage or area.
- Editorial check: the formula follows from the later preprint [2022-mcculloch-qi-thrust-casimir](../2022-mcculloch-qi-thrust-casimir/README.md). Its Eq. 5, with P = IV, Q = 1 and v² = q_eV/(2m_e) (as in its Sect. 7), gives F = (π²/240)(2m_ec/q_e) · IA/d². In SI units the coefficient is 1.40 × 10⁻⁴. Voltage cancels out. So the blog's "McCulloch (2021)" formula matches the 2022 model, not Eq. 6 of this July 2021 copy. It may come from a later ResearchGate version of this preprint.
  > [!UNVERIFIED] Whether the "Version 2" on ResearchGate contains F = 0.00014 IA/d² has not been checked.
- Editorial check: N_e = I/q is a rate (electrons per second), not a number, so Eq. 6 as written does not have units of force without an implicit time factor of 1 s.

## Data used
- Becker & Bhatt's (2018) thrust-versus-plate-separation data, which they "kindly provided" (Acknowledgements, p. 5): 5000 V, 10 µA, polyethylene dielectric ([2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md)).
- Refractive index: the text says polyethylene has n = 1.2 (p. 3), but the predictions in Sect. 3 and Fig. 2 use n = 1.49 and n = 1 (p. 4; p. 7). The paper does not explain the difference.
- Prediction error bars of 20%, from an assumed 10% voltage error plus a 10% refractive-index error (Becker and Bhatt, pers. comm.; p. 4).

## Results & predictions
- Predictions with n = 1 (Unruh waves at speed c) and n = 1.49 (waves slowed in the dielectric) "agree within the error bars of the data" (p. 4; Fig. 2, p. 7).
- Largest force: about 6 × 10⁻³ N at the smallest separation (about 10 µm on Fig. 2's axis), for 5000 V and 10 µA, i.e. 0.05 W input. That gives 120 N/kW (p. 4).
  - Editorial check: 6 × 10⁻³ N / 0.05 W = 0.12 N/W = 120 N/kW, as stated.
  - Editorial check: Eq. 6 at s = 10 µm gives about 6.6 mN with n = 1.49 and 9.9 mN with n = 1, so the paper's numbers are in the right range for Fig. 2.
  - For comparison, Becker & Bhatt's own preprint extrapolates performance "above 0.4 [N/kW]" for a 1 kW stacked device ([2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md)). This repository has not reconciled the two figures.
- Launch-system estimate: a Lithium-air battery at 1.8 kW/kg would give "an upwards force of 180N", more than the weight of the battery and thruster (p. 4).
  - Editorial check: 1.8 kW × 120 N/kW = 216 N, not 180 N. The conclusion (thrust far exceeding weight) is unchanged.
- The paper says thrust "increases exponentially as the plate separation is reduced" (p. 4), and that QI "predicts exponentially more thrust for closer plates" (p. 5).
  - Editorial check: Eq. 6 is a 1/s² power law, not an exponential. Becker & Bhatt and Tajmar & Schreiber's fit to their data both describe the measured trend as exponential.
- **Text vs figure:** p. 3 says s "is of the order of a micron - see the x axis of Figure 2", but Fig. 2's x axis runs from about 1 × 10⁻⁵ m to 1.2 × 10⁻⁴ m (10–120 µm). That matches Becker & Bhatt's 13–80 µm dielectrics, not 1 µm.
- **Not modelled:** the gradual loss of thrust as the cathode is thickened, and the reversal when a neutral conductor is placed between the cathode and the Rindler horizon. The model assumes the metal plates block Unruh radiation completely, "a factor which is simply unknown" (p. 4).
- **Later, blog-only reports (not in this preprint):**
  - "On the Cusp?" (2022-11): Plymouth tests found an anode-directed force of "about 10 milligrams", "only 1/3 of the force predicted (McCulloch, 2021)".
  - "How to (Maybe) See QI in Your Lab" (2022-07): "In our 22 tests so far 14% of them have shown a thrust."
  - "A Thrust from 'Nothing'" (2021-11): QI predicts Becker & Bhatt's and Mansell's results "exactly". This preprint does not mention Mansell or IVO Ltd; Mansell appears as a personal communication in the 2022 preprint.
  - A 2026 post describes the 2021 derivation as using "dimensional and physical arguments" and says it predicts measurements from California (Becker & Bhatt), Virginia (IVO Ltd), Italy and Plymouth. This preprint compares only with Becker & Bhatt.
  > [!UNVERIFIED] These Plymouth, IVO and Italian results are known only from McCulloch's blog. They are not in this preprint and were not found as publications.

## Figures
*Figure (local only): Fig. 1 — Schematic of the QI mechanism: (a) an electron accelerating in open space sees more Unruh radiation in front (orange) than behind, where the Rindler horizon damps it, giving inertia; (b) in the capacitor the plates damp the waves in front, so the electron is pushed forwards and pushes the anode; (c) the abrupt deceleration at the anode is said to enhance the rightward thrust. (PDF p. 6.)*

*Figure (local only): Fig. 2 — "Observed thrust & that predicted by QI": Becker & Bhatt's observed force (black diamonds, with error bars) against plate separation (about 10–120 µm), with QI predictions from Eq. 6 for n = 1.49 (squares) and n = 1 (crosses, labelled "dc/dt=0"). (PDF p. 7.)*

## Notable quotes
> "One experiment has claimed that the capacitors' thrust was as large as 120 N/kW, and quantised inertia predicts that this is further enhanceable, making this a potential launch system." (Abstract, p. 1)

> "In a sense the electrons' inertial mass reverses." (p. 2)

> "Therefore this test by Becker and Bhatt (2018) may be the first direct observation of a horizon." (p. 5)

## Criticisms & responses
- **Status:** a single-author, non-peer-reviewed preprint. The only data are Becker & Bhatt's, supplied by the experimenters, who worked with McCulloch ("after some liaison with the author", p. 2), within McCulloch's DARPA-funded programme. It is not independent support.
- **Independent capacitor test:** [Tajmar & Schreiber 2020 (2020-tajmar-capacitor-thrust)](../../03-criticism/2020-tajmar-capacitor-thrust/README.md) built a clean set-up (on-board high-voltage supply in a mu-metal box, liquid-metal feeds, ±0.3 mg accuracy). It included a leakage-current (field-emission) capacitor replicating Becker & Bhatt: 90 µm polyethylene, about 10 µA, discharge at 2.1–4 kV. They measured < 0.3 mg against 6.8 mg from an empirical fit to Becker & Bhatt's data, and say the claim is "ruled out by an order of magnitude". They add that differences from the original set-up (voltage, dielectric thickness, nearby conductors) leave some uncertainty.
  - That paper predates this preprint and tests an empirical fit, not Eq. 6. This preprint does not cite or respond to it.
  - Editorial dimensional check: with s = 90 µm, I = 10 µA and n = 1.49, literal substitution gives about 8 × 10⁻⁵ N/s because N_e = I/q is a rate. Treating that as a force would implicitly insert a one-second counting time, which the model does not justify. The paper also requires electron accelerations high enough for Unruh waves to interact with the plates without quantifying that threshold. The [A3 audit](../../09-analysis/a3-thrust-ledger/README.md) therefore retains this arithmetic without assigning a force/limit ratio.
- **Becker & Bhatt result:** the underlying measurement ([2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), arXiv:[1810.04368](https://arxiv.org/abs/1810.04368)) used a consumer digital scale near high-voltage wiring. It has not been independently replicated in the peer-reviewed literature, according to this repository's notes on that source.
- **Internal inconsistencies (editorial):** n = 1.2 in the text vs 1.49 in the results; "of the order of a micron" vs 10–120 µm on the plotted axis; "exponential" vs a 1/s² formula; 180 N vs 216 N in the launch estimate; N_e defined as a rate. See the sections above.
- **Two different QI capacitor formulas:** the 2022 preprint ([2022-mcculloch-qi-thrust-casimir](../2022-mcculloch-qi-thrust-casimir/README.md)) re-derives the capacitor thrust from a modified Casimir formula. That version depends on plate area A and gives the blog's F = 0.00014 IA/d². This version has no area dependence. For Becker & Bhatt's 2.5 cm × 2.5 cm plates the two happen to give similar values (editorial check: 9.87 × 10⁻⁸ I/(ns²) vs 8.8 × 10⁻⁸ I/d² in SI units, for n = 1 and A = 6.25 × 10⁻⁴ m²). This numerical comparison also inherits the missing time in Eq. 6 and is not a dimensionally valid equivalence of force laws. For other plate sizes even the numerical values would not agree.
- **Laser and cavity tests:** the related QI thrust predictions for photon devices were tested at TU Dresden with null results ([Neunzig et al. 2022, laser resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md)). This preprint is about electron (capacitor) thrust, and the 2022 preprint argues that photon devices should give much less thrust.
- **Spaceflight test:** IVO Ltd's in-orbit "QI thruster" demonstration on Barry-1 (2023–24) ended after the satellite had power-system problems and lost contact. No thrust result was published. See [2024-debrief-ivo-failure](../../07-media/2024-debrief-ivo-failure/README.md).
- General QI critique: [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md), [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md), [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md), [2022-mcculloch-qi-thrust-casimir](../2022-mcculloch-qi-thrust-casimir/README.md), [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2020-mcculloch-nano-materials](../2020-mcculloch-nano-materials/README.md), [2022-satnews-ivo](../../07-media/2022-satnews-ivo/README.md), [2024-debrief-ivo-failure](../../07-media/2024-debrief-ivo-failure/README.md)
