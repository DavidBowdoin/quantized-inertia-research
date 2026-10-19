---
title: "Pioneer anomaly"
tags: [pioneer-anomaly, solar-system, spacecraft-navigation, thermal-recoil]
verdict: mainstream-explained
---

# Pioneer anomaly

## The phenomenon and the data
- Pioneer 10 and 11 radiometric Doppler tracking (20–70 AU) showed an unmodelled, roughly constant Sunward acceleration **a_P = (8.74 ± 1.33) × 10⁻¹⁰ m s⁻²**. It is equivalent to a blue-shifted frequency drift of about 6 × 10⁻⁹ Hz s⁻¹ ([Turyshev & Toth 2010](../01-papers/2010-turyshev-pioneer-review/README.md); [Iorio 2015](../01-papers/2015-iorio-solar-system-anomalies/README.md)).
- Early (1998) values were (8.09 ± 0.20) × 10⁻¹⁰ m s⁻² for Pioneer 10 and (8.56 ± 0.15) × 10⁻¹⁰ m s⁻² for Pioneer 11. No variation with distance was found within 2 × 10⁻¹⁰ m s⁻² over 40–60 AU.
- Several independent analysts confirmed the anomaly in the data (Markwardt, Olsen, Toth, Levy et al.). Its direction cannot be told apart: Sunward, Earthward, spin-axis and velocity directions all lie within a few degrees of each other.
- Ulysses gave an ambiguous possible Sunward anomaly of (12 ± 3) × 10⁻¹⁰ m s⁻². Galileo data could not separate an anomaly from solar radiation pressure.
- No anomaly is seen inside ~10 AU (Anderson et al.'s 6 AU point) or in planetary motions. Ephemerides of Uranus, Neptune, Pluto and TNOs rule out a Pioneer-like Sunward acceleration on natural bodies. The TNO fit gives A = (0.87 ± 1.6) × 10⁻¹⁰ m s⁻², compatible with zero ([Iorio 2015](../01-papers/2015-iorio-solar-system-anomalies/README.md)).

## Mainstream explanation
- **Anisotropic thermal recoil** from the RTGs and electrical heat. The 2010 review already concluded that the heat was likely underestimated in 2002 and "may, in fact, account for all of it". It also predicted that the anomaly should decline as the ²³⁸Pu decays.
- Turyshev et al. (2012, *PRL* 108, 241101) built a finite-element model of Pioneer 10 with about 3,300 surface elements, using flight telemetry as boundary conditions. It reproduces about 80% of the Doppler-estimated acceleration: about 35% from the RTGs and 45% from electrical heat. The remaining ~20% lies within the combined 1σ error (total error budget 26.3%). The authors conclude that "no statistically significant acceleration anomaly exists".
- The Doppler data prefer an acceleration that decreases with time. The exponential fit gives τ = 28.8 ± 2.0 yr from the Doppler data and τ = 36.9 ± 6.7 yr from the thermal model ([2012-turyshev-pioneer-thermal](../03-criticism/2012-turyshev-pioneer-thermal/README.md)).
- Independent thermal studies reached similar conclusions: Rievers & Lämmerzahl 2011, and Francisco et al. 2012 (cited in the same README).
- Caveat stated by the authors: Pioneer 11 was not analysed at the same level of detail.

## QI's prediction
- **Paper:** [McCulloch 2007, MNRAS](../01-papers/2007-mcculloch-pioneer-anomaly/README.md), the founding MiHsC paper.
- **Model:** inertia is a reaction to Unruh radiation, and only wavelengths λ_n = 2Θ/n with Θ = 2c/H are allowed. The modified inertial mass is

  $$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{a\Theta}\right), \qquad a = \frac{GM_\odot}{r^2} + \frac{\beta\pi^2 c^2}{\Theta} \approx \frac{GM_\odot}{r^2} + 0.99\,cH $$

- **Number:** predicted **6.9 ± 3.5 × 10⁻¹⁰ m s⁻²**, against 8.74 ± 1.33 × 10⁻¹⁰ m s⁻² observed. Inputs were β = 0.2, H = 2.3 ± 0.9 × 10⁻¹⁸ s⁻¹ and Θ = 2.7 × 10²⁶ m.
  - The ~40% uncertainty in the prediction comes from H.
  - The paper claims "no adjustable parameters".
- **Acknowledged failure:** the same paper predicts an anomaly inside 10 AU and for the planets, and neither is seen. It suggests that the effect depends on the trajectory (bound vs unbound orbits) but does not model this.
- **Holographic re-derivation:** Giné (2011), who is not McCulloch's co-author, recovers a = GM/r² + ~cH₀ from a Verlinde/MOND-like interpolation function ([2011-gine-pioneer-holographic](../01-papers/2011-gine-pioneer-holographic/README.md)). He concedes that a constant a₀ "is dramatically inconsistent with the motion of the inner planets": Mercury's precession limits any extra constant acceleration to more than 10× below a₀.

## Independent tests, critiques and null results
- The thermal analysis of Turyshev et al. 2012 removes the observation QI was built to explain. Iorio's 2015 review treats the Pioneer anomaly as resolved by conventional effects.
- Turyshev & Toth (2010) call the coincidence a_P ≃ cH₀ "misleading":
  - A cosmic-expansion effect would point *away* from the Sun.
  - Matching a_P would need H₀ ≃ 95 ± 14 km s⁻¹ Mpc⁻¹.
  - They also call the "onset" of the anomaly at the bound-to-unbound transition at Saturn "highly suspect", quite likely an artifact. McCulloch 2007 cited that onset as a possible test.
- The review names McCulloch only once (p. 93), in a list of new-physics candidates.
- The outer-planet and TNO ephemerides limit a constant extra acceleration on bound natural bodies ([Iorio 2015](../01-papers/2015-iorio-solar-system-anomalies/README.md)).
- **McCulloch's response** (blog, 1 May 2012): six objections to the thermal model.
  - The Ulysses anomaly.
  - Noisy decay evidence.
  - The fitted half-lives differ from the 87.7-yr Pu half-life.
  - The lack of an inner-Solar-System thermal signal.
  - Anderson et al.'s earlier estimate of only ~0.55 × 10⁻¹⁰ m s⁻² from the RTG fins.
  - A complex model with "fitting parameters".

  Editorial note in the criticism README: the acceleration mixes RTG heat with electrical heat, which falls faster, so a shorter fitted half-life is expected.
- No independent group has defended a QI origin for the Pioneer anomaly in the literature collected here.

## Assessment
The Pioneer anomaly was real in the tracking data. It is now explained, within stated uncertainties, by anisotropic thermal recoil from the spacecraft, and three independent thermal studies agree. QI's 2007 prediction (6.9 ± 3.5 × 10⁻¹⁰ m s⁻²) did match the size of the effect within its large error bar, which mostly comes from the then-uncertain Hubble constant. However, the same model predicts an anomaly in the inner Solar System and on bound planetary orbits that is not seen, and the paper says so itself. The proposed escape, that the effect works only on unbound trajectories, has never been made quantitative. McCulloch still disputes parts of the thermal model, but the observation that QI explained has largely gone away, so it no longer counts as evidence for QI.

## Sources
- [2007-mcculloch-pioneer-anomaly](../01-papers/2007-mcculloch-pioneer-anomaly/README.md)
- [2010-turyshev-pioneer-review](../01-papers/2010-turyshev-pioneer-review/README.md)
- [2011-gine-pioneer-holographic](../01-papers/2011-gine-pioneer-holographic/README.md)
- [2015-iorio-solar-system-anomalies](../01-papers/2015-iorio-solar-system-anomalies/README.md)
- [2012-turyshev-pioneer-thermal](../03-criticism/2012-turyshev-pioneer-thermal/README.md)
- Related evidence: [flyby-anomaly](flyby-anomaly.md), [cosmic-acceleration](cosmic-acceleration.md), [derivation](derivation.md)
