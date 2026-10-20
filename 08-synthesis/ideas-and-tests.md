---
title: "Ideas: analyses we could run and tests that would decide"
tags: [synthesis, ideas, predictions]
as_of: 2026-10-18
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

## C. Suggested next steps for this repository
1. ~~Build `09-analysis/` with A1 (SPARC refit) as the first notebook.~~ Done: [A1](../09-analysis/a1-sparc-rar-refit/README.md). [A1b](../09-analysis/a1b-sparc-per-galaxy/README.md) (per-galaxy fits) also done. Next: A2 (Renda-corrected F(a)), which can reuse both scripts.
2. Ask McCulloch (via the blog) for the IVO OTP-2 telemetry and the Alcalá DARPA results.
3. Track new papers: set up a recurring check of arXiv for "quantised inertia" / "MiHsC", and new posts on physicsfromtheedge.blogspot.com.
