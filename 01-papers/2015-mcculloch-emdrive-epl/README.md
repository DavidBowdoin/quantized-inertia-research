---
title: Testing quantised inertia on the emdrive
authors: [Michael E. McCulloch]
year: 2015
type: paper
venue: "EPL (Europhysics Letters) 111(6), 60005"
doi: 10.1209/0295-5075/111/60005
arxiv: 1604.03449
url: "https://doi.org/10.1209/0295-5075/111/60005"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, figures/fig-1-cavity.png]
status: supports
tags: [emdrive, propulsion, lab-test]
---

# Testing quantised inertia on the emdrive

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1604.03449](https://arxiv.org/abs/1604.03449) · [doi:10.1209/0295-5075/111/60005](https://doi.org/10.1209/0295-5075/111/60005).

**Citation:** McCulloch, M. E. (2015). *Testing quantised inertia on the emdrive*. EPL 111(6), 60005. https://doi.org/10.1209/0295-5075/111/60005. Preprint: [arXiv:1604.03449](https://arxiv.org/abs/1604.03449) (posted April 2016; `paper.pdf` is the arXiv version).

**TL;DR:** This paper extends the 1-D model in the Progress in Physics paper ([2015-mcculloch-emdrive-pip](../2015-mcculloch-emdrive-pip/README.md)) to a crude 3-D one. The assumption is that photons in a tapered microwave cavity have an inertial mass set by Unruh waves, which must fit inside the cavity. More waves fit at the wide end, so photons gain inertia going that way, and conserving momentum pushes the cavity towards its narrow end. The model has no adjustable parameters. Its predictions are compared with 8 published emdrive thrust measurements and are of the right order of magnitude, but off by more than 10× in two NASA cases. It predicts thrust reversal when the axial length equals the small-end diameter.

## Key claims
- Truncated-cone microwave cavities (emdrives) show an anomalous thrust towards the narrow end. The paper says standard physics has no explanation and "an error has not yet been found" (Abstract).
- The inertial mass of the cavity photons is assumed to come from Unruh radiation, with the cavity walls acting as the horizon in place of the Hubble scale. The photons' acceleration (a ~ c²/L) is so large that their Unruh wavelengths are about the size of the cavity (Sec. 2).
- The Unruh waves are averaged crudely over 6 directions inside the cavity (a "3-d" model), replacing the earlier lateral-only model. That earlier model predicted infinite thrust for a pointed cone (Eqs. 8–14).
- The force always points to the narrow end, whichever way the photons travel (Fig. 1, Discussion).
- Thrust should increase with power P, with Q factor, and if c is reduced by a dielectric. Thrust should reverse if L equals the small-end width (Discussion, Conclusion).
- The paper states two "controversial assumptions": photons have a finite inertial mass that varies with MiHsC, and the speed of light changes in the cavity (Discussion).

## Key equations
MiHsC inertial mass (Eq. 1), with Θ twice the Hubble distance:
$$m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) = m\left(1 - \frac{\lambda}{4\Theta}\right)$$

Earlier 1-D thrust formula from McCulloch (2015, Progress in Physics) (Eq. 2):
$$F = -\frac{PQL}{c}\left(\frac{1}{w_s} - \frac{1}{w_b}\right)$$

Momentum conservation for photons whose mass varies (Eqs. 3–5):
$$\frac{\partial (mv)}{\partial t} = 0 = m\frac{\partial v}{\partial t} + v\frac{\partial m}{\partial t}, \qquad F = -c^2\frac{\partial m}{\partial x}$$

3-D-averaged thrust (Eq. 14):
$$F = -\frac{6PQL}{c}\left(\frac{1}{L + 4w_s} - \frac{1}{L + 4w_b}\right)$$

## Data used
Published emdrive thrust tests with documented power, Q and geometry. Cavity dimensions were partly estimated from photographs by forum members (see Acknowledgements):
- Shawyer (2008): S1, S2
- Cannae drive, Fetta (2014): C1
- NASA Eagleworks, Brady et al. (2014): B1–B3, plus the vacuum test B4v
- Tajmar & Fiedler (2015) vacuum test: T1
- Juan et al. (2012, China) was excluded because the Q factor and geometry were not reported.

## Results & predictions
Table 1 of the arXiv version (thrusts in mN):

| Expt | P (W) | Q | L (m) | w_big/w_small (m) | F 1-D | F 3-D | F observed |
|---|---|---|---|---|---|---|---|
| S1 | 850 | 5900 | 0.156 | 0.16/0.1275 | 4.2 | 3.8 | 16 |
| S2 | 1000 | 45,000 | 0.345 | 0.28/0.1289 | 217 | 149 | 80–214 |
| C1 | 10.5 | 11×10⁶ | 0.03 | 0.22/0.2 | 5.3 | 7.3 | 9 |
| B1 | 16.9 | 7,320 | 0.2286 | 0.2794/0.1588 | 0.26 | 0.23 | 0.091 |
| B2 | 16.7 | 18,100 | 〃 | 〃 | 0.63 | 0.57 | 0.05 |
| B3 | 2.6 | 22,000 | 〃 | 〃 | 0.12 | 0.11 | 0.055 |
| B4v | 50 | 6730 | 〃 | 〃 | 0.70 | 0.64 | 0.03 |
| T1 | 700 | 20 | 0.1008 | 0.1062/0.075 | 0.02 | 0.02 | 0.02–0.11 |

- The author says the model "predicts the correct order of magnitude for all the cases". He also says the worst agreements are B2 and B4v, where the prediction is "over a factor of ten out". The 3-D version does "slightly better" than the 1-D version in almost all cases.
- Error bars on the observations are said to be unclear.
- Testable prediction: the thrust reverses when L equals w_s. The paper suggests this "may have been seen in recent NASA experiments".
- The abstract lists observed thrusts as 16, 147, 9, 0.09, 0.05, 0.06, 0.03 and 0.02 mN. The table gives a range for S2 (80–214).

## Figures
*Figure (local only): Fig. 1 — The emdrive cavity (solid line) showing a photon moving right (lower dashed arrows) and then bouncing back towards the left (upper arrows). Line thickness shows the photon's mass and line length shows its speed. In both directions, momentum conservation needs a force towards the narrow end.*

## Notable quotes
> "Standard physics has no explanation for this and an error has not yet been found." (p. 1, Abstract)

> "The worst agreements are for B2 and B4v where MiHsC is over a factor of ten out." (p. 6)

> "This proposal predicts the observations quite well, but makes two controversial assumptions." (p. 7)

## Criticisms & responses
- **The thrust itself.** Later high-precision tests found no thrust beyond experimental artefacts. Dresden (Tajmar group, SpaceDrive project) traced the apparent emdrive thrust to thermal and cabling/magnetic effects. See [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md), [2018-tajmar-spacedrive](../../04-experiments/2018-tajmar-spacedrive/README.md) and [2019-kossling-spacedrive-balance](../../04-experiments/2019-kossling-spacedrive-balance/README.md). If no real thrust exists, the agreement in Table 1 does not support the model.
- **The data.** Several of the input measurements (Shawyer, Cannae, early Eagleworks) came from conference reports without full error budgets. The paper itself says the observational uncertainties are unclear. See also [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md) and [2016-samsonov-emdrive-null](../../03-criticism/2016-samsonov-emdrive-null/README.md).
- **The theory.** The model assumes photons have an inertial mass that varies with cavity width, and that photon speed varies in the cavity. Both conflict with standard electrodynamics, and the author calls them "controversial". General critique of QI: [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).
- **The author's own revision.** McCulloch (2017, EPL 118, 34003) said the photon acceleration assumed here was unnecessary and added dielectric effects. See [2017-mcculloch-emdrives-dielectrics](../2017-mcculloch-emdrives-dielectrics/README.md).

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources:
  - [2015-mcculloch-emdrive-pip](../2015-mcculloch-emdrive-pip/README.md) (1-D predecessor)
  - [2017-mcculloch-emdrives-dielectrics](../2017-mcculloch-emdrives-dielectrics/README.md) (follow-up)
  - [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md)
  - [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md)
  - [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md)
  - [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md)
