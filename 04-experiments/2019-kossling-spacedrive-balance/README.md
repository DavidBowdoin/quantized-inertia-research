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
license: accepted-manuscript
files: [paper.pdf, figures/fig-1-noise-calibration.png, figures/fig-2-met-orientations.png, figures/fig-3-emdrive.png]
status: critical
tags: [emdrive, mach-effect, tu-dresden, thrust-balance, thermal-drift, null-result]
---

# The SpaceDrive project - Thrust balance development and new measurements of the Mach-Effect and EMDrive Thrusters

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`accepted-manuscript`) does not permit redistribution. Read the paper at [doi:10.1016/j.actaastro.2019.05.020](https://doi.org/10.1016/j.actaastro.2019.05.020).

**Citation:** Kößling, M., Monette, M., Weikert, M. & Tajmar, M. (2019). *The SpaceDrive project – Thrust balance development and new measurements of the Mach-Effect and EMDrive Thrusters*. Acta Astronautica, 161, 139–152. https://doi.org/10.1016/j.actaastro.2019.05.020. Received 13 Dec 2018, revised 8 May 2019, accepted 13 May 2019.

**Stored version: the Elsevier ACCEPTED MANUSCRIPT, not the typeset journal article.** 22 PDF pages: an Elsevier cover sheet (PDF p. 1), the paper paginated "Page 1 of 20" to "Page 20 of 20" (PDF pp. 2–21), and a highlights page (PDF p. 22). The manuscript still carries the IAC-18 header (69th IAC, Bremen, 1–5 Oct 2018, IAC-18,C4,7-C3.5,5,x46021; "Copyright ©2018 by the International Astronautical Federation (IAF)"). Supplied by the archive owner and kept local only. **Page numbers below are manuscript pages ("ms. p. N of 20").** The manuscript is a revised text, not identical to the 16-page IAC-18 conference paper used earlier for this entry (see Criticisms).

**TL;DR:** The paper describes an automated torsion balance for devices up to 10 kg. The abstract claims a capability of measuring 100 nN; a 140-profile noise run gave σ = 11 nN. With it the team tested Woodward's Mach-Effect Thruster (MET), their own MET, a magnetostrictive transducer and an EMDrive (Aug–Sep 2018). **Settling the earlier discrepancy:** the accepted manuscript agrees with the journal abstract ("no final conclusions can be drawn"). It does **not** contain the IAC-18 sentence "only thermal drifts and no real thrust". For the EMDrive it says the measurements "seem to indicate the presence of thermal drifts" but that, without reverse and 90° runs, "there can be no definite conclusions". For Woodward's MET a force remained after subtracting the 90° run (SNR 14 at 0°, 3 at 180°); the authors conclude there is no "clear unidirectional thrust of the magnitude claimed by Woodward" and call for better resolution. QI is cited (McCulloch 2015, Progress in Physics) only among EMDrive "new concepts".

## Key claims
- **Targets (Sect. 2.1, ms. p. 2):** claimed forces are "sub-µN up to 2 µN" for the MET [3, 4] and "up to 90 µN" for the EMDrive [2, White et al. 2017]. An SNR of 10 therefore needs at least 200 nN resolution. All tests here were at 10⁻² mbar (the balance is designed for 10⁻⁶ mbar).
- **Balance (Sect. 2.2, ms. pp. 2–3):** attocube IDS3010 interferometer (1 pm resolution, 2 nm noise at room temperature); two C-Flex E-20 pivots (k = 3.344 mN·m/°); four coaxial Galinstan liquid contacts plus a 30 kV high-voltage contact and a Galinstan RF feedthrough (4 dB reflection loss) so the EMDrive amplifier can stay outside the chamber; eddy-current damping (damping ratio 0.43); motorised tilt control; 0.5 mm mu-metal shielding of thruster box, electronics box and arm; motorised rotation of the experiment box; infrared serial link and LabJack T7.
- **Drift removal (Sect. 2.3.2, ms. pp. 3–4):** method 1 removes a linear fit to sector 1 (before power-on); method 2 joins linear fits to sectors 1 and 5 (after power-off) to remove thermal drift "to some extent".
- **Calibration (Sect. 2.3.4, ms. p. 4):** seven voice-coil steps from −12 to +12 µN gave K = 6.7 µN/µm. 200 overnight 1 µN pulses of 60 s read 0.9 µN, "a 10% discrepancy which still needs to be optimized (long term drift)". 80 pulses of 25 s read only 0.8 µN, because the balance does not reach steady state. Below 30 s an impulse can still be detected "with 80% accuracy".
- **Noise (Sect. 2.3.5, ms. p. 4):** 140 averaged profiles gave a standard deviation of 11 nN, so "a reasonable SNR of > 100 is expected if a thrust of 2 µN is to be measured".
- **Woodward MET (Sect. 3.3, ms. pp. 5–6):** all at the 31 kHz mechanical resonance; 140 overnight runs per orientation.
  - Single sine with a 6:1 transformer at 140 V: 0° peak 2.2 µN at 0.86 A (balance noise 0.2 µN); 180° peak 1.2 µN at 0.46 A; 90° (no thrust expected) 0.6 µN at 0.81 A. The authors subtract the 90° value from both: "This leads to a force of -2.8 µN for 0° and 0.6 µN for 180°. This would mean 180° shows 4.7 times less force with half the power."
  - Mixed ω + 2ω signal at 37 V: a small signal that flips between 0° and 180° but is "more or less present in the 90° orientation"; "The low SNR ... allows no conclusion". Woodward's theory predicts an increase "by orders of magnitude", which "cannot be seen".
  - On a 250 g copper heat sink, bridge mode at 180 V: "no thrust is now observed".
- **TUD-built MET (ms. p. 6):** "no force below 100 nN" up to 180 V at 36 kHz, and none at the second resonance (72 kHz), although theory says thrust scales as ω⁴.
- **Magnetostrictive transducer (Etrema CU18A; Sect. 4, ms. pp. 6–7):** single-sine on/off transients of about 0.3 µN that did not reverse with orientation; a 26 Ω resistor drawing the same current reproduced the behaviour, so "any force observed during magnetostrictor tests are likely due to electromagnetic interactions on the balance". Conclusion: it "did not show any thrust. This seems to indicate that the theory developed by Woodward does not apply to this device."
- **EMDrive (Sect. 5, ms. pp. 7–8):** copper frustum close to NASA's geometry, 4 cm HDPE disc (NASA used 5.4 cm), amplifier (EMPower 1164, 47 dB, 50 W) outside the chamber; three-stub tuner, power meters and cavity inside the mu-metal box; automatic resonance tracking; 60 s pulses.
  - 1933 MHz, flat end-caps with HDPE: 55 profiles, 3.4 µN with sector-1 drift removed. "However, the force response does not show a clear impulsive behavior, especially when compared to the voice coil calibration". The power and force "are similar to the values reported by March (4.7 µN for 3.2 W)".
  - 1920 MHz, flat end-caps without HDPE: "the same behavior".
  - 2576 MHz, spherical end-caps without HDPE: 3.0 µN.
  - "it seems that the observed force follows the trend of the temperature measured on the cavity. Since 180° and 90° measurements are missing, there can be no definite conclusions based on these." Power delivered to the cavity was below the commanded power because of RF losses that depended on the feedthrough, cable and shield positions (ms. p. 8).
- **Overall conclusion (Sect. 6, ms. pp. 8–9):** "The measurements do not show a clear unidirectional thrust of the magnitude claimed by Woodward. Although the measurement for one orientation of the transformer configuration shows a force with a SNR of 14, all other configurations have a lower SNR (< 5). These results indicate the need for better measurement resolution and more systematic and rigorous testing." For the EMDrive, "preliminary tests still seem to indicate the presence of thermal drifts regardless of the configuration".

## Key equations
Woodward's mass fluctuation in a piezo stack (Eq. 1; ρ₀ = density, E₀ = internal energy) and the resulting time-averaged thrust (Eq. 2), as given in the manuscript:
$$ \delta m(t) = \frac{1}{4\pi G c^2 \rho_0}\,\frac{\partial^2 E_0}{\partial t^2}, \qquad F = \frac{\omega}{2\pi}\int_0^{2\pi/\omega} \delta m(t)\,a(t)\,dt $$

## Data used
- Thrust-balance profiles in vacuum (10⁻² mbar), split into five sectors (before, ramp-up, steady, ramp-down, after), averaged over 55–200 repetitions, with voice-coil calibration before and after each measurement. Temperatures from thermocouples and IR sensors on the devices.

## Results & predictions
| Device / configuration | Claimed or expected | Measured (ms.) | Authors' reading |
|---|---|---|---|
| Woodward MET, sine + transformer, 140 V, 31 kHz | 1–5 µN (Woodward, 200–250 V); 0.2 µN at 100 V (Buldrini) | 0°: 2.2 µN; 180°: 1.2 µN; 90°: 0.6 µN; after subtracting 90°: −2.8 / 0.6 µN | force remains, SNR 14 (0°) and 3 (180°); not a clear unidirectional thrust |
| Woodward MET, mixed signal, 37 V | orders of magnitude more than sine | small, also present at 90° | "allows no conclusion" |
| Woodward MET on heat sink, 180 V | — | no thrust at 0° | force removed |
| TUD MET, 180 V, 36 and 72 kHz | ∝ ω⁴ | < 100 nN | no force |
| Magnetostrictor CU18A | larger than MET | ~0.3 µN transients, not reversing; reproduced by resistor | electromagnetic artefact |
| EMDrive, HDPE, 1933 MHz | March: 4.7 µN at 3.2 W | 3.4 µN | follows cavity temperature; no definite conclusion |
| EMDrive, no HDPE, 1920 MHz | — | "same behavior" | as above |
| EMDrive, spherical caps, 2576 MHz | — | 3.0 µN | as above |

- Editorial reading of Fig. 27 (not stated in the text): the 1920 MHz trace peaks near 4.5 µN at about 4 W, and in all three traces the force keeps rising through the power-on period and decays slowly after switch-off, unlike the step shape of the voice-coil calibration.
- Editorial note: the "−2.8 µN for 0°" after subtracting 0.6 µN from a 2.2 µN peak is as printed; arithmetic on the printed peaks would give 1.6 µN. The sign and magnitude may refer to a different reading of the averaged trace; the manuscript does not explain it.

## Figures
*Figure (local only): Figs. 8–10 — Balance damping for a 20 µN step, the 140-profile noise measurement (σ = 0.011 µN), and voice-coil calibration: 7-step run, displacement fit (6.7 µN/µm), 200 × 1 µN for 60 s and 80 × 1 µN for 25 s. (PDF p. 14.)*

*Figure (local only): Figs. 14–16 — Woodward MET averaged force and current at 0°, 180° and 90° (single mode + transformer, 140 V, 31 kHz), with the mixed-signal (37 V) and heat-sink (180 V) runs. (PDF p. 17.)*

*Figure (local only): Fig. 27 — EMDrive measurements at 0° with sector-1 drift removed: HDPE on flat end-caps at 1933 MHz, flat end-caps at 1920 MHz, spherical end-caps at 2576 MHz; force and power against time. (PDF p. 21.)*

## Notable quotes
> "Results of the tests performed between August and September 2018 are presented, but no final conclusions can be drawn." (abstract, ms. p. 1 of 20)

> "When comparing Figure 7c and Figure 27a, it seems that the observed force follows the trend of the temperature measured on the cavity. Since 180° and 90° measurements are missing, there can be no definite conclusions based on these." (Sect. 5.3, ms. p. 8 of 20)

> "The measurements do not show a clear unidirectional thrust of the magnitude claimed by Woodward." (Sect. 6, ms. p. 9 of 20)

## Criticisms & responses
- **Discrepancy resolved (journal vs conference wording):** an earlier batch summary said the "apparent EMDrive thrust was traced to experimental artefacts", based on the IAC-18 conference paper ("So far, only thermal drifts and no real thrust has been observed in all our measurements"). The accepted manuscript, which is the journal text, does not contain that sentence or the IAC wording that the MET signal "most likely results from non-linear thermal drift". It is more cautious throughout: thermal drift is the leading suspect for the EMDrive ("seem to indicate"), the MET result is called inconclusive, and the authors ask for better resolution. Only the magnetostrictor signal is positively attributed to an artefact (electromagnetic). Reports of this paper should therefore say "inconclusive, thermal drift suspected", not "artefacts identified".
- **Self-identified limitations:** no 180° or 90° EMDrive runs; RF power in the cavity uncertain because of reflected waves; the balance slow for 25 s MET pulses; long-term calibration drift of 10% (ms. pp. 4, 8–9).
- **McCulloch's response:** no post specifically about this paper was found. In May 2018, reacting to the earlier Dresden EMDrive results, he argued that Tajmar did "not yet even have a working emdrive". He cited a QI expectation of 0.19 mN against 0.004 mN observed. He also relayed a comment from Phil Wilson that the cavity "does not have a resonance at 1.865GHz (the frequency he is inputting)" ([blog](https://physicsfromtheedge.blogspot.com/2018/05/emdrive-trial-by-media.html)).
- **Later Dresden work** resolved the EMDrive question with a different balance (inverted counterbalanced double pendulum) and battery power, and reproduced White-like signals as mounting artefacts: [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md).
- Minor: the manuscript's highlights page (PDF p. 22) repeats word for word the highlights of [Tajmar et al. 2018](../2018-tajmar-spacedrive/README.md).

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2018-tajmar-spacedrive](../2018-tajmar-spacedrive/README.md), [2016-white-eagleworks](../2016-white-eagleworks/README.md), [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md), [2015-mcculloch-emdrive-pip](../../01-papers/2015-mcculloch-emdrive-pip/README.md), [2018-mcculloch-propellantless-propulsion](../../01-papers/2018-mcculloch-propellantless-propulsion/README.md)
