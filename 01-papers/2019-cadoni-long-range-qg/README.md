---
title: "Galactic dynamics and long-range quantum gravity"
authors: [Mariano Cadoni, Matteo Tuveri]
year: 2019
type: paper
venue: "Physical Review D 100:024029"
doi: 10.1103/PhysRevD.100.024029
arxiv: 1904.11835
url: "https://arxiv.org/abs/1904.11835"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf]
status: neutral
tags: [mond, de-sitter, radial-acceleration-relation]
---

# Galactic dynamics and long-range quantum gravity

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1904.11835](https://arxiv.org/abs/1904.11835) · [doi:10.1103/PhysRevD.100.024029](https://doi.org/10.1103/PhysRevD.100.024029).

**Citation:** Cadoni, M. & Tuveri, M. (2019). *Galactic dynamics and long-range quantum gravity*. Physical Review D, 100, 024029. https://doi.org/10.1103/PhysRevD.100.024029. arXiv:[1904.11835](https://arxiv.org/abs/1904.11835). The stored PDF is arXiv v2 of 6 May 2019.

**TL;DR:** The authors argue that baryonic matter breaks the scale symmetry of de Sitter spacetime and creates an IR scale r₀. It also creates a huge number of soft bosonic "dark energy" excitations, with wavelengths larger than the cosmological horizon, in thermal equilibrium at the de Sitter temperature. Their Bose–Einstein statistics produce an extra "dark force" acceleration that reproduces the McGaugh et al. radial-acceleration-relation (RAR) interpolating function. Using a proposed "generalized thermal equivalence principle" (GTEP), the authors also fix a₀ = H/2π. McCulloch's 2016 EPL paper is cited only once, in a list of works suggesting that MOND may express quantum gravity. The paper does not discuss QI further.

## Key claims
- Long-range quantum-gravity effects, not dark matter, could produce galactic-scale dynamics.
- The number of DE excitations follows a BE distribution at T_dS = ħ/2πL. Exponential suppression of hard modes explains why the effect appears only beyond r₀ ≃ √(Gm_B/a₀).
- The resulting a_DF matches the McGaugh–Lelli–Schombert RAR form up to a factor that the GTEP fixes at 1/2π.
- The result can be "uplifted" covariantly as GR sourced by an anisotropic fluid.
- The authors distinguish their approach from Smolin (2017), who attributes the effect to an environment-dependent change in the ratio m_i/m_g.
- Stated limitations: there is no quantum theory of the DE excitations or of dS quantum gravity, and lensing, structure formation and the Bullet Cluster are not addressed. The authors write that the approach "cannot represent a full alternative to dark matter and the ΛCDM model".

## Key equations
de Sitter temperature and static metric:
$$ T_{dS} = \frac{\hbar}{2\pi L}, \qquad f(r) = 1 - \frac{r^2}{L^2} - \frac{2Gm_B}{r} $$
Scaling-argument result (Eq. 22) and McGaugh RAR form (Eq. 23):
$$ a_{DF} = \frac{2\pi a_B}{e^{2\pi\sqrt{a_B/H}} - 1}, \qquad a_{DF} = \frac{a_B}{e^{\sqrt{a_B/a_0}} - 1} $$
(The paper says Eq. 22 matches Eq. 23 "up to a numerical factor, 1/(2π)".)
GTEP result (Eq. 36), which is identical to Eq. 23 with $a_0 = H/2\pi$:
$$ a_{DF} = \frac{a_B}{e^{\sqrt{2\pi a_B/H}} - 1} $$
Interpolating function: $F(x) = 1/(1 - e^{-\sqrt{x}})$ with $x = a_B/a_0$. Deep-MOND limit: $a_{DF} = \sqrt{a_B a_0}$.

## Data used
- No new data. The comparison is with the McGaugh, Lelli & Schombert (2016) RAR from SPARC: 2693 points in 153 galaxies, with a₀ ≈ 1.2 × 10⁻¹⁰ m/s², which the paper says is approximately H/2π.

## Results & predictions
- Reproduces the RAR functional form, with the proportionality a₀ = H/2π derived rather than fitted (via the GTEP).
- The paper makes no new quantitative observational predictions. It says lensing would be a key test.

## Figures
None (the paper contains no figures).

## Notable quotes
> "our result can be also derived as the weak field limit of Einstein's general relativity sourced by an anisotropic fluid." (abstract, p. 1)

> "the GTEP allows us to determine the value 1/2π for the proportionality factor between the MOND acceleration parameter a₀ and the cosmological acceleration H." (p. 16)

> "the long-range quantum gravity approach we have presented here cannot represent a full alternative to dark matter and the ΛCDM model." (p. 16)

## Criticisms & responses
- The authors list the main weaknesses themselves (see Key claims): no microscopic theory, an ad hoc GTEP, and no lensing or cosmology yet.
- > [!UNVERIFIED] A brief search found no specific published critique of this paper.
- Relevance to QI: the paper shares the theme that a horizon-scale (de Sitter / Hubble) effect sets a₀ ~ cH. QI is cited only in passing (ref. [47], McCulloch 2016 EPL), in footnote 2.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmology](../../02-evidence/cosmology.md)
- Sources: [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md) (the QI paper cited), [2017-smolin-mond-quantum-gravity](../2017-smolin-mond-quantum-gravity/README.md) (ref. [39], which the paper compares itself with), [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md), [2018-hernandez-bounding-curvature](../2018-hernandez-bounding-curvature/README.md), [2020-gine-luciano-eup-modified-inertia](../2020-gine-luciano-eup-modified-inertia/README.md)
