---
title: "Can We Hide Gravitational Sources behind Rindler Horizons?"
authors: [Michael Edward McCulloch]
year: 2019
type: paper
venue: "Progress in Physics 15(2), 72-74"
doi:
arxiv:
url: "https://progress-in-physics.com/2019/PP-57-05.PDF"
open_access: true
license: CC-BY-NC-ND-2.5
files: [paper.pdf, figures/fig-1-hubble-rindler-schematic.png]
status: supports
tags: [lab-test, gravity, rindler-horizon]
---

# Can We Hide Gravitational Sources behind Rindler Horizons?

<!-- local-only-note -->
> 📁 **Local only:** the figures rendered from this paper are kept out of the public repository (`CC-BY-NC-ND-2.5` does not permit derivatives). The PDF itself is included.

**Citation:** McCulloch, M. E. (2019). *Can We Hide Gravitational Sources behind Rindler Horizons?* Progress in Physics, 15(2), 72–74. https://progress-in-physics.com/2019/PP-57-05.PDF (submitted 5 May 2019).

**TL;DR:** The paper takes the Machian stance that "what cannot be observed does not exist" and argues that mass behind an object's Rindler horizon stops pulling on it gravitationally. Applied to a photon in its Hubble sphere, this gives an acceleration of order the cosmic acceleration. Applied to a spinning disc, it proposes a lab test: above about 1.4 × 10¹⁰ m/s² the horizon should come close enough to hide part of the Earth's gravity, and the disc's weight should change. The work was funded by DARPA grant HR001118C0125.

## Key claims
- An accelerating object has a Rindler horizon at a distance c²/a behind it. Gravitational sources beyond that horizon are hidden from the object.
- For a photon, all the mass behind it is hidden. The resulting gravitational imbalance reproduces the observed cosmic acceleration and the galactic critical acceleration, an alternative route to the QI result in Eq. 3.
- Every particle in a spinning disc accelerates toward the axis. At a high enough spin rate the Rindler horizon would fall closer than the Sun or the Earth, and the disc would stop feeling part of their gravity.
- Hiding the Sun at r = 0.1 m needs about 23k rpm, which the paper says is achievable. Hiding the Earth needs about 1.43 × 10¹⁰ m/s². The paper says Arita et al. (2013) reached 1.58 × 10¹⁰ m/s² with a laser-spun microsphere.
- The paper suggests this could give "new kinds of thrust".

## Key equations
QI modified inertial mass:
$$ m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) $$
Resulting dynamics:
$$ a = \frac{GM}{r^2} + \frac{2c^2}{\Theta} $$
Spinning-disc acceleration, Rindler-horizon distance, and required rpm:
$$ a = \frac{4\pi^2 r R^2}{3600}, \qquad d_R = \frac{c^2}{a} = \frac{900\,c^2}{\pi^2 r R^2}, \qquad R = \sqrt{\frac{900\,c^2}{\pi^2 r d_R}} $$

## Data used
- Cosmic baryonic mass of 10^(52±1) kg and Hubble radius of 4.4 × 10²⁶ m. In the text the radius first appears as "4.4 × 10⁻¹⁰ m", which looks like a typo, because Eq. 5 uses 4.4 × 10²⁶.
- The Arita, Mazilu & Dholakia (2013) laser-rotated microgyroscope: r = 4 × 10⁻⁶ m, 6 × 10⁸ rpm.

## Results & predictions
- Photon-in-Hubble-sphere estimate: a = 2.45 × 10^(−11±1) m/s². The paper says this agrees with the observed cosmic acceleration and the galactic critical acceleration of about 2 × 10⁻¹⁰ m/s².
- Table 1, for a disc at r = 0.1 m:

| Object | Distance | a needed (m/s²) | rpm | a_g (m/s²) |
|---|---|---|---|---|
| Sun | 1 AU | 600,000 | 23 k | 0.006 |
| Earth | 6371 km | 1.43 × 10¹⁰ | 3589 k | 9.8 |

- Expected Sun signal for a disc of radius 0.2 m, averaged over the whole disc: about 6.25 × 10⁻⁶ m/s².

## Figures
*Figure (local only): Fig. 1 — Schematic of the Hubble horizon with a photon moving rightwards at c. Its Rindler horizon passes through it, so mass in the shaded left half is "irrelevant" and the right half's pull dominates, which the paper says predicts cosmic acceleration. (Rendered page 2 of the PDF.)*

## Notable quotes
> "if an object, say a disc, is rotationally accelerated by over ∼10¹⁰ m/s² then the Rindler horizon it sees should come close enough to hide part of the Earth" (abstract, p. 72)

> "It is proposed here that Rindler horizons have physical consequences beyond their effects on light: they are able to hide gravitational sources." (p. 74)

## Criticisms & responses
- > [!UNVERIFIED] A brief search found no published experimental test or critique that addresses this specific spinning-disc proposal.
- Mainstream physics treats a Rindler horizon as an observer-dependent causal boundary, not a physical screen for an already-established gravitational field. Renda 2019 raises the general QI concerns: [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).
- Context: DARPA funded McCulloch's QI lab-test programme (see [2018 Plymouth DARPA press](../../07-media/2018-plymouth-darpa/README.md)). Related rotating-mass and propellantless tests by Tajmar's group are in [04-experiments](../../04-experiments/2018-tajmar-spacedrive/README.md).

## Related
- Evidence: [lab-tests](../../02-evidence/lab-tests.md), [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md), [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md), [2014-mcculloch-physics-from-edge](../../07-media/2014-mcculloch-physics-from-edge/README.md)
