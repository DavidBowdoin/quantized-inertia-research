---
title: "Can Nano-Materials Push Off the Vacuum?"
authors: [Michael Edward McCulloch]
year: 2020
type: paper
venue: "Progress in Physics 16(2), 92-93"
doi:
arxiv:
url: "https://progress-in-physics.com/2020/PP-60-02.PDF"
open_access: true
license: CC-BY-NC-ND-2.5
files: [paper.pdf, figures/fig-1-cavity.png]
status: supports
tags: [propulsion, nanotechnology, uncertainty-principle, asymmetric-cavity]
---

# Can Nano-Materials Push Off the Vacuum?

<!-- local-only-note -->
> 📁 **Local only:** the figures rendered from this paper are kept out of the public repository (`CC-BY-NC-ND-2.5` does not permit derivatives). The PDF itself is included.

**Citation:** McCulloch, M. E. (2020). *Can Nano-Materials Push Off the Vacuum?* Progress in Physics, 16(2), 92–93 (Issue 2, October 2020). PDF: https://progress-in-physics.com/2020/PP-60-02.PDF

**TL;DR:** A two-page note. It models one photon bouncing between the wide and narrow parts of an asymmetric metal double cavity and applies Heisenberg's uncertainty principle as an *equality* in each part. The result is a net force on the cavity. Setting this force equal to the cavity's weight, the note finds that a cavity of about 129 nm or smaller should levitate on the zero-point field alone, with no input power. It suggests that arrays of such nano-cavities could make a "self-thrusting material". The work acknowledges DARPA grant HR001118C0125.

## Key claims
- QI predicts that electromagnetic energy confined in an asymmetric cavity perceives a vacuum gradient and so produces a force on the cavity. This is the mechanism QI proposes for the emdrive.
- Below about 129 nm, the energy of the unexcited zero-point field alone (a single quantum, ħ) gives a thrust comparable to Earth's gravity.
- A material built from arrays of asymmetric nano-structures of this size or smaller "will levitate without input power".
- Caveat stated by the author: at these scales, thermal or plasmonic effects become important. Whether the approach works "will be dependent on these other effects cancelling out".

## Key equations
Uncertainty principle, taken as an equality, with the cavity size as Δx (wide part L, narrow part l):
$$ \Delta p_w = \frac{\hbar}{2L}, \qquad \Delta p_n = \frac{\hbar}{2l} $$
Force from the photon oscillating over distance d:
$$ F = \frac{\Delta p}{\Delta t} = \frac{c(\Delta p_n - \Delta p_w)}{d} = \frac{\hbar c}{2\left(\frac{L}{2}+\frac{l}{2}\right)}\left(\frac{1}{l}-\frac{1}{L}\right) $$
With l = L/2:
$$ F = ma = \frac{2\hbar c}{3L^2} $$
With the mass of two hollow spheres, m = 5πL²ρδ/4 (wall density ρ, thickness δ):
$$ L^2 = \frac{2\hbar c}{3ma} = \frac{8\hbar c}{15\pi L^2 \rho\delta a} \;\Rightarrow\; L = \sqrt[4]{\frac{8\hbar c}{15\pi\rho\delta a}} $$

## Data used
- No observational data are used. The inputs are illustrative: wall density ρ = 2000 kg/m³, wall thickness δ = 1 mm, and a = g = 9.8 m/s².

## Results & predictions
- L = 129 nm (Eq. 8). At this scale, the predicted zero-point-field thrust equals Earth-surface gravity for the stated wall parameters.
- The note states: "The smaller the cavity, the larger the predicted thrust."
- No experiment is reported or proposed in detail.

## Figures
*Figure (local only): Fig. 1 — The asymmetrical metal cavity: a wide sphere (size L) joined to a narrow one (size l), with a photon moving back and forth over distance d. Rendered page 92 (PDF p. 1).*

## Notable quotes
> "if we build an asymmetric metal cavity such as that shown in Figure 1, with its narrow end upwards and on a scale of 129 nm or less, then it should levitate simply from the already-present zero point field without any input power." (p. 93)

> "One difficulty will be that, on the nanoscales considered here, other thermal or plasmonic effects will become important" (p. 93)

## Criticisms & responses
- No published critique of this specific note was found in a brief search.
- **Factual observations on the derivation:**
  - The mass formula assumes the walls are 1 mm thick while the cavity is only 129 nm across. That means the walls would be thousands of times thicker than the cavity itself. The note does not discuss this geometric inconsistency.
  - The result also depends on two assumptions: that the uncertainty principle holds as an equality, and that Δx equals the cavity size.
- **Wider critiques:**
  - General critiques of QI's derivations: [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).
  - [Dickmann et al. 2023](../../03-criticism/2023-dickmann-casimir-contradicts/README.md) argued that QI's cavity-thrust picture contradicts the measured Casimir effect.
  - Laboratory searches for QI-type thrust in asymmetric cavities and laser resonators have so far reported null results: [Neunzig et al. 2022, laser resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md) and [Neunzig et al. 2022, EmDrive](../../03-criticism/2022-neunzig-emdrive-thrust/README.md).

## Related
- Evidence: [propulsion](../../02-evidence/propulsion.md), [emdrive](../../02-evidence/emdrive.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md), [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md), [2017-taylor-laser-resonators](../2017-taylor-laser-resonators/README.md), [2022-mcculloch-qi-thrust-casimir](../2022-mcculloch-qi-thrust-casimir/README.md), [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md)
