---
title: Can the Emdrive Be Explained by Quantised Inertia?
authors: [Michael Edward McCulloch]
year: 2015
type: paper
venue: "Progress in Physics 11(1), 78-80"
doi:
arxiv:
url: "https://progress-in-physics.com/2015/PP-40-15.PDF"
open_access: true
license: CC-BY-NC-ND-2.5
files: [paper.pdf]
status: supports
tags: [emdrive, propulsion]
---

# Can the Emdrive Be Explained by Quantised Inertia?

**Citation:** McCulloch, M. E. (2015). *Can the Emdrive Be Explained by Quantised Inertia?* Progress in Physics 11(1), 78–80 (January 2015 issue; submitted 18 Dec 2014, accepted 19 Dec 2014). https://progress-in-physics.com/2015/PP-40-15.PDF. Progress in Physics does not assign DOIs, and old ptep-online.com links now point to an unrelated site.

**TL;DR:** This is McCulloch's first QI model of the emdrive. Photons in a tapered cavity are assumed to have an inertial mass caused by Unruh radiation, and only Unruh waves that fit the cavity width are allowed. Photons therefore have more inertia at the wide end, and conserving momentum pushes the cavity towards the narrow end. A simple 1-D formula, F = −(PQl/c)(1/W_big − 1/W_small), is compared with 5 published thrust measurements. It gets the order of magnitude right in 4 cases and overpredicts the fifth by 10×.

## Key claims
- Emdrives (Shawyer 2008; Juan et al. 2012; NASA, Brady et al. 2014) show an anomalous thrust towards the narrow end. The paper says this has no accepted explanation and violates conservation of momentum.
- In MiHsC, inertia comes from Unruh radiation subject to a horizon-scale Casimir-like cutoff. In the emdrive, the photons' acceleration is so high that their Unruh waves are about the size of the cavity, so the cavity walls play the role of the horizon.
- Assuming the waves only need to fit laterally (the cavity width), photon inertial mass is greater at the wide end, and a force towards the narrow end appears.
- Thrust should rise with power, Q factor, cavity length and taper, and with a dielectric (which lowers c). The paper adds in parentheses that "such an effect has recently been seen".
- The paper says the model makes "a number of controversial assumptions", notably that photons have a finite inertial mass that varies with MiHsC.

## Key equations
MiHsC (Eq. 1):
$$m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) = m\left(1 - \frac{\lambda}{4\Theta}\right)$$

Force from momentum conservation (Eqs. 3–5):
$$F = -c\frac{\partial m}{\partial t} = -c^2\frac{\partial m}{\partial x}, \qquad F = -c^2\left(\frac{m_{bigend} - m_{smallend}}{l}\right)$$

Unruh wavelength in the cavity, λ = 8c²/a = 4l, giving (Eq. 7):
$$F = -4c^2 m\left(\frac{1}{4W_{big}} - \frac{1}{4W_{small}}\right)$$

Final thrust formula (Eq. 10):
$$F = \frac{-PQl}{c}\left(\frac{1}{W_{big}} - \frac{1}{W_{small}}\right)$$

## Data used
- Shawyer (2008): two cavities, the experimental thruster (section 6 of that paper) and the demonstrator engine (section 7).
- NASA Eagleworks, Brady et al. (2014): three tests, not in vacuum at the time.
- Juan et al. (2012): excluded because Q and geometry were not specified.
- Some dimensions were estimated from photographs by forum members (see Acknowledgements).

## Results & predictions
Table 1 (thrust in mN):

| Expt | P (W) | Q/1000 | l (m) | W_big/W_small (m) | F predicted | F observed |
|---|---|---|---|---|---|---|
| S1 | 850 | 5.9 | 0.156 | 0.16/0.1275 | 4.2 | 16 |
| S2 | 1000 | 45 | 0.345 | 0.28/0.1289 | 216 | 80–214 |
| B1 | 16.9 | 7.32 | 0.332 | 0.397/0.244 | 0.22 | 0.091 |
| B2 | 16.7 | 18.1 | 0.332 | 0.397/0.244 | 0.53 | 0.05 |
| B3 | 2.6 | 22 | 0.332 | 0.397/0.244 | 0.1 | 0.055 |

- S1: the predicted 4.2 mN is "about a third" of the observed 16 mN.
- S2: the predicted 216 mN "agrees with" the observed 80–214 mN/kW.
- The author says the model "predicts the correct order of magnitude for cases S1, S2, B1 and B3". In B2 it overpredicts by a factor of ten. He notes B2 is odd in other ways: Q more than doubled from B1 while thrust almost halved.
- The B-cavity geometry here differs from that used in the later EPL paper (0.2286 m length, 0.2794/0.1588 m ends).
- Inconsistency in the source: the worked S2 calculation (Eq. 12) uses l = 0.325 m, but Table 1 lists 0.345 m.

## Figures
No figures in the paper (Table 1 only).

## Notable quotes
> "This model predicts the available observations quite well, although the observational uncertainties are not well known." (p. 78, Abstract)

> "This proposal makes a number of controversial assumptions. For example that the inertial mass of photons is finite and varies in line with MiHsC." (p. 80)

## Criticisms & responses
- **The thrust.** Later precision measurements by the Dresden SpaceDrive group attributed emdrive thrust signals to artefacts, mainly thermal and cable/magnetic effects. See [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md) and [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md). If there is no thrust, the comparison here tests nothing.
- **Venue.** Progress in Physics is a low-impact journal outside the mainstream. This paper was accepted one day after submission (dates printed on p. 80).
- **The model.** The author refined it himself in EPL 111, 60005 (crude 3-D averaging, removing the 1-D model's divergence for pointed cones), and again in EPL 118, 34003 (dielectrics; the photon acceleration dropped as unnecessary).
- General QI critique: [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources:
  - [2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md)
  - [2017-mcculloch-emdrives-dielectrics](../2017-mcculloch-emdrives-dielectrics/README.md)
  - [2008-mcculloch-flyby-anomalies-jbis](../2008-mcculloch-flyby-anomalies-jbis/README.md) (cited for the idea of reducing the horizon distance)
  - [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md)
  - [2016-samsonov-emdrive-null](../../03-criticism/2016-samsonov-emdrive-null/README.md)
