# 09-analysis: our own calculations

> **Editorial.** Reproducible analyses carried out for this repository with public data. They are proposed in [ideas-and-tests](../08-synthesis/ideas-and-tests.md). They are our own work, not published results, and each one states its method, caveats and how to rerun it.

Each analysis is a folder holding a `README.md` (question, bottom line, method, results, caveats), a Python script (A1 needs only the standard library; later analyses use numpy and scipy, see [requirements.txt](requirements.txt)) and a `results/` folder of generated tables, JSON and SVG figures. Third-party input data are downloaded by the script into a git-ignored `data/` folder; they are not redistributed.

A1 and A1b implement McCulloch's 2017 Eq. 8. The older-Θ run is a scale-sensitivity experiment within that equation. A1 now includes a public-bin reconstruction: the published curve lies within one tabulated scatter of all 14 bin means. Identity with his privately supplied bins remains unverified. Likelihood diagnostics extend that visual comparison; A1b adds four prior-width scenarios and galaxy-influence checks.

| ID | Analysis | Data | Status | Bottom line |
|---|---|---|---|---|
| A1 | [Fixed-Θ refit of the SPARC radial acceleration relation](a1-sparc-rar-refit/README.md) | SPARC (2,693 points, 147 galaxies) | done | Under the tested assumptions, both fixed Θ values fit worse than a free scale (best Θ ≈ 1.23 × 10²⁷ m). Published-Θ mean offsets coexist with agreement within scatter in 14/14 public bins. No calibrated exclusion claim |
| A1b | [Per-galaxy rotation-curve fits with distance, inclination and Υ★ priors](a1b-sparc-per-galaxy/README.md) | SPARC (3,168 points, 153 galaxies) | done | Prior-penalized fit loss favors a free scale (baseline Θ ≈ 1.37 × 10²⁷ m). Includes velocity-error and prior-width refits, distance diagnostics and galaxy influence; loss differences are not BIC |
