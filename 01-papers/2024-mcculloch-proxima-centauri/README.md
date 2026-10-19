---
title: "Testing quantized inertia on Proxima Centauri"
authors: [Michael Edward McCulloch]
year: 2024
type: paper
venue: "Monthly Notices of the Royal Astronomical Society: Letters 532(1), L67-L69"
doi: 10.1093/mnrasl/slae047
arxiv:
url: "https://doi.org/10.1093/mnrasl/slae047"
open_access: true
files: []
status: supports
tags: [wide-binaries, alpha-centauri, mond, proxima-centauri]
---

# Testing quantized inertia on Proxima Centauri

**Citation:** McCulloch, M. E. (2024). *Testing quantized inertia on Proxima Centauri*. Monthly Notices of the Royal Astronomical Society: Letters, 532(1), L67–L69 (published 20 May 2024). https://doi.org/10.1093/mnrasl/slae047 (open access).

> [!UNVERIFIED] PDF not retrievable. The OUP PDF link (academic.oup.com/…/slae047.pdf) returned a bot-check HTML page rather than a PDF, so no copy is stored. This README draws on two sources. The abstract comes from Crossref. Equations and numbers come from the publisher's HTML full text, read through an automated fetch and summary. Neither has been checked against the typeset PDF, and no page numbers are given. The numbers were re-computed here from the stated inputs and are consistent with them.

**TL;DR:** Proxima Centauri appears to orbit α Cen A+B too fast to be bound by their visible mass alone: 0.53 ± 0.14 km/s observed (as cited) against 0.344 km/s Newtonian. Yet its co-motion and chemistry suggest it is bound. McCulloch applies QI's modified inertia. In the low-acceleration limit this gives v⁴ = 2GMc²/Θ, so v = 0.483 ± 0.01 km/s, within the observed error bars. He argues that dark matter, adding mass to A and B, and MOND (because of its external field effect) do not fix the problem.

## Key claims
- From the abstract: "the fast orbit of Proxima implies it is gravitationally unbound given the visible mass of A and B."
- This "cannot be fixed with the addition of dark matter, which must be uniform on such scales, or adding mass to A and B (their mass is well constrained) or by Modified Newtonian Dynamics."
- QI "predicts the observed orbital velocity, within the bounds of observational uncertainty, and binds Proxima, without the need for extra mass."
- Matching the observed speed in Newtonian gravity would need A+B's mass increased by about three times its stated uncertainty (per the HTML text).

## Key equations
As given in the HTML full text.
$$ m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) $$
$$ v = \sqrt{\frac{GM}{r}} \quad\text{(Newtonian)} $$
$$ v^4 = \frac{2GMc^2}{\Theta} \;\Rightarrow\; v = \left(\frac{2GMc^2}{\Theta}\right)^{1/4} \quad\text{(QI)} $$

## Data used
As reported in the HTML text, with the sources cited there.

| Quantity | Value | Cited source |
|---|---|---|
| Mass of α Cen A+B | 2.00 ± 0.11 M☉ | Anosova et al. (1994) |
| Mass of Proxima | 0.123 ± 0.006 M☉ | Ségransan et al. (2003) |
| Orbital radius of Proxima | 15,000 ± 700 AU | — |
| Distance | 1.30197 ± 0.00008 pc | Gaia Collaboration |
| Observed orbital velocity | 0.53 ± 0.14 km/s | as cited |
| Θ | 8.8 × 10²⁶ m | — |

## Results & predictions
- Newtonian: 0.344 ± 0.018 km/s.
- MOND (a₀ = 1.2 × 10⁻¹⁰ m/s², Beech 2009): 0.424 ± 0.001 km/s.
- QI: 0.483 ± 0.01 km/s, against 0.53 ± 0.14 km/s observed.
- These values were re-computed here from the listed inputs and are consistent.
- The paper notes that future Gaia astrometry of Proxima's orbit could test the models further.

## Figures
None stored (no PDF).

## Notable quotes
> "It is shown here that if QI is applied to Proxima Centauri in the same way, it predicts the observed orbital velocity, within the bounds of observational uncertainty, and binds Proxima, without the need for extra mass." (abstract)

## Criticisms & responses
- **Bound Newtonian orbit already reported:** [Kervella, Thévenin & Lovis (2017), A&A 598, L7](https://doi.org/10.1051/0004-6361/201629930) used HARPS absolute radial velocities and revised α Cen parameters. They concluded that "Proxima and α Cen are gravitationally bound with a high degree of confidence". They derived an orbital period of about 550,000 yr, eccentricity 0.50 (+0.08/−0.09), and apastron at about 13.0 kau.
  - That result conflicts with this letter's premise that Proxima is unbound under Newtonian gravity.
  - > [!UNVERIFIED] Whether the letter discusses Kervella et al. was not checked.
- **Proposed decisive test:** [Banik & Kroupa (2019), MNRAS 487, 1653](https://arxiv.org/abs/1906.08264) showed that Proxima's orbit differs significantly between Newton and MOND. They proposed a test with about 10 years of 0.5 μas-precision astrometry (Theia-class). So MOND is not ruled out by existing data on this system.
- **Single-system caveats (factual):** the letter tests one system, with a 26% uncertainty on the observed velocity. It assumes a circular orbit at the current separation, while Kervella et al. find e ≈ 0.5.
- General QI critique: [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).
- Earlier history: McCulloch's blog references list a 2015 "Testing quantised inertia on the Alpha Centauri system (to be submitted)" alongside Wertheimer & Laughlin (2006, AJ 132, 1995), "Are Proxima and Alpha Centauri gravitationally bound?".

## Related
- Evidence: [wide-binaries](../../02-evidence/wide-binaries.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2019-mcculloch-wide-binaries](../2019-mcculloch-wide-binaries/README.md), [2025-mcculloch-jupiter-mass-binaries](../2025-mcculloch-jupiter-mass-binaries/README.md), [2023-chae-wide-binaries](../2023-chae-wide-binaries/README.md), [2024-hernandez-wide-binary-review](../2024-hernandez-wide-binary-review/README.md), [2023-banik-gaia-dr3-wide-binaries](../../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md), [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
