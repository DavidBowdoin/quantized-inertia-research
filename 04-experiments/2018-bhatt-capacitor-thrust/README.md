---
title: "Electrostatic accelerated electrons within symmetric capacitors during field emission condition events exert bidirectional propellant-less thrust"
authors: [Ankur S. Bhatt, F. M. Becker]
year: 2018
type: experiment-report
venue: "arXiv preprint (physics.app-ph), v3 June 2019"
doi: 10.48550/arXiv.1810.04368
arxiv: 1810.04368
url: "https://arxiv.org/abs/1810.04368"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, figures/fig-9-force-vs-current.png, figures/fig-18-blockers.png, figures/fig-21-wireless.png]
status: supports
tags: [capacitor, propulsion, qi-collaborators, unruh, rindler-horizon, not-peer-reviewed, lab-test]
---

# Electrostatic accelerated electrons within symmetric capacitors during field emission condition events exert bidirectional propellant-less thrust

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1810.04368](https://arxiv.org/abs/1810.04368) · [doi:10.48550/arXiv.1810.04368](https://doi.org/10.48550/arXiv.1810.04368).

**Citation:** Bhatt, A. S. & Becker, F. M. (2018). *Electrostatic accelerated electrons within symmetric capacitors during field emission condition events exert bidirectional propellant-less thrust*. arXiv:[1810.04368](https://arxiv.org/abs/1810.04368) (v1 10 Oct 2018; v3 17 Jun 2019, "added data, corrected typos").

The stored PDF is **v3** (24 pages). The arXiv metadata lists Bhatt first, while the PDF title block lists "Becker, F. M., Bhatt, Ankur S.". Other sources cite it both as "Bhatt & Becker" and as "Becker & Bhatt". The preprint was not peer-reviewed or published in a journal as far as was found.

**TL;DR:** Thin parallel-plate capacitors with polyethylene dielectrics of 13–80 µm were charged at about 5 kV, with roughened cathodes to promote field emission. Over 507 data points the authors report a small force towards the anode, measured on a digital scale (LEADZM B300T, 0.001 mg resolution). The force is linear in discharge current, rises exponentially as the electrode gap shrinks, and reverses when a conductor insulated from the cathode is placed behind it within a range "R". The authors speculate that R corresponds to the Rindler horizon c²/a of the accelerated electrons, linking the effect to Unruh radiation. They thank McCulloch "for encouraging us and providing us directions". They report "performance above 0.4 N/kW" and call for replication with better equipment.

## Key claims
- The effect appears only during field emission or partial breakdown, when electrons are accelerated to about 10¹⁸–10¹⁹ m s⁻². Arcing, which brings in positive ions, suppresses it. Paper, glycerin and porous dielectrics did not work.
- **Observed trends:**
  - Force is linear in current ("accelerated mass").
  - At a normalised 10 µA, force grows exponentially as electrode distance decreases (Figs. 7–8).
  - Stacking capacitors roughly doubles the force.
  - Force falls slightly as voltage increases from 1 to 10 kV (97 points).
- **Directional reversal with "blockers"** (144 points), where conductive aluminium sheets a few tenths of a mm thick are placed near the cathode (Figs. 17–20):
  - A conductor insulated from the cathode and placed behind it within range R gives full force reversal.
  - Beyond R, the original force returns.
  - Thickening the cathode reduces the force; thickening it beyond R gives full reversal.
  - Conductors placed in front of the anode have no effect.
- **Speculative interpretation:** "This range might correspond to the rindler horizon equation (which is equal to c²/a) [5]" (p. 16). In the Discussion, the electron is described as sitting in a Casimir-like region between the electrodes plus Rindler-horizon radiation, producing an "energy/momentum gradient".
- **Controls reported:**
  - Vertical-orientation null test, "as advised by Prof. Dr. M. Tajmar", gave null force.
  - Twisted supply wires.
  - Soft vacuum (about 20 Torr), which reduced scatter from 12% to 8%.
  - A January 2019 battery-powered wireless set-up inside a grounded Faraday cage reproduced the trend line for the 20 µm capacitor.
  - An Earth's-field Lorentz-force estimate gave at most about 1 mg.
  - Flipping the capacitor without rewiring reversed the force.
- **Acknowledged weaknesses:** buoyancy from pre-heating to about 50 °C, which correlates with the greater thrust for thicker insulators when the anode faces up. The appendix covers Trichel/corona pulses and leakage currents. The authors state that the experiment should be repeated "with a more sophisticated testing facility".

## Key equations
Skin depth used to choose blocker thickness (Eq. 1):
$$ \delta = \sqrt{\frac{2\rho}{2\pi f \mu_r \mu_0}} $$
The proposed range is identified with the Rindler distance. This identification is speculative in the source.
$$ R \sim \frac{c^2}{a} $$

## Data used
- 507 force readings in total: 266 versus electrode distance, 97 versus voltage, and 144 with blockers, plus wireless runs. Currents were measured via a shunt and Keysight DSO1052B oscilloscope. A flyback transformer supplied voltages up to about 10 kV.

## Results & predictions
- The vacuum median for the 33 µm capacitor is about 1.1 × 10⁻³ N with σ ≈ 8.7 × 10⁻⁵ N, against about 1.0 × 10⁻³ N with σ ≈ 1.2 × 10⁻⁴ N in air (p. 9).
- About 10 mg force was "commonplace" for the 20 µm capacitor in the wireless set-up (p. 21).
- Performance "above 0.4 [N/kW]", extrapolated to a 1 kW stacked device (Fig. 11, p. 11; text pp. 21–22).
- No quantitative theoretical prediction is given. The authors say "an existing theoretical framework … seems to predict the observed forces", meaning McCulloch's then-unpublished QI capacitor model.

## Figures
*Figure (local only): Fig. 9 — Force versus current (accelerated electron mass) for several dielectric thicknesses, anode up/down, including low-vacuum points. (Rendered p. 10.)*

*Figure (local only): Figs. 17 & 18 — "Rindler radiation attenuation": force versus current for various conductive blockers (cathode-connected or insulated, different coverage), and averaged force by blocker type showing reversal for insulated blockers within range R. (Rendered p. 17.)*

*Figure (local only): Fig. 21 — Wireless, battery-powered set-up results (Jan 2019) compared with the earlier wired 20 µm data. (Rendered p. 19.)*

## Notable quotes
> "Overall the illustrated results of the four different sub-experiments, with an adequately high sample size (507 data points collected) with evident trend lines, suggest that a new phenomenon, and not an artifact, has been observed." (p. 20)

> "Speculatively, This range might correspond to the rindler horizon equation (which is equal to c2/a) [5] since the electron experiences high acceleration" (p. 16)

## Criticisms & responses
- **Independent null test:** [Tajmar & Schreiber (2020, J. Electrostatics)](../../03-criticism/2020-tajmar-capacitor-thrust/README.md) built a clean set-up: on-board high-voltage supply in a mu-metal box, liquid-metal low-voltage feeds and a rotation rig, with ±0.3 mg accuracy. They fitted an empirical law to this paper's data, which predicted 6.8 mg. They measured less than 0.3 mg, ruling out the claim "by an order of magnitude". They caveat that their discharge voltage (2.1 kV), dielectric thickness (90 µm) and surroundings differed, so the result "may not completely rule out the claim". They also note the original set-up was "poorly described and hard to replicate".
- **Measurement concerns (factual, from the source):** the readings come from a consumer-grade digital scale near high-voltage wiring. The authors themselves observed display corruption within about 50 mm of the scale. Pre-heating creates buoyancy, which they acknowledge. In 2021 McCulloch also wrote that "they had used a high voltage with a digital balance so there was a potential for glitches" ([blog, 2 Nov 2021](https://physicsfromtheedge.blogspot.com/2021/11/a-thrust-from-nothing.html)).
- **McCulloch's position:** he treats this as QI's strongest laboratory result.
  - 2 Nov 2021: Becker "read my papers, remembered a capacitor-based Biefeld-Brown-type experiment he had done, and with a few discussion with me, he and Ankur Bhatt tried it and produced milliNewtons of thrust". "Even DARPA emailed me". Richard Mansell of IVO Ltd "tried it with an analogue method and agreed with them" ([blog](https://physicsfromtheedge.blogspot.com/2021/11/a-thrust-from-nothing.html)).
  - 23 Jan 2022: "QI predicts the capacitor results perfectly … results now seen in two labs" ([blog](https://physicsfromtheedge.blogspot.com/2022/01/learning-from-experiments.html)).
  - His model is in [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md).
  > [!UNVERIFIED] The IVO/Mansell replication; no peer-reviewed report of it was located for this entry.
- **Space test:** IVO Ltd flew a QI-capacitor thruster. Contact problems and the outcome are covered in [2024-debrief-ivo-failure](../../07-media/2024-debrief-ivo-failure/README.md) and [2024-futurism-ivo-contact-lost](../../07-media/2024-futurism-ivo-contact-lost/README.md).

## Related
- Evidence: [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md), [2018-mcculloch-propellantless-propulsion](../../01-papers/2018-mcculloch-propellantless-propulsion/README.md), [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md), [2022-mcculloch-qi-thrust-casimir](../../01-papers/2022-mcculloch-qi-thrust-casimir/README.md)
- Media: [2023-debrief-ivo-launch](../../07-media/2023-debrief-ivo-launch/README.md), [2023-inverse-ivo](../../07-media/2023-inverse-ivo/README.md), [2023-universetoday-ivo](../../07-media/2023-universetoday-ivo/README.md), [2022-satnews-ivo](../../07-media/2022-satnews-ivo/README.md), [2026-nextbigfuture-ivo-review](../../07-media/2026-nextbigfuture-ivo-review/README.md)
