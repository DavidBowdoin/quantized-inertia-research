---
title: "Deriving quantised inertia using horizon-widths in the uncertainty principle"
authors: [Michael Edward McCulloch, Jaume Giné]
year: 2020
type: paper
venue: "Advanced Studies in Theoretical Physics 14(1), 1-8"
doi: 10.12988/astp.2020.9416
arxiv:
url: "https://doi.org/10.12988/astp.2020.9416"
open_access: true
license: CC-BY-NC-ND
files: [paper.pdf]
status: supports
tags: [coauthored-with-mcculloch, derivation, uncertainty-principle]
---

# Deriving quantised inertia using horizon-widths in the uncertainty principle

**Citation:** McCulloch, M. E. & Giné, J. (2020). *Deriving quantised inertia using horizon-widths in the uncertainty principle*. Advanced Studies in Theoretical Physics, 14(1), 1–8. Hikari Ltd. https://doi.org/10.12988/astp.2020.9416 (received 12 May 2019, published 14 July 2019; CC BY-NC-ND). PDF from the publisher: https://www.m-hikari.com/astp/astp2020/astp1-4-2020/p/gineASTP1-4-2020.pdf

**TL;DR:** The paper refines McCulloch's 2016 uncertainty-principle derivation of QI. That earlier version came out 26% too large. Here the position uncertainty Δx is taken as the *half-circumference (width)* of each horizon, π × radius, following Giné 2018, rather than the horizon distance. With that change the derivation recovers m_i = m(1 − 2c²/aΘ) exactly. The paper also notes that this formula equals the first two terms of the series expansion of MoND's "simple" interpolation function, with a₀ = 2c²/Θ.

## Key claims
- Inertia comes from gradients in the Unruh-radiation energy seen by an accelerating object, and the uncertainty principle fixes that energy.
- The relevant Δx is the uncertainty in the "crossing point" of a horizon, taken as half its circumference: πc²/a for the Rindler horizon and πΘ/2 for the cosmic horizon.
- This gives QI "exactly", improving on the 26% overestimate of McCulloch (2016, EPL 115, 69001).
- QI matches the first two terms of the Maclaurin expansion of the simple MoND function, with MoND's free a₀ replaced by 2c²/Θ.
- The introduction notes that Milgrom (1999) concluded Unruh radiation could not cause inertia because it is isotropic, and calls the Haisch–Rueda–Puthoff zero-point-field model "unconvincing" because it needs an arbitrary cutoff.

## Key equations
$$ \Delta p\,\Delta x \sim \frac{\hbar}{2}, \qquad \Delta E\,\Delta x \sim \frac{\hbar c}{2} $$
$$ \Delta E = \frac{\hbar c}{2}\left(\frac{1}{\Delta x_2} - \frac{1}{\Delta x_1}\right) $$
With horizon half-circumferences $\pi c^2/a$ (Rindler) and $\pi\Theta/2$ (cosmic):
$$ \Delta E = \frac{\hbar c}{2}\left(\frac{a}{\pi c^2} - \frac{2}{\pi\Theta}\right) = \frac{\hbar a}{2\pi c}\left(1 - \frac{2c^2}{a\Theta}\right) $$
Unruh temperature, then scaling to N photons:
$$ T = \frac{\hbar a}{2\pi c k_B}, \qquad \Delta E_p = E_p\left(1 - \frac{2c^2}{a\Theta}\right), \qquad \Delta m = m\left(1 - \frac{2c^2}{a\Theta}\right) $$
MoND comparison:
$$ m_i = m\left(\frac{1}{1 + a_0/a}\right) = m\left(1 - \frac{a_0}{a} + \frac{a_0^2}{a^2} - \dots\right) $$
(The last term is printed as "− a₀²/a²" in the PDF. The Maclaurin series of 1/(1+x) has +x² as its second-order term.)

## Data used
- None. A purely theoretical derivation.

## Results & predictions
- Recovers QI's Eq. 1 with no adjustable parameter. The implied MoND acceleration scale is a₀ = 2c²/Θ.
- No new numerical predictions. Galaxy rotation and cosmic acceleration are referred to earlier papers.

## Figures
None (the paper contains no figures).

## Notable quotes
> "quantised inertia … can be derived exactly and simply by assuming that the property of inertia is caused by gradients in the energy in the Unruh radiation field" (abstract, p. 1)

> "[22] derived a formula close to Eq. 1 (quantised inertia) by using relativistic horizons in the uncertainty principle but the expression derived was 26% too large." (p. 3)

> "quantised inertia predicts an expression close to the simple empirical interpolation function used in MoND." (p. 6)

## Criticisms & responses
- McCulloch's later paper [2020-mcculloch-information-theory](../2020-mcculloch-information-theory/README.md) says of this approach that "there is no good justification for using the width instead of the area".
- Factual notes: the choice of half-circumference for Δx is adopted from Giné (2018) rather than derived. The labels Δx₁ and Δx₂ are swapped partway through Section 2 of the text. As printed, the MoND series in Eq. 15 has a sign error in the a₀²/a² term. These points do not change the first-order result.
- The general critique of QI's uncertainty-principle reasoning and its claimed MoND equivalence is in [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md).
- Venue: Hikari Ltd journals have been listed on Beall's list of potential predatory publishers. > [!UNVERIFIED] The current status of this specific journal was not checked.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md)
- Sources: [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md), [2018-gine-hawking-unruh-uncertainty](../2018-gine-hawking-unruh-uncertainty/README.md), [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md), [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md), [2017-mcculloch-information-loss](../2017-mcculloch-information-loss/README.md), [2020-gine-luciano-eup-modified-inertia](../2020-gine-luciano-eup-modified-inertia/README.md), [2014-mcculloch-gravity-uncertainty](../2014-mcculloch-gravity-uncertainty/README.md)
