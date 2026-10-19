---
title: "Hawking radiation (and de Sitter horizon temperature)"
tags: [context, black-holes, horizons, quantum-field-theory, cosmology]
related: [unruh-effect.md, rindler-horizons.md, holographic-principle.md, cosmological-constant-dark-energy.md]
---

# Hawking radiation

## Plain-language explanation

Hawking (1974, 1975) showed that, once quantum fields are included, a black hole is not perfectly black: its event horizon emits thermal radiation with a temperature inversely proportional to its mass. Over enormous times this makes black holes slowly evaporate. The physics is closely related to the [Unruh effect](unruh-effect.md): near the horizon, a static observer must accelerate hard to avoid falling in, and sees a thermal bath. Gibbons & Hawking (1977) extended the result to **cosmological (de Sitter) horizons**: an observer in an exponentially expanding universe sees thermal radiation from their cosmic horizon at a temperature set by the Hubble rate.

For a solar-mass black hole the Hawking temperature is ~60 nK, far colder than the cosmic microwave background, so astrophysical black holes currently absorb more than they emit.

## Key equations

Hawking temperature of a Schwarzschild black hole of mass $M$ (surface gravity $\kappa = c^4/4GM$):

$$
T_H = \frac{\hbar \kappa}{2\pi c\,k_B} = \frac{\hbar c^3}{8\pi G M k_B} \approx 6.2\times10^{-8}\ \mathrm{K}\ \left(\frac{M_\odot}{M}\right)
$$

Bekenstein–Hawking entropy (horizon area $A$):

$$
S_{BH} = \frac{k_B c^3 A}{4 G \hbar}
$$

Gibbons–Hawking temperature of a de Sitter horizon with Hubble rate $H$:

$$
T_{dS} = \frac{\hbar H}{2\pi k_B}
$$

## Mainstream status

- **Theory:** Hawking radiation is accepted by most theorists as a robust semiclassical result; it underpins black-hole thermodynamics and the black-hole information problem.
- **Observation:** It has **not been observed** from any astrophysical black hole (the signal is far too weak). Analogue experiments, notably Steinhauer's group with sonic horizons in Bose–Einstein condensates (Muñoz de Nova et al. 2019), report thermal Hawking-like radiation in analogue systems; these test the kinematics of horizon radiation, not gravity itself.

## How it relates to QI

QI borrows the horizon–thermal-radiation idea twice: from local [Rindler horizons](rindler-horizons.md) (Unruh) and from the cosmic horizon. McCulloch's "toy cosmology" ([2014 Galaxies paper](../01-papers/2014-mcculloch-toy-cosmology/README.md)) models the Hubble volume as a black hole emitting Hawking-like radiation inwards. Giné rederives Hawking and Unruh temperatures heuristically from the uncertainty principle in QI style ([Giné 2018](../01-papers/2018-gine-hawking-unruh-uncertainty/README.md)).

Mainstream caveats: the Gibbons–Hawking temperature of our cosmic horizon is ~$10^{-30}$ K, and standard semiclassical gravity gives no mechanism by which this radiation, or the cosmic horizon as a "boundary", modifies the inertia of ordinary bodies. Heuristic uncertainty-principle derivations reproduce the *scaling* of these temperatures but are not substitutes for the QFT calculations.

## References

- Hawking, S. W. (1974). Black hole explosions? *Nature* 248, 30. https://doi.org/10.1038/248030a0
- Hawking, S. W. (1975). Particle creation by black holes. *Commun. Math. Phys.* 43, 199. https://doi.org/10.1007/BF02345020
- Bekenstein, J. D. (1973). Black holes and entropy. *Phys. Rev. D* 7, 2333. https://doi.org/10.1103/PhysRevD.7.2333
- Gibbons, G. W., Hawking, S. W. (1977). Cosmological event horizons, thermodynamics, and particle creation. *Phys. Rev. D* 15, 2738. https://doi.org/10.1103/PhysRevD.15.2738
- Muñoz de Nova, J. R. et al. (2019). Observation of thermal Hawking radiation and its temperature in an analogue black hole. *Nature* 569, 688. https://doi.org/10.1038/s41586-019-1241-0
- Wikipedia: Hawking radiation. https://en.wikipedia.org/wiki/Hawking_radiation
