---
title: "EmDrive (asymmetric microwave cavity thrust)"
tags: [emdrive, propulsion, lab-test, null-result, tu-dresden, nasa-eagleworks]
verdict: refuted-or-null
---

# EmDrive

## The phenomenon and the data
- **Claim:** a closed, tapered (truncated-cone) microwave cavity produces a net thrust towards its narrow end with no exhaust. That would violate momentum conservation unless something external takes up the momentum.
- **Claimed thrusts used in QI comparisons** ([2015-mcculloch-emdrive-epl](../01-papers/2015-mcculloch-emdrive-epl/README.md)):
  - Shawyer S1 16 mN and S2 80–214 mN.
  - Cannae 9 mN.
  - NASA Eagleworks 2014: 0.091, 0.05, 0.055 mN, and 0.03 mN in vacuum.
  - Tajmar & Fiedler 2015: 0.02–0.11 mN.

  The input data were mostly conference reports without full error budgets. Some cavity dimensions were estimated from photographs by forum members.
- **NASA Eagleworks, White et al. 2017** (J. Propulsion & Power 33, 830; [2016-white-eagleworks](../04-experiments/2016-white-eagleworks/README.md)):
  - Set-up: a torsion pendulum in vacuum (< 8 × 10⁻⁶ Torr) at 40/60/80 W.
  - Result: **1.2 ± 0.1 mN/kW** towards the narrow end, with forward thrusts of about 30–128 µN (±6 µN).
  - Interpretation: the authors explain the thrust with a quantum-vacuum pilot-wave model, *not* QI. They acknowledge that thermal centre-of-gravity shifts need a "modified Cavendish balance approach ... to definitively rule out thermal".
- **Null and artefact results:**
  - **Samsonov 2016** (viXra, amateur, in air; [2016-samsonov-emdrive-null](../03-criticism/2016-samsonov-emdrive-null/README.md)): battery-powered, wireless, on a 3 m tungsten pendulum. Any force is below ~40 µN, against a Shawyer prediction of 640 µN. Spurious thermal forces were observed. No QI prediction was computed.
  - **Kößling et al. 2019, Dresden** ([2019-kossling-spacedrive-balance](../04-experiments/2019-kossling-spacedrive-balance/README.md)): 3.0–3.4 µN signals, similar to March's 4.7 µN at 3.2 W, that follow the cavity temperature. The journal text (accepted manuscript) says they "seem to indicate the presence of thermal drifts" but, with no 180° or 90° runs, "there can be no definite conclusions"; the stronger IAC-18 wording ("only thermal drifts and no real thrust") is not in the journal version.
  - **Tajmar, Neunzig & Weikert 2021/22** (CEAS Space J. 14, 31; [2021-tajmar-emdrive-false-positive](../03-criticism/2021-tajmar-emdrive-false-positive/README.md)):
    - Set-up: a replica of the White et al. geometry. A conventional mount reproduced ~1 µN/W, "similar to the one reported by White et al.".
    - With a bolt-bearing mount and battery power the signal vanished. Noise was 10–30 nN, and there was no thrust above the photon-thrust limit (36 nN at 11 W).
    - Conclusion: earlier claims are ruled out "by at least two orders of magnitude".
  - **Neunzig, Weikert & Tajmar 2022** (Acta Astronautica 195, 583; [2022-neunzig-emdrive-thrust](../03-criticism/2022-neunzig-emdrive-thrust/README.md)):
    - Devices: a spherical-end-cap EmDrive (loaded Q 113–1027, 4.2–10 W) and a superconducting YBCO EmDrive (Q 2063–2599, 18–19 W, in liquid/solid nitrogen at about −196 to −202 °C; the balance itself is rated down to 65 K).
    - F = PQ/c predicted 2.3–22.6 µN and 156–164 µN respectively. Measured: (−11 ± 25) to (13 ± 31) nN, and (−0.33 ± 0.54) to (0.14 ± 0.23) µN, i.e. balance noise only (Tables B1–B2, p. 594).

- **Editorial ledger ([A3](../09-analysis/a3-thrust-ledger/README.md)).** Dresden's PQ/c predictions for their own EmDrives exceed the descriptive bounds max(m, 0) + 2σ by 30–377× (copper, spherical end cap), 144–273× (superconducting) and, applying the same convention to the White-geometry replica, 175–383×. These ratios are conditional on that adaptation, not calibrated confidence levels. The implemented McCulloch formulas reproduce the tabulated comparisons within rounding (2018 Eq. 7 is transcribed only); across the five model versions, Shawyer 1 goes from 0.24× to −0.99× to 1.6× the claimed 16 mN.

## Mainstream explanation(s)
- **Experimental artefacts**, as catalogued by TU Dresden:
  - thermal expansion and centre-of-gravity shifts;
  - thermally dependent cable stiffness;
  - buoyancy (~150 µN per °C in air);
  - liquid-metal-contact forces;
  - magnetic interaction of cables and damping magnets with the Earth's field. In White et al.'s set-up "the damping magnet was mounted on the external supporting structure and not on the balance arm".
- With these removed, no force above classical photon thrust (P/c) remains.

## QI's prediction
- **Progress in Physics 2015** ([2015-mcculloch-emdrive-pip](../01-papers/2015-mcculloch-emdrive-pip/README.md)): photons in the cavity are assumed to have Unruh-wave inertia, with the cavity walls as the horizon. The 1-D formula is

  $$ F = -\frac{PQL}{c}\left(\frac{1}{w_{big}} - \frac{1}{w_{small}}\right) $$

  - It gets the right order of magnitude in 4 of 5 cases and is 10× too high for NASA B2.
  - The paper was accepted one day after submission.
  - The S2 worked example uses L = 0.325 m while the table lists 0.345 m.
- **EPL 2015** ([2015-mcculloch-emdrive-epl](../01-papers/2015-mcculloch-emdrive-epl/README.md)): a crude 3-D average,

  $$ F = -\frac{6PQL}{c}\left(\frac{1}{L+4w_s} - \frac{1}{L+4w_b}\right) $$

  - Results: the right order of magnitude for 8 tests, but "over a factor of ten out" for NASA B2 and B4v.
  - It predicts thrust reversal when L = w_s.
  - It relies on two "controversial assumptions": a variable photon inertial mass and a variable speed of light in the cavity.
- **EPL 2017, dielectrics** ([2017-mcculloch-emdrives-dielectrics](../01-papers/2017-mcculloch-emdrives-dielectrics/README.md)):
  - It drops the photon-acceleration assumption and treats a dielectric as widening that end by n.
  - NASA predictions fall from 10× too high to within a factor of ~1–6 (worst: 0.01 vs 0.055 mN for the 2.6 W 2014 run), e.g. 2016 runs 0.06/0.09/0.13 vs 0.04/0.09/0.09 mN.
  - Shawyer 1 now has the right magnitude but the **wrong sign** (−15.84 vs +16 mN).
- **J. Space Exploration 2018** ([2018-mcculloch-propellantless-propulsion](../01-papers/2018-mcculloch-propellantless-propulsion/README.md)): F = (PQL/2c)(1/Δx_left − 1/Δx_right), derived from the uncertainty principle, predicts 4.2 mN for Shawyer S1 against 16 mN observed.
- **Dresden 2018.** McCulloch blogged a QI expectation of 0.19 mN against 0.004 mN observed. He argued that Dresden did "not yet even have a working emdrive" ([2018-tajmar-spacedrive](../04-experiments/2018-tajmar-spacedrive/README.md)).
- **2022 reinterpretation** (blog). The thrust "may now not be due to the Unruh waves from the microwaves but from the Unruh waves seen by electrons ... in the metal walls", and "QI still predicts the emdrive" ([2021-tajmar-emdrive-false-positive](../03-criticism/2021-tajmar-emdrive-false-positive/README.md)).

## Independent tests, critiques and null results
- **The thrust itself is not real.** The highest-precision tests, by TU Dresden and partly funded by the same DARPA award (HR001118C0125) that funded McCulloch's QI programme, found no thrust above photon pressure. That leaves nothing for QI to explain. The Dresden authors describe all EmDrive theories, QI included, as "highly controversial".
- **Meaning of Q.** Dresden note that in McCulloch's definition "Q is not the quality factor but the number of reflections within the cavity". This choice affects every prediction.
- **Model flexibility.** QI's "no free parameters" claim is weakened by the successive changes:
  - a 1-D formula, then a 3-D one;
  - a dielectric correction applied per experiment, which flips one sign;
  - a 2018 uncertainty-principle formula;
  - a 2022 switch from photons to wall electrons.
- **Remaining proponent argument.** Proponents cite lower Q in the Dresden cavities (100s–2600) than in Shawyer's or NASA's (thousands to tens of thousands). The superconducting test was designed to address this and still found nothing.
- **Press.** Press coverage around 2016 amplified QI as an EmDrive explanation. Koberlein criticised both the physics and the reporting ([2016-koberlein-theoretical-dream-emdrive](../07-media/2016-koberlein-theoretical-dream-emdrive/README.md), [2016-jalopnik-emdrive](../07-media/2016-jalopnik-emdrive/README.md), [2016-register-emdrive-inertia](../07-media/2016-register-emdrive-inertia/README.md), [2016-mittechreview-flyby-emdrive](../07-media/2016-mittechreview-flyby-emdrive/README.md)).

## Assessment
The EmDrive thrust that QI was fitted to has not survived better measurement. TU Dresden reproduced a NASA-like ~1 µN/W signal as a mounting artefact. With improved balances and battery power, they measured no force above classical photon thrust, two or more orders of magnitude below earlier claims. Their tests include high-Q superconducting cavities. QI's agreement with the earlier claimed thrusts was within an order of magnitude at best. It needed several model revisions, including one that reversed a predicted sign. A good fit to spurious data is not evidence for the theory. On present evidence the effect is null, and McCulloch's later move to an electron-based mechanism has no published quantitative test.

## Sources
- [2015-mcculloch-emdrive-pip](../01-papers/2015-mcculloch-emdrive-pip/README.md)
- [2015-mcculloch-emdrive-epl](../01-papers/2015-mcculloch-emdrive-epl/README.md)
- [2017-mcculloch-emdrives-dielectrics](../01-papers/2017-mcculloch-emdrives-dielectrics/README.md)
- [2018-mcculloch-propellantless-propulsion](../01-papers/2018-mcculloch-propellantless-propulsion/README.md)
- [2016-white-eagleworks](../04-experiments/2016-white-eagleworks/README.md)
- [2018-tajmar-spacedrive](../04-experiments/2018-tajmar-spacedrive/README.md)
- [2019-kossling-spacedrive-balance](../04-experiments/2019-kossling-spacedrive-balance/README.md)
- [2016-samsonov-emdrive-null](../03-criticism/2016-samsonov-emdrive-null/README.md)
- [2021-tajmar-emdrive-false-positive](../03-criticism/2021-tajmar-emdrive-false-positive/README.md)
- [2022-neunzig-emdrive-thrust](../03-criticism/2022-neunzig-emdrive-thrust/README.md)
- Media: [2016-jalopnik-emdrive](../07-media/2016-jalopnik-emdrive/README.md), [2016-koberlein-theoretical-dream-emdrive](../07-media/2016-koberlein-theoretical-dream-emdrive/README.md), [2016-register-emdrive-inertia](../07-media/2016-register-emdrive-inertia/README.md), [2016-mittechreview-flyby-emdrive](../07-media/2016-mittechreview-flyby-emdrive/README.md)
- Related evidence: [propulsion](propulsion.md), [lab-tests](lab-tests.md)
