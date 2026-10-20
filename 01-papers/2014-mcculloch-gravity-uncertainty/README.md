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
license: all-rights-reserved
files: [paper.pdf, citation.bib]
status: supports
tags: [derivation, gravity]
---

# Gravity from the uncertainty principle

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`all-rights-reserved`) does not permit redistribution. Read the paper at [doi:10.1007/s10509-013-1686-9](https://doi.org/10.1007/s10509-013-1686-9).

**Citation:** McCulloch, M. E. (2014). *Gravity from the uncertainty principle*. Astrophysics and Space Science 349(2), 957-959. Received 22 Oct 2013, accepted 26 Oct 2013, published online Nov 2013; issue dated Feb 2014. [doi:10.1007/s10509-013-1686-9](https://doi.org/10.1007/s10509-013-1686-9)

**TL;DR:** A three-page paper that tries to derive Newton's inverse-square law from Heisenberg's uncertainty principle. It assumes that gravity acts only between whole Planck masses, gives each pair of Planck masses (one in each body) an uncertainty product of ħ, sets the position uncertainty equal to the orbital radius r, and uses ΔE = FΔx. The result is F ~ ħc·mM/(m_P² r²). Substituting m_P = √(ħc/G) then gives F ~ GmM/r². The paper defines m_P using G on the same page (p. 2), so G is put in rather than derived. The paper does not comment on this. McCulloch first called the step circular in his 2016 follow-up.

> **Stored version:** the Springer online-first PDF (3 pages; header "Astrophys Space Sci, DOI 10.1007/s10509-013-1686-9", with no volume or page numbers; "© Springer Science+Business Media Dordrecht 2013"). Page numbers below are PDF pages 1–3, which correspond to journal pp. 957–959. Owner-supplied copy, kept locally only. The paper has no figures.

## Key claims
- Newton's gravity law can be derived from the uncertainty principle. As two orbiting bodies get closer, their position uncertainty falls, so their momentum uncertainty, and hence the force, must rise (abstract; §3, p. 2; §4, p. 3).
- The model "assumes that the gravitational interaction only occurs between whole Planck masses" (p. 2). The Planck mass is called "the maximum mass to which we can apply quantum mechanics" (p. 2).
- MiHsC modifies inertial mass. This paper is about gravitational mass and is presented as a separate model (p. 2).
- The paper does not claim to be a complete theory. It says the derivation is "merely to point out that Newton's gravity law can be derived in this way, with some intuitive reasoning behind it" (p. 2).
- Prediction: masses below the Planck mass feel no gravitational attraction. Space should therefore contain many dust grains below m_P, with an abrupt drop in their number above it (abstract; pp. 2–3).
- The introduction cites Nesvizhevsky et al. (2002) as showing "that gravity is quantised", using neutrons in Earth's gravitational well (p. 1).
- The paper never discusses why the force should be attractive. All relations use "~", with no sign. This matches McCulloch's 2016 remark that "the inevitability of attraction was not discussed" here.

## Key equations
Transcribed from §2 (p. 2). Here i and j count the Planck masses in M (N of them) and m (n of them).

$$ \Delta p\,\Delta x \sim \hbar \quad (1) \qquad\qquad \Delta\bar p\,\Delta\bar x \sim \sum_{i=1}^{N}\sum_{j=1}^{n}\hbar \quad (2) $$
$$ E = pc:\ \ \frac{\Delta\bar E\,\Delta\bar x}{c} \sim \sum\sum\hbar \quad (3) \qquad \Delta\bar x = r:\ \ \frac{\Delta\bar E\, r}{c} \sim \sum\sum\hbar \quad (4) $$
$$ \Delta E = F\Delta x:\ \ \frac{F\,\Delta x\, r}{c} \sim \sum\sum\hbar \quad (5) \qquad \frac{F r^2}{c} \sim \sum\sum\hbar \quad (6) $$
$$ \frac{F r^2}{c} \sim \frac{\hbar\, mM}{m_P^2} \quad (7) \qquad F \sim \frac{\hbar c}{m_P^2}\frac{mM}{r^2} \quad (8) \qquad m_P=\sqrt{\hbar c/G}\ \Rightarrow\ F \sim \frac{GmM}{r^2} \quad (9) $$

The Planck mass is introduced earlier on the same page through the definition Gm_P²/r = ħc/r, so m_P = √(ħc/G) = 21.76 µg. The discussion repeats it as 2.176 × 10⁻⁸ kg. The text before Eq. (1) says "the total uncertainty is twice that for a single particle", but Eq. (1) is written as Δp Δx ~ ħ, with no factor of 2.

These equations agree in substance with McCulloch's 2016 restatement ([2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md), pp. 3–4), which the earlier version of this README used.

## Data used
- None. This is a theoretical derivation. The only numbers are the Planck mass (21.76 µg = 2.176 × 10⁻⁸ kg).

## Results & predictions
- **Newton's law (Eq. 9).** The form F ∝ mM/r² comes from setting Δx = r twice (Eqs. 4–6) and counting n·N = mM/m_P² pairs (Eq. 7). The coefficient ħc/m_P² equals G only because m_P is defined from G. The paper says (p. 2) that "the correct value for the gravitational constant G is only obtained when it is assumed that the gravitational interaction occurs between whole multiples of the Planck mass."
  - Editorial check: ħc = 3.1615 × 10⁻²⁶ J m and m_P² = (2.1764 × 10⁻⁸ kg)² = 4.737 × 10⁻¹⁶ kg², so ħc/m_P² = 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻². This is G exactly, as it must be, because m_P is built from G. No independent value of G is predicted.
- **Is the circularity visible in the 2014 text? (editorial check)** Yes. The paper defines the Planck mass with G (p. 2, "Gm_P²/r = ħc/r so that m_P = √(ħc/G)"), then substitutes m_P = √(ħc/G) to turn Eq. (8) into Eq. (9). The circularity can be read straight off the page. The paper itself does not flag it: it presents Eq. (9) as "Newton's gravity law, derived from the uncertainty principle". The explicit admission comes only in 2016 (quote below).
- **Planck-mass label (editorial check).** The text calls m_P "the reduced Planck mass" (p. 2), but the value it uses, √(ħc/G) = 21.76 µg, is the ordinary Planck mass. The reduced Planck mass is √(ħc/8πG) ≈ 4.34 µg. The derivation uses the ordinary value throughout, so this is a labelling slip and does not change the result.
- **Sub-Planck-mass prediction.** "gravitational attraction is only possible for masses greater than the Planck mass" (p. 2). The suggested test is a sharp drop in space-dust abundance above about 2 × 10⁻⁸ kg (pp. 2–3). No data are analysed.

## Figures
None. The paper has no figures.

## Notable quotes
> "This model assumes that the gravitational interaction only occurs between whole Planck masses" (p. 2)

> "One prediction of this model is that gravitational attraction is only possible for masses greater than the Planck mass" (p. 2)

From the 2016 follow-up (not this paper):
> "…this last part of the derivation involves some circular reasoning since the Planck mass is defined using the value for G (this was not discussed in the precursor gravity paper, [21])." (McCulloch 2016, arXiv:1610.06787, p. 8; [21] = this paper)

## Criticisms & responses
- **Circularity.** This is visible in the 2014 text (see Results) and acknowledged by the author in 2016. The 2016 paper presents itself as extending and correcting this derivation, adding horizons and an argument for why the force is attractive. See [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md).
- **Sub-Planck-mass gravity contradicts the paper's own citation (editorial check).** The paper cites Nesvizhevsky et al. (2002, *Nature* 415, 297) on p. 1 as evidence that gravity is quantised. That experiment depends on neutrons falling in Earth's gravity. A neutron (1.675 × 10⁻²⁷ kg) is about 8 × 10⁻²⁰ m_P, so by the paper's own prediction (p. 2) it should feel no gravitational attraction. The paper does not address this contradiction. Atoms in atom-interferometer gravimeters and ordinary laboratory falling bodies are also far below, or not whole multiples of, m_P. We found no published critique that makes this point about this paper specifically.
- **Heuristic steps (editorial reading).** The paper applies E = pc, which holds for massless quanta, to Planck masses. It also uses ΔE = FΔx with Δx = r a second time to go from Eq. (5) to Eq. (6). The paper calls the argument "intuitive reasoning" and not a complete theory (p. 2).
- **Supportive reinterpretation.** Haug (2018) argues the derivation has a deeper meaning in terms of Planck-mass "atomism"; see [2018-haug-mcculloch-derivation](../2018-haug-mcculloch-derivation/README.md).
- Renda (2019) critiques QI's foundations in general; see [2019-renda-sceptical](../../03-criticism/2019-renda-sceptical/README.md).

## Related
- Evidence: [derivation](../../02-evidence/derivation.md)
- Sources:
  - [2016-mcculloch-relativity-uncertainty](../2016-mcculloch-relativity-uncertainty/README.md)
  - [2018-haug-mcculloch-derivation](../2018-haug-mcculloch-derivation/README.md)
  - [2020-mcculloch-horizon-widths](../2020-mcculloch-horizon-widths/README.md)
  - [2018-gine-casimir-uncertainty](../2018-gine-casimir-uncertainty/README.md)
  - [2013-mcculloch-asymmetric-casimir](../2013-mcculloch-asymmetric-casimir/README.md)
