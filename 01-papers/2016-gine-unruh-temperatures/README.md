---
title: Inertial mass from Unruh temperatures
authors: [Jaume Giné, Michael E. McCulloch]
year: 2016
type: paper
venue: "Modern Physics Letters A 31(17), 1650107"
doi: 10.1142/S0217732316501078
arxiv:
url: "https://doi.org/10.1142/S0217732316501078"
open_access: false
license: all-rights-reserved
files: [paper.pdf, citation.bib, figures/fig-1-rindler-cosmic-horizons.png]
status: supports
tags: [derivation, unruh-radiation]
---

# Inertial mass from Unruh temperatures

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.1142/S0217732316501078](https://doi.org/10.1142/S0217732316501078).

**Citation:** Giné, J. & McCulloch, M. E. (2016). *Inertial mass from Unruh temperatures*. Modern Physics Letters A 31(17), 1650107 (7 pp.). Received 5 Feb 2016, accepted 18 Apr 2016, published 26 May 2016 (dates as printed on the PDF). https://doi.org/10.1142/S0217732316501078

**About the stored PDF:** `paper.pdf` is the published World Scientific version (owner-supplied, local only; copyrighted). Article pages 1650107-1 to -7 are PDF pp. 1–7. Page references below use the printed article page numbers.

**Authorship:** the PDF lists two authors, J. Giné (Lleida) and M. E. McCulloch (Plymouth). As a McCulloch co-authored paper it is **not independent support** for QI.

**TL;DR:** The paper corrects a factor-of-two error in McCulloch's 2013 "asymmetric Casimir" derivation of inertia. A Rindler horizon at c²/a behind an accelerating particle suppresses Unruh radiation from that side, and the far Hubble horizon only slightly suppresses it from the front. Treating the Rindler side consistently (horizon "diameter" 2c²/(a cos θ)) lowers the predicted mass of a Planck-length cube from 2.53 m_P to 2.799 × 10⁻⁸ kg, 29% above the Planck mass. A second, qualitative section rewrites MiHsC as a Carnot-like efficiency between the Unruh temperature of the object and that of the cosmic horizon, and suggests looking for anomalous heat from highly accelerated systems.

## Key claims
- McCulloch's 2013 derivation (EPL 101, 59001) "included a factor of two error and so overpredicted the inertial mass" (p. 1650107-3). The corrected result is closer to the Planck mass. The paper also corrects a word in the 2013 paper: "anisotropic" should have been "isotropic" (p. 1650107-4).
- Inertia comes from the imbalance of Unruh radiation pressure: the radiation from the Rindler side is reduced by a "Rindler-scale Casimir effect", the radiation from the front only by a "Hubble-scale Casimir effect" (pp. 1650107-2, -3).
- The MiHsC equivalence-principle violation (m_i ≠ m_g) is argued to be invisible to torsion-balance tests, because the extra acceleration is mass-independent and equal for both test masses (p. 1650107-2).
- Thermal reading: m_I = m_i(1 − T_H/T_L) has the form of the Carnot limit W = Q₁(1 − T₂/T₁), so inertia "could also be thought of as the work done by the leakage of Unruh heat from the accelerated reference frame to the background cosmic reference frame" (p. 1650107-5). The relevant background is the Unruh temperature of the Hubble boundary, not the environmental temperature, since terrestrial Unruh temperatures are ~10⁻²⁰ K.
- The second law is invoked for the direction of inertia: only a force opposing the imposed acceleration reduces the "Utemperature" difference and increases entropy (p. 1650107-6). The authors call this explanation qualitative only.
- Proposed test: look for anomalous non-frictional heating or radiation near highly accelerated objects. The paper cites anomalous infrared emission from electrons accelerated around gold nanotips (Beversluis et al. 2003), which Smolyaninov (2008) proposed was Unruh radiation (p. 1650107-6).

## Key equations
Transcribed from the PDF.

MiHsC modified inertia, with β = 0.2 and Θ = 2c/H₀ = 2R_U (Eq. 1, p. 1650107-2):
$$ m_I = m_i\left(1 - \frac{\beta\pi^2 c^2}{|a|\Theta}\right) \sim m_i\left(1 - \frac{2c^2}{|a|\Theta}\right) \qquad (1) $$

Radiation pressure and the net force along a line at angle θ (Eqs. 2–3):
$$ F = \frac{uA}{3} \qquad (2), \qquad dF_x = \frac{u_{left}A\cos\theta}{3} - \frac{u_{right}A\cos\theta}{3} \qquad (3) $$
with u_right = u(1 − λ/(4Θ)) and, the correction made here, u_left = u(1 − λ/(4(2c²/(a cos θ)))).

Net force, angular integration (θ from 0 to π/2, doubled; φ from 0 to π) and result (Eqs. 4–7, p. 1650107-4):
$$ dF_x = \frac{u\lambda A\cos\theta}{3}\left(\frac{1}{4\Theta} - \frac{a\cos\theta}{8c^2}\right) \qquad (4) $$
$$ F = 2\times\frac{u\lambda A}{3}\int_0^{\pi}\!\!\int_0^{\pi/2}\left(\frac{\cos\theta}{4\Theta} - \frac{a\cos^2\theta}{8c^2}\right)d\theta\,d\phi \qquad (5) $$
$$ F = \pi\frac{2u\lambda A}{3}\left(\frac{1}{4\Theta} - \frac{\pi a}{32c^2}\right) \qquad (6), \qquad F = -\frac{\pi^2 u\lambda A a}{48c^2} \qquad (7) $$

With u = E/V = hc/(λV) and A/V = 1/l_P for a Planck-length cube (Eqs. 8–9):
$$ F = -\frac{\pi^2 h A a}{48 c V} \qquad (8), \qquad F = -\frac{\pi^2 h a}{48 c\, l_P} \;\Rightarrow\; m_i \sim \frac{\pi^2 h}{48 c\, l_P} \sim 2.799\times10^{-8}\ \text{kg} \qquad (9) $$

Thermal form (Eqs. 10–13, pp. 1650107-4, -5):
$$ m_I = m_i\left(1 - \frac{a_H}{|a|}\right) \;(10), \qquad m_I = m_i\left(1 - \frac{T_H}{T_L}\right) \;(11), \qquad W = Q_1\left(1 - \frac{T_2}{T_1}\right) \;(12), \qquad m_W = m_1\left(1 - \frac{T_2}{T_1}\right) \;(13) $$

Editorial check: the integrals in Eq. 5 are ∫₀^{π/2} cos θ dθ = 1 and ∫₀^{π/2} cos²θ dθ = π/4, which give Eq. 6; dropping the 1/(4Θ) term gives Eq. 7 ✓. Numerically π²h/(48 c l_P) = 2.81 × 10⁻⁸ kg with CODATA h and c and l_P = 1.616 × 10⁻³⁵ m, i.e. 1.29 m_P, so the printed 2.799 × 10⁻⁸ kg and "29%" are consistent ✓. The formula uses h, not ħ; with ħ it would give 4.5 × 10⁻⁹ kg. For the neglected term, πaΘ/(8c²) ≈ 10¹⁰ at a = 9.8 m/s² and Θ ≈ 2.6 × 10²⁶ m, so dropping 1/(4Θ) is justified at terrestrial accelerations.

## Data used
- None (theoretical). Constants used: l_P = 1.616 × 10⁻³⁵ m and m_P = 2.176 × 10⁻⁸ kg (p. 1650107-4). The cosmic acceleration is quoted as about 6.7 × 10⁻¹⁰ m/s² (p. 1650107-5).

## Results & predictions
- Corrected inertial mass of a Planck-length cube: 2.799 × 10⁻⁸ kg, **29% greater** than m_P. The 2013 result was 2.53 m_P (p. 1650107-4).
- **26% vs 29% (resolved):** Giné (2017, IJMPA) restates this result as "2.75 × 10⁻⁸ kg which is 26% greater than the Planck mass" ([2017-gine-inertial-mass-holographic](../2017-gine-inertial-mass-holographic/README.md), p. 1750043-3). This paper prints 2.799 × 10⁻⁸ kg and 29%. Editorial check: the formula gives 2.81 × 10⁻⁸ kg (1.29 m_P), so 29% is correct and the later 26% follows from the mis-copied 2.75 × 10⁻⁸ kg (2.75/2.176 = 1.26).
- Terrestrial Unruh temperature: about 4 × 10⁻²⁰ K at 9.8 m/s² (p. 1650107-6). Editorial check: ħa/(2πck_B) = 3.97 × 10⁻²⁰ K ✓. The printed formula "T = a/2πck" omits ħ, a typo.
- The thermal model is qualitative only. Its one prediction, anomalous heat from highly accelerated systems, has no quantitative estimate.
- Scope: the derivation produces a mass only for a body assumed to be a Planck-length cube (A/V = 1/l_P). It does not give the mass of any real particle, and Giné himself later wrote that this approach "does not give correct results for an elementary particle" (2017, p. 1750043-9).

## Figures
*Figure (local only): Fig. 1: A particle accelerating to the right sees a Rindler horizon at c²/a to its left and the cosmic horizon at Θ/2 to its right. The resulting asymmetry in Unruh radiation pressure pushes the particle back against its acceleration; θ is the integration angle in the x–y plane. (PDF p. 3.)*

## Notable quotes
> "However, the previous derivation included a factor of two error and so overpredicted the inertial mass." (p. 1650107-3)

> "this implies that the energy required to produce inertial mass could also be thought of as the work done by the leakage of Unruh heat from the accelerated reference frame to the background cosmic reference frame." (p. 1650107-5)

> "In this qualitative way, the second law of thermodynamics provides an explanation for inertia and also its direction." (p. 1650107-6)

## Criticisms & responses
- **Renda (2019)** argues that Eq. 8's substitution u = E/V = hc/(λV) assumes that only the peak wavelength of the Unruh spectrum contributes. He calls this "deeply incorrect" for classical accelerations, and quotes the 2.799 × 10⁻⁸ kg result as resting on it ([2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)).
- **Giné & Luciano (2021)**, with the same first author, say that the azimuthal integration over [0, π] used here (and in McCulloch 2013) gives "a incorrect numerical factor", and that the energy-density volume V is "not properly justified" because it should be the volume of space (a Planck volume), not of the particle ([2021-gine-luciano-inertia-fluctuations](../2021-gine-luciano-inertia-fluctuations/README.md), p. 4). Their re-derivation integrates φ from −θ to θ and gets F_x ≈ −0.6 m_p a/k.
- **Giné (2017)** concludes that this corrected development "still does not give the correct value of the Planck mass" and so does not work for an elementary particle (p. 1750043-9).
- Editorial notes:
  - The Planck mass is the comparison target only because the particle is assumed to be a Planck-length cube. The result is an O(1) multiple of h/(c l_P), so agreement to within a factor 1.29 is largely set by dimensional analysis.
  - The thermal section's m_I = m_i(1 − T_H/T_L) is a rewriting of Eq. 10, since Unruh temperature is proportional to acceleration. The Carnot analogy is not a derivation, and the authors call it qualitative.
  - The Hubble-scale term (the part of QI that drives its astrophysical predictions) is dropped in Eq. 7, so this derivation tests only ordinary inertia, not the MiHsC correction.
- No published critique specific to this paper beyond those above was found.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources:
  - [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md) (the model corrected here)
  - [2017-gine-inertial-mass-holographic](../2017-gine-inertial-mass-holographic/README.md) (follow-up; restates the result as 26%)
  - [2021-gine-luciano-inertia-fluctuations](../2021-gine-luciano-inertia-fluctuations/README.md) (later correction of this derivation)
  - [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
  - [2012-gine-holographic-modified-inertia](../2012-gine-holographic-modified-inertia/README.md) (source of the T_H/T_L form, Ref. 2)
  - [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md)
  - [2017-mcculloch-information-loss](../2017-mcculloch-information-loss/README.md)
  - [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md)
  - [2018-gine-hawking-unruh-uncertainty](../2018-gine-hawking-unruh-uncertainty/README.md)
