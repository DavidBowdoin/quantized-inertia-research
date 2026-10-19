---
title: "Challenging a Newtonian prediction through Gaia wide binaries"
authors: [Xavier Hernandez, R. A. M. Cortés, Christine Allen, Riccardo Scarpa]
year: 2019
type: paper
venue: "International Journal of Modern Physics D 28(8):1950101"
doi: 10.1142/S0218271819501013
arxiv: 1810.08696
url: "https://arxiv.org/abs/1810.08696"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, figures/fig-4-1d-relative-velocities.png, figures/fig-5-rms-velocity-vs-separation.png]
status: neutral
tags: [wide-binaries, gaia, data-source]
---

# Challenging a Newtonian prediction through Gaia wide binaries

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1810.08696](https://arxiv.org/abs/1810.08696) · [doi:10.1142/S0218271819501013](https://doi.org/10.1142/S0218271819501013).

**Citation:** Hernandez, X., Cortés, R. A. M., Allen, C. & Scarpa, R. (2019). *Challenging a Newtonian prediction through Gaia wide binaries*. International Journal of Modern Physics D, 28(8), 1950101. https://doi.org/10.1142/S0218271819501013. arXiv:[1810.08696](https://arxiv.org/abs/1810.08696). The stored PDF is arXiv v3 of 7 March 2019, the accepted version.

**TL;DR:** The authors take a strictly cleaned sample of Hipparcos wide binaries from Shaya & Olling (2011, "SO11"), with chance-association probability below 10%, and re-measure them with Gaia DR2 astrometry. The final sample is 81 pairs in v3; v1 had 83. They compare rms 1D relative velocities against projected separation with the Newtonian simulations of Jiang & Tremaine (2010). The data agree with Newton below about 7000 AU (0.034 pc). Above that separation, where internal accelerations fall below a₀ = 1.2 × 10⁻¹⁰ m/s², the velocities level off instead of falling as Δr⁻¹ᐟ², which the authors say is inconsistent with Newtonian gravity. The paper does not mention quantised inertia. It is the data source for the [McCulloch & Lucio 2019](../2019-mcculloch-wide-binaries/README.md) QI comparison.

## Key claims
- Wide binaries probe low-acceleration dynamics on scales where dark matter is not expected to matter.
- Below 7000 AU the data are consistent with Newtonian predictions. Above it they are "inconsistent with Newtonian predictions" and level off at about the Δv seen at the a₀ point, qualitatively like flat galaxy rotation curves.
- The SO11 selection, if anything, is biased *against* high-velocity-difference pairs, which the authors say strengthens the result.
- The results confirm the earlier Hipparcos-based result (Hernandez et al. 2012), now with much smaller error bars from an independent satellite.
- The standard MOND/AQUAL external field effect would predict only a modest effect in the solar neighbourhood. The authors say the data therefore favour MONDian variants with a suppressed or absent EFE.

## Key equations
The paper contains no new theoretical equations. The tested quantity is the binned rms one-dimensional relative velocity against projected separation:
$$ \langle \Delta v_{1D}^2 \rangle^{1/2} \ \text{vs}\ \Delta r_p $$
compared with the Newtonian expectation $\Delta v \propto \Delta r^{-1/2}$ (out to the tidal radius of about 1.7 pc). The text cites the MOND Tully–Fisher scale $V_{TF} = (GMa_0)^{1/4}$.

## Data used
- The SO11 Hipparcos wide-binary catalogue: 840 pairs between 0.003 and 10 pc, of which 359 have P_ch < 10%. Stars are of narrow spectral type, with masses around 0.5 M☉.
- Gaia DR2 cross-match and successive cuts: 151 pairs with both components in DR2, then 131 after removing multiple identifications, 117 after a 3σ proper-motion agreement cut against Hipparcos, 100 after a parallax-distance agreement cut (within 13%), and 81 after a radial-velocity-difference cut of ΔV_r < 4 km/s.
- Radial velocities are available for at least one component in 71 of the 81 pairs.
- The Newtonian comparison uses the Jiang & Tremaine (2010) simulations: 50,000 binaries per run, with Galactic tides and field-star perturbations over 10 Gyr.

## Results & predictions
- The bins (left to right) contain 21, 23, 17, 8 and 12 binaries in v3. In v1 they contained 21, 24, 17, 8 and 13 (83 binaries total), which are the counts McCulloch & Lucio 2019 quote.
- The 7000 AU threshold corresponds to a Newtonian acceleration of a₀ for a solar-mass binary.
- The Newtonian rms curve falls to about 0.05 km/s near 1 pc and then rises to about 0.1 km/s beyond the tidal radius. The observed rms values at large separations sit near or above 1 km/s (read from Fig. 5 on a log axis, so these are approximate).
- The paper notes a population of non-chance pairs at a few pc with relative velocities of about 1 km/s, "over an order of magnitude above bound expectations".

## Figures
*Figure (local only): Fig. 4 — One-dimensional relative velocities for each binary in the final sample, from right-ascension-only and declination-only proper motions, with 1σ error bars. A flat upper envelope is visible. (Rendered page 7.)*

*Figure (local only): Fig. 5 — Binned rms 1D relative velocity against projected separation (circles: RA; triangles: Dec) compared with the Newtonian prediction of Jiang & Tremaine 2010 (solid red curve). The dashed vertical line marks 7000 AU. (Rendered page 8.)*

## Notable quotes
> "The results are consistent with the Newtonian prediction for projected separations below 7000 AU, but inconsistent with it at larger separations" (abstract, p. 1)

> "A full answer and validation or otherwise of our results, necessarily awaits a much more extensive study through the full Gaia catalogue" (p. 9)

> "within a MONDian frame our results imply the validity of not the most well studied version, but rather of a variant where the external field effect does not appear, or is much suppressed" (pp. 9–10)

## Criticisms & responses
- **Caveat raised by the authors:** some apparent binaries may belong to loose, dissolving moving groups. They say this needs the full Gaia catalogue to resolve.
- **Contamination:** Pittordis & Sutherland (2019, MNRAS 488, 4740; arXiv:1905.09619) found that a significant fraction of Gaia DR2 wide-binary candidates have relative velocities too high for any plausible gravity theory, which points to contamination by unbound or triple systems.
- **Statistical power:** Banik (2019, MNRAS 487, 5291) argued that more wide-binary data are needed for the test to be conclusive (this point is cited by McCulloch & Lucio 2019).
- **Gaia DR3:** [Banik et al. 2024](../../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md) used a much larger sample and detailed forward-modelling, and favoured Newtonian gravity over MOND. [Chae 2023](../2023-chae-wide-binaries/README.md) and later Hernandez papers ([2024 review](../2024-hernandez-wide-binary-review/README.md)) reported MOND-like anomalies. The disagreement continues.

## Related
- Evidence: [wide-binaries](../../02-evidence/wide-binaries.md), [globular-clusters](../../02-evidence/globular-clusters.md)
- Sources: [2012-hernandez-wide-binaries](../2012-hernandez-wide-binaries/README.md) (the Hipparcos predecessor), [2019-mcculloch-wide-binaries](../2019-mcculloch-wide-binaries/README.md) (QI applied to this data), [2023-chae-wide-binaries](../2023-chae-wide-binaries/README.md), [2024-hernandez-wide-binary-review](../2024-hernandez-wide-binary-review/README.md), [2023-banik-gaia-dr3-wide-binaries](../../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md), [2018-hernandez-bounding-curvature](../2018-hernandez-bounding-curvature/README.md)
