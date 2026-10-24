---
title: Dark matter fraction in disk-like galaxies over the past 10 Gyr
authors: [Gauri Sharma, Glenn van de Ven, Paolo Salucci, Marco Martorano]
year: 2025
type: paper
venue: "Astronomy & Astrophysics 699, A164"
doi: 10.1051/0004-6361/202347922
arxiv: 2309.04541
url: "https://doi.org/10.1051/0004-6361/202347922"
open_access: true
license: CC-BY-4.0
files: [paper.pdf]
status: neutral
tags: [galaxy-rotation, high-redshift, dark-matter, kmos3d, kross]
---

# Dark matter fraction in disk-like galaxies over the past 10 Gyr

**Citation:** Sharma, G., van de Ven, G., Salucci, P. & Martorano, M. (2025). *Dark matter fraction in disk-like galaxies over the past 10 Gyr*. Astronomy & Astrophysics 699, A164. https://doi.org/10.1051/0004-6361/202347922. Preprint: [arXiv:2309.04541](https://arxiv.org/abs/2309.04541) (`paper.pdf` is the arXiv version, CC BY 4.0). Catalogues: [Zenodo 10.5281/zenodo.15458539](https://doi.org/10.5281/zenodo.15458539) (CC BY 4.0).

**TL;DR:** Hα kinematics of 263 star-forming discs at 0.6 ≤ z < 2.5 from the public KMOS3D, KGES and KROSS surveys, modelled in 3D and corrected for pressure support. Dark-matter fractions are computed without a halo model, by subtracting baryonic mass (photometry plus gas scaling relations) from dynamical mass at three radii. The fraction rises with radius and falls with redshift. The paper does not mention QI; its catalogues are the input to our [A6e](../../09-analysis/a6e-sharma-qi/README.md).

## Key claims
- At fixed redshift, the dark-matter fraction increases with radius, so the outskirts are dark-matter dominated, as in local discs (Abstract).
- The fraction decreases with increasing redshift, and on average remains above 50% within R_e and beyond (Abstract).
- Galaxies with log M★ ≤ 10 show stronger evolution (Abstract).
- About 22% of the sample has baryonic mass exceeding dynamical mass, which the authors attribute mainly to overestimated photometric stellar masses (Sect. 5).

## Key equations
Halo-independent dark-matter fraction: $f_{\rm DM}(<R) = 1 - M_{\rm bar}(<R)/M_{\rm dyn}(<R)$, with $M_{\rm bar} = M_\star + M_{\rm H_2} + 1.33\,M_{\rm HI}$ (Appendix D).

## Data used
- Public KMOS3D (73 galaxies), KGES (21) and KROSS (169) integral-field data, modelled with 3DBarolo (Sect. 3).
- Stellar masses and SFRs from SED fits; molecular gas from Tacconi et al. 2018 scalings and atomic gas from scaling relations, each with an extra 0.3 dex uncertainty (Sects. 2.4, 5).
- Radii R_e, R_opt = 1.89 R_e and R_out = 2.95 R_e; velocities are interpolated where a rotation curve does not reach a radius, with inflated errors (Sect. 3.3).

## Results & predictions
- Scaling relations between dark-matter fraction, baryon surface density and circular velocity at R_out, e.g. their Eq. 5 (Sect. 4).

## Figures
No figures are stored.

## Notable quotes
> "the outskirts of galaxies are dark matter dominated, similarly to local star-forming disk galaxies" (Abstract)

## Criticisms & responses
- The authors discuss their own systematics in detail (Sect. 5): photometric masses, gas scalings, interpolation of rotation curves and unphysical fractions.
- Editorial: in [A6e](../../09-analysis/a6e-sharma-qi/README.md), QI scales fitted at the same redshift differ by a factor of about 2.4 between KROSS and KMOS3D, so survey systematics dominate any redshift trend.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2023-nestorshachar-rc100-rotation-curves](../2023-nestorshachar-rc100-rotation-curves/README.md), [2017-ubler-tully-fisher-evolution](../2017-ubler-tully-fisher-evolution/README.md)
- Analysis: [A6e](../../09-analysis/a6e-sharma-qi/README.md)
