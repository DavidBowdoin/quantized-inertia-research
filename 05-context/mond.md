---
title: "MOND (Modified Newtonian Dynamics), a0, and the a0 ≈ cH0/2π coincidence"
tags: [context, mond, galaxy-rotation, dark-matter-alternatives, wide-binaries, qi-evidence]
related: [dark-matter.md, cosmological-constant-dark-energy.md, equivalence-principle.md, holographic-principle.md]
---

# MOND

## Plain-language explanation

Mordehai Milgrom (1983) proposed that the "missing mass" in galaxies is instead a failure of Newtonian dynamics at **very low accelerations**. Below a characteristic acceleration $a_0 \approx 1.2\times10^{-10}\ \mathrm{m\,s^{-2}}$, the effective acceleration becomes $\sqrt{a_N a_0}$ rather than the Newtonian $a_N$. This one rule, with one constant, explains flat rotation curves and predicts the **baryonic Tully–Fisher relation** ($v^4 \propto M_{\text{baryon}}$) and the tight **radial acceleration relation** (RAR) seen in disc galaxies (McGaugh, Lelli & Schombert 2016). MOND can be formulated as **modified gravity** (e.g. AQUAL, QUMOND; relativistic versions such as TeVeS and AeST) or as **modified inertia** (Milgrom 1994, 2011).

## Key equations

$$
\mu\!\left(\frac{|\mathbf a|}{a_0}\right)\mathbf a = \mathbf a_N, \qquad \mu(x)\to 1\ (x\gg1),\quad \mu(x)\to x\ (x\ll1)
$$

Deep-MOND limit and baryonic Tully–Fisher relation:

$$
a = \sqrt{a_N a_0}\quad\Rightarrow\quad v^4 = G M a_0
$$

The cosmological coincidence (Milgrom 1983 onward):

$$
2\pi a_0 \approx c H_0 \approx c\sqrt{\Lambda/3}
\qquad\Rightarrow\qquad a_0 \approx \frac{cH_0}{2\pi}\approx 1.1\times10^{-10}\ \mathrm{m\,s^{-2}}\ \ (H_0\approx 70\ \mathrm{km\,s^{-1}Mpc^{-1}})
$$

Milgrom (1999) noted that the difference between the Unruh temperature of an accelerated observer in de Sitter space, $T\propto\sqrt{a^2 + a_0'^2}$, and the Gibbons–Hawking temperature $T\propto a_0'$ ($a_0' = c\sqrt{\Lambda/3}$) behaves like $a$ at high acceleration and like $a^2/2a_0'$ at low acceleration, giving MOND-like inertia with $a_0 \sim 2c\sqrt{\Lambda/3}$ up to factors of order unity. He called this a suggestive argument, not a theory.

## Mainstream status

- **Successes:** MOND is remarkably successful at the scale of individual galaxies (rotation curves, RAR, Tully–Fisher, many dwarf systems). Famaey & McGaugh (2012) is the standard review.
- **Problems:** It fails to account for the dynamics of **galaxy clusters** without additional unseen mass (Sanders 2003), and non-relativistic MOND cannot address the **CMB acoustic peaks**, structure formation or the **Bullet Cluster** without extra ingredients (see [dark-matter.md](dark-matter.md)). The relativistic AeST theory (Skordis & Złośnik 2021) claims fits to the CMB and matter power spectrum, but it adds new fields and is not widely accepted.
- **Wide binaries:** a live test. Chae (2023) and Hernandez and collaborators report a MOND-like boost in Gaia wide binaries at accelerations below ~$10^{-9}\ \mathrm{m\,s^{-2}}$ ([Chae 2023](../01-papers/2023-chae-wide-binaries/README.md), [Hernandez et al. 2012](../01-papers/2012-hernandez-wide-binaries/README.md), [2019](../01-papers/2019-hernandez-gaia-wide-binaries/README.md), [2024 review](../01-papers/2024-hernandez-wide-binary-review/README.md)); Banik et al. (2024) find Newtonian gravity preferred over MOND at 19σ ([criticism folder](../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md)). The disagreement is unresolved and centres on sample cleaning (hidden triples, projection effects).
- Overall, MOND is a minority but scientifically serious position, published in mainstream journals; ΛCDM with dark matter is the consensus framework.

## How it relates to QI

QI is best understood as a **specific modified-inertia variant of MOND-like phenomenology** that claims to *derive* $a_0$ instead of fitting it:

$$
m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right),\qquad
v^4 = \frac{2GMc^2}{\Theta}\ \ \Longleftrightarrow\ \ a_0^{\text{QI}} = \frac{2c^2}{\Theta}
$$

([McCulloch 2012](../01-papers/2012-mcculloch-galactic-scales/README.md), [2017 SPARC](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md), [2017 dwarfs](../01-papers/2017-mcculloch-dwarf-galaxies/README.md)). With $\Theta$ as the comoving diameter of the observable universe ($8.8\times10^{26}$ m), $2c^2/\Theta\approx 2.0\times10^{-10}\ \mathrm{m\,s^{-2}}$, within a factor of ~2 of the empirical $a_0$. This is QI's version of the $a_0\approx cH_0/2\pi$ coincidence: any $a_0$ built from $c$ and a cosmic length is automatically within an order of magnitude of $cH_0$.

Points to weigh:

1. **The choice of $\Theta$ matters.** The 2007 Pioneer paper used $\Theta = 2.6\times10^{26}$ m (twice the Hubble distance), giving $2c^2/\Theta\approx 6.9\times10^{-10}\ \mathrm{m\,s^{-2}}$; the 2017 SPARC paper explicitly switched to $8.8\times10^{26}$ m (comoving diameter). Since the result scales as $1/\Theta$, the "no adjustable parameter" claim depends on which cosmic length is regarded as physically correct. Order-unity factors are exactly what distinguishes a derivation from a numerical coincidence.
2. **Redshift dependence.** Because $\Theta$ grows with time, QI predicts $a_0$ was larger in the past (claimed consistent with data up to $z\approx2.2$ in the SPARC paper). Standard MOND treats $a_0$ as constant (though Milgrom has considered variation). This is a genuine distinguishing prediction.
3. **Interpolation function.** Several papers claim QI yields an expression close to the "simple" MOND interpolating function ([McCulloch & Giné 2020](../01-papers/2020-mcculloch-horizon-widths/README.md), [Giné & Luciano 2020](../01-papers/2020-gine-luciano-eup-modified-inertia/README.md)).
4. **Shared problems.** QI inherits MOND's difficulties with clusters, the Bullet Cluster and the CMB, and its predictions for wide binaries ([McCulloch & Lucio 2019](../01-papers/2019-mcculloch-wide-binaries/README.md)) stand or fall with the contested wide-binary data. Pickering's resonant-cavity extension tries to link MiHsC and MOND more tightly ([Pickering 2017](../01-papers/2017-pickering-resonant-cavity/README.md)); Smolin (2017) and Cadoni & Tuveri (2019) explore related horizon/quantum-gravity origins for $a_0$ ([Smolin](../01-papers/2017-smolin-mond-quantum-gravity/README.md), [Cadoni](../01-papers/2019-cadoni-long-range-qg/README.md)).

## References

- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *ApJ* 270, 365. https://doi.org/10.1086/161130
- Milgrom, M. (1999). The modified dynamics as a vacuum effect. *Phys. Lett. A* 253, 273. https://doi.org/10.1016/S0375-9601(99)00077-8 (arXiv:astro-ph/9805346)
- Milgrom, M. (2014). MOND theory. arXiv:1404.7661. https://arxiv.org/abs/1404.7661
- Famaey, B., McGaugh, S. S. (2012). Modified Newtonian Dynamics (MOND): observational phenomenology and relativistic extensions. *Living Rev. Relativ.* 15, 10. https://doi.org/10.12942/lrr-2012-10
- McGaugh, S. S., Lelli, F., Schombert, J. M. (2016). Radial acceleration relation in rotationally supported galaxies. *Phys. Rev. Lett.* 117, 201101. https://doi.org/10.1103/PhysRevLett.117.201101
- Sanders, R. H. (2003). Clusters of galaxies with modified Newtonian dynamics. *MNRAS* 342, 901. https://doi.org/10.1046/j.1365-8711.2003.06596.x
- Skordis, C., Złośnik, T. (2021). New relativistic theory for modified Newtonian dynamics. *Phys. Rev. Lett.* 127, 161302. https://doi.org/10.1103/PhysRevLett.127.161302
- McCulloch, M. E. (2017). Galaxy rotations from quantised inertia and visible matter only. arXiv:1709.04918. https://arxiv.org/abs/1709.04918
- Wikipedia: Modified Newtonian dynamics. https://en.wikipedia.org/wiki/Modified_Newtonian_dynamics
