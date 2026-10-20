---
title: "Casimir effect and the uncertainty principle"
authors: [Jaume Giné]
year: 2018
type: paper
venue: "Modern Physics Letters A 33(24):1850140"
doi: 10.1142/S0217732318501407
arxiv:
url: "https://doi.org/10.1142/S0217732318501407"
open_access: false
license: all-rights-reserved
files: [paper.pdf, citation.bib, figures/fig-1-shielded-volume.png]
status: neutral
tags: [casimir, uncertainty-principle]
---

# Casimir effect and the uncertainty principle

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.1142/S0217732318501407](https://doi.org/10.1142/S0217732318501407).

**Citation:** Giné, J. (2018). *Casimir effect and the uncertainty principle*. Modern Physics Letters A, 33(24), 1850140 (8 pp.). Received 11 Apr 2018, accepted 26 Jun 2018, published 23 Jul 2018 (dates as printed on the PDF). https://doi.org/10.1142/S0217732318501407

**About the stored PDF:** `paper.pdf` is the published World Scientific version (owner-supplied, local only; copyrighted). Article pages 1850140-1 to -8 are PDF pp. 1–8. Page references below use the printed article page numbers.

**Authorship:** sole author Jaume Giné (Lleida, Inspires Research Centre), confirmed on the PDF. Giné is a frequent McCulloch co-author. The paper does not mention QI or MiHsC; McCulloch 2013 is cited only among works on vacuum energy and cosmic acceleration (p. 1850140-2).

**TL;DR:** The companion to Giné's EPL paper on the Hawking and Unruh temperatures. Section 2 gets the oscillator zero-point energy ħω/2 from the uncertainty principle. Section 3 reproduces the textbook Casimir result, ΔE = −π²ħcA/(720d³) and F = −π²ħcA/(240d⁴), by the usual mode sum with Euler–Maclaurin regularisation. Section 4, the new part, tries to get the Casimir energy from AΔxΔE = ħc/2. It treats Δx as the volume from which virtual photons can reach a point on a plate, cut off at an unknown "effective radius" r_e. The result, ΔE = 3ħcA/(4πr_e³), matches the standard coefficient only if r_e is fitted: r_e³ = 540d³/π³, so r_e ≈ 2.6d. The coefficient is fitted, not derived, consistent with the abstract's "we try".

## Key claims
- The zero-point energy E₀ = ħω/2 of each field oscillator follows from minimising the oscillator energy subject to ΔxΔp ≥ ħ/2 (Sec. 2).
- The standard Casimir energy and force are re-derived by the mode sum for ideal plates (Sec. 3).
- In the uncertainty-principle approach (Sec. 4), a virtual photon reaching a point p₀ on one plate can come from all space except the region shadowed by the second plate. Δx is taken as the unshielded volume V_T − V_c, which in the limit L ≫ d is ≈ (2/3)πR³ (p. 1850140-6).
- Because the probability that a photon reaches p₀ falls with distance, the volume is cut off at a finite effective radius r_e > d, giving ΔE = 3ħcA/(4πr_e³). "The computation of this effective radius r_e would give the correct expression of the uncertainty of the energy" (p. 1850140-6).
- Comparing with the standard result gives r_e ≈ 2.6d. The paper gives the first finite-plate correction to V_c as a Taylor series in d/√A (p. 1850140-7).
- Increasing d lowers the shielded volume, raises Δx and lowers ΔE, so the force falls "as expected". The paper adds that "the dependence of the Casimir force on d is more involved and future experimental tests should confirm this dependence on d" (p. 1850140-7).

## Key equations
Transcribed from the PDF. Equations in Sec. 4 are unnumbered in the paper.

Zero-point energy from the HUP (Eqs. 1–6):
$$ \Delta x\,\Delta p \ge \frac{\hbar}{2} \;\;(1), \qquad \Delta E = \frac{\hbar^2}{8m(\Delta x)^2} + \frac12 m\omega^2(\Delta x)^2 \;\;(4), \qquad E_0 = \frac{\hbar\omega}{2} \;\;(6) $$

Standard Casimir derivation (Eqs. 14, 16, 17):
$$ \Delta E_{1D} = -\frac{\hbar c\pi}{12d} \;\;(14), \qquad \Delta E = -\frac{\pi^2\hbar cL^2}{720d^3} = -\frac{\pi^2\hbar cA}{720d^3} \;\;(16), \qquad F = -\frac{\partial\Delta E}{\partial L} = -\frac{\pi^2\hbar cA}{240d^4} \;\;(17) $$

Uncertainty-principle route (Eq. 18 and Sec. 4, pp. 1850140-5 to -7), with k = L/(2d) = tan α:
$$ \Delta x\,\Delta E \ge \frac{\hbar c}{2} \;\;(18), \qquad V_c = \frac13\pi\left[2\left(1 - \frac{1}{\sqrt{1+k^2}}\right)R^3 - d^3k^2\right] $$
$$ \Delta x = V_T - V_c \approx \frac23\pi R^3 \;\to\; \frac23\pi r_e^3, \qquad \Delta E = \frac{3\hbar cA}{4\pi r_e^3}, \qquad r_e^3 = \frac{540\,d^3}{\pi^3} \;\Rightarrow\; r_e \approx 2.6\,d $$

Editorial checks:
- Setting 3/(4πr_e³) = π²/(720d³) gives r_e³ = 540d³/π³ ✓, and r_e = 2.59d ✓.
- Eq. 17 is printed as −∂ΔE/∂L. The derivative giving −π²ħcA/(240d⁴) from Eq. 16 is with respect to the separation d, so "∂L" is a typo ✓.
- Dimensions: the text sets Δx equal to a volume, (2/3)πr_e³, and then substitutes into "AΔxΔE = ħc/2". Read literally, that gives ΔE = 3ħc/(4πAr_e³), which is not an energy. The printed ΔE = 3ħcA/(4πr_e³) follows instead from (V/A)·ΔE = ħc/2, i.e. using the length volume ÷ area. The step from the stated relation to the printed ΔE is therefore not consistent as written.
- The printed text also says the curves intersect at x² + y² = R; it should be R².

## Data used
- None (theoretical). The paper cites Lamoreaux (1997) as experimental confirmation of the Casimir force.

## Results & predictions
- Sec. 3 reproduces the standard ideal-plate result, which is not new.
- Sec. 4 does **not** derive the Casimir coefficient. It gives ΔE ∝ ħcA/r_e³, with r_e fitted to the standard result (r_e ≈ 2.6d), and says computing r_e from first principles is future work. Once r_e ∝ d is assumed, the d⁻³ energy scaling follows, but the proportionality itself comes from the fit.
- No testable prediction is given. The closing remark that the d-dependence is "more involved" is not quantified.

## Figures
*Figure (local only): Fig. 1: Geometry of the uncertainty-principle argument: the point p₀ on one plate, the second plate (side L) at distance d subtending angle α, and the shaded volume V_c inside radius R from which photons are shielded from p₀. (PDF p. 6.)*

## Notable quotes
> "In this work, we try to deduce the Casimir effect directly from the uncertainty principle." (p. 1850140-1, abstract)

> "The computation of this effective radius r_e would give the correct expression of the uncertainty of the energy." (p. 1850140-6)

> "After this analysis through the uncertainty principle, the dependence of the Casimir force on d is more involved and future experimental tests should confirm this dependence on d." (p. 1850140-7)

## Criticisms & responses
- No published critique that addresses this paper specifically was found in a brief search.
- Editorial notes:
  - The new result has one free parameter, r_e, fixed by matching the known answer. That makes Sec. 4 a reparameterisation rather than a derivation.
  - The dimensional step noted above is inconsistent.
  - The paper also mentions (p. 1850140-2) Jaffe's (2005) point that Casimir forces can be computed without reference to vacuum fluctuations. That point matters for QI's reliance on a Casimir analogy, but the paper does not pursue it.
- **QI context:** QI describes inertia as a "Rindler-scale" and "Hubble-scale" Casimir effect. [Dickmann et al. 2023](../../03-criticism/2023-dickmann-casimir-contradicts/README.md) argue that QI's use of the Casimir effect contradicts standard Casimir physics. That critique concerns QI, not this paper directly.
- [Giné & Luciano (2021)](../2021-gine-luciano-inertia-fluctuations/README.md) take up the same HUP-plus-effective-cutoff idea (integrating ΔE ≃ ħc/2Δx out to an effective radius r_e). Their footnote 3 explains why the plate Casimir force is weak while a "Rindler-scale" one would give macroscopic inertia.
- This archive's [Renda (2019)](../../03-criticism/2019-renda-sceptical/README.md) entry groups this paper with the alternative derivations that do not use the discrete Unruh-spectrum sum Renda criticised. That is our grouping, not Renda's. This paper does not address inertia at all, and no published assessment of whether these derivations answer Renda was found.
- [McCulloch & Giné 2020](../2020-mcculloch-horizon-widths/README.md) cite this paper alongside the Hawking/Unruh paper as support for the horizon-width approach.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources:
  - [2018-gine-hawking-unruh-uncertainty](../2018-gine-hawking-unruh-uncertainty/README.md) (the companion paper, Ref. 5)
  - [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md) (Ref. 14)
  - [2017-gine-inertial-mass-holographic](../2017-gine-inertial-mass-holographic/README.md) (Ref. 4)
  - [2012-gine-holographic-modified-inertia](../2012-gine-holographic-modified-inertia/README.md) (Ref. 3)
  - [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md)
  - [2021-gine-luciano-inertia-fluctuations](../2021-gine-luciano-inertia-fluctuations/README.md)
  - [2022-mcculloch-qi-thrust-casimir](../2022-mcculloch-qi-thrust-casimir/README.md)
  - [2023-dickmann-casimir-contradicts](../../03-criticism/2023-dickmann-casimir-contradicts/README.md)
