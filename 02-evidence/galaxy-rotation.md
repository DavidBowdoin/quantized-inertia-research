---
title: "Galaxy rotation curves and the radial acceleration relation"
tags: [galaxy-rotation, dark-matter, mond, tully-fisher, sparc, high-redshift]
verdict: supported-by-author-only
---

# Galaxy rotation curves and the radial acceleration relation

## The phenomenon and the data
- Disc galaxies rotate faster in their outskirts than their visible (baryonic) mass predicts under Newtonian gravity. The anomaly appears at accelerations below about a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻².
- Two empirical regularities summarise it:
  - The **baryonic Tully–Fisher relation**, v⁴ ∝ M_b. McCulloch 2012 used the binned McGaugh et al. 2010 dwarfs, spirals and clusters, with a 30% error on observed velocities.
  - The **radial acceleration relation (RAR)** of SPARC: 153 galaxies, about 2,700 points (McGaugh, Lelli & Schombert 2016, *PRL* 117, 201101). The empirical fit is a_obs = a_bar / (1 − e^(−√(a_bar/a₀))).
- These data are cited in [2017-mcculloch-galaxy-rotations-sparc](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md), [2017-smolin-mond-quantum-gravity](../01-papers/2017-smolin-mond-quantum-gravity/README.md) and [2019-cadoni-long-range-qg](../01-papers/2019-cadoni-long-range-qg/README.md).
- **High redshift:**
  - Übler et al. 2017 (KMOS) find the Tully–Fisher zero point evolving by −0.38 to −0.47 dex at z ≈ 0.9 and −0.2 to −0.47 dex at z ≈ 2.3.
  - Genzel et al. 2017 report six strongly baryon-dominated discs at z = 0.85–2.38.
  - MUSE-DARK III (Ciocan et al. 2026) measures the RAR for 79 galaxies at 0.33 < z < 1.44 and finds a₀ rising from about 1.99 to 2.71 × 10⁻¹⁰ m s⁻² across four redshift bins ([2026-ciocan-muse-dark-rar](../01-papers/2026-ciocan-muse-dark-rar/README.md)). Alcock 2026 refits those bins and finds a₀ ∝ (1+z)^0.78±0.15, consistent with H(z) tracking ([2026-alcock-rar-scale-hubble](../01-papers/2026-alcock-rar-scale-hubble/README.md)). Neither paper mentions QI.

## Mainstream explanation(s)
- **Dark matter halos (ΛCDM)** are the standard account. McCulloch's own media piece is noted as non-peer-reviewed, and its README states that dark matter remains the mainstream explanation ([2018-mcculloch-dark-matter-scitrends](../07-media/2018-mcculloch-dark-matter-scitrends/README.md)).
- Übler et al. and Genzel et al. interpret their high-z results within ΛCDM, in terms of high gas fractions and pressure support.
- **MOND** (Milgrom) is the main empirical alternative, with a fitted a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻². Several independent theorists derive MOND-like behaviour from horizons or de Sitter physics without using QI:
  - Smolin 2017: a_Λ = c²√Λ, a₀ ≈ a_Λ/8.3.
  - Cadoni & Tuveri 2019: a₀ = H/2π.
  - Hernandez et al. 2019: bounding curvature.
  - Haug 2021: g_min = GM_u/r_u² ≈ 5.18 × 10⁻¹¹ m s⁻².

  These papers cite McCulloch only in passing. Hernandez et al. call his vacuum route "unsatisfactory".

## QI's prediction
- **Minimum acceleration (2010).** [McCulloch 2010, EPL](../01-papers/2010-mcculloch-minimum-accelerations/README.md) derives a minimum acceleration 2c²/Θ. It predicts a minimum apparent disc-galaxy mass of 1.1 × 10⁹ M☉ within 500 pc, against an observed ~10⁹ M☉ (McGaugh et al. 2010).
- **Tully–Fisher law (2012).** [McCulloch 2012, Ap&SS](../01-papers/2012-mcculloch-galactic-scales/README.md) assumes that the local "jitter" acceleration a′ at a galaxy's edge sits at the minimum 2c²/Θ. That gives

  $$ v^4 = \frac{2GMc^2}{\Theta}, \qquad \frac{2c^2}{\Theta} = 6.7 \pm 0.6 \times 10^{-10}\ \mathrm{m\,s^{-2}} \quad (\Theta = 2.7\times10^{26}\ \mathrm{m}) $$

  - The paper reports agreement "within error bars", but QI overpredicts velocities by up to 44% for dwarfs, 30–54% for spirals and 3–38% for clusters.
  - In the paper's words: "MoND performs better for spirals and MiHsC performs better for galaxy clusters."
- **RAR (2017).** [McCulloch 2017, Ap&SS](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md), now with Θ = 8.8 × 10²⁶ m (present co-moving diameter), so 2c²/Θ ≈ 2.0 × 10⁻¹⁰ m s⁻²:

  $$ a_{pred} = a_{bar}\sqrt{1 + \frac{2c^2}{a_{bar}\Theta}}, \qquad v^4 = \frac{2GMc^2(1+z)}{\Theta_{now}} $$

  - The curve lies on binned SPARC data "within the error bars". No χ² or RMS statistic is given.
  - **Redshift prediction:** the mass at fixed rotation speed should change by −0.28 dex at z = 0.9 (observed −0.38 to −0.47) and −0.52 dex at z = 2.3 (observed −0.2 to −0.47).
  - For the Genzel galaxies, QI accelerations are 9–19% above observed for the four lower-z galaxies, and agreement "is worse" for the two highest-z galaxies.
- **Further derivations** reach the same formula by other routes: information theory ([2020-mcculloch-information-theory](../01-papers/2020-mcculloch-information-theory/README.md)) and a cosmic resonant cavity ([Pickering 2017](../01-papers/2017-pickering-resonant-cavity/README.md)). Pickering, an independent author in a small journal, uses Θ = 4.3 × 10²⁶ m and a minimum acceleration of 4.18 × 10⁻¹⁰ m s⁻².

## Independent tests, critiques and null results
- **Θ differs between versions.** It is 2.6–2.7 × 10²⁶ m in 2007–2012, 4.3 × 10²⁶ m in Pickering 2017, and 8.8 × 10²⁶ m from 2017 on. The 2017 SPARC paper notes the change itself. Because the predicted scale is 2c²/Θ, this choice moves the prediction by a factor of ~3.4. Each version needs to be tested using its stated cosmological definition. The change alone does not show that Θ was fitted to galaxy data (see Criticisms in the [SPARC paper README](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)).
- **Same deep limit as MOND.** The QI RAR shares MOND's low-acceleration limit, with an effective a₀ = 2c²/Θ ≈ 2.0 × 10⁻¹⁰ m s⁻², versus the fitted 1.2 × 10⁻¹⁰ m s⁻². In the deep-MOND regime it predicts accelerations about 30% higher, which is visible in the lowest SPARC bins (editorial observation in the README). McCulloch & Lucio (2019) note that MOND with a₀ = 2 × 10⁻¹⁰ m s⁻² is "practically equivalent to QI".
- **Redshift evolution is not unique to QI.** Milgrom noted a₀ ≈ cH₀/2π and discussed a time-varying a₀.
- **Haug 2021** ([2021-haug-minimum-acceleration](../01-papers/2021-haug-minimum-acceleration/README.md)) plots QI on 2,793 SPARC points just below MOND, which "fits the observations very well". This is a visual comparison only, and Haug's own g_min is a different quantity.
- **Renda 2019** ([2019-renda-sceptical](../03-criticism/2019-renda-sceptical/README.md)) reports that his reconstruction of the discrete Unruh-spectrum sum gives a non-linear F(a) with a peak F ≈ 2.17 near 1.2 × 10⁻⁹ m s⁻². Adopting that reconstruction would change the early spectral model; it is not the galaxy equation used in A1/A1b. Renda does not test data. McCulloch points to later derivations of the same inertia law in his [2026 response](https://physicsfromtheedge.blogspot.com/2026/08/responding-to-criticisms.html); these require separate assessment. Junghanns 2026 (preprint) argues that this peak comes from a mode-counting error: with electromagnetic polarisation counted correctly, F(a) rises monotonically to 1 ([2026-junghanns-causal-restriction-nogo](../03-criticism/2026-junghanns-causal-restriction-nogo/README.md)).
- **Wide binaries.** Banik et al. 2024 state that the wide-binary data "falsify" QI's asymptotically flat-velocity prediction ([wide-binaries](wide-binaries.md)). This is relevant because the same formula is used.
- **No Tully–Fisher evolution to z ≈ 2.5** (McGaugh 2025 blog, drawing on McGaugh et al. 2024, ApJ 976, 13, and the RC100 data of Nestor Shachar et al. 2023; [2025-mcgaugh-kinematics-high-redshift](../07-media/2025-mcgaugh-kinematics-high-redshift/README.md)): McGaugh sees "no perceptible evolution" and says this excludes a₀ evolving with H(z). He does not mention QI. Editorial check (in the README): QI's 2017 Θ₀/(1+z) prescription implies about −0.54 dex at z = 2.5, comparable to the case McGaugh calls excluded, and this sits uneasily with the Übler 2017 evolution McCulloch cited. McCulloch replied on his blog (2026).
- **Urueña Palomo 2025** (blog; [2025-uruena-problems-quantized-inertia](../07-media/2025-uruena-problems-quantized-inertia/README.md)): argues that QI's evolving a₀ is ruled out by McGaugh's result (his inference; McGaugh does not name QI), that QI lacks MOND's external-field effect, and that it does not derive MOND. The author proposes a rival "Machian MOND".
- No independent group has fitted QI to SPARC or to rotation curves with a published goodness-of-fit statistic.
- **Our own refits (editorial, not peer-reviewed): [A1](../09-analysis/a1-sparc-rar-refit/README.md) and [A1b](../09-analysis/a1b-sparc-per-galaxy/README.md).** A1 fits the stacked RAR; A1b fits individual rotation curves with distance, inclination and Υ★ priors. Both favor a free scale under their tested assumptions, with baseline Θ ≈ 1.2–1.4 × 10²⁷ m. The A1 low-acceleration offset for Θ = 8.8 × 10²⁶ m is 17–32% in acceleration (about 8–15% in velocity at fixed radius).
- **Our binned redshift test (editorial): [A6](../09-analysis/a6-rar-redshift-evolution/README.md).** It converts QI's scale into MUSE-DARK's convention and compares it with the four binned values. Under its approximate curve conversion, the published prediction (Θ₀ = 8.8 × 10²⁶ m, (1+z)) is 28–45% above every bin. A single −0.11 dex baryonic-mass shift removes most of that offset in the synthetic-curve check. The printed (1+z) shape fits best of the laws tested when the amplitude is free, and A1's SPARC-calibrated scale evolved with (1+z) agrees without refitting. These results use four digitized points whose bar convention is unstated.
- **MUSE-DARK per galaxy (editorial): [A6b](../09-analysis/a6b-musedark-per-galaxy/README.md).** Rebuilding the galaxies from public fit parameters, the rise depends on the mass budget, as [Karpov 2026](../01-papers/2026-karpov-musedark-a0z-audit/README.md) (preprint) found. With the survey's dynamical masses the best-fit QI scale rises faster than (1+z); SED masses give a weaker, poorly constrained rise that depends on the radial grid. The revised SED budgets conserve total stellar mass when a bulge is present. The radial sampling also changes the result, so these public products cannot decide the question.
- **RC100 at z = 0.6–2.5 (editorial): [A6c](../09-analysis/a6c-rc100-qi/README.md).** Using the dark-matter fractions of [Nestor Shachar et al. 2023](../01-papers/2023-nestorshachar-rc100-rotation-curves/README.md), following [Sentina 2026](../01-papers/2026-sentina-a0z-rc100/README.md) (preprint), QI's published law fits worse (Δ(−ln L) = +42.4 against a constant scale) under the approximate likelihood, now including the journal's radius and velocity errors. The (1+z) shape with free amplitude also fits worse (+6.1; fitted exponent −0.56). The ranking survives the tested error correlations. These are conditional comparisons of halo-based decompositions, not calibrated exclusion significances; most of the leverage comes from z ≈ 2.
- **McCulloch's own 2017 high-z comparisons, reproduced (editorial): [A6d](../09-analysis/a6d-mcculloch-2017-highz/README.md).** His Genzel comparison reproduces approximately, but five of the six galaxies lie below the "minimum acceleration" he compares them with, and his Eq. 8 overpredicts all six by 23–49%. [Übler et al. 2017](../01-papers/2017-ubler-tully-fisher-evolution/README.md)'s baryonic Tully–Fisher zero point rises by +0.17 ± 0.06 dex from z ≈ 0.9 to 2.3, where QI predicts −0.24 dex.
- **Halo-independent baryons (editorial): [A6e](../09-analysis/a6e-sharma-qi/README.md).** With the 263 discs of [Sharma et al. 2025](../01-papers/2025-sharma-dark-matter-fraction/README.md), whose baryonic masses come from photometry and gas scalings, the published normalization requires baryonic masses about 0.3 dex lower, comparable to the gas-scaling uncertainty. Survey offsets (a factor of 2.4 at the same redshift) exceed any redshift trend; within KMOS3D the (1+z) shape is mildly disfavoured.
- **z ≈ 4.5 (editorial): [A6f](../09-analysis/a6f-rizzo-z45-qi/README.md).** Six ALMA discs ([Rizzo et al. 2020](../01-papers/2020-rizzo-cold-disc-early/README.md), [2021](../01-papers/2021-rizzo-dsfg-dynamics/README.md)) imply a QI scale of about 0.33 times the published prediction, a rise of 1.8× over QI's z = 0 value against a predicted 5.5×. The galaxies scatter more than their errors allow for a single scale.
- **MUSE-DARK without a halo:** the authors' MOND-framework refit, converted to QI's convention in [A6](../09-analysis/a6-rar-redshift-evolution/README.md), gives the (1+z) shape (γ = 1.02) at 0.66 times the published normalization. This is the most theory-consistent MUSE-DARK result and is favourable to QI's shape.
- **Limits of that editorial comparison.** A1's point-level likelihood approximates correlated errors. A1b reports Q = velocity χ² + prior penalty, not BIC, and includes full velocity-error and prior-width sensitivity refits, method-specific distance diagnostics and galaxy-influence checks. The scores and galaxy bootstraps are conditional on the error and prior assumptions, not calibrated exclusion significances. Full calculations and interpretation are in the analysis folders.

## Assessment
QI reproduces the general shape of the baryonic Tully–Fisher relation and the RAR from visible mass alone. It does so with a MOND-like formula whose acceleration scale, 2c²/Θ, is set by a cosmic length rather than fitted. That is an interesting coincidence, shared by several independent horizon-based ideas. The author's 2017 comparison is visual, with binned data displayed using RMS scatter. The value of Θ has changed between papers by a factor of about 3, and the early version overpredicted spiral velocities by 30–54%. The later version predicts deep-MOND accelerations about 30% above the data. The predicted change with redshift is distinctive. Reproducing the 2017 high-z comparisons ([A6d](../09-analysis/a6d-mcculloch-2017-highz/README.md)) shows that, once his Eq. 8 and Übler's baryonic numbers are used, those sources do not support it. The observers themselves read those data within ΛCDM. No independent quantitative test of QI's rotation-curve predictions exists in the sources, so the claim rests on McCulloch's own comparisons. Our editorial refits ([A1](../09-analysis/a1-sparc-rar-refit/README.md), [A1b](../09-analysis/a1b-sparc-per-galaxy/README.md)) identify a normalization tension under the assumptions tested: a freely fitted Θ is preferred, at ≈ 1.4–1.6 times the 2017 value. A1 also reconstructs the visual comparison from SPARC's public binned table: the published curve lies within one tabulated scatter of all 14 means. This is consistent with the author's visual claim; identity with his privately supplied bins remains unverified. The additional likelihood tests study offsets from means and do not establish model-independent exclusion of QI. Our binned test against MUSE-DARK ([A6](../09-analysis/a6-rar-redshift-evolution/README.md)) finds the same pattern at z ≈ 0.5–1.3: the direction and approximate rate of the predicted (1+z) rise agree with the data, while the published normalization is 28–45% too high under the assumed curve conversion and survey mass scale. Two further tests qualify the case for the predicted rise: SED masses weaken the MUSE-DARK trend but leave broad ranges compatible with both no evolution and (1+z) ([A6b](../09-analysis/a6b-musedark-per-galaxy/README.md)), and the RC100 sample at z = 0.6–2.5 prefers a constant scale over (1+z) under the tested decomposition and error assumptions ([A6c](../09-analysis/a6c-rc100-qi/README.md)). Across all the high-z tests, the published normalization is too high: by 0.3 dex in halo-independent masses (A6e, within their systematics) and by about a factor of 3 at z ≈ 4.5 (A6f). The shape evidence is split: MUSE-DARK's halo-free refit gives (1+z), while RC100, KMOS3D alone and the z ≈ 4.5 discs rise more slowly.

## Sources
- [2010-mcculloch-minimum-accelerations](../01-papers/2010-mcculloch-minimum-accelerations/README.md)
- [2012-mcculloch-galactic-scales](../01-papers/2012-mcculloch-galactic-scales/README.md)
- [2017-mcculloch-galaxy-rotations-sparc](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)
- [2017-pickering-resonant-cavity](../01-papers/2017-pickering-resonant-cavity/README.md)
- [2020-mcculloch-information-theory](../01-papers/2020-mcculloch-information-theory/README.md)
- [2017-smolin-mond-quantum-gravity](../01-papers/2017-smolin-mond-quantum-gravity/README.md)
- [2019-cadoni-long-range-qg](../01-papers/2019-cadoni-long-range-qg/README.md)
- [2018-hernandez-bounding-curvature](../01-papers/2018-hernandez-bounding-curvature/README.md)
- [2021-haug-minimum-acceleration](../01-papers/2021-haug-minimum-acceleration/README.md)
- [2019-renda-sceptical](../03-criticism/2019-renda-sceptical/README.md)
- [2026-junghanns-causal-restriction-nogo](../03-criticism/2026-junghanns-causal-restriction-nogo/README.md)
- [2025-mcgaugh-kinematics-high-redshift](../07-media/2025-mcgaugh-kinematics-high-redshift/README.md)
- [2026-ciocan-muse-dark-rar](../01-papers/2026-ciocan-muse-dark-rar/README.md)
- [2026-alcock-rar-scale-hubble](../01-papers/2026-alcock-rar-scale-hubble/README.md)
- [2026-karpov-musedark-a0z-audit](../01-papers/2026-karpov-musedark-a0z-audit/README.md)
- [2026-sentina-a0z-rc100](../01-papers/2026-sentina-a0z-rc100/README.md)
- [2023-nestorshachar-rc100-rotation-curves](../01-papers/2023-nestorshachar-rc100-rotation-curves/README.md)
- [2017-genzel-baryon-dominated-discs](../01-papers/2017-genzel-baryon-dominated-discs/README.md)
- [2017-ubler-tully-fisher-evolution](../01-papers/2017-ubler-tully-fisher-evolution/README.md)
- [2025-sharma-dark-matter-fraction](../01-papers/2025-sharma-dark-matter-fraction/README.md)
- [2020-rizzo-cold-disc-early](../01-papers/2020-rizzo-cold-disc-early/README.md)
- [2021-rizzo-dsfg-dynamics](../01-papers/2021-rizzo-dsfg-dynamics/README.md)
- [2025-uruena-problems-quantized-inertia](../07-media/2025-uruena-problems-quantized-inertia/README.md)
- [2012-physorg-dark-matter-inertia](../07-media/2012-physorg-dark-matter-inertia/README.md) (press)
- [2023-banik-gaia-dr3-wide-binaries](../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md)
- [2018-mcculloch-dark-matter-scitrends](../07-media/2018-mcculloch-dark-matter-scitrends/README.md)
- Related evidence: [dwarf-galaxies](dwarf-galaxies.md), [wide-binaries](wide-binaries.md), [globular-clusters](globular-clusters.md), [cosmology](cosmology.md), [derivation](derivation.md)
