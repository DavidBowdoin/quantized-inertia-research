---
title: "Dark matter: evidence and the challenge for no-dark-matter theories"
tags: [context, dark-matter, cosmology, bullet-cluster, cmb, galaxy-rotation]
related: [mond.md, cosmological-constant-dark-energy.md, equivalence-principle.md]
---

# Dark matter

## Plain-language explanation

"Dark matter" is the name for gravitating mass that does not emit or absorb light. The case for it rests on **many independent lines of evidence** at very different scales and epochs, which is why most cosmologists regard it as established even though its particle nature is unknown:

1. **Galaxy rotation curves** stay flat far beyond the visible disc (Rubin & Ford 1970 and later 21-cm data).
2. **Galaxy clusters**: velocity dispersions (Zwicky 1933), hot X-ray gas in hydrostatic equilibrium, and gravitational lensing all require ~5–6× more mass than baryons provide.
3. **The Bullet Cluster (1E 0657-558):** two clusters collided; the hot gas (most of the baryons) was slowed and sits between them, but weak and strong **lensing shows the mass peaks offset from the gas, coinciding with the galaxies** (Clowe et al. 2006, 8σ offset). This is widely cited as direct evidence for collisionless mass and a strong challenge to pure modified-gravity or modified-inertia explanations, which would place the lensing mass on the baryons.
4. **The cosmic microwave background (CMB) acoustic peaks:** the relative heights of the peaks in the CMB temperature power spectrum (notably the third peak relative to the second) and the polarisation spectra require a component that clusters gravitationally but does not feel photon pressure. Planck 2018 gives $\Omega_c h^2 = 0.120\pm0.001$ versus $\Omega_b h^2 = 0.0224\pm0.0001$.
5. **Large-scale structure and BAO:** the growth of structure from tiny CMB fluctuations to today's cosmic web and the baryon acoustic oscillation feature (Eisenstein et al. 2005) fit cold dark matter.
6. **Big-Bang nucleosynthesis** fixes the baryon density independently, confirming most matter is non-baryonic.

## Key equations

Flat rotation curve implies mass growing linearly with radius:

$$
\frac{v^2}{r} = \frac{G M(r)}{r^2}\ \Rightarrow\ M(r) = \frac{v^2 r}{G}\ \propto r\quad (v=\text{const})
$$

Lensing convergence measures the projected total mass directly:

$$
\kappa(\boldsymbol\theta) = \frac{\Sigma(\boldsymbol\theta)}{\Sigma_{\rm cr}}, \qquad \Sigma_{\rm cr} = \frac{c^2 D_s}{4\pi G D_l D_{ls}}
$$

## Mainstream status

ΛCDM (cosmological constant + cold dark matter) is the consensus model. Unsolved problems: no confirmed non-gravitational detection (e.g. LZ 2023 null results for WIMPs), and small-scale tensions (cusp–core, too-big-to-fail, the tightness of the RAR that MOND predicts naturally). Bertone & Hooper (2018) give a history and overview.

## How it relates to QI

QI claims to explain galaxy rotation ([2012](../01-papers/2012-mcculloch-galactic-scales/README.md), [2017 SPARC](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md)), dwarf satellites ([2017](../01-papers/2017-mcculloch-dwarf-galaxies/README.md)), wide binaries ([2019](../01-papers/2019-mcculloch-wide-binaries/README.md)), Proxima Centauri ([2024](../01-papers/2024-mcculloch-proxima-centauri/README.md)) and Jupiter-mass binaries ([2025](../01-papers/2025-mcculloch-jupiter-mass-binaries/README.md)) **without dark matter**, and McCulloch has popularised this ([SciTrends 2018](../07-media/2018-mcculloch-dark-matter-scitrends/README.md)). The 2012 paper also claims galaxy-cluster velocities.

To be a full replacement for dark matter, however, QI would need to account for:

- **Gravitational lensing.** QI modifies *inertial* mass, not gravitational mass. Light bending depends on the spacetime curvature produced by gravitational mass, so it is not obvious how a modification of inertia produces the extra lensing seen in clusters. McCulloch has a [2022 preprint](../01-papers/2022-mcculloch-light-bending/README.md) on solar light bending, but a quantitative QI treatment of cluster lensing is not established in the sources collected here.
- **The Bullet Cluster offset** between lensing mass and baryonic gas.
- **The CMB power spectrum** (peak heights, polarisation) and structure growth, which require a quantitative cosmological model that QI's [toy cosmology](../01-papers/2014-mcculloch-toy-cosmology/README.md) does not supply.

> [!UNVERIFIED]
> No peer-reviewed QI calculation of the Bullet Cluster lensing map or of the CMB acoustic peaks was identified while writing this note. If one exists it should be added to `01-papers/` and linked here.

## References

- Rubin, V. C., Ford, W. K. (1970). Rotation of the Andromeda nebula from a spectroscopic survey of emission regions. *ApJ* 159, 379. https://doi.org/10.1086/150317
- Clowe, D. et al. (2006). A direct empirical proof of the existence of dark matter. *ApJ* 648, L109. https://doi.org/10.1086/508162 (arXiv:astro-ph/0608407)
- Markevitch, M. et al. (2004). Direct constraints on the dark matter self-interaction cross section from the merging galaxy cluster 1E 0657-56. *ApJ* 606, 819. https://doi.org/10.1086/383178
- Planck Collaboration (2020). Planck 2018 results. VI. Cosmological parameters. *A&A* 641, A6. https://doi.org/10.1051/0004-6361/201833910
- Eisenstein, D. J. et al. (2005). Detection of the baryon acoustic peak in the large-scale correlation function of SDSS luminous red galaxies. *ApJ* 633, 560. https://doi.org/10.1086/466512
- Bertone, G., Hooper, D. (2018). History of dark matter. *Rev. Mod. Phys.* 90, 045002. https://doi.org/10.1103/RevModPhys.90.045002
- LZ Collaboration (2023). First dark matter search results from the LUX-ZEPLIN (LZ) experiment. *Phys. Rev. Lett.* 131, 041002. https://doi.org/10.1103/PhysRevLett.131.041002
- Wikipedia: Dark matter. https://en.wikipedia.org/wiki/Dark_matter ; Bullet Cluster. https://en.wikipedia.org/wiki/Bullet_Cluster
