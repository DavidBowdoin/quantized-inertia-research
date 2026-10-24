---
title: "Reproducibility package for “No strong redshift evolution of the radial acceleration scale out to z ≈ 2.5”"
authors: [Luigi Sentina]
year: 2026
type: preprint
venue: "Zenodo (reproducibility package v6.2; manuscript prepared for A&A)"
doi: 10.5281/zenodo.23442383
arxiv: null
url: "https://doi.org/10.5281/zenodo.23442383"
open_access: true
license: CC-BY-4.0
files: []
status: neutral
tags: [galaxy-rotation, high-redshift, rar, mond, rc100, muse-dark]
---

# Reproducibility package for "No strong redshift evolution of the radial acceleration scale out to z ≈ 2.5"

**Citation:** Sentina, L. (2026). *Reproducibility package for "No strong redshift evolution of the radial acceleration scale out to z ≈ 2.5"*. Zenodo, v6.2, 20 October 2026. https://doi.org/10.5281/zenodo.23442383. Data and results CC BY 4.0, code MIT. Not peer reviewed; the author is an independent researcher.

**TL;DR:** Scripts, results and a transcribed input table for a manuscript that tests redshift laws for the RAR scale against the RC100 sample. The package change log states that strong Hubble tracking is "not supported" and a constant scale is "compatible/preferred among the strong laws tested". The manuscript itself is not in the package. It does not test QI.

> [!UNVERIFIED] The manuscript is not public; its claims are summarised from the package README, change log and stored results only.

## Key claims
- RC100 main test: with McGaugh's function and a free amplitude, Hubble tracking is worse than a constant scale by Δ(−ln L) ≈ 9.0 (`results/fdm_test.json`). The change log frames the result as strong H(z) tracking "not supported" (`CHANGELOG_V6.md`).
- A MUSE-DARK stress test on 89 public-product galaxies is described as "non-diagnostic" between a constant scale and Hubble tracking (`MUSE_DARK_SAMPLE_NOTE.md`).
- The package says it is not a reproduction of the 79-galaxy MUSE-DARK III sample.

## Key equations
The RC100 likelihood predicts $f_{\rm DM}=1-g_{\rm bar}/g_{\rm obs}$ at $R_e$, with $g_{\rm obs}=V_{\rm circ}^2/R_e$ and $g_{\rm bar}$ obtained by inverting the McGaugh RAR (`scripts/fdm_test.py`).

## Data used
- `data/rc100_table3.csv`: a transcription of Table B1 of [Nestor Shachar et al. 2023](../2023-nestorshachar-rc100-rotation-curves/README.md) (100 galaxies). The README notes that rows 67 and 83 are internally inconsistent in the published table.
- MUSE-DARK public-release products (not redistributed), with per-galaxy summaries in `results/`.

## Results & predictions
- Editorial check: we compared the transcription with the journal PDF. 99 rows match; row 87 (J0901+1814) differs in every fitted column. See [A6c](../../09-analysis/a6c-rc100-qi/README.md).

## Figures
No figures are stored.

## Notable quotes
> "The MUSE-DARK calculations archived here are a statistical/methodological stress test of public model products." (`MUSE_DARK_SAMPLE_NOTE.md`)

## Criticisms & responses
- Not peer reviewed. The README discloses that blind re-implementations and audits were written with Claude (Anthropic) and ChatGPT (OpenAI).
- The author's earlier Zenodo record (July 2026, 10.5281/zenodo.21442845) proposes a "composite horizon law" for the scale's redshift evolution, so the author has a competing model.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2023-nestorshachar-rc100-rotation-curves](../2023-nestorshachar-rc100-rotation-curves/README.md), [2026-ciocan-muse-dark-rar](../2026-ciocan-muse-dark-rar/README.md), [2026-karpov-musedark-a0z-audit](../2026-karpov-musedark-a0z-audit/README.md)
- Analyses: [A6b](../../09-analysis/a6b-musedark-per-galaxy/README.md), [A6c](../../09-analysis/a6c-rc100-qi/README.md)
