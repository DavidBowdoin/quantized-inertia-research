---
title: "Hawking effect and Unruh effect from the uncertainty principle"
authors: [Jaume Giné]
year: 2018
type: paper
venue: "EPL 121(1):10001"
doi: 10.1209/0295-5075/121/10001
arxiv:
url: "https://doi.org/10.1209/0295-5075/121/10001"
open_access: false
files: []
status: neutral
tags: [unruh, uncertainty-principle]
---

# Hawking effect and Unruh effect from the uncertainty principle

**Citation:** Giné, J. (2018). *Hawking effect and Unruh effect from the uncertainty principle*. EPL (Europhysics Letters), 121(1), 10001. https://doi.org/10.1209/0295-5075/121/10001 (received 30 Aug 2017, accepted 20 Nov 2017, published 1 Mar 2018).

**TL;DR:** A short heuristic derivation of the *exact* Hawking and Unruh temperatures from the Heisenberg uncertainty principle, by considering vacuum particle–antiparticle pairs that appear close to an event horizon. Later QI papers say its key move is to take the position uncertainty as the horizon's *half-circumference* (π × radius) rather than its distance. McCulloch & Giné (2020) and Giné & Luciano (2020) adopt this step to derive the QI inertia formula exactly.

> Paywalled. No PDF is stored. This summary is based on the abstract (OpenAlex / publisher metadata) and on how later open-access papers describe it.

## Key claims
- From the abstract: "The exact expressions of the Hawking temperature and Unruh temperature are deduced using the uncertainty principle of Heisenberg and the vacuum fluctuations that cause the appearance of a particle-antiparticle pair close to an event horizon."
- As described by [McCulloch & Giné 2020](../2020-mcculloch-horizon-widths/README.md): "The Hawking and Unruh temperatures were derived exactly with a similar method by [Giné 2018] with the new proposal that what is important is not the horizon distance but the half-circumference (width) of the horizon".
- As described by [Giné & Luciano 2020](../2020-gine-luciano-eup-modified-inertia/README.md): the Unruh temperature follows from the HUP by "setting Δx ∼ πc²/a, where we are assuming a form of half circumference for the Rindler horizon".

## Key equations
The target results are the standard ones. Their reconstruction from the HUP below follows Giné & Luciano 2020, Eqs. 2–4, not this paper directly:
$$ \Delta x\,\Delta E \sim \frac{\hbar c}{2}, \qquad \Delta x \sim \frac{\pi c^2}{a} \;\Rightarrow\; \Delta E \sim \frac{\hbar a}{2\pi c} = k_B T_U, \qquad T_U = \frac{\hbar a}{2\pi c k_B} $$
> [!UNVERIFIED] The exact form of the Hawking-temperature step in this paper (presumably Δx ∼ πR_s with surface gravity) was not checked against the full text.

## Data used
- None (theoretical).

## Results & predictions
- Reproduces the standard Hawking temperature T_H = ħc³/(8πGMk_B) and the Unruh temperature T_U = ħa/(2πck_B) exactly, according to the abstract's claim of "exact expressions". No new predictions are known.

## Figures
None (no PDF available).

## Notable quotes
> "The exact expressions of the Hawking temperature and Unruh temperature are deduced using the uncertainty principle of Heisenberg" (abstract)

## Criticisms & responses
- > [!UNVERIFIED] A brief search found no published critique that addresses this paper specifically.
- Context: heuristic uncertainty-principle derivations of T_H and T_U are known to reproduce the standard results only up to O(1) factors that depend on the choice of Δx. Here that choice (the half-circumference) fixes the factor of 2π. The same choice is what makes the later QI derivation "exact" (see [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md)). McCulloch's own 2020 information-theory paper says of that step that "there is no good justification for using the width instead of the area" ([2020-mcculloch-information-theory](../2020-mcculloch-information-theory/README.md)).
- Crossref lists McCulloch 2014 (Ap&SS, gravity from the uncertainty principle) and McCulloch 2016 (EPL 115, 69001) among its 15 references, which places it within the QI uncertainty-principle line of work.

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources: [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md), [2014-mcculloch-gravity-uncertainty](../2014-mcculloch-gravity-uncertainty/README.md), [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md) (the companion paper), [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md), [2020-gine-luciano-eup-modified-inertia](../2020-gine-luciano-eup-modified-inertia/README.md), [2016-gine-unruh-temperatures](../2016-gine-unruh-temperatures/README.md), [2019-kholupenko-unruh-anisotropy-1](../2019-kholupenko-unruh-anisotropy-1/README.md)
