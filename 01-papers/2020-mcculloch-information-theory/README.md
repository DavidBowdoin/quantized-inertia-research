---
title: "Quantised Inertia and Galaxy Rotation from Information Theory"
authors: [Michael Edward McCulloch]
year: 2020
type: paper
venue: "Advances in Astrophysics 5(4), 91-94"
doi: 10.22606/adap.2020.54002
arxiv:
url: "https://doi.org/10.22606/adap.2020.54002"
open_access: true
license: all-rights-reserved
files: [paper.pdf, figures/fig-1-horizon-bits-schematic.png]
status: supports
tags: [derivation, information-theory, galaxy-rotation]
---

# Quantised Inertia and Galaxy Rotation from Information Theory

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.22606/adap.2020.54002](https://doi.org/10.22606/adap.2020.54002).

**Citation:** McCulloch, M. E. (2020). *Quantised Inertia and Galaxy Rotation from Information Theory*. Advances in Astrophysics, 5(4), 91–94. Isaac Scientific Publishing. https://doi.org/10.22606/adap.2020.54002

**TL;DR:** A short theory paper that derives the QI modified-mass formula m′ = m(1 − 2c²/aΘ) from Landauer's principle. It counts "bits" as Planck lengths between an object and the horizon it sees. When the object accelerates, its Rindler horizon comes closer, bits are erased, and the energy released is identified with inertia. The paper presents this as a third route to QI, after the Unruh-gradient and uncertainty-principle derivations. The work was funded by DARPA grant HR001118C0125.

## Key claims
- Information is stored in the *space* between an object and its horizon, not on the horizon's area as in McCulloch & Giné 2017.
- When acceleration brings the Rindler horizon closer than the cosmic horizon, bits are erased. The second law then requires an energy release, which the paper says is "exactly the amount required for quantised inertia".
- The paper uses log₂ rather than ln in Landauer's principle, arguing that the natural log was a mathematical rather than physical choice and that experiments (Hong et al. 2016) are "ambiguous enough to allow both".
- The paper acknowledges that QI is "not yet mathematically complete as pointed out by [Renda 2019]". It also notes that attributing inertia to virtual photons "simply pushes the inertia problem further back".
- It says the 2017 area-based derivation gave Eq. 1 only to within 8%, and that the 2020 horizon-width fix had "no good justification".

## Key equations
QI modified inertia (Θ = 8.8 × 10²⁶ m):
$$ m' = m\left(1 - \frac{2c^2}{a\Theta}\right) $$
Landauer erasure energy (base-2 log):
$$ dE = kT\log_2 2, \qquad dE = kTN\log_2 2 = kTN = mc^2 $$
Bits to the cosmic and Rindler horizons:
$$ N_1 = \frac{\Theta}{2l_P}, \qquad N_2 = \frac{d_R}{l_P} = \frac{c^2}{a\,l_P} $$
$$ dE = kTN_1 - kTN_2 = mc^2 \;\Rightarrow\; M = \frac{kT\Theta}{2c^2 l_P}\left(1 - \frac{2c^2}{a\Theta}\right) $$
Dividing by the object length Θ/2l_P gives Eq. 9, which is identical in form to Eq. 1.

## Data used
- None. A theoretical derivation. Galaxy-rotation and wide-binary agreement are asserted by citing earlier papers (McCulloch 2012; McCulloch & Lucio 2019).

## Results & predictions
- Recovers the QI formula exactly (Eq. 9), compared with the earlier ~8% discrepancy of the area-based version.
- The paper makes no new quantitative prediction. Galaxy rotation and propellantless thrust are referred to earlier work.

## Figures
*Figure (local only): Fig. 1 — Schematic of an extended object that sees the cosmic horizon. When it accelerates left, a closer Rindler horizon appears, "some spatial bits are erased", and the energy released opposes the acceleration. (Rendered page 3 of the PDF.)*

## Notable quotes
> "QI can be derived from Landauer's principle by assuming that bits of information are stored in the distances between objects and the horizons they see." (abstract, p. 91)

> "The theory is not yet mathematically complete as pointed out by [13]" (p. 91; [13] = Renda 2019)

> "The derivation is simple and elegant." (p. 93)

## Criticisms & responses
- Factual notes on the derivation: the exact coefficient depends on two choices. One is replacing ln 2 with log₂ 2 = 1. The other is counting bits as horizon *distance* in Planck lengths (with the cosmic horizon taken as Θ/2) and then dividing by an object length of Θ/2l_P. The paper argues for these choices but does not derive them from first principles.
- A later revision, *Quantised Inertia from Information Theory (Corrected)* (ResearchGate, 2022, publication 345459726), appears to update this paper. > [!UNVERIFIED] The changes in that revision have not been checked here.
- The broader critique of QI's mathematical foundations is in [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md), which this paper cites.
- Venue: Isaac Scientific Publishing's *Advances in Astrophysics* is a small open-access journal. > [!UNVERIFIED] Its review standards were not assessed.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2017-mcculloch-information-loss](../2017-mcculloch-information-loss/README.md) (the area-based predecessor), [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md), [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md), [2012-mcculloch-galactic-scales](../2012-mcculloch-galactic-scales/README.md), [2019-mcculloch-wide-binaries](../2019-mcculloch-wide-binaries/README.md), [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
