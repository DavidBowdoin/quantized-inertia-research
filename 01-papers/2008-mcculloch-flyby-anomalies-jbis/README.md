---
title: "Can the flyby anomalies be explained by a modification of inertia?"
authors: [Michael E. McCulloch]
year: 2008
type: paper
venue: "Journal of the British Interplanetary Society 61, 373-378"
doi:
arxiv: "0712.3022"
url: "https://arxiv.org/abs/0712.3022"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-galileo-flyby.png, figures/fig-2-near-flyby.png]
status: supports
tags: [flyby-anomaly, propulsion]
---

# Can the flyby anomalies be explained by a modification of inertia?

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:0712.3022](https://arxiv.org/abs/0712.3022).

**Citation:** McCulloch, M. E. (2008). *Can the flyby anomalies be explained by a modification of inertia?* Journal of the British Interplanetary Society 61, 373-378. [arXiv:0712.3022](https://arxiv.org/abs/0712.3022)

**TL;DR:** This is the first application of MiHsC (the name is introduced here) to the Earth-flyby anomalies of Galileo, NEAR, Cassini and Rosetta. In the model, inertial mass collapses for ~10⁻⁷ s when the craft's acceleration passes near zero around closest approach. That gives Earthward velocity jumps of a few mm/s, close to the observed values except for NEAR. The paper stresses that the result works only for a very narrow range of the Hubble constant. It also proposes metamaterials as a way to reduce inertia in the lab.

> Notes: No DOI was found for JBIS; the journal reference comes from the arXiv journal_ref. The text and page numbers here are from arXiv v1 (Dec 2007), a summary of a talk given at the British Interplanetary Society on 15 Nov 2007.
>
> [!UNVERIFIED] Repository notes say the author describes most of this paper as superseded (compare the later MNRAS letter, [2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md)). The original statement has not been located.

## Key claims
- The galaxy-rotation, Pioneer and flyby anomalies can all be read as unexpected increases in gravitational interaction, and a loss of inertial mass is one way to get that.
- Modified inertia is presented as "the only approach that can be made to depend upon trajectory", which the author argues the Pioneer data and the planets require.
- Following Ignatiev (2007), the paper argues that short zones of reduced inertia can occur when a body's total acceleration (relative to the galactic centre, approximated here by the Sun) passes near zero.
- In this paper bound orbits (Earth, Moon, Sun) are assumed not to show the effect, so only the spacecraft's inertia is modified.
- Metamaterials that bend Unruh radiation around an object, or that make a smaller effective Θ, might reduce its inertial mass measurably.

## Key equations
MiHsC inertial mass, with a measured relative to the galactic centre, β = 0.2 and Θ = 2c/H:
$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{a\Theta}\right) $$

## Data used
- JPL Horizons ephemerides at 1-minute resolution for the Earth, the Moon and the spacecraft.
- Observed flyby ΔV values (Anderson et al. 2007; Lämmerzahl et al. 2006): Galileo 3.92 ± 0.08, NEAR 13.46 ± 0.13, Cassini 0.11, Rosetta 1.82 ± 0.05 mm/s.
- Method:
  - Forward-stepping Newtonian + MiHsC integration over 6 h, with a 0.2 s time step refined to O(10⁻⁷ s) at the moment of zero acceleration.
  - Acceleration held at or above 6.9 × 10⁻¹⁰ m s⁻².
  - H = 2.33 × 10⁻¹⁸ s⁻¹.

## Results & predictions
| Mission | Observed dV (mm/s) | Predicted Earthward dV (mm/s) | Mass, nominal (minimum) (kg) | Mass-loss duration (s) | Time after C.A. (min) |
|---|---|---|---|---|---|
| Galileo | 3.92 | 2.6 | 2497 (2.1) | 3 × 10⁻⁷ | 12 |
| NEAR | 13.46 | 1.2 | 730 (0.6) | 0.6 × 10⁻⁷ | −2 |
| Cassini | 0.11 | 1.4 | 4612 (4.0) | 2 × 10⁻⁷ | 7 |
| Rosetta | 1.82 | 1.9 | 2895 (2.5) | 2 × 10⁻⁷ | 9 |

- Galileo and Rosetta agree "quite well". NEAR is an order of magnitude too small.
- The result is very sensitive to the Hubble constant:
  - H = 2.3 × 10⁻¹⁸ s⁻¹ gives jumps of less than 1 mm/s.
  - H ≥ 2.34 × 10⁻¹⁸ s⁻¹ gives negative jumps.
- For Galileo, the predicted distance anomaly grows at about 10 m per hour (~3 mm/s).
- The Unruh wavelength at 9.8 m s⁻² is ~10¹⁶ m. The paper cites Pendry & Wood (2007) on zero-frequency metamaterials as a possible route to a test.

## Figures
*Figure (local only): Fig. 1 — Galileo Earth flyby, 8 Dec 1990. Panels: trajectories (top left), velocity, acceleration and inertial mass (bottom left), predicted velocity anomaly (top right), predicted distance anomaly (bottom right) (p. 10).*

*Figure (local only): Fig. 2 — NEAR Earth flyby, 23 Jan 1998, with the same panels; the predicted jump is about an order of magnitude below the observed one (p. 11).*

## Notable quotes
> "However, these results were extremely sensitive to the Hubble constant used." (p. 1)

> "Therefore, this theory succeeds for only a very narrow range of values of H." (pp. 6–7)

> "It is therefore hoped that other specialist groups can reproduce these results." (p. 8)

## Criticisms & responses
- **Fine-tuning.** The paper itself states that the agreement depends on choosing H within ~1% (2.33 vs 2.30 or 2.34 × 10⁻¹⁸ s⁻¹), and that NEAR's anomaly is not reproduced.
- **Superseded model.** Later the same year, the MNRAS letter ([2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md)) replaced the galactic-centre / zero-crossing mechanism with accelerations relative to the spinning Earth.
- **Later flyby data.** A reconstruction of Juno's October 2013 Earth flyby (Thompson et al., AAS 14-435; [NTRS 20160008163](https://ntrs.nasa.gov/citations/20160008163)) found no anomalous velocity change at or near perigee. This limits all flyby-anomaly models, but it is not a specific response to this paper.
- No published rebuttal aimed specifically at this JBIS paper was found in a brief search.

## Related
- Evidence: [flyby-anomaly](../../02-evidence/flyby-anomaly.md), [propulsion](../../02-evidence/propulsion.md)
- Sources:
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md)
  - [2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md)
  - [2015-iorio-solar-system-anomalies](../2015-iorio-solar-system-anomalies/README.md)
