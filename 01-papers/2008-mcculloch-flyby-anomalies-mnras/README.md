---
title: "Modelling the flyby anomalies using a modification of inertia"
authors: [Michael E. McCulloch]
year: 2008
type: paper
venue: "Monthly Notices of the Royal Astronomical Society: Letters 389(1), L57-L60"
doi: 10.1111/j.1745-3933.2008.00523.x
arxiv: "0806.4159"
url: "https://doi.org/10.1111/j.1745-3933.2008.00523.x"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-near-geometry.png, figures/fig-2-observed-vs-predicted.png]
status: supports
tags: [flyby-anomaly]
---

# Modelling the flyby anomalies using a modification of inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:0806.4159](https://arxiv.org/abs/0806.4159) · [doi:10.1111/j.1745-3933.2008.00523.x](https://doi.org/10.1111/j.1745-3933.2008.00523.x).

**Citation:** McCulloch, M. E. (2008). *Modelling the flyby anomalies using a modification of inertia*. Monthly Notices of the Royal Astronomical Society: Letters 389(1), L57-L60. [doi:10.1111/j.1745-3933.2008.00523.x](https://doi.org/10.1111/j.1745-3933.2008.00523.x) / [arXiv:0806.4159](https://arxiv.org/abs/0806.4159)

**TL;DR:** This paper reworks the MiHsC flyby model. The craft's acceleration is now taken relative to every particle of the rotating Earth. A craft leaving over a pole "sees" less acceleration than one leaving over the equator, so its inertia is lower and, with momentum conserved, its speed rises. The result is a formula with the same dependence on cos φ₁ − cos φ₂ as Anderson et al.'s (2008) empirical fit. It reproduces three of six flybys within error bars; the other three are off by 1–3 mm/s.

> Text and page numbers are from arXiv v2 (Jun 2008), stored as `paper.pdf`.

## Key claims
- In this version of MiHsC, the acceleration *a* is "the acceleration of the craft relative to the matter in its local environment". For a flyby, that means the average acceleration of the rotating Earth's mass as seen by the craft.
- A craft leaving on a polar path sees a lower average relative acceleration, so it has lower inertial mass and, by momentum conservation, gains speed.
- The derived formula has no adjustable parameters. It reproduces the latitude dependence of Anderson et al. (2008), whose formula was fitted to the data.
- The model "only seems to apply to unbound trajectories and the reason for this is unknown". The paper notes that the same variation of inertia would conflict with Earth-based equivalence-principle tests (Carusotto et al. 1992; Schlamminger et al. 2008).
- Prediction: larger anomalies for slower-spinning, larger bodies. The paper gives the Rosetta Mars flyby (Feb 2007) as a test, where the anomaly should be about double Earth's.

## Key equations
Anderson et al. (2008) empirical formula (as quoted):
$$ dv = 3.099\times10^{-6}\, v_\infty (\cos\phi_1 - \cos\phi_2) $$
MiHsC inertia:
$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{a\Theta}\right) $$
Velocity change due to modified inertia:
$$ dv' = \frac{\beta\pi^2 c^2}{\Theta}\left(\frac{v_2}{a_2} - \frac{v_1}{a_1}\right) $$
Using the mean Earth-particle acceleration a = (0.07 v_e²/R) cos φ:
$$ dv' = \frac{\beta\pi^2 R c^2}{0.07\, v_e^2\, \Theta}\left(\frac{v_2\cos\phi_1 - v_1\cos\phi_2}{\cos\phi_1\cos\phi_2}\right) = 2.8\times10^{-7}\left(\frac{v_2\cos\phi_1 - v_1\cos\phi_2}{\cos\phi_1\cos\phi_2}\right) $$
Appendix (linear density profile, α = 0.974):
$$ \bar a_x = \frac{4 v_e^2}{\pi R}\left(\frac14 - \frac{\alpha}{5}\right) \sim 0.07\,\frac{v_e^2}{R} $$

## Data used
- Six Earth flybys (speeds, incoming and outgoing latitudes, observed ΔV) from Anderson et al. (2008, *PRL* 100, 091102).
- Inputs: R = 6371 km, v_e = 465 m/s, Θ = 2.7 × 10²⁶ m. Errors assume 9% uncertainty in H, ±3° in latitude, and 10% in the density profile.

## Results & predictions
| Mission | Latitudes in, out (deg) | Observed dV (mm/s) | Predicted (mm/s) |
|---|---|---|---|
| Galileo-I | −12.5, −34.2 | 3.92 ± 0.08 | 2.9 ± 0.6 |
| Galileo-II | −34.3, −4.9 | −4.6 ± 0.08 | −0.9 ± 0.2 |
| NEAR | −20.8, −72 | 13.46 ± 0.13 | 20.1 ± 4.0 |
| Cassini | −12.9, −5 | −2 | 0.9 ± 0.2 |
| Rosetta | −2.8, −34.3 | 1.8 ± 0.05 | 3.2 ± 0.6 |
| Messenger | 31.4, −31.9 | 0.02 ± 0.05 | −1.3 ± 0.2 |

- The paper reports agreement for Galileo-I, NEAR and Rosetta. The differences are about 1 mm/s for Messenger, 2 mm/s for Cassini and 3 mm/s for Galileo-II. For Galileo-II the paper notes that the observed value had to be corrected for atmospheric drag.
- The correlation between observed and predicted values is 0.94, "although this is not significant at the 5% level". The preprint gives "the p value is 30", presumably meaning 30%.
- The paper says Pioneer results from McCulloch (2007) would be largely unchanged, because the Pioneers stayed at low latitude relative to the Sun.

## Figures
*Figure (local only): Fig. 1 — Schematic of the NEAR flyby (incoming at −21°, outgoing at −72° latitude) with the angles used in the derivation (p. 12).*

*Figure (local only): Fig. 2 — Observed (diamonds) and predicted (pluses, with error bars) velocity jumps for the six flybys, in mm/s (p. 13).*

## Notable quotes
> "These results suggest that, if this model is correct, it only applies to unbound orbits. The reason for this is unknown." (p. 5)

> "The predictions of equation (8) are not as close as the predictions of Anderson et al.'s suggestive equation (1), although their empirical formula was, of course, fitted to the data, whereas equation (8) was derived from a theory." (p. 7)

## Criticisms & responses
- **Equivalence principle and bound orbits.** The paper concedes that the predicted variation of inertia conflicts with laboratory equivalence-principle tests unless the effect applies only to unbound trajectories, a restriction it does not explain.
- **Small sample.** The paper itself states that the correlation between observed and predicted values (r = 0.94, n = 6) is not significant at 5%.
- **New definition of acceleration.** The acceleration is taken relative to all particles of the rotating Earth. This differs from the 2007 Pioneer paper and the JBIS flyby paper ([2008-mcculloch-flyby-anomalies-jbis](../2008-mcculloch-flyby-anomalies-jbis/README.md)), which used the Sun or galactic centre. Readers may see this as an extra modelling choice.
- **Later flyby data.** A reconstruction of Juno's 2013 Earth flyby (Thompson et al., AAS 14-435; [NTRS 20160008163](https://ntrs.nasa.gov/citations/20160008163)) found no anomalous velocity change at perigee. Iorio's review of Solar System anomalies covers flyby-anomaly proposals more generally; see [2015-iorio-solar-system-anomalies](../2015-iorio-solar-system-anomalies/README.md).
- **EPOXI.** McCulloch himself later reported (2011, [2011-mcculloch-tajmar-effect](../2011-mcculloch-tajmar-effect/README.md), p. 7) that the EPOXI flyby showed zero anomaly, although MiHsC predicted a large one. He attributed this to EPOXI's larger periapse (49,835 km).
- > [!UNVERIFIED] No published check of this paper's Mars-flyby prediction was found in a brief search.

## Related
- Evidence: [flyby-anomaly](../../02-evidence/flyby-anomaly.md)
- Sources:
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
  - [2008-mcculloch-flyby-anomalies-jbis](../2008-mcculloch-flyby-anomalies-jbis/README.md)
  - [2015-iorio-solar-system-anomalies](../2015-iorio-solar-system-anomalies/README.md)
  - [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
