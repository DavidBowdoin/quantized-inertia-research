---
title: "QI Thrust as an Asymmetric Casimir Effect"
authors: [Michael Edward McCulloch]
year: 2022
type: preprint
venue: "ResearchGate preprint (not peer-reviewed)"
doi:
arxiv:
url: "https://www.researchgate.net/publication/358089705"
open_access: true
license: unknown
files: [paper.pdf, citation.bib]
status: supports
tags: [propulsion, preprint, derivation, casimir, capacitor-thrust, emdrive, laser]
---

# QI Thrust as an Asymmetric Casimir Effect

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`unknown`) does not permit redistribution. Read the paper at [source](https://www.researchgate.net/publication/358089705).

**Citation:** McCulloch, M. E. (2022). *QI Thrust as an Asymmetric Casimir Effect*. ResearchGate preprint 358089705 (not peer-reviewed). https://www.researchgate.net/publication/358089705

**About the stored PDF:** `paper.pdf` is a 7-page LaTeX preprint dated **January 25, 2022** on its title page (the PDF metadata gives the same date), with a University of Plymouth affiliation. It is a **non-peer-reviewed preprint**: no journal, DOI or arXiv identifier appears in it, and no published version was found. It has no figures, only two tables (pp. 5–6). Page numbers below are the PDF's own (pp. 1–7). The title, author and year in the earlier Google Scholar listing are confirmed.

**TL;DR:** McCulloch re-derives QI thrust by starting from the ordinary Casimir force between plates and replacing ħ with the electrical energy-time put into the device (ħ → PQτ², with τ = d/v the time the energy carriers spend crossing the cavity). The resulting formula is F = π²PQcA/(240v²d²). Because v is the speed of the accelerated carriers, the formula predicts far more thrust when electrons (slow) rather than photons (speed c) are the "accelerand". He applies it to six experiments and says it is consistent with five: Shawyer's EmDrive, the Dresden laser cavity and fibre loop, the Becker & Bhatt capacitor and Moddel's photoinjector. The positive Madrid fibre-loop result, which it under-predicts by orders of magnitude, "was an artefact". He concludes that devices accelerating electrons by tunnelling "are the way to go".

## Key claims
- QI is "an asymmetric Casimir effect" in which the cosmic (Hubble) horizon plays the role of a Casimir plate. It predicts galaxy rotation and wide binaries without dark matter (Abstract and Sect. 1, p. 1; citing McCulloch 2017 and McCulloch & Lucio 2019, the latter co-authored).
- **Revised mechanism:** the earlier idea that photon acceleration generates the relevant Unruh waves "was false". Instead, the photons excite electrons in the metal, and those electrons generate the Unruh waves (Abstract, p. 1).
- Thrusters based on trapped photons have given zero or ambiguous thrust, while those that accelerate electrons in metal cavities have given positive thrust (Abstract, p. 1).
- Becker & Bhatt's own QI derivation was flawed (h used instead of ħ/2, 12.5 times too large, plus a compensating error). This repeats the argument of the 2021 capacitor preprint (p. 2).
- The Madrid (Pérez-Díaz et al.) positive fibre-loop result is 250 times larger than predicted, which "suggests that the Spanish positive result was an artefact" (p. 4).
- Electron-based systems are "orders of magnitude more effective, as is also predicted (admittedly now with hindsight) by the QI theory - albeit without the need to change the theory, just to reconsider what the accelerand is" (p. 6).

## Key equations
Standard Casimir force between parallel plates of area A and separation d (Eq. 1, p. 2):
$$ F = \frac{\hbar c \pi^2 A}{240 d^4} $$
Replacing ħ with the energy-time input, where P is input power, Q the quality factor (Q = 1 for a single pass) and τ the time applied (Eqs. 2–3, pp. 2–3):
$$ \hbar \to E\tau, \qquad \hbar = PQ\tau^2 $$
With τ = d/v (Eq. 4, p. 3):
$$ \hbar = \frac{PQd^2}{v^2} $$
Resulting thrust (Eq. 5, p. 3), where the factor c²/v² separates light-based (v = c) from matter-based systems:
$$ F = \frac{\pi^2 P Q c^2 A}{240\,c\,v^2 d^2} $$
For the capacitor (Sect. 7, p. 5), the electron speed comes from v² = ¼(2q_eV/m_e) ≈ (2 × 10⁷ m/s)². The paper writes this as "v² … ∼ 20000000m/s", but the number is v, not v².
- Editorial check: with P = IV and Q = 1, the voltage cancels and Eq. 5 becomes F = (π²/240)(2m_ec/q_e) · IA/d² ≈ 1.40 × 10⁻⁴ · IA/d² (SI units). This is the F = 0.00014 IA/d² that McCulloch's blog attributes to "McCulloch (2021)". The paper does not write it in this form. It is not in the July 2021 copy of [2021-mcculloch-symmetric-capacitors](../2021-mcculloch-symmetric-capacitors/README.md), whose formula has no area term.

## Data used
Inputs are taken from published or reported experiments (Sects. 3–8, pp. 3–5; Table 1, p. 6):

| Test | Accelerand | P (W) | Q | v | A (m²) | d (m) |
|---|---|---|---|---|---|---|
| Shawyer EmDrive | e⁻ | 850 (table: 1000) | 5900 | c/6.16 (table: 0.16c) | 0.01 | text uses A/d² = 1 |
| Laser in metal cavity (Neunzig et al.) | photons | 0.203 | 39 | c | 0.001 | 0.05 |
| Madrid fibre loop (Pérez-Díaz et al.) | photons | 0.129 | 300 | 0.7c (table: c) | 0.01 (table: 0.1) | 0.1 (A/d² = 1) |
| Dresden fibre loop (Neunzig et al.) | photons | 0.203 | 300 | 0.7c | 0.01 (table: 0.1) | 0.1 (A/d² = 1) |
| Becker & Bhatt capacitor | e⁻ | 0.05 (10 µA, 5000 V) | 1 | ≈ 2 × 10⁷ m/s (0.07c) | 0.025 × 0.025 | 13 × 10⁻⁶ (text says "10 micron") |
| Moddel photoinjector | e⁻ | 1.4 × 10⁻¹² | 1 | 990,000 m/s | 2 × 10⁻⁸ | 43 × 10⁻⁹ (table: 3.3 × 10⁻⁸) |

- The Shawyer EmDrive dielectric (n = 6.16) is used to slow the carriers. The plate separation and Mansell data come from personal communications, and the Madrid test from a paper "submitted" at the time (references, p. 7).
- Where text and table differ, as marked above, the paper gives no explanation.

## Results & predictions
The paper's comparison table (p. 6):

| Test | QI prediction | Observed | "Consistent?" | Thrust/power (N/kW, as printed) |
|---|---|---|---|---|
| EmDrive (Shawyer) | 26 mN | 16 mN | Yes | 0.019 |
| Laser cavity (Dresden) | 0.4 ± 0.1 nN | < 2 nN | Yes | 0.00001 |
| Laser loop 1 (Madrid) | 20 ± 5 nN | 10000 ± 6000 nN | No | 0.077 |
| Laser loop 2 (Dresden) | 40 ± 10 nN | 50 ± 200 nN | Yes | 0.00025 |
| Capacitor (Becker & Bhatt) | 5.7 ± 5 mN | 6 ± 2 mN | Yes | 120 |
| Photoinjector (Moddel) | 0.35 nN | 0.1 nN | Yes | 71 |

- Capacitor: "The observed thrust was 6mN and indeed varies with the separation of the plates and area in exactly the manner predicted by QI" (p. 5).
- Photoinjector: the observed force is "one third of that predicted" (p. 5).
- **Editorial arithmetic checks** (recomputing Eq. 5 with the paper's own inputs):
  - EmDrive 26 mN, laser cavity 0.43 nN and capacitor 5.7 mN reproduce.
  - The fibre loops give about 11 nN (Madrid) and 17 nN (Dresden) with the stated inputs, not 20 and 40 nN. The Madrid ratio is 10000/20 = 500, not the "250" in the text.
  - The photoinjector gives about 0.19 nN with d = 43 nm (text) and 0.32 nN with d = 33 nm (table).
  - The photoinjector's thrust/power is 0.1 nN / 1.4 × 10⁻¹² W ≈ 71 N/W, i.e. about 71,000 N/kW. The "71" in the N/kW column is in N/W.
  - None of these changes which tests the paper calls consistent, since the error bars are wide and the Madrid discrepancy remains orders of magnitude.
- Earlier QI EmDrive formulas gave a different Shawyer prediction: this repository's [propulsion](../../02-evidence/propulsion.md) note lists 4.2 mN against 16 mN observed, from McCulloch's earlier photon-based formula ([2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md); see also [2015-mcculloch-emdrive-pip](../2015-mcculloch-emdrive-pip/README.md)). Here the prediction is 26 mN, from the new electron-based assumption.

## Figures
None. The PDF contains no figures, only Tables 1 and 2 (pp. 5–6), transcribed above.

## Notable quotes
> "It is argued that the previous conception that it was the photon acceleration that generated the Unruh waves was false, and that instead the photons excite electrons in metal, which then generate Unruh waves." (Abstract, p. 1)

> "This suggests that the Spanish positive result was an artefact." (p. 4)

> "The overall conclusion is that systems that accelerate electrons via tunneling are the way to go." (p. 6)

## Criticisms & responses
- **Status:** a single-author, non-peer-reviewed preprint. The data it fits are mostly from McCulloch's own collaborators or DARPA-programme partners (Becker & Bhatt, Pérez-Díaz, Mansell, Neunzig/Tajmar). Agreement with them is not independent support.
- **Post-hoc revision (editorial reading):** the paper says the electron-based reinterpretation is made "admittedly now with hindsight" (p. 6). The new formula puts photon-device predictions at 0.4–40 nN, at or below the Dresden balance's noise. TU Dresden had tested QI predictions 2–3 orders of magnitude above photon thrust and found only photon thrust ([Neunzig et al. 2022, laser resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md)). In a follow-up that addressed McCulloch's objections, the fibre loop gave ≤ 0.09 ± 0.18 µN against QI predictions of 0.34–2.23 µN ([2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md)). Under the revised model these nulls become "consistent", so they no longer test QI.
- **EmDrive:** Dresden's replications of EmDrive-type devices found that earlier positive signals were artefacts ([2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md)). This paper treats Shawyer's 16 mN as a genuine thrust to be explained.
- **Capacitor:** the Becker & Bhatt result it fits ([2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md)) is unreplicated. A clean replication by [Tajmar & Schreiber 2020](../../03-criticism/2020-tajmar-capacitor-thrust/README.md) found < 0.3 mg against 6.8 mg expected from Becker & Bhatt's data, with caveats about replication differences. This preprint does not mention that test.
- **Scaling with plate separation (editorial):** Eq. 5 gives a 1/d² power law. Becker & Bhatt, and Tajmar & Schreiber's fit to their data, describe the force as rising exponentially as d shrinks. Saying it varies "in exactly the manner predicted by QI" is the author's claim; the paper compares only one separation numerically.
- **Two different capacitor formulas:** this preprint's capacitor force depends on plate area; the July 2021 copy of [2021-mcculloch-symmetric-capacitors](../2021-mcculloch-symmetric-capacitors/README.md) (F = N_eħc/2ns²) does not. Both are presented as QI's prediction for the same experiment.
- **Asymmetric-Casimir framing of QI generally:**
  - [Dickmann et al. 2023 (2023-dickmann-casimir-contradicts)](../../03-criticism/2023-dickmann-casimir-contradicts/README.md) argued that QI's cavity mechanism is inconsistent with the measured Casimir effect.
  - [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md) criticised the original "inertia from an asymmetric Casimir effect" derivation.
- No critique aimed specifically at this preprint was found.

## Related
- Evidence: [propulsion](../../02-evidence/propulsion.md), [derivation](../../02-evidence/derivation.md), [lab-tests](../../02-evidence/lab-tests.md), [emdrive](../../02-evidence/emdrive.md)
- Sources: [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2021-mcculloch-symmetric-capacitors](../2021-mcculloch-symmetric-capacitors/README.md), [2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md), [2020-mcculloch-nano-materials](../2020-mcculloch-nano-materials/README.md), [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md), [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md), [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md), [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md), [2019-mcculloch-wide-binaries](../2019-mcculloch-wide-binaries/README.md)
