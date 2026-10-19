---
title: "The Pioneer anomaly and the holographic scenario"
authors: [Jaume Giné]
year: 2011
type: paper
venue: "Astrophysics and Space Science 337(1), 483-486"
doi: 10.1007/s10509-011-0840-5
arxiv: "1108.3565"
url: "https://arxiv.org/abs/1108.3565"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib]
status: supports
tags: [pioneer-anomaly, holographic, verlinde]
---

# The Pioneer anomaly and the holographic scenario

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1108.3565](https://arxiv.org/abs/1108.3565) · [doi:10.1007/s10509-011-0840-5](https://doi.org/10.1007/s10509-011-0840-5).

**Citation:** Giné, J. (2011). *The Pioneer anomaly and the holographic scenario*. Astrophysics and Space Science 337(1), 483-486 (online Sep 2011; issue Jan 2012). [doi:10.1007/s10509-011-0840-5](https://doi.org/10.1007/s10509-011-0840-5) / [arXiv:1108.3565](https://arxiv.org/abs/1108.3565)

**TL;DR:** This is a short (5-page) note by Jaume Giné, who is not one of McCulloch's co-authors. It uses Giné's own MOND-like interpolation function, set within Verlinde's entropic/holographic gravity, to recover McCulloch's (2007) Pioneer formula a = GM/r² + ~cH₀. Giné says McCulloch's Unruh-radiation proposal "acquires its meaning in the wake of the holographic scenario". He also acknowledges that a constant extra acceleration of this size is ruled out in the inner Solar System.

> The volume and pages come from Crossref (337(1), 483-486). The source list for this repository gave volume 335, which appears to be wrong.
>
> Text and page numbers are from arXiv v1 (Aug 2011), stored as `paper.pdf`. The PDF uses two columns, so the extracted text order is imperfect.

## Key claims
- Verlinde's (2011) holographic model gives Newton's second law and gravity from thermodynamics. Funkhouser (2010) showed that in de Sitter space it gives a MOND-like second law, with 2k = 2√(Λ/3) playing the role of a₀.
- Giné's interpolation function a/|a + a_e| has a_e ≈ a₀ for local objects. Expanded for a ≫ a₀ and with m_i = m_g, it gives a constant extra Sunward acceleration a₀.
- Giné argues from his earlier work (2009, 2011a) that a₀ ~ cH₀. This reproduces McCulloch's equation a = GM☉/r² + 0.99 cH₀.
- A constant a₀ "is dramatically inconsistent with the motion of the inner planets". The paper cites Sanders (2006): Mercury's precession limits any extra constant acceleration to more than 10× below a₀. So MOND-like effects would have to act differently for bound orbits.
- Giné argues that the result "reinforces" the idea that the Pioneer anomaly is Earth-directed, variable and environment-dependent.

## Key equations
Milgrom's modified inertia and Giné's (2009) interpolation:
$$ m_i\,\mu(a/a_0)\,\mathbf{a} = \mathbf{F}, \qquad \frac{a}{a + a_0}\, m_i \mathbf{a} = \mathbf{F} $$
Giné (2010) form, with a_e = a₀(1 − R_obs/R_U) R̂_U:
$$ \frac{|\mathbf{a}|}{|\mathbf{a} + \mathbf{a}_e|}\, m_i \mathbf{a} = \mathbf{F} $$
Verlinde entropic relations:
$$ \Delta S = 2\pi k_B \frac{mc}{\hbar}\Delta x, \quad F\Delta x = T\Delta S, \quad T = \frac{1}{2\pi}\frac{\hbar a}{k_B c}, \quad N = \frac{4\pi R^2 c^3}{G\hbar} $$
Funkhouser's de Sitter second law, with k = √(Λ/3):
$$ m\left[(a^2 + k^2)^{1/2} - k\right] = F $$
Resulting Pioneer acceleration (matching McCulloch 2007):
$$ a = \frac{GM_\odot}{r^2} + a_0, \qquad a = \frac{GM_\odot}{r^2} + \tfrac12\beta\pi^2 cH_0 \sim \frac{GM_\odot}{r^2} + 0.99\, cH_0 $$

## Data used
- No new data. The paper uses the Pioneer value 8.74 ± 1.33 × 10⁻¹⁰ m s⁻² (Anderson et al. 1998, 2002) and H₀ = 2.3 ± 0.9 × 10⁻¹⁸ s⁻¹.

## Results & predictions
- a₀ = 6.9 ± 3.5 × 10⁻¹⁰ m s⁻², stated to agree with the observed anomaly. This is the same number as McCulloch (2007), and about six times the MOND a₀ of 1.2 × 10⁻¹⁰ m s⁻².
- The paper makes no new quantitative prediction. It says the interpolation function that separates bound (planetary) from unbound (Pioneer) orbits "is still open to find".

## Figures
No figures in this paper.

## Notable quotes
> "The modified-inertia approaches to solve the Pioneer anomaly have been also considered under Unruh radiation by McCulloch, see McCulloch (2007). This proposal acquires its meaning in the wake of the holographic scenario established in the work of Verlinde" (p. 3)

> "However, the constant acceleration a0 is also present in the inner solar system where it is dramatically inconsistent with the motion of the inner planets" (p. 3)

## Criticisms & responses
- **Inner Solar System.** The paper itself concedes that a constant a₀ conflicts with the motions of the inner planets (Mercury, Icarus) by one to two orders of magnitude.
- **Thermal explanation.** Turyshev et al. (2012) attributed the Pioneer anomaly to thermal recoil; see [2012-turyshev-pioneer-thermal](../../03-criticism/2012-turyshev-pioneer-thermal/README.md). Their 2010 review, cited in this paper, had already noted that the a_P ≃ cH₀ match is approximate and probably coincidental; see [2010-turyshev-pioneer-review](../2010-turyshev-pioneer-review/README.md).
- No published reply aimed at this paper was found in a brief search.

## Related
- Evidence: [pioneer-anomaly](../../02-evidence/pioneer-anomaly.md), [derivation](../../02-evidence/derivation.md)
- Sources:
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
  - [2012-gine-holographic-modified-inertia](../2012-gine-holographic-modified-inertia/README.md)
  - [2012-gine-cosmological-holographic](../2012-gine-cosmological-holographic/README.md)
  - [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md)
  - [2017-gine-inertial-mass-holographic](../2017-gine-inertial-mass-holographic/README.md)
  - [2010-turyshev-pioneer-review](../2010-turyshev-pioneer-review/README.md)
