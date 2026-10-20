---
title: Testing quantised inertia on emdrives with dielectrics
authors: [Michael E. McCulloch]
year: 2017
type: paper
venue: "EPL (Europhysics Letters) 118(3), 34003"
doi: 10.1209/0295-5075/118/34003
arxiv:
url: "https://doi.org/10.1209/0295-5075/118/34003"
open_access: true
license: CC-BY-3.0
files: [paper.pdf, figures/fig-1-cavity-schematic.png, figures/fig-2-predicted-vs-observed.png]
status: supports
tags: [emdrive, propulsion, lab-test]
---

# Testing quantised inertia on emdrives with dielectrics

**Citation:** McCulloch, M. E. (2017). *Testing quantised inertia on emdrives with dielectrics*. EPL 118(3), 34003 (May 2017 issue; received 23 Jan 2017, accepted 14 June 2017, published online 7 July 2017). https://doi.org/10.1209/0295-5075/118/34003. Open access under CC BY 3.0.

**About the stored PDF:** `paper.pdf` is the published EPL version (6 PDF pages). PDF p. 1 is an IOPscience download cover page; the article itself is pp. 34003-p1 to 34003-p5 (PDF pp. 2–6). The PDF states the CC BY 3.0 licence on p. 34003-p1. Page references below give both the journal page and the PDF page.

**TL;DR:** This updates McCulloch's QI emdrive model ([2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md)). First, it drops the earlier "controversial" assumption that photon speed changes in the cavity: the new derivation keeps the speed of light constant and lets only the photons' (QI-modified) mass change. Second, it treats a dielectric of refractive index n at one end as equivalent to widening the cavity at that end, using m = m_L(1 − λ_U/4nS). With dielectrics included (n = 1.46 for the NASA polyethylene, 6.16 for Shawyer's first test), the predictions match the 11 tabulated thrusts, including three 2016 NASA results, except Shawyer's first test. There the magnitude matches but the predicted direction is reversed. The paper predicts that a dielectric at the *wide* end would boost thrust.

## Key claims
- Emdrives move slightly towards their narrow ends, "in contradiction to standard physics" (abstract, p. 34003-p1).
- QI explains this through photon inertia due to Unruh radiation, more of which is allowed at the wide end. Photons gain inertia going towards the wide end, so the cavity must move towards its narrow end to conserve momentum.
- The previous analysis "predicted a controversial photon acceleration, which is shown here to be unnecessary". It also mispredicted thrust for emdrives with dielectrics, overpredicting the NASA results "by up to a factor of ten" (p. 34003-p3).
- A dielectric at one end reduces the photon speed and hence the Unruh wavelength, so more Unruh waves fit there. This has "the same effect as widening the cavity at that end, producing a thrust away from the end with the dielectric" (p. 34003-p4).
- The cavity walls are assumed to act as a horizon for the Unruh waves (as in the 2015/2016 papers).
- The paper says that "quantised inertia has no adjustable parameters" (p. 34003-p3).
- It admits the model is approximate: microwaves are assumed to travel only along the axis, 3-D resonance is "only crudely modelled", and "a full 3-d model is needed" (p. 34003-p4).
- The conclusion counts nine tests in four independent labs showing anomalous thrust towards the narrow end.
- Suggested tests: change or reverse thrust by altering the cavity aspect ratio (or shortening L / changing the frequency), increasing P or Q, filling the cavity uniformly with dielectric, or (more effectively) adding a dielectric at the wide end. The paper adds that a thrust reversal "may have been seen in recent NASA experiments" (p. 34003-p4).

## Key equations
Transcribed from the PDF (pp. 34003-p1 to -p3, PDF pp. 2–4). Θ is "twice the Hubble distance"; no numerical value is used in this paper.

QI modified inertia (eq. 1), with λ_U ∼ 8c²/a:
$$m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) = m\left(1 - \frac{\lambda_U}{4\Theta}\right) \qquad (1)$$

The earlier (2015/2016) emdrive thrust formula, used for the F₋d column (eq. 2):
$$F = \frac{-6PQL}{c}\left(\frac{1}{L + 4w_b} - \frac{1}{L + 4w_s}\right) \qquad (2)$$

Photon mass in the cavity, with n̄ the average refractive index (eqs. 3–6):
$$m_L = \frac{E}{c^2} = \frac{Pt}{c^2} = \frac{P}{c^2}\times Q \times \frac{L}{c/\bar n} = \frac{PQL\bar n}{c^3} \qquad (3\text{–}6)$$

Momentum conservation with constant light speed (eqs. 7–8):
$$\frac{d}{dt}(m_c v_c + m_L c) = 0 = m_c a_c + m_L\frac{dc}{dt} + c\frac{dm_L}{dt}, \qquad F_c = -c^2\frac{dm_L}{dx} \qquad (7, 8)$$

With a dielectric, m = m_L(1 − λ_U/4nS). As a finite difference between the small (s) and big (b) ends (eq. 9), then using a = 2c²/L so λ_U = 4L (eq. 10):
$$F_c = -c^2 m_L\,\frac{\left(1 - \frac{\lambda_U}{4n_sS_s}\right) - \left(1 - \frac{\lambda_U}{4n_bS_b}\right)}{L}, \qquad F_c = m_L c^2\left(\frac{1}{n_bS_b} - \frac{1}{n_sS_s}\right) \qquad (9, 10)$$

With the average cavity size S ≈ (L + 4w)/6 (eqs. 11–12), and n̄ ≈ 1 because the dielectric fills a tenth or less of the length (eq. 13, used for the F₊d column):
$$F_c = \frac{6PQL}{c}\left(\frac{1}{n_b(L + 4w_b)} - \frac{1}{n_s(L + 4w_s)}\right) \qquad (13)$$

n_{s,b} = 1 with no dielectric; 1.46 (polyethylene, NASA tests) or 6.16 (Shawyer's first test, citing Shawyer's 2002 SPR report) where there is one (p. 34003-p3).

Editorial check (sign convention): as printed, eq. (13) has the opposite overall sign to eq. (2). With no dielectric (n = 1), eq. (13) gives a negative value where eq. (2) gives a positive one. Recomputing Table 1 shows that the F₊d column uses the sign convention of eq. (2) (positive = towards the narrow end): for NASA 2016a, eq. (2) gives 0.54 mN and the magnitude of eq. (13) gives 0.063 mN; for Shawyer 1, eq. (2) gives 3.8 mN and eq. (13) gives a magnitude of ≈ 15.7 mN with the reversed sign. The tabulated numbers are therefore reproducible, but the printed sign of eq. (13) is inconsistent with them.

## Data used
Published emdrive tests (Table 1, p. 34003-p2): Shawyer (×2, refs. 2008 IAC paper and 2002 SPR report), Cannae (Fetta 2014), NASA Eagleworks 2014 (×4, rows 4–7, described as "the earlier NASA tests done in air", Brady et al. 2014), Tajmar & Fiedler 2015 (row 8, described as "the vacuum test"), and NASA Eagleworks 2016 in vacuum (×3, rows 9–11; White et al., J. Propuls. Power 33, 830, 2017), summarised as 1.2 mN/kW. Information about the dielectrics came from P. March and P. Wilson (acknowledgements).

Correction to the earlier summary: Table 1 labels row 7 simply "NASA 2014"; the "(vac)" label in the previous version of this README is not in the paper. The text's results paragraph reads most naturally as assigning the vacuum test to Tajmar & Fiedler (row 8), although the introduction says the NASA effect was seen "most recently in a vacuum" (p. 34003-p1).

## Results & predictions
Table 1 from the PDF (mN; p. 34003-p2, PDF p. 3), checked against the publisher HTML version used for the earlier summary; the values agree. F₋d ignores dielectrics (eq. 2); F₊d includes them (eq. 13).

| Experiment | P (W) | Q | L (m) | w_big/w_small (m) | Dielectric | F₋d | F₊d | F_obs |
|---|---|---|---|---|---|---|---|---|
| Shawyer 1 | 850 | 5900 | 0.156 | 0.16/0.1275 | narrow | 3.8 | −15.84 | 16 |
| Shawyer 2 | 1000 | 45000 | 0.345 | 0.28/0.1289 | – | 149 | 148.85 | 80–214 |
| Cannae | 10.5 | 11×10⁶ | 0.03 | 0.22/0.2 | – | 7.3 | 7.34 | 9 |
| NASA 2014 | 16.9 | 7320 | 0.2286 | 0.2794/0.1588 | narrow | 0.23 | 0.03 | 0.091 |
| NASA 2014 | 16.7 | 18100 | 〃 | 〃 | narrow | 0.57 | 0.07 | 0.05 |
| NASA 2014 | 2.6 | 22000 | 〃 | 〃 | narrow | 0.11 | 0.01 | 0.055 |
| NASA 2014 | 50 | 6730 | 〃 | 〃 | narrow | 0.64 | 0.08 | 0.03 |
| Tajmar 1 | 700 | 20 | 0.1008 | 0.1062/0.075 | – | 0.02 | 0.02 | 0.02–0.11 |
| NASA 2016a | 40 | 7123 | 0.229 | 0.279/0.159 | narrow | 0.54 | 0.06 | 0.04 |
| NASA 2016b | 60 | 7123 | 〃 | 〃 | narrow | 0.81 | 0.09 | 0.09 |
| NASA 2016c | 80 | 7123 | 〃 | 〃 | narrow | 1.08 | 0.13 | 0.09 |

- Including dielectrics brings the NASA predictions down from up to 10× too high to within a factor of ~1–6 of the observations (editorial reading of the table: the worst case is NASA 2014 at 2.6 W, 0.01 vs 0.055 mN, a factor of 5.5; the previous summary's "~1–3" understated this). The paper says QI is "particularly close for the latest batch of NASA experiments", which "arguably had the greatest experimental controls" (p. 34003-p3).
- For Shawyer 1, the dielectric-corrected value has the right magnitude (15.84 vs 16 mN) but the opposite sign.
- Editorial check: eq. (2) with the NASA 2016a inputs gives 6PQL/c × (1/0.865 − 1/1.345) ≈ 1.31 × 10⁻³ N × 0.413 ≈ 0.54 mN, matching the table.

## Figures
![Fig. 1 — Schematic of the QI emdrive mechanism: without a dielectric (top) the microwave centre of mass shifts towards the wide end, so the cavity moves towards its narrow end; with a dielectric (bottom, shaded) the photon centre of mass shifts towards the dielectric and the cavity moves the other way. Table 1 and eq. (2) are on the same page. (PDF p. 3.)](figures/fig-1-cavity-schematic.png)

![Fig. 2 — Observed emdrive thrusts (y-axis) against QI predictions (x-axis), without dielectrics (open squares) and with dielectrics (black diamonds); the diagonal marks perfect agreement. Discussion, prediction and conclusion text are on the same page. (PDF p. 5.)](figures/fig-2-predicted-vs-observed.png)

## Notable quotes
> "A previous analysis with quantised inertia predicted a controversial photon acceleration, which is shown here to be unnecessary." (p. 34003-p1, abstract; PDF p. 2)

> "It should also be noted, in its favour, that quantised inertia has no adjustable parameters." (p. 34003-p3; PDF p. 4)

> "A new prediction is that the anomalous emdrive thrust could be enhanced by increasing the overall refractive index in the cavity (see eq. (12)), and also by inserting a dielectric at the wide end (see eq. (13))." (p. 34003-p4; PDF p. 5)

## Criticisms & responses
- **The thrust.** The main criticism concerns whether emdrive thrust exists at all. The Dresden SpaceDrive group (Tajmar et al.) found that, with improved balances, the apparent thrust from emdrive cavities could be reproduced by thermal and cable/magnetic artefacts. See [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md) and [2018-tajmar-spacedrive](../../04-experiments/2018-tajmar-spacedrive/README.md). If the thrust is an artefact, the fits here are not evidence for QI.
- **NASA data.** The 2016 Eagleworks results (White et al., J. Propulsion and Power 2017) were themselves debated for possible thermal-drift systematics. See [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md).
- **Model flexibility.** The "dielectric" correction is applied per experiment, depending on where the dielectric sits and which refractive index is assumed (1.46 or 6.16), and it flips the sign for Shawyer 1. The paper itself claims "no adjustable parameters"; the per-experiment choice of n and dielectric placement is nonetheless an extra modelling input worth noting.
- **Internal consistency (editorial).** The printed eq. (13) has the opposite overall sign to eq. (2), although the tabulated values follow eq. (2)'s convention (see Key equations). The cavity-as-horizon assumption, the 1-D photon picture and the S ≈ (L + 4w)/6 average size are all carried over from the earlier papers and are acknowledged in the paper as crude.
- General QI critique: [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources:
  - [2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md) (model being revised)
  - [2015-mcculloch-emdrive-pip](../2015-mcculloch-emdrive-pip/README.md)
  - [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md)
  - [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md)
  - [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md)
