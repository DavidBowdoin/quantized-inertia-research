---
title: "Modification of Inertia Resulting from a Hubble-Scale Casimir Effect Contradicts Classical Inertia"
authors: [Walter Dickmann, Johannes Dickmann]
year: 2023
type: critique
venue: "Kinematics and Physics of Celestial Bodies 39(6):356-359 (Ukrainian original: Kinematika i Fizika Nebesnykh Tel 39(6):80-86)"
doi: 10.3103/S0884591323060041
arxiv:
url: "https://doi.org/10.3103/S0884591323060041"
open_access: true
license: unknown
files: [paper.pdf, figures/fig-1-qi-schematic.png]
status: critical
tags: [theory, unruh, casimir, refutation, derivation, critique]
---

# Modification of Inertia Resulting from a Hubble-Scale Casimir Effect Contradicts Classical Inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`unknown`) does not permit redistribution. Read the paper at [doi:10.3103/S0884591323060041](https://doi.org/10.3103/S0884591323060041).

**Citation:** Dickmann, W. & Dickmann, J. (2023). *Modification of Inertia Resulting from a Hubble-Scale Casimir Effect Contradicts Classical Inertia*. Kinematics and Physics of Celestial Bodies, 39(6), 356–359. https://doi.org/10.3103/S0884591323060041. The Ukrainian-language original is Kinematika i Fizika Nebesnykh Tel 39(6), 80–86, https://doi.org/10.15407/kfnt2023.06.080. **The stored PDF is the freely available Ukrainian original** from the Main Astronomical Observatory of NAS Ukraine. The English translation is paywalled and was not stored. Page numbers below refer to the Ukrainian journal pagination (80–86).

**TL;DR:** A short communication (W. Dickmann, independent researcher; J. Dickmann, TU Braunschweig) that builds on [Renda 2019](../2019-renda-sceptical/README.md). It computes the Unruh energy density on both sides of an accelerating particle without the peak-wavelength-only simplification. On the cosmic-horizon side it integrates the continuous Planck spectrum. On the Rindler-horizon side it sums Renda's discrete cavity modes with cavity length L = c²/a. Both energy densities scale as a⁴, so the net radiation-pressure force from the QI mechanism is ∝ a⁴, not ∝ a. The authors conclude that this contradicts Newton's second law, which has been tested down to 10⁻¹³ m s⁻² (Gundlach et al. 2007). In their words, they "refute" QI as an explanation of inertia.

## Key claims
- QI/MiHsC attributes inertia to an asymmetric Casimir effect. A Rindler horizon forms at distance c²/a behind an accelerating particle. Unruh-radiation energy density is lower on that side than on the side facing the far more distant cosmic horizon (Fig. 1). Only Unruh radiation is considered in QI; other backgrounds such as the CMB are ignored (p. 82).
- Recap of Renda's two objections (p. 81). (1) At very small accelerations (a < 10⁻⁷ m s⁻² in their wording) Planck's law must be replaced by its constrained-cavity form, which produces Renda's unobserved stationary point near 10⁻⁹ m s⁻². (2) Collapsing the Unruh energy density onto the peak wavelength may be acceptable when only a few modes are allowed, but gives "extremely wrong" results at "classical" accelerations (a > 10⁻⁷ m s⁻²).
- **Main argument (pp. 83–84):**
  - On the cosmic side, λ_peak ≈ (1/a) × 7 × 10¹⁷ m² s⁻², which is much smaller than the Hubble radius. The continuous Planck integral therefore applies and gives U_right ∝ a⁴ (Eq. 4).
  - On the Rindler side, the cavity length is c²/a, which is of the same order as λ_peak. The discrete sum must be used (Eq. 5, following Renda). After substituting T_a, the remaining sum over p is a pure constant independent of a, so U_left ∝ a⁴ too (Eq. 6).
  - The net force, the surface integral of U/3 over the particle, is therefore ∝ a⁴ for any particle shape (Eqs. 7–8).
- **Diagnosis:** "The main flaw in the MiHsC derivations proposed by Giné and McCulloch [7, 13] is the calculation of the energy density U of Unruh radiation in only one mode, namely the peak wavelength." That simplification gives U ∝ a, whereas summing all allowed modes gives U ∝ a⁴ "for both bounded and unbounded systems" (p. 84).
- **Limits of the claim:** The authors say this "does not mean the general failure" of modelling inertia as an interaction with the quantum vacuum. They cite Haisch, Rueda & Puthoff (1994) and Rueda & Haisch (2005) as possibly more rigorous routes (p. 85).

## Key equations
Planck spectral energy density at the Unruh temperature (Eqs. 1–2; T_a written as ha/((2π)²ck), i.e. ħa/(2πck)):
$$ u_\lambda(\lambda, T_a) = \frac{8\pi h c}{\lambda^5}\,\frac{1}{\exp\!\left(\frac{hc}{\lambda k T_a}\right) - 1}, \qquad T_a = \frac{h a}{(2\pi)^2 c k} $$
Continuous integral on the cosmic-horizon side (Eq. 4):
$$ U_{\rm right} = \int_0^\infty u_\lambda(\lambda, T_a)\,d\lambda = \frac{h}{480\pi^3 c^7}\,a^4 $$
Discrete sum on the Rindler side, with L = c²/a (Eqs. 5–6):
$$ U_{\rm left} = \sum_{p^2=1}^{\infty} \frac{2N(p)\,hc}{L^3 \lambda_p}\,\frac{1}{\exp\!\left(\frac{hc}{\lambda_p k T_a}\right) - 1} = \frac{h}{c^7}\,a^4 \sum_{p^2=1}^{\infty} \frac{p\,N(p)}{\exp(2\pi^2 p) - 1} $$
Net QI force, with both surface integrals depending only on the particle's size and shape (Eq. 8):
$$ F_{QI} = \frac{1}{3}\frac{h}{c^7}\left( \sum_{p^2=1}^{\infty} \frac{pN(p)}{\exp(2\pi^2 p)-1} \iint_{\rm left} f(\theta,\varphi)\,\mathbf{e}_a\cdot d\mathbf{A} \;-\; \frac{1}{480\pi^3} \iint_{\rm right} \mathbf{e}_a\cdot d\mathbf{A} \right) a^4 $$

## Data used
- None. Analytic argument. The empirical anchor is Gundlach et al. (2007, PRL 98, 150801), a laboratory test of Newton's second law at accelerations down to about 10⁻¹³ m s⁻², which the authors cite for F ∝ a.

## Results & predictions
- The QI radiation-pressure mechanism, evaluated over all modes, yields F ∝ a⁴ for classical accelerations (a > 10⁻⁷ m s⁻²), "not a, but a⁴", which "directly contradicts Newton's second law" (p. 84).
- Conclusion: MiHsC is "inadequate" for describing inertia (p. 85).
- No numerical evaluation of the mode sum is given. The authors state that it is a constant and that it is not needed for the argument.

## Figures
*Figure (local only): Fig. 1 — Schematic of quantised inertia as described by the authors: a particle accelerating with proper acceleration a sees Unruh radiation and a Rindler horizon at c²/a on the opposite side; inertia is attributed to the excess of fluctuations towards the far more distant cosmic horizon. (Rendered page 3 of the Ukrainian PDF, journal p. 82.)*

## Notable quotes
Translated from the Ukrainian original (this translation is for this archive, not the official English text):
> "In this work, we refute the explanation of inertia by the concept of … (MiHsC), or quantised inertia (QI)." (p. 80; this matches the English abstract)

> "Thus, expression (8) shows that the net force acting on the particle obtained from the QI approach is proportional not to a, but to a⁴. This directly contradicts Newton's second law." (p. 84)

## Criticisms & responses
- **McCulloch response:** none found. Searches of physicsfromtheedge.blogspot.com for "Dickmann" returned no posts discussing this paper (checked Oct 2026). His general reply to the peak-wavelength objection (see [Renda 2019](../2019-renda-sceptical/README.md)) is that QI's formula has since been re-derived from the uncertainty principle and from information erasure at horizons ([blog, 30 Aug 2026](https://physicsfromtheedge.blogspot.com/2026/08/responding-to-criticisms.html)). Those derivations do not use the Unruh-spectrum pressure calculation that Dickmann & Dickmann analyse.
  > [!UNVERIFIED] Whether any author has published a reply to this paper; none was found via Crossref or arXiv searches.
- **Points a reader may want to check (editorial, not from the source):** The sum in Eq. 6 is treated as acceleration-independent because L = c²/a scales the mode wavelengths together with T_a. The paper also does not address the cosmic-horizon cut-off (the "Hubble-scale" part of MiHsC) on the right-hand side. It treats that side as an unbounded continuum.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources critiqued: [2013-mcculloch-asymmetric-casimir](../../01-papers/2013-mcculloch-asymmetric-casimir/README.md), [2016-gine-unruh-temperatures](../../01-papers/2016-gine-unruh-temperatures/README.md), [2007-mcculloch-pioneer-anomaly](../../01-papers/2007-mcculloch-pioneer-anomaly/README.md), [2012-mcculloch-galactic-scales](../../01-papers/2012-mcculloch-galactic-scales/README.md)
- Builds on: [2019-renda-sceptical](../2019-renda-sceptical/README.md)
- Alternative QI derivations: [2020-mcculloch-information-theory](../../01-papers/2020-mcculloch-information-theory/README.md), [2018-gine-casimir-uncertainty](../../01-papers/2018-gine-casimir-uncertainty/README.md), [2021-gine-luciano-inertia-fluctuations](../../01-papers/2021-gine-luciano-inertia-fluctuations/README.md)
