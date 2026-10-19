---
title: "Mach's principle (incl. Sciama 1953)"
tags: [context, inertia, general-relativity, history, qi-foundation]
related: [sed-inertia.md, equivalence-principle.md, holographic-principle.md, conservation-of-momentum.md]
---

# Mach's principle

## Plain-language explanation

Why does water climb the sides of a spinning bucket (Newton's bucket)? Newton's answer was rotation relative to **absolute space**. Ernst Mach (1883) argued instead that rotation and acceleration only make sense relative to the **distant matter of the universe**, so inertia itself should somehow be caused by that matter. Einstein coined the name "Mach's principle" (1918) and was motivated by it while building general relativity, but GR turned out to be only partially Machian: it has vacuum solutions with inertia but no matter, and the local inertial frame is set by the metric, not directly by distant masses.

There is no single agreed statement of Mach's principle; Barbour & Pfister's 1995 volume lists many inequivalent versions.

## Sciama (1953)

Dennis Sciama's paper "On the origin of inertia" built a toy, vector-potential (electromagnetism-like) model of gravity in which a body accelerating relative to the rest of the universe experiences an induced "gravitational electric field" from all distant matter. Requiring that this field exactly cancel the gravitational pull of the body's own acceleration gives a condition linking $G$ to the mass and size of the universe:

$$
\frac{G\,M_U}{R_U\,c^2} \sim 1 \quad\Longleftrightarrow\quad G \approx \frac{R_U c^2}{M_U}
$$

i.e. inertia arises from gravitational induction by the whole universe, and the condition is numerically roughly satisfied by the observed universe. Sciama acknowledged the model was not a full theory.

## Key equations (related formalisms)

Brans–Dicke scalar–tensor gravity (1961), explicitly motivated by Mach, makes $G$ dynamical via a scalar field $\phi \sim 1/G$ sourced by matter:

$$
\Box\phi = \frac{8\pi}{3 + 2\omega} T
$$

Solar-system tests (Cassini) require $\omega \gtrsim 4\times10^4$, i.e. very close to GR.

## Mainstream status

- Mach's principle is a respected **heuristic and philosophical** idea, not an established law. GR exhibits Machian effects such as **frame dragging** (Lense–Thirring), measured by Gravity Probe B (Everitt et al. 2011) and LAGEOS, but these do not show that inertia *as a whole* originates from distant matter.
- Scalar–tensor Machian theories are constrained to be very close to GR.

## How it relates to QI

QI is self-consciously Machian in spirit: the inertia of a body depends on a cosmic quantity (the horizon scale $\Theta$), so in QI "the universe" sets inertia. McCulloch describes inertia as arising from the interplay between local Rindler horizons and the cosmic horizon (see [rindler-horizons.md](rindler-horizons.md)). Unlike Sciama's gravitational-induction picture, QI's mechanism is quantum (Unruh radiation) rather than gravitational. QI is often compared with James Woodward's "Mach effect" propulsion concept, which also claims propellantless thrust from Machian arguments; Woodward himself is a critic of QI (quoted in the [2018 Motherboard/Vice article](../07-media/2018-motherboard-darpa-pseudoscience/README.md)), and Tajmar's group has tested Mach-effect thrusters alongside QI-motivated devices ([2018 SpaceDrive overview](../04-experiments/2018-tajmar-spacedrive/README.md), [2019 balance tests](../04-experiments/2019-kossling-spacedrive-balance/README.md)). Millis (2017) reviews inertial-frame physics in a propulsion context ([source](../01-papers/2017-millis-inertial-frames/README.md)).

## References

- Sciama, D. W. (1953). On the origin of inertia. *MNRAS* 113, 34. https://doi.org/10.1093/mnras/113.1.34
- Brans, C., Dicke, R. H. (1961). Mach's principle and a relativistic theory of gravitation. *Phys. Rev.* 124, 925. https://doi.org/10.1103/PhysRev.124.925
- Barbour, J. B., Pfister, H. (eds.) (1995). *Mach's Principle: From Newton's Bucket to Quantum Gravity*. Birkhäuser (Einstein Studies vol. 6).
- Everitt, C. W. F. et al. (2011). Gravity Probe B: final results. *Phys. Rev. Lett.* 106, 221101. https://doi.org/10.1103/PhysRevLett.106.221101
- Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Rev. Relativ.* 17, 4. https://doi.org/10.12942/lrr-2014-4
- Wikipedia: Mach's principle. https://en.wikipedia.org/wiki/Mach%27s_principle
