---
title: "Equivalence principle"
tags: [context, general-relativity, inertial-mass, gravitational-mass, experimental-tests]
related: [machs-principle.md, sed-inertia.md, mond.md, dark-matter.md, conservation-of-momentum.md]
---

# Equivalence principle

## Plain-language explanation

The **weak equivalence principle (WEP)** says that all bodies fall with the same acceleration in a gravitational field, regardless of composition or mass. Equivalently, **inertial mass** $m_i$ (resistance to acceleration in $F = m_i a$) equals **passive gravitational mass** $m_g$ (what gravity pulls on). Einstein elevated this into the **Einstein equivalence principle** (local physics in free fall is that of special relativity), the foundation of general relativity, and the **strong equivalence principle** extends it to gravitationally bound bodies.

## Key equations

$$
m_i\,\mathbf a = m_g\,\mathbf g \quad\Rightarrow\quad \mathbf a = \frac{m_g}{m_i}\mathbf g
$$

Eötvös parameter comparing two bodies A and B:

$$
\eta(A,B) = 2\,\frac{|a_A - a_B|}{|a_A + a_B|}
$$

Best limits: torsion balances (Eöt-Wash, Schlamminger et al. 2008) $\eta \lesssim 2\times10^{-13}$; the MICROSCOPE satellite (Touboul et al. 2022) $\eta = [-1.5 \pm 2.3\,(\text{stat}) \pm 1.5\,(\text{syst})]\times10^{-15}$.

## Mainstream status

One of the best-tested principles in physics. Violations are searched for as signals of new physics (e.g. string-inspired scalar fields), but none has been found. Note that these tests are performed at accelerations far above $10^{-10}\ \mathrm{m\,s^{-2}}$ and test *composition* dependence.

## How it relates to QI

QI modifies **inertial mass only**: $m_i = m_g\,(1 - 2c^2/|a|\Theta)$. So QI explicitly **violates the WEP in an acceleration-dependent way**: the ratio $m_g/m_i$ depends on the body's acceleration (relative to a frame that QI must specify). Consequences:

- At laboratory and Solar-System accelerations $|a| \gg 2c^2/\Theta \sim 10^{-10}\ \mathrm{m\,s^{-2}}$, the correction is tiny (~$2\times10^{-11}$ at $a = 9.8\ \mathrm{m\,s^{-2}}$ with $\Theta = 8.8\times10^{26}$ m). Because it depends on acceleration rather than composition, two test masses in the same field get the same correction, so Eötvös/MICROSCOPE-type composition tests do not directly constrain it.
- At very low accelerations (galaxy outskirts, wide binaries) the violation is large; that is how QI produces MOND-like dynamics.
- Which acceleration enters QI (relative to what?) is a recurring point. In flyby and Tajmar-effect papers McCulloch uses accelerations relative to local matter (e.g. the spinning Earth or ring; [2008 flybys](../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md), [2011 Tajmar effect](../01-papers/2011-mcculloch-tajmar-effect/README.md)), which introduces model choices.
- Light: a photon has no rest mass, yet QI papers attribute inertial mass to photons in cavities ([emdrive papers](../01-papers/2015-mcculloch-emdrive-epl/README.md)). How this is reconciled with the Einstein equivalence principle and with GR's description of light propagation is not resolved in mainstream terms.
- The Dickmann & Dickmann critique argues the QI inertia modification is inconsistent with classical inertia ([criticism](../03-criticism/2023-dickmann-casimir-contradicts/README.md)).

Milgrom's modified-inertia MOND has the same structural feature; see [mond.md](mond.md).

## References

- Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Rev. Relativ.* 17, 4. https://doi.org/10.12942/lrr-2014-4
- Schlamminger, S. et al. (2008). Test of the equivalence principle using a rotating torsion balance. *Phys. Rev. Lett.* 100, 041101. https://doi.org/10.1103/PhysRevLett.100.041101
- Touboul, P. et al. (MICROSCOPE) (2022). MICROSCOPE mission: final results of the test of the equivalence principle. *Phys. Rev. Lett.* 129, 121102. https://doi.org/10.1103/PhysRevLett.129.121102
- Wikipedia: Equivalence principle. https://en.wikipedia.org/wiki/Equivalence_principle
