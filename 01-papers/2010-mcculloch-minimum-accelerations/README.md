---
title: "Minimum accelerations from quantised inertia"
authors: [Michael E. McCulloch]
year: 2010
type: paper
venue: "EPL (Europhysics Letters) 90(2), 29001"
doi: 10.1209/0295-5075/90/29001
arxiv: "1004.3303"
url: "https://doi.org/10.1209/0295-5075/90/29001"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib]
status: supports
tags: [cosmic-acceleration, dwarf-galaxies, galaxy-rotation, lab-test]
---

# Minimum accelerations from quantised inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1004.3303](https://arxiv.org/abs/1004.3303) · [doi:10.1209/0295-5075/90/29001](https://doi.org/10.1209/0295-5075/90/29001).

**Citation:** McCulloch, M. E. (2010). *Minimum accelerations from quantised inertia*. EPL (Europhysics Letters) 90(2), 29001. [doi:10.1209/0295-5075/90/29001](https://doi.org/10.1209/0295-5075/90/29001) / [arXiv:1004.3303](https://arxiv.org/abs/1004.3303)

**TL;DR:** MiHsC (here also called "Quantised Inertia") implies a minimum acceleration of 2c²/Θ for any object, which the paper notes is close to the observed cosmic acceleration. Applied to a disc galaxy at r = 500 pc, it gives a minimum apparent mass of 1.1 × 10⁹ M☉. That matches the observed lower limit of ~10⁹ M☉ for disc galaxies reported by McGaugh et al. (2010). The same argument applied to the observable universe gives ~2 × 10⁵³ kg, close to the critical (closure) mass. The paper proposes a particle-accelerator test of the Unruh-inertia assumption.

> Text and page numbers are from arXiv v1 (Apr 2010), stored as `paper.pdf`. The paper has no figures.

## Key claims
- In the MiHsC inertia formula, |a| is here "the average mutual acceleration of every other mass in the universe", which the paper describes as Mach's principle.
- MiHsC implies a minimum acceleration in nature, 2c²/Θ, even with no gravitating mass nearby. The paper says this is close to the acceleration attributed to dark energy.
- Very low-mass disc galaxies are "at the edge of boundedness". The extra MiHsC term would be misread as dark mass, which sets a minimum apparent disc-galaxy mass.
- Elliptical (pressure-supported) galaxies can be lighter (~10⁷ M☉) because their non-rotational accelerations keep them above the minimum. This explanation is qualitative only.
- The same minimum-acceleration argument for the whole observable universe gives a mass close to the Friedmann closure mass. The paper offers this as a possible explanation of the flatness problem.
- Problems listed by the paper itself:
  1. There is no proven reason why bound and unbound trajectories should behave differently.
  2. It is unclear how such long Unruh waves interact with matter and the Hubble scale.
  3. It is unclear why the large particle accelerations inside stars and atoms can be ignored.
  4. Both the increased sensitivity to force and the momentum changes need to be considered.

## Key equations
MiHsC inertia:
$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{|a|\Theta}\right) $$
Galaxy orbit with βπ² ≈ 2 (stated as a 1.5% error):
$$ \left(1 - \frac{2c^2}{|a|\Theta}\right)a = \frac{GM}{r^2} \;\Rightarrow\; a = \frac{GM}{r^2} + \frac{2c^2}{\Theta}\hat a $$
Minimum acceleration and the apparent dark mass that follows from it:
$$ a = \frac{2c^2}{\Theta}, \qquad M_{dark} = \frac{2c^2 r^2}{G\Theta} $$
Observable universe (r = Θ/2) compared with the closure mass:
$$ M_{dark} = \frac{c^2\Theta}{2G}, \qquad M_{closed} = \frac{c^2\Theta}{4G} $$
Unruh wavelength:
$$ \lambda = \frac{4\beta\pi^2 c^2}{a} $$

## Data used
- Observed minimum baryonic mass of rotationally supported galaxies (~10⁹ M☉ within the central 500 pc), from McGaugh, Schombert, de Blok & Zagursky (2010, *ApJ* 708, L14).
- Θ = 2.7 × 10²⁶ m. Supernova cosmic acceleration (Perlmutter et al. 1999; Riess et al. 1998) is used qualitatively.

## Results & predictions
- Minimum apparent disc-galaxy mass within 500 pc: 2.3 × 10³⁹ kg = 1.1 × 10⁹ M☉. Observed: ~10⁹ M☉.
- MiHsC "minimum" mass of the observable universe: 2 × 10⁵³ kg. Closure mass: 1 × 10⁵³ kg.
- Proposed lab test, a particle at 0.9c in a 1 km ring:
  - The particle's acceleration is 7.3 × 10¹³ m/s², so the Unruh wavelength it sees is 9.7 km.
  - Applying man-made radiation of 22 km wavelength (which the moving particle sees as 9.7 km) should, if assumption 1 is right, increase its inertia detectably.
- At 9.8 m/s² the Unruh wavelength is ~10¹⁶ m.

## Figures
No figures in this paper.

## Notable quotes
> "MiHsC (the second term on the right hand side) predicts that an object must still accelerate: there is a minimum acceleration in nature." (p. 4)

> "1) there is no proven reason why bound and unbound trajectories should behave differently, 2) how do such long Unruh waves interact with matter and the Hubble scale?" (p. 6)

## Criticisms & responses
- **Open issues stated by the paper.** The paper lists its own unresolved problems (see Key claims). The most significant is the unexplained difference between bound and unbound systems.
- **Pioneer basis.** The paper treats the Pioneer anomaly as unexplained and says the thermal studies then available account for "up to one third" of it. Turyshev et al. (2012) later attributed the whole anomaly to thermal recoil; see [2012-turyshev-pioneer-thermal](../../03-criticism/2012-turyshev-pioneer-thermal/README.md).
- **Derivation of the minimum acceleration.** Renda (2019) disputes the physical basis of QI's Hubble-scale Casimir effect and inertia formula; see [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).
- > [!UNVERIFIED] No published attempt to carry out the proposed accelerator test was found in a brief search.

## Related
- Evidence:
  - [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md)
  - [dwarf-galaxies](../../02-evidence/dwarf-galaxies.md)
  - [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
  - [lab-tests](../../02-evidence/lab-tests.md)
  - [cosmology](../../02-evidence/cosmology.md)
- Sources:
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
  - [2012-mcculloch-galactic-scales](../2012-mcculloch-galactic-scales/README.md)
  - [2017-mcculloch-dwarf-galaxies](../2017-mcculloch-dwarf-galaxies/README.md)
  - [2021-haug-minimum-acceleration](../2021-haug-minimum-acceleration/README.md)
  - [2014-mcculloch-toy-cosmology](../2014-mcculloch-toy-cosmology/README.md)
