---
title: "The SpaceDrive project – Developing revolutionary propulsion at TU Dresden"
authors: [Martin Tajmar, Matthias Kößling, Marcel Weikert, Maxime Monette]
year: 2018
type: paper
venue: "Acta Astronautica 153:1-5"
doi: 10.1016/j.actaastro.2018.10.028
arxiv:
url: "https://doi.org/10.1016/j.actaastro.2018.10.028"
open_access: false
license: accepted-manuscript
files: [paper.pdf, figures/fig-1-thrust-balance.png, figures/fig-2-emdrive-met-designs.png]
status: neutral
tags: [emdrive, mach-effect, program-overview, tu-dresden, thrust-balance]
---

# The SpaceDrive project – Developing revolutionary propulsion at TU Dresden

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`accepted-manuscript`) does not permit redistribution. Read the paper at [doi:10.1016/j.actaastro.2018.10.028](https://doi.org/10.1016/j.actaastro.2018.10.028).

**Citation:** Tajmar, M., Kößling, M., Weikert, M. & Monette, M. (2018). *The SpaceDrive project – Developing revolutionary propulsion at TU Dresden*. Acta Astronautica, 153, 1–5. https://doi.org/10.1016/j.actaastro.2018.10.028. Received 11 Nov 2017, revised 4 Jul 2018, accepted 17 Oct 2018.

**Stored version: the Elsevier ACCEPTED MANUSCRIPT, not the typeset journal article.** It is 10 PDF pages: an Elsevier cover sheet (PDF p. 1), the paper itself, which still carries the IAC-17 header (68th International Astronautical Congress, Adelaide, 25–29 Sep 2017, IAC-17,C4,7-C3.5,10,x38595; "Copyright ©2017 by the International Astronautical Federation (IAF). All rights reserved") and is paginated "Page 1 of 8" to "Page 8 of 8" (PDF pp. 2–9), and a highlights page (PDF p. 10). Supplied by the archive owner and kept local only. **Page numbers below are manuscript pages ("ms. p. N of 8")**, not journal pages 1–5. The text matches the IAC-17 conference version used earlier for this entry; no substantive differences were found.

**TL;DR:** A programme overview, not a results paper. Since 2012 TU Dresden has had a breakthrough-propulsion group to test, with high-confidence instrumentation, concepts that "claim to be at least an order of magnitude more efficient in producing thrust compared to photon rockets". SpaceDrive (launched May 2017, funded by DLR/BMWi 50RS1704) concentrates on the **EMDrive** and the **Mach-Effect Thruster**, plus side experiments. It describes an upgraded torsion balance under development: up to 25 kg payload, nN-range noise with sub-nN resolution, an attocube laser interferometer, and motors to reverse the thruster without breaking vacuum so that thermal centre-of-gravity shifts can be told apart from thrust. **QI is cited only once, in passing**, as one of the "alternative theories" for the EMDrive (ref. [24], McCulloch 2017, EPL 118, 34003). The paper contains no measurements. It is the starting point of the Dresden programme that later ran the DARPA-funded QI laser-cavity tests.

## Key claims
- **Motivation (ms. p. 1 of 8):** even nuclear propulsion at Isp ≥ 10,000 s needs propellant "on the order of the mass of our sun" to reach the nearest star within a lifetime; Breakthrough Starshot needs a 100 GW laser for gram-scale probes. "Most of these schemes rely on modifying the inertial mass, which in turn could lead to a new propellantless propulsion method."
- **Two routes considered (ms. p. 2):** negative mass (Forward's gravitational dipole, which self-accelerates without violating conservation laws) and variable/oscillating mass (Wanser: momentum conservation applies only to constant-mass systems). The "real challenge" is producing macroscopic negative or oscillating inertial mass.
- **Balance requirements (Sect. 2.1, ms. pp. 2–3):** nN resolution, blocking of electromagnetic interactions, limited balance–chamber-wall interaction. "Vibration and thermal expansion/drifts are the two most important artefacts that must be carefully isolated to obtain reliable measurements."
- **EMDrive (Sect. 2.2, ms. p. 3–4):**
  - Shawyer's radiation-pressure explanation "was highly criticized as not being compatible with electromagnetism and conservation laws".
  - "Alternative theories have appeared [23],[24] including a variable mass approach as outlined above [25], however, the community remains highly sceptical on the theoretical grounds of this concept." [23] is Grahn et al. (2016), [24] McCulloch's "Testing Quantised Inertia on Emdrives with Dielectrics" (EPL 2017), [25] Montillet (Mach-Lorentz theory).
  - Experimentally, high-vacuum tests, "especially NASA's latest test results by White et al [29] revealed that air is not an issue with thrusts up to 80 µN with 80 W input power". But "Thermal drifts were especially significant in the latest reported test by White et al. [29] and possible magnetic interaction with feeding cables has yet to be assessed."
  - Plan: build a White-like EMDrive on the upgraded balance, optimise thermal design, and test other geometries.
- **Mach-Effect Thruster (Sect. 2.3, ms. p. 4):** "Here the theoretical case is much more sound". Woodward's linearised-GR/Sciama analysis predicts mass fluctuations "up to 11 orders of magnitude higher for typical devices than classically expected from E=mc²". Measured effects are "on the order or less than one µN" (Woodward; Buldrini). "Most notably, vibration and thermal effects are critical."
- **Complementary experiments (Sect. 2.4, ms. p. 5):** a rotating mass-fluctuation device (Woodward's hardware); a magnetic-suspension balance to weigh samples heated to 1000 °C (Dmitriev's mass–temperature claims); weight change of polarised ceramic capacitors (cf. the later [capacitor paper](../../03-criticism/2020-tajmar-capacitor-thrust/README.md)); and inertial mass in a charged Faraday cage (Assis / Weber electrodynamics).
- **Conclusion (ms. pp. 5–6):** "It is a high-risk/high-payoff effort. Each thruster concept has its supporters and critics and each of them can be attacked on theoretical grounds and possible experimental artefacts." At least, SpaceDrive is "an excellent educational project".

## Key equations
None. The paper is an overview; it mentions E = mc² for capacitor mass fluctuations only qualitatively (ms. p. 2).

## Data used
- None new. Facilities described: vacuum chamber 0.9 m diameter × 1.5 m, 2300 L Pfeiffer turbo pump plus vibration-isolated scroll pump, 10⁻⁷ mbar range, on a separately isolated concrete block (ms. p. 2).
- **Planned balance features (ms. pp. 2–3):** up to 25 kg of thruster and electronics in two separately shielded boxes; attocube IDS laser displacement sensor (picometre digital resolution); variable eddy-current damping; stepper motors for levelling and for reversing the thruster; two calibration methods (voice coil and electrostatic combs); displacement or force-compensated mode; mu-metal shielding; wireless control via a LabJack T7 Pro with laser links and infrared serial port; four pairs of liquid-metal contacts; LabVIEW scripting. A further test bed rotating the thruster through 360° was being designed.

## Results & predictions
- No thrust results and no predictions. The paper sets out plans; the EMDrive and Mach-Effect measurements appeared in [Kößling et al. 2019](../2019-kossling-spacedrive-balance/README.md) and later Dresden papers.

## Figures
*Figure (local only): Figs. 1–2 — Thrust balance schematic and the balance inside the 0.9 m × 1.5 m vacuum chamber. (PDF p. 4.)*

*Figure (local only): Figs. 3–5 — Planned EMDrive model design, schematic of a Mach-Effect Thruster, and a typical Woodward thruster. (PDF p. 5.)*

## Notable quotes
> "Our intention is to develop an excellent research infrastructure to test new ideas and measure thrusts and/or artefacts with high confidence to determine if a concept works and if it does how to scale it up." (abstract, ms. p. 1 of 8)

> "Alternative theories have appeared [23],[24] including a variable mass approach as outlined above [25], however, the community remains highly sceptical on the theoretical grounds of this concept." (Sect. 2.2, ms. p. 3 of 8)

> "Each thruster concept has its supporters and critics and each of them can be attacked on theoretical grounds and possible experimental artefacts." (Conclusions, ms. pp. 5–6 of 8)

## Criticisms & responses
- **No QI content to criticise:** QI appears only as reference [24] in a list of EMDrive theories, together with the remark that the community "remains highly sceptical" of EMDrive theory in general. This is a citation in passing, not an assessment of QI.
- **McCulloch and the Dresden programme:**
  - 25 Jul 2020: "I persuaded Tajmar to take part in my DARPA-funded project in 2017. The idea was that if I could get even the famous 'Dr Zero' to say 'Hmm..' then the world would listen." He said an early asymmetric copper cavity "immediately, as expected" gave the QI-predicted thrust (140 nN from 0.35 W), but "Later tests though have shown less thrust" ([blog](https://physicsfromtheedge.blogspot.com/2020/07/five-experiments.html)).
  - Oct 2018: he blogged about visiting TU Dresden to talk on QI ([blog](https://physicsfromtheedge.blogspot.com/2018/10/bozeman-montana-or-tu-dresden.html)).
  - The published Dresden laser-cavity results were null; see [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md) and [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md).
- **Media reaction to the first SpaceDrive EMDrive results (2018):** McCulloch argued the media were "attempting to debunk the emdrive based on Tajmar's new result". In his view Tajmar did "not yet even have a working emdrive": QI expected 0.19 mN for the Dresden set-up against 0.004 mN observed ([blog, 24 May 2018](https://physicsfromtheedge.blogspot.com/2018/05/emdrive-trial-by-media.html)). Those results are in the Space Propulsion 2018 paper (Tajmar, Weikert & Monette, SP2018_016), not in this overview.
- **On the EMDrive thrust figure:** the paper's "thrusts up to 80 µN with 80 W" summarises White et al. 2016/17 (ms. p. 3). See [2016-white-eagleworks](../2016-white-eagleworks/README.md) for that paper's own numbers.

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2019-kossling-spacedrive-balance](../2019-kossling-spacedrive-balance/README.md), [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md), [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md), [2016-white-eagleworks](../2016-white-eagleworks/README.md), [2017-mcculloch-emdrives-dielectrics](../../01-papers/2017-mcculloch-emdrives-dielectrics/README.md), [2010-mcculloch-tajmar-effect-explained](../../01-papers/2010-mcculloch-tajmar-effect-explained/README.md), [2017-millis-inertial-frames](../../01-papers/2017-millis-inertial-frames/README.md)
