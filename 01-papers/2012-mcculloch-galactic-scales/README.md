---
title: "Testing quantised inertia on galactic scales"
authors: [Michael E. McCulloch]
year: 2012
type: paper
venue: "Astrophysics and Space Science 342(2), 575-578"
doi: 10.1007/s10509-012-1197-0
arxiv: "1207.7007"
url: "https://doi.org/10.1007/s10509-012-1197-0"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-btfr-mihsc-vs-mond.png]
status: supports
tags: [galaxy-rotation, galaxy-clusters, dark-matter]
---

# Testing quantised inertia on galactic scales

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1207.7007](https://arxiv.org/abs/1207.7007) · [doi:10.1007/s10509-012-1197-0](https://doi.org/10.1007/s10509-012-1197-0).

**Citation:** McCulloch, M. E. (2012). *Testing quantised inertia on galactic scales*. Astrophysics and Space Science 342(2), 575-578. [doi:10.1007/s10509-012-1197-0](https://doi.org/10.1007/s10509-012-1197-0) / [arXiv:1207.7007](https://arxiv.org/abs/1207.7007)

**TL;DR:** This is the first QI/MiHsC treatment of galaxy and cluster rotation. It assumes that a star at a galaxy's edge keeps a total acceleration of at least 2c²/Θ through small-scale motions. From that it derives a baryonic Tully–Fisher relation, v⁴ = 2GMc²/Θ, with a constant of 6.7 ± 0.6 × 10⁻¹⁰ m/s² and no free parameters. Against McGaugh et al.'s binned data, the formula agrees within the stated errors (30% observed, 20% predicted), but it overpredicts velocities:
- by up to 44% for dwarfs,
- by 30–54% for spirals,
- by 3–38% for clusters.

MOND fits spirals better; MiHsC fits clusters better.

> Text and page numbers are from arXiv v1 (Jul 2012), stored as `paper.pdf`.

## Key claims
- A star's acceleration relative to nearby matter splits into a mean rotational part *a* and a varying local part *a′*. At the galaxy's edge, *a′* is assumed to sit at the MiHsC minimum 2c²/Θ.
- This gives a Tully–Fisher law v⁴ = GM|a′|, with no adjustable parameter. MOND needs the fitted a₀.
- It applies to dwarfs, spirals and clusters "within error bars, from the baryonic mass only", but "tends to overpredict the velocities by between a third and a half".
- MOND underestimates cluster velocities. MiHsC does better there and worse for spirals.
- Testable prediction: in galaxy outskirts, small-scale accelerations must rise to keep the total above 6.7 × 10⁻¹⁰ m/s².
- The derivation strictly applies only to rotationally supported discs, although the paper notes that clusters "seem" to be well predicted.

## Key equations
MiHsC inertia:
$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{|a|\Theta}\right) \sim m_g\left(1 - \frac{2c^2}{|a|\Theta}\right) $$
Orbit with split acceleration:
$$ \left(1 - \frac{2c^2}{(|a| + |a'|)\Theta}\right)a = \frac{GM}{r^2} $$
With a′ = 2c²/Θ and a ≪ a′:
$$ a^2 = \frac{GM|a'|}{r^2} \;\Rightarrow\; v^4 = GM|a'| = \frac{2GMc^2}{\Theta} $$
MOND comparison:
$$ v^4 = GMa_0 $$

## Data used
- Binned baryonic masses (gas plus stars) and outer circular velocities for dwarf galaxies, spiral galaxies and galaxy clusters, from McGaugh, Schombert, de Blok & Zagursky (2010, *ApJ* 708, L14; cited as 2009). The observed velocities carry a 30% error from extrapolation.
- Θ = 2.7 × 10²⁶ m, with a 9% uncertainty in H (Freedman 2001). Mass-to-light uncertainty is a factor of 2.

## Results & predictions
- MiHsC Tully–Fisher constant: a′ = 2c²/Θ = 6.7 ± 0.6 × 10⁻¹⁰ m/s². MOND uses a₀ = 1.2–2 × 10⁻¹⁰ m/s².
- Overprediction of v: dwarfs up to 44%; spirals 30–54%; clusters 3–38%. The paper says all are within the combined errors.
- Prediction: total local accelerations stay at or above 2c²/Θ at galaxy edges.

## Figures
*Figure (local only): Fig. 1 — Observed outer rotation velocity against baryonic mass for binned dwarfs, spirals and clusters (McGaugh et al.; black circles, solid line), with MiHsC (dashed) and MOND for a₀ = 1.2 and 2 × 10⁻¹⁰ m/s² (dotted) (p. 7).*

## Notable quotes
> "MiHsC … can predict the rotation velocity of dwarf galaxies, spiral galaxies and galaxy clusters within error bars, from the baryonic mass only, and with no adjustable parameters (see Eq. 9), but tends to overpredict the velocities by between a third and a half." (p. 5)

> "MoND performs better for spirals and MiHsC performs better for galaxy clusters." (p. 5)

## Criticisms & responses
- **Systematic overprediction.** The paper itself reports this. The MiHsC constant 2c²/Θ is about 3–6 times MOND's empirically fitted a₀. Since v ∝ (constant)^(1/4), this gives velocities roughly 30–50% too high for spirals. The agreement relies on the stated 30% and 20% error bars.
- **Ad hoc a′ assumption.** The step that sets the edge-of-galaxy local acceleration a′ equal to the minimum 2c²/Θ is a modelling assumption, not derived in the paper.
- **Later re-evaluations.** McCulloch's own later SPARC comparison is [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md). For a general critique of QI's foundations and galaxy predictions, see Renda (2019), [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).
- **Cluster comparison.** MOND's well-known cluster deficit (Sanders 2002/2003; Aguirre et al. 2001) is cited as an advantage for MiHsC. The comparison uses coarse bins only.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [dwarf-galaxies](../../02-evidence/dwarf-galaxies.md), [cosmology](../../02-evidence/cosmology.md)
- Sources:
  - [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md)
  - [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md)
  - [2017-mcculloch-dwarf-galaxies](../2017-mcculloch-dwarf-galaxies/README.md)
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
  - [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
