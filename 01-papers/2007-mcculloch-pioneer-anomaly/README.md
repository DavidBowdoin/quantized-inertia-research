---
title: "Modelling the Pioneer anomaly as modified inertia"
authors: [Michael E. McCulloch]
year: 2007
type: paper
venue: "Monthly Notices of the Royal Astronomical Society 376(1), 338-342"
doi: 10.1111/j.1365-2966.2007.11433.x
arxiv: astro-ph/0612599
url: "https://doi.org/10.1111/j.1365-2966.2007.11433.x"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-allowed-wavelengths.png, figures/fig-2-pioneer-prediction.png]
status: supports
tags: [pioneer-anomaly, derivation, cosmic-acceleration]
---

# Modelling the Pioneer anomaly as modified inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:astro-ph/0612599](https://arxiv.org/abs/astro-ph/0612599) · [doi:10.1111/j.1365-2966.2007.11433.x](https://doi.org/10.1111/j.1365-2966.2007.11433.x).

**Citation:** McCulloch, M. E. (2007). *Modelling the Pioneer anomaly as modified inertia*. Monthly Notices of the Royal Astronomical Society 376(1), 338-342. [doi:10.1111/j.1365-2966.2007.11433.x](https://doi.org/10.1111/j.1365-2966.2007.11433.x) / [arXiv:astro-ph/0612599](https://arxiv.org/abs/astro-ph/0612599)

**TL;DR:** The founding paper of what became MiHsC / Quantised Inertia. It assumes (1) inertia is a reaction to Unruh radiation and (2) only Unruh wavelengths that fit within a Hubble-scale length Θ = 2c/H are allowed (a Casimir-like effect). Low accelerations then reduce inertial mass slightly, which adds a constant Sunward term of 6.9 ± 3.5 × 10⁻¹⁰ m s⁻² for the Pioneer probes. That matches the observed 8.74 ± 1.33 × 10⁻¹⁰ m s⁻² beyond 10 AU within error bars, but the model also predicts an anomaly inside 10 AU, which was not observed.

> Note: the text here was taken from the arXiv preprint (v1, Dec 2006), which is stored as `paper.pdf`. Page numbers are preprint pages; the published MNRAS version may differ in wording and pagination.

## Key claims
- Inertia is assumed to be a reaction to Unruh radiation (building on Haisch, Rueda & Puthoff 1994 and Milgrom 1994/1999).
- Only Unruh wavelengths that fit exactly into twice the Hubble distance (Θ = 2c/H, "a Hubble diameter") are allowed, "a process similar to the Casimir effect".
- The thinner sampling of the spectrum at long wavelengths is modelled by a linear factor F = 1 − λ_m/4Θ, which gives a modified inertial mass that falls below the gravitational mass at low acceleration.
- The model gives the Pioneer anomaly with "no adjustable parameters". The author contrasts this with Moffat & Brownstein's STVG fit, which uses two adjustable parameters but fits the data more closely.
- There is a minimum acceleration ~ 0.99 × cH, which the paper notes is close to the Hubble expansion rate cH.
- The model predicts an anomaly within 10 AU of the Sun and for the planets, neither of which is observed. The paper suggests this may be because the Pioneers' trajectories are unbound, citing Milgrom (2005) on how modified-inertia predictions depend on trajectory.

## Key equations
Unruh temperature and peak wavelength (Wien's law, β = 0.2):
$$ T = \frac{\hbar a}{2\pi c k}, \qquad \lambda_m = \frac{4\pi^2 \beta c^2}{a} $$
Allowed (Casimir-like) wavelengths:
$$ \lambda_n = \frac{2\Theta}{n} $$
Modified inertial mass:
$$ m_I = m_i\left(1 - \frac{\lambda_m}{4\Theta}\right) = m_g\left(1 - \frac{\beta\pi^2 c^2}{a\Theta}\right) $$
Equation of motion for the Pioneer craft and the resulting acceleration:
$$ a = \frac{GM_\odot}{r^2} + \frac{\beta\pi^2 c^2}{\Theta} \;\approx\; \frac{GM_\odot}{r^2} + 0.99 \times cH $$
Predicted maximum black-hole mass (applying the same wavelength limit to Hawking radiation):
$$ M \le \frac{c^3}{8\pi^2 G \beta H} $$

## Data used
- Pioneer 10/11 anomalous acceleration against heliocentric distance out to ~45 AU, from Anderson et al. (1998, 2002).
- Hubble constant H = 2.3 ± 0.9 × 10⁻¹⁸ s⁻¹ (so Θ = 2.7 × 10²⁶ m).

## Results & predictions
- Predicted anomaly: 6.9 ± 3.5 × 10⁻¹⁰ m s⁻². Observed: 8.74 ± 1.33 × 10⁻¹⁰ m s⁻². The ~40% uncertainty in the prediction comes from the uncertainty in H.
- The extra term is about six times the MOND constant a₀ = 1.2 × 10⁻¹⁰ m s⁻².
- Milgrom's abrupt cut-off would apply at ~26 × 10⁻¹⁰ m s⁻². The paper argues an abrupt break cannot explain Pioneer, because the craft's acceleration at 50 AU (~10⁻⁵ m s⁻²) is still far above that.
- For a 1 kg object at 9.8 m s⁻², inertial mass is predicted to be lower by 7 × 10⁻¹¹ kg. For the Pioneer craft, inertia is predicted to fall by 0.01%.
- Predicted maximum black-hole mass: about 1 × 10⁵² kg (~10²² solar masses).
- Very cold bodies should radiate slightly less than the Stefan–Boltzmann law predicts. At 100 pK the fractional change is 2.7 × 10⁻²⁰.
- Proposed tests:
  - Radial variations in m_I/m_g in galaxy rotation curves.
  - Roche-lobe shapes that depend on the probe's trajectory (modified inertia) or do not (modified gravity).
  - The anomaly starting when the Pioneers moved from bound to hyperbolic orbits.
  - Galaxy anomalous accelerations that correlate with distance (cosmic time).
- Failed prediction (acknowledged): an anomaly inside ~10 AU, where Anderson et al.'s 6 AU point shows none.

## Figures
*Figure (local only): Fig. 1 — Schematic of Unruh spectra at higher and lower acceleration, with dashed vertical lines marking the wavelengths allowed within twice the Hubble distance (preprint p. 14).*

*Figure (local only): Fig. 2 — Observed Pioneer 10/11 anomaly against distance from the Sun (bars, from Anderson et al. 2002), with the constant predicted value from Eq. 11 (solid line) and its error range (dashed lines) (preprint p. 15).*

## Notable quotes
> "This new scheme is appealingly simple and does not require adjustable parameters. However, it also predicts an anomaly within 10 AU of the Sun, which has not been observed." (p. 1)

> "The assumptions made in equation (6) and (7) have not individually been verified, but they do produce results similar to the Pioneer anomaly." (p. 10)

## Criticisms & responses
- **Thermal explanation of the Pioneer anomaly.** Turyshev et al. (2012, *Phys. Rev. Lett.* 108, 241101, [arXiv:1204.2507](https://arxiv.org/abs/1204.2507)) concluded that anisotropic thermal recoil from the spacecraft accounts for the anomaly, with no unexplained residual. This removed the observation the paper set out to explain. See [2012-turyshev-pioneer-thermal](../../03-criticism/2012-turyshev-pioneer-thermal/README.md).
- **Inner Solar System.** The paper itself notes that it predicts an anomaly inside 10 AU and for bound planetary orbits, which is not seen. Its suggested reason is trajectory dependence, which it does not model quantitatively.
- **Assumed parameterisation.** The linear factor F and the identification of inertia with the integral of the Unruh spectrum are assumed rather than derived, as the paper itself states (p. 10). Later critics of the QI derivation in general include Renda (2019); see [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).
- Turyshev & Toth's 2010 review lists this proposal among candidate new-physics explanations; see [2010-turyshev-pioneer-review](../2010-turyshev-pioneer-review/README.md).

## Related
- Evidence: [pioneer-anomaly](../../02-evidence/pioneer-anomaly.md), [derivation](../../02-evidence/derivation.md), [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md)
- Sources:
  - [2010-turyshev-pioneer-review](../2010-turyshev-pioneer-review/README.md)
  - [2011-gine-pioneer-holographic](../2011-gine-pioneer-holographic/README.md)
  - [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md)
  - [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md)
  - [2012-turyshev-pioneer-thermal](../../03-criticism/2012-turyshev-pioneer-thermal/README.md)
  - [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
