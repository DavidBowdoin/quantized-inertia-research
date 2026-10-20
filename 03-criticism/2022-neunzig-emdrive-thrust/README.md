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
license: all-rights-reserved
files: [paper.pdf, figures/fig-1-silver-cavity.png, figures/fig-2-taylor-cone.png, figures/fig-3-fibre-loop.png]
status: critical
tags: [emdrive, lab-test, laser, null-result, propulsion, superconducting, tu-dresden, direct-qi-test, darpa-collaborator]
---

# Thrust measurements of microwave-, superconducting- and laser-type emdrives

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.1016/j.actaastro.2022.02.014](https://doi.org/10.1016/j.actaastro.2022.02.014).

**Citation:** Neunzig, O., Weikert, M. & Tajmar, M. (2022). *Thrust measurements of microwave-, superconducting- and laser-type emdrives*. Acta Astronautica, 195, 583–595. https://doi.org/10.1016/j.actaastro.2022.02.014. Received 14 Dec 2021, revised 14 Feb 2022, accepted 17 Feb 2022.

**Stored version:** the typeset Acta Astronautica version (13 pp., "© 2022 IAA. Published by Elsevier Ltd. All rights reserved"), supplied by the archive owner and kept local only. Page numbers are journal pages 583–595 (PDF p. 1 = p. 583). An earlier version of this entry was written from the conference paper IAC-21-C4.10-C3.5.1.x63502 (Dubai, Oct 2021). The journal text has the same experiments and conclusions; differences found are noted below.

**TL;DR:** The Dresden follow-up to [Tajmar et al. 2021](../2021-tajmar-emdrive-false-positive/README.md) and [Neunzig et al. 2021](../2022-neunzig-laser-resonators/README.md). It implements "all the requested changes" from the devices' advocates, Shawyer and McCulloch (p. 583). Tested:
1. a microwave EMDrive with a spherical end-cap and no dielectric, on battery power;
2. a superconducting (YBCO) EMDrive cooled with liquid, then solid, nitrogen on the balance;
3. the QI silver laser cavities with the aluminium case removed, and a Taylor resonator enclosed in an aluminium cone (McCulloch's two objections);
4. an asymmetric fibre-optic loop run outside the vacuum chamber (McCulloch's third objection).

None gave thrust above balance noise. Except for the superconducting cavity, every limit is below the photon thrust P/c for the power used. The laser devices gave exactly the classical photon thrust (S = 1), against QI predictions 39–3300 times larger.

## Key claims
- **Balance (Sect. 2, p. 584):** inverted, counterbalanced double pendulum read by an attocube IDS3010 interferometer. It detects a 0.5 W laser (1.67 nN) at a thrust-to-noise ratio of 10 and carries thrusters up to 10 kg. Calibration factor "usually in the range of 1 μN/μm". The chamber (0.9 m × 1.5 m, own concrete foundation) reaches about 10⁻⁷ mbar at best. Laser tests ran at 10⁻⁶ mbar, the spherical EMDrive at 10⁻² mbar.
- **Spherical EMDrive (Sect. 3, pp. 585–586):** same cavity as before, with a spherical large end-cap and the HDPE dielectric removed, following Shawyer's suggestions. On-board battery pack; liquid-metal feedthroughs only for data. Four resonances (Table 1): 1918 MHz (Q 113, hybrid), 1945 MHz (Q 486, TM210), 2030 MHz (Q 677, TE113), 2054 MHz (Q 1027, TM020). "Each thrust measurement at either of the resonance frequencies resulted in balance noise only." A ±10 µN "preload" (Shawyer's claimed requirement) applied with the voice coil made no difference.
- **Superconducting EMDrive (Sect. 4, pp. 586–588):** copper cylinder (160 mm diameter, 210 mm long) with YBCO-on-sapphire end plates (T_c = 92 K) in a polystyrene LN₂ reservoir on the balance. The feed antenna was mounted off the balance, without contact, so the RF electronics stayed outside the chamber. Nitrogen was solidified by pumping to 10⁻¹ mbar, which removes boiling and sloshing and lowers the temperature by a further 15 K; each filling gave about 30 min of measurement.
  - With a 40 mm HDPE disc, no extra superconducting resonances appeared. A signal at 1843 MHz was the same above and below T_c and did not reverse when the device was turned 180°, so it is "a measurement artefact and does not represent any real force".
  - Without HDPE, narrow superconducting resonances appeared at 1819 MHz (Q 2600) and 1959 MHz (Q 2063), only below T_c. At 20 W commanded power, no thrust above noise.
- **Laser-type EMDrives and QI (Sect. 5, pp. 588–591):** the paper describes QI's modified inertial mass (Eq. 1) and the QI laser prediction F = PS/c with S the number of reflections. It responds to McCulloch's April 2021 blog post (ref. [4]):
  - *Aluminium plate:* "According to McCulloch, the resonators should have never been able to generate thrust due to an aluminium plate being present that supposedly prevents Unruh radiation to interact as intended" (p. 589). The plate had been a shield against stray laser light. It was removed and the three silver-plated cavities (reflectivity 97.5%, S = 39) retested.
  - *Asymmetric metal cavity:* McCulloch said the Taylor beam "requires an asymmetric metal cavity surrounding the laser beam". An aluminium cone plus end-cap fully enclosed the Taylor-Light beam path (p. 589).
  - *Vacuum chamber:* McCulloch "suggested that the vacuum chamber itself was responsible for the non-existent thrust", its conductive walls cancelling Unruh radiation (p. 590). The balance was moved onto a marble table in the lab, where "in front of and behind the fiber-optic coil there were no metallic objects in at least 80 m distance". The loop was 2.2 km of multimode fibre on a PEEK former (radii 70 mm and 40 mm, centres 150 mm apart), S up to 3300, with an 830 nm, 1 W laser and battery on the balance. Three Unruh-shield positions were tested: none, small radius, big radius.
- **Conclusion (p. 591):** "None of the enhancements in any laser resonator setup revealed anomalous thrust. All measurements stayed within the thrust limit of classical forces due to radiation pressure (S = 1) for the given amount of power." "Neither the microwave- and superconducting cavities nor the infrared laser resonators passed our requirements for a breakthrough in space propulsion."
- **Funding (p. 591):** DLR/BMWi (50RS1704) and **DARPA DSO award HR001118C0125**, the award that funded McCulloch's QI programme.

## Key equations
QI modified inertia as quoted by the authors (Eq. 1; Θ = diameter of the observable universe):
$$ m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) $$
Photon thrust (Eq. 2), simplified QI laser prediction with force-amplification (reflection) factor S (Eq. 3), and the microwave-cavity prediction with loaded Q (Table B1/B2):
$$ F_{\rm Photon} = \frac{P}{c}, \qquad F_{QI} = \frac{PS}{c}, \qquad F_{\rm pred} = \frac{PQ}{c} $$

## Data used
- Thrust-balance profiles, each an average of repeated runs with drift removal in LabVIEW. Voice-coil calibration before every series. The fibre loop was measured in air outside the chamber. Laser power was measured before each resonator with a Coherent LaserCheck meter; for the fibre loop the average of input and output power was used.

## Results & predictions
All values from Appendix B (pp. 594–595). Error bars are the standard deviation of repeated runs.

**Table B1, spherical EMDrive**

| Resonance | Q_loaded | Power in cavity | Photon thrust (P/c) | Prediction (PQ/c) | Measured |
|---|---|---|---|---|---|
| 1918 MHz | 113 | 6 W | 20 nN | 2261 nN | (13 ± 31) nN |
| 1945 MHz | 486 | 4.2 W | 14 nN | 6808 nN | (−7 ± 18) nN |
| 2030 MHz | 677 | 10 W | 33 nN | 22582 nN | (−4 ± 38) nN |
| 2054 MHz | 1027 | 5.5 W | 18 nN | 18841 nN | (−11 ± 25) nN |

**Table B2, superconducting EMDrive (no HDPE)**

| Resonance | Q_loaded | Superconducting? | Power | Prediction (PQ/c) | Measured |
|---|---|---|---|---|---|
| 1819 MHz | 2599 | yes | 19 W | 164 µN | (0.14 ± 0.23) µN |
| 1819 MHz | – | no | – | – | (0.05 ± 0.24) µN |
| 1959 MHz | 2063 | yes | 18 W | 156 µN | (−0.33 ± 0.54) µN |
| 1959 MHz | – | no | – | – | (0.07 ± 0.08) µN |

**Table B3, silver-plated laser cavities (aluminium case removed; S = 39)**

| Set-up | Power | QI prediction (PS/c) | Photon thrust | Measured |
|---|---|---|---|---|
| Beam trap (reference) | 279 / 467 mW | – | 0.93 / 1.56 nN | (0.91 ± 0.31) / (1.51 ± 0.15) nN |
| CC/CX | 467 mW | 60 nN | 1.56 nN | (1.52 ± 0.41) nN |
| CC/CC | 279 / 467 mW | 36 / 60 nN | 0.93 / 1.56 nN | (1.04 ± 0.12) / (1.65 ± 0.14) nN |
| Circle | 279 / 467 mW | 36 / 60 nN | 0.93 / 1.56 nN | (0.89 ± 0.14) / (1.50 ± 0.17) nN |

**Table B4, Taylor-Light resonator in a tapered aluminium cavity**

| Power | QI prediction | Photon thrust | Measured |
|---|---|---|---|
| 289 mW | 482 nN | 0.96 nN | (1.01 ± 0.30) nN |
| 493 mW | 822 nN | 1.64 nN | (1.62 ± 0.26) nN |

**Table B5, fibre-optic loop in air outside the chamber (S = 3300)**

| Shield | Avg. power | QI prediction | Measured |
|---|---|---|---|
| none | 31 / 203 mW | 0.34 / 2.23 µN | (0.02 ± 0.26) / (0.05 ± 0.30) µN |
| small radius | 31 / 203 mW | > 0.34 / > 2.23 µN | (0.01 ± 0.19) / (0.09 ± 0.18) µN |
| big radius | 31 / 203 mW | > 0.34 / > 2.23 µN | (0.02 ± 0.15) / (0.06 ± 0.16) µN |

- The paper says the loop measurement, even in air, had a resolution "below the predicted thrust values with worst-case assumptions by a factor of 14" (p. 591).
- **Editorial checks:**
  - Table B1 predictions follow from PQ/c (e.g. 10 W × 677 / c ≈ 22.6 µN). The text's "up to 22.5 μN" (p. 586) is the 2030 MHz row.
  - Table B2: 19 W × 2599 / c ≈ 165 µN matches the 1819 MHz entry. For 1959 MHz, 18 W × 2063 / c ≈ 124 µN, not the printed 156 µN; 156 µN corresponds to Q ≈ 2600. This looks like a slip in the table. Either way the ±0.54 µN uncertainty is about 230–300 times smaller than the prediction.
  - Table B4: 482 nN at 289 mW implies S ≈ 500, although the text says the Taylor resonators "reached up to 1000 internal reflections" (p. 589).
  - Table B3: S = 39 from 97.5% reflectivity is consistent with S ≈ 1/(1 − R) = 40.
- **Differences from the IAC-21 version used earlier:** the journal section on the fibre-loop results is Sect. 5.6 (the IAC paper numbered it 5.5); the result tables are in Appendix B; the superconducting measurements were at −202 °C (1819 MHz) and −196 °C (1959 MHz) per the figure captions, with 65 K given as the balance's cryogenic capability (abstract, Conclusions); and the cryogenic runs were at 10⁻¹ mbar, not "about 10¹ mbar" as this entry previously said. The earlier entry's prediction range "2261–6808 nN" for the spherical EMDrive was incomplete; the full range is 2261–22582 nN.

## Figures
*Figure (local only): Figs. 13–14 — The illuminated silver CC/CX cavity on the balance, and a thrust measurement at 467 mW with the aluminium case removed: pure photon thrust. (PDF p. 7.)*

*Figure (local only): Figs. 16–18 — Taylor set-up thrust at 493 mW inside the tapered aluminium cone (photon thrust only), the proposed QI thrust principle for an asymmetric fibre loop with an "Unruh shield", and the loop on a marble table outside the vacuum chamber. (PDF p. 8.)*

*Figure (local only): Figs. 19–20 — Fibre-optic loop thrust outside the vacuum chamber at 203 mW average power with the Unruh shield at the small and at the big radius: balance noise only. The page also carries the Conclusions. (PDF p. 9.)*

## Notable quotes
> "The only setup change of removing the aluminium plate did not have any effect on measured thrust whatsoever." (Sect. 5.2, p. 589)

> "The vacuum chamber did not hide the proposed QI effects." (Sect. 5.6, p. 591)

> "Despite the enhancements made to each device, we did not detect any evidence in favour of the proposed theories." (abstract, p. 583)

## Criticisms & responses
- **This paper is itself a response to McCulloch's critique** of the 2021 laser tests ([blog, 27 Apr 2021](https://physicsfromtheedge.blogspot.com/2021/04/response-to-tajmars-new-cavity-results.html), the paper's ref. [4]). Each of the three objections is answered with a modified set-up (aluminium case, metal enclosure for the Taylor beam, chamber walls). See [2022-neunzig-laser-resonators](../2022-neunzig-laser-resonators/README.md) for the full exchange. Shawyer's objections ("Notes on the Recent Dresden TU Paper", ref. [3]) are answered by the spherical end-cap, the removed dielectric, the preload test and the superconducting cavity.
- **McCulloch's reaction (blog, 23 Jan 2022).** He cites this work as "Neunzig, O., M. Weikert and M. Tajmar, 2021. Thrust measurements of microwave-, superconducting and laser type emdrives. 72nd IAC, Dubai." He changed the interpretation rather than the experiment. Light-based QI thrusters "did not perform well", whereas electron-based (capacitor) thrusters did. He traces this to his earlier assumption that v = c. With the correct speed, he says, QI "accounts for the effectively zero thrusts seen by Tajmar's team for the laser cavities". He also says QI "still predicts the emdrive", now via Unruh waves seen by electrons in the cavity walls, and that "QI has not been falsified" ([blog](https://physicsfromtheedge.blogspot.com/2022/01/learning-from-experiments.html)). The journal paper (submitted Dec 2021) does not discuss this revision.
  > [!UNVERIFIED] Whether McCulloch published a quantitative revised prediction for the Dresden laser or EMDrive configurations.
  - Editorial note: the QI predictions in this paper's tables are the simplified F = PS/c with no geometric factors (p. 588). The paper does not claim they are the only possible QI predictions; it tests the formula as used in the earlier QI laser-cavity proposals.
- **Remaining issue for EMDrive proponents (factual):** the microwave cavity's loaded Q values (113–1027, and up to about 2600 superconducting) are lower than the Q values Shawyer and NASA reported (thousands to tens of thousands). Proponents have cited such Q gaps as a reason for null results. The superconducting test was meant to raise Q; with the HDPE disc it gave no superconducting resonances at all (p. 587). The measured limits still sit 2–3 orders of magnitude below PQ/c at the Q values achieved.
- **Limits of the superconducting test (stated by the authors):** the cavity could not be hung from a single suspension point; evaporating nitrogen adds cold-gas thrust and noise; and the balance calibration drifts as nitrogen mass is lost (pp. 587–588). The resulting noise (0.08–0.54 µN) is above photon thrust, which is why the abstract excludes this device from the "below photon pressure" statement.

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2022-neunzig-laser-resonators](../2022-neunzig-laser-resonators/README.md), [2021-tajmar-emdrive-false-positive](../2021-tajmar-emdrive-false-positive/README.md), [2017-taylor-laser-resonators](../../01-papers/2017-taylor-laser-resonators/README.md), [2015-mcculloch-emdrive-pip](../../01-papers/2015-mcculloch-emdrive-pip/README.md), [2017-mcculloch-emdrives-dielectrics](../../01-papers/2017-mcculloch-emdrives-dielectrics/README.md), [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md), [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md), [2019-kossling-spacedrive-balance](../../04-experiments/2019-kossling-spacedrive-balance/README.md)
