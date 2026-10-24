---
title: "A6e: QI's redshift law against 263 discs with halo-independent baryonic masses"
tags: [analysis, galaxy-rotation, high-redshift, tully-fisher, theta, kmos3d, kross]
as_of: 2026-10-24
---

# A6e: QI's redshift law against 263 discs with halo-independent baryonic masses

> **Editorial analysis.** This is our own calculation, not a published result. It uses the catalogues of [Sharma et al. 2025](../../01-papers/2025-sharma-dark-matter-fraction/README.md), whose baryonic masses come from photometry and gas scaling relations rather than from a dark-matter halo fit. That makes them closer to what a no-dark-matter theory such as QI needs than the inputs of [A6](../a6-rar-redshift-evolution/README.md), [A6b](../a6b-musedark-per-galaxy/README.md) or [A6c](../a6c-rc100-qi/README.md).

## Question
Using circular velocities and effective baryonic masses at up to three radii for 263 discs at 0.6 ≤ z < 2.5, does McCulloch's 2017 Eq. 8 with a_Q = 2c²(1+z)/Θ₀ fit? Does the (1+z) shape hold within a single survey? Do fitted scales differ between stellar-mass groups? QI predicts no mass dependence at fixed redshift, but the groups here are not matched in redshift.

## Bottom line
1. **A lower baryonic mass scale improves the published prediction under this likelihood.** At R_out, the published law is 22 worse in −ln L than a constant scale with fitted amplitude. A common −0.31 dex shift in baryonic mass removes most of the difference. This is comparable in magnitude to the 0.3 dex gas-scaling uncertainty, and the authors suspect overestimated stellar masses. However, a common shift in all baryons is not the same uncertainty as a gas-mass error. This sensitivity check neither establishes that the masses are wrong nor demonstrates a jointly allowed correction; the normalization inference remains conditional on the mass calibration and error model.
2. **Survey systematics are larger than any redshift trend.** At the same redshift, z ≈ 0.85–0.89, KROSS gives a QI scale of 1.32 and KMOS3D 3.11 × 10⁻¹⁰ m s⁻². Pooling surveys mixes this offset into the redshift dependence, so the pooled shape is unconstrained: γ = 0.10, bootstrap 16–84% −1.15 to 1.00.
3. **Within KMOS3D, the only survey spanning z = 0.7–2.4, the (1+z) shape is mildly disfavoured.** The fitted γ is −1.66, and γ ≥ 1 occurs in 1.5% of galaxy resamples. The binned values (3.11, 3.90 and 2.21 × 10⁻¹⁰ at z ≈ 0.9, 1.4 and 1.7) are not monotonic, and the first two are 0.8 times McCulloch's prediction.
4. **The fitted scales differ between stellar-mass halves, in opposite directions in the two large surveys.** In KROSS the upper mass half gives a larger scale; in KMOS3D, a smaller one. QI predicts no mass dependence at fixed redshift. These halves are not matched in redshift or other properties, so this is a diagnostic of possible systematics rather than an isolated test of mass dependence.
5. **The Eq. 13 offsets are descriptive; its applicability at R_out is unverified.** Substituting V(R_out) into the deep-limit Tully–Fisher formula gives masses below the catalogue's baryonic masses within R_out by median offsets of 0.40–0.62 dex. Using total baryonic mass, including an assumed extended atomic-gas disc, gives offsets of 0.86–0.92 dex. We have not established that V(R_out) is asymptotic, that the acceleration is sufficiently low, or that R_out encloses the mass used in the total-mass comparison. These offsets therefore do not separately exclude QI. The main Eq. 8 fits retain its transition term. The medians include galaxies with M_bar > M_dyn (19% at R_out); their central values cannot be matched by a positive QI scale with baryons fixed, but their mass and velocity uncertainties still matter.

The data quality limits these conclusions. Most fits require no additional intrinsic scatter under the adopted errors. That does not establish that the likelihood differences are conservative: shared calibration errors do not average down as independent galaxy errors. The clearest diagnostics are the survey offset and the sensitivity to a common mass shift. A reliable strength of evidence requires modelling shared survey and mass-calibration uncertainties.

## Data
- **Catalogues:** `KMOS3D_FDM_CATALOG_GS.csv`, `KGES_FDM_CATALOG_GS.csv` and `KROSS_FDM_CATALOG_GS.csv` from [Zenodo 10.5281/zenodo.15458539](https://doi.org/10.5281/zenodo.15458539) (CC BY 4.0), downloaded into the git-ignored `data/` folder and checked by SHA-256.
- **Per galaxy:** redshift, stellar mass, R_e with error, circular velocity (pressure-corrected) at R_e, R_opt = 1.89 R_e and R_out = 2.95 R_e with errors, and baryonic mass enclosed within each radius with errors. Baryonic mass is M★ + M_H₂ + 1.33 M_HI, with gas from scaling relations.
- **Convention check (editorial):** at R_out the catalogue's dynamical mass agrees with V²R/G to within 0.5% in the median. At R_opt it includes a factor of about 1.05. We compute g_obs directly from V²/R at every radius. Sharma Appendix D constructs the tabulated baryonic component masses from disc velocities via M(<R) = V²R/G, so G M_bar(<R)/R² recovers that model's baryonic acceleration; these are effective dynamical masses, not literal enclosed masses for a spherical baryon distribution.

## Method
- **Model:** g = g_bar √(1 + a/g_bar) (McCulloch 2017 Eq. 8), with a(z) published, SPARC-calibrated, constant, (1+z), H(z) or (1+z)^γ. A variant adds a common shift in baryonic mass to the published law.
- **Likelihood:** Gaussian in ln g_obs. Variance = (2σ_V/V)² + s²σ_M² + (2s − 1)²σ_R² + τ², the first-order effect of velocity, baryonic-mass and radius errors, with R entering both accelerations. Mass errors use a log-normal width matched to the linear error.
- **Weights:** the slope s = (1 + (g_bar/g_obs)²)/2 is Eq. 8's derivative evaluated at the observed point, the same for every model. An earlier version let s follow each model; with mass errors of about 0.55 dex, fits then lowered their own variances, and a mass-shifted law appeared better than it was.
- **Samples:** R_out (main; the authors' most reliable radius), KMOS3D alone, R_opt, R_e where R_e exceeds the PSF, all radii together, and an illustrative cut excluding M_bar > M_dyn.
- **Uncertainty:** 400 galaxy bootstrap resamples, keeping each galaxy's radii together, and 1σ profile intervals for binned scales.

## Results
Generated by the script (`results/summary.md`). Δ(−ln L) relative to a constant scale with fitted amplitude; positive is worse.

| Sample | Published | Published + mass shift | (1+z), free amplitude | γ fitted |
|---|---|---|---|---|
| R_out, all surveys | +22.0 | +0.6 (shift −0.31 dex) | +0.3 | 0.10 |
| R_out, KMOS3D only | +2.3 | +1.0 (shift −0.13 dex) | +1.1 | −1.66 |
| All radii | +35.8 | −2.0 (shift −0.24 dex) | −0.7 | 0.85 |
| R_e, resolved (53 galaxies) | +0.3 | +0.1 | −0.1 | 0.82 |

![QI scale by survey and redshift](results/fig-1-aq-by-survey.svg)

*Figure 1. The constant QI scale fitted at R_out in each survey and, for KMOS3D, in three redshift bins, with 1σ profile intervals. The orange line is McCulloch's published prediction.*

## Caveats
- **Baryonic masses rest on SED fits and gas scaling relations**, with atomic gas assumed to extend to twice the ionised-gas radius. Those assumptions dominate the error budget and may vary with redshift and survey.
- **Velocities at R_opt and R_out are sometimes interpolated or extrapolated**; about a third of rotation curves do not reach R_out, and the authors inflate the errors accordingly.
- **Shared systematic errors are not modelled.** Treating them as independent can overstate precision on a common offset or trend. Neither a small fitted τ nor inflated marginal errors determines whether a likelihood difference is conservative. Galaxy resampling preserves within-galaxy grouping but does not propagate a shared survey calibration; its fractions are not exclusion probabilities.
- **The baryonic accelerations inherit the catalogue's disc profiles.** The halo-independent input still depends on assumed stellar and gas distributions, inclination, pressure support and photometric/gas calibrations. The Eq. 13 comparison additionally needs the deep, asymptotic regime, which is not established here.

## Reproduce
```sh
.venv/bin/python -I 09-analysis/a6e-sharma-qi/test_sharma_qi.py
.venv/bin/python -I 09-analysis/a6e-sharma-qi/sharma_qi.py --boot 400   # ~1 min; downloads three catalogues on first run
```
Requires numpy and scipy. The bootstrap seed is fixed (`--seed 20261023`).

## Related
- Analyses: [A6](../a6-rar-redshift-evolution/README.md), [A6b](../a6b-musedark-per-galaxy/README.md), [A6c](../a6c-rc100-qi/README.md), [A6d](../a6d-mcculloch-2017-highz/README.md)
- Sources: [2025-sharma-dark-matter-fraction](../../01-papers/2025-sharma-dark-matter-fraction/README.md), [2017-ubler-tully-fisher-evolution](../../01-papers/2017-ubler-tully-fisher-evolution/README.md), [2017-mcculloch-galaxy-rotations-sparc](../../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
