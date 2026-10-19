---
title: "Gravity from the uncertainty principle"
authors: [Michael E. McCulloch]
year: 2014
type: paper
venue: "Astrophysics and Space Science 349(2), 957-959"
doi: 10.1007/s10509-013-1686-9
arxiv:
url: "https://doi.org/10.1007/s10509-013-1686-9"
open_access: false
files: [citation.bib]
status: supports
tags: [derivation, gravity]
---

# Gravity from the uncertainty principle

**Citation:** McCulloch, M. E. (2014). *Gravity from the uncertainty principle*. Astrophysics and Space Science 349(2), 957-959. Published online 7–8 Nov 2013; issue dated Feb 2014. [doi:10.1007/s10509-013-1686-9](https://doi.org/10.1007/s10509-013-1686-9)

**TL;DR:** A three-page paper that tries to derive Newton's inverse-square law from Heisenberg's uncertainty principle. As two orbiting bodies get closer, their position uncertainty shrinks, so their momentum uncertainty, and the force between them, must grow. Summing this over all pairs of Planck masses in the two bodies gives F = GMm/r². McCulloch's own 2016 follow-up says the final step "involves some circular reasoning", because the Planck mass is defined using G.

> PDF not retrievable: paywalled (Springer), and no arXiv version was found. The publisher page could not be fetched. The content below comes from (a) an abstract-level description in web search results, which is paraphrased and marked as such, and (b) McCulloch's own restatement of the derivation in the open-access follow-up [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md) (arXiv:1610.06787, pp. 3–4 and 8).

## Key claims
- > [!UNVERIFIED] Paraphrase of the publisher abstract, taken from search results and not read directly:
  - Newton's gravity law can be derived from the uncertainty principle.
  - As the distance between two bodies in mutual orbit decreases, their position uncertainty decreases, so momentum, and hence force, must increase.
  - Summing over interactions between Planck masses gives Newton's law.
  - Masses below the Planck mass should not feel gravity. A suggested test is an abrupt change in space-dust density at about the Planck mass.
- The 2016 follow-up (p. 4) states that "the inevitability of attraction was not discussed in [the 2014 paper]". The 2014 formalism could give either attraction or repulsion.

## Key equations
As restated by McCulloch (2016, arXiv:1610.06787, pp. 3–4) as the derivation of the 2014 paper. These equations have not been checked against the 2014 text.
$$ \Delta p\,\Delta x \sim \hbar, \qquad \Delta \bar E\,\Delta \bar x \sim \hbar c $$
$$ \Delta \bar E = \frac{\hbar c\, mM}{m_P^2\,\Delta \bar x} \quad\Rightarrow\quad F \sim \frac{\hbar c}{m_P^2}\frac{mM}{r^2} = \frac{GMm}{r^2} $$

## Data used
- None. This is a theoretical derivation.

## Results & predictions
- Newton's law, with G recovered only if the Planck mass m_P is inserted (and m_P is itself defined using G).
- > [!UNVERIFIED] Prediction, paraphrased from the abstract: no gravitational response for masses below the Planck mass (~2 × 10⁻⁸ kg). Crossref's reference list includes Nesvizhevsky et al. (2002) on quantum states of neutrons in Earth's gravity. That experiment shows that neutrons, far below the Planck mass, respond to gravity. Whether, and how, the paper addresses this is unverified.

## Figures
None (no PDF).

## Notable quotes
From the 2016 follow-up (not this paper):
> "…this last part of the derivation involves some circular reasoning since the Planck mass is defined using the value for G (this was not discussed in the precursor gravity paper, [21])." (McCulloch 2016, arXiv:1610.06787, p. 8; [21] = this paper)

## Criticisms & responses
- **Circularity (self-acknowledged).** See the quote above. The 2016 paper presents itself as extending and correcting this derivation, adding horizons and an argument for why the force is attractive. The repository summary describes the 2014 version as superseded by the 2016 one.
- **Supportive reinterpretation.** Haug (2018) argues the derivation has a deeper meaning in terms of Planck-mass "atomism"; see [2018-haug-mcculloch-derivation](../2018-haug-mcculloch-derivation/README.md).
- **Sub-Planck-mass gravity.** Neutrons and atoms, both far below the Planck mass, demonstrably fall in Earth's gravity, for example in neutron quantum-bounce experiments (Nesvizhevsky et al. 2002, *Nature* 415, 297). This challenges the prediction as paraphrased above.
  - > [!UNVERIFIED] This is an editorial observation based on the paper's cited literature; no published critique making this point specifically about this paper was located.
- Renda (2019) critiques QI's foundations in general; see [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources:
  - [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md)
  - [2018-haug-mcculloch-derivation](../2018-haug-mcculloch-derivation/README.md)
  - [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md)
  - [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md)
  - [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md)
