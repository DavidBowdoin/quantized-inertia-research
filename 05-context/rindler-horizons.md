---
title: "Rindler horizons"
tags: [context, special-relativity, horizons, accelerated-frames, qi-foundation]
related: [unruh-effect.md, hawking-radiation.md, holographic-principle.md, equivalence-principle.md]
---

# Rindler horizons

## Plain-language explanation

If you accelerate uniformly forever, there is a region of spacetime behind you from which light can **never catch up** with you. The boundary of that region is the **Rindler horizon**. It sits a distance $c^2/a$ behind the accelerating observer (in their instantaneous rest frame). The horizon is observer-dependent: an inertial observer sees nothing special there. Rindler coordinates (Rindler 1966) are the natural coordinates for a uniformly accelerated observer in flat spacetime and provide the cleanest setting for the [Unruh effect](unruh-effect.md). Near any black-hole horizon, spacetime locally looks like Rindler spacetime, which is why the Rindler case is used as a model for [Hawking radiation](hawking-radiation.md).

For $a = 9.8\ \mathrm{m\,s^{-2}}$ the horizon is about $9\times10^{15}$ m (~1 light-year) away. For $a \sim 10^{-10}\ \mathrm{m\,s^{-2}}$ it is comparable to the size of the observable universe.

## Key equations

Rindler metric (acceleration along $x$):

$$
ds^2 = -\left(\frac{a\,\xi}{c}\right)^2 c^2\,d\eta^2 + d\xi^2 + dy^2 + dz^2
$$

Distance to the horizon for proper acceleration $a$:

$$
d_H = \frac{c^2}{a}
$$

Hyperbolic worldline of the accelerated observer in inertial coordinates:

$$
x^2 - c^2t^2 = \left(\frac{c^2}{a}\right)^2
$$

## Mainstream status

Rindler horizons are textbook special relativity; there is nothing controversial about their kinematics. What is debated is how much *physical* significance (entropy, information, thermodynamics) observer-dependent horizons carry. Jacobson's 1995 thermodynamic derivation of Einstein's equations and Verlinde's entropic gravity (see [holographic-principle.md](holographic-principle.md)) treat local Rindler horizons as carrying entropy; this is an active research programme, not established physics.

## How it relates to QI

Rindler horizons are QI's central device. In the [2013 mechanism paper](../01-papers/2013-mcculloch-asymmetric-casimir/README.md) the horizon behind an accelerating body acts like one plate of a Casimir cavity, damping Unruh radiation on that side. The cosmic horizon (taken as Hubble-scale, diameter $\Theta$) sets the other limit. When $c^2/a$ becomes comparable to $\Theta$, the two horizons interact and QI's modification of inertia switches on, giving QI's "minimum acceleration"

$$
a_{\min} \sim \frac{2c^2}{\Theta}
$$

([2010 minimum-accelerations paper](../01-papers/2010-mcculloch-minimum-accelerations/README.md)). Later QI work (e.g. [McCulloch & Giné 2017](../01-papers/2017-mcculloch-information-loss/README.md), [2020 horizon widths](../01-papers/2020-mcculloch-horizon-widths/README.md)) rephrases this in terms of horizon information or uncertainty-principle arguments. McCulloch has proposed engineering "artificial horizons" (e.g. in asymmetric cavities, [2018 propulsion paper](../01-papers/2018-mcculloch-propellantless-propulsion/README.md)) and a lab test using a rapidly accelerated disc ([2019 Rindler horizons](../01-papers/2019-mcculloch-rindler-horizons/README.md)).

Critics point out that a Rindler horizon only exists for *eternal* uniform acceleration; real bodies with variable, finite acceleration do not have a sharp horizon, and an observer-dependent horizon is not a physical surface that can reflect radiation like a Casimir plate. QI's treatment of horizons as physical boundaries is therefore a hypothesis, not a consequence of standard relativity.

## References

- Rindler, W. (1966). Kruskal space and the uniformly accelerated frame. *Am. J. Phys.* 34, 1174. https://doi.org/10.1119/1.1972547
- Crispino, Higuchi & Matsas (2008). *Rev. Mod. Phys.* 80, 787. https://doi.org/10.1103/RevModPhys.80.787
- Jacobson, T. (1995). Thermodynamics of spacetime: the Einstein equation of state. arXiv:gr-qc/9504004. https://arxiv.org/abs/gr-qc/9504004
- Wikipedia: Rindler coordinates. https://en.wikipedia.org/wiki/Rindler_coordinates
