---
title: "Modified inertia from extended uncertainty principle(s) and its relation to MoND"
authors: [Jaume Giné, Giuseppe Gaetano Luciano]
year: 2020
type: paper
venue: "European Physical Journal C 80:1039"
doi: 10.1140/epjc/s10052-020-08636-x
arxiv:
url: "https://doi.org/10.1140/epjc/s10052-020-08636-x"
open_access: true
license: CC-BY-4.0
files: [paper.pdf, figures/fig-1-horizons-schematic.png]
status: supports
tags: [uncertainty-principle, mond, minimum-acceleration]
---

# Modified inertia from extended uncertainty principle(s) and its relation to MoND

**Citation:** Giné, J. & Luciano, G. G. (2020). *Modified inertia from extended uncertainty principle(s) and its relation to MoND*. European Physical Journal C, 80, 1039. https://doi.org/10.1140/epjc/s10052-020-08636-x (received 4 Aug 2020, accepted 30 Oct 2020; CC BY 4.0, SCOAP3). The stored PDF was downloaded from the Universitat de Lleida repository (hdl:10459.1/70036), because the publisher link is behind a bot check.

**TL;DR:** The paper first re-derives the QI formula m_I = m(1 − 2c²/aΘ) from the Heisenberg principle using horizon half-circumferences, following McCulloch & Giné 2020. It then replaces Heisenberg with two "extended uncertainty principles" (EUPs) that include a cosmological (de Sitter) length l_H. **Case I** (a quadratic correction, the natural (A)dS EUP) gives m_I = m[1 + (γπ²/2)(a_H/a)²]. This matches MoND's *standard* interpolating function if γ = −1/π² (de Sitter) and a₀ = a_H = c²/l_H. **Case II** (linear plus quadratic terms) gives the *linear* QI/simple-MoND form if α = 2/π. The authors conclude that modified inertia can be traced to cosmic accelerated expansion.

## Key claims
- QI's modified inertia can be "naturally derived" within the EUP framework, and is "a direct consequence of the minimal acceleration experienced by any body due to the cosmic expansion".
- In the HUP derivation, a₀ = 2c²/Θ matches QI to the MoND simple interpolating function at leading order.
- Case I (the de Sitter EUP) does **not** reproduce the linear QI correction. It gives a quadratic (a_H/a)² correction, consistent with MoND's standard interpolating function.
- Case II reproduces the linear correction. The authors caution that its EUP "arises from the first terms in the expansion of a metric which has no evident physical meaning" and so "should only be considered as a mathematical framework".
- Caveats from the authors: QI "is not given" as a full implementation, and it is difficult to obtain the inertial mass itself rather than a modification of it. The physical existence of Rindler horizons is "quite debated". EUP physics is "largely heuristic". The paper notes "some criticism (see Ref. [23])" of QI.

## Key equations
QI (Eq. 1), with Θ = 2R_U:
$$ m_I = m\left(1 - \frac{2c^2}{a\Theta}\right) $$
HUP derivation with $\Delta x_2 \sim \pi c^2/a$ and $\Delta x_1 \sim \pi\Theta/2$:
$$ \Delta E_p \sim \frac{\hbar c}{2}\left(\frac{1}{\Delta x_2} - \frac{1}{\Delta x_1}\right) \sim K_B T_U\left(1 - \frac{2c^2}{a\Theta}\right), \qquad T_U = \frac{\hbar a}{2\pi c K_B} $$
Case I EUP and its result:
$$ \Delta x\,\Delta p \sim \frac{\hbar}{2}\left(1 + \gamma\frac{\Delta x^2}{l_H^2}\right) \;\Rightarrow\; m_I \sim m\left[1 + \frac{\gamma\pi^2}{2}\left(\frac{a_H}{a}\right)^2\right], \quad \gamma = -\frac{1}{\pi^2} $$
Equivalent form in terms of Λ:
$$ m_I \sim m\left(1 - \frac{1}{2}\frac{c^4\Lambda}{a^2}\right) $$
Case II EUP and its result:
$$ \Delta x\,\Delta p \sim \frac{\hbar}{2}\left(1 - \frac{\alpha}{2}\frac{\Delta x}{l_H} + \frac{3\alpha^2}{2}\frac{\Delta x^2}{l_H^2}\right) \;\Rightarrow\; m_I \sim m\left[1 - \frac{\alpha\pi}{2}\frac{a_H}{a} + \frac{3\alpha^2\pi^2}{2}\left(\frac{a_H}{a}\right)^2\right], \quad \alpha = \frac{2}{\pi} $$

## Data used
- None. A theoretical paper. The only numerical inputs are Λ ∼ 10⁻⁵² m⁻² and illustrative accelerations.

## Results & predictions
- For terrestrial a ∼ 10 m/s², (m_I − m)/m ∼ O(10⁻²¹), "below the current experimental sensitivity".
- For a ∼ 10⁻⁹ m/s² (galaxy edges or dwarf galaxies), (m_I − m)/m ∼ O(10⁻¹).
- MoND's a₀ is identified with the cosmic background acceleration a_H = c²/l_H.
- The authors suggest that future observations could distinguish a linear (Case II / QI) from a quadratic (Case I) dependence on 1/a. They also mention metamaterial "artificial event horizons" as a possible test route.

## Figures
![Fig. 1 — Schematic of quantized inertia: a body accelerating rightward sees the cosmic horizon at Θ/2 on its right and a Rindler horizon at c²/a on its left. Fluctuations from the unbalanced strip produce a net force opposing the acceleration. (Rendered page 3.)](figures/fig-1-horizons-schematic.png)

## Notable quotes
> "We prove that modified inertia is a direct consequence of the minimal acceleration experienced by any body due to the cosmic expansion." (abstract, p. 1)

> "the physical meaning of the latter is quite debated and its real existence often questioned" (on Rindler horizons, p. 7)

> "given that EUP physics is largely heuristic, one should keep any scenario open." (p. 7)

## Criticisms & responses
- The criticism the authors acknowledge, Ref. [23], is Renda 2019 (MNRAS 489, 881): [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md). The authors do not reply to its specific points.
- Factual notes: the physically motivated de Sitter EUP (Case I) gives a *quadratic* correction, unlike QI's linear one. The linear QI form needs the Case II EUP, whose underlying metric the authors call physically unclear. Both cases fix their deformation parameter (γ or α) by matching to MoND rather than deriving it.
- > [!UNVERIFIED] A brief search found no independent published critique of this specific paper.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md)
- Sources: [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md) (the HUP derivation reviewed in Sect. 2), [2018-gine-hawking-unruh-uncertainty](../2018-gine-hawking-unruh-uncertainty/README.md) (the half-circumference Δx), [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md), [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md), [2007-mcculloch-pioneer-anomaly](../2007-mcculloch-pioneer-anomaly/README.md), [2021-gine-luciano-inertia-fluctuations](../2021-gine-luciano-inertia-fluctuations/README.md), [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md)
