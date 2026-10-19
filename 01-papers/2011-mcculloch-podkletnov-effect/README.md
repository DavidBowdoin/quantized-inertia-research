---
title: "Can the Podkletnov effect be explained by quantised inertia?"
authors: [Michael E. McCulloch]
year: 2011
type: paper
venue: "Physics Procedia 20, 134-139"
doi: 10.1016/j.phpro.2011.08.012
arxiv: "1108.3488"
url: "https://doi.org/10.1016/j.phpro.2011.08.012"
open_access: true
license: arXiv-nonexclusive
files: [paper.pdf, citation.bib, figures/fig-1-setup-schematic.png]
status: supports
tags: [podkletnov-effect, lab-test]
---

# Can the Podkletnov effect be explained by quantised inertia?

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`arXiv-nonexclusive`) does not permit redistribution. Read the paper at [arXiv:1108.3488](https://arxiv.org/abs/1108.3488) · [doi:10.1016/j.phpro.2011.08.012](https://doi.org/10.1016/j.phpro.2011.08.012).

**Citation:** McCulloch, M. E. (2011). *Can the Podkletnov effect be explained by quantised inertia?* Physics Procedia 20, 134-139 (SPESIF-2011 proceedings). [doi:10.1016/j.phpro.2011.08.012](https://doi.org/10.1016/j.phpro.2011.08.012) / [arXiv:1108.3488](https://arxiv.org/abs/1108.3488)

**TL;DR:** This paper applies MiHsC to Podkletnov's reported weight loss (0.05–0.07%) of test masses above an AC-driven, levitated, supercooled superconducting disc. Vibration of the disc raises the test mass's inertia, and conserving momentum then gives an upward acceleration of 0.0029 m/s² (0.03% of g). That is about half the reported effect. With the disc spinning at 5000 rpm, MiHsC predicts 0.042%, but Podkletnov reported 0.3–0.5%. The predicted increase from rotation is therefore 28 times too small.

> Text and page numbers are from arXiv v1 (Aug 2011), stored as `paper.pdf`. The arXiv text says that the doubling of the vibrational acceleration in the Physics Procedia version "is incorrect", so the two versions differ.

## Key claims
- The Podkletnov effect, as reported:
  - It is independent of test-mass composition.
  - It persists when the mass is encased in glass or shielded by a metal screen.
  - It is largest near the disc edge and during deceleration.
  - It "has so far been observed in only one laboratory".
- In MiHsC the test mass's inertia depends on the accelerations of its surroundings: the fixed stars, via the Earth's spin at Tampere (61.5° N), and the disc. Vibration and rotation of the disc raise that inertia, and momentum conservation produces an apparent upward force.
- The paper argues MiHsC does not show up in torsion-balance tests of the equivalence principle, because the rigidly connected balls have the same acceleration relative to distant masses.
- MiHsC predicts the effect should vanish outside the cryostat. The paper notes this "disagrees with the extended vertical column of the weight loss observed".
- The Tajmar-effect treatment (the gyroscope co-moves with the ring) and this treatment (the mass accelerates upward) "need to be checked further" for consistency.

## Key equations
MiHsC inertia, where a is the relative acceleration of surrounding matter:
$$ m_I = m\left(1 - \frac{2c^2}{a\Theta}\right) $$
Momentum conservation:
$$ dv = \frac{2c^2}{\Theta}\left(\frac{v_2}{a_2} - \frac{v_1}{a_1}\right) $$
Predicted anomalous upward acceleration, from disc rotation R (rpm), radius r and AC field B:
$$ da = \frac{2c^2}{\Theta}\left(\frac{4\pi^2 R^2 r}{3600\, a_s} + \frac{B^2 A}{2\mu_0 m a_s}\right) $$

## Data used
- Podkletnov (1997, arXiv:cond-mat/9701074) and Podkletnov & Nieminen (1992, *Physica C* 203:441).
- Inputs:
  - AC field B = 2 T; disc mass 0.95 kg; disc radius 0.135 m; rotation rate 5000 rpm.
  - a_s = 0.022 m/s²: 0.016 from the Earth's spin at 61.5° N plus 0.006 from its orbit.
- Error bars assume a 9% uncertainty in H.

## Results & predictions
- AC field only: da = 0.0029 ± 0.00025 m/s², i.e. 0.03% (±0.0025%) of g. Observed: 0.05–0.07%.
- AC field plus 5000 rpm: da = 0.0041 m/s², i.e. 0.042% of g. Observed: 0.3–0.5%. The rotational increase is underestimated by ~28×.
- Predicted to grow with disc radius, rotation rate, B², latitude (smaller a_s) and lower disc mass. The paper says it should also be possible without a superconductor.
- Predicted, but untested: test masses should appear slightly heavier during cooling.

## Figures
*Figure (local only): Fig. 1 — Schematic viewed from the North Pole: cryostat, disc and test mass rotating eastward with the Earth; when the test mass gains inertia by MiHsC it accelerates upward (da) (p. 8).*

## Notable quotes
> "The effect has so far been observed in only one laboratory." (p. 1)

> "However, for case 2 the predicted weight loss was 0.042%, an increase which is 28 times smaller than the extra weight loss observed." (p. 7)

> "According to MiHsC the anomalous effect should vanish outside the cryostat, which disagrees with the extended vertical column of the weight loss observed by [2]." (p. 6)

## Criticisms & responses
- **The effect being explained is unconfirmed.** Replication attempts cited in the paper itself did not find the effect, though the paper says they did not reproduce the conditions exactly:
  - Li, Noever, Robertson, Koczor & Brantley (1997, *Physica C* 281:260), a NASA Marshall static test.
  - Woods et al. (2001, AIAA 2001-3363).
- **Partial and inconsistent agreement.** The paper itself reports that it gets about half the static effect and is 28× too small for the rotational effect, and that the spatial extent is predicted wrongly.
- **Internal inconsistency in the published version.** The arXiv version says the Physics Procedia text's doubling of the vibrational acceleration is incorrect, so the published numbers may differ.
- > [!UNVERIFIED] The published Physics Procedia figures were not checked against the arXiv version.

## Related
- Evidence: [lab-tests](../../02-evidence/lab-tests.md), [other-anomalies](../../02-evidence/other-anomalies.md)
- Sources:
  - [2010-mcculloch-tajmar-effect-explained](../2010-mcculloch-tajmar-effect-explained/README.md)
  - [2011-mcculloch-tajmar-effect](../2011-mcculloch-tajmar-effect/README.md)
  - [2010-mcculloch-minimum-accelerations](../2010-mcculloch-minimum-accelerations/README.md)
