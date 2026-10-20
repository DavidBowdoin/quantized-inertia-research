---
title: "Cosmology: flatness, mass of the universe, CMB low-l power"
tags: [cosmology, cmb, flatness-problem, hubble-scale-casimir, holographic]
verdict: supported-by-author-only
---

# Cosmology

## The phenomenon and the data
- **Flatness.** The observable universe is close to the critical (flat) density. McCulloch quotes a visible mass of about 1.8 × 10^52±1 kg, from ~9 × 10²¹ stars of roughly solar mass. Funkhouser (2006) estimates 2.4 × 10⁵² kg ([2014-mcculloch-toy-cosmology](../01-papers/2014-mcculloch-toy-cosmology/README.md)).
- **CMB low-multipole deficit.** Planck 2013 reported a 5–10% deficit in power at low multipoles (l < 40), at 2.5–3σ significance (as cited in the toy-cosmology paper).
- **Galaxy-scale cosmology.** The Tully–Fisher zero point evolves at z ≈ 1–2.3 (Übler et al. 2017), and high-z discs are baryon-dominated (Genzel et al. 2017); see [galaxy-rotation](galaxy-rotation.md).

## Mainstream explanation(s)
- **Flatness:** inflation is the standard explanation. The toy-cosmology paper presents its own model as an alternative and says the reason for flatness is "not known".
- **Low-l CMB anomaly:** cosmic variance and other statistical explanations are standard in the literature. The repository has no source on this, and the README records no independent check of QI's claim against later Planck releases.
- **High-z kinematics:** within ΛCDM, the observers explain their high-z results by high gas fractions and pressure support.

## QI's prediction
- **Minimum mass of the universe.** [McCulloch 2010, EPL](../01-papers/2010-mcculloch-minimum-accelerations/README.md): applying the minimum acceleration to the observable universe gives M_dark = c²Θ/2G ≈ 2 × 10⁵³ kg, against a closure mass c²Θ/4G ≈ 1 × 10⁵³ kg. This is offered as a possible explanation of flatness.
- **Toy cosmology.** [McCulloch 2014, *Galaxies*](../01-papers/2014-mcculloch-toy-cosmology/README.md) treats the Hubble horizon as an inside-out black hole radiating inward. Only wavelengths that fit the Hubble scale are allowed, which gives

  $$ M_{eq} = \frac{\Theta c^2}{4\pi^2 G\beta} \sim \frac{c^3}{4GH} \approx 4.6 \pm 0.4\times10^{52}\ \mathrm{kg} $$

  - The predicted mass is compared with an observed 1.8 × 10^52±1 kg.
  - For the CMB, E′ = E(1 − 1/2L) gives a **5.5%** power drop for l < 40, compared with Planck's 5–10%.
  - Qualitative predictions: the universe's mass grows linearly with its diameter, and the universe was hotter in the past.
  - The paper calls itself an "incomplete toy model ... to stimulate discussion", and it corrects the 2007 paper (λ = 2Θ, not Θ).
- **Maximum black-hole mass.** [McCulloch 2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md) predicts M ≤ c³/(8π²GβH) ≈ 10⁵² kg, about 10²² M☉.
- **Redshift dependence of the galactic anomaly.** Θ_z = Θ_now/(1+z), so v⁴ = 2GMc²(1+z)/Θ_now ([2017-mcculloch-galaxy-rotations-sparc](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)). For the numbers, see [galaxy-rotation](galaxy-rotation.md).
- **Holographic connections by Giné.**
  - [2012-gine-holographic-modified-inertia](../01-papers/2012-gine-holographic-modified-inertia/README.md) (abstract only) claims a modified Friedmann equation from two holographic screens, giving inflation and late-time acceleration without dark energy, plus a MOND-like law.
  - [2012-gine-cosmological-holographic](../01-papers/2012-gine-cosmological-holographic/README.md) is not accessible, so its content is unverified.
  - [2024-gine-luciano-discretization-lambda](../01-papers/2024-gine-luciano-discretization-lambda/README.md) combine QI's Hubble-horizon damping of Unruh radiation with Planck-scale "resonant points" to get Λ = 2H₀²/c², against an observed 3Ω_Λ H₀²/c² ≈ 2.07 H₀²/c². Editorial check (in the README): ℓ_P cancels, so the content is the heuristic O(1) prefactor, and the horizon used is c/H₀, not Θ.
- **Universe as a resonant cavity.** [Pickering 2017](../01-papers/2017-pickering-resonant-cavity/README.md) treats the recombination plasma as a conducting cavity. That gives Θ = 3.4125 × Hubble length ≈ 4.3 × 10²⁶ m.
  - The README notes that the comoving distance to last scattering is considerably larger than c/H₀.
  - The paper also approximates the sphere by a cylinder.

## Independent tests, critiques and null results
- **Mass of the universe.** The "agreement" of 4.6 × 10⁵² kg with 1.8 × 10^52±1 kg rests on an observed value uncertain by a factor of 10. The prediction is about 2.5× the central estimate.
- **CMB.** No independent check of the CMB-suppression claim exists in the sources.
- **No full cosmological model.** No QI paper provides a full model: no H(z), no CMB power-spectrum fit, no structure formation. Smolin and Cadoni & Tuveri, in their own horizon-based approaches, explicitly say they do not address clusters, lensing or large-scale structure. QI papers do not address these either.
- **Underlying theory.** Renda 2019 shows that the Hubble-cavity Unruh calculation underlying QI does not give the linear F(a) assumed in McCulloch 2007 ([2019-renda-sceptical](../03-criticism/2019-renda-sceptical/README.md)). The toy cosmology applies the same wavelength-cutoff logic to Hawking radiation. It also assumes that Wien's law holds at Hubble scales, which the paper itself calls a "bold" assumption.
- **Hernandez et al. 2019** consider deriving galactic dark-matter effects from cosmological vacuum effects, as McCulloch does, "unsatisfactory" ([2018-hernandez-bounding-curvature](../01-papers/2018-hernandez-bounding-curvature/README.md)).
- **Varying Θ.** Θ has been 2.6, 2.7, 4.3 and 8.8 × 10²⁶ m in different papers, so cosmological numbers derived from it are not unique. Junghanns 2026 notes that 2c/H(t), the particle- and event-horizon diameters, Θ₀/(1+z) and a fixed Θ₀ give different a₀(t) histories ([2026-junghanns-causal-restriction-nogo](../03-criticism/2026-junghanns-causal-restriction-nogo/README.md)). McGaugh reports no Tully–Fisher evolution to z ≈ 2.5 ([2025-mcgaugh-kinematics-high-redshift](../07-media/2025-mcgaugh-kinematics-high-redshift/README.md)); see [galaxy-rotation](galaxy-rotation.md).

## Assessment
QI's cosmological claims are order-of-magnitude coincidences between horizon-scale quantities (c, H, Θ) and observed totals: the mass of the universe, closure density and the low-l CMB deficit. They come from a model its author calls an incomplete toy. The comparisons rely on very loose observational bounds (±1 in the exponent) or on a single number (5.5% vs 5–10%). No independent group has tested them, and QI has not produced the standard cosmological observables (expansion history, CMB spectrum, structure growth) that would allow a real comparison with ΛCDM.

## Sources
- [2007-mcculloch-pioneer-anomaly](../01-papers/2007-mcculloch-pioneer-anomaly/README.md)
- [2010-mcculloch-minimum-accelerations](../01-papers/2010-mcculloch-minimum-accelerations/README.md)
- [2014-mcculloch-toy-cosmology](../01-papers/2014-mcculloch-toy-cosmology/README.md)
- [2017-mcculloch-galaxy-rotations-sparc](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)
- [2017-pickering-resonant-cavity](../01-papers/2017-pickering-resonant-cavity/README.md)
- [2012-gine-holographic-modified-inertia](../01-papers/2012-gine-holographic-modified-inertia/README.md)
- [2012-gine-cosmological-holographic](../01-papers/2012-gine-cosmological-holographic/README.md)
- [2024-gine-luciano-discretization-lambda](../01-papers/2024-gine-luciano-discretization-lambda/README.md)
- [2026-junghanns-causal-restriction-nogo](../03-criticism/2026-junghanns-causal-restriction-nogo/README.md)
- [2025-mcgaugh-kinematics-high-redshift](../07-media/2025-mcgaugh-kinematics-high-redshift/README.md)
- [2017-smolin-mond-quantum-gravity](../01-papers/2017-smolin-mond-quantum-gravity/README.md)
- [2019-cadoni-long-range-qg](../01-papers/2019-cadoni-long-range-qg/README.md)
- [2018-hernandez-bounding-curvature](../01-papers/2018-hernandez-bounding-curvature/README.md)
- [2019-renda-sceptical](../03-criticism/2019-renda-sceptical/README.md)
- Related evidence: [cosmic-acceleration](cosmic-acceleration.md), [galaxy-rotation](galaxy-rotation.md), [derivation](derivation.md)
