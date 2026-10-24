---
title: "A2b: McCulloch's later derivations traced to the galaxy predictions"
tags: [analysis, derivation, galaxy-rotation, theta, uncertainty-principle, information-theory]
as_of: 2026-10-24
---

# A2b: McCulloch's later derivations traced to the galaxy predictions

> **Editorial analysis.** This is our own reading and arithmetic, not a published result. It reproduces the printed mass expressions, checks selected steps leading to them, and separates the author's results from our variants. Reproducing an expression does not establish that it follows from the preceding equations. Proposed as A2b in [ideas-and-tests](../../08-synthesis/ideas-and-tests.md). It is kept separate from Renda's disputed spectrum reconstruction (A2).

## Question
In his [30 August 2026 reply to critics](https://physicsfromtheedge.blogspot.com/2026/08/responding-to-criticisms.html), McCulloch accepts Renda's point that the early derivation "only looked at the peak" of the Unruh spectrum. He points instead to the uncertainty-principle and information-erasure derivations. The audit asks four questions:
- What does each later route actually assume?
- Which of those assumptions fix the galaxy-scale constant 2c²/Θ, and which only fix the normalisation?
- How does the inertial-mass formula become the galaxy law that A1, A1b and A6 test?
- Which published criticism applies to which step?

## Bottom line
1. **The printed final expressions share a linear bracket, with qualifications.** The 2016 uncertainty principle, the linearised 2017 information-loss route, the 2020 horizon widths and the 2020 information theory give expressions proportional to 1 − d_R/d_H:
   - d_R = c²/a is the Rindler-horizon distance;
   - d_H = Θ/2 is "the radius of the cosmos".

   In these linear expressions, 2c²/Θ comes from the ratio of the two distances. The 2016 and 2017 prefactors are not exactly one, and the 2017 linearisation is valid only near a = 2c²/Θ. Several papers first compute a mass change dm and identify it with the inertial-mass expression. **Editorial check:** the 2016 Eq. 14 has the opposite sign to the mass change implied by its Eq. 13, as [Haug 2018b](../../01-papers/2018-haug-foundation-quantized-inertia/README.md) first reported (a typo McCulloch confirmed privately, according to Haug). Our table preserves Eqs. 14–20 as printed and flags this inconsistency; it does not certify the derivation.
2. **The tested choices change P while leaving κ fixed; that alone does not preserve galaxy predictions.** Four choices are at issue:
   - ħ vs ħ/2;
   - radius vs half-circumference;
   - Wien-peak photon vs k_BT;
   - log₂ vs ln.

   The listed variants move P between 0.20 and 6.3 while leaving κ = 2 (Table 1); one variant combines ħ/2 with half-circumferences. At fixed G and baryonic masses, retaining P changes the force balance and galaxy prediction. Dividing by the high-acceleration limit P can remove it only with an explicit, consistent calibration of mass or G. All SPARC scores here use the published mass law with P = 1.

   In the 2020 widths route, the changes ½ × 1/π × 1/β cancel the 2016 factor 2πβ. The count N = mc²/E_p converts the photon energy change into a particle mass change; that count alone does not force P = 1, as the variants show. The 2020 information route uses log₂ and divides by N₁ bits after identifying kT with mc² per bit. Its P = 1 likewise depends on those assignments. Recovering the desired normalisation does not independently validate the physical choices.
3. **κ = 2 is not forced by the general idea.** Three variants that fit the general idea give other values:
   - Half-circumference for the Rindler horizon only: κ = 2π.
   - Counting bits out to Θ rather than Θ/2: κ = 1.
   - Areas instead of distances (2017): a *quadratic* law, 1 − (2c²/aΘ)², which the paper linearises near a ≈ 2c²/Θ.

   Giné & Luciano's de Sitter uncertainty principle also gives a quadratic correction. The earlier routes give 1.99 (2007) and 1.27 (2013, taken literally). Which cosmic radius to use is not fixed by any derivation. Editorial check: the present proper particle-horizon diameter in Planck 2018 ΛCDM is 8.74 × 10²⁶ m, which matches the Θ = 8.8 × 10²⁶ m used since 2017.
4. **The step from the mass formula to an orbit law is not unique.** McCulloch's papers use four laws from the same Eq. 1 (Table 2, Fig. 1):
   - **2017 Eq. 8** (tested in A1) replaces |a| with a_bar on the right-hand side of his Eq. 6.
   - **The exact solution of Eq. 6** is MOND's "simple" function with a₀ = 2c²/Θ. It uses the same algebra as McCulloch & Lucio's 2019 wide-binary formula.
   - **The deep-limit law** v⁴ = 2GMc²/Θ is used in 2012, 2017 and 2024.
   - **The additive law** a = g + a_Q (2010, 2019 Rindler horizons, 2025 JuMBOs) has no Tully–Fisher limit.
5. **On SPARC at the published Θ, the choice of law matters as much as the choice of Θ.** These results use A1's data and likelihood:
   - **The exact solution of Eq. 6** fits worse than Eq. 8: ΔBIC +608 at Υ_disk = 0.5 (+162 to +813 for Υ_disk = 0.4–0.6), and it fits worse in 200/200 galaxy-bootstrap resamples. It adds a_Q rather than a_Q/2 at high acceleration.
   - **The additive law** fits substantially worse: ΔBIC +8,225 against the free-scale McGaugh fit (+7,733 against fixed-Θ Eq. 8), with mean residuals of −1.1 dex in the lowest bins. This applies the additive law to SPARC under A1's assumptions.
   - **With the scale free,** the exact solution is MOND's simple function at 1.13 × 10⁻¹⁰ m s⁻², an equivalent Θ of 1.6 × 10²⁷ m (1.8 times the published value).

   Part of the 2017 comparison's agreement at the published Θ therefore rests on the Eq. 7 substitution. Neither completion is derived for inner radii, because a′ = 2c²/Θ is assumed only "at the edge of a galaxy".
6. **The redshift law is a further, separate assumption** (editorial extension). Eq. 9, Θ(z) = Θ₀/(1+z), is the size at epoch z of *today's* horizon sphere. Taken literally, the derivations' "cosmic horizon seen by the object" gives different evolution. The particle horizon at each epoch gives a_Q ∝ (1+z)^1.4. The pre-2017 Hubble diameter 2c/H(z) gives exponents of 0.7–1.2, but its normalisation is already strongly disfavoured by the SPARC data in A1. Neither reading is a published QI prediction.

The later routes use uncertainty or information assumptions instead of reproducing the earlier pressure integral. The 2016 route still uses the Wien-peak photon energy, so it has not eliminated spectral assumptions; this alone does not show that Renda's particular pressure-integral objection transfers unchanged. [Junghanns 2026](../../03-criticism/2026-junghanns-causal-restriction-nogo/README.md), §10 (unreviewed), assesses the horizon–uncertainty identification and additional conservation assumptions in the 2016 route while explicitly leaving that formulation outside his Rindler–Casimir no-go result. The galaxy prediction also needs a mass normalisation, cosmic radius, orbit law and Θ(z). These derivation issues do not change A1's numerical diagnostics of the published Eq. 8, whose validity remains a separate empirical question.

## Data
- **Sources:** the derivation papers are read from the stored PDFs:
  - [2016](../../01-papers/2016-mcculloch-relativity-uncertainty/README.md);
  - [2017 information loss](../../01-papers/2017-mcculloch-information-loss/README.md) (accepted manuscript);
  - [2020 widths](../../01-papers/2020-mcculloch-horizon-widths/README.md);
  - [2020 information theory](../../01-papers/2020-mcculloch-information-theory/README.md).
- **Orbit laws:** taken from [2012](../../01-papers/2012-mcculloch-galactic-scales/README.md), [2017 SPARC](../../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md), [2017 dwarfs](../../01-papers/2017-mcculloch-dwarf-galaxies/README.md), [2019 wide binaries](../../01-papers/2019-mcculloch-wide-binaries/README.md), [2019 Rindler horizons](../../01-papers/2019-mcculloch-rindler-horizons/README.md), [2024 Proxima](../../01-papers/2024-mcculloch-proxima-centauri/README.md) and [2025 JuMBOs](../../01-papers/2025-mcculloch-jupiter-mass-binaries/README.md).
- **SPARC:** the radial acceleration relation points (2,693 points, 147 galaxies) come through [A1](../a1-sparc-rar-refit/README.md)'s loader. The script fetches them into A1's git-ignored `data/` if they are missing. The SHA-256 sums are in `results/results.json`.
- **Cosmology:** flat ΛCDM with Planck 2018 values (H₀ = 67.66 km s⁻¹ Mpc⁻¹, Ω_m = 0.3111) and radiation for N_eff = 3.046 massless neutrinos (an approximation).
- **Not available:**
  - The 2024 book, which the 2026 blog post cites for a "more robust" uncertainty-principle derivation. > [!UNVERIFIED] Its derivation has not been checked.
  - A 2022 "Corrected" revision of the 2020 information paper (ResearchGate). > [!UNVERIFIED]

## Method
- **Routes.** The functions `route_*` reproduce the printed mass expressions, which some papers write as dm/m rather than m_i/m. For expressions linear in 1/a, P and κ in P(1 − κc²/(aΘ)) are recovered from two accelerations and checked to ~10⁻¹⁵ over 2.5c²/Θ < a < 10³ m s⁻². This is an algebraic check of the expression, not an extension of the 2017 approximation's domain. The unlinearised area route is reported separately. The variants change the choices listed in Table 1; the combined ħ/2 and half-circumference variant changes two at once. `check_2016_conservation` separately checks the mass change against Eq. 13.
- **Laws.** Each orbit law is checked against the equation it claims to solve, to machine precision. McCulloch & Lucio's 2019 Eq. 13 is checked against the exact solution of Eq. 6. Each law is then scored on SPARC with A1's likelihood: Gaussian in log g_obs, errors on both axes and a fitted intrinsic scatter. The scoring is done at fixed Θ (k = 1) and with the scale free (k = 2). It is repeated for Υ_disk = 0.4, 0.5 and 0.6, and with 200 galaxy-bootstrap resamples for the fixed-Θ comparison.
- **Θ(z).** Three readings are computed: Eq. 9; the proper particle-horizon diameter 2χ_p(z)/(1+z); and the Hubble diameter 2c/H(z). For each, γ is the equivalent exponent in a_Q ∝ (1+z)^γ.

## Results
All numbers below are generated by the script ([summary](results/summary.md)).

### Editorial check: the 2016 sign inconsistency

In the stored [2016 preprint](https://arxiv.org/pdf/1610.06787), p. 5, Eq. 13 states

$$m_1c^2 + \frac{\hbar c}{\Delta x_1} = m_2c^2 + \frac{\hbar c}{\Delta x_2}.$$

For its definition dm = m₂ − m₁, rearranging gives

$$dm = \frac{\hbar}{c}\left(\frac{1}{\Delta x_1} - \frac{1}{\Delta x_2}\right).$$

Printed Eq. 14 reverses the two terms. With Δx₁ = Θ/2 and Δx₂ = c²/a, Eq. 13 gives a negative mass change for a > 2c²/Θ, whereas Eqs. 14–20 give a positive one. At a = 2a_Q, the generated check obtains dm/m = −0.632733 from Eq. 13 and +0.632733 from the printed expression. Substituting the printed change back into Eq. 13 leaves an energy residual of +1.265466 in units of the Wien-peak mc². The residual vanishes with Eq. 13's own rearrangement. This is a sign inconsistency even accepting the proposed conservation law; it does not establish a negative total inertial mass.

**This is not a new finding.** [Haug 2018b](../../01-papers/2018-haug-foundation-quantized-inertia/README.md) reported it first. He writes that McCulloch confirmed in correspondence that Eq. 13 should carry minus signs, m₁c² − ħc/Δx₁ = m₂c² − ħc/Δx₂, from which printed Eq. 14 follows. The confirmation is known only through Haug's account; no published erratum was found. Haug also argues that, once corrected, the relation can no longer be read as conservation of "mass-energy plus the energy uncertainty", which is how the paper motivates it. Our check reproduces the inconsistency in the printed text. It does not decide which conserved quantity, if any, the route should assume.

### Editorial check: retaining the prefactor

If the mass ratio is P(1 − a_Q/(a+a_Q)) under the 2017 split-acceleration assumption, the force balance at fixed G and baryonic masses is

$$P\left(1-\frac{a_Q}{a+a_Q}\right)a = g, \qquad a^2 = \frac{g}{P}(a+a_Q).$$

Thus P affects even the deep-limit relation: v⁴ = GMa_Q/P. One may instead define the inertial mass relative to its high-acceleration limit, dividing out P, but that requires matching the mass and G calibration used to construct g. This analysis does not infer that calibration from the derivations. The SPARC comparisons below test P = 1; they do not propagate every prefactor in Table 1 into a new fit.

**Table 1. Printed expressions written as m_i/m (or dm/m) = P(1 − κc²/(aΘ)).**

| Route | As printed / variant | P | κ |
|---|---|---|---|
| 2007 Unruh spectrum | as printed | 1 | βπ² = 1.988 |
| 2013 asymmetric Casimir | Eq. 8 bracket taken literally | 1 | 4/π = 1.273 |
| 2016 uncertainty principle | Eqs. 14–20 as printed; sign conflicts with Eq. 13 (ħ, radii, Wien-peak photon) | 2πβ = 1.266 ("26% too large") | 2 |
| | with k_BT instead of the Wien peak | 2π | 2 |
| | with ħ/2 and half-circumferences | β = 0.201 | 2 |
| 2017 information loss (areas) | as printed, linearised near a ≈ 2c²/Θ | (4/3) ln 2 = 0.924 | 2 |
| | same steps without the linearisation | not of this form: (2/3) ln 2 (1 − (2c²/aΘ)²) | — |
| 2020 horizon widths | as printed (ħ/2, both half-circumferences, k_BT) | 1 | 2 |
| | radii for both horizons | π | 2 |
| | half-circumference for the Rindler horizon only | 1 | **2π** |
| | Wien-peak photon, as in 2016 | β | 2 |
| 2020 information theory | as printed (log₂ 2 = 1, distance Θ/2) | 1 | 2 |
| | natural log (Landauer's kT ln 2) | ln 2 = 0.693 | 2 |
| | bits counted to Θ instead of Θ/2 | 2 | **1** |

**Table 2. Orbit laws in McCulloch's papers** (g = GM/r², a_Q = 2c²/Θ = 2.04 × 10⁻¹⁰ m s⁻²).

| Law | Form | High-g offset | Deep limit | Used in |
|---|---|---|---|---|
| Deep limit | a² = g·a_Q | — | v⁴ = 2GMc²/Θ | 2012 Eqs. 7–9; 2017 SPARC Eqs. 10–13; 2017 dwarfs; 2024 Proxima |
| 2017 Eq. 8 | a = √(g² + g·a_Q) | +a_Q/2 | same | 2017 SPARC; tested in A1, A1b, A6–A6f |
| Eq. 6 solved exactly | a = g/2 + √(g²/4 + g·a_Q) (MOND simple, a₀ = a_Q) | +a_Q | same | same algebra as 2019 wide binaries Eqs. 10–13 |
| Additive | a = g + a_Q | +a_Q | a → a_Q (no Tully–Fisher) | 2010; 2019 Rindler horizons Eq. 3; 2025 JuMBOs Eq. 6 |

**SPARC scores** (Υ_disk = 0.5; ΔBIC against the McGaugh 2016 fit with a₀ free):

| Law | Θ fixed at 8.8 × 10²⁶ m | Θ free (best a, equivalent Θ) |
|---|---|---|
| 2017 Eq. 8 | +494 | +77 (1.47 × 10⁻¹⁰; 1.23 × 10²⁷ m) |
| Eq. 6 solved exactly | +1,102 | +4 (1.13 × 10⁻¹⁰; 1.60 × 10²⁷ m) |
| Additive | +8,225 | +1,446 (2.6 × 10⁻¹¹; 7.0 × 10²⁷ m) |

The exact law's mean residuals at fixed Θ are −0.05 to −0.14 dex in every bin from 10⁻¹² to 10⁻⁹ m s⁻², a near-uniform overprediction. Eq. 8's residuals are within 0.03 dex of zero above 10⁻¹⁰ m s⁻². These offsets are conditional on SPARC's Υ★ and the A1 error model; see A1's caveats.

**Θ(z) readings** (a_Q(z)/a_Q(0)):

| z | Eq. 9 | particle horizon (γ) | Hubble 2c/H(z) (γ) |
|---|---|---|---|
| 1.0 | 2.00 | 2.63 (1.40) | 1.78 (0.83) |
| 2.3 | 3.30 | 5.54 (1.43) | 3.45 (1.04) |
| 4.5 | 5.50 | 11.98 (1.46) | 7.25 (1.16) |

The high-redshift comparisons constrain different things. [A6](../a6-rar-redshift-evolution/README.md)'s binned MUSE-DARK analysis favors the approximate (1+z) shape with a fitted amplitude and disfavors the steeper proper-particle-horizon variant under its conversion and error model. Its conversion of the halo-free MOND refit also gives approximately (1+z), at a lower normalisation. [A6b](../a6b-musedark-per-galaxy/README.md)'s evolution inference depends strongly on mass budget and radial sampling and is inconclusive. [A6c](../a6c-rc100-qi/README.md) and the within-KMOS3D comparison in [A6e](../a6e-sharma-qi/README.md) prefer weaker evolution under their adopted decompositions or baryonic calibrations and approximate errors; the pooled A6e slope is poorly constrained.

[A6d](../a6d-mcculloch-2017-highz/README.md)'s Genzel comparison is a normalisation check conditional on halo-fitted baryons, while its Übler comparison requires verifying the deep-limit formula's applicability to peak velocities. [A6f](../a6f-rizzo-z45-qi/README.md) has no measured local baseline and cannot separate normalisation from evolution. A steeper horizon prescription increases the predicted high-z scale at fixed present normalisation, but these checks do not establish a common measured growth deficit across A6–A6f. The alternative horizon readings remain our cosmology-dependent extensions, not the author's predictions.

![Four orbit laws against public SPARC bins](results/fig-1-orbit-laws.svg)

*Figure 1. The four orbit laws at Θ = 8.8 × 10²⁶ m, with the public SPARC bin means ± within-bin standard deviation (descriptive only; see A1). The deep-limit curve is drawn only where it applies.*

![Θ(z) readings](results/fig-2-theta-z.svg)

*Figure 2. Growth of the acceleration scale with redshift under McCulloch's Eq. 9 and two literal readings of "the cosmic horizon" (editorial).*

## Which criticism applies to which step

| Step | Assumption | Criticism | Applies to later routes? |
|---|---|---|---|
| Unruh spectrum cut by a Hubble-scale Casimir effect (2007), peak-only energy (2013) | linear F; all energy in the peak mode | [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md): the mode sum is not linear, and the peak-only treatment is invalid; [Dickmann & Dickmann 2023](../../03-criticism/2023-dickmann-casimir-contradicts/README.md): the full sum gives a force ∝ a⁴ | The later routes do not repeat that pressure integral. The 2016 route still substitutes a Wien-peak photon energy; the 2020 widths route uses k_BT. Applicability of the specific spectrum objection needs a separate argument |
| Horizons act as boundaries on vacuum modes | Rindler horizon damps Unruh radiation | [Junghanns 2026](../../03-criticism/2026-junghanns-causal-restriction-nogo/README.md) (unreviewed): a horizon restricts access but imposes no Casimir boundary; Milgrom 1999 and [Koberlein 2017](../../07-media/2017-koberlein-doing-it-wrong/README.md): isotropy | Partly. Junghanns says the 2016 route is not excluded but needs independent assumptions; the 2020 papers still motivate the bracket by horizon damping |
| Energy bookkeeping | mass-energy + ħc/Δx (2016); horizon energy-uncertainty difference (2020 widths); energy from information loss (2017, 2020 information) | [Junghanns 2026](../../03-criticism/2026-junghanns-causal-restriction-nogo/README.md), §10 (unreviewed), assesses the 2016 horizon–uncertainty identification and extra conservation assumptions. [Haug 2018b](../../01-papers/2018-haug-foundation-quantized-inertia/README.md) reports a sign typo in 2016 Eq. 13, which McCulloch confirmed privately (per Haug); with minus signs, Haug argues, the relation is no longer conservation of mass-energy plus uncertainty energy | Junghanns does not exclude the 2016 formulation; his discussion is not a comprehensive assessment of all later routes. Our check reproduces Haug's sign finding in the printed text |
| Normalisation | ħ/2, half-circumference, k_BT, log₂ | McCulloch himself: "no good justification for using the width"; log₂ is argued, not derived | The tested variants change P at fixed κ. Predictions at fixed baryonic masses and G still depend on P; removing it requires an explicit calibration |
| Bracket coefficient | same geometry for both horizons; distance (not area) counting; cosmic radius Θ/2 | none published | Sets the galaxy constant; varies with these choices (Table 1) |
| m_i ≠ m_g | Eq. 1 applies to inertial mass only | equivalence-principle bounds ([Turyshev review](../../01-papers/2010-turyshev-pioneer-review/README.md)); QI's torsion-balance argument | All routes |
| Orbit law | split into rotation plus a′ = 2c²/Θ "at the edge", applied at all radii; Eq. 7 substitution | none published (this analysis) | All galaxy predictions |
| Θ and Θ(z) | Θ = 8.8 × 10²⁶ m since 2017; Θ₀/(1+z) | [equations §7](../../00-overview/equations.md#7-discrepancies-and-inconsistencies-between-papers); A1 and A6 | All galaxy and redshift predictions |

## Caveats
- **The 2024 book's derivation is unread.** It is the version McCulloch now calls "more robust"; it may differ from the 2016 and 2020 versions read here.
- **Reproducing printed results is not a validation of every derivation step.** The 2016 conservation check reproduces the sign typo first reported by Haug (2018b). Other route tests reproduce the final expressions and selected identities; they do not verify every transition or physical assumption. The separate 2020 widths route starts from an energy-uncertainty difference, so the 2016 sign finding cannot simply be transferred to it.
- **The SPARC comparisons inherit A1's assumptions:** Υ★, the error model and points within a galaxy treated as independent apart from the bootstrap. The fixed-Θ ΔBIC values are not calibrated significances.
- **The exact solution of Eq. 6 is our completion,** not McCulloch's galaxy formula. He uses the same algebra only for wide binaries. It should be labelled as an editorial variant wherever it is reused.
- **The Θ(z) readings depend on the assumed cosmology.** Eq. 9 itself is stated as "assuming a linear expansion of the cosmos with time".

## Reproduce
```sh
python3 -I 09-analysis/a2b-derivation-trace/test_derivation_trace.py
python3 -I 09-analysis/a2b-derivation-trace/derivation_trace.py            # 200 bootstrap resamples
python3 -I 09-analysis/a2b-derivation-trace/derivation_trace.py --no-sparc # routes and Θ(z) only, no download
```
Standard library only. Imports A1's `rar_refit.py` for the SPARC loader, likelihood and plotting.

## Related
- Analyses: [A1](../a1-sparc-rar-refit/README.md), [A1b](../a1b-sparc-per-galaxy/README.md), [A6](../a6-rar-redshift-evolution/README.md), [A6d](../a6d-mcculloch-2017-highz/README.md)
- Evidence: [derivation](../../02-evidence/derivation.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmology](../../02-evidence/cosmology.md)
- Sources: [2018-gine-hawking-unruh-uncertainty](../../01-papers/2018-gine-hawking-unruh-uncertainty/README.md) (origin of the half-circumference), [2020-gine-luciano-eup-modified-inertia](../../01-papers/2020-gine-luciano-eup-modified-inertia/README.md), [2024-mcculloch-quantised-accelerations](../../07-media/2024-mcculloch-quantised-accelerations/README.md)
