---
title: "Approaching the Dark Sector through a bounding curvature criterion"
authors: [Xavier Hernandez, Roberto A. Sussman, Luis Nasser]
year: 2019
type: paper
venue: "Monthly Notices of the Royal Astronomical Society 483(1):147"
doi: 10.1093/mnras/sty3073
arxiv: 1705.06356
url: "https://arxiv.org/abs/1705.06356"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, figures/fig-1-bounding-curvature-schematic.png, figures/fig-2-expansion-history.png]
status: neutral
tags: [mond, curvature, cosmology]
---

# Approaching the Dark Sector through a bounding curvature criterion

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1705.06356](https://arxiv.org/abs/1705.06356) · [doi:10.1093/mnras/sty3073](https://doi.org/10.1093/mnras/sty3073).

**Citation:** Hernandez, X., Sussman, R. A. & Nasser, L. (2019). *Approaching the Dark Sector through a bounding curvature criterion*. Monthly Notices of the Royal Astronomical Society, 483(1), 147. https://doi.org/10.1093/mnras/sty3073. arXiv:[1705.06356](https://arxiv.org/abs/1705.06356). The stored PDF is arXiv v3 of 8 November 2018.

**TL;DR:** For a Schwarzschild metric, the Kretschmann scalar times r⁴/M takes the same value for every mass at the MOND transition radius R_c ∝ (GM/a₀)¹ᐟ². The authors call this "bounding curvature", κ_B = 28Ga₀/c⁴. Holding κ_B fixed beyond R_c reproduces the metric of an isothermal dark-matter halo. Imposing it on a flat FLRW universe gives an asymptotically de Sitter expansion history within 5% of ΛCDM for 1/2 < a < 1. McCulloch appears only in one sentence, as a "relative exception" whose vacuum / cosmological-constant route to R_c the authors call "unsatisfactory" for their purposes.

## Key claims
- Gravitational anomalies appear "always (and only)" below a₀ = 1.2 × 10⁻¹⁰ m/s², at R_c = α(GM/a₀)¹ᐟ².
- κ_B = K r⁴/M evaluated at R_c is mass-independent. It falls as r⁻² inside R_c and stays constant beyond it, consistent with isothermal-halo metric potentials and with no dark matter required.
- Consistency requires α = (48/28)¹ᐟ² = 2(3/7)¹ᐟ² = 1.309.
- The same condition on flat FLRW gives late-time cosmic acceleration with no dark energy, with one free parameter γ = 0.2935.
- The claim that MOND's acceleration scale is incompatible with covariant frameworks is "in fact not present", because κ_B is a covariant geometric invariant.
- On McCulloch: "Relative exceptions are the recent works of McCulloch (2017) and Verlinde (2016) where however, it is the effect of a cosmological constant resulting from a quantum vacuum which leads to R_c … explaining galactic dark matter as a result of cosmological dark energy appears unsatisfactory." (The reference cited is McCulloch 2017, Ap&SS 362, 57.)

## Key equations
$$ R_c = \alpha R_M = \alpha\left(\frac{GM}{a_0}\right)^{1/2} $$
$$ K_S = 48\frac{G^2M^2}{c^4 r^6}, \qquad K_S\,r^4/M\big|_{r=R_c} = 48\frac{Ga_0}{\alpha^2 c^4} $$
Isothermal-halo potentials $A \simeq (r/R_M)^{2\beta^2}$ and $B = 1+2\beta^2$, with $\beta = V_{TF}/c$, give:
$$ K_{SSS} = 28\left(\frac{\beta}{r}\right)^4 + O(\beta^6/r^4), \qquad \kappa_B = 28\frac{Ga_0}{c^4}, \qquad \alpha = \left(\frac{48}{28}\right)^{1/2} = 1.309 $$
Flat FLRW:
$$ K_F = \frac{12}{c^4}\left[(\dot H + H^2)^2 + H^4\right], \qquad \left(\frac{\dot H}{H^2} + 1\right)^2 + 1 = \frac{8\times10^{-3}}{\gamma^4} $$
$$ \frac{H}{H_0} = \left[1 + X^{\pm}(T - T_0)\right]^{-1} $$

## Data used
- No new data. The paper uses the empirical relation cH₇₀ = 5.83a₀ (Milgrom 2002), a baryonic density of 0.04ρ_c, and a ΛCDM comparison with Ω_M = 0.3 and Ω_Λ = 0.7.

## Results & predictions
- κ_B = 28Ga₀/c⁴, which has units of kg⁻¹. α = 1.309, so R_c = 2(3/7)¹ᐟ² (GM/a₀)¹ᐟ².
- Corrections to the halo result are of order β², at most about 10⁻⁶ (V_TF ≲ 300 km/s).
- With γ = 0.2935, the H/H₀ history agrees with ΛCDM to within 5% for 1/2 < a < 1 (z < 1). It tends asymptotically to de Sitter.

## Figures
*Figure (local only): Fig. 1 — Schematic of κ ∝ M/r² inside the approximately Schwarzschild region of galaxies of different mass. Each reaches the same κ_B at its own R_c, and κ_B stays fixed beyond R_c. (Rendered page 3.)*

*Figure (local only): Fig. 2 — H/H₀ against scale factor: ΛCDM (upper curve on the right) compared with the analytic constant-bounding-curvature solution for flat FLRW (lower curve). (Rendered page 4.)*

## Notable quotes
> "the scalar curvature, K, multiplied by (r⁴/M) at the critical MOND transition radius, r = R_c, has an invariant value of κ_B = K(r⁴/M) = 28Ga₀/c⁴." (abstract, p. 1)

> "explaining galactic dark matter as a result of cosmological dark energy appears unsatisfactory." (p. 2)

> "a fixed minimum κ_B principle could constitute the basis of a covariant modified theory of gravity." (p. 5)

## Criticisms & responses
- > [!UNVERIFIED] A brief search found no published critique that addresses this paper specifically.
- Factual notes: the result is a phenomenological criterion, not a field theory. The cosmological part adds a fitted parameter γ and assumes a constant mass M within c/H₀. The galactic part assumes the isothermal-halo metric that is inferred under GR.
- Relevance to QI is indirect. The paper is a MOND/geometry approach that mentions McCulloch only in passing, and critically.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md), [cosmology](../../02-evidence/cosmology.md)
- Sources: [2017-mcculloch-dwarf-galaxies](../2017-mcculloch-dwarf-galaxies/README.md) (the McCulloch 2017, Ap&SS 362, 57 paper cited here), [2019-hernandez-gaia-wide-binaries](../2019-hernandez-gaia-wide-binaries/README.md), [2012-hernandez-wide-binaries](../2012-hernandez-wide-binaries/README.md), [2017-smolin-mond-quantum-gravity](../2017-smolin-mond-quantum-gravity/README.md), [2019-cadoni-long-range-qg](../2019-cadoni-long-range-qg/README.md), [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md)
