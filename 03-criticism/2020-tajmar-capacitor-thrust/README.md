---
title: "Put strong limits on all proposed theories so far assessing electrostatic propulsion: Does a charged high-voltage capacitor produce thrust?"
authors: [Martin Tajmar, Tom Schreiber]
year: 2020
type: experiment-report
venue: "Journal of Electrostatics 107:103477"
doi: 10.1016/j.elstat.2020.103477
arxiv:
url: "https://doi.org/10.1016/j.elstat.2020.103477"
open_access: false
files: []
status: critical
tags: [capacitor, electrostatic, tu-dresden, indirect, null-result, biefeld-brown, lab-test]
---

# Put strong limits on all proposed theories so far assessing electrostatic propulsion: Does a charged high-voltage capacitor produce thrust?

**Citation:** Tajmar, M. & Schreiber, T. (2020). *Put strong limits on all proposed theories so far assessing electrostatic propulsion: Does a charged high-voltage capacitor produce thrust?* Journal of Electrostatics, 107, 103477. https://doi.org/10.1016/j.elstat.2020.103477.

The journal version is paywalled, so no PDF is stored. This summary is based on the authors' manuscript hosted by TU Dresden ([PDF](https://tu-dresden.de/ing/maschinenwesen/ilr/rfs/ressourcen/dateien/forschung/folder-2007-08-21-5231434330/ag_raumfahrtantriebe/Paper-Assessing-Electrostatic-Propulsion-Final.pdf), 23 pp., headed "Journal of Electrostatics 107 (2020) 103477"), read but not stored, and on the published abstract. Page numbers refer to that manuscript.

**TL;DR:** TU Dresden built a capacitor weight-change set-up that removes high-voltage artefacts. A Sartorius balance (0.1 mg) holds a hanging mu-metal/Faraday box containing an on-board 10 kV supply and a rotation rig, fed only through low-voltage Galinstan liquid-metal contacts. Accuracy is ±0.3 mg (3σ). They tested symmetric ceramic and Teflon capacitors, an asymmetric wire-plate Teflon capacitor, a half-wax-filled spherical capacitor, and a leakage-current (field-emission) capacitor that replicates the **Becker & Bhatt** claim QI was invoked for. No force was found in any configuration. The Bhatt/Becker claim is "ruled out by an order of magnitude". The authors add that replication uncertainties mean the result "may not completely rule out the claim" and that it should be re-checked at higher resolution.

## Key claims
- Historical framing: the Biefeld-Brown effect in air is explained by corona/ion wind (Tajmar 2004). Some later claims say a residual, purely electrostatic force tied to the dielectric exists. These claims lack set-ups that rule out conventional explanations (pp. 1–2).
- **Models tested (Sect. 2):**
  - Ivanov (and the related Musha and Zhu models), Eq. 1.
  - Porcelli & dos Santos Filho, Eqs. 2–3.
  - Minotti's version of the Mbelek–Lachièze-Rey scalar-tensor theory, Eqs. 4–5. The authors correct a missing ε_r⁻² factor.
  - The "discharge through a thin dielectric sheet" claim of [Bhatt & Becker (2018)](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), "predicted by a modified inertia model based on Unruh radiation forming a so-called Rindler horizon" (citing McCulloch 2010, *Minimum accelerations from quantised inertia*). Because "no actual force model is shown", the authors digitise Bhatt & Becker's force-versus-power data and fit an empirical law (Eq. 6, R² = 0.9996).
- **Artefacts identified (Sect. 3):** corona wind from thin or poorly insulated cables and joints; high-voltage-induced wire bending and centre-of-mass shifts; buoyancy from supply heating (1 °C in a 10 × 10 × 10 cm³ box ≈ 4 mg); and electromagnetic interaction with the environment. Null tests with an EMCO V1G high-voltage resistor in place of a capacitor stay within ±0.1 mg, with one 0.3 mg peak at 10 kV.
- **Overall answer:** "Can we answer the question if a charged high-voltage capacitor produces thrust? So far, our answer must be: No – within our measurement accuracy." Ivanov and Bhatt are singled out as "worth to be pursued with better setups in the future" (Conclusion).

## Key equations
Ivanov's force for a parallel-plate capacitor (Eq. 1):
$$ F_{\rm Ivanov} = \sqrt{G\varepsilon_0\varepsilon_r}\cdot\frac{m}{d}\cdot V $$
Porcelli & dos Santos Filho, symmetric case (Eq. 2):
$$ F_{\rm Porcelli} = \frac{0.102}{16\pi^2}\,\frac{\varepsilon_r - 1}{\varepsilon_r + 2}\,\varepsilon_0 A E^2 $$
Minotti, parallel-plate form (Eq. 5), with Γ = 3.35 × 10⁻¹² (units as given in the paper):
$$ F_{\rm Minotti} = -\frac{\Gamma A \rho V^2}{2\varepsilon_r^2} $$
Empirical fit to Bhatt & Becker's data (Eq. 6; P in mW, d in µm, F in µN):
$$ F_{\rm Bhatt} = P\cdot\left(2.7 + 114.8\,e^{-d/16.9} + 2679\,e^{-d/3.6}\right) $$

## Data used
- Laboratory weight-change profiles: 60 s on and 60 s off, averaged over 5–20 profiles, sampled at 1 Hz, with linear drift removal from the off-periods. Voice-coil calibration at 0.758 µN/µA gave a 92% balance response to the commanded force.

## Results & predictions
| Test | Prediction (mass-equivalent) | Measured |
|---|---|---|
| Symmetric ceramic (2 × Murata DHRB34A102MF1B, ε_r ≈ 4500), 10 kV | Ivanov 2.4 mg | < 0.3 mg at all orientations |
| Symmetric Teflon (ε_r = 2.1), 10 kV | Porcelli 118.8 mg; Minotti 11.8 mg | < 0.3 mg |
| Asymmetric wire-plate Teflon | Porcelli 29.7 kg | < 0.3 mg |
| Spherical, half-filled with bee wax (315 g) | Minotti 24.4 mg (7.5 mg with ε_r⁻² correction) | < 0.3 mg |
| Leakage-current capacitor (90 µm PE, needle-perforated Al-foil cathode, about 10 µA, discharge at 2.1–4 kV) | Bhatt (Eq. 6) 6.8 mg | < 0.3 mg |

- Porcelli is ruled out by close to three orders of magnitude, Minotti by two, and Ivanov by one ("quite close to our resolution").
- **Bhatt & Becker caveats (manuscript p. 8):** the discharge voltage was 2.1 kV rather than 5 kV; the dielectric was 90 µm rather than 13–80 µm; and the distance to conductive surroundings may differ from Bhatt & Becker's, which matters because Bhatt & Becker reported "force blocking" by nearby conductors. Hence "our null result is important for comparison with a clean setup although it may not completely rule out the claim due to the exact replica uncertainties."

## Figures
No PDF stored, so no figures are reproduced. The manuscript's Fig. 2 shows the set-up and Fig. 12 the leakage-current results.

## Notable quotes
> "No force was detected for a variety of configurations ruling out most theories by many orders of magnitude." (abstract)

> "the force claim from Bhatt and Becker [15] on leakage current capacitors is ruled out by an order of magnitude, but also here, the actual experimental configuration leaves enough uncertainty that this should be re-checked with a higher resolution." (Conclusion, manuscript p. 8)

## Criticisms & responses
- **McCulloch's position (blog):** No post directly addressing this paper was found (searches for "Schreiber" and "Tajmar" in Oct 2026). McCulloch continued to cite the Becker & Bhatt capacitor results as QI's strongest laboratory support:
  - 23 Jan 2022: "QI predicts the capacitor results perfectly (top right): results now seen in two labs" ([blog](https://physicsfromtheedge.blogspot.com/2022/01/learning-from-experiments.html)).
  - 2 Nov 2021: Richard Mansell of IVO Ltd "tried it with an analogue method and agreed with them" ([blog](https://physicsfromtheedge.blogspot.com/2021/11/a-thrust-from-nothing.html)).
  - 4 Aug 2022: describes his own capacitor tests with R. Arundal ([blog](https://physicsfromtheedge.blogspot.com/2022/08/glimpses-of-qi-in-lab.html)).

  These are McCulloch's claims. The IVO and Plymouth measurements were not located as peer-reviewed publications for this entry.
- McCulloch's QI capacitor force model, F = 0.00014 IA/d², appeared later in [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md). This paper therefore compares against an empirical fit, not a QI prediction.
- Subsequent space test: IVO Ltd's QI-capacitor thruster flight in 2023–24. See [2023-debrief-ivo-launch](../../07-media/2023-debrief-ivo-launch/README.md), [2024-debrief-ivo-failure](../../07-media/2024-debrief-ivo-failure/README.md) and [2024-futurism-ivo-contact-lost](../../07-media/2024-futurism-ivo-contact-lost/README.md).

## Related
- Evidence: [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md)
- Sources: [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md), [2010-mcculloch-minimum-accelerations](../../01-papers/2010-mcculloch-minimum-accelerations/README.md), [2018-mcculloch-propellantless-propulsion](../../01-papers/2018-mcculloch-propellantless-propulsion/README.md), [2018-tajmar-spacedrive](../../04-experiments/2018-tajmar-spacedrive/README.md), [2022-neunzig-laser-resonators](../2022-neunzig-laser-resonators/README.md)
