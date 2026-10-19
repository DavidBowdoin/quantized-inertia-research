---
title: "Thrust measurements of microwave-, superconducting- and laser-type emdrives"
authors: [Oliver Neunzig, Marcel Weikert, Martin Tajmar]
year: 2022
type: experiment-report
venue: "Acta Astronautica 195:583-595"
doi: 10.1016/j.actaastro.2022.02.014
arxiv:
url: "https://doi.org/10.1016/j.actaastro.2022.02.014"
open_access: false
files: []
status: critical
tags: [emdrive, lab-test, laser, null-result, propulsion, superconducting, tu-dresden, direct-qi-test, darpa-collaborator]
---

# Thrust measurements of microwave-, superconducting- and laser-type emdrives

**Citation:** Neunzig, O., Weikert, M. & Tajmar, M. (2022). *Thrust measurements of microwave-, superconducting- and laser-type emdrives*. Acta Astronautica, 195, 583–595. https://doi.org/10.1016/j.actaastro.2022.02.014.

The journal version is paywalled, so no PDF is stored. This summary is based on the conference version, IAC-21-C4.10-C3.5.1.x63502 (72nd International Astronautical Congress, Dubai, 25–29 Oct 2021, 15 pp.), hosted by TU Dresden ([PDF](https://tu-dresden.de/ing/maschinenwesen/ilr/rfs/ressourcen/dateien/forschung/folder-2007-08-21-5231434330/ag_raumfahrtantriebe/IAC-Thrust-Measurements-of-Microwave-Superconducting-and-Laser-Type-EMDrives.pdf)). It was read but not stored.
> [!UNVERIFIED] Differences between the IAC version and the Acta Astronautica version; the journal abstract was not available via Crossref or Semantic Scholar, and ScienceDirect blocked access.

**TL;DR:** This is the Dresden follow-up to [Tajmar et al. 2021](../2021-tajmar-emdrive-false-positive/README.md) and [Neunzig et al. 2021/22](../2022-neunzig-laser-resonators/README.md). It explicitly "engaged the recent criticism by the inventors of our devices under test", including McCulloch's objections to the QI laser-cavity tests. Four kinds of device were tested:
1. A microwave EMDrive with a spherical end-cap and no dielectric.
2. A superconducting (YBCO end-cap) EMDrive at cryogenic temperature, on a balance cooled with solid nitrogen down to 65 K.
3. The QI silver cavities with the aluminium case removed, and a Taylor resonator wrapped in an asymmetric metal cone.
4. A fibre-optic loop operated outside the vacuum chamber.

None produced thrust above balance noise. Apart from the superconducting cavity, where the noise floor is higher, all results stay below classical photon thrust.

## Key claims
- **Balance:** the inverted double pendulum resolves a 0.5 W laser, 1.67 nN, at a thrust-to-noise ratio of 10, for thruster masses up to 10 kg. The vacuum chamber reaches about 10⁻⁷ mbar. The microwave EMDrive ran on an on-board battery with no electrical feedthroughs.
- **Microwave EMDrive (spherical end-cap, no dielectric):** four resonances at 1918, 1945, 2030 and 2054 MHz, with loaded Q of 113, 486, 677 and 1027. No thrust at any of them. An "inventor's pre-load condition" of ±10 µN was also tested and made no difference.
- **Superconducting EMDrive:** with an HDPE dielectric, no superconducting resonances formed. Without it, resonances at 1819 and 1959 MHz appeared only below T_c = 92 K, with loaded Q up to about 2600. Comparisons above and below T_c showed no thrust above noise.
- **QI laser devices, retested after McCulloch's criticism:**
  - "According to McCulloch the resonators should have never been able to generate thrust due to an aluminium plate being present … We removed the aluminium case from the cavity and retested each of the three resonators … The only setup change of removing the aluminium plate did not have any effect on measured thrust whatsoever."
  - Taylor-Light was enclosed in a tapered aluminium cone with an end-cap, because McCulloch said "the beam requires an asymmetric metal cavity". The result was pure photon thrust.
  - Fibre-optic loop: McCulloch "suggested that the vacuum chamber itself was responsible for the nonexistent thrust", because its conductive walls cancel Unruh radiation. The balance was moved onto a marble table in the lab, with "no metallic objects in at least 80 m distance" in front of and behind the coil. Still no thrust: "The vacuum chamber did not hide the proposed QI effects."
- **Conclusion:** "None of the enhancements in any laser resonator setup revealed anomalous thrust." "In summary, we did not encounter unsolvable false-positive thrust signatures in any of our tested devices. Neither the microwave- and superconducting cavities nor the infrared laser resonators passed our requirements for a breakthrough in space propulsion."
- **Funding:** DLR/BMWi (50RS1704) and **DARPA DSO award HR001118C0125**, the award that funded McCulloch's QI programme.

## Key equations
Comparison formulae used in the result tables. S is the force-amplification (reflection) factor for photon devices; Q is the loaded Q for microwave cavities:
$$ F_{QI} = \frac{P\,S}{c}, \qquad F_{\rm photon} = \frac{P}{c} \quad (S = 1), \qquad F_{\rm pred} = \frac{P\,Q}{c} $$

## Data used
- Thrust-balance profiles in vacuum, and in air for the loop test outside the chamber; S11 and sense-antenna power scans; cryogenic runs with solid nitrogen at about 10¹ mbar.

## Results & predictions
Values are taken from the IAC paper's tables.

| Device | Power | Prediction | Photon thrust | Measured |
|---|---|---|---|---|
| Silver cavities CC/CX, CC/CC, Circle (no Al case) | 279 / 467 mW | 36 / 60 nN | 0.93 / 1.56 nN | 0.89–1.04 nN / 1.50–1.65 nN (± 0.12–0.41) |
| Taylor-Light + tapered metal cavity | 289 / 493 mW | 482 / 822 nN | 0.96 / 1.64 nN | (1.01 ± 0.30) / (1.62 ± 0.26) nN |
| Fibre-optic coil: no shield, small-radius shield, big-radius shield | 31 / 203 mW average | 0.34 / 2.23 µN (> for shielded) | — | between (0.01 ± 0.19) and (0.09 ± 0.18) µN |
| Spherical microwave EMDrive (Q 113–1027) | 4.2–10 W | 2261–6808 nN at listed resonances (F = PQ/c) | 14–33 nN | balance noise only |
| Superconducting EMDrive (Q ≈ 2063–2599) | 18–19 W | 156–164 µN (F = PQ/c) | — | (0.14 ± 0.23), (0.05 ± 0.24), (−0.33 ± 0.54), (0.07 ± 0.08) µN |

- For the earlier NASA-like cavity with worst-case assumptions, "the predicted force values reached up to 22.5 µN for the power levels used, but each thrust measurement at either of the resonance frequencies resulted in balance noise only."

> [!UNVERIFIED] The exact row-by-row mapping of the microwave and superconducting table entries; the PDF table text layer is garbled, and values are given as ranges.

## Figures
No PDF stored, so no figures are reproduced. In the IAC paper, Fig. 8 shows the superconducting EMDrive on the balance, Figs. 15–16 the Taylor set-up with a metal cone, and Figs. 18–20 the fibre loop outside the vacuum chamber.

## Notable quotes
> "The only setup change of removing the aluminium plate did not have any effect on measured thrust whatsoever." (IAC paper, Sect. 5.2)

> "The vacuum chamber did not hide the proposed QI effects." (IAC paper, Sect. 5.5, "Fiberoptic Loop – Results & Discussion")

## Criticisms & responses
- **This paper is itself a response to McCulloch's critique** of the 2021 laser tests ([blog, 27 Apr 2021](https://physicsfromtheedge.blogspot.com/2021/04/response-to-tajmars-new-cavity-results.html)). See [2022-neunzig-laser-resonators](../2022-neunzig-laser-resonators/README.md) for the full exchange.
- **McCulloch's reaction (blog, 23 Jan 2022).** He cites this work as "Neunzig, O., M. Weikert and M. Tajmar, 2021. Thrust measurements of microwave-, superconducting and laser type emdrives. 72nd IAC, Dubai." He changed the interpretation rather than the theory. Light-based QI thrusters "did not perform well", whereas electron-based (capacitor) thrusters did. He traces this to his earlier assumption that v = c. With the correct speed, he says, QI "accounts for the effectively zero thrusts seen by Tajmar's team for the laser cavities". He also says QI "still predicts the emdrive", now via Unruh waves seen by electrons in the cavity walls, and that "QI has not been falsified" ([blog](https://physicsfromtheedge.blogspot.com/2022/01/learning-from-experiments.html)). Whether a revised QI prediction for these specific devices has been published was not checked here.
  > [!UNVERIFIED] Whether McCulloch published a quantitative revised prediction for the Dresden laser or EMDrive configurations.
- **Remaining issue for EMDrive proponents (factual):** the microwave cavities' loaded Q values (113–1027, and about 2600 superconducting) are lower than the Q values Shawyer and NASA reported (thousands to tens of thousands). Proponents have cited this kind of gap in Q as a reason for null results. The superconducting test was designed to raise Q.

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2022-neunzig-laser-resonators](../2022-neunzig-laser-resonators/README.md), [2021-tajmar-emdrive-false-positive](../2021-tajmar-emdrive-false-positive/README.md), [2017-taylor-laser-resonators](../../01-papers/2017-taylor-laser-resonators/README.md), [2015-mcculloch-emdrive-pip](../../01-papers/2015-mcculloch-emdrive-pip/README.md), [2017-mcculloch-emdrives-dielectrics](../../01-papers/2017-mcculloch-emdrives-dielectrics/README.md), [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md), [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md), [2019-kossling-spacedrive-balance](../../04-experiments/2019-kossling-spacedrive-balance/README.md)
