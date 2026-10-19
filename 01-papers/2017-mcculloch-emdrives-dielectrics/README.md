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
files: []
status: supports
tags: [emdrive, propulsion, lab-test]
---

# Testing quantised inertia on emdrives with dielectrics

**Citation:** McCulloch, M. E. (2017). *Testing quantised inertia on emdrives with dielectrics*. EPL 118(3), 34003 (May 2017). https://doi.org/10.1209/0295-5075/118/34003. Open access under CC BY 3.0 (hybrid OA).

> [!NOTE]
> **PDF not retrievable.** The publisher PDF (iopscience.iop.org) is bot-protected and returned HTML to automated download. No arXiv preprint was found. This summary is based on the publisher's HTML article page, fetched 2026-10-18, so page numbers are not available.

**TL;DR:** This updates McCulloch's QI emdrive model ([2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md)). First, it drops the earlier "controversial" assumption that photon speed changes in the cavity, calling that photon acceleration unnecessary. Second, it treats a dielectric of refractive index n at one end as equivalent to widening the cavity at that end, using m = m_L(1 − λ_U/4nS). With dielectrics included, the predictions match the observed thrusts, including three 2016 NASA results, except Shawyer's first test. There the magnitude matches but the predicted direction is reversed. The paper predicts that a dielectric at the *wide* end would boost thrust.

## Key claims
- Emdrives move slightly towards their narrow ends, "in contradiction to standard physics" (Abstract, per publisher page).
- QI explains this through photon inertia due to Unruh radiation, more of which is allowed at the wide end.
- The previous analysis "predicted a controversial photon acceleration, which is shown here to be unnecessary". It also mispredicted thrust for emdrives with dielectrics.
- A dielectric at one end is modelled as making that end effectively wider by a factor n.
- The conclusion counts nine tests in four independent labs showing anomalous thrust towards the narrow end.
- Suggested tests: change or reverse thrust by altering the cavity aspect ratio, increasing P or Q, filling the cavity with dielectric, or (more effectively) adding a dielectric at the wide end.

## Key equations
As rendered on the publisher's page (the main thrust equations are images and were not transcribed):

MiHsC modified inertial mass for the cosmic-horizon case, with S the horizon/cavity scale:
$$m = m_L\left(1 - \frac{\lambda_U}{4S}\right)$$

Generalisation for a dielectric of refractive index n:
$$m = m_L\left(1 - \frac{\lambda_U}{4nS}\right)$$

> [!UNVERIFIED] The full thrust formula with dielectric terms could not be transcribed from the source.

## Data used
Published emdrive tests: Shawyer (×2), Cannae, NASA Eagleworks 2014 (×4, including a vacuum test), Tajmar & Fiedler 2015, and NASA Eagleworks 2016 (×3; White et al. 2016/2017, summarised as ~1.2 mN/kW).

## Results & predictions
Table 1 as given on the publisher's HTML page (mN). F₋d ignores dielectrics; F₊d includes them.

| Experiment | P (W) | Q | L (m) | w_big/w_small (m) | Dielectric | F₋d | F₊d | F_obs |
|---|---|---|---|---|---|---|---|---|
| Shawyer 1 | 850 | 5900 | 0.156 | 0.16/0.1275 | narrow | 3.8 | −15.84 | 16 |
| Shawyer 2 | 1000 | 45000 | 0.345 | 0.28/0.1289 | – | 149 | 148.85 | 80–214 |
| Cannae | 10.5 | 11×10⁶ | 0.03 | 0.22/0.2 | – | 7.3 | 7.34 | 9 |
| NASA 2014 | 16.9 | 7320 | 0.2286 | 0.2794/0.1588 | narrow | 0.23 | 0.03 | 0.091 |
| NASA 2014 | 16.7 | 18100 | 〃 | 〃 | narrow | 0.57 | 0.07 | 0.05 |
| NASA 2014 | 2.6 | 22000 | 〃 | 〃 | narrow | 0.11 | 0.01 | 0.055 |
| NASA 2014 (vac) | 50 | 6730 | 〃 | 〃 | narrow | 0.64 | 0.08 | 0.03 |
| Tajmar 1 | 700 | 20 | 0.1008 | 0.1062/0.075 | – | 0.02 | 0.02 | 0.02–0.11 |
| NASA 2016a | 40 | 7123 | 0.229 | 0.279/0.159 | narrow | 0.54 | 0.06 | 0.04 |
| NASA 2016b | 60 | 7123 | 〃 | 〃 | narrow | 0.81 | 0.09 | 0.09 |
| NASA 2016c | 80 | 7123 | 〃 | 〃 | narrow | 1.08 | 0.13 | 0.09 |

- Including dielectrics brings the NASA predictions down from 10× too high to within a factor of ~1–3 of the observations.
- For Shawyer 1, the dielectric-corrected value has the right magnitude (15.84 vs 16 mN) but the opposite sign.

## Figures
Not reproduced (no PDF obtained).

## Notable quotes
> [!UNVERIFIED] Quotes and page numbers could not be verified against a PDF. The abstract on the publisher page includes: "A previous analysis with quantised inertia predicted a controversial photon acceleration, which is shown here to be unnecessary."

## Criticisms & responses
- **The thrust.** The main criticism concerns whether emdrive thrust exists at all. The Dresden SpaceDrive group (Tajmar et al.) found that, with improved balances, the apparent thrust from emdrive cavities could be reproduced by thermal and cable/magnetic artefacts. See [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md) and [2018-tajmar-spacedrive](../../04-experiments/2018-tajmar-spacedrive/README.md). If the thrust is an artefact, the fits here are not evidence for QI.
- **NASA data.** The 2016 Eagleworks results (White et al., J. Propulsion and Power 2017) were themselves debated for possible thermal-drift systematics. See [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md).
- **Model flexibility.** The "dielectric" correction is applied per experiment, depending on where the dielectric sits, and it flips the sign for Shawyer 1. Since QI is advertised as having no free parameters, this added modelling choice is worth noting.
- General QI critique: [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [emdrive](../../02-evidence/emdrive.md), [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources:
  - [2015-mcculloch-emdrive-epl](../2015-mcculloch-emdrive-epl/README.md) (model being revised)
  - [2015-mcculloch-emdrive-pip](../2015-mcculloch-emdrive-pip/README.md)
  - [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md)
  - [2016-white-eagleworks](../../04-experiments/2016-white-eagleworks/README.md)
  - [2021-tajmar-emdrive-false-positive](../../03-criticism/2021-tajmar-emdrive-false-positive/README.md)
