---
title: "Inertia from an asymmetric Casimir effect"
authors: [Michael E. McCulloch]
year: 2013
type: paper
venue: "EPL (Europhysics Letters) 101(5), 59001"
doi: 10.1209/0295-5075/101/59001
arxiv: "1302.2775"
url: "https://doi.org/10.1209/0295-5075/101/59001"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-rindler-hubble-horizons.png]
status: supports
tags: [derivation, propulsion]
---

# Inertia from an asymmetric Casimir effect

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1302.2775](https://arxiv.org/abs/1302.2775) · [doi:10.1209/0295-5075/101/59001](https://doi.org/10.1209/0295-5075/101/59001).

**Citation:** McCulloch, M. E. (2013). *Inertia from an asymmetric Casimir effect*. EPL (Europhysics Letters) 101(5), 59001. [doi:10.1209/0295-5075/101/59001](https://doi.org/10.1209/0295-5075/101/59001) / [arXiv:1302.2775](https://arxiv.org/abs/1302.2775)

**TL;DR:** This is the first proposed mechanism for why Unruh radiation should produce inertia in MiHsC. An accelerating object has a Rindler horizon at c²/a behind it, which suppresses Unruh radiation from that side through a "Rindler-scale Casimir effect". Radiation from the front is only slightly reduced by the distant Hubble horizon. The resulting imbalance in radiation pressure always opposes the acceleration, as inertia does. Integrating over angles gives F ∝ −a. With a Planck-length scale inserted, the inertial mass per particle comes out at ~5.5 × 10⁻⁸ kg, about twice the Planck mass. The paper suggests that artificial horizons, for example made with metamaterials, might produce motion.

> Text and page numbers are from arXiv v1 (Feb 2013), stored as `paper.pdf`.

## Key claims
- Previous MiHsC papers assumed inertia is "(somehow)" tied to Unruh radiation without a mechanism. This paper proposes one: an asymmetric Casimir effect between the Rindler horizon (behind) and the Hubble horizon (ahead).
- The net force has two terms. The term containing the Hubble scale is the MiHsC correction, and it matters only at low acceleration. The leading term is a force proportional to −a, i.e. inertia.
- The paper says this is simpler than the zero-point-field Lorentz-force model of Haisch, Rueda & Puthoff (1994), and needs no high-frequency cut-off. It notes that Levin (2009) criticised the Haisch et al. model.
- The model depends on Unruh radiation existing, which "has not been directly observed". The paper says the agreement of MiHsC with anomalies gives "some indirect evidence" for it.
- If Unruh radiation could be damped on one side of an object, or an artificial event horizon created there (perhaps with metamaterials), "the object could then be accelerated in a new way". This later becomes the QI propulsion idea.
- The derivation is valid only for single particles at speeds much less than c.

## Key equations
MiHsC inertia:
$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{|a|\Theta}\right) \sim m_g\left(1 - \frac{2c^2}{|a|\Theta}\right) $$
Radiation pressure on a small area, and the net force along angle θ:
$$ F = \frac{uA}{3}, \qquad dF_x = \frac{uA\cos\theta}{3}\left(1 - \frac{\lambda a\cos\theta}{4c^2} - 1 + \frac{\lambda}{4\Theta}\right) $$
After integrating over angles:
$$ dF_x = \frac{2\pi u\lambda A}{3}\left(\frac{1}{4\Theta} - \frac{\pi a}{16c^2}\right) \;\approx\; -\frac{\pi^2 u\lambda A a}{24c^2} $$
With u = hc/λV, and A/V = 1/l_P:
$$ dF_x = -\frac{\pi^2 h A a}{24 c V} = -\frac{\pi^2 h a}{24 c\, l_P}, \qquad m_i \sim \frac{\pi^2 h}{24 c\, l_P} \sim 5.5\times10^{-8}\ \text{kg} $$

## Data used
- None. This is a conceptual and theoretical derivation. It uses Θ = 2.7 × 10²⁶ m (Freedman et al. 2001) and l_P = 1.616 × 10⁻³⁵ m.

## Results & predictions
- The derived inertial mass per "particle" is ~5.5 × 10⁻⁸ kg, about 2.5× the Planck mass of 2.176 × 10⁻⁸ kg (the paper says "about twice"). The paper says that for compound objects this should be multiplied by the number of particles.
- Qualitative prediction: an asymmetric horizon or Unruh-damping arrangement next to an object should accelerate it, the basis of later QI propulsion proposals.

## Figures
*Figure (local only): Fig. 1 — A particle O accelerating to the right, with the cosmic horizon at Θ/2 to the right and a Rindler horizon at c²/a to the left; the resulting asymmetric Casimir effect pushes O back against its acceleration (p. 7).*

## Notable quotes
> "This produces an imbalance in the radiation pressure on the object, and a net force that always opposes acceleration, like inertia." (p. 1)

> "This explanation for inertia depends upon the existence of Unruh radiation, which has not been directly observed." (p. 5)

> "…if some way could be found to damp the Unruh waves on one side of an object, or create an artificial event horizon on that side (perhaps using metamaterials), the object could then be accelerated in a new way." (p. 6)

## Criticisms & responses
- **Choice of length scale.** The inertial mass in Eq. 11 depends on the arbitrary choice A/V = 1/x with x = l_P. That gives a single mass near the Planck mass rather than the masses of actual particles. The paper does not explain how electrons or protons would get their observed masses.
- **Foundational critiques.** Renda (2019, *MNRAS* 489, 881) is a critical analysis of QI's theoretical basis, including its use of Unruh radiation and horizons; see [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).
  - > [!UNVERIFIED] Whether Renda addresses this specific 2013 derivation in detail has not been checked here.
- **Unruh radiation itself.** The model depends on Unruh radiation being physically real and able to exert momentum on the accelerating object. This is debated. For an experimental proposal relevant to the Unruh effect, see [2023-lynch-accelerated-electron-thermometer](../2023-lynch-accelerated-electron-thermometer/README.md).
- **Propulsion claims built on this idea.** Laboratory tests of horizon-based thrust claims include [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md), [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md) and [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md).

## Related
- Evidence: [derivation](../../02-evidence/derivation.md), [propulsion](../../02-evidence/propulsion.md), [emdrive](../../02-evidence/emdrive.md)
- Sources:
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
  - [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md)
  - [2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md)
  - [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md)
  - [2019-mcculloch-rindler-horizons](../2019-mcculloch-rindler-horizons/README.md)
  - [2022-mcculloch-qi-thrust-casimir](../2022-mcculloch-qi-thrust-casimir/README.md)
  - [2023-dickmann-casimir-contradicts](../../03-criticism/2023-dickmann-casimir-contradicts/README.md)
