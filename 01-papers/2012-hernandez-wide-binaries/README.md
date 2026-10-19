---
title: "Wide binaries as a critical test of classical gravity"
authors: [Xavier Hernandez, M. Alejandra Jiménez, Christine Allen]
year: 2012
type: experiment-report
venue: "European Physical Journal C 72:1884"
doi: 10.1140/epjc/s10052-012-1884-6
arxiv: "1105.1873"
url: "https://arxiv.org/abs/1105.1873"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-hipparcos-sdss-dv-vs-s.png, figures/fig-2-fraction-and-rms-velocity.png]
status: neutral
tags: [wide-binaries, data-source]
---

# Wide binaries as a critical test of classical gravity

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1105.1873](https://arxiv.org/abs/1105.1873) · [doi:10.1140/epjc/s10052-012-1884-6](https://doi.org/10.1140/epjc/s10052-012-1884-6).

**Citation:** Hernandez, X., Jiménez, M. A. & Allen, C. (2012). *Wide binaries as a critical test of classical gravity*. European Physical Journal C 72:1884. [doi:10.1140/epjc/s10052-012-1884-6](https://doi.org/10.1140/epjc/s10052-012-1884-6) / [arXiv:1105.1873](https://arxiv.org/abs/1105.1873)

**TL;DR:** The paper proposes wide binaries as a test of gravity at low acceleration. For 1 M☉ systems, a < a₀ beyond ~7000 AU. It applies the test to two catalogues:
- 280 Hipparcos pairs from Shaya & Olling (2011);
- 417 SDSS SLoWPoKES pairs from Dhital et al. (2010).

In both, the upper envelope of projected relative velocities is flat at ~3 ± 1 km/s over three orders of magnitude in separation, instead of falling as s^(−1/2). The RMS 1D velocity is ~1 ± 0.5 km/s, roughly 10× the Newtonian Galactic-evolution model of Jiang & Tremaine (2010). The authors call this "suggestive" of a breakdown of Kepler's third law near a₀. The paper does not test QI. McCulloch & Lucio later used this dataset to argue for QI.

> Text and page numbers are from arXiv v4 (Feb 2012), stored as `paper.pdf`. The PDF lists the authors by initials only. "Xavier" and "Alejandra" come from the paper's footnotes and acknowledgements. "Christine" for C. Allen is an inference from the address chris@astroscu.unam.mx and is unverified.

## Key claims
- Under modified-gravity schemes with an acceleration scale a₀, binaries wider than ~7000 AU (3.4 × 10⁻² pc) should show "flat rotation curves" and a Tully–Fisher-like relation, V ∝ (GMa₀)^(1/4).
- Both independent catalogues show a flat upper envelope of ΔV against projected separation s. Under Newton, the envelope should fall as s^(−1/2).
- The binned RMS ΔV₁D departs from the Newtonian prediction of Jiang & Tremaine (2010) outward of the a = a₀ line, "and not before". The probability that the Newtonian model is consistent with eight points lying beyond 1σ is quoted as < (0.272)⁸ = 3 × 10⁻⁵.
- Checks for systematics:
  - Errors do not grow with separation.
  - High-S/N and nearby (d < 50 pc) subsamples give the same result.
  - The SDSS selection cut does not produce the flat envelope.
- Under modified gravity, wide binaries would be much more robust to Galactic tides, to first order.
- The paper explicitly does "not attempt to test any particular modified gravity theory". It calls for independent confirmation with purpose-built samples, mass cuts, and radial velocities.

## Key equations
Newtonian upper limit for equal-mass circular binaries, and the generic modified-gravity expectation:
$$ \Delta V_N = 2\left(\frac{GM}{s}\right)^{1/2}, \qquad \Delta V_{MG} = C\,(GMa_0)^{1/4} $$
Modified-gravity tidal condition, the analogue of the classical tidal density criterion ρ_s > ρ:
$$ \frac{(GM(R)a_0)^{1/2}}{R^2}\,\Delta r = \frac{(GM_s a_0)^{1/2}}{\Delta r} \;\Rightarrow\; \rho_s > \left(\frac{\Delta r}{R}\right)\bar\rho $$
Projected relative velocity from proper motions:
$$ \Delta v = 4.74\times10^{-3}\,\Delta\mu\, d $$

## Data used
- **Hipparcos:** the Shaya & Olling (2011, *ApJS* 192, 2) Bayesian wide-binary catalogue. The authors kept pairs with chance-alignment probability < 0.1, S/N > 0.3 and 6 < d < 100 pc, giving 280 binaries with mean S/N 1.7 and mean ΔV error 0.83 km/s.
- **SDSS:** the SLoWPoKES catalogue of Dhital et al. (2010, *AJ* 139, 2566), with < 2% false positives. The authors used 225 < d < 338 pc, giving 417 binaries with mean S/N 0.5 and mean ΔV error 11.3 km/s. Triples and white-dwarf/subdwarf primaries were excluded.
- **Newtonian comparison:** the Jiang & Tremaine (2010, *MNRAS* 401, 977) simulation of 50,000 1 M☉ binaries evolved for 10 Gyr in the Galactic tidal field. It gives a Jacobi radius of 1.7 pc and an RMS ΔV₁D of ~0.1 km/s at large s.

## Results & predictions
- Flat upper envelope at 3 ± 1 km/s over three orders of magnitude in s, in both catalogues.
- RMS ΔV₁D ≈ 1 ± 0.5 km/s. The Newtonian prediction is about a factor of 10 lower.
- For SDSS, the fraction of systems below the Newtonian limit falls from ~1 at log(s/pc) ≈ −2 to ~0 at log(s/pc) ≈ −1 (Fig. 3).
- The implied non-circularity factor in modified gravity is 4.5, compared with √2 for Newtonian.
- Using 0.5 M☉ rather than 1 M☉ would move the Newtonian prediction a further factor √2 from the data.

## Figures
*Figure (local only): Fig. 1 — Paper Figs. 1–2: projected relative velocity against projected separation for the Hipparcos sample (280 pairs, left) and the SDSS sample (417 pairs, right), with the Newtonian s^(−1/2) line and the flat upper envelope (p. 4).*

*Figure (local only): Fig. 2 — Paper Figs. 3–4: fraction of SDSS systems below the Newtonian limit against log(s/pc) (left), and binned RMS 1D relative velocity against the Jiang & Tremaine (2010) Newtonian model (curve), with the a = a₀ threshold marked by a dashed line (right) (p. 5).*

## Notable quotes
> "Our results are suggestive of a breakdown of Kepler's third law beyond a ≈ a0 scales, in accordance with generic predictions of modified gravity theories designed not to require any dark matter at galactic scales and beyond." (p. 1)

> "Figure (1) could then be a first direct evidence of the breakdown of classical gravity theories in the low acceleration regime of a < a0." (p. 4)

> "Given the relevance of the subject matter discussed, it would be highly desirable to obtain an independent confirmation" (p. 6)

## Criticisms & responses
- **Data quality.** The SDSS sample has mean S/N ≈ 0.5 on ΔV and the Hipparcos sample ~1.7–2. Projected velocities are also sensitive to contamination by chance alignments, unresolved triples and flyby companions. The authors address some of these in their appendix.
- **Gaia-era tests disagree on the outcome:**
  - Banik et al. (2024, *MNRAS* 527, 4573; Gaia DR3) report strong preference for Newtonian gravity over MOND for wide binaries within 250 pc. See [2023-banik-gaia-dr3-wide-binaries](../../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md).
  - Chae (2023) and Hernandez's later Gaia work report a MOND-like gravitational anomaly. See [2023-chae-wide-binaries](../2023-chae-wide-binaries/README.md), [2019-hernandez-gaia-wide-binaries](../2019-hernandez-gaia-wide-binaries/README.md) and [2024-hernandez-wide-binary-review](../2024-hernandez-wide-binary-review/README.md).
  - The disagreement is ongoing. It largely concerns sample selection and the treatment of hidden triples and of kinematic contamination.
- **Use by QI.** McCulloch & Lucio (2019) applied QI to this dataset; see [2019-mcculloch-wide-binaries](../2019-mcculloch-wide-binaries/README.md). This paper makes no claim about QI.

## Related
- Evidence: [wide-binaries](../../02-evidence/wide-binaries.md), [globular-clusters](../../02-evidence/globular-clusters.md)
- Sources:
  - [2019-mcculloch-wide-binaries](../2019-mcculloch-wide-binaries/README.md)
  - [2019-hernandez-gaia-wide-binaries](../2019-hernandez-gaia-wide-binaries/README.md)
  - [2018-hernandez-bounding-curvature](../2018-hernandez-bounding-curvature/README.md)
  - [2023-chae-wide-binaries](../2023-chae-wide-binaries/README.md)
  - [2024-hernandez-wide-binary-review](../2024-hernandez-wide-binary-review/README.md)
  - [2023-banik-gaia-dr3-wide-binaries](../../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md)
