---
title: "Is the acceleration scale of the radial acceleration relation tracking the cosmic expansion rate?"
authors: [G. T. Alcock]
year: 2026
type: paper
venue: "Monthly Notices of the Royal Astronomical Society 551(4), stag1485 (Letter)"
doi: 10.1093/mnras/stag1485
arxiv: 2609.38796
url: "https://doi.org/10.1093/mnras/stag1485"
open_access: true
license: CC-BY-4.0
files: [paper.pdf]
status: neutral
tags: [galaxy-rotation, high-redshift, rar, mond, cosmology]
---

# Is the acceleration scale of the radial acceleration relation tracking the cosmic expansion rate?

**Citation:** Alcock, G. T. (2026). *Is the acceleration scale of the radial acceleration relation tracking the cosmic expansion rate?* MNRAS 551(4), stag1485 (Letter). https://doi.org/10.1093/mnras/stag1485. Preprint: [arXiv:2609.38796](https://arxiv.org/abs/2609.38796) (`paper.pdf` is the journal version, CC BY 4.0).

**TL;DR:** A four-page reanalysis of the binned MUSE-DARK a₀(z) values. Fitting a₀ ∝ (1+z)^γ gives γ = 0.78 ± 0.15. A constant scale and matter-density scaling are both excluded, and H(z) tracking is the preferred one-parameter law. The paper tabulates the digitized bins, which makes it the input for our binned QI test. It does not mention QI.

## Key claims
- γ = 0.78 ± 0.15 with the plotted bars read as 1σ. A constant scale is excluded at 5.3σ and (1+z)^1.5 at 4.8σ (Sect. 3).
- H(z) tracking fits with χ² = 5.2/3 and amplitude (1.40 ± 0.03) × 10⁻¹⁰ m s⁻², 17% above the SPARC value. It is the AICc-preferred one-parameter law. The fitted exponent is 2.1σ below H(z)'s effective 1.10.
- If the bars are 95% intervals, γ = 0.78 ± 0.08 and pure H(z) tracking is in tension (p = 1.8 × 10⁻⁴).
- MUSE-DARK's "faster than H(z)" remark depends on anchoring to the local value. With a free amplitude the binned growth is, if anything, slightly slower.
- Exponent-based conclusions do not change under redshift-independent rescalings of a₀, so they are robust to common-mode stellar-mass errors (Sect. 4).

## Key equations
$$a_0(z) = A\,(1+z)^{\gamma}, \qquad a_0(z) = A\,E(z),\; E \equiv H(z)/H_0$$

## Data used
- Table 1: the four binned a₀(z) values of Ciocan et al. 2026 (Fig. 3), digitized "with axis-calibrated precision of ∼ 0.01". The two printed extreme values are recovered exactly.
- The SPARC a₀ = 1.20 ± 0.26 × 10⁻¹⁰ m s⁻² (McGaugh et al. 2016) as an optional anchor.
- Cosmology Ω_m = 0.307, H₀ = 67.7 km s⁻¹ Mpc⁻¹.

## Results & predictions
| Model | χ²/ν (bars = 1σ) | Parameters |
|---|---|---|
| Constant | 28.8/3 | A = 2.28 |
| A E(z) | 5.2/3 | A = 1.40 ± 0.03 |
| A (1+z)^1.5 | 23.2/3 | A = 0.90 ± 0.02 |
| A (1+z)^γ | 1.2/2 | γ = 0.78 ± 0.15 |

- Beyond the measured range, H(z) tracking predicts a₀ ≈ 3.2 × 10⁻¹⁰ m s⁻² at z = 2, against 4.2 for the linear form. JWST, ALMA and SKA kinematics could separate them.

## Figures
*Figure 1 (not stored): the binned values, the SPARC point and the fitted laws.*

## Notable quotes
> "the long-noted coincidence a0 ∼ cH0 survives its first confrontation with direct kinematic measurements at intermediate redshift" (Abstract)

## Criticisms & responses
- The author treats the four bins as independent and notes this is "optimistic for the absolute significances" (Sect. 4).
- He notes that an evolving external field effect could mimic an evolving a₀ in MOND readings.
- Editorial: QI's printed law, a_Q ∝ (1+z), is the γ = 1 member of the family fitted here. Our [A6](../../09-analysis/a6-rar-redshift-evolution/README.md) reproduces these fits and adds QI's normalization and function.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmology](../../02-evidence/cosmology.md)
- Sources: [2026-ciocan-muse-dark-rar](../2026-ciocan-muse-dark-rar/README.md), [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md)
- Context: [mond](../../05-context/mond.md)
- Analysis: [A6](../../09-analysis/a6-rar-redshift-evolution/README.md)
