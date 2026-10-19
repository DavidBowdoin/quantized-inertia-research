---
title: "A sceptical analysis of Quantized Inertia"
authors: [Michele Renda]
year: 2019
type: critique
venue: "Monthly Notices of the Royal Astronomical Society 489(1):881-885"
doi: 10.1093/mnras/stz2189
arxiv: 1908.01589
url: "https://arxiv.org/abs/1908.01589"
open_access: true
license: CC-BY-4.0
files: [paper.pdf, figures/fig-3-F-of-a.png, figures/fig-5-G-of-a.png]
status: critical
tags: [theory, derivation, unruh, casimir, critique, peer-reviewed]
---

# A sceptical analysis of Quantized Inertia

**Citation:** Renda, M. (2019). *A sceptical analysis of Quantized Inertia*. Monthly Notices of the Royal Astronomical Society, 489(1), 881–885. https://doi.org/10.1093/mnras/stz2189. arXiv:[1908.01589](https://arxiv.org/abs/1908.01589). The stored PDF is arXiv v1 (6 pages); page numbers below refer to it.

**TL;DR:** Renda (IFIN-HH, Romania, ATLAS group) re-examines the derivations in McCulloch (2007, MNRAS) and McCulloch (2013, EPL) and reports "two major flaws". (1) The linear F(a) factor in MiHsC is not what you get when you actually sum the discrete Unruh black-body spectrum allowed inside the Hubble-scale cavity. Doing that sum numerically gives a different F(a) with a peak (F ≈ 2.17) near 1.2 × 10⁻⁹ m s⁻². (2) The 2013 "asymmetric Casimir" inertia derivation puts all the Unruh energy into the peak wavelength. Renda shows that the peak mode carries almost none of the energy at ordinary accelerations. He does not test QI against data. He says the flaws, "if they do not invalidate, at least will require a major rethinking of the whole theory". This is the first critique of QI published in a peer-reviewed journal.

## Key claims
- **Recap of QI (Sect. 2):** QI makes two statements. (i) There is a minimum acceleration a₀ = 2c²/Θ ≈ 2 × 10⁻¹⁰ m s⁻². (ii) Inertia comes from an imbalance of Unruh radiation between the cosmic horizon and the Rindler horizon. Renda names QI's main strengths: no tunable parameters, a simple formulation and a wide range of phenomena. He names its main weakness: it relies on Unruh radiation, which has not been measured.
- **Flaw 1: F(a) (Sect. 3).** McCulloch (2007, sect. 2.2) asserts "using a not better specified direct calculation" that the ratio of discretely sampled to continuous Unruh radiance is a *linear* function of λ_peak. That ratio is 1 when λ_peak → 0 and 0 when λ_peak → 4Θ, which gives Eq. (7). Renda re-derives Planck's law for a cavity in which the wavelengths are comparable to the cavity size. He counts modes with l² + m² + n² = p² (OEIS A002102) instead of using the continuum approximation 4πp²dp/8. He then computes F = B_s/B numerically.
- **What the result shows:** F → 1 for a > 1 × 10⁻⁸ m s⁻² and F → 0 for a < a₀, both "as predicted by McCulloch (2007)". In between, F has a maximum F ≈ 2.17 at a_p ≈ 1.20 × 10⁻⁹ m s⁻². Renda notes this would act as a stable point for accelerations, and that "no such behaviour was ever measured or predicted theoretically by other models".
- **Flaw 2: the inertia derivation (Sect. 4).** McCulloch (2013, eqs. 9–10) and Giné & McCulloch (2016, eqs. 7–8) substitute the energy density u = E/V = hc/(λV). This assumes that only the peak wavelength of the Unruh spectrum contributes. Renda calls this "deeply incorrect" for classical accelerations (a > 1 × 10⁻⁸ m s⁻²). He defines G(a), the fraction of the total energy density in the mode nearest the peak, and shows that G → 0 at high acceleration (Fig. 5).
- **Scope (Conclusions):** Renda says explicitly that the paper does "not address the ability of Quantized Inertia to match the observational data". He argues that speculative physics is valuable and that conflict with the equivalence principle alone should not be the criterion for judging QI. Any new version, he says, needs "a stronger mathematical derivation" and a strategy for experimental verification.
- **Numerical choice:** H₀ = 2.3 ± 0.9 × 10⁻¹⁸ s⁻¹ is used, as in McCulloch (2007), so that results can be compared directly. This gives a Hubble diameter Θ = 2c/H₀ ≈ 2.607 × 10²⁶ m.

## Key equations
MiHsC modified inertia as recapitulated (Renda Eq. 7, from McCulloch 2007), with β = 1/a₅ ≈ 0.2:
$$ m_I = F(a)\,m_i = \left(1 - \frac{\beta \pi^2 c^2}{a\Theta}\right) m_i $$
The linear-ratio assumption being examined (Eq. 8):
$$ m_I = F(a)\,m_i = \frac{B_s(a)}{B(a)}\,m_i $$
Renda's discrete-spectrum result (Eq. 28), with N(p) the number of lattice modes with l² + m² + n² = p²:
$$ F(a) = \frac{30\pi^3 H_0^4 c^4}{a^4} \sum_{p^2=1}^{\infty} \frac{N(p)\,p}{e^{p\pi c H_0/a} - 1} $$
QI inertial force from McCulloch (2013) / Giné & McCulloch (2016), as quoted (Eq. 29):
$$ F = -\frac{\pi^2 h A}{48 c V}\,a $$
The substitution being criticised (Eq. 30):
$$ u = \frac{E}{V} = \frac{hc}{\lambda V} $$
The peak-mode energy fraction, which goes to zero at classical accelerations (Eq. 31):
$$ G(a) = \frac{u_s(p', a)}{U_s(a)} $$

## Data used
- None observational. The paper is a theoretical and numerical re-derivation. Mode counts come from OEIS sequence A002102, and the numerical sums were evaluated across a range of accelerations (plots made with Bokeh).

## Results & predictions
- Re-derived F(a): F = 1 for a > 1 × 10⁻⁸ m s⁻²; F = 0 for a < a₀ ≈ 2 × 10⁻¹⁰ m s⁻²; maximum F ≈ 2.17 at a_p ≈ 1.20 × 10⁻⁹ m s⁻² (p. 4, Fig. 3).
- Giné & McCulloch (2016) obtained a mass of 2.799 × 10⁻⁸ kg for a Planck-length cube, 29% above the Planck mass of 2.176 × 10⁻⁸ kg. Renda quotes this result and argues that it rests on the peak-only substitution (p. 4).
- G(a) is close to 1 at very low accelerations, where only a few modes are allowed, and tends to zero at higher accelerations (Fig. 5).
- No new observational prediction is tested. The paper only shows that the original derivation does not reproduce Eq. (7).

## Figures
![Fig. 3 — F(a) = B_s(a)/B(a) for low accelerations from Renda's discrete-mode sum: F → 1 at high a, F → 0 as a → 0, with a peak near a_p ≈ 1.2 × 10⁻⁹ m s⁻². Marks show where the calculation was performed. (Rendered page 4 of the arXiv PDF, which also shows Figs. 2b and 4.)](figures/fig-3-F-of-a.png)

![Fig. 5 — G(a), the fraction of the total Unruh energy density carried by the mode nearest the peak wavelength. It is close to 1 at low accelerations and tends to zero at classical accelerations, which is the basis for "Correction 2". (Rendered page 5 of the arXiv PDF.)](figures/fig-5-G-of-a.png)

## Notable quotes
> "Two major flaws were found in the original derivation." (p. 1, abstract)

> "In this substitution, the authors imply that only the peak wavelength of the Unruh spectrum contributes to the energy densities. In reality, this is deeply incorrect" (p. 4)

> "Such flaws, if they do not invalidate, at least will require a major rethinking of the whole theory." (p. 5)

## Criticisms & responses
- **McCulloch's responses (blog only; no peer-reviewed reply found).** In "Physics with an Edge & Thank Yous" (17 May 2020) McCulloch thanks "M. Renda (who wrote the first serious criticism of QI - very useful to me)" ([blog](https://physicsfromtheedge.blogspot.com/2020/05/physics-with-edge.html)). In "Responding to Criticisms" (30 Aug 2026), under the heading "The Maths is Wrong", he writes that Renda "usefully pointed out some shortcoming of my previous derivations of QI in which I failed to consider the whole Unruh spectrum, and only looked at the peak, so I responded by deriving the same formula in a more robust manner from the uncertainty principle (see my 2024 book) and the erasure of information by horizons (see my 2020 paper and 2024 book)" ([blog](https://physicsfromtheedge.blogspot.com/2026/08/responding-to-criticisms.html)). In other words, McCulloch accepts the specific point about the peak wavelength. His response is to point to alternative derivations of the same formula rather than to defend the 2007 and 2013 Unruh-spectrum calculations.
- **Do the alternative derivations answer Renda?** These derivations are [McCulloch 2020, information theory](../../01-papers/2020-mcculloch-information-theory/README.md), the uncertainty-principle derivations with Giné ([2018-gine-casimir-uncertainty](../../01-papers/2018-gine-casimir-uncertainty/README.md), [2018-gine-hawking-unruh-uncertainty](../../01-papers/2018-gine-hawking-unruh-uncertainty/README.md)), and [Haug & McCulloch 2018](../../01-papers/2018-haug-mcculloch-derivation/README.md). They do not use the discrete Unruh-spectrum sum that Renda re-computed. Neither Renda nor any other author located for this entry has published an assessment of whether they avoid his objections.
  > [!UNVERIFIED] Whether Renda (or MNRAS) received or published any formal reply; none was found in MNRAS or on arXiv.
- **Follow-up critique:** [Dickmann & Dickmann 2023](../2023-dickmann-casimir-contradicts/README.md) builds directly on Renda's mode sum. They argue that once all modes are summed, the net Unruh-pressure force scales as a⁴ rather than a, which contradicts Newton's second law.
- **Context:** Renda cites Koberlein (2017, Forbes) as the only earlier criticism, from outside peer-reviewed journals; see [2017-koberlein-doing-it-wrong](../../07-media/2017-koberlein-doing-it-wrong/README.md).

## Related
- Evidence: [derivation](../../02-evidence/derivation.md), [pioneer-anomaly](../../02-evidence/pioneer-anomaly.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources critiqued: [2007-mcculloch-pioneer-anomaly](../../01-papers/2007-mcculloch-pioneer-anomaly/README.md), [2013-mcculloch-asymmetric-casimir](../../01-papers/2013-mcculloch-asymmetric-casimir/README.md), [2016-gine-unruh-temperatures](../../01-papers/2016-gine-unruh-temperatures/README.md)
- Later derivations offered in response: [2020-mcculloch-information-theory](../../01-papers/2020-mcculloch-information-theory/README.md), [2018-gine-casimir-uncertainty](../../01-papers/2018-gine-casimir-uncertainty/README.md), [2018-haug-mcculloch-derivation](../../01-papers/2018-haug-mcculloch-derivation/README.md), [2024-mcculloch-quantised-accelerations](../../07-media/2024-mcculloch-quantised-accelerations/README.md)
- Other critiques: [2023-dickmann-casimir-contradicts](../2023-dickmann-casimir-contradicts/README.md), [2017-koberlein-doing-it-wrong](../../07-media/2017-koberlein-doing-it-wrong/README.md)
