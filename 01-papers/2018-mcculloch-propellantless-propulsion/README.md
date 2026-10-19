---
title: "Propellant-less Propulsion from Quantized Inertia"
authors: [Michael Edward McCulloch]
year: 2018
type: paper
venue: "Journal of Space Exploration 7(3), 1-7"
doi:
arxiv:
url: "https://www.tsijournals.com/articles/propellantless-propulsion-from-quantized-inertia-13923.html"
open_access: true
license: all-rights-reserved
files: [paper.pdf, figures/fig-2-woodward-asymmetric-capacitor.png]
status: supports
tags: [propulsion, emdrive, review]
---

# Propellant-less Propulsion from Quantized Inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [source](https://www.tsijournals.com/articles/propellantless-propulsion-from-quantized-inertia-13923.html).

**Citation:** McCulloch, M. E. (2018). *Propellant-less Propulsion from Quantized Inertia*. Journal of Space Exploration, 7(3), 151 (pp. 1–7). Trade Science Inc. https://www.tsijournals.com/articles/propellantless-propulsion-from-quantized-inertia-13923.html (received 20 Nov 2018, published 20 Dec 2018).

**TL;DR:** The paper derives one QI thrust formula from the uncertainty principle, F = (PQL/2c)(1/Δx_left − 1/Δx_right), and applies it to three kinds of claimed propellantless thrusters: Shawyer's emdrive, the Woodward / Mach Effect Thruster, and a NASA asymmetric capacitor tested in vacuum. It reports order-of-magnitude agreement with the reported thrusts in all three cases. For the Mach Effect Thruster, it says Woodward's own theory underestimates the thrust by a factor of 10–1000.

## Key claims
- QI says horizons truncate the position uncertainty Δx differently in different directions. This produces a net force from "quantum jitter", and asymmetric conducting structures should feel thrust toward the side that damps Unruh waves more.
- A Casimir-like V shape should move toward its narrow end. The emdrive (a truncated cone) is described as an example of this.
- QI predicts thrust from the Mach Effect Thruster (MET) better than Woodward's Mach-effect theory does.
- The paper says thrust from NASA's 2004 asymmetric-capacitor test in vacuum is reproduced to the right order.
- Proposed test: vary the drive frequency around the cavity resonance to maximise or reverse the thrust (via λ = 8c²/a). The paper notes that a symmetric arrangement (Fearn & Woodward 2013) produced no thrust, "as QI would predict".

## Key equations
$$ \Delta p\,\Delta x \ge \frac{\hbar}{2} \;\;\rightarrow\;\; \Delta \bar F = \frac{E}{2\,\overline{\Delta x}} $$
Using $E = P\tau$ with $\tau = QL/c$:
$$ \Delta \bar F = \frac{PQL}{2c\,\Delta x}, \qquad F = \Delta F_{left} - \Delta F_{right} = \frac{PQL}{2c}\left(\frac{1}{\Delta x_{left}} - \frac{1}{\Delta x_{right}}\right) $$
Limiting case where one end blocks Unruh waves fully ($\Delta x_{left}=L/2$) and the other not at all ($\Delta x_{right}=\Theta$):
$$ F = \frac{PQ}{c} $$
Woodward's Mach-effect prediction as quoted (Eq. 8):
$$ F = f^3 L P \times 2.6\times10^{-13} = 0.05\ \mu\text{N} $$

## Data used
- Shawyer's first emdrive: P = 850 W, Q = 5900, L = 0.156 m, end widths 0.16 m and 0.1275 m. Observed thrust 16 mN.
- Mahood (1999) 1st-generation MET: P = 145 W, f = 11 kHz, Q estimated at 60 (range 60–190). Observed thrust of order 50 µN.
- Fearn et al. (2013) MET: P = 63 W (assumed), f = 32.35 kHz, observed 1.5 µN.
- NASA/CR-2004-213312 (Canning et al.) asymmetric capacitor at 5.5 × 10⁻⁵ Torr, as reported by Martins & Pinheiro (2011): 44 kV, plate gap 0.0635 m, plate width 0.03 m. Observed force 14 mN, direction "unspecified".

## Results & predictions
| Device | Observed | Woodward theory | QI prediction |
|---|---|---|---|
| Shawyer emdrive (Eq. 7) | 16 mN | — | 4.2 mN |
| Mahood 1999 MET | ~50 µN | 0.05 µN | 29–92 µN |
| Fearn et al. 2013 MET | 1.5 µN | 0.1 µN | 12.6–40 µN |
| NASA asymmetric capacitor (Eq. 14) | 14 mN | — | 12 mN |

- The paper says the QI value for Fearn et al. is too high, and attributes this to the assumption that the end caps block Unruh waves completely or not at all.
- For the capacitor, the electromagnetic Q estimate (Q = 2πfE/P) for the MET gives 53.8, which the paper says is consistent with the assumed Q of about 60.

## Figures
*Figure (local only): Fig. 2 — (a) Simplified Woodward / Mach Effect Thruster, with thrust toward the thicker brass cap; (b) an asymmetric capacitor. Fig. 1 (emdrive schematic) is on page 3. (Rendered page 4 of the PDF.)*

## Notable quotes
> "thrust effects from asymmetric capacitors (including the Woodward effect) can also be predicted to the right order of magnitude." (abstract, p. 1)

> "The predictions are of the correct order of magnitude in all three cases." (p. 6)

> "Although quantized inertia predicts that the direction of thrust should be towards the larger capacitor plate, the observed direction was not explicitly reported" (p. 6)

## Criticisms & responses
- **Emdrive:** later high-precision tests by Tajmar's group at TU Dresden attributed the apparent emdrive thrust to thermal and electromagnetic artefacts and set upper limits far below the earlier claims. See [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md) and [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md).
- **Asymmetric capacitors:** Tajmar's group tested capacitor thrust claims linked to QI and reported null results. See [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md).
- **Mach Effect Thruster:** the Dresden SpaceDrive project also studied METs. See [2018-tajmar-spacedrive](../../04-experiments/2018-tajmar-spacedrive/README.md) and [2019-kossling-spacedrive-balance](../../04-experiments/2019-kossling-spacedrive-balance/README.md).
- Methodological note (factual): the paper itself says that Q values for the MET are estimated rather than measured, and that the observed MET thrust was only given to order of magnitude.
- The general theoretical critique of QI is in [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md), [2015-mcculloch-emdrive-pip](../2015-mcculloch-emdrive-pip/README.md), [2017-mcculloch-emdrives-dielectrics](../2017-mcculloch-emdrives-dielectrics/README.md), [2017-taylor-laser-resonators](../2017-taylor-laser-resonators/README.md), [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md), [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md), [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2021-mcculloch-symmetric-capacitors](../2021-mcculloch-symmetric-capacitors/README.md)
