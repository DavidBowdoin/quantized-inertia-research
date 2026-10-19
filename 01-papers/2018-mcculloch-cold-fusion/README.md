---
title: "Can Cold Fusion Be Explained by Quantised Inertia?"
authors: [Michael Edward McCulloch]
year: 2018
type: paper
venue: "Progress in Physics 14(2), 63-65"
doi:
arxiv:
url: "https://progress-in-physics.com/2018/PP-53-02.PDF"
open_access: true
license: CC-BY-NC-ND-2.5
files: [paper.pdf, figures/fig-1-sheltering-schematic.png]
status: supports
tags: [lenr, cold-fusion, unruh-radiation]
---

# Can Cold Fusion Be Explained by Quantised Inertia?

<!-- local-only-note -->
> 📁 **Local only:** the figures rendered from this paper are kept out of the public repository (`CC-BY-NC-ND-2.5` does not permit derivatives). The PDF itself is included.

**Citation:** McCulloch, M. E. (2018). *Can Cold Fusion Be Explained by Quantised Inertia?* Progress in Physics, 14(2), 63–65. https://progress-in-physics.com/2018/PP-53-02.PDF (submitted 20 January 2018).

**TL;DR:** A three-page note. It applies the quantised inertia (QI) uncertainty-principle argument to nanoscale cracks in palladium. It claims that cracks narrower than 28 nm reach about 27,000 K, and that deuterons there shield each other from this thermal radiation. The result would be an attractive radiation-recoil force larger than the Coulomb repulsion at 1.6 × 10⁻¹⁵ m, which the paper offers as a possible mechanism for LENR / cold fusion.

## Key claims
- Successful LENR experiments have nanoscale cracks or defects in common (the paper cites Aoyama, and Storms).
- Confining a particle to a cavity of width D increases its momentum uncertainty. QI assumes this momentum "can become real", which gives an energy ħc/2D and a temperature T > ħc/3kD.
- Two deuterons in such a defect shelter each other from the thermal radiation. Each one absorbs radiation only on the side facing away from the other, so a net recoil force pushes them together.
- For cracks with D < 28 nm, this force beats the Coulomb repulsion at the strong-force distance d_s = 1.6 × 10⁻¹⁵ m.
- The inward force may help explain why LENR shows no neutrons. The paper says it "does not directly explain the lack of gamma rays".

## Key equations
Coulomb force between deuterons:
$$ F_C = \frac{q_P^2}{4\pi\varepsilon_0 d^2} $$
Uncertainty-principle energy and temperature in a cavity of width D:
$$ \Delta E > \frac{\hbar c}{2D}, \qquad T > \frac{\hbar c}{3kD} $$
Radiation recoil force:
$$ F_R = \frac{P}{c} = \frac{\sigma T^4}{c} $$
Condition $F_R > F_C$ at $d_s$, which gives the critical crack size:
$$ D < (4\pi\varepsilon_0\sigma)^{1/4}\,\frac{\hbar}{3k}\,c^{3/4}\,\sqrt{\frac{d_s}{q}} = 28\ \text{nm} $$
(Eq. 7. The exponents were checked by re-solving Eq. 6 for D.)

## Data used
- No new data. Literature values only: the Fleischmann–Pons excess-heat reports, Storms & Scanlan's X-ray observations during LENR, nanocrack formation in stressed Pd (Kim et al. 2016), and sonoluminescence temperatures (Brenner et al. 2002).

## Results & predictions
- Critical crack width: **D < 28 nm**. Temperature in such cracks: **ħc/3kD ≥ 27,000 K**.
- Prediction: metals with cracks of size D should emit radiation of wavelength about D. The paper notes that Storms & Scanlan saw nanometre-wavelength X-rays.
- Sonoluminescence: for a bubble of 0.5 µm, Eq. 4 gives about 1500 K. The paper compares this with measured apparent temperatures of 2300–5100 K.
- Prediction: a nanometal made with regular cracks smaller than 28 nm should produce LENR "far more uniformly".

## Figures
*Figure (local only): Fig. 1 — Schematic of two deuterons a distance d apart inside a crack of width D in a palladium lattice. Mutual sheltering creates a radiation-free zone between them, and the non-uniform thermal radiation pushes them together. (Rendered page 2 of the PDF.)*

## Notable quotes
> "quantised inertia predicts that in cracks in the metal with diameters less than 28 nm, the temperature is 27,000 K" (abstract, p. 63)

> "it does not directly explain the lack of gamma rays." (p. 64)

> "a nanometal manufactured with cracks of size 28 nm or less should produce LENR more uniformly." (p. 64)

## Criticisms & responses
- > [!UNVERIFIED] A brief search found no published critique or reply that addresses this paper specifically.
- General context: LENR / cold fusion is not accepted by mainstream physics, and reproducibility has been disputed since 1989. The paper itself notes "many unsuccessful" reproductions as well as successful ones.
- The broader QI critique applies to the step at the core of the argument, which treats uncertainty-principle momentum as real energy. See [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [other-anomalies](../../02-evidence/other-anomalies.md), [derivation](../../02-evidence/derivation.md)
- Sources: [2017-mcculloch-proton-radius](../2017-mcculloch-proton-radius/README.md) (the mutual-sheltering idea this paper builds on), [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md), [2014-mcculloch-toy-cosmology](../2014-mcculloch-toy-cosmology/README.md), [2020-mcculloch-nano-materials](../2020-mcculloch-nano-materials/README.md)
