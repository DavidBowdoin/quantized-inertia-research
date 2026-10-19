---
title: "Jupiter Mass Binary Objects Show a Minimum Acceleration"
authors: [Michael Edward McCulloch]
year: 2025
type: paper
venue: "Astronomy (MDPI) 5(1), 1"
doi: 10.3390/astronomy5010001
arxiv:
url: "https://doi.org/10.3390/astronomy5010001"
open_access: true
license: CC-BY-4.0
files: [paper.pdf, figures/fig-1-jumbo-accelerations.png]
status: supports
tags: [jumbos, wide-binaries, minimum-acceleration, jwst, orion]
---

# Jupiter Mass Binary Objects Show a Minimum Acceleration

**Citation:** McCulloch, M. E. (2025). *Jupiter Mass Binary Objects Show a Minimum Acceleration*. Astronomy, 5(1), 1 (Brief Report). https://doi.org/10.3390/astronomy5010001 (CC BY). Received 29 September 2025, accepted 12 December 2025, published 26 December 2025. The volume is dated 2026, and the author's blog cites the paper as 2026. The PDF was retrieved from MDPI's file server (mdpi-res.com).

**TL;DR:** The paper takes the 42 JuMBO pairs that Pearson & McCaughrean (2023) reported in JWST images of the Trapezium Cluster (separations 25–390 AU, masses 0.7–13 M_Jup). It computes their Newtonian mutual accelerations a = 2GM/r² and argues that these "level off" near QI's minimum 2c²/Θ = 2 × 10⁻¹⁰ m/s². Two pairs (JuMBOs 1 and 10) fall marginally below it. QI then predicts that the widest pairs (about 400 AU) should orbit up to about 70 m/s faster than Newtonian, which could be tested with Doppler spectroscopy. Funding came from Patreon crowdfunding.

## Key claims
- JuMBO mutual accelerations deviate from the Newtonian trend and level off around 2c²/Θ, "in exactly the same way as for galaxy rotations and wide binaries".
- Dark matter cannot explain anomalies on these scales "since it must stay spread out to explain the galactic cases".
- QI has an advantage over MOND because it predicts a₀ = 2c²/Θ rather than fitting it. QI has no external field effect.
- The paper acknowledges that "The QI theory may not yet be mathematically complete, as pointed out by [21]" (Renda 2019). Renda's modified form would affect some results, though less so at the minimum acceleration.
- On contamination, the paper cites Luhman (2024), who argued some JuMBOs could be reddened background sources. It counters that the Trapezium lies at galactic latitude −19.4°, so "contamination from background stars should be minimal".

## Key equations
$$ m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right), \qquad \Theta = 8.8\times10^{26}\ \mathrm{m} $$
Minimum mutual acceleration and the bound-system condition:
$$ a_{min} = \frac{2c^2}{\Theta}, \qquad \frac{GM}{r^2} > \frac{2c^2}{\Theta} $$
Dynamical acceleration with QI inertia:
$$ a = \frac{GM}{r^2} + \frac{2c^2}{\Theta} $$
Predicted orbital speed:
$$ v = \sqrt{\frac{GM}{r} + \frac{2c^2 r}{\Theta}} $$

## Data used
- Table 1 of Pearson & McCaughrean (2023, arXiv:[2310.01231](https://arxiv.org/abs/2310.01231)): 42 JuMBO pairs, with projected separations and estimated masses. The distance is 390 pc.
- Mass uncertainties are assumed to be 50%, based on the error bars in their Fig. 4, which gives 50% uncertainty in acceleration.
- The paper uses projected separations directly, with no deprojection. Accelerations use M as the average mass of the two objects in a pair.

## Results & predictions
- Newtonian mutual accelerations decrease with separation and "level off around a minimum of 2 × 10⁻¹⁰ m/s²". JuMBOs 1 and 10 lie marginally below this.
- QI dynamical accelerations (Eq. 6) all lie above 2c²/Θ. The paper notes this "is not surprising given the form of Equation (6)".
- Excess orbital speed predicted by QI: rises from about 0 at 50 AU to "almost 70 m/s" at about 400 AU. It is potentially measurable with HARPS-class spectrographs (1 m/s resolution), given enough spatial and spectral resolution.

## Figures
![Fig. 1 — (a) Mutual accelerations of the 42 JuMBOs against separation (AU), as predicted by Newtonian gravity (black) and by QI (blue), with error bars and the QI minimum 2c²/Θ (red line). (b) Excess orbital speed needed to keep mutual accelerations above the QI minimum. Rendered p. 3.](figures/fig-1-jumbo-accelerations.png)

## Notable quotes
> "Two of the pairs (JuMBOs 1 and 10) do have an acceleration that is marginally lower than the QI limit" (p. 3)

> "All these values level off above the QI minimum (2c²/Θ), which is not surprising given the form of Equation (6)" (p. 4)

> "many more observations need to be collected to confirm that the JuMBOs are indeed binary objects." (p. 5)

## Criticisms & responses
- **Nature of JuMBOs disputed:**
  - Luhman (2024, AJ 168, 230) re-analysed the JWST photometry. He concluded that many JuMBO candidates are probably reddened background sources, and that the photometry suggests at most one promising substellar binary, whose components do not approach Jupiter mass. The summary is via [Wikipedia: Jupiter-mass binary object](https://en.wikipedia.org/wiki/Jupiter-mass_binary_object).
  - A 2025 JWST/NIRSpec study of Orion brown-dwarf candidates ([arXiv:2507.03679](https://arxiv.org/abs/2507.03679)) reported that seven NIRSpec targets previously identified as JuMBOs are background sources rather than brown dwarfs.
  - > [!UNVERIFIED] Details of these two studies were taken from search summaries, not checked against their full texts.
- **Formation:** Portegies Zwart & Hochart (2025, Nat. Astron.), which the paper cites as its ref. 6, argue that wide JuMBOs cannot form by standard routes. The paper uses this as motivation.
- **Method (factual):**
  - The "levelling off" is in Newtonian accelerations computed from *projected* separations and photometric masses, with 50% assumed errors. No velocities are measured.
  - The plotted QI accelerations are bounded below by 2c²/Θ by construction (Eq. 6).
  - If many pairs are chance alignments, the separation–acceleration trend would not reflect bound dynamics.
- General QI critique: [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md), which the paper itself cites.

## Related
- Evidence: [wide-binaries](../../02-evidence/wide-binaries.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2024-mcculloch-proxima-centauri](../2024-mcculloch-proxima-centauri/README.md), [2019-mcculloch-wide-binaries](../2019-mcculloch-wide-binaries/README.md), [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md), [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md), [2023-chae-wide-binaries](../2023-chae-wide-binaries/README.md), [2023-lynch-accelerated-electron-thermometer](../2023-lynch-accelerated-electron-thermometer/README.md), [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
