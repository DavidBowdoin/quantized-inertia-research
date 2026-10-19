---
title: "Can the Tajmar effect be explained using a modification of inertia?"
authors: [Michael E. McCulloch]
year: 2010
type: paper
venue: "EPL (Europhysics Letters) 89(1), 19001"
doi: 10.1209/0295-5075/89/19001
arxiv: "0912.1108"
url: "https://doi.org/10.1209/0295-5075/89/19001"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-setup-b-schematic.png]
status: supports
tags: [tajmar-effect, lab-test]
---

# Can the Tajmar effect be explained using a modification of inertia?

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:0912.1108](https://arxiv.org/abs/0912.1108) · [doi:10.1209/0295-5075/89/19001](https://doi.org/10.1209/0295-5075/89/19001).

**Citation:** McCulloch, M. E. (2010). *Can the Tajmar effect be explained using a modification of inertia?* EPL (Europhysics Letters) 89(1), 19001. [doi:10.1209/0295-5075/89/19001](https://doi.org/10.1209/0295-5075/89/19001) / [arXiv:0912.1108](https://arxiv.org/abs/0912.1108)

**TL;DR:** This paper applies MiHsC to the "Tajmar effect": small anomalous gyroscope accelerations reported above supercooled spinning rings. The gyroscope's inertia is taken to depend on its acceleration relative to the fixed stars (via Earth's spin) and to the nearby ring, weighted by mass over distance squared. When the ring spins up, the gyroscope's inertia rises slightly. Conserving momentum then gives a clockwise gyro/ring acceleration ratio of 1.78 ± 0.25 × 10⁻⁸; the observed ratio was 3 ± 1.2 × 10⁻⁸. The model does not explain the parity violation seen in setup A.

> Text and page numbers are from arXiv v1 (Dec 2009), stored as `paper.pdf`.

## Key claims
- Following Mach's principle, the acceleration in the MiHsC inertia formula is taken relative to all surrounding masses. Here those are the fixed stars (seen via the Earth's rotation and orbit) and the spinning ring.
- Cooling suppresses nearby atomic thermal accelerations, so the gyroscope's inertia becomes sensitive to the small fixed-star acceleration (0.0371 m/s² at Seibersdorf, 48° N). Its inertia falls by ~2 × 10⁻¹⁰ kg per kg.
- When the ring accelerates, the gyroscope's inertia rises again. To conserve momentum in the fixed-star frame, it must rotate opposite to the Earth's spin: clockwise in the northern hemisphere.
- The predicted ratio agrees within errors with Tajmar et al. (2009) setup B, but the model does not predict the parity violation seen in setup A.
- The paper raises a criticism of MiHsC itself: why ignore the large accelerations of atoms in the spinning fixed stars?

## Key equations
MiHsC inertia:
$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{|a|\Theta}\right) $$
Momentum conservation with modified inertia:
$$ v_{gs2} - v_{gs1} = \frac{\beta\pi^2 c^2}{\Theta}\left(\frac{v_{gs2}}{|a_{g2}|} - \frac{v_{gs1}}{|a_{g1}|}\right) $$
Weighted mean acceleration (fixed stars s, ring R):
$$ a_{g2} = \frac{\frac{m_s}{r_s^2}a_s + \frac{m_R}{r_R^2}a_R}{\frac{m_s}{r_s^2} + \frac{m_R}{r_R^2}} $$
Predicted anomalous acceleration:
$$ da' \sim -\frac{\beta\pi^2 c^2}{\Theta}\frac{a_{gs}}{|a_s|} \sim -\frac{6.6\times10^{-10}}{0.0371}a_{gs} \sim -1.78 \pm 0.25 \times 10^{-8}\, a_{gs} $$

## Data used
- Tajmar, Plesescu & Seifert (2009, *J. Phys. Conf. Ser.* 150, 032101), setup B: a laser gyroscope above a stainless-steel ring of radius 0.075 m and mass ~0.336 kg, with ring angular acceleration 33 rad/s² (2.5 m/s²). Rings of niobium, aluminium, YBCO and Teflon gave similar results.
- Total stellar mass ~2.4 × 10⁵² kg (Funkhouser 2006) at r_s ~ 2.7 × 10²⁶ m. Ring distance r_R ~ 0.039 m. Error bars assume a 9% uncertainty in H.

## Results & predictions
- Predicted gyro/ring acceleration ratio: −1.78 ± 0.25 × 10⁻⁸, clockwise. A more exact calculation with the full weighting equation gives −1.8 × 10⁻⁸.
- Observed: about −3 ± 1.2 × 10⁻⁸ at 5 K, rising from zero above ~25 K.
- In a uniformly cold environment the effect falls to half its size at r_R = 56 m. In a warm laboratory, the paper argues it should fall off with distance squared. It compares this with the observed difference between setups A (no decay) and C (fast decay).
- Proposed tests:
  - Repeat setup B in the southern hemisphere, where the effect should be anticlockwise.
  - Run the experiment in a frame counter-rotating against the Earth's spin, where the effect should be larger.
  - Spin the ring with acceleration near 0.036 m/s², where the effect should vanish, and below that, where it should reverse (up to ~229× larger).
  - Look for a latitude dependence of weight.

## Figures
*Figure (local only): Fig. 1 — Schematic of Tajmar et al.'s setup B: the spinning ring, the laser gyroscope above it, dimensions, and the fixed stars (p. 9).*

## Notable quotes
> "However, this model does not explain the parity violation seen in some of the gyroscope data." (p. 1)

> "Why should the acceleration of the accelerometer with respect to the fixed stars be only 0.0371m/s² as assumed here, when the fixed stars are rotating with larger accelerations than this and contain atoms with very large accelerations?" (p. 6)

## Criticisms & responses
- **The effect being explained has not been confirmed.** The paper itself notes that the Tajmar effect "has not yet been reproduced in another laboratory". A search by the Canterbury ring-laser group for frame-dragging from a spinning lead disc at 4 K (Graham et al. 2008) found no signal. Tajmar et al. ([arXiv:0806.2271](https://arxiv.org/abs/0806.2271)) report that test as about two orders of magnitude less sensitive than their own design.
  - > [!UNVERIFIED] The full bibliographic details of Graham et al. (2008) were not checked here.
- **Parity violation.** The paper concedes that it does not reproduce the setup-A parity violation. A follow-up paper attempts to address it; see [2011-mcculloch-tajmar-effect](../2011-mcculloch-tajmar-effect/README.md).
- **Ad hoc weighting.** The mass/distance² weighting of contributions to inertia is assumed. The paper says its details do not affect the final result.
- For later Tajmar-group tests of QI-related claims, see [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md) and [2018-tajmar-spacedrive](../../04-experiments/2018-tajmar-spacedrive/README.md).

## Related
- Evidence: [lab-tests](../../02-evidence/lab-tests.md), [other-anomalies](../../02-evidence/other-anomalies.md)
- Sources:
  - [2011-mcculloch-tajmar-effect](../2011-mcculloch-tajmar-effect/README.md)
  - [2011-mcculloch-podkletnov-effect](../2011-mcculloch-podkletnov-effect/README.md)
  - [2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md)
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
