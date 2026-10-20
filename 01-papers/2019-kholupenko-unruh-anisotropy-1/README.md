---
title: "On the Possible Anisotropy of the Unruh Radiation. Part I: Massless Scalar Field in (1+1)D Space-Time"
authors: [E. E. Kholupenko]
year: 2019
type: paper
venue: "Gravitation and Cosmology 25(3):213-225"
doi: 10.1134/S0202289319030071
arxiv:
url: "https://doi.org/10.1134/S0202289319030071"
open_access: false
license: all-rights-reserved
files: [paper.pdf, citation.bib, figures/fig-1-delayed-trajectories.png, figures/fig-2-weight-function.png]
status: neutral
tags: [unruh, anisotropy, theory-basis]
---

# On the Possible Anisotropy of the Unruh Radiation. Part I: Massless Scalar Field in (1+1)D Space-Time

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.1134/S0202289319030071](https://doi.org/10.1134/S0202289319030071).

**Citation:** Kholupenko, E. E. (2019). *On the Possible Anisotropy of the Unruh Radiation. Part I: Massless Scalar Field in (1+1)D Space-Time*. Gravitation and Cosmology, 25(3), 213–225. https://doi.org/10.1134/S0202289319030071

**TL;DR:** The paper re-derives the Unruh effect for a massless scalar field in (1+1)D and argues that the standard Bogoliubov-coefficient integral hides an ambiguity in the order of limits. Two physical assumptions remove the ambiguity: a finite integration region, or a Rindler metric that spreads out at the speed of light from when acceleration begins. With either one, the Rindler particles that come from the backward hemisphere (the side of the Rindler horizon) vanish. The Rindler particles from the forward hemisphere keep the usual Planck occupation at the Unruh temperature. The paper concludes that Unruh radiation is anisotropic and not thermal, and that an accelerated body would feel an extra "deceleration force", scaling as a² in (1+1)D (a⁴ expected in (3+1)D). The paper cites Giné & McCulloch (2016) once. It notes their claim that Casimir-type effects make Unruh radiation anisotropic, calls their argument in need of "very careful consideration", and says its own anisotropy is "of different origin". It does not discuss QI or MiHsC beyond that.

> **Stored version:** the published Pleiades journal PDF (13 pages, journal pp. 213–225; "© Pleiades Publishing, Ltd., 2019"; received and revised 14 Mar 2019, accepted 30 Apr 2019). Journal page = PDF page + 212. Owner-supplied copy, kept locally only. It is described as a fuller version of the short report Kholupenko (2018), EPJ Web of Conferences 191, 07006 (p. 214).

## Key claims
- Earlier work disagrees on whether Unruh radiation is isotropic: Gerlach and Grove & Ottewill found it isotropic, while Hinton et al., Israel & Nester and Sanchez found anisotropy. Most of the anisotropic results come from directional detector models (pp. 213–214). The paper says the "currently prevailing common opinion" is that Unruh radiation is isotropic (p. 214).
- The paper says its anisotropy is not a detector effect but a property of the field's distribution function. It considers no detector model (p. 214).
- **Mathematical point (§4.3.1, pp. 217–218).** The Bogoliubov coefficient β_κk is an improper integral over ρ, and the stationary result needs τ → ∞ as well. For quanta from the forward hemisphere (k < 0), the two limits commute and give the standard Unruh value. For quanta from the backward hemisphere (k > 0), they do not commute: taking ρ₁ → ∞ first gives β^Unruh, while taking τ → ∞ first gives 0 (Eqs. 34–36). The coefficient is zero for any cutoff ρ₁ that grows more slowly than exp(aτ/c).
- **Physical point (§4.3.2, pp. 218–222).** An accelerated reference frame can be physically realised only by bodies, or a bar, whose parts start moving with a light-speed delay (Eqs. 37–40, Figs. 1–2). Equivalently, a real gravitational field that switches on at t = 0 spreads out at c (Eq. 41). In both cases the Rindler metric covers space at a finite speed, so the KFG inner product (Eq. 11) should be integrated over a finite region, not the whole of space.
- **Interpretation (§4.3.3, pp. 222–223).** In a finite Rindler region, Minkowski modes with k > 0 freeze because of the Doppler factor exp(−aτ/c). They contribute only at ρ ~ ρ₀ exp(aτ/c), which corresponds to Minkowski distances far beyond the observable Universe. Modes with k < 0 need only finite regions (x ≈ ρ₀/2).
- **Consequences (§5, p. 224).** Unruh radiation, and by analogy Hawking radiation, is not equilibrium radiation. Black holes "should not be treated as thermodynamic objects", and their evaporation times should be re-estimated. Accelerated bodies would feel a deceleration force and would make the vacuum radiate.

## Key equations
Standard Unruh temperature (Eq. 1, p. 213), and the Rindler metric with observer and horizon positions (Eq. 2 and p. 215):
$$ T = \frac{\hbar a}{2\pi c k_B}, \qquad ds^2 = \left(\frac{a\rho}{c}\right)^2 d\tau^2 - d\rho^2,\quad \rho_0 = c^2/a,\ \rho_{RH}=0 $$
Mean number of Rindler particles in the Minkowski vacuum (Eq. 20, p. 216), and the paper's corrected result from integrating over a finite region R ≫ max{ρ₀, 2π/k, 2π/κ} (Eqs. 52–53, p. 224):
$$ \langle 0_M|\hat N^R_\kappa|0_M\rangle = 2\!\int |\beta_{\kappa k}|^2 dk \ \longrightarrow\ \begin{cases} 2\left[\exp\!\left(\dfrac{2\pi c^2|\kappa|}{a}\right)-1\right]^{-1}, & \kappa<0 \\ 0, & \kappa>0 \end{cases} $$
Editorial check: with ω = c|κ|, the exponent 2πc²|κ|/a equals ħω/(k_B T) for the T of Eq. (1). So the κ < 0 branch is the ordinary Unruh Planck spectrum, and only the κ > 0 branch is removed. The paper's convention is that k, κ < 0 are quanta "coming from the forward hemisphere" and k, κ > 0 are quanta "coming from the backward hemisphere" (p. 218).

Delayed reference-bar trajectories (Eqs. 37–38, p. 220), and the field of a plane mass that switches on at t = 0 (Eq. 41, p. 221):
$$ x = f_D + \left[(\rho-f_D)^2 + (ct-f_D)^2\right]^{1/2}\ (ct\ge|\rho-\rho_0|),\quad f_D=\gamma^{-1}|\rho-\rho_0|; \qquad g_{00} = (1+[\rho-ct]/\rho_0)^2\ \ \text{for}\ \rho/c\le t\le(\rho+\rho_0)/c $$

## Data used
- None. This is a theoretical paper on a (1+1)D massless scalar field. There is one numerical illustration: a body accelerating at 1 g for 20 years of proper time.

## Results & predictions
- **Anisotropy.** Thermal Rindler quanta from the forward hemisphere only, and none from the backward (horizon) hemisphere (Eq. 53). The paper calls this "significantly anisotropic" (p. 225) and non-thermal in the equilibrium sense (p. 224).
- **Worked scales (pp. 222–223).** For 1 g over 20 years of proper time (about 2.4 × 10⁸ years of Minkowski time), ρ₀ ≈ 1 light-year. Quanta from behind need ρ₁ ≈ 5 × 10⁸ ly in Rindler coordinates, which is x₁ ≈ 1.2 × 10¹⁷ ly in Minkowski space, "about 10⁷ times larger than the size of the observed Universe" (Eqs. 48–49). Quanta from ahead need only ρ₁ ≈ 2 × 10⁻⁹ ly, or x₁ ≈ ρ₀/2 ≈ 0.5 ly (Eqs. 50–51).
  - Editorial check: these numbers follow from aτ/c ≈ 20. With a = 9.8 m s⁻² and τ = 20 yr exactly, aτ/c ≈ 20.6, which makes ρ₁ about 1.8 times and x₁ about 3.4 times larger. The order-of-magnitude argument is unchanged.
- **Dynamical consequence (p. 224).** An extra "deceleration force" equal to the sum, over particle species, of the Unruh spectrum convolved with the body's interaction cross-sections. It is proportional to a² in (1+1)D, and the paper expects a⁴ in (3+1)D. No numerical estimate is given.
- The (3+1)D massless and massive cases are deferred to Part II (p. 214, footnote 2). See [Part II](../2022-kholupenko-unruh-anisotropy-2/README.md).

## Figures
*Figure (local only): Fig. 1: Trajectories of reference bodies (points of a reference bar). Dashed curves are uniformly accelerated (Rindler) observers or points of a perfectly rigid bar. Solid curves are bodies whose acceleration is delayed by light-speed propagation (Eq. 37). The dash-dotted line is the Rindler horizon, and dotted lines show the propagation of the interaction. Axes are x in units of ρ₀ and t in units of c/a. (PDF p. 8.)*

*Figure (local only): Fig. 2: The weight function W(x) that interpolates between the Minkowski metric (W = 0) and the Rindler metric (W = 1), plotted for t = 1 to 10 in units of c/a. The Rindler region spreads outwards at finite speed; at fixed ρ, 1 − W ~ t⁻³. (PDF p. 9.)*

## Notable quotes
> "Some recent investigations (see [23] and references therein) argued that the Unruh radiation may be anisotropic due to the Casimir effect because of the finite distance from the observer to the Rindler horizon. But this demands a very careful consideration" (p. 214; [23] = Giné & McCulloch 2016)

> "This anisotropy is of different origin than that considered in [16, 17, 19, 20, 23], and, in this sense, it is a new physical effect." (p. 214)

> "the Unruh radiation is not a thermal (equilibrium) radiation." (p. 224)

## Criticisms & responses
- **What the paper says about QI/MiHsC.** The paper never uses the terms "quantised inertia" or "MiHsC". Its only engagement is reference [23], Giné & McCulloch, *Mod. Phys. Lett. A* 31, 1650107 (2016), on p. 214. It summarises their claim as Unruh radiation being anisotropic "due to the Casimir effect because of the finite distance from the observer to the Rindler horizon". It then raises an objection: Rindler time dilation gives "an infinite number of oscillations of the quantization modes between the observer and the Rindler horizon", so the allowed wave vectors "represent a continuous spectrum". That undercuts a discrete Casimir-type cutoff set by the horizon distance. The paper explicitly does not aim to judge the earlier work (footnote 3, p. 214).
- **Bearing on QI's directional-Unruh assumption (editorial reading).** The paper is **neutral**, with partial qualitative compatibility:
  - *Compatible in sign.* QI assumes the Rindler horizon behind an accelerating body suppresses the Unruh radiation coming from that side, leaving a net push from the front ([2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md)). Kholupenko's Eq. (53) also removes the backward-hemisphere (horizon-side) quanta and keeps the forward ones, and predicts a force that opposes the acceleration. This addresses the isotropy objection associated with Milgrom (1999), at least in principle.
  - *Different mechanism.* The suppression comes from finite light-speed spreading of the metric, or a finite integration volume. It does not come from a Casimir cutoff of wavelengths longer than the horizon distance. The paper casts doubt on the Giné–McCulloch Casimir argument.
  - *Different physics.* The force is an *additional* drag, scaling as a² (or a⁴ in 3+1D), on top of ordinary inertia. It is not a derivation of inertial mass (which needs F ∝ a), and the paper has no cosmic-horizon term and no low-acceleration modification. So it neither derives nor tests QI's m_i(1 − 2c²/|a|Θ) formula.
- **Mainstream context.** The standard result is a thermal, isotropic bath for an eternally, uniformly accelerated observer (Unruh 1976; Crispino, Higuchi & Matsas 2008, both cited). The paper's conclusion rests on its argument about the order of limits and on its physical assumptions. It does not solve the time-dependent KFG problem ("We do not consider here such an exact time-dependent KFG equation because of a significant complexity", p. 218). The final result (Eq. 53) uses an approximate cutoff. A brief search found no published critique or reply addressing this paper specifically.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Context: [unruh-effect](../../05-context/unruh-effect.md)
- Sources: [2022-kholupenko-unruh-anisotropy-2](../2022-kholupenko-unruh-anisotropy-2/README.md), [2025-kholupenko-unruh-anisotropy-3](../2025-kholupenko-unruh-anisotropy-3/README.md), [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md) (the Giné & McCulloch paper cited as [23]), [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md), [2018-gine-hawking-unruh-uncertainty](../2018-gine-hawking-unruh-uncertainty/README.md), [2023-lynch-accelerated-electron-thermometer](../2023-lynch-accelerated-electron-thermometer/README.md)
