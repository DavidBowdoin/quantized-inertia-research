---
title: "Conservation of momentum and propellantless thrust"
tags: [context, momentum-conservation, noether, propulsion, emdrive, controversy]
related: [machs-principle.md, equivalence-principle.md, unruh-effect.md, casimir-effect.md]
---

# Conservation of momentum (and why propellantless thrust is controversial)

## Plain-language explanation

A rocket moves forward by throwing mass backward; the total momentum of rocket plus exhaust stays constant. A **closed box that accelerates itself without expelling anything** (and without pushing on anything external: no photons out, no solar wind, no magnetic field) would change the total momentum of an isolated system. That would contradict one of the most deeply grounded laws in physics.

Momentum conservation is not just an empirical rule: by **Noether's theorem** (1918) it follows from the **translation symmetry** of the laws of physics (physics is the same here as over there). Violating it means either that space is not homogeneous or that the system is not actually closed. In GR, momentum conservation holds locally ($\nabla_\mu T^{\mu\nu} = 0$).

A related point: a device producing constant thrust $F$ for input power $P$ with $F/P > 1/c$ (the photon-rocket limit, $3.3\ \mathrm{nN/W} = 3.3\ \mu\mathrm{N/kW}$) would, at sufficiently high speed, gain kinetic energy faster than it consumes power, i.e. it would be a perpetual-motion machine unless its thrust depends on velocity relative to some preferred frame or external field.

## Key equations

$$
\frac{d}{dt}\sum_i \mathbf p_i = \sum \mathbf F_{\text{ext}} = 0 \quad\text{(isolated system)}
$$

Noether: invariance under $\mathbf x \to \mathbf x + \boldsymbol\epsilon$ $\Rightarrow$ conserved $\mathbf P = \sum_i \partial L/\partial \dot{\mathbf x}_i$.

Photon rocket bound and the energy argument:

$$
\left(\frac{F}{P}\right)_{\text{photon}} = \frac{1}{c}\approx 3.3\ \mu\mathrm{N\,W^{-1}}, \qquad
\frac{dE_{\text{kin}}}{dt} = F v > P \ \text{ when } v > \frac{P}{F}
$$

## Mainstream status

Momentum conservation is regarded as exact within known physics. Claims of reactionless drives (Dean drive, EmDrive, Mach-effect thrusters, Cannae, QI drives) have repeatedly been traced to experimental artefacts when tested carefully: thermal drift, magnetic interaction of cables with the Earth's field, vibration, electrostatic forces, and outgassing. Tajmar's group at TU Dresden, using improved balances and battery-powered set-ups, reported that earlier EmDrive "thrust" was an artefact of power feeding and found no anomalous thrust at levels well below the original claims ([Kößling et al. 2019](../04-experiments/2019-kossling-spacedrive-balance/README.md), [Tajmar et al. 2021](../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [Neunzig et al. 2022](../03-criticism/2022-neunzig-emdrive-thrust/README.md)). NASA Eagleworks' 1.2 mN/kW result ([White et al. 2016](../04-experiments/2016-white-eagleworks/README.md)) was not replicated. Null EmDrive results also include [Samsonov 2016](../03-criticism/2016-samsonov-emdrive-null/README.md).

## How it relates to QI

QI claims to **preserve** momentum conservation by including the horizon / Unruh-radiation field: an asymmetric cavity is said to create an asymmetric horizon-damped Unruh field so that thrust is a reaction against the cosmic horizon (or against "information" at the horizon), analogous to a Casimir force ([McCulloch 2015 emdrive](../01-papers/2015-mcculloch-emdrive-epl/README.md), [2018 propulsion](../01-papers/2018-mcculloch-propellantless-propulsion/README.md), [2020 nano-materials](../01-papers/2020-mcculloch-nano-materials/README.md)). Mainstream objections:

1. **Where does the momentum go?** If the horizon "absorbs" momentum, it must be shown how and at what rate; a distant cosmic horizon cannot respond causally within the time of a lab experiment. Critics regard "momentum goes to the horizon" as an unfalsifiable bookkeeping device unless quantified.
2. **Energy.** QI-claimed thrust-to-power ratios (e.g. IVO's claimed ~45–52 mN/W, [Satnews 2022](../07-media/2022-satnews-ivo/README.md)) exceed the photon-rocket bound by a factor of ~$10^7$, which would imply over-unity energy at modest speeds unless a preferred frame exists.
3. **Experiments.** The DARPA-funded TU Dresden tests of QI-motivated laser resonators and fibre loops found no thrust at the nN level ([Neunzig, Weikert & Tajmar 2022](../03-criticism/2022-neunzig-laser-resonators/README.md)); capacitor-thrust claims ([Bhatt & Becker 2018](../04-experiments/2018-bhatt-capacitor-thrust/README.md), [McCulloch 2021](../01-papers/2021-mcculloch-symmetric-capacitors/README.md)) are constrained by [Tajmar & Schreiber 2020](../03-criticism/2020-tajmar-capacitor-thrust/README.md). In-orbit IVO tests have so far not produced a conclusive result (see [ivo-ltd.md](../06-people-orgs/ivo-ltd.md)).

QI papers do not treat propellantless thrust as violating momentum conservation; the burden is that this claim be backed by a quantitative account of momentum transfer and reproducible, artefact-controlled thrust.

## References

- Noether, E. (1918). Invariante Variationsprobleme. *Nachr. Ges. Wiss. Göttingen*, 235–257. English translation: arXiv:physics/0503066. https://arxiv.org/abs/physics/0503066
- Millis, M. G., Davis, E. W. (eds.) (2009). *Frontiers of Propulsion Science*. AIAA Progress in Astronautics and Aeronautics vol. 227. https://doi.org/10.2514/4.479953
- Tajmar, M., Neunzig, O., Weikert, M. (2022). High-accuracy thrust measurements of the EMDrive and elimination of false-positive effects. *CEAS Space J.* 14, 31. https://doi.org/10.1007/s12567-021-00385-1
- Wikipedia: Noether's theorem. https://en.wikipedia.org/wiki/Noether%27s_theorem ; Reactionless drive. https://en.wikipedia.org/wiki/Reactionless_drive
