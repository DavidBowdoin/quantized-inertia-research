---
title: Quantised inertia from relativity and the uncertainty principle
authors: [Michael E. McCulloch]
year: 2016
type: paper
venue: "EPL (Europhysics Letters) 115(6), 69001"
doi: 10.1209/0295-5075/115/69001
arxiv: 1610.06787
url: "https://doi.org/10.1209/0295-5075/115/69001"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf]
status: supports
tags: [derivation, gravity]
---

# Quantised inertia from relativity and the uncertainty principle

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1610.06787](https://arxiv.org/abs/1610.06787) · [doi:10.1209/0295-5075/115/69001](https://doi.org/10.1209/0295-5075/115/69001).

**Citation:** McCulloch, M. E. (2016). *Quantised inertia from relativity and the uncertainty principle*. EPL 115(6), 69001. https://doi.org/10.1209/0295-5075/115/69001. Preprint: [arXiv:1610.06787](https://arxiv.org/abs/1610.06787) (`paper.pdf` is the arXiv version).

**TL;DR:** The paper makes two assumptions. First, nature conserves mass-energy *plus* the Heisenberg energy uncertainty ħc/Δx. Second, relativistic horizons (the Rindler horizon from acceleration, or the cosmic horizon) set the position uncertainty Δx. From these McCulloch derives the MiHsC/QI inertia formula up to a factor 2πβ ≈ 1.26, and the inverse-square law of gravity (which needs G to be assumed). He also estimates electron, proton and Planck masses.

## Key claims
- Conserving mass-energy plus uncertainty energy, with Δx limited by horizons, gives an extra inertial mass that reproduces the MiHsC formula apart from a prefactor of 2πβ ≈ 1.26. The author puts that prefactor down to treating the Rindler horizon as a sphere (Sec. 3).
- Gravity: summing the uncertainty interactions between Planck-mass constituents of two bodies gives a force ∝ mM/r². This extends McCulloch (2014, Ap&SS 349, 957). The paper adds that only *attraction* releases energy (Sec. 2).
- The paper says the gravity derivation is partly circular: the correct G only comes out by assuming interactions between Planck masses, and the Planck mass is defined using G (Sec. 5).
- Setting Δx to the Compton wavelength, the nuclear radius or the Planck length gives particle masses close to the electron, proton/neutron and Planck masses (Sec. 4.1).
- The aim is to show inertia arising "from the interplay of relativity (horizons) and quantum mechanics (Unruh waves)".

## Key equations
MiHsC (Eq. 1), with Θ the diameter of the observable universe:
$$m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right)$$

Uncertainty-energy gravity (Eqs. 5, 9):
$$\Delta\bar{E} = \frac{\hbar c\, mM}{m_P^2\, \Delta\bar{x}}, \qquad F \sim \frac{\hbar c}{m_P^2}\frac{mM}{r^2}$$

Conservation of mass-energy plus uncertainty energy (Eqs. 13–14):
$$m_1c^2 + \frac{\hbar c}{\Delta x_1} = m_2c^2 + \frac{\hbar c}{\Delta x_2}, \qquad dm = \frac{\hbar}{c}\left(\frac{1}{\Delta x_2} - \frac{1}{\Delta x_1}\right)$$

With Δx₁ = Θ/2 (cosmic horizon) and Δx₂ = c²/a (Rindler horizon) (Eqs. 17, 20):
$$dm = \frac{\hbar a}{c^3}\left(1 - \frac{2c^2}{a\Theta}\right) \;\Rightarrow\; dm = 2\pi\beta\, m\left(1 - \frac{2c^2}{a\Theta}\right)$$

Electron mass from the Compton wavelength (Eq. 23):
$$dm = \frac{\hbar}{c\lambda_C} = 9.1\times10^{-31}\ \text{kg}$$

## Data used
- No observational data sets. Only physical constants: Compton wavelength 2.426×10⁻¹² m, hydrogen nuclear radius 1.75×10⁻¹⁵ m, Planck length 1.616×10⁻³⁵ m, and Wien's β = 0.2.

## Results & predictions
- Inertia formula recovered up to a factor **2πβ ≈ 1.26**.
- Electron: **9.1 × 10⁻³¹ kg**, "very close" to the measured value.
- Proton/neutron (Δx = 1.75×10⁻¹⁵ m): **1.3 × 10⁻²⁷ kg**. Observed: 1.67 × 10⁻²⁷ kg.
- Planck length scale: 1.4 × 10⁻⁷ kg. Using 2πl_P: **2.2 × 10⁻⁸ kg**, compared with the Planck mass of 2.2176 × 10⁻⁸ kg.
- A tiny correction to the proton mass, ~41 orders of magnitude below the main term.
- The paper suggests no new experimental test.

## Figures
No figures in the paper.

## Notable quotes
> "if we assume that what is conserved in nature is not simply mass-energy, but rather mass-energy plus the energy uncertainty of the uncertainty principle" (p. 1, Abstract)

> "this last part of the derivation involves some circular reasoning since the Planck mass is defined using the value for G" (p. 8)

> "This is the same as Eq. 1, except for the initial factor of 2πβ ∼ 1.26 which could be due to the crudity of this model" (p. 6)

## Criticisms & responses
- **Self-acknowledged.** The derivation of G is circular (Sec. 5), and the prefactor 2πβ is unexplained.
- **Hand-picked scales, and ħ vs h.** The particle-mass "predictions" use hand-chosen length scales (Compton wavelength, nuclear radius, 2πl_P). Editorial arithmetic check, not a published critique: the printed numbers match h/(cΔx), not the ħ/(cΔx) written in Eqs. 21–26. For example, h/(c·2.426×10⁻¹² m) = 9.1×10⁻³¹ kg, while ħ/(c·2.426×10⁻¹² m) = 1.45×10⁻³¹ kg. Using h, the electron result is the definition of the Compton wavelength (λ_C = h/m_e c) rather than a prediction. Similarly, the "2πl_P" case is just ħ/(cl_P), which is the (non-reduced) Planck mass by definition.

  > [!UNVERIFIED] No published critique of this specific point was found.

- **General critique.** Renda (2019) published a critical analysis of QI's foundations, including its use of Unruh radiation and horizon arguments: [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).
- **Later rederivations.** McCulloch and co-authors gave alternative derivations of QI (information loss, Unruh temperatures, uncertainty principle with Casimir effects). See [2017-mcculloch-information-loss](../2017-mcculloch-information-loss/README.md), [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md) and [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md).

## Related
- Evidence: [derivation](../../02-evidence/derivation.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md)
- Sources:
  - [2014-mcculloch-gravity-uncertainty](../2014-mcculloch-gravity-uncertainty/README.md) (precursor gravity derivation)
  - [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md)
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
  - [2018-gine-hawking-unruh-uncertainty](../2018-gine-hawking-unruh-uncertainty/README.md)
  - [2018-haug-mcculloch-derivation](../2018-haug-mcculloch-derivation/README.md)
  - [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
