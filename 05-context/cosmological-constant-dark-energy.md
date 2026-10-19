---
title: "Cosmological constant and dark energy"
tags: [context, cosmology, dark-energy, vacuum-energy, cosmic-acceleration]
related: [dark-matter.md, mond.md, casimir-effect.md, hawking-radiation.md, holographic-principle.md]
---

# Cosmological constant and dark energy

## Plain-language explanation

In 1998–99 two supernova teams (Riess et al.; Perlmutter et al.) found that distant Type Ia supernovae are fainter than expected, implying the expansion of the universe is **accelerating**. The simplest explanation is Einstein's **cosmological constant** $\Lambda$, equivalent to a constant vacuum energy density with negative pressure ($w = p/\rho c^2 = -1$). "Dark energy" is the general name for whatever causes the acceleration. Combined with the CMB and BAO, the data give about 69% dark energy, 26% dark matter and 5% baryons today.

The **cosmological constant problem** (Weinberg 1989): naive quantum-field-theory estimates of vacuum energy exceed the observed value by roughly 60–120 orders of magnitude, depending on the cutoff. Why $\Lambda$ is so small but non-zero, and why it is comparable to the matter density today (the "coincidence problem"), are unsolved.

## Key equations

Friedmann equation with $\Lambda$:

$$
H^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}
$$

Acceleration equation:

$$
\frac{\ddot a}{a} = -\frac{4\pi G}{3}\left(\rho + \frac{3p}{c^2}\right) + \frac{\Lambda c^2}{3}
$$

Observed value: $\Lambda \approx 1.1\times10^{-52}\ \mathrm{m^{-2}}$, $\rho_\Lambda \approx 6\times10^{-27}\ \mathrm{kg\,m^{-3}}$. The characteristic acceleration $c^2\sqrt{\Lambda/3}\approx 5\times10^{-10}\ \mathrm{m\,s^{-2}}$ is of the same order as $cH_0$ and the MOND scale $a_0$ (see [mond.md](mond.md)).

## Mainstream status

Cosmic acceleration is established from several independent probes (SNe Ia, CMB, BAO, lensing). ΛCDM fits most data well. Open questions: the theoretical value of $\Lambda$; the **Hubble tension** between early- and late-universe $H_0$; and hints in DESI BAO data (2024–2025) that dark energy may evolve with time ($w\neq-1$), at roughly 2.8–4.2σ depending on the supernova sample combined. These hints are not yet conclusive.

## How it relates to QI

- **QI's claimed derivation of cosmic acceleration.** QI predicts a minimum acceleration $\sim 2c^2/\Theta$, which McCulloch identifies with the observed cosmic acceleration ([2010 minimum accelerations](../01-papers/2010-mcculloch-minimum-accelerations/README.md)), and a [toy cosmology](../01-papers/2014-mcculloch-toy-cosmology/README.md) that treats the Hubble volume as a black hole and claims to explain flatness. Giné discusses cosmological consequences in a holographic framework ([2012](../01-papers/2012-gine-cosmological-holographic/README.md)); Hernandez, Sussman & Nasser (2019) relate $a_0$ and dark energy via a curvature criterion ([source](../01-papers/2018-hernandez-bounding-curvature/README.md)).
- **What a replacement must reproduce.** Mainstream cosmology fits the full luminosity-distance curve $d_L(z)$, the CMB angular scale and the BAO ruler with one parameter $\Lambda$. A QI alternative would need to reproduce these quantitatively, not only the order of magnitude of the acceleration. Matching an acceleration of order $cH_0$ is not by itself strong evidence, because any acceleration built from $c$ and the Hubble scale lands there.
- **Vacuum energy.** QI, like the [Casimir effect](casimir-effect.md) and [SED](sed-inertia.md), invokes vacuum fields, but it does not address the cosmological constant problem of why vacuum energy gravitates so weakly.

## References

- Riess, A. G. et al. (1998). Observational evidence from supernovae for an accelerating universe and a cosmological constant. *AJ* 116, 1009. https://doi.org/10.1086/300499
- Perlmutter, S. et al. (1999). Measurements of Ω and Λ from 42 high-redshift supernovae. *ApJ* 517, 565. https://doi.org/10.1086/307221
- Weinberg, S. (1989). The cosmological constant problem. *Rev. Mod. Phys.* 61, 1. https://doi.org/10.1103/RevModPhys.61.1
- Carroll, S. M. (2001). The cosmological constant. *Living Rev. Relativ.* 4, 1. https://doi.org/10.12942/lrr-2001-1
- Planck Collaboration (2020). Planck 2018 results. VI. *A&A* 641, A6. https://doi.org/10.1051/0004-6361/201833910
- DESI Collaboration (2025). DESI 2024 VI: cosmological constraints from BAO. *JCAP* 02, 021. https://doi.org/10.1088/1475-7516/2025/02/021
- DESI Collaboration (2025). DESI DR2 Results II: BAO and cosmological constraints. arXiv:2503.14738. https://arxiv.org/abs/2503.14738
- Wikipedia: Cosmological constant problem. https://en.wikipedia.org/wiki/Cosmological_constant_problem
