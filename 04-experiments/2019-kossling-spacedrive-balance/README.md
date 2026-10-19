---
title: "The SpaceDrive project - Thrust balance development and new measurements of the Mach-Effect and EMDrive Thrusters"
authors: [Matthias Kößling, Maxime Monette, Marcel Weikert, Martin Tajmar]
year: 2019
type: experiment-report
venue: "Acta Astronautica 161:139-152"
doi: 10.1016/j.actaastro.2019.05.020
arxiv:
url: "https://doi.org/10.1016/j.actaastro.2019.05.020"
open_access: false
files: []
status: critical
tags: [emdrive, mach-effect, tu-dresden, thrust-balance, thermal-drift, null-result]
---

# The SpaceDrive project - Thrust balance development and new measurements of the Mach-Effect and EMDrive Thrusters

**Citation:** Kößling, M., Monette, M., Weikert, M. & Tajmar, M. (2019). *The SpaceDrive project – Thrust balance development and new measurements of the Mach-Effect and EMDrive Thrusters*. Acta Astronautica, 161, 139–152. https://doi.org/10.1016/j.actaastro.2019.05.020.

The journal version is paywalled, so no PDF is stored. This summary uses the published abstract and the conference version presented at the 69th International Astronautical Congress, Bremen, 1–5 Oct 2018 (IAC-18,C4,7-C3.5,5,x46021; 16 pp.), hosted by TU Dresden ([PDF](https://tu-dresden.de/ing/maschinenwesen/ilr/rfs/ressourcen/dateien/forschung/folder-2007-08-21-5231434330/ag_raumfahrtantriebe/IAC-The-SpaceDrive-Project-Thrust-Balance-Development-and-New-Measurements-of-the-Mach-Effect-and-EMDrive-Thrusters.pdf)). That version was read but not stored.

**TL;DR:** The paper describes an automated torsion balance. It resolves about 100 nN in the journal abstract and 11 nN in the IAC conclusion, for devices up to 10 kg. Features include electromagnetic calibration, magnetic damping, tilt control, mu-metal shielding, infrared wireless control, three liquid-metal feedthroughs (≤ 500 V/200 kHz, ≤ 30 kV, ≤ 3 GHz) and 180° rotation without breaking vacuum. With it the team tested Woodward's Mach-Effect Thrusters, their own MET, a magnetostrictive variant and an EMDrive in several configurations (August–September 2018). The **journal abstract** says "no final conclusions can be drawn". The **IAC version** is more direct: "So far, only thermal drifts and no real thrust has been observed in all our measurements". The EMDrive signals of about 3–3.4 µN, similar in size to NASA/March's reported 4.7 µN at 3.2 W, were identified as thermal drift. QI is cited (McCulloch 2015) only among EMDrive theories.

## Key claims
- Claimed forces under test: sub-µN up to 2 µN for the Mach-Effect Thruster and up to 90 µN for the EMDrive, depending on power. The IAC text attributes the sub-µN–2 µN figure to its MET references [3],[4] and the 90 µN figure to EMDrive reference [2].
- **Balance:** calibration factor 6.7 µN/µm (example). Overnight runs of 200 × 1 µN pulses showed 0.9 µN, a 10% discrepancy still to be optimised. For 25 s pulses the balance reached only 0.8 µN, because it does not reach steady state.
- **Drift handling:** linear fits to off-sectors remove inherent drift, but "the thermal drift is mostly non-linear (for both heating up and cooling down)".
- **Mach-Effect Thruster:** Woodward claimed 1–5 µN at 200–250 V; Buldrini replicated 0.2 µN at 100 V. The Dresden 0° run peaked at 2 µN at 140 V, but its shape "does not show impulse-like behavior". "The fact that the reverse measurement (180°) does not show the same force magnitude indicates that the observed force signal most likely results from non-linear thermal drift." The magnetostrictive device "did not show the any thrust".
- **EMDrive:** amplifier outside the chamber with an RF feedthrough (4 dB loss). An average of 55 profiles with 60 s pulses gave 3.4 µN after drift removal, but "the shape of the graph seems to indicate the effect of a thermal drift rather than a net thrust". Without the HDPE disc at about 1920 MHz the team saw 3.0 µN, again identified as thermal drift. "Our latest measurements on the EMDrive in different configurations and frequency ranges seem to indicate only thermal drifts."

## Key equations
None central for this archive.

## Data used
- Thrust-balance profiles in vacuum, averaged over many repetitions (e.g. 55 or 80 profiles), with voice-coil calibration pulses of −12 to +12 µN.

## Results & predictions
- MET: forces of up to about 2 µN that do not reverse with orientation, attributed to thermal drift. Magnetostrictive MET: no thrust.
- EMDrive: 3.0–3.4 µN signals attributed to thermal drift, "similar to the values reported by March (4.7 µN for 3.2 W)", except that March saw a step response where Dresden saw drift.
- Journal-level conclusion (abstract): "Results of the tests performed between August and September 2018 are presented, but no final conclusions can be drawn."

## Figures
No PDF stored, so no figures are reproduced.

## Notable quotes
> "The device can be rotated by 180° to measure three different thrust directions without breaking the vacuum and changing the setup in order to gain confidence and refute e.g. thermal drifts." (abstract)

> "So far, only thermal drifts and no real thrust has been observed in all our measurements." (IAC version, abstract)

## Criticisms & responses
- **Discrepancy within the batch metadata:** this archive's batch summary said that "apparent EMDrive thrust was traced to experimental artefacts". The IAC version supports this ("thermal drifts"). The *journal* abstract is more cautious ("no final conclusions can be drawn").
  > [!UNVERIFIED] Whether the journal body text differs from the IAC version on this point.
- **McCulloch's response:** no post specifically about this paper was found. In May 2018, reacting to the earlier Dresden EMDrive results, he argued that Tajmar did "not yet even have a working emdrive". He cited a QI expectation of 0.19 mN against 0.004 mN observed. He also relayed a comment from Phil Wilson that the cavity "does not have a resonance at 1.865GHz (the frequency he is inputting)" ([blog](https://physicsfromtheedge.blogspot.com/2018/05/emdrive-trial-by-media.html)).
- **Later Dresden work** resolved the EMDrive question with a different balance (inverted counterbalanced double pendulum) and battery power: [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md).

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2018-tajmar-spacedrive](../2018-tajmar-spacedrive/README.md), [2016-white-eagleworks](../2016-white-eagleworks/README.md), [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md), [2015-mcculloch-emdrive-pip](../../01-papers/2015-mcculloch-emdrive-pip/README.md), [2018-mcculloch-propellantless-propulsion](../../01-papers/2018-mcculloch-propellantless-propulsion/README.md)
