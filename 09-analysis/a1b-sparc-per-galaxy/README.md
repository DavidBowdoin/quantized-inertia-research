---
title: "A1b: per-galaxy SPARC rotation-curve fits, QI vs MOND"
tags: [analysis, galaxy-rotation, sparc, mond, theta]
as_of: 2026-10-20
---

# A1b: per-galaxy SPARC rotation-curve fits, QI vs MOND

> **Editorial analysis.** This is our own calculation, not a published result. It follows up [A1](../a1-sparc-rar-refit/README.md) by fitting individual rotation curves with distance, inclination and stellar mass-to-light priors in the style of [Li et al. 2018](https://doi.org/10.1051/0004-6361/201732547).

## Question
Does allowing per-galaxy uncertainties in distance, inclination and Υ★ remove the preference for a free QI scale found in the stacked SPARC RAR fit?

## Findings and limits
Under the tested priors and velocity-error assumptions, the 2017 QI equation at either fixed Θ tested here fits less well than a free scale. The baseline best QI scale is Θ ≈ 1.37 × 10²⁷ m (galaxy-bootstrap 16–84%: 1.22–1.51 × 10²⁷ m), compared with 1.23 × 10²⁷ m in A1. This identifies a conditional normalization tension, but does not establish model-independent exclusion of QI. This per-galaxy fit extends the author's binned/RMS comparison rather than reproducing it; see [A1's scope](../a1-sparc-rar-refit/README.md#relation-to-mccullochs-comparison).

The comparison uses **Q = velocity χ² + prior penalty**, a descriptive penalized fit loss. It is **not BIC, a Bayes factor, or an exclusion significance**. There is no `k ln n` term. Free-scale QI includes the fixed scales and has an extra global parameter, so a lower Q is expected; the improvement alone does not reject a fixed scale. Bootstrap ranges show sampling variation conditional on the selected errors and priors, not posterior model probabilities.

| Model | Baseline ΔQ vs MOND simple | Interpretation |
|---|---|---|
| QI, Θ = 2.6 × 10²⁶ m | about +14,500 | Substantially larger loss under the tested assumptions |
| QI, Θ = 8.8 × 10²⁶ m | about +1,200 | Larger loss; the fit also shifts distances downward |
| QI, Θ free | about +612 | Higher loss than MOND simple at the baseline priors and errors |

The [generated results](results/summary.md) give velocity χ² and prior penalties separately, bootstrap ranges, and the full sensitivity refit. The loss differences in this analysis cannot be compared in magnitude with A1's point-level BIC differences: the sample, residuals and objectives differ.

## Velocity-error sensitivity
The script runs a second complete analysis with velocity errors enlarged by a common factor. It chooses the factor as √max(1, χ²_velocity / (n − p − 1)) from the baseline MOND simple fit, where n = 3,168 and p = 490 nuisance parameters. **Prior penalties are excluded from that diagnostic ratio.** Distance, inclination and Υ★ priors remain unchanged. All galaxy profiles and global scales are refitted, and the galaxy bootstrap is repeated on those new profiles.

The resulting multiplier is **2.1659** (variance multiplier 4.6912). The best QI scale remains near **Θ = 1.39 × 10²⁷ m**. Fixed Θ = 8.8 × 10²⁶ m has ΔQ ≈ **+498** against MOND simple (bootstrap +368 to +655), compared with +1,203 in the baseline fit. Its median D/D₀ becomes **0.928**, with **37/153** galaxies shifted more than 20% closer, compared with 50/153 at baseline. The direction of the fit comparison persists in this scenario, while the score differences and distance shifts change.

This is a sensitivity scenario, not an inferred noise model or a conservative bound on evidence. The factor is held fixed during its bootstrap; its own uncertainty is not propagated. A large residual χ² can reflect underestimated errors, correlated residuals or model inadequacy. A common multiplier does not distinguish these possibilities or model galaxy-specific systematics. Numerical results for this scenario are in [results/summary.md](results/summary.md#enlarged-velocity-errors-full-refit).

## Distance shifts and their uncertainties
For fixed Θ = 8.8 × 10²⁶ m, the baseline fit moves 50 of 153 galaxies more than 20% closer, with median D/D₀ ≈ 0.88. The corresponding free-scale QI and MOND simple medians are near 0.97. Distance changes g_obs ∝ 1/D while leaving g_bar unchanged, so it can absorb part of a scale mismatch.

A 20% shift is not the same as a statistically significant disagreement with a measured distance. The affected galaxies use different distance methods:

| Distance method | Galaxies in sample | D/D₀ < 0.8, fixed late Θ |
|---|---|---|
| Hubble flow | 83 | 34 |
| TRGB | 39 | 5 |
| Cepheids | 3 | 1 |
| Ursa Major cluster | 26 | 9 |
| Supernovae | 2 | 1 |

Thus 43 of the 50 use Hubble-flow or cluster distances; seven use TRGB, Cepheid or supernova distances. The [generated distance table](results/summary.md#baseline-distances-by-measurement-method) reports **(D_fit − D₀)/σ_D** by method, including counts below −2 and −3, alongside the MOND reference. These shifts are conditional diagnostics; catalogue errors and shared distance calibrations may themselves be imperfect.

Using standardized pulls, 28/153 galaxies move below −2σ_D in the fixed late-Θ fit, compared with 12/153 for MOND simple. Among TRGB distances, the counts are 13/39 and 8/39 respectively. Thus the distance tension is not absent in the more precise subsample, but the aggregate count of 20% shifts does not measure it.

## Data and sample
- **SPARC** mass models and galaxy table: Lelli, McGaugh & Schombert 2016, AJ 152, 157, [doi:10.3847/0004-6256/152/6/157](https://doi.org/10.3847/0004-6256/152/6/157). A1 fetches the tables into its git-ignored `data/` directory. Input SHA-256 checksums are recorded in `results.json`.
- **Sample:** 153 galaxies with Q < 3 and inclination ≥ 30°, totaling 3,168 usable positive-radius, positive-velocity points with positive velocity errors. A1's 10% velocity-error cut is not applied; its RAR sample retains points from 147 of these galaxies.
- The distance-method labels and errors come from the SPARC galaxy table.

## Method
- **Models:** V_pred = √(g_bar ν(g_bar/a) R), with the same QI, MOND simple, MOND standard and McGaugh functions as A1. QI uses [McCulloch 2017 Eq. 8](../../00-overview/equations.md#5-galaxy-scale-relations-2017-onward), with a = 2c²/Θ.
- **Priors:** Gaussian penalties in log₁₀ Υ_disk around log₁₀ 0.5 and log₁₀ Υ_bulge around log₁₀ 0.7, each with width 0.1 dex. Bulgeless galaxies have no bulge parameter. Distance and inclination have Gaussian penalties around catalogue values, with catalogue errors (floors: 1% in distance and 1° in inclination). Gas mass is fixed, with helium already included in SPARC's gas velocities.
- **Scaling:** radii scale with D and baryonic velocities with √D. Observed velocities and errors scale by sin i₀ / sin i. There are 490 nuisance parameters across the sample.
- **Optimization:** at each shared log₁₀ a, minimize Q over each galaxy's nuisance parameters using L-BFGS-B. The scale grid covers −11 to −8.5 in 0.01-dex steps and includes both exact fixed-Θ scales for QI. Distance and inclination bounds are generally ±5 catalogue standard deviations, intersected with physical bounds; log₁₀ Υ bounds are −1.5 to 0.7. Fits start from neighboring scale solutions. The global profile is summed, its minimum refined parabolically on the regular grid, and compared with any better exact fixed-scale point. Final nuisance diagnostics are refitted at that global scale.
- **Reporting:** Q is split into velocity χ² and prior penalty. These are maximum-a-posteriori fits in the stated parameter coordinates, not marginalized posterior evidence. Standard BIC is based on maximized likelihood; adding prior penalties and cancelling equal nuisance counts does not by itself establish that approximation ([Schwarz 1978](https://doi.org/10.1214/aos/1176344136)).
- **Bootstrap:** 1,000 resamples of whole galaxies, with replacement. Each resample re-sums the appropriate scenario's stored profiles and refines the global scale. Bootstrap results use this grid approximation. Both scenarios use the same seed and galaxy draws. No model-probability or exclusion interpretation is assigned to these ranges.

## Figures
Our own figures (CC BY 4.0), showing the baseline catalogue-error fits.

![Total misfit against the shared acceleration scale](results/fig-1-global-profile.svg)

*Figure 1. Q summed over all galaxies, relative to the best model, on a log(1 + Δ) scale. This is a fit-loss profile, not an evidence scale. The models approach Newtonian behavior when g_bar/a is large.*

![Cumulative distribution of fitted distance over catalogue distance](results/fig-2-distance-shift.svg)

*Figure 2. Cumulative distribution of fitted ÷ catalogue distance. Values outside 0.3–1.7 are drawn at the frame edge. Interpret fractional shifts together with the method-specific standardized pulls above.*

![Histogram of the Θ preferred by each galaxy alone](results/fig-3-theta-per-galaxy.svg)

*Figure 3. Each galaxy's best QI Θ, with its nuisance parameters fitted. The wide distribution of point estimates is not an estimate of intrinsic scale variation: individual uncertainties and grid-edge solutions must also be considered.*

## Caveats
- **Error-model and prior dependence:** enlarging random velocity errors is only one sensitivity check. Correlated rotation-curve residuals, variations in prior widths and shared calibration errors remain unmodeled. A galaxy bootstrap changes sample composition while retaining these assumptions; it does not make the result independent of per-point errors.
- **Goodness of fit:** velocity χ² is kept separate from prior penalties. Ratios using n − p are descriptive because informative priors alter effective degrees of freedom; they are not calibrated goodness-of-fit tests here.
- **Optimization:** local minima remain possible. Warm starts and convergence checks on final fits do not prove global optimality or replace posterior marginalization.
- **Physics scope:** only the published 2017 QI function is tested. The older-Θ run substitutes an earlier scale into that function; it is not a reproduction of the 2007 or 2012 analysis. Renda's disputed reconstruction remains a separate investigation (A2), alongside an audit of McCulloch's later derivations (A2b in [ideas-and-tests](../../08-synthesis/ideas-and-tests.md)). MOND's external field effect is omitted.

## Reproduce
```sh
uv venv --python 3.13 .venv
uv pip install --python .venv/bin/python -r 09-analysis/requirements.txt
.venv/bin/python -I 09-analysis/a1b-sparc-per-galaxy/test_fit_galaxies.py
.venv/bin/python -I 09-analysis/a1b-sparc-per-galaxy/fit_galaxies.py
```
The last command runs both scenarios, with 1,000 galaxy resamples each. The seed is fixed (`--seed 20261019`); `--boot 0` skips resampling while still refitting both scenarios. Outputs:
- `results/results.json`: baseline fits, separate objective terms, per-galaxy diagnostics and profiles, plus the full `velocity_error_sensitivity` analysis
- `results/summary.md`: generated comparison and distance tables
- `results/fig-*.svg`: baseline figures

## Related
- [A1: stacked RAR refit](../a1-sparc-rar-refit/README.md) · [ideas-and-tests](../../08-synthesis/ideas-and-tests.md)
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2017-mcculloch-galaxy-rotations-sparc](../../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md), [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
