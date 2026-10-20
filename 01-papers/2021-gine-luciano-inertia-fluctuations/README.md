---
title: "Modeling inertia through the interaction with quantum fluctuations"
authors: [Jaume Giné, Giuseppe Gaetano Luciano]
year: 2021
type: paper
venue: "Results in Physics 28, 104543"
doi: 10.1016/j.rinp.2021.104543
arxiv:
url: "https://doi.org/10.1016/j.rinp.2021.104543"
open_access: true
license: CC-BY-4.0
files: [paper.pdf, figures/fig-1-rindler-casimir.png]
status: supports
tags: [rindler-horizon, casimir, quantum-fluctuations, uncertainty-principle, origin-of-inertia]
---

# Modeling inertia through the interaction with quantum fluctuations

**Citation:** Giné, J. & Luciano, G. G. (2021). *Modeling inertia through the interaction with quantum fluctuations*. Results in Physics, 28, 104543 (received 19 Feb 2021, accepted 10 July 2021, available online 29 July 2021). https://doi.org/10.1016/j.rinp.2021.104543 (gold open access, CC BY 4.0).

**About the stored PDF:** `paper.pdf` is the published Elsevier version (5 pages, article pages 1–5 = PDF pp. 1–5). The CC BY 4.0 licence is stated on p. 1. Page references below are PDF/article pages.

**TL;DR:** The paper models inertia as arising from interactions between a body's Planck-size "resonant parts" and quantum (vacuum) fluctuations. Model 1 applies the Heisenberg uncertainty principle: each resonant part receives energy ≈ ħc/2ℓ_p, i.e. mass m_p/2, and a body of n parts has M ≃ n m_p/2. Model 2 revisits McCulloch's QI as a "Rindler-scale Casimir effect": the Rindler horizon at c²/a damps fluctuations on one side, giving a force F_x ≃ −0.6 m_p a/k per resonant part. Requiring the two to agree fixes k ≃ 1.2. The paper deliberately neglects the Hubble-scale (MiHsC) correction, so it addresses ordinary inertia only, and it corrects two steps in McCulloch's earlier derivations.

## Key claims
- Two assumptions (p. 1): (i) any body is a collection of resonant parts of Planck size, generalising the corpuscular (Dvali–Gomez) picture of black holes to any macroscopic body; (ii) inertia is the result of these parts interacting with vacuum fluctuations.
- Model 1 (HUP, pp. 2–3): fluctuations of energy ΔE ≃ ħc/2Δx act on each resonant part; integrating from ℓ_p to an effective cutoff radius r_e ≫ ℓ_p gives E ≃ ħc/2ℓ_p, i.e. mass m_p/2 per part. Counting parts as n ≃ r_s/ℓ_p = 2M/m_p (via a Schwarzschild-radius "particle event horizon" picture) closes the loop: n E/c² ≃ M. The authors present this as a realisation of Mach's principle with quantum fluctuations in place of distant stars.
- An entropy relation links the number of resonant parts to a body's density, S = n²[1 + log(ρ_bh/ρ)], using an assumed ξ ≃ κ/ρ for the number of states per graviton (p. 3).
- Model 2 (Rindler-scale Casimir effect, pp. 3–4): for a body accelerating to the right, the Rindler horizon at c²/a on the left weakens fluctuations from that side, giving a net force against the acceleration. The Hubble-scale correction 2c²/(aΘ), with Θ ≃ 10²⁶ m, is neglected because the paper is "interested in explaining the origin of pure inertia" (p. 3). Footnote 2: 2c²/Θ ≃ 10⁻¹⁰ m/s².
- Corrections to QI papers (p. 4): the azimuthal integration in McCulloch (2013) and Giné & McCulloch (2016) over [0, π] gives "a incorrect numerical factor"; and the energy-density calculation in McCulloch (2007, 2013) and Giné & McCulloch (2016) is "not properly justified", because the volume V should be that of the space (a Planck volume, via causal-set discreteness), not that of the particle.
- Inertia here is ascribed to the anisotropic pressure of fluctuations beyond the Rindler horizon, "rather than Unruh radiation on its own", which is described as isotropic and extremely faint (p. 4).
- Footnote 3 (p. 4) explains why the plate Casimir effect is weak while the Rindler-scale one gives macroscopic inertia: the Planck-size parts of the plates play no role, whereas in inertia every resonant part contributes.
- Conclusions (p. 5): the two frameworks "are consistent as regards the resulting expressions for inertia". Open questions: circular orbits (no clear rotational analogue of a Rindler horizon), the equivalence principle, GUP corrections, and non-thermal Unruh spectra.

## Key equations
Transcribed from the PDF (pp. 2–4). The calligraphic force symbol is written F here.

Model 1 (HUP):
$$\Delta x\,\Delta p \simeq \frac{\hbar}{2} \;\Longrightarrow\; \Delta E \simeq \frac{\hbar c}{2\Delta x} \qquad (1)$$
$$F(r) = -\frac{\partial(\Delta E)}{\partial r} \simeq \frac{\hbar c}{2r^2} \qquad (2)$$
$$E = \int_{\ell_p}^{r_e} F(r)\,dr \simeq \frac{\hbar c}{2}\left(\frac{1}{\ell_p} - \frac{1}{r_e}\right) \simeq \frac{\hbar c}{2\ell_p} \qquad (3)$$
$$n \simeq \frac{r_s}{\ell_p} = \frac{2M}{m_p} \;\;(4), \qquad M \simeq n\frac{m_p}{2} \;\;(5), \qquad n = \sqrt{N} \;\;(6), \qquad n\frac{E}{c^2} \simeq n\frac{m_p}{2} = M \;\;(7)$$

Entropy (eqs. 8–11):
$$S_{bh} = \log\xi_{bh}^N \simeq N = n^2 \;\;(8), \qquad S = N\log(\rho_{bh}\xi_{bh}/\rho) \simeq n^2\left[1 + \log(\rho_{bh}/\rho)\right] \;\;(11)$$

Model 2 (Rindler-scale Casimir effect):
$$T_U = \frac{\hbar a}{2\pi c} \;\;(12), \qquad F = \frac{uA}{3} \;\;(13), \qquad dF_x = \frac{(u_{left} - u_{right})A\cos\theta}{3} \;\;(14)$$
$$u_{left} = u\left(1 - \lambda_U^{peak}\frac{a\cos\theta}{8c^2}\right) \;\;(15), \qquad dF_x = -\frac{u\lambda_U^{peak}A\cos^2\theta}{24c^2}\,a \;\;(16)$$

Integrating φ from −θ to θ and θ over (0, π/2), doubled:
$$F_x = -\frac{(\pi^2 - 4)}{96}\frac{u\lambda_U^{peak}A}{c^2}\,a \qquad (17)$$

With T ≤ T_U (eq. 18), λ_p^peak = kλ_U^peak (k ≳ 1), u = E/V ≃ hc/(kλ_U^peak V) (eq. 19), V ≃ (4/3)πℓ_p³ and A ≃ 2πℓ_p²:
$$F_x \simeq -\frac{(\pi^2 - 4)\pi\, m_p}{32k}\,a \simeq -\frac{0.6\,m_p}{k}\,a \;\;(20), \qquad M \simeq n\frac{0.6\,m_p}{k} \;\;(21)$$

Matching eq. (21) to eq. (7) gives k ≃ 1.2.

Editorial check: uλA = (hc/kλV)·λ·A = 3πħc/(kℓ_p) = 3π m_p c²/k, so eq. (17) gives (π² − 4)π m_p a/(32k) ✓; (π² − 4)π/32 ≈ 0.576 ≈ 0.6 ✓; 0.576/0.5 ≈ 1.15 ≈ 1.2 ✓.

## Data used
- None (theoretical). No observational data or numerical fits.

## Results & predictions
- Both models give an inertial mass proportional to the number n of Planck-size parts: M ≃ n m_p/2 (Model 1) and M ≃ 0.6 n m_p/k (Model 2). Agreement requires k ≃ 1.2, which the authors read as the dominant fluctuation wavelength being λ_p^peak ≃ 1.2 λ_U^peak > λ_U^peak, consistent with their bound λ_p ≥ λ_U (p. 4).
- No new quantitative predictions or observational tests are given. Because the Hubble-scale term is neglected, the paper makes no statement about QI's low-acceleration anomalies (galaxy rotation, Pioneer, etc.).
- Editorial check: the single numerical factor k is fixed by requiring the two models to agree, so their "consistency" is partly by construction at the level of the O(1) prefactor; the shared scaling M ∝ n m_p follows from both models assigning roughly one Planck mass per resonant part, which is close to the definition n ≃ 2M/m_p in eq. (4).

## Figures
![Fig. 1 — Schematic of the Rindler-scale Casimir picture: a body accelerating rightwards sees a Rindler horizon at distance c²/a to its left; the net inertial force comes from fluctuations beyond c²/a on the right. θ is the integration angle in the (x, y)-plane, φ the azimuth. Eqs. (10)–(15) and the discussion of Renda (2019) are on the same page. (PDF p. 3.)](figures/fig-1-rindler-casimir.png)

## Notable quotes
> "the asymmetric (Casimir-like) damping of the radiation experienced by an accelerated object due to the appearance of a Rindler horizon" (p. 1, abstract)

> "the computation of the energy density carried out in Refs. [10,20,21] is not properly justified, since the volume V that appears in Eq. (19) is not the volume of the particle" (p. 4)

> "In spite of the underlying differences, the two frameworks are consistent as regards the resulting expressions for inertia." (p. 5)

## Criticisms & responses
- No published critique of this specific paper was found in a brief search. Crossref listed 5 citing works as of 2026-10.
- **Context from the reference list:** the paper cites McCulloch 2007 (Pioneer), McCulloch 2013 (asymmetric Casimir), Giné & McCulloch 2016, the Haisch–Rueda–Puthoff zero-point-field inertia programme and Levin's 2009 critical analysis of it, and [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md). It notes that both the HRP and QI approaches "have been partly criticized [11,12]" (p. 1).
- **Response to Renda (2019), in the paper:** Renda argued that McCulloch's damping formula (eq. 15 here) is incorrect around a_p ≃ 10⁻⁹ m/s², based on a discrete vs continuous Planck-law calculation. The authors reply that for a ≪ a_p and a ≫ a_p Renda's result behaves approximately like eq. (15), which they say justifies its use at the high accelerations considered here (p. 3); and that Renda's analysis omits space-time discretisation and therefore concludes the peak-wavelength contribution tends to zero at large accelerations (p. 4). Editorial note: this sidesteps rather than answers Renda's point for QI's anomalies, which live near a ~ 10⁻¹⁰–10⁻⁹ m/s², the regime this paper excludes.
- **Self-correction of QI derivations:** the paper itself states that McCulloch's (2013) and Giné & McCulloch's (2016) integration range gives a wrong numerical factor and that their energy-density volume is not properly justified (p. 4). Giné is a frequent McCulloch co-author, so this is not independent support, but it is an internal correction worth noting.
- The paper's own assumptions are heuristic: the Planck-size resonant parts, the "completely inelastic collision" model (described as one that "must be confirmed by further works", p. 2), ξ ≃ κ/ρ, and the hemispherical Rindler horizon.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources: [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md), [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md), [2020-gine-luciano-eup-modified-inertia](../2020-gine-luciano-eup-modified-inertia/README.md), [2017-gine-inertial-mass-holographic](../2017-gine-inertial-mass-holographic/README.md), [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md), [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md)
