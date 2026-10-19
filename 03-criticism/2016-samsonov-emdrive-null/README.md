---
title: "Null Result for Prediction of Asymmetrical Anomalous Force from Frustum-shaped RF Resonant Cavity"
authors: [Eugene Samsonov]
year: 2016
type: experiment-report
venue: "viXra:1603.0153"
doi:
arxiv:
url: "https://vixra.org/abs/1603.0153"
open_access: true
license: unknown
files: [paper.pdf, figures/fig-7-8-low-noise-and-thermal.png]
status: critical
tags: [emdrive, amateur, indirect, null-result, pendulum, not-peer-reviewed]
---

# Null Result for Prediction of Asymmetrical Anomalous Force from Frustum-shaped RF Resonant Cavity

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`unknown`) does not permit redistribution. Read the paper at [source](https://vixra.org/abs/1603.0153).

**Citation:** Samsonov, E. (2016). *Null Result for Prediction of Asymmetrical Anomalous Force from Frustum-shaped RF Resonant Cavity*. viXra:1603.0153 (manuscript dated Feb 2016). https://vixra.org/abs/1603.0153. The stored PDF is viXra v1 (11 pages). The paper is not peer-reviewed.

**TL;DR:** An amateur experiment funded by the author, a software engineer who notes the work is not endorsed by his employer. A copper frustum ("EmDrive") with a TE012 mode near 2.3 GHz was driven with about 30 W of RF. It was battery-powered and wirelessly controlled, on a 4 kg platform hanging from a 3 m tungsten wire. The predicted force from **Shawyer's** theory was 600+ µN. No RF-correlated force was seen. Electrostatic test pulses as small as 160 µN were clearly detected, and the quietest run limits any anomalous force to below about 40 µN. Spurious forces of thermal origin, from hot-air convection and possibly laser-sensor refraction, were observed. McCulloch's QI EmDrive paper is cited only as one of the "controversial theories". No QI-specific prediction is computed.

## Key claims
- The test targets Shawyer (2008), whose predicted forces of a few hundred µN from 30 W were large enough for a simple pendulum. McCulloch (2015, Progress in Physics) is cited alongside Shawyer as an attempt to explain the phenomenon.
- **Set-up:** acrylic platform on 0.28 mm tungsten wire. On board: cavity, RF amplifier, programmable RF generator, LiPo battery and XBee wireless link, with "no physical wires of any kind" crossing to the base. A Keyence LK-2001 laser displacement sensor (1 µm resolution) gives a scale factor of 13 µN/µm. Electrostatic plates at 1 kV supply calibration pulses and computer-controlled damping.
- **Cavity:** COMSOL-designed. Simulated unloaded Q ≈ 75,000. The as-built (crude) cavity had a loaded Q of about 3,100.
  - First build: TE012 at 2,308 MHz, below the small-end cut-off frequency (2,313 MHz) required by Shawyer's theory, so the predicted thrust was 0.
  - Second build: 8 mm cut from the small end, giving 2,331 MHz, 75 MHz above the 2,256 MHz cut-off, Q ≈ 2,300 and a predicted thrust of 640 µN.
- **Protocol:** more than 50 runs of 60–80 s with RF pulses, high-voltage test pulses or both. Delivered RF was at least 27.5 W, typically 29.0–29.7 W. A 50 Ω dummy load served as control.
- **Conclusion:** "The corresponding theoretical approach has thus been wholly or partially falsified."

## Key equations
The PDF text layer does not preserve the pendulum equations (1)–(2) legibly. The paper describes them as the standard small-angle result: the shift x₀ of the oscillation mid-point is proportional to a small horizontal force F′, with scale factor mg/L ≈ 13 µN/µm for m = 4 kg and L = 3 m.
> [!UNVERIFIED] Exact typeset form of Eqs. (1)–(2); not reproduced here.

## Data used
- Laser-displacement time series sampled at 100 Hz. Mid-points of each oscillation cycle were extracted to detect steady forces.

## Results & predictions
- Predicted Shawyer thrust at 30 W: 950 µN (first cavity, nominally 0 because it violates the cut-off condition) and 640 µN (modified cavity).
- Detection threshold demonstrated: 160 µN electrostatic pulses "easily detected".
- Upper limit from the quietest runs: any anomalous force "must be under ~40 µN", more than an order of magnitude below prediction (p. 8).
- Spurious forces were typically under 200 µN and uncorrelated with RF. One thermal force did correlate: the amplifier's aluminium heat spreader reached 60–80 °C. It began mid-pulse, often reversed after a few seconds, persisted after the pulse, appeared with the dummy load too, and depended on frustum orientation. The author attributes it to (1) a convective "chimney" effect and (2) a change in air refractive index affecting the laser triangulation sensor, worth an estimated 26–390 µN.

## Figures
*Figure (local only): Figs. 7 & 8 — Fig. 7: a low-noise run in which an electrostatic test pulse overlaps the RF pulse; only the electrostatic force appears, setting the ~40 µN upper limit. Fig. 8: spurious thermal forces whose sign/magnitude depend on frustum orientation. (Rendered page 8 of the viXra PDF.)*

## Notable quotes
> "No force resulting from the application of RF energy has been detected within the resolution of the experimental setup. Spurious forces of thermal origin have been observed." (p. 1, abstract)

> "any anomalous force, if present, must be under ~40 µN which is more than an order of magnitude below the predicted value." (p. 8)

> "However, there is hardly anything anomalous about the origin of this force." (p. 10)

## Criticisms & responses
- **No McCulloch response found.** A search of physicsfromtheedge.blogspot.com for "Samsonov" returned no relevant post (Oct 2026). McCulloch's EmDrive comparisons in 2016–2018 plot predicted against observed thrust for Shawyer, Cannae, NASA, Tajmar and others. They do not include this test ([blog, 28 Nov 2016](https://physicsfromtheedge.blogspot.com/2016/11/emdrives-dielectrics-nasa-shift.html); [blog, 24 May 2018](https://physicsfromtheedge.blogspot.com/2018/05/emdrive-trial-by-media.html)).
- **Relevance to QI is indirect.** The prediction tested is Shawyer's. McCulloch's QI EmDrive formula ([2015-mcculloch-emdrive-pip](../../01-papers/2015-mcculloch-emdrive-pip/README.md), [2015-mcculloch-emdrive-epl](../../01-papers/2015-mcculloch-emdrive-epl/README.md)) also scales with power × Q and cavity geometry. In its 2015 form, McCulloch interprets Q as the number of round trips; see the Dresden discussion in [2022-neunzig-laser-resonators](../2022-neunzig-laser-resonators/README.md). Nobody has computed what that formula predicts for this cavity.
  > [!UNVERIFIED] QI-predicted thrust for this cavity; not computed in the source or found elsewhere.
- **Limitations (factual):** The test was in air, not vacuum. It is a single-author, non-peer-reviewed report on viXra. The author thanks the NASASpaceflight.com "EMDrive Developments" forum for feedback during the experiment.

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2015-mcculloch-emdrive-pip](../../01-papers/2015-mcculloch-emdrive-pip/README.md), [2015-mcculloch-emdrive-epl](../../01-papers/2015-mcculloch-emdrive-epl/README.md), [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md), [2021-tajmar-emdrive-false-positive](../2021-tajmar-emdrive-false-positive/README.md), [2019-kossling-spacedrive-balance](../../04-experiments/2019-kossling-spacedrive-balance/README.md)
