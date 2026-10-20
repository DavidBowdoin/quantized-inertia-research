---
title: "Hawking effect and Unruh effect from the uncertainty principle"
authors: [Jaume Giné]
year: 2018
type: paper
venue: "EPL 121(1):10001"
doi: 10.1209/0295-5075/121/10001
arxiv:
url: "https://doi.org/10.1209/0295-5075/121/10001"
open_access: false
license: all-rights-reserved
files: [paper.pdf, citation.bib, figures/fig-2-rindler-half-sphere.png]
status: neutral
tags: [unruh, uncertainty-principle]
---

# Hawking effect and Unruh effect from the uncertainty principle

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.1209/0295-5075/121/10001](https://doi.org/10.1209/0295-5075/121/10001).

**Citation:** Giné, J. (2018). *Hawking effect and Unruh effect from the uncertainty principle*. EPL (Europhysics Letters), 121(1), 10001 (4 pp.; issue dated January 2018). Received 30 Aug 2017, accepted 20 Nov 2017, published online 1 Mar 2018. https://doi.org/10.1209/0295-5075/121/10001

**About the stored PDF:** `paper.pdf` is the published EPL version (owner-supplied, local only; © EPLA 2018). PDF p. 1 is a publisher cover sheet, so article pages 10001-p1 to -p4 are PDF pp. 2–5. Page references below use the printed article page numbers.

**Authorship:** sole author Jaume Giné (Lleida, Inspires Research Centre), confirmed on the PDF. Giné is a frequent McCulloch co-author, but this paper does not discuss QI. It cites two McCulloch uncertainty-principle papers and his 2014 book.

**TL;DR:** A four-page letter that recovers the exact Unruh temperature ħa/(2πck_B) and Hawking temperature ħc³/(8πGMk_B) from ΔpΔx ≃ ħ/2 and E = pc = k_BT. The key step is the choice of Δx. For the Unruh case Giné takes the half-circumference πc²/a of a hemispherical Rindler horizon. For the Hawking case he takes the full circumference 2πr_s of the black-hole horizon. He then derives the Bekenstein–Hawking entropy S = k_Bc³A/(4Għ) from dS = dQ/T. Earlier heuristic derivations (Scardigli 1995; McCulloch's 2014 book) are described as giving only approximate values. Later QI papers reuse the half-circumference choice to get the QI formula "exactly".

## Key claims
- Both temperatures follow from vacuum fluctuations producing a pair near a horizon, with the uncertainty principle applied to the partner that crosses the horizon (pp. 10001-p1, -p2).
- **Unruh:** the Rindler horizon is at c²/a "in any direction to its left", so "a first approximation of this Rindler event horizon is to consider it as a half sphere" (p. 10001-p1). Since Δx is one-dimensional and should be maximal, Giné takes the plane through the crossing point and the observer. Its intersection with the half-sphere is a semicircle of length L = 2A/r = πr, so Δx = πc²/a (p. 10001-p2).
- **Hawking:** the same reasoning applied to the full spherical horizon gives a full circle, L = 2πr, so Δx = 2πr_s = 4πGM/c² (pp. 10001-p2, -p3).
- Using the horizon surface gravity g = c⁴/(4GM), the Hawking temperature equals the Unruh temperature for acceleration g (Eq. 17).
- Integrating dS = dQ/T with dQ = c²dM gives S = (1/4)k_Bc³A/(Għ), the Bekenstein–Hawking entropy (Eq. 20).
- "Although we have made an approximation assuming a half spherical Rindler horizon and spherical event horizon of a black hole, the expressions derived are exactly in agreement with those previously known … Hence these approximations must be in a good agreement with the reality" (p. 10001-p3).

## Key equations
Transcribed from the PDF.

Uncertainty principle and the Unruh temperature (Eqs. 1–2):
$$ \Delta p\,\Delta x \simeq \frac{\hbar}{2} \;\;(1), \qquad T = \frac{\hbar a}{2\pi c k_B} \;\;(2) $$

Unruh derivation (Eqs. 3–8, p. 10001-p2):
$$ L = \frac{2A}{r} = \pi r \;\;(3), \qquad \Delta x = \frac{\pi c^2}{a} \;\;(4), \qquad \Delta p\,\frac{\pi c^2}{a} \simeq \frac{\hbar}{2} \;\;(5), \qquad \Delta p \simeq \frac{\hbar a}{2\pi c^2} \;\;(6) $$
$$ \Delta E \simeq \frac{\hbar a}{2\pi c} \;\;(7), \qquad \Delta T \simeq \frac{\hbar a}{2\pi c k_B} \;\;(8) $$

Hawking derivation (Eqs. 9–17, pp. 10001-p2, -p3):
$$ L = \frac{2A}{r} = 2\pi r \;\;(9), \qquad \Delta x = \frac{4\pi GM}{c^2} \;\;(10), \qquad \Delta p \simeq \frac{\hbar c^2}{8\pi GM} \;\;(12), \qquad \Delta E \simeq \frac{\hbar c^3}{8\pi GM} \;\;(13), \qquad \Delta T \simeq \frac{\hbar c^3}{8\pi k_B GM} \;\;(14) $$
$$ g = \frac{GM}{r_s^2} = \frac{c^4}{4GM} \;\;(15\text{–}16), \qquad T = \frac{\hbar c^3}{8\pi GMk_B} = \frac{\hbar}{2\pi c k_B}\left(\frac{c^4}{4GM}\right) = \frac{\hbar g}{2\pi c k_B} \;\;(17) $$

Entropy (Eqs. 18–20):
$$ dS = \frac{dQ}{T} = \frac{8\pi GMk_B}{\hbar c^3}\,dQ \;\;(18), \qquad S = \frac{Gk_B}{\hbar c}4\pi M^2 = \frac{Gk_B}{\hbar c}\frac{c^4 r_s^2}{4G^2}4\pi = \frac14\frac{k_B c^3 A}{G\hbar} \;\;(20) $$

Editorial checks:
- Eqs. 4 → 8 and 10 → 14 follow algebraically from Eq. 1 with ΔE = cΔp and E = k_BT ✓. Eq. 20 follows from Eq. 18 with A = 4πr_s² ✓.
- The geometric factor is what makes the results "exact". Δx = c²/a or r_s (horizon distance) would give T too large by π (Unruh) or 2π (Hawking). The half-circle is used for the Rindler case and the full circle for the black hole, each justified by the assumed horizon shape.
- Small wording slip: Eq. 9 calls A = πr² "the area of the sphere"; it is the area of the disc.

## Data used
- None (theoretical).

## Results & predictions
- Reproduces the standard Unruh temperature, Hawking temperature and Bekenstein–Hawking entropy exactly. Nothing new is predicted.
- The step that later QI papers adopt is Δx = π × (horizon distance) for a Rindler horizon. [McCulloch & Giné 2020](../2020-mcculloch-horizon-widths/README.md) and [Giné & Luciano 2020](../2020-gine-luciano-eup-modified-inertia/README.md) use it to derive m_I = m(1 − 2c²/aΘ).

## Figures
*Figure (local only): Fig. 2: The approximate half-sphere of the Rindler event horizon to the left of the accelerated observer, with the circular sector (a semicircle of length πc²/a) used as the position uncertainty Δx. (PDF p. 3.)*

## Notable quotes
> "Hence a first approximation of this Rindler event horizon is to consider it as a half sphere in the spatial dimensions." (p. 10001-p1)

> "So we have Δx = πr_R, where r_R is the Rindler radius of the Rindler event horizon that coincides with the distance from the observer to the Rindler event horizon" (p. 10001-p2)

> "Hence these approximations must be in a good agreement with the reality." (p. 10001-p3)

## Criticisms & responses
- **The Δx choice is fixed by the answer.** Heuristic uncertainty-principle derivations of T_H and T_U reproduce the standard results only up to O(1) factors that depend on the choice of Δx. Here the factors π and 2π come from taking the horizon half-circumference or circumference. The argument that this "must be in a good agreement with the reality" because it reproduces the known results (p. 10001-p3) is circular as a test of the method. McCulloch later wrote of the related width step in his QI derivation that "there is no good justification for using the width instead of the area" ([2020-mcculloch-information-theory](../2020-mcculloch-information-theory/README.md)). (Editorial reading.)
- **Inconsistent geometry between cases** (editorial): the Unruh case uses half the horizon (hemisphere) and the Hawking case the whole horizon. Both are presented as "the maximal value of Δx", so the rule is not one uniform prescription.
- **Relevance to Renda (2019):** this derivation does not use the discrete Unruh-spectrum sum that [Renda (2019)](../../03-criticism/2019-renda-sceptical/README.md) criticised, so his objections do not apply to it directly. No one has published an assessment of whether the QI derivations built on it avoid them.
- **Later reuse:** [Giné & Luciano (2021)](../2021-gine-luciano-inertia-fluctuations/README.md) keep the hemispherical Rindler horizon and the HUP style of argument (ΔE ≃ ħc/2Δx) for their resonant-parts model.
- No published critique specific to this paper was found in a brief search.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources:
  - [2014-mcculloch-gravity-uncertainty](../2014-mcculloch-gravity-uncertainty/README.md) (Ref. 5)
  - [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md) (Ref. 6)
  - [2014-mcculloch-physics-from-edge](../../07-media/2014-mcculloch-physics-from-edge/README.md) (Ref. 14; "only approximations" there)
  - [2017-gine-inertial-mass-holographic](../2017-gine-inertial-mass-holographic/README.md) (Ref. 12)
  - [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md) (the companion paper)
  - [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md)
  - [2020-gine-luciano-eup-modified-inertia](../2020-gine-luciano-eup-modified-inertia/README.md)
  - [2021-gine-luciano-inertia-fluctuations](../2021-gine-luciano-inertia-fluctuations/README.md)
  - [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md)
  - [2019-kholupenko-unruh-anisotropy-1](../2019-kholupenko-unruh-anisotropy-1/README.md)
