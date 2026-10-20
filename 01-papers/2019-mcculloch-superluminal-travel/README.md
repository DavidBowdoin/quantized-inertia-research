---
title: "Superluminal Travel from Quantised Inertia"
authors: [Michael Edward McCulloch]
year: 2019
type: paper
venue: "Journal of Space Exploration 8(2), 1-6"
doi:
arxiv:
url: "https://www.tsijournals.com/articles/superluminal-travel-from-quantised-inertia-13969.html"
open_access: true
license: all-rights-reserved
files: [paper.pdf]
status: supports
tags: [propulsion, faster-than-light, minimum-acceleration, special-relativity, galactic-jets, metamaterials, darpa]
---

# Superluminal Travel from Quantised Inertia

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [source](https://www.tsijournals.com/articles/superluminal-travel-from-quantised-inertia-13969.html).

**Citation:** McCulloch, M. E. (2019). *Superluminal Travel from Quantised Inertia*. Journal of Space Exploration, 8(2), 158 (pp. 1–6). Trade Science Inc. ISSN 2319-9822. https://www.tsijournals.com/articles/superluminal-travel-from-quantised-inertia-13969.html (received 27 May 2019, accepted 3 June 2019, published 12 June 2019). No DOI was found (Crossref has no record; OpenAlex W2953639584 lists vol. 8, issue 2, pp. 1–6 and no DOI).

**About the stored PDF:** `paper.pdf` is the 6-page publisher PDF, downloaded from the link in the [quantizedinertia.com papers list](../../07-media/2023-quantizedinertia-website/README.md) (`https://www.tsijournals.com/articles/superluminal-travel-from-quantised-inertia.pdf`). Its footer reads "©2019 Trade Science Inc." and it carries no Creative Commons or other licence statement, so it is recorded as all-rights-reserved (same publisher and treatment as [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md)). The acknowledgment credits DARPA grant HR001118C0125 (p. 6). The PDF has no figures, only one table (p. 5).

**TL;DR:** McCulloch combines the special-relativistic inertial mass m₀/√(1−v²/c²) with QI's factor (1 − 2c²/aΘ). Solving for the acceleration leaves a residual term 2c²/Θ ≈ 2 × 10⁻¹⁰ m s⁻² that survives even at v = c. He argues that this means the light-speed limit "can be broken", though only at that tiny rate. He suggests that the apparent 6c motion in the M87 jet may be real superluminal motion, and that a ship could raise the residual acceleration by surrounding itself with a much smaller artificial horizon (metamaterials, fast spin, or anti-phase radiation).

## Key claims
- At low accelerations Unruh waves no longer fit inside the cosmic diameter Θ, so inertia "dissipates". Where special relativity makes inertia infinite at c, QI leaves a "relativity-proof" minimum acceleration 2c²/Θ (pp. 3–4).
- This minimum acceleration is the observed cosmic acceleration (Perlmutter, Riess), attributed to dark energy "but, as shown here, it is predicted by QI" (p. 4).
- QI effects would be undetectable in particle accelerators, because circulating particles are highly accelerated: at v = 0.9c at CERN the QI term is "22 orders of magnitude smaller" than the relativistic one (p. 4).
- Objects may lose inertia along the spin axes of galaxies, as QI says flyby craft do near Earth's polar axis. The M87 jet's apparent 6c speed implies real speeds above c unless the jet lies within about 20° of the line of sight, which Biretta et al. call problematic (pp. 4–5, Table 1).
- Engine concepts (p. 5): replace Θ by a much smaller horizon "bubble" around the ship, made with metamaterials that bend the electromagnetic part of the Unruh waves; create a "Rindler-cylinder" by fast spin; or cancel the Unruh waves with emitted anti-phase radiation. Damping the vacuum in front of the ship would also give a forward push without the fuel needed to counter relativistic mass.
- Open problems acknowledged by the author (p. 5): how such long Unruh waves interact with matter and "feel the distant Hubble scale quickly enough"; a discrete rather than smooth treatment of allowed wavelengths; and causality, which "have not yet been considered". He says the most useful step would be isolating QI in a laboratory experiment.

## Key equations
QI inertial mass (Eq. 4), with Θ = 8.8 × 10²⁶ m (the post-2017 value; see [equations](../../00-overview/equations.md)):
$$ m_i = m_g\left(1 - \frac{2c^2}{a\Theta}\right) $$
Combined with special relativity (Eq. 9):
$$ m_i = m_0\,\frac{1 - 2c^2/(a\Theta)}{\sqrt{1 - v^2/c^2}} $$
Solving F = m_i a for a (Eq. 11):
$$ a = \frac{F}{m_0}\sqrt{1 - \frac{v^2}{c^2}} + \frac{2c^2}{\Theta} $$
Wavelength of the Unruh radiation, from Unruh's temperature and Wien's law with β = 0.2 (Eq. 3):
$$ \lambda = \frac{4\beta\pi^2 c^2}{a} $$
Apparent speed of a relativistic jet at angle θ to the line of sight (Eq. 15): $v_{app} = v\sin\theta/(1-\cos\theta)$.

## Data used
- CERN: ring radius r = 4 km, acceleration a = v²/r (Eqs. 12–14).
- M87 jet: apparent speed 6c and a most likely angle to the line of sight of 64° (printed "64.5π", apparently a garbled degree sign), from Biretta, Sparks & Macchetto (1999).
- Flyby formula dv = 2.8 × 10⁻⁷ v (cos φ₁ − cos φ₂)/(cos φ₁ cos φ₂), quoted from [2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md).

## Results & predictions
| Assumed angle of the M87 jet | Real speed implied by 6c apparent (Table 1, p. 5) |
|---|---|
| 64° | 3.7c |
| 30° | 1.6c |
| 20° | 1.05c |

- Residual acceleration 2c²/Θ ≈ 2 × 10⁻¹⁰ m s⁻². The paper says this takes a craft from 0 to 60 mph in 8500 years, and from 0 to c in the lifetime of the universe (p. 5).
- For a ship at 9.8 m s⁻² the Unruh wavelength is about 7 × 10¹⁶ m (Eq. 16).
- **Editorial checks** (our arithmetic, using the paper's inputs):
  - Eq. 11 follows algebraically from Eqs. 9–10. 2c²/Θ = 2.05 × 10⁻¹⁰ m s⁻² with Θ = 8.8 × 10²⁶ m. Eq. 13's 8.1 × 10⁻⁷ and Eq. 14's 5.6 × 10⁻¹⁸ reproduce, as do Table 1 (3.75c, 1.61c, 1.06c) and Eq. 16 (7.3 × 10¹⁶ m).
  - 60 mph (26.8 m s⁻¹) at 2.05 × 10⁻¹⁰ m s⁻² takes about 1.3 × 10¹¹ s ≈ 4,200 years, not 8,500. The 8,500-year figure corresponds to about 1 × 10⁻¹⁰ m s⁻². Reaching c takes about 4.6 × 10¹⁰ years, about 3 times the age of the universe, so "the lifetime of the universe" holds only to order of magnitude.
  - Eq. 14 uses the binomial approximation √(1−v²/c²) ≈ 1 − v²/2c², which is poor at v = 0.9c (0.44 exact vs 0.60). This does not change the "22 orders of magnitude" conclusion.
  - The abstract writes the minimum acceleration in "m/s" rather than m s⁻² (a typo; the body text uses m s⁻²).

## Figures
None. The PDF contains no figures, only Table 1 (p. 5), transcribed above.

## Notable quotes
> "This implies that the speed of light limit can be broken, albeit with this tiny acceleration" (abstract, p. 1)

> "it is possible that this is evidence for the FTL speeds implied by QI." (p. 5, on the M87 jet)

> "The consequences of the FTL discussed here for causality are complex, and have not yet been considered." (p. 5)

## Criticisms & responses
- No critique aimed specifically at this paper was found.
- **Status and venue (factual):** a single-author paper in a Trade Science Inc. journal. No independent analysis of the superluminal claim exists in this repository.
- **Mainstream reading of the M87 jet (editorial, from the paper's own references):** the paper itself notes that, per Rees (1966; cited as "Reiss"), apparent superluminal speeds can be a projection effect of relativistic motion. Its argument for real superluminal motion depends on the jet's angle to the line of sight. That angle is uncertain, and the paper acknowledges that it "may change" (p. 5).
- **The residual acceleration is the same 2c²/Θ term** whose match to the cosmic acceleration this repository rates as an author-only, order-of-magnitude coincidence ([cosmic-acceleration](../../02-evidence/cosmic-acceleration.md)).
- **Theory.** The equivalence-principle violation the paper concedes (p. 4), and the general derivation of the (1 − 2c²/aΘ) factor, are criticised in [Renda 2019](../../03-criticism/2019-renda-sceptical/README.md). See also [derivation](../../02-evidence/derivation.md).
- **Propulsion concepts.** None of the proposed horizon-engineering methods has been tested. QI's laboratory thrust predictions have so far given null results in controlled tests ([propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)).

## Related
- Evidence: [cosmic-acceleration](../../02-evidence/cosmic-acceleration.md), [propulsion](../../02-evidence/propulsion.md), [flyby-anomaly](../../02-evidence/flyby-anomaly.md), [derivation](../../02-evidence/derivation.md)
- Sources: [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md) (same journal), [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md), [2008-mcculloch-flyby-anomalies-jbis](../2008-mcculloch-flyby-anomalies-jbis/README.md), [2008-mcculloch-flyby-anomalies-mnras](../2008-mcculloch-flyby-anomalies-mnras/README.md), [2019-mcculloch-rindler-horizons](../2019-mcculloch-rindler-horizons/README.md), [2023-quantizedinertia-website](../../07-media/2023-quantizedinertia-website/README.md)
