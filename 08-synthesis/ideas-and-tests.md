---
title: "Ideas: analyses we could run and tests that would decide"
tags: [synthesis, ideas, predictions]
as_of: 2026-10-19
---

# What we can come up with: analyses and decisive tests

> **Editorial.** These are proposals, not results. Items marked 🔧 are analyses this repository could carry out with public data. Items marked 🔬 need new observations or experiments.

## A. Analyses we could do ourselves

### 🔧 A1. Fixed-Θ refit of the SPARC radial acceleration relation
Take the public [SPARC](http://astroweb.cwru.edu/SPARC/) RAR (153 galaxies, ~2700 points) and fit:
- QI with Θ = 2.6 × 10²⁶ m (fixed, early papers)
- QI with Θ = 8.8 × 10²⁶ m (fixed, 2017 on)
- QI with Θ free
- MOND (simple and standard μ, a₀ free)

Compare χ² / BIC. This settles in numbers whether QI's "no free parameter" fit is competitive, and how much the choice of Θ matters. McCulloch 2017 showed agreement only by eye ([source](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)). This could be a short Python notebook in a new `09-analysis/` folder.

> **Status (2026-10-19): done at the RAR level** → [09-analysis/a1-sparc-rar-refit](../09-analysis/a1-sparc-rar-refit/README.md). Θ = 2.6 × 10²⁶ m is excluded. Θ = 8.8 × 10²⁶ m over-predicts by 17–32% below g_bar ≈ 10⁻¹¹ m s⁻² (ΔBIC +490 vs MOND simple; galaxy bootstrap +343 to +671). The best Θ is ≈ 1.23 × 10²⁷ m, and even then the QI function is slightly worse than MOND simple (ΔBIC +73, not decisive given Υ★ systematics). **A1b done** → [per-galaxy fits](../09-analysis/a1b-sparc-per-galaxy/README.md). Each galaxy gets its own distance, inclination and Υ★ (Li et al. 2018 style). Fixed Θ = 8.8 × 10²⁶ m remains ΔBIC +1,195 behind MOND simple (+225 after rescaling for underestimated velocity errors), and it is only reached by pulling a third of galaxies > 20% closer. The best Θ is ≈ 1.37 × 10²⁷ m.

### 🔧 A2. Renda-corrected F(a) applied to galaxies
Renda (2019) gives the proper discrete-spectrum F(a), which peaks at ≈ 2.17 near 1.2 × 10⁻⁹ m s⁻² ([source](../03-criticism/2019-renda-sceptical/README.md)). Feed that F(a) into the rotation-curve formula and see whether "corrected QI" still fits the RAR. If it does not, the galaxy fits depend on the flawed step.

### 🔧 A3. Thrust-prediction ledger
Make a table of every quantitative QI thrust prediction: EmDrive, laser resonators, fibre loops, capacitors, IVO. For each, list the prediction, the measured upper limit and the ratio. The data are already in [propulsion](../02-evidence/propulsion.md) and the 03-criticism READMEs. A log-scale chart would show where QI has been tested and where it hasn't.

### 🔧 A4. Wide-binary external-field-effect discriminator
QI predicts **no external field effect**; MOND predicts one. Using Gaia DR3 wide-binary samples (Chae / Banik public catalogues), split binaries by the Galactic field they sit in and check whether the anomaly (if any) depends on it. This is a test that could separate QI from MOND rather than just from Newton.

### 🔧 A5. Θ-sensitivity audit of every paper
For each QI paper, recompute the headline number with both Θ values. This shows which "successes" hold under one consistent choice ([equations §6–7](../00-overview/equations.md)).

## B. Decisive observations and experiments

| # | Test | What QI predicts | What a null means |
|---|---|---|---|
| 🔬 B1 | High-z rotation curves (JWST/ALMA, z ~ 1–3) | a₀ ∝ (1+z): stronger "missing mass" at high z | A constant a₀ would argue against QI's horizon mechanism |
| 🔬 B2 | Gaia DR4 wide binaries | Flat Δv beyond ~7000 AU, independent of the external field | Newtonian behaviour (Banik) or EFE-dependent behaviour (MOND) would both disfavour QI |
| 🔬 B3 | Independent orbital test of a QI thruster with published telemetry | Measurable orbit raising / reduced decay | Further null data |
| 🔬 B4 | Low-acceleration torsion pendulum / free-fall at a ≲ 10⁻¹⁰ m s⁻² (e.g. in space) | Inertial mass deviates from gravitational mass | Constrains QI directly, independent of astrophysical modelling |
| 🔬 B5 | Lensing in the Bullet Cluster / galaxy–galaxy lensing | Needs a relativistic QI that doesn't exist yet | — (theory must come first) |
| 🔬 B6 | Unruh-radiation detection (analogue or accelerator-based) | Required ingredient; anisotropy is what matters | Absence would remove QI's mechanism, though not its phenomenology |

## D. Desk tests from the October 2026 review

> **Editorial.** This section comes from a review of the whole repository plus a literature and data search (19 Oct 2026). Every item can be carried out with public data or the published literature; none needs a laboratory. The brief was to find tests that could **move QI forward**. A test can do that only if it could also go against QI, so each item says what a QI-favourable result would look like and what would count against it. Identifiers were checked against arXiv, Crossref or the data provider on 19 Oct 2026 unless marked `[!UNVERIFIED]`. Arithmetic marked "editorial check" is ours.

### D0. Ranking at a glance

| Rank | ID | Test | Why it could help QI | Chance of a QI-favourable result | Effort |
|---|---|---|---|---|---|
| 1 | A6 | Redshift evolution of the acceleration scale (MUSE-DARK III, Genzel) | It is QI's only *distinctive* galaxy prediction (a scale tied to the horizon); standard MOND predicts no evolution | **Good**: new 2026 data already show a rising scale | Days |
| 2 | A8 | Wide binaries binned by internal acceleration (Gaia DR4, 2 Dec 2026) | No external field effect means the boost keeps growing at low acceleration; MOND levels off | Uncertain: the field is split | Weeks |
| 3 | A12 | Does the SPARC external-field signal survive? | QI predicts **no** environment dependence; recent reanalyses find weak or no evidence for it | Moderate | Days |
| 4 | A13 | Isolated-vs-EFE dwarf and UDG population test | Coma UDGs prefer no EFE; several Milky Way and Andromeda dwarfs prefer EFE | Mixed | Days |
| 5 | A7 | Pre-registered Θ, then held-out tests | Converts a post-hoc coincidence into a real prediction | Unknown | Hours |
| 6 | A9 | Flyby formula applied to post-2013 flybys | The later nulls have never been checked against QI's own formula | Moderate | Days |
| 7 | A10 | Independent OTP-2 orbit-decay analysis | The only in-space QI thrust test; the data are public | Low (see below) | Days |
| 8 | A11 | Chae's inner/outer rotation-curve test with QI's own function | A direct test of "modified inertia" against "modified gravity" | Low to moderate | Days |
| 9 | A14 | Weak-lensing Tully–Fisher normalisation | Lensing reaches far lower accelerations than rotation curves | Uncertain; QI has no lensing theory | Hours |
| — | A15–A18 | Consistency checks QI must pass (Solar System, globular clusters, CMB, small items) | Needed before any positive result is persuasive | Mostly low | Hours each |

### Tier 1: tests with a real chance of a distinctive positive result

#### 🔧 A6. Does the acceleration scale grow with redshift, and how fast?
**Why it matters.** QI ties its scale to the cosmic horizon (a_Q = 2c²/Θ), so the scale must change over cosmic time. MOND's a₀ is a constant of nature. This is the clearest place where QI and MOND make different predictions for galaxies. It is the existing B1 idea, and it can now be done with published data rather than new observations.

**New data.** MUSE-DARK III (Ciocan, Bouché et al. 2026, *A&A* 709, L16, [arXiv:2604.22613](https://arxiv.org/abs/2604.22613), doi:10.1051/0004-6361/202659230) measures the radial acceleration relation for 79 galaxies at 0.33 < z < 1.44. It finds a₀(z ≈ 1) = 2.38 ± 0.1 × 10⁻¹⁰ m s⁻², a scale that "systematically increases with z", and a linear slope a₁ = 1.59 ± 0.1 × 10⁻¹⁰ m s⁻² per unit z. The authors report similar results when they model the data in MOND. They do not mention QI. Earlier constraints come from Genzel et al. 2020 ([arXiv:2006.03046](https://arxiv.org/abs/2006.03046)); Milgrom 2017 ([arXiv:1703.06110](https://arxiv.org/abs/1703.06110)) argues that the Genzel z ≈ 1–2.4 discs "all but exclude" a scale four times the local one at z ≈ 2.

**What each law predicts** (editorial check; the ratio of the scale at z to the scale today, using Planck 2018 parameters H₀ = 67.4, Ω_m = 0.315):

| z | MOND (constant a₀) | QI as printed, Θ ∝ 1/(1+z) ([2017](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)) | Scale ∝ H(z) (cH/2π variants) | Θ = proper particle-horizon diameter at that epoch |
|---|---|---|---|---|
| 0.5 | 1 | 1.50 | 1.32 | 1.74 |
| 1 | 1 | 2.00 | 1.79 | 2.63 |
| 2 | 1 | 3.00 | 3.03 | 4.80 |

The last column matters. McCulloch 2017 takes the **comoving** diameter (8.8 × 10²⁶ m) and divides by (1+z). But the comoving particle horizon was itself smaller in the past, so a horizon-set Θ shrinks faster than 1/(1+z). The two readings of QI separate clearly by z ≈ 1–2. This is a choice the theory has to make, and the data can make it.

**Editorial reading of the headline numbers.** Against the local a₀ ≈ 1.2 × 10⁻¹⁰, MUSE-DARK's z ≈ 1 value is a ratio of about 2.0. Against the paper's own fitted intercept the ratio is larger, about 2.4 `[!UNVERIFIED: intercept read from the paper body by a research agent, not from the abstract]`. Either way the scale rises, which standard MOND does not predict and QI does. The printed (1+z) law gives 2.0; the proper-horizon reading gives 2.6 at z = 1 but 4.8 at z = 2, where Milgrom's argument bites.

**The test.**
1. Download the MUSE-DARK rotation curves (data releases at dark.univ-lyon1.fr; check exactly what is served) and refit them with **QI's own function**, a = a_bar·√(1 + a_Q/a_bar), in redshift bins. The paper uses a different interpolating function, and our A1 refit showed that the QI scale and the McGaugh a₀ differ by about 1.3× locally.
2. Fit a_Q(z) = a_Q(0)·f(z) for each column of the table above, with a_Q(0) **fixed from SPARC** (A1/A1b, on the `analysis/a1-sparc-refit` branch), and compare.
3. Add the Genzel et al. 2020 z ≈ 1–2.4 sample as a high-z lever arm.

**QI-favourable result:** the scale rises at the rate of one of QI's two Θ(z) laws, starts from the SPARC value at z = 0, and stays consistent with Genzel at z ≈ 2. **Against QI:** the rise turns out to be a modelling artefact (the paper uses a dark-matter disc–halo decomposition, and ΛCDM simulations also predict some drift), or it follows neither law.

**Caveats.** The paper's a₀ is a fitted parameter of a disc–halo model, not a direct observable. A rising scale also fits some "a₀ ∝ cH" MOND variants, so success would not single out QI from every horizon-based model ([mond](../05-context/mond.md)). Junghanns 2026 already lists the competing Θ(t) prescriptions as untested ([source](../03-criticism/2026-junghanns-causal-restriction-nogo/README.md)).

#### 🔧 A7. Pre-register Θ, then test it on data it was not fitted to
**Why it matters.** The scorecard's main objection is that Θ was chosen after looking at the data. Our SPARC fits prefer a_Q ≈ 1.31–1.47 × 10⁻¹⁰ m s⁻², which is Θ ≈ 1.23–1.37 × 10²⁷ m, and neither published Θ.

**Editorial check (a coincidence, not a result).** With Planck 2018 parameters, the comoving particle-horizon radius is R_p = 4.37 × 10²⁶ m. Its diameter, 2R_p = 8.73 × 10²⁶ m, is QI's 2017 Θ. Its **half circumference**, πR_p = 1.371 × 10²⁷ m, gives a_Q = 1.31 × 10⁻¹⁰ m s⁻². That is the A1b per-galaxy best fit (Θ ≈ 1.37 × 10²⁷ m) almost exactly. McCulloch's 2020 derivation already uses horizon *half circumferences* for Δx ([2020](../01-papers/2020-mcculloch-horizon-widths/README.md)), but plugging that length in for Θ is not what the derivation does. Other standard lengths give 6.5 × 10⁻¹⁰ (2c/H₀), 5.7 × 10⁻¹⁰ (event-horizon diameter), 5.4 × 10⁻¹⁰ (de Sitter diameter) and 1.7 × 10⁻¹⁰ (de Sitter circumference).

**The test.** Write down one Θ, with its justification, **before** looking at new data. Then test that frozen value on samples it was not tuned to: the high-z data in A6, the lensing data in A14, the dwarfs in A13 and the wide binaries in A8. A coincidence found by searching a list of cosmological lengths is worth nothing on its own. A frozen value that then predicts held-out data would be the first genuinely parameter-free QI success.

#### 🔧 A8. Gaia DR4 wide binaries, binned by internal acceleration (upgrades B2)
**Timing.** ESA's Gaia archive reopens with **DR4 on 2 Dec 2026**: 66 months of data and the first epoch astrometry. Epoch astrometry can reveal hidden third stars, the main systematic in the debate.

**State of play** (all checked on arXiv):
- Anomaly found: Chae et al. 2026, γ = G_eff/G = 1.60 (+0.24/−0.14) from 36 binaries with full 3D velocities ([arXiv:2601.21728](https://arxiv.org/abs/2601.21728)). The authors say this exceeds what MOND predicts.
- No anomaly: Saad & Ting 2026 reanalyse the same 36 pairs and get γ = 1.00 (+0.24/−0.19) ([arXiv:2603.11015](https://arxiv.org/abs/2603.11015)). Their C3PO radial-velocity sample also disfavours standard a₀ ([arXiv:2512.19652](https://arxiv.org/abs/2512.19652)).
- Also Newtonian: Banik et al. 2024 ([arXiv:2311.03436](https://arxiv.org/abs/2311.03436)) and Pittordis, Sutherland & Shepherd 2025 ([arXiv:2504.07569](https://arxiv.org/abs/2504.07569)).
- Pittordis & Sutherland 2019 found MOND-like theories **without** an external field effect "strongly inconsistent" with Gaia DR2. That is a direct strike against QI, which the repo already records ([wide-binaries](../02-evidence/wide-binaries.md)).

**The QI-specific test.** Bin the velocity boost by *internal* acceleration. With the Milky Way's field near 1.8 a₀ at the Sun, MOND with EFE predicts a boost that levels off near γ ≈ 1.4. QI (no EFE) predicts a boost that **keeps growing** below ~10⁻¹⁰·⁵ m s⁻². Chae's γ = 1.6 "exceeding MOND" is the kind of result QI needs, but it is disputed. **QI-favourable:** after triples are removed with DR4 epoch astrometry, the boost keeps rising. **Against:** γ = 1 (Newton) or a plateau (MOND with EFE).

### Tier 2: tests that separate QI from MOND (QI could win or lose)

#### 🔧 A12. Is the "external field effect" in SPARC real?
QI's sharpest qualitative difference from MOND is that it has **no** external field effect. Chae et al. 2020 ([arXiv:2009.11525](https://arxiv.org/abs/2009.11525)) reported the EFE in SPARC rotation curves at high significance, with per-galaxy field estimates in Chae et al. 2021 (ApJ 921, 104). Later work is more sceptical: Desmond 2023 (MNRAS 526, 3342) finds only weak evidence, Stiskalek & Desmond 2023 find the external field adds no predictive power, and Paranjape & Sheth (MNRAS, 2022) argue that ΛCDM gives a similar signal with the opposite sign `[!UNVERIFIED: these three identifiers come from a research agent and were not re-checked]`.

**Test.** Using our A1b per-galaxy fits, correlate the outer-curve residuals of QI and MOND with each galaxy's environmental field. QI predicts **zero** correlation, MOND a negative one, ΛCDM the opposite sign. **QI-favourable:** a null correlation, especially in the cleanest isolated subsample. Chae 2021's Appendix B tables may need transcribing.

#### 🔧 A13. Population test of dwarfs and ultra-diffuse galaxies: isolated or EFE?
QI predicts every dwarf behaves as if isolated. Editorial check: in deep-MOND scaling, QI's dispersion is about the isolated MOND value × (a_Q/a₀)^¼, which is ×1.14 for a_Q = 2.04 × 10⁻¹⁰ (Θ = 8.8 × 10²⁶ m) and ×1.02 for the A1b value.

| System | Observed σ (km s⁻¹) | MOND isolated | MOND with EFE | Direction for QI | Source |
|---|---|---|---|---|---|
| Coma cluster UDGs | — | fits | fit "seriously deteriorates" | **favours QI** | Freundlich et al. 2022 ([arXiv:2109.04487](https://arxiv.org/abs/2109.04487)) |
| Antlia 2 | ≈ 5.7–6.0 | — | 2.8 | leans to QI, but tides confound it | Ji et al. 2021 `[!UNVERIFIED]` |
| Crater II | 2.7 ± 0.3 | ≈ 4 | 2.1 (predicted beforehand) | against QI | McGaugh 2016 ([arXiv:1610.06189](https://arxiv.org/abs/1610.06189)) |
| NGC 1052-DF2 / DF4 | ≈ 8.5 / 4.2 | ≈ 20 / 18.6 | consistent | against QI (distance disputed) | Famaey et al. 2018; Haghi et al. 2019 `[!UNVERIFIED]` |
| Andromeda dwarfs (≈ 13 systems) | table | table | table | mixed | McGaugh & Milgrom 2013 ([arXiv:1308.5894](https://arxiv.org/abs/1308.5894)) |

**Test.** Compute one joint χ² for QI-as-isolated across all of them, not object by object. **QI-favourable:** the population as a whole prefers no EFE (Freundlich's result generalises). **Against:** Crater II-type systems dominate. This also refreshes the 2017 dwarf comparison with the revised Tri II and Boo II data ([dwarf-galaxies](../02-evidence/dwarf-galaxies.md)).

#### 🔧 A11. Chae's inner/outer test, rerun with QI's own function
Chae 2022 ([arXiv:2207.11069](https://arxiv.org/abs/2207.11069)) finds that the inner (rising) and outer (flat) parts of SPARC rotation curves sit differently on the acceleration plane, a 6.9σ difference he calls "inconsistent with current proposals of modified inertia". QI is a modified-inertia theory with a one-curve algebraic relation, so this applies to it directly. But Chae's residuals are taken relative to MOND's *simple* function, not QI's. **Test:** rerun the split with QI's function using the A1b code. **QI-favourable:** the offset shrinks to insignificance. This is the riskiest Tier 2 test, and it is the one QI most needs to pass to stay viable as *inertia*.

#### 🔧 A14. Weak-lensing Tully–Fisher normalisation
Mistele et al. 2024 ([arXiv:2406.09685](https://arxiv.org/abs/2406.09685)) find lensing circular speeds flat out to ~1 Mpc, with a lensing baryonic Tully–Fisher relation (machine-readable tables) that matches the kinematic one. Brouwer et al. 2021 ([arXiv:2106.11677](https://arxiv.org/abs/2106.11677)) extend the RAR to lower accelerations. McCulloch's blog (6 Oct 2026) cites the flatness as qualitative support. **Test:** fit V⁴ = G M a_Q to the lensing BTFR. a_Q = 2.04 × 10⁻¹⁰ and MOND's 1.2 × 10⁻¹⁰ differ by 0.23 dex in mass at fixed V. **Caveat:** QI has no lensing theory, so this assumes light traces the same dynamical mass (open question 6).

#### 🔧 A9. QI's flyby formula on the post-2013 flybys
The repository records Juno (2013), Rosetta II/III and BepiColombo (2020) as nulls, but no one has computed **QI's** prediction for them. Only EPOXI is a recorded failure ([flyby-anomaly](../02-evidence/flyby-anomaly.md)). The inbound and outbound geometry for Juno, BepiColombo, Solar Orbiter (Nov 2021, 454 km altitude), Lucy and JUICE can be derived from JPL Horizons. The Rosetta **Mars** flyby (2007), which McCulloch predicted would show about twice Earth's anomaly, is untested rather than refuted: Budnik & Morley (ISSFD 2007) saw "no anomalous Δv" but had no two-way tracking near pericentre `[!UNVERIFIED: read via research agent]`.
**Test:** compute the 2008 and "spinning Earth" predictions for each flyby, alongside Anderson's formula and zero. **QI-favourable:** QI predicts sub-error-bar Δv where Anderson predicts a detectable one. **Against:** QI predicts a detectable Δv that wasn't seen. A related 2026 paper attributes the Rosetta I anomaly to outgassing (Hoffmann & Budnik, [arXiv:2609.23482](https://arxiv.org/abs/2609.23482)).

#### 🔧 A10. Independent analysis of the OTP-2 orbit (upgrades B3)
McCulloch's own analysis is on his blog ("A Tale of Two Satellites", 30 Jan 2026). OTP-2 (NORAD 63235) lost 4.88 km from 30 Sep to 30 Dec 2025 against 5.48 km for its comparison satellite, AeroCube 18A (NORAD 63220). He predicted about 5 m/day of relative rise under assumed burn times.
**Editorial check (CelesTrak elements, 19 Oct 2026):** mean altitudes are now OTP-2 489.4 km, AeroCube 18A 488.7 km and its twin AeroCube 18B (NORAD 63222) 489.0 km. If McCulloch's altitudes use the same definition, OTP-2's lead over 18A has fallen from 1.9 km to 0.7 km since December, so it has decayed *faster*. OTP-2's drag term B* is also about 15% higher than both AeroCubes.
**Test:** pull the full element history (free Space-Track account, `gp_history`) for OTP-2, both AeroCubes and about ten Transporter-13 neighbours at 488–498 km. Fit drag-normalised decay rates against space weather (CelesTrak SW-All). Use the 18A–18B pair as the empirical noise floor. **QI-favourable:** OTP-2's residual exceeds the twin scatter during operation and vanishes when the drive stops. **Limits:** CubeSat attitude changes drag by up to 2–3×, and without IVO's drive-on log the result will stay ambiguous. Asking IVO for that log is worth more than any amount of fitting.

### Tier 3: consistency checks QI must pass

These are not where QI is likely to gain. But a positive galaxy-scale result will not persuade anyone while they are open, so stating QI's answer to each is itself progress.

- **🔧 A15. Solar System ephemerides.** Taken literally, the 2010 orbit equation adds a constant ~2 × 10⁻¹⁰ m s⁻² sunward (Θ = 8.8 × 10²⁶ m; 6.9 × 10⁻¹⁰ with 2.6 × 10²⁶ m). Planetary ephemerides bound any constant extra acceleration to ≲ 10⁻¹⁴ m s⁻² at Saturn and ≲ 10⁻¹⁵ at Mars (Iorio 2011, [arXiv:1012.0226](https://arxiv.org/abs/1012.0226)), and Cassini now bounds MOND-like effects tightly (Park et al. 2026, *PRD* 114, 024066, [arXiv:2602.17884](https://arxiv.org/abs/2602.17884)). The editorial check is a gap of 10⁴–10⁵. QI's escape is that bound orbits are exempt ([pioneer-anomaly](../02-evidence/pioneer-anomaly.md)). **The test is to state that exemption as a formula** and check that it still allows the galaxy effect, the wide-binary effect and the JuMBO prediction. If one formula does all of this, it is real progress for QI.
- **🔧 A16. Outer-halo globular clusters (the first QI globular-cluster prediction).** Pal 14 has σ = 0.38 ± 0.12 km s⁻¹ (Jordi et al. 2009, [arXiv:0903.4448](https://arxiv.org/abs/0903.4448)). Editorial check: QI as deep MOND without EFE gives roughly 2 km s⁻¹ for an assumed 1–2 × 10⁴ M☉. Repeat this for Pal 4, NGC 2419 and the Baumgardt catalogue (public, with dispersion profiles). It fills the gap in [globular-clusters](../02-evidence/globular-clusters.md). QI will probably fail unless its bound-system rule (A15) also suppresses the effect here, which would at least make the rule testable.
- **🔧 A17. The low-ℓ CMB deficit.** The 2014 toy model predicts 5.5% less power at ℓ < 40 ([2014](../01-papers/2014-mcculloch-toy-cosmology/README.md)). It was compared with Planck 2013's 5–10% deficit at 2.5–3σ ([arXiv:1303.5075](https://arxiv.org/abs/1303.5075)). Planck 2018 finds "no strong evidence for an amplitude mismatch" once the optical depth is better constrained ([arXiv:1807.06209](https://arxiv.org/abs/1807.06209), §6.1). **Test:** run the public Planck 2018 low-ℓ TT likelihood with a fixed 0.945 amplitude against 1. **QI-favourable:** Δχ² prefers 0.945.
- **🔧 A18. Quick literature checks** (an hour or so each):
  - Proxima: refit with the real eccentric orbit (Kervella et al. 2017, e ≈ 0.50, bound in Newtonian dynamics, [arXiv:1611.03495](https://arxiv.org/abs/1611.03495)) rather than a circular one.
  - Giné & Luciano 2024's Λ = 2H₀²/c² against Planck's 3Ω_Λ ≈ 2.06 ([source](../01-papers/2024-gine-luciano-discretization-lambda/README.md)).
  - Haug's g_min = 5.18 × 10⁻¹¹ and the Giné–Luciano quadratic variant as extra models in the A1 refit.
  - M87 jet: whether published jet angles make the 2019 superluminal argument unnecessary `[!UNVERIFIED]`.
  - McCulloch's blog prediction for the gas cloud AC G185.0-11.5 (44.5 ± 14.5 against 42.2 ± 2 km s⁻¹, 22 May 2025): find the primary measurement.

### New sources to add (found during the review)
- Ciocan, Bouché et al. 2026, MUSE-DARK III (A&A 709, L16): central to A6.
- Chae 2022 (ApJ 941, 55): the strongest published test of modified inertia as a class (A11).
- Gillot 2026, "Quantum modified inertia: application to galaxy rotation curves" (*EPJC* 86, 846, doi:10.1140/epjc/s10052-026-16000-8): an independent, related bounded-acceleration model, not QI itself.
- Mistele et al. 2024 (lensing BTFR), Freundlich et al. 2022 (Coma UDGs), Saad & Ting 2026 and Chae et al. 2026 (wide binaries), Park et al. 2026 (Cassini).
- McCulloch blog posts with numbers: "A Tale of Two Satellites" (30 Jan 2026), the AC G185.0-11.5 prediction (22 May 2025), weak lensing (6 Oct 2026).

## C. Suggested next steps for this repository
1. ~~Build `09-analysis/` with A1 (SPARC refit) as the first notebook.~~ Done: [A1](../09-analysis/a1-sparc-rar-refit/README.md). [A1b](../09-analysis/a1b-sparc-per-galaxy/README.md) (per-galaxy fits) also done. Next: A2 (Renda-corrected F(a)), which can reuse both scripts.
2. Ask McCulloch (via the blog) for the IVO OTP-2 telemetry and the Alcalá DARPA results.
3. Track new papers: set up a recurring check of arXiv for "quantised inertia" / "MiHsC", and new posts on physicsfromtheedge.blogspot.com.
4. Do A6 (redshift evolution) next. It is QI's most distinctive galaxy prediction, the data are new, and it reuses the A1/A1b code. Freeze Θ first (A7).
5. Prepare A8 now so it can run on Gaia DR4 when it appears on 2 Dec 2026.
6. Ask IVO (as well as McCulloch) for the OTP-2 drive-on log. Without it, A10 cannot be decisive.
