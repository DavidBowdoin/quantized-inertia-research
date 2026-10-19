---
title: "Can the Standard Model Predict a Minimum Acceleration That Gets Rid of Dark Matter?"
authors: [Espen Gaarder Haug]
year: 2021
type: paper
venue: "Journal of High Energy Physics, Gravitation and Cosmology 7(2), 602-606"
doi: 10.4236/jhepgc.2021.72035
arxiv:
url: "https://doi.org/10.4236/jhepgc.2021.72035"
open_access: true
license: CC-BY-4.0
files: [paper.pdf, figures/fig-1-sparc-accelerations.png]
status: neutral
tags: [minimum-acceleration, dark-matter, sparc, galaxy-rotation]
---

# Can the Standard Model Predict a Minimum Acceleration That Gets Rid of Dark Matter?

**Citation:** Haug, E. G. (2021). *Can the Standard Model Predict a Minimum Acceleration That Gets Rid of Dark Matter?* Journal of High Energy Physics, Gravitation and Cosmology, 7(2), 602–606. https://doi.org/10.4236/jhepgc.2021.72035 (CC BY 4.0). Received 7 March 2021; published 25 April 2021.

**TL;DR:** Haug proposes a minimum gravitational acceleration taken from the mass and radius of the observable universe, g_min = GM_u/r_u² ≈ 5.18 × 10⁻¹¹ m/s². He adds this term to the Newtonian acceleration of baryonic matter. Plotted against 2,793 SPARC data points from 153 galaxies, the model comes much closer to the observations than baryonic Newtonian gravity. With a radius 1.3 times larger it comes closer still. The paper mentions QI as another minimum-acceleration model and plots QI's prediction, but it does not derive or test QI's 2c²/Θ. The author describes the idea as needing "additional rigorous study".

## Key claims
- Taking gravity's "infinite" extent and the mass of the observable universe into account gives a minimum acceleration that matches galaxy rotations far better than baryonic Newtonian gravity.
- MOND is described as "more of a curve-fitting model" without an explanation for its a₀. The paper presents QI as a model that "according to its inventor, McCulloch," has an explanatory mechanism.
- The proposed model is "non-relativistic" and also explains the minimum acceleration.
- Stated caveats:
  - The uncertainty in the mass and radius of the universe allows the fit to be tuned.
  - A galaxy near "the edge of the observable universe" might show asymmetric arm accelerations (different redshifts on each side), which the author does not believe has been observed.

## Key equations
$$ g_{min} = \frac{GM_u}{r_u^2} \approx \frac{G \times 1.5\times10^{53}}{(4.4\times10^{26})^2} \approx 5.18\times10^{-11}\ \mathrm{m/s^2} $$
$$ a = \frac{GM}{r^2} + g_{min} = \frac{GM}{r^2} + \frac{GM_u}{r_u^2} $$
Mass of the observable universe used for context:
$$ M_u = \frac{c^3}{GH_0} $$

## Data used
- SPARC: 2,793 individual data points for 153 galaxies, via McGaugh, Lelli & Schombert (2016).
- Cosmological inputs:
  - r_u ≈ 4.4 × 10²⁶ m (93 billion light years)
  - M_u ≈ 1.5 × 10⁵³ kg
  - Age 13.77 Gyr, so c × age ≈ 1.3 × 10²⁶ m

## Results & predictions
- g_min ≈ 5.18 × 10⁻¹¹ m/s², which the paper notes is "considerably smaller" than MOND's ≈ 1.2 × 10⁻¹⁰ m/s².
- Fig. 1 shows several curves:
  - The red curve (r_u = 4.4 × 10²⁶ m) is a "strong improvement" over baryonic Newtonian gravity (green).
  - The orange curve (1.3 × r_u) fits better.
  - The variant with 1.3 × r_u and M_u = 10⁵³ kg is also close to the data.
  - With r = 1.3 × 10²⁶ m (light-travel distance, no expansion), the predictions "diverge greatly from observations".
  - MOND (yellow) "fits the observations very well". QI (light blue) lies just below MOND.
- No new quantitative goodness-of-fit statistic is given. The comparison is visual.

## Figures
![Fig. 1 — Galactic accelerations for 2,793 SPARC data points (black dots), shown against baryonic Newtonian predictions (green), MOND (yellow), QI (light blue), and the paper's minimum-acceleration model with r_u = 4.4e26 m (red), 1.3 × r_u (orange), 1.3 × r_u with M_u = 1e53 kg (white/green dots), and r = c × age (blue). Rendered from PDF p. 3 (journal p. 604).](figures/fig-1-sparc-accelerations.png)

## Notable quotes
> "This would, at least, dramatically reduce the amount of dark matter required to push the model to fit observations." (p. 605)

> "However, there may be several issues with this method and the approach requires additional rigorous study." (p. 605)

## Criticisms & responses
- No published critique of this specific paper was found in a brief search.
- **Factual observations:**
  - Adding a constant, direction-less g_min to a radial acceleration is not derived from Newtonian gravity. Under Newton's shell theorem, the net pull of a roughly homogeneous, isotropic universe on a galaxy cancels.
  - The paper itself raises the direction problem for galaxies off-centre in the observable universe.
  - The fit depends on the adopted cosmic mass and radius, which the author treats as adjustable.
- **Relation to QI:** QI's minimum acceleration 2c²/Θ ≈ 2 × 10⁻¹⁰ m/s² is a different quantity, about 4 times larger than this g_min. This paper does not claim to derive it.
- Haug had earlier co-authored a QI derivation: [2018-haug-mcculloch-derivation](../2018-haug-mcculloch-derivation/README.md).

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmology](../../02-evidence/cosmology.md), [derivation](../../02-evidence/derivation.md)
- Sources: [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md), [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md), [2018-haug-mcculloch-derivation](../2018-haug-mcculloch-derivation/README.md), [2012-mcculloch-galactic-scales](../2012-mcculloch-galactic-scales/README.md)
