---
title: "The Universe as a Resonant Cavity: a Small Step Towards Unification of MoND and MiHsC"
authors: [Keith A. Pickering]
year: 2017
type: paper
venue: "Advances in Astrophysics 2(1), 9-11"
doi: 10.22606/adap.2017.21002
arxiv:
url: "https://doi.org/10.22606/adap.2017.21002"
open_access: true
license: all-rights-reserved
files: [paper.pdf]
status: supports
tags: [cosmology, galaxy-rotation, horizon-size, mond]
---

# The Universe as a Resonant Cavity: a Small Step Towards Unification of MoND and MiHsC

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.22606/adap.2017.21002](https://doi.org/10.22606/adap.2017.21002).

**Citation:** Pickering, K. A. (2017). *The Universe as a Resonant Cavity: a Small Step Towards Unification of MoND and MiHsC*. Advances in Astrophysics 2(1), 9–11 (February 2017), Isaac Scientific Publishing. https://doi.org/10.22606/adap.2017.21002

**TL;DR:** This is a three-page note by an independent author (not McCulloch). It treats the opaque, conducting plasma at recombination as a perfectly conducting shell around a universe of radius equal to the Hubble length, so the universe is a resonant cavity. Approximating that cavity as a cylindrical waveguide, the dominant TE₁₁ mode cutoff gives the longest allowed wavelength, Θ = 2πH₀/χ′₁₁ ≈ 3.4125 × Hubble length ≈ 4.3×10²⁶ m. This Θ is larger than MiHsC's usual 2 × Hubble length. It lowers the MiHsC minimum acceleration from 7.13 to 4.18 ×10⁻¹⁰ m/s², closing about half of the gap to MoND's a₀.

## Key claims
- Shortly after the Big Bang, the hot dense hydrogen plasma had permittivity and conductivity tending to infinity (citing Hansen & McDonald 1981). Looking back far enough, the universe is therefore bounded by a perfectly conducting shell, a "spherical resonant cavity with a radius of H₀, the Hubble length". The CMB is the redshifted blackbody emission of this shell.
- A cylinder of radius H₀ and length 2H₀ is used as a close analogue of the sphere. Its dominant-mode (TE₁₁) cutoff sets Θ, the longest wavelength the universe allows. The author says this limit also applies to blackbody and Unruh radiation.
- This Θ is greater by a factor π/χ′₁₁ = 1.71 than the Θ = 2H₀ of McCulloch (2007).
- Because MiHsC has no free parameters, changing an underlying constant in a way that brings MiHsC closer to MoND is presented as "a modest advance".

## Key equations
Cutoff frequency of a cylindrical waveguide mode (Eq. 1):
$$(f_c)_{mn} = \frac{\chi'_{mn}}{2\pi a\sqrt{\mu\varepsilon}}$$

Longest allowed wavelength, from the dominant TE₁₁ mode with a = H₀ (Eqs. 2–3):
$$\Theta = \frac{2\pi H_0}{\chi'_{1,1}}, \qquad \chi'_{1,1} = 1.8412 \;\Rightarrow\; \Theta = 3.4125\,H_0 \approx 4.3\times10^{26}\ \text{m}$$

(H₀ here denotes the Hubble *length*, 1.27×10²⁶ m, from Riess et al. 2016.)

## Data used
- Hubble length 1.27×10²⁶ m (Riess et al. 2016).
- MoND a₀ = 1.24 ± 0.14 ×10⁻¹⁰ m/s² (McGaugh 2011, gas-rich galaxies).
- Bessel-derivative zero χ′₁₁ = 1.8412 (Balanis 2012).

## Results & predictions
Table 1:

| Quantity | MoND | MiHsC (McCulloch 2007) | MiHsC (this work) |
|---|---|---|---|
| Minimum acceleration (×10⁻¹⁰ m/s²) | 1.24 | 7.13 | 4.18 |
| Minimum rotational velocity for a 10¹¹ M☉ galaxy (km/s) | 358 | 555 | 485 |

- Removes "about 35%" of the MoND–MiHsC discrepancy in rotation velocity and "about half" in acceleration.

## Figures
No figures in the paper.

## Notable quotes
> "the Universe as a whole can be considered to be a spherical resonant cavity with a radius of H0, the Hubble length." (p. 9)

> "Thus we have eliminated about 35% of the discrepancy between MoND and MiHsC in rotational velocity for typical galaxies, and about half the discrepancy in acceleration." (p. 10)

## Criticisms & responses
- No published critique of this note was found. It has 0 citations in Crossref as of this writing. McCulloch cites it in [2017-mcculloch-dwarf-galaxies](../2017-mcculloch-dwarf-galaxies/README.md) for "the slightly different result of Pickering, 2017".
- **Assumptions to note (editorial):**
  - The note equates the radius of the last-scattering shell with the Hubble length. In standard cosmology the comoving distance to last scattering is considerably larger than c/H₀.
  - It replaces a sphere with a cylindrical waveguide.
  - It treats a plasma that expands and cools over time as a static conducting wall.
- **Later QI work changed Θ again.** McCulloch's later papers used Θ = 8.8×10²⁶ m, the present co-moving diameter ([2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md)). That gives 2c²/Θ ≈ 2×10⁻¹⁰ m/s², closer to MoND than either value here. This shows the horizon-scale choice is still open in QI. See [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md) for general critique.
- **Venue.** Isaac Scientific Publishing's *Advances in Astrophysics* is a small open-access journal. The paper is three pages.

## Related
- Evidence: [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmology](../../02-evidence/cosmology.md), [derivation](../../02-evidence/derivation.md)
- Sources:
  - [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md) (source of Θ = 2H₀)
  - [2017-mcculloch-dwarf-galaxies](../2017-mcculloch-dwarf-galaxies/README.md) (cites this note)
  - [2017-mcculloch-galaxy-rotations-sparc](../2017-mcculloch-galaxy-rotations-sparc/README.md)
  - [2014-mcculloch-toy-cosmology](../2014-mcculloch-toy-cosmology/README.md)
  - [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md)
