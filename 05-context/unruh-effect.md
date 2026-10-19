---
title: "Unruh effect"
tags: [context, quantum-field-theory, unruh-radiation, horizons, qi-foundation]
related: [rindler-horizons.md, hawking-radiation.md, casimir-effect.md, sed-inertia.md, equivalence-principle.md]
---

# Unruh effect

## Plain-language explanation

In quantum field theory the "vacuum" is not uniquely defined for every observer. An observer moving at constant velocity sees the Minkowski vacuum as empty. An observer undergoing **constant proper acceleration** $a$ instead finds that the same quantum state looks like a **thermal bath of particles** at a temperature proportional to $a$. This prediction, made by Fulling (1973), Davies (1975) and Unruh (1976), is the Unruh (or Fulling–Davies–Unruh) effect. It is closely related to Hawking radiation: in both cases a horizon (here the [Rindler horizon](rindler-horizons.md)) hides part of spacetime from the observer, and tracing over the hidden modes leaves a thermal state.

The temperature is tiny for everyday accelerations: about $4\times10^{-20}$ K for $a = 9.8\ \mathrm{m\,s^{-2}}$. Reaching 1 K requires roughly $2.5\times10^{20}\ \mathrm{m\,s^{-2}}$.

## Key equations

Unruh temperature:

$$
T_U = \frac{\hbar a}{2\pi c\, k_B} \approx 4.05\times10^{-21}\ \mathrm{K}\ \times \frac{a}{1\ \mathrm{m\,s^{-2}}}
$$

Peak (Wien) wavelength of the thermal spectrum seen by the accelerated observer, scaling as $\lambda \sim c^2/a$:

$$
\lambda_{\text{peak}} = \frac{4\pi^2 c^2}{\beta\, a} \approx \frac{8c^2}{a}, \qquad \beta \approx 4.965
$$

(The second form follows from inserting $T_U$ into Wien's law $\lambda_{\text{peak}} = hc/(\beta k_B T)$; the scaling $\lambda \sim c^2/a$ is what lets QI argue that Unruh wavelengths approach the cosmic scale $\Theta$ when $a$ is very small.)

## Mainstream status

- **Theory:** The effect is regarded as a robust consequence of quantum field theory in flat spacetime. The standard review is Crispino, Higuchi & Matsas (2008). There are long-running debates about interpretation (e.g. whether an accelerated *detector* "radiates" in the inertial frame), but not about the existence of the thermal response of a uniformly accelerated detector in the idealised case.
- **Experiment:** There is **no direct, unambiguous detection** of Unruh radiation for a real accelerated body. Related evidence includes the proposal by Bell & Leinaas (1983) linking incomplete electron spin polarisation in storage rings to an Unruh-like effect, analogue "quantum simulations" in Bose–Einstein condensates (Hu et al. 2019), and the reinterpretation of radiation from ultra-accelerated channelled electrons as Unruh-like (Lynch, Ievlev & Good 2023, see [source folder](../01-papers/2023-lynch-accelerated-electron-thermometer/README.md)). These are suggestive, not decisive.
- **Isotropy:** For an ideal eternal uniform acceleration with an ideal pointlike detector, the bath is thermal and (in the detector's frame) isotropic in the sense relevant to most textbook treatments. Kholupenko's series of papers argues that with finite integration times, defined start times, or screened/directional detectors the response can be **anisotropic and non-thermal** ([part 1](../01-papers/2019-kholupenko-unruh-anisotropy-1/README.md), [part 2](../01-papers/2022-kholupenko-unruh-anisotropy-2/README.md), [part 3](../01-papers/2025-kholupenko-unruh-anisotropy-3/README.md)).

## How it relates to QI

The Unruh effect is QI's first assumption. McCulloch's founding paper ([2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md)) hypothesises that inertia is a reaction to Unruh radiation. The [2013 asymmetric-Casimir paper](../01-papers/2013-mcculloch-asymmetric-casimir/README.md) proposes the mechanism: the Rindler horizon on one side of an accelerating body suppresses Unruh radiation on that side, creating a net radiation-pressure imbalance that opposes acceleration. At very low accelerations, Unruh wavelengths grow towards the cosmic scale $\Theta$, some are "disallowed" by a Hubble-scale [Casimir-like effect](casimir-effect.md), and inertial mass is reduced:

$$
m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right)
$$

Points of contention:

1. **Magnitude.** Unruh radiation energy densities at ordinary accelerations are absurdly small. Critics (e.g. Koberlein, see [media](../07-media/2017-koberlein-doing-it-wrong/README.md)) argue that isotropic or near-isotropic Unruh radiation cannot by itself supply forces of the size of ordinary inertia. McCulloch's derivations rely on heuristic arguments (uncertainty principle, horizon information) rather than a standard QFT calculation of radiation pressure.
2. **Derivation errors.** Renda (2019) argues the 2007/2013 derivation contains two major flaws and that a careful treatment with a discrete black-body Unruh spectrum yields a different $F(a)$ ([criticism folder](../03-criticism/2019-renda-sceptical/README.md)).
3. **Anisotropy.** QI needs the Unruh field seen by a body to be anisotropic; Kholupenko's results are sometimes cited as consistent with this, but they do not test QI.

## References

- Unruh, W. G. (1976). Notes on black-hole evaporation. *Phys. Rev. D* 14, 870. https://doi.org/10.1103/PhysRevD.14.870
- Fulling, S. A. (1973). Nonuniqueness of canonical field quantization in Riemannian space-time. *Phys. Rev. D* 7, 2850. https://doi.org/10.1103/PhysRevD.7.2850
- Davies, P. C. W. (1975). Scalar production in Schwarzschild and Rindler metrics. *J. Phys. A* 8, 609. https://doi.org/10.1088/0305-4470/8/4/022
- Crispino, L. C. B., Higuchi, A., Matsas, G. E. A. (2008). The Unruh effect and its applications. *Rev. Mod. Phys.* 80, 787. https://doi.org/10.1103/RevModPhys.80.787
- Bell, J. S., Leinaas, J. M. (1983). Electrons as accelerated thermometers. *Nucl. Phys. B* 212, 131. https://doi.org/10.1016/0550-3213(83)90601-6
- Hu, J. et al. (2019). Quantum simulation of Unruh radiation. *Nature Physics* 15, 785. https://doi.org/10.1038/s41567-019-0537-1
- Wikipedia: Unruh effect. https://en.wikipedia.org/wiki/Unruh_effect
