---
title: "Measurement of Impulsive Thrust from a Closed Radio-Frequency Cavity in Vacuum"
authors: [Harold White, Paul March, James Lawrence, Jerry Vera, Andre Sylvester, David Brady, Paul Bailey]
year: 2017
type: experiment-report
venue: "Journal of Propulsion and Power 33(4):830-841 (online Nov 2016)"
doi: 10.2514/1.B36120
arxiv:
url: "https://doi.org/10.2514/1.B36120"
open_access: true
license: NTRS-public-use-permitted
files: [paper.pdf, figures/fig-13-forward-thrust-vacuum.png, figures/fig-18-null-test.png, figures/fig-19-thrust-vs-power.png]
status: neutral
tags: [emdrive, nasa-eagleworks, torsion-pendulum, vacuum, positive-claim]
---

# Measurement of Impulsive Thrust from a Closed Radio-Frequency Cavity in Vacuum

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because NTRS's "public use permitted" is not an open licence. Read the paper at [doi:10.2514/1.B36120](https://doi.org/10.2514/1.B36120).

**Citation:** White, H., March, P., Lawrence, J., Vera, J., Sylvester, A., Brady, D. & Bailey, P. (2017). *Measurement of Impulsive Thrust from a Closed Radio-Frequency Cavity in Vacuum*. Journal of Propulsion and Power, 33(4), 830–841 (online November 2016). https://doi.org/10.2514/1.B36120.

The stored PDF is the NASA Technical Reports Server copy (NTRS 20170000277), a 34-page manuscript-format document. Page numbers below refer to it.

**TL;DR:** NASA JSC Eagleworks tested a tapered, dielectrically loaded copper RF cavity excited in the TM212 mode at 1937 MHz. It sat on a torsion pendulum in vacuum below 8 × 10⁻⁶ Torr, at 40, 60 and 80 W. Forward, reverse and null orientations were tested. The team separated an "impulsive" signal from a thermal baseline (centre-of-gravity drift) with a superposition model. They report a thrust-to-power ratio of **1.2 ± 0.1 mN/kW**, with the force directed towards the narrow end. The null tests identified no mundane source. The paper interprets the result with a quantum-vacuum pilot-wave / "Q-thruster" model, **not QI**. McCulloch later used these data in his QI comparisons. TU Dresden later reproduced a similar signal as an artefact ([Tajmar et al. 2021](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md)).

## Key claims
- **Test article:** integrated tapered cavity with RF amplifier and electronics on the pendulum arm; later a "split" configuration with the amplifier separate, which reduced the thermal contribution. Ambient "green runs" were used to confirm tuning before vacuum runs.
- **Signal analysis:** the displacement is modelled as an impulsive (step) thrust superposed on a thermally shifting baseline caused by thermal expansion of the aluminium heat sink and amplifier. The thermal drift is larger in vacuum because radiative cooling is limited. A slope-filtering method extracts the impulsive part.
- **Error budget (p. 18, table):** SA210 ±1 µN, fin calibration ±2.2 µN, seismic ±2.2 µN, thermal ±4.5 µN, others below 1 µN. Total ±6 µN.
- **Interpretation (Sect. II):** the thrust is attributed to momentum exchange with the quantum vacuum, treated as a dynamic medium. This is a pilot-wave / stochastic-electrodynamics picture in which the zero-point field plays the role of the guiding wave.
- **Context given by the authors:** 1.2 mN/kW is about an order of magnitude below a Hall thruster (about 60 mN/kW), but more than two orders above light sails and photon rockets (3.33–6.67 µN/kW).
- **Caveat stated by the authors:** "future testing efforts should seek to develop testing approaches that are immune to CG shifts from thermal expansion", and "a modified Cavendish balance approach could be employed to definitively rule out thermal" (p. 32).

## Key equations
None central to the result. The extracted quantity is thrust-to-power, with forward-thrust values at 40/60/80 W in vacuum of about 30–128 µN (tables, pp. 20 and 22).

## Data used
- Torsion-pendulum displacement (optical displacement sensor), electrostatic-fin calibration pulses, RF power measurements, and IR thermal imagery (Fluke Ti100). Vacuum runs: three at each power for forward thrust, three at each power for reverse thrust, and three null runs at 80 W.

## Results & predictions
- Forward thrust, vacuum (as tabulated): Run 1 at 40.1 / 60.6 / 81.3 W gave 48 ± 6 / 106 ± 6 / 76 ± 6 µN. Run 2 gave 30 ± 6 / 91 ± 6 / 119 ± 6 µN. Run 3 gave 53 ± 6 / 128 ± 6 / 117 ± 6 µN.
- Reverse thrust, vacuum: values of 30–83 µN in the same power ranges.
- Null orientation (80 W): shifting thermal baseline, no impulsive thrust (Fig. 18).
- Overall: 1.2 ± 0.1 mN/kW, "very close to the average impulsive performance measured in air" (p. 32).

## Figures
*Figure (local only): Fig. 13 — Forward thrust in vacuum, representative runs at 40, 60 and 80 W, with ±6 µN error bars; impulsive pulse superposed on thermal baseline. (Rendered NTRS p. 21.)*

*Figure (local only): Fig. 18 — Null-thrust test run at 80 W in vacuum: shifting baseline due to thermal effects, no impulsive thrust. (Rendered NTRS p. 25.)*

*Figure (local only): Fig. 19 — Forward and reverse thrust in vacuum versus power, with linear fit giving ≈1.2 mN/kW. (Rendered NTRS p. 29.)*

## Notable quotes
> "Thrust data from forward, reverse, and null suggests that the system is consistently performing with a thrust to power ratio of 1.2 ± 0.1 mN/kW." (p. 1, abstract)

> "As indicated in the error section, a modified Cavendish balance approach could be employed to definitively rule out thermal." (p. 32)

## Criticisms & responses
- **McCulloch's use of these data (blog):**
  - 28 Nov 2016: in his predicted-versus-observed plot, the NASA points are "all shifted rightwards. This shows that MiHsC over-predicts the thrust for NASA's tests by a factor that can be as much as ten." He proposed that the dielectric at the narrow end reduces the effective taper. This idea became [McCulloch 2017, EPL "Testing quantised inertia on emdrives with dielectrics"](../../01-papers/2017-mcculloch-emdrives-dielectrics/README.md) ([blog](https://physicsfromtheedge.blogspot.com/2016/11/emdrives-dielectrics-nasa-shift.html)).
  - 8 Dec 2016: he called NASA's own vacuum-plasma model "adjustable and complex so it's easy to get the right answer for the wrong reason" ([blog](https://physicsfromtheedge.blogspot.com/2016/12/notes-on-emdrive-and-mihsc.html)).
  - 24 May 2018: he cited this paper's forward, reverse and null configurations as evidence that the thrust followed the cavity, not the cables, so it was not a Lorentz force ([blog](https://physicsfromtheedge.blogspot.com/2018/05/emdrive-trial-by-media.html)).
- **TU Dresden replication and critique:** [Tajmar, Neunzig & Weikert (2021/22)](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md) used White's cavity geometry. A conventional mount gave about 1 µN/W, "similar to the one reported by White et al.", which disappeared with a bearing mount and battery power. They point out that in White et al.'s set-up "the damping magnet was mounted on the external supporting structure and not on the balance arm, which can very well cause orientation-dependent magnetic interaction forces of similar magnitude compared to their claimed thrusts". They also call the single-arm torsion balance "far too sensitive to center of gravity shifts due to thermal expansion".
- **Earlier Dresden work:** [Tajmar et al. 2018, SpaceDrive](../2018-tajmar-spacedrive/README.md) notes that thermal drifts "were especially significant in the latest reported test [White et al.]" and that "possible magnetic interaction with feeding cables has yet to be assessed". [Kößling et al. 2019](../2019-kossling-spacedrive-balance/README.md) found a similar-magnitude signal (about 3–3.4 µN) that they identified as thermal drift.

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2015-mcculloch-emdrive-epl](../../01-papers/2015-mcculloch-emdrive-epl/README.md), [2015-mcculloch-emdrive-pip](../../01-papers/2015-mcculloch-emdrive-pip/README.md), [2017-mcculloch-emdrives-dielectrics](../../01-papers/2017-mcculloch-emdrives-dielectrics/README.md), [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md), [2016-samsonov-emdrive-null](../../03-criticism/2016-samsonov-emdrive-null/README.md)
- Media: [2016-jalopnik-emdrive](../../07-media/2016-jalopnik-emdrive/README.md), [2016-register-emdrive-inertia](../../07-media/2016-register-emdrive-inertia/README.md), [2016-koberlein-theoretical-dream-emdrive](../../07-media/2016-koberlein-theoretical-dream-emdrive/README.md)
