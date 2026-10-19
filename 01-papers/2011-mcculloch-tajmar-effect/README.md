---
title: "The Tajmar effect from quantised inertia"
authors: [Michael E. McCulloch]
year: 2011
type: paper
venue: "EPL (Europhysics Letters) 95(3), 39002"
doi: 10.1209/0295-5075/95/39002
arxiv: "1106.3266"
url: "https://doi.org/10.1209/0295-5075/95/39002"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-setup-a-schematic.png]
status: supports
tags: [tajmar-effect, lab-test]
---

# The Tajmar effect from quantised inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1106.3266](https://arxiv.org/abs/1106.3266) · [doi:10.1209/0295-5075/95/39002](https://doi.org/10.1209/0295-5075/95/39002).

**Citation:** McCulloch, M. E. (2011). *The Tajmar effect from quantised inertia*. EPL (Europhysics Letters) 95(3), 39002. [doi:10.1209/0295-5075/95/39002](https://doi.org/10.1209/0295-5075/95/39002) / [arXiv:1106.3266](https://arxiv.org/abs/1106.3266)

**TL;DR:** This revises the 2010 MiHsC model of the Tajmar spinning-ring anomaly. Momentum is now conserved relative to the moving ring instead of the fixed stars, which the author says was "the wrong reference frame". The gyroscope then follows the ring, with a gyro/ring ratio of 1.78 ± 0.16 × 10⁻⁸. When the gyro's own rotation relative to the fixed stars is included, the ratio becomes 2.67 ± 0.24 × 10⁻⁸ for clockwise and 1.34 ± 0.12 × 10⁻⁸ for anticlockwise rotation. Observed: 3 ± 1.2 × 10⁻⁸ and 1.5 ± 1.2 × 10⁻⁸. The model thus accounts for the parity asymmetry. It replaces the 2010 paper's southern-hemisphere prediction.

> Text and page numbers are from arXiv v1 (Jun 2011), stored as `paper.pdf`.

## Key claims
- Conserving momentum relative to the ring explains setup A of Tajmar et al. (2009), including its parity violation. It also explains setup B "if the bias is corrected"; Tajmar said in a personal communication that setup B's rotation direction may have had a clockwise bias.
- The parity violation arises because a gyroscope co-rotating with the ring changes its acceleration relative to the fixed stars. Clockwise co-rotation opposes the Earth's spin, which lowers a_gs and gives a larger effect.
- This corrects the 2010 prediction. In the southern hemisphere, the gyroscope should still follow the ring, but the larger signal should be for anticlockwise rotation.
- The paper argues MiHsC's violation of the equivalence principle would not appear in torsion-balance tests, because rigidly connected masses share the same acceleration relative to distant masses.
- The paper reports that the EPOXI Earth flyby showed zero anomaly although MiHsC predicted a large one. It attributes this to EPOXI's larger periapse (49,835 km). It adds that flyby fits improve if accelerations within the Sun are assumed to be 1 m/s², and that "it is not known whether this value is realistic".

## Key equations
MiHsC inertia:
$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{|a|\Theta}\right) $$
Momentum conservation relative to the ring:
$$ v_{gr2} - v_{gr1} = \frac{\beta\pi^2 c^2}{\Theta}\left(\frac{v_{gr2}}{|a_{g2}|} - \frac{v_{gr1}}{|a_{g1}|}\right) $$
Predicted anomalous acceleration:
$$ da' \sim \frac{\beta\pi^2 c^2}{\Theta}\frac{a_{rg}}{|a_{gs}|} \sim \frac{6.6\times10^{-10}}{0.0371}a_{rg} \sim 1.78 \pm 0.16 \times 10^{-8}\, a_{rg} $$

## Data used
- Tajmar, Plesescu & Seifert (2009, *J. Phys. Conf. Ser.* 150, 032101), setup A: three laser gyroscopes above a cooled ring.
- Ring mass ~0.336 kg; r_R ~ 0.0533 m; a_R = 2.5 m/s²; a_s = 0.0371 m/s² at Seibersdorf (48° N).
- Fixed stars: m_s ~ 2.4 × 10⁵² kg at r_s ~ 2.7 × 10²⁶ m. A 9% uncertainty in H is assumed.
- Reported in the text: at the ring's top speed, the anomalous gyro output equalled one third of the Earth's rotation rate.

## Results & predictions
| Case | Predicted gyro/ring ratio | Observed |
|---|---|---|
| Basic (no gyro co-rotation) | 1.78 ± 0.16 × 10⁻⁸ | 3 ± 1.2 × 10⁻⁸ |
| Clockwise | 2.67 ± 0.24 × 10⁻⁸ | 3 ± 1.2 × 10⁻⁸ |
| Anticlockwise | 1.34 ± 0.12 × 10⁻⁸ | 1.5 ± 1.2 × 10⁻⁸ |

- Predicted decay with distance (setup A): 0.03%, 0.8%, 11.5% and 50% smaller at 1, 5, 20 and 56 m.
- Proposed test: reduce the ring mass by ≥10,000×. The ratio at the lower gyro (0.0553 m) should stay the same, while the upper gyro (0.2283 m) should see a 13.6% drop.
- Southern-hemisphere prediction: the gyro co-rotates, and the larger signal is anticlockwise.

## Figures
*Figure (local only): Fig. 1 — Schematic of Tajmar et al.'s setup A: the ring, the lower, middle and upper laser gyroscopes, dimensions, and the fixed stars (p. 9).*

## Notable quotes
> "A previous paper by the author applied the same theory [10], but it is now thought that the reference frame used was wrong, so that the proposed test (an exact mirror-image result in the southern hemisphere) was wrong." (p. 7)

> "The flyby anomalies can be predicted more successfully, if the accelerations within the Sun are assumed to be 1m/s². It is not known whether this value is realistic." (p. 7)

## Criticisms & responses
- **Unreplicated target effect.** The paper states the Tajmar effect "has not yet been reproduced in another laboratory". A search by the Canterbury ring-laser group (Graham et al. 2008) for frame-dragging from a spinning lead disc at 4 K found no signal; it is discussed in Tajmar et al. ([arXiv:0806.2271](https://arxiv.org/abs/0806.2271)).
  - > [!UNVERIFIED] Later Tajmar-group reports on whether the effect persisted were not checked here.
- **Changing frames.** The change of reference frame between the 2010 and 2011 papers reverses the main prediction (mirror-image rotation in the southern hemisphere becomes co-rotation everywhere). Readers may see this as post-hoc flexibility. The change of frame is the author's own correction, based on a personal communication from Tajmar about a bias in setup B.
- **Flyby side-note.** The admission of a zero EPOXI anomaly where MiHsC predicted a large one is relevant to [2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md).
- For later Tajmar-group experiments testing QI claims, see [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md).

## Related
- Evidence:
  - [lab-tests](../../02-evidence/lab-tests.md)
  - [other-anomalies](../../02-evidence/other-anomalies.md)
  - [flyby-anomaly](../../02-evidence/flyby-anomaly.md)
- Sources:
  - [2010-mcculloch-tajmar-effect-explained](../2010-mcculloch-tajmar-effect-explained/README.md)
  - [2011-mcculloch-podkletnov-effect](../2011-mcculloch-podkletnov-effect/README.md)
  - [2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md)
