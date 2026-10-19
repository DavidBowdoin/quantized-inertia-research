---
title: "Testing Newton/GR, MoND and quantised inertia on wide binaries"
authors: [Michael Edward McCulloch, J. H. Lucio]
year: 2019
type: paper
venue: "Astrophysics and Space Science 364(8), 121"
doi: 10.1007/s10509-019-3615-z
arxiv: 1908.01434
url: "https://doi.org/10.1007/s10509-019-3615-z"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, figures/fig-1-wide-binary-velocities.png]
status: supports
tags: [coauthored-with-mcculloch, dark-matter, gaia, mond, wide-binaries]
---

# Testing Newton/GR, MoND and quantised inertia on wide binaries

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1908.01434](https://arxiv.org/abs/1908.01434) · [doi:10.1007/s10509-019-3615-z](https://doi.org/10.1007/s10509-019-3615-z).

**Citation:** McCulloch, M. E. & Lucio, J. H. (2019). *Testing Newton/GR, MoND and quantised inertia on wide binaries*. Astrophysics and Space Science, 364(8), 121. https://doi.org/10.1007/s10509-019-3615-z. arXiv:[1908.01434](https://arxiv.org/abs/1908.01434). The stored PDF is the arXiv v1.

**TL;DR:** The paper derives closed-form relative orbital velocity Δv(d) for equal-mass circular binaries under Newton/GR, under MoND (simple interpolation function plus an external field effect, EFE), and under QI. It compares these with the binned rms relative velocities of 83 Gaia DR2 wide binaries from Hernandez et al. (2019, IJMP-D; cited as 2018). Newton/GR and MoND (with EFE) under-predict the velocities beyond about 0.3 pc. The paper concludes that "QI alone agrees with the data given the error bars", with no tunable parameter. The work was funded by DARPA grant HR001118C0125.

## Key claims
- Dark matter cannot rescue Newton/GR for wide binaries, because it must be smooth on these scales to fit galaxy rotation curves.
- With the EFE (a_g ≈ 1 × 10⁻¹⁰ m/s²), MoND behaves almost like Newton for nearby binaries and also under-predicts the data.
- QI has no external field effect. Its acceleration scale 2c²/Θ is fixed rather than fitted, so "it either works or it does not".
- Caveats noted by the authors: Banik (2019) says more data is needed to make Hernandez et al. conclusive. Pittordis & Sutherland (2019) showed that false binaries "are likely still an issue". All the data points lie *above* even the QI curve.

## Key equations
QI inertial mass (Θ = 8.8 × 10²⁶ m):
$$ M_I = M_g\left(1 - \frac{2c^2}{A\Theta}\right) $$
Newtonian relative velocity:
$$ \Delta v_N = \sqrt{\frac{2GM}{d}} $$
MoND with external field $a_g$:
$$ \Delta v_{MoND} = \sqrt{\frac{GM}{d} - a_g d + \sqrt{\left(a_g d - \frac{GM}{d}\right)^2 + 4GM(a_g + a_0)}} $$
QI quartic and solution:
$$ v^4 - \frac{GM}{2d}v^2 - \frac{GMc^2}{2\Theta} = 0, \qquad \Delta v_{QI} = \sqrt{\frac{GM}{d} + \sqrt{\frac{G^2M^2}{d^2} + \frac{8GMc^2}{\Theta}}} $$

## Data used
- Hernandez, Cortés, Allen & Scarpa (2019): rms sky-projected relative velocities of 83 Gaia DR2 wide binaries in five separation bins containing 21, 24, 17, 8 and 13 pairs, all within 100 pc of the Sun.
- Inputs: M = 1 × 10³⁰ kg per star, with an uncertainty range of 0.5M–2M. a₀ = 1.2 × 10⁻¹⁰ m/s², with a range of 1.0–2.0 × 10⁻¹⁰. Θ uncertainty of 9%. a_g ≈ 1 × 10⁻¹⁰ m/s².

## Results & predictions
- Separations of 0.007–4 pc are plotted. Newton/GR and MoND+EFE fall well below the observations for d ≳ 0.3 pc (60,000 AU).
- The QI curve flattens at about 0.5 km/s at large separations. The observed bins sit at about 0.8 km/s, inside the grey uncertainty band (read from Fig. 1).
- Cross-check against Banik & Zhao (2018) at 0.1 pc: Newton 0.15 km/s there vs 0.2 km/s here; MoND 0.2 km/s there vs 0.3 km/s here. The paper attributes the difference to the assumed total mass (1.5 M☉ vs 2 M☉).
- The paper notes that using a₀ = 2 × 10⁻¹⁰ m/s² in MoND gives "an expression practically equivalent to QI".

## Figures
*Figure (local only): Fig. 1 — Relative velocity Δv (km/s) against separation d (pc) for Gaia DR2 wide binaries (crosses, with the grey area showing uncertainty), compared with Newton/GR (dotted), MoND with EFE of 1e-10 m/s² (dashed) and QI (solid), each with upper and lower bounds. (Rendered page 8 of the arXiv PDF.)*

## Notable quotes
> "QI alone agrees with the data given the error bars." (p. 6)

> "The data points all lie above the prediction of QI, but still in agreement. It is possible that some of the data has been contaminated by false binaries" (p. 6)

> "It either works or it does not, whereas Eq. (9) MoND has an arbitrary, tunable, parameter." (p. 5)

## Criticisms & responses
- **Data reliability:** Pittordis & Sutherland (2019), which the paper itself cites, argued that Gaia DR2 wide-binary samples contain many systems whose velocities are implausibly high for any gravity theory, which inflates rms velocities. The large error bars in Fig. 1 (from 83 binaries) limit how strongly the models can be discriminated.
- **Later Gaia DR3 analyses:** [Banik et al. 2024 (2023-banik-gaia-dr3-wide-binaries)](../../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md) found the DR3 wide-binary data favour Newtonian gravity and exclude MOND at high significance. [Chae 2023](../2023-chae-wide-binaries/README.md) reported a MOND-like gravitational anomaly at low accelerations. Hernandez and collaborators continued to report deviations; see [2024-hernandez-wide-binary-review](../2024-hernandez-wide-binary-review/README.md). The question was still contested at the time of writing.
- **Data version (factual):** the 83 binaries and the bin counts 21/24/17/8/13 match arXiv v1 of Hernandez et al. The published v3 / IJMP-D version has 81 binaries (21/23/17/8/12).
- **Model simplifications (factual):** the comparison uses equal-mass, circular orbits and compares the model's relative velocity with sky-projected rms velocities, without forward-modelling eccentricities, projection or contamination. Later studies such as Banik & Zhao 2018 and Banik et al. 2024 do forward-model these effects.
- General QI critique: [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [wide-binaries](../../02-evidence/wide-binaries.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2019-hernandez-gaia-wide-binaries](../2019-hernandez-gaia-wide-binaries/README.md) (the data source), [2012-hernandez-wide-binaries](../2012-hernandez-wide-binaries/README.md), [2023-chae-wide-binaries](../2023-chae-wide-binaries/README.md), [2024-hernandez-wide-binary-review](../2024-hernandez-wide-binary-review/README.md), [2023-banik-gaia-dr3-wide-binaries](../../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md), [2024-mcculloch-proxima-centauri](../2024-mcculloch-proxima-centauri/README.md), [2025-mcculloch-jupiter-mass-binaries](../2025-mcculloch-jupiter-mass-binaries/README.md), [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
