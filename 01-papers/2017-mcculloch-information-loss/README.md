---
title: Modified inertial mass from information loss
authors: [Michael E. McCulloch, Jaume Giné]
year: 2017
type: paper
venue: "Modern Physics Letters A 32(28), 1750148"
doi: 10.1142/S0217732317501486
arxiv:
url: "https://doi.org/10.1142/S0217732317501486"
open_access: true
license: author-manuscript
files: [paper.pdf]
status: supports
tags: [coauthored-with-mcculloch, derivation, information-theory]
---

# Modified inertial mass from information loss

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`author-manuscript`) does not permit redistribution. Read the paper at [doi:10.1142/S0217732317501486](https://doi.org/10.1142/S0217732317501486).

**Citation:** McCulloch, M. E. & Giné, J. (2017). *Modified inertial mass from information loss*. Modern Physics Letters A 32(28), 1750148. https://doi.org/10.1142/S0217732317501486. Accepted manuscript: Plymouth PEARL, http://hdl.handle.net/10026.1/10355 (repository date 2017-09-14).

**About the stored PDF:** `paper.pdf` is the authors' accepted manuscript from the University of Plymouth PEARL repository, not the World Scientific version of record. It has 10 PDF pages: **two** repository cover pages (PDF pp. 1–2), then the 8-page manuscript, which carries its own page numbers 1–8 (manuscript p. N = PDF p. N + 2). The manuscript is dated "November 30, 2017" on its title page. Page references below are **manuscript pages**. The cover sheet states that there is no open licence and that the published version should be cited; wording, equation numbering and pagination may differ from the journal version.

**TL;DR:** QI says inertia comes from Unruh radiation made inhomogeneous by Rindler horizons (giving standard inertia) or the Hubble horizon (giving galaxy rotation without dark matter and cosmic acceleration without dark energy). This paper proposes an alternative derivation from conservation of energy + mass + information ("EMI"), using Landauer's principle and a holographic count of Planck areas on horizons. When an object accelerates, the horizon behind it shrinks from half the Hubble sphere to a Rindler horizon, information is lost, and the corresponding mass–energy dm = (4/3) m (1 − 2c²/aΘ) ln 2 is released. The prefactor (4/3) ln 2 ≈ 0.92 lets the authors say QI is recovered "within 8%", but only near the minimum acceleration a ≈ 2c²/Θ. They also derive a maximum acceleration ~1.4 × 10⁵² m/s², predict quantised accelerations at very high a, and offer a numerical coincidence with the cosmological constant problem.

## Key claims
- What is conserved is the sum of energy–mass (E = mc²) and information, called EMI (manuscript p. 2).
- Landauer's principle (E = kT ln 2 per erased bit, cited as experimentally confirmed by Bérut et al. 2012 and Jun et al. 2014) converts lost horizon information into mass–energy (pp. 2–3).
- Holographic assumption: the information content is the number of Planck areas on the nearest horizon. Before acceleration the rear horizon is half the Hubble horizon; once accelerating it shrinks to a Rindler horizon, assumed for simplicity to be a hemisphere of radius d = c²/a (p. 3).
- The result reproduces the MiHsC formula up to the factor (4/3) ln 2 ≈ 0.92, but "is only valid when 2c²/aΘ − 1 = small", i.e. "for cosmologically-low accelerations" (p. 4).
- The authors name the hemispherical Rindler horizon as "one definite source of error" that may explain the different numerical factor; the true horizon shape needs a better model (p. 4).
- Since the Rindler horizon cannot be smaller than one Planck area, there is a maximum acceleration (p. 5), alongside MiHsC's existing minimum acceleration 2c²/Θ ∼ 7 × 10⁻¹⁰ m/s².
- Proposed test: accelerations (and inertial mass) should be quantised at very high accelerations, because the horizon can only shrink by whole Planck areas (pp. 5–6). Papini et al. are cited as suggesting light in cavities and type I superconductors may reach such accelerations.
- Cosmological constant: the relative jump size for the cosmic horizon, ~10⁻¹²⁵, is "similar to" the observed ratio of cosmological to Planck energy density, ~10⁻¹²² (p. 6).

## Key equations
Transcribed from the manuscript (pp. 2–6). Θ is defined as "twice the Hubble distance" (p. 2) and R_U = Θ/2 is the Hubble-sphere radius.

MiHsC (eq. 1, p. 2):
$$m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) \qquad (1)$$

EMI conservation and the mass change (eqs. 2–3, p. 3):
$$m_1c^2 + kTN_1\ln 2 = m_2c^2 + kTN_2\ln 2 \qquad (2)$$
$$m_2 - m_1 = dm = \frac{kT}{c^2}(N_1 - N_2)\ln 2 = \frac{kT}{c^2}N_1\left(1 - \frac{N_2}{N_1}\right)\ln 2 \qquad (3)$$

Planck-area counts for half the Hubble horizon and a hemispherical Rindler horizon (eqs. 4–5, p. 3):
$$N_1 = \frac{2\pi R_U^2}{l_P^2}, \qquad N_2 = \frac{2\pi d^2}{l_P^2} \qquad (4, 5)$$

With d = c²/a and R_U = Θ/2 (eqs. 6–7, pp. 3–4):
$$dm = \frac{kT}{c^2}N_1\left(1 - \frac{4c^4}{a^2\Theta^2}\right)\ln 2 \qquad (7)$$

Assuming a ≈ 2c²/Θ, using ρ ≈ −ln(1 − ρ) (eq. 8), equipartition (eq. 9), and ln(1 + x) ≈ x (eqs. 11–12) (p. 4):
$$E = \frac{3}{2}N_1kT = mc^2 \qquad (9)$$
$$dm = -\frac{4}{3}m\ln\left(\frac{2c^2}{a\Theta}\right)\ln 2 \;\;(10) \quad\Longrightarrow\quad dm = \frac{4}{3}m\left(1 - \frac{2c^2}{a\Theta}\right)\ln 2 \qquad (13)$$

Maximum acceleration from a one-Planck-area horizon (eqs. 14–15, p. 5):
$$2\pi d^2 \sim l_P^2,\quad d = \frac{c^2}{a_{max}} \;\Rightarrow\; a_{max} \sim \frac{\sqrt{2\pi}\,c^2}{l_P} \sim 1.4\times10^{52}\ \mathrm{m/s^2} \qquad (14, 15)$$

Relative acceleration jump for a Rindler horizon (eq. 16, p. 5) and for the cosmic horizon (eq. 17, p. 6):
$$J = \frac{l_P^2}{2\pi d^2} = \frac{l_P^2a^2}{2\pi c^4} = 5\times10^{-105}\,a^2, \qquad J = \frac{l_P^2}{4\pi\Theta^2} \qquad (16, 17)$$

## Data used
- None (theoretical). The only numerical inputs are physical constants and, in eq. (17), "the co-moving cosmic diameter: Θ = 8.8 × 10²⁶ m" (p. 6).

## Results & predictions
- Alternative derivation of MiHsC: dm = (4/3)(1 − 2c²/aΘ) m ln 2, a prefactor of ≈ 0.92 relative to eq. (1), "within 8%" (pp. 4, 6). Valid only near a ≈ 2c²/Θ.
- Maximum acceleration a_max ∼ 1.4 × 10⁵² m/s² (eq. 15), said to be close to Caianiello's maximal acceleration from quantum mechanics and to cure black-hole divergences noted by 't Hooft and Susskind & Uglum (p. 5).
- Minimum acceleration (existing MiHsC result) 2c²/Θ ∼ 7 × 10⁻¹⁰ m/s², said to agree with the observed cosmic acceleration (p. 5).
- Acceleration quantisation: J ≈ 5 × 10⁻¹⁰⁵ a², i.e. ~10⁻¹⁰³ for terrestrial accelerations and → 1 near a_max (p. 5). Not testable in practice except at extreme accelerations.
- Cosmic-horizon jump: J = 2.63 × 10⁻¹²⁵ with Θ = 8.8 × 10²⁶ m, compared with the ~10⁻¹²² cosmological-constant ratio (p. 6).
- Editorial check: √(2π) c²/l_P = 2.507 × 8.99 × 10¹⁶ / 1.616 × 10⁻³⁵ ≈ 1.39 × 10⁵² m/s² ✓. l_P²/(2πc⁴) ≈ 5.1 × 10⁻¹⁰⁵ ✓. l_P²/(4πΘ²) with Θ = 8.8 × 10²⁶ m ≈ 2.7 × 10⁻¹²⁵ (paper: 2.63 × 10⁻¹²⁵) ✓ within rounding.
- Editorial check (Θ inconsistency): the minimum acceleration 2c²/Θ ∼ 7 × 10⁻¹⁰ m/s² on p. 5 corresponds to the older Θ ≈ 2.6 × 10²⁶ m; with the Θ = 8.8 × 10²⁶ m used on p. 6 it would be ≈ 2.0 × 10⁻¹⁰ m/s². The paper uses both values without comment (see [equations §7](../../00-overview/equations.md)).
- Editorial check (regime of agreement): eq. (13) and eq. (1) are both proportional to (1 − 2c²/aΘ), so they agree in functional form; but the derivation's approximations (eq. 8 and eq. 12) hold only where that bracket is small, i.e. where both expressions are close to zero. Agreement at ordinary (high) accelerations, where m_i ≈ m, is not derived. Also, eq. (13) is the mass–energy *released*, which the paper identifies with the modified inertial mass without a separate argument; the ambient temperature T cancels via the equipartition assumption (eq. 9).

## Figures
None (the manuscript has no figures).

## Notable quotes
> "It is proposed here that this model can be derived in an alternative way by assuming that the sum of mass (M), energy (E) and the information content of horizons (I) is conserved (EMI)" (manuscript p. 1, abstract)

> "One definite source of error in this derivation, and which may account for the different numerical factors in Eq. 13 when compared to Eq. 1, is the assumption that the Rindler horizon is a sphere centred on the accelerating body." (manuscript p. 4)

> "It is shown here to be derivable, within 8%, by assuming the conservation of a sum of energy, mass and holographic information." (manuscript p. 6)

## Criticisms & responses
- This is one of several alternative derivations of the same formula: uncertainty principle ([2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md)), Unruh temperatures ([2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md)), and information theory ([2020-mcculloch-information-theory](../2020-mcculloch-information-theory/README.md)). Critics argue that QI lacks a single consistent theoretical framework, for example in a relativistic field-theory form. See [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).
- The derivation itself flags its limits: a hemispherical Rindler horizon, validity only at cosmologically low accelerations, and an 8% mismatch in the prefactor. See also the editorial checks above on the Θ values and the regime of agreement.
- > [!UNVERIFIED] No critique specific to this paper was found.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md), [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources:
  - [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md)
  - [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md)
  - [2020-mcculloch-information-theory](../2020-mcculloch-information-theory/README.md) (later information-theoretic derivation)
  - [2017-gine-inertial-mass-holographic](../2017-gine-inertial-mass-holographic/README.md)
  - [2018-gine-hawking-unruh-uncertainty](../2018-gine-hawking-unruh-uncertainty/README.md)
