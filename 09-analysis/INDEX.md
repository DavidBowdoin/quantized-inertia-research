# 09-analysis: our own calculations

> **Editorial.** Reproducible analyses carried out for this repository with public data. They are proposed in [ideas-and-tests](../08-synthesis/ideas-and-tests.md). They are our own work, not published results, and each one states its method, caveats and how to rerun it.

Each analysis is a folder holding a `README.md` (question, bottom line, method, results, caveats), a Python script (A1 needs only the standard library; later analyses use numpy and scipy, see [requirements.txt](requirements.txt)) and a `results/` folder of generated tables, JSON and SVG figures. Third-party input data are downloaded by the script into a git-ignored `data/` folder; they are not redistributed.

| ID | Analysis | Data | Status | Bottom line |
|---|---|---|---|---|
| A1 | [Fixed-Θ refit of the SPARC radial acceleration relation](a1-sparc-rar-refit/README.md) | SPARC (2,693 points, 147 galaxies) | done | Θ = 2.6 × 10²⁶ m is excluded. Θ = 8.8 × 10²⁶ m over-predicts deep-MOND accelerations by 17–32% (ΔBIC +490 vs MOND). The data prefer Θ ≈ 1.2 × 10²⁷ m |
| A1b | [Per-galaxy rotation-curve fits with distance, inclination and Υ★ priors](a1b-sparc-per-galaxy/README.md) | SPARC (3,168 points, 153 galaxies) | done | Per-galaxy freedom does not rescue fixed Θ. Θ = 8.8 × 10²⁶ m: ΔBIC +1,195 vs MOND (conservative +225), with a third of galaxies pulled > 20% closer. Best Θ ≈ 1.37 × 10²⁷ m |
