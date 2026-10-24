---
title: "RC100: Rotation Curves of 100 Massive Star-forming Galaxies at z = 0.6–2.5 Reveal Little Dark Matter on Galactic Scales"
authors: [A. Nestor Shachar, S. H. Price, N. M. Förster Schreiber, R. Genzel, T. T. Shimizu, L. J. Tacconi, H. Übler, A. Burkert, R. I. Davies, A. Dekel, R. Herrera-Camus, L. L. Lee, D. Liu, D. Lutz, T. Naab, R. Neri, A. Renzini, R. Saglia, K. F. Schuster, A. Sternberg, E. Wisnioski, S. Wuyts]
year: 2023
type: paper
venue: "The Astrophysical Journal 944, 78"
doi: 10.3847/1538-4357/aca9cf
arxiv: 2209.12199
url: "https://doi.org/10.3847/1538-4357/aca9cf"
open_access: true
license: CC-BY-4.0
files: [paper.pdf, table-b1-errors.csv]
status: neutral
tags: [galaxy-rotation, high-redshift, dark-matter]
---

# RC100: Rotation Curves of 100 Massive Star-forming Galaxies at z = 0.6–2.5 Reveal Little Dark Matter on Galactic Scales

**Citation:** Nestor Shachar, A., Price, S. H., Förster Schreiber, N. M., Genzel, R., et al. (2023). *RC100: Rotation Curves of 100 Massive Star-forming Galaxies at z = 0.6–2.5 Reveal Little Dark Matter on Galactic Scales*. The Astrophysical Journal 944, 78. https://doi.org/10.3847/1538-4357/aca9cf. Preprint: [arXiv:2209.12199](https://arxiv.org/abs/2209.12199) (`paper.pdf` is the journal version, CC BY 4.0).

**TL;DR:** Hα and CO rotation curves of 100 massive star-forming discs at z ≈ 0.6–2.5, fitted with discs, bulges and dark-matter halos including pressure support. The dark-matter fraction inside the effective radius falls with redshift, and many z ≈ 2 discs are baryon dominated. The paper interprets this within ΛCDM and does not mention QI or MOND scales.

## Key claims
- The median dark-matter fraction f_DM(R_e) = V²_DM/V²_circ is 0.38 ± 0.23 at z ≈ 1 and 0.27 ± 0.18 at z ≈ 2 (Abstract).
- A third of the galaxies at z ≈ 1, and half at z ≈ 2, are maximal discs with f_DM(R_e) < 0.28 (Abstract).
- At z ≈ 2 there is about 40% less dark matter within R_e than expected from cosmological stellar-mass–halo-mass relations (Abstract).
- Dark-matter fractions correlate inversely with baryonic surface density. The authors suggest cored inner halos, produced by feedback or dynamical friction (Abstract, Sect. 4).

## Key equations
The paper defines $f_{\rm DM}(R_e)=V_{\rm DM}^2(R_e)/V_{\rm circ}^2(R_e)$ (Sect. 3).

## Data used
- SINFONI and KMOS (VLT), LUCI (LBT), NOEMA and ALMA kinematics of 100 galaxies with rotation curves extending to several effective radii.
- Forward models of turbulent rotating discs with bulges in dark-matter halos, fitted to the major-axis kinematics. Free parameters are log M_baryon, R_e, σ₀ and f_DM(R_e).
- Table B1 lists the best-fit parameters for every galaxy, including V_circ(R_e) with 20% uncertainties for nearly all objects. The lensed galaxy J0901+1814 uses values from the de-lensed model of Liu et al. 2023 (Sect. 3).
- [Table B1 uncertainty columns](table-b1-errors.csv): transcription of the published R_e and V_circ errors for all 100 objects (pp. 17–21, CC BY 4.0). Units are kpc and km s⁻¹; IDs follow Table B1. These supplement Sentina's table, which omits both columns.

## Results & predictions
- Not a QI paper. Its per-galaxy table is the input for our [A6c](../../09-analysis/a6c-rc100-qi/README.md) test of QI's redshift law, following [Sentina 2026](../2026-sentina-a0z-rc100/README.md).

## Figures
No figures are stored.

## Notable quotes
> "a third (half) of all galaxies are maximal disks with fDM(Re) < 0.28" (Abstract)

## Criticisms & responses
- Editorial: f_DM comes from a halo-based decomposition with mass priors. A modified-dynamics fit would not necessarily return the same fractions.
- McGaugh's 2025 blog uses RC100 to argue against a₀ evolving with H(z) ([2025-mcgaugh-kinematics-high-redshift](../../07-media/2025-mcgaugh-kinematics-high-redshift/README.md)).

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2026-sentina-a0z-rc100](../2026-sentina-a0z-rc100/README.md), [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md) (QI's (1+z) prediction)
- Analysis: [A6c](../../09-analysis/a6c-rc100-qi/README.md)
