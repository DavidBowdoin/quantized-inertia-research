---
title: The redshift evolution of a0 in MUSE-DARK is degenerate with the choice of stellar mass
authors: [Anton Karpov]
year: 2026
type: preprint
venue: "Zenodo (preprint, v1)"
doi: 10.5281/zenodo.22278304
arxiv: null
url: "https://doi.org/10.5281/zenodo.22278304"
open_access: true
license: unknown
files: [paper.pdf]
status: neutral
tags: [galaxy-rotation, high-redshift, rar, mond, muse-dark]
---

# The redshift evolution of a0 in MUSE-DARK is degenerate with the choice of stellar mass

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`unknown`) does not permit redistribution. Read the paper at [doi:10.5281/zenodo.22278304](https://doi.org/10.5281/zenodo.22278304).

**Citation:** Karpov, A. (2026). *The redshift evolution of a0 in MUSE-DARK is degenerate with the choice of stellar mass*. Zenodo preprint v1, 3 September 2026. https://doi.org/10.5281/zenodo.22278304. Not peer reviewed; the author is an independent researcher.

**TL;DR:** A reanalysis of the MUSE-DARK III claim that the RAR scale rises with redshift. Rebuilding the rotation curves from the public release, the author finds that the rise appears with the survey's dynamically fitted stellar masses and disappears with the release's SED masses. The paper does not mention QI, but its result bears directly on QI's (1+z) prediction.

## Key claims
- The survey's dynamical disc masses fall below the SED masses increasingly with redshift, by −0.39 ± 0.11 dex between z = 0.53 and 1.31 at fixed mass (Sect. 5.1). This matches the +0.2 to +0.45 dex shifts that Ciocan et al. say would be needed for a constant a₀.
- On identical kinematic points, the slope of log a₀ between the extreme redshift bins is +0.22 with dynamical masses, −0.07 with SED masses and −0.15 to −0.35 with SED masses plus molecular gas (Sect. 5.2).
- Published a₀ zero points at z < 0.1 scatter by 0.176 dex between surveys, more than the claimed slope of 0.134 dex over Δz = 0.8 (Sect. 4).
- Treating galaxies rather than points as the independent units, the trend's significance is 2.5–5σ rather than the quoted 30σ (Sect. 7).
- In the author's words, the evolution "is not established", and neither is its absence; an independent molecular-gas measurement is needed (Sect. 10).

## Key equations
The author fits the McGaugh RAR, $g_{\rm obs}=g_{\rm bar}/[1-\exp(-\sqrt{g_{\rm bar}/a_0})]$, while holding the rebuilt total circular speed fixed and changing the baryonic mass budget (Sect. 3).

## Data used
- The public MUSE-DARK release, retrieved 2 September 2026: per-galaxy GalPaK3D parameter files for 126 galaxies, the halo-fit and photometric catalogues.
- A compiled table of published a₀ determinations at z < 0.1 (`a0_ladder.csv`).
- The close-pair catalogue of Ventou et al. 2019, as a merger proxy.

## Results & predictions
- The rebuild reproduces the release's rotation speed at 2 kpc (ratio 1.002) and the two lowest published bins within 20%. It does not reproduce the two highest bins, which come out 40–65% higher (Sect. 9).
- The author's statements are therefore about differences between mass budgets on identical points, not absolute values.

## Figures
No figures are stored.

## Notable quotes
> "Which estimate is correct is not decided here" (Abstract)

## Criticisms & responses
- Not peer reviewed. No response from the MUSE-DARK team is known.
- Our editorial [A6b](../../09-analysis/a6b-musedark-per-galaxy/README.md) reproduces these binned values within 4% when using the source's radial grid and mass bookkeeping. Its main calculation conserves total SED stellar mass when a bulge is present and tests the dependence on radial sampling.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2026-ciocan-muse-dark-rar](../2026-ciocan-muse-dark-rar/README.md), [2026-alcock-rar-scale-hubble](../2026-alcock-rar-scale-hubble/README.md), [2026-sentina-a0z-rc100](../2026-sentina-a0z-rc100/README.md)
- Analyses: [A6](../../09-analysis/a6-rar-redshift-evolution/README.md), [A6b](../../09-analysis/a6b-musedark-per-galaxy/README.md)
