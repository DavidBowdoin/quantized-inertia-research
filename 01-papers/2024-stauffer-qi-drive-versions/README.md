---
title: "Proposed Versions of Quantized-Inertia Drives"
authors: [Titus Stauffer]
year: 2024
type: preprint
venue: "ResearchGate 377926730 (self-published; not peer-reviewed); mirrored at rocketslinger.com/Quant_Inert/"
doi:
arxiv:
url: "https://www.researchgate.net/publication/377926730_Proposed_Versions_of_Quantized-Inertia_Drives"
open_access: true
license: unknown
files: [paper.pdf, citation.bib, figures/fig-1-basic-thruster.png, figures/fig-2-stacked-cells.png, figures/fig-3-baffled-expander.png]
status: neutral
tags: [propulsion, drive-design, thermal-gradient, speculative, not-peer-reviewed, self-published, hobbyist]
---

# Proposed Versions of Quantized-Inertia Drives

<!-- local-only-note -->
> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public repository because this copy's licence (`unknown`) does not permit redistribution. Read the paper at [source](https://www.researchgate.net/publication/377926730_Proposed_Versions_of_Quantized-Inertia_Drives).

**Citation:** Stauffer, T. (2024). *Proposed Versions of Quantized-Inertia Drives*. ResearchGate publication 377926730 (self-published, not peer-reviewed; 22 pp.). https://www.researchgate.net/publication/377926730_Proposed_Versions_of_Quantized-Inertia_Drives. The author's HTML mirror of the same text is at http://www.rocketslinger.com/Quant_Inert/ (page "last updated 02 February 2024").

**About this summary:** the stored `paper.pdf` is the ResearchGate PDF (22 pages, created 2 February 2024), supplied by the repository owner because ResearchGate blocks scripted downloads. It is kept **local only** (licence `unknown`). Page numbers below refer to it. A word-level comparison with the author's HTML mirror (fetched 2026-10-19) found the body text identical. The only differences are the mirror's header line (contact and "last updated 02 February 2024") and its link back to ResearchGate, and the six figures, which are images on the mirror and vector drawings with text labels in the PDF. The site declares its ideas "defensively published" into the public domain to prevent patenting (p. 2). That statement is not a copyright licence for the text, so the licence is recorded as `unknown`.

**Who the author is:** Titus Stauffer publishes as "RocketSlinger" on his personal site rocketslinger.com, a collection of defensively published rocketry and engineering ideas that he calls his "hobby" writings (p. 3). He also added this paper and its follow-up to the [quantizedinertia.com papers list](../../07-media/2023-quantizedinertia-website/README.md) (2025). **Not a McCulloch co-author, and not a professional physicist as far as could be determined.**

**TL;DR:** A speculative engineering note, "purely speculation and internet research", with no drives built or tested. It proposes a reactionless "QI Thruster": a sealed gas-filled cylinder heated at the leading end (by a Peltier device or heater) and cooled at the trailing end. The author's reasoning is that hot molecules bounce off the hot plate with higher accelerations, and so "should carry lots of inertia", while cold molecules at the rear carry less. The difference would give net forward thrust "if theories of quantized inertia are correct". Variants include stacked cells with valves, segmented heaters for steering, and gas expanders (porous filters or baffled layers in a flowing gas) that "double up as QI thrusters". There is no mathematics.

## Key claims
- Both the EmDrive and IVO's quantum drive "attempt to violate Newton's laws of action and reaction (as conventionally understood)" (p. 1). Detailed testing "seems to say" that the EmDrive does not work. The author was awaiting results from IVO's in-orbit test (as of February 2024) and recommends a NextBigFuture article as background (p. 3).
- His reading of QI: "at higher rates of acceleration, matter has higher inertia, and at lower rates of acceleration, matter has lower inertia" (p. 4).
- Simple design (section "Simple Basic Design Here", Fig. 1, pp. 4–7): two Peltier devices set up a temperature gradient in a sealed gas cavity. The gas presses equally on the side walls, and the hot end gets more "QI thrust" than the cold end. Reversing the Peltier current (with an H-bridge) would reverse the thrust. The suggested gas is xenon or krypton. The author also states the conventional objection himself: the colder gas at the rear is denser, so more molecules hit the cold plate, "balancing the gas-forces on the hot-end plate… In the absence of validity of the QI theory" (p. 6). Without QI, he says, the device would be a close relative of a perpetual-motion machine.
- Section "Basic Design, With Some Implausible Variations or Features" (Fig. 2, pp. 8–12): insulation and an infrared photon-thrust bonus (extra insulation judged not worth the mass), smooth inner walls with no baffles, and speculative ways to sort heavy and light molecules (magnetic gases, ferrofluids, suspended ferromagnetic dust). He found no workable option.
- Section "More-Plausible Variations or Features" (Figs. 3–5, pp. 12–17): stacked cells with valves that can be switched to pump fluid by "quasi-peristalsis" (a mode that "will negate any 'QI thrust' effects", p. 12), a rounded leading edge with segmented heaters for steering, and reversible QI thrusters as replacements for cold-gas attitude thrusters.
- Section "Gas Compressors and Expanders Which Double Up as QI Thrusters" (Fig. 6, pp. 17–22): a gas expander, such as a permeable filter with a thermal gradient along the flow, "should give us a tiny bit of thrust" if QI is correct (p. 18). A layered baffle with metal-foil cold faces is proposed, along with Peltier devices on compressor or turbine blades and in ducts.
- Conclusion: "I, for one, am sure hoping that 'QI theories' (of Quantum Inertia) can be exploited!" (p. 22). The paper has no references ("References (none for now)", p. 22).

## Key equations
None. The paper explicitly avoids mathematics ("nor do I plan to attempt to tackle much if any math here", p. 3).

## Data used
- None. It links to Wikipedia pages (EmDrive, MOND, thermoelectric cooling, RTGs, ferrofluids, radiometers and others), an introductory-chemistry textbook figure on molecular speed distributions, an OSTI page on gaseous diffusion, and a NextBigFuture article on IVO.

## Results & predictions
- No quantitative prediction. The claimed effect is conditional on QI being true and is not sized.
- **Editorial check (our reading of QI's published formula):** QI's correction to inertia is the factor (1 − 2c²/aΘ). It matters only when the acceleration a is near 2c²/Θ ≈ 2 × 10⁻¹⁰ m s⁻² (see [equations](../../00-overview/equations.md)). A gas molecule hitting a wall reverses about 300 m s⁻¹ in very roughly 10⁻¹³ s, an acceleration of order 10¹⁵ m s⁻². That makes the QI correction about 10⁻²⁵ for both hot and cold molecules. So QI's published formula gives no usable temperature-dependent inertia difference here, and the device's premise is not one McCulloch's papers make. McCulloch's thrust proposals instead rely on asymmetric damping of Unruh waves by nearby conductors or cavities ([propulsion](../../02-evidence/propulsion.md)).
- The author's own follow-up ([2025-stauffer-qi-experiments](../2025-stauffer-qi-experiments/README.md), "Last-Paper Errata and Embellishments") concludes that molecules bouncing off the side walls would take the thrust back: "I will bet that it all balances out, with or without QI effects."

## Figures
*Figure (local only): Fig. 1 — "Basic Starting Design": the "QI Thruster", a sealed gas cavity with a Peltier device's hot side at the leading (top) end and another Peltier device's cold side at the trailing end; infrared emission from the rear is labelled as extra thrust. (PDF p. 5.)*

*Figure (local only): Fig. 3 — "Forced Fluid Flow 'Phase A'": four stacked hot-gas and cold-gas cells with reversible Peltier devices and valves, switched to pump fluid by quasi-peristalsis (a mode the author says cancels any QI thrust). (PDF p. 13.)*

*Figure (local only): Fig. 6 — "Passive Baffled Gas Expander": perforated baffle layers with hot (red) and cold (blue) faces in a downward gas flow; the proposed QI thrust points upstream. (PDF p. 19.)*

The PDF has six figures in all. Not reproduced: Fig. 2 (insulation added to Fig. 1, p. 9), Fig. 4 ("Phase B" of the stacked cells, p. 14) and Fig. 5 (rounded leading edge with six segmented heaters, p. 16).

## Notable quotes
> "This is purely speculation and internet research here. No experimental drives were produced or tested, by the author of this paper." (p. 1, abstract)

> "If theories of quantized inertia are correct, this design should work." (p. 2, abstract)

> "Note that if 'QI' theory is NOT true, then our here-described QI thruster is some sort of close relative to the long-sought but perpetually-out-of-reach, forbidden 'perpetual motion machine'!" (p. 6)

## Criticisms & responses
- No published critique of this paper was found. The main correction comes from the author himself in the 2025 follow-up (see above). In this paper he already gives the conventional reason it should fail: denser cold gas balances the pressure on the hot plate (p. 6).
- **Momentum conservation:** reactionless thrust from a closed system conflicts with momentum conservation ([Provatidis 2024 review](../2024-provatidis-inertial-propulsion-review/README.md); [propulsion](../../02-evidence/propulsion.md)). The author acknowledges that such drives try to violate Newton's third law "as conventionally understood".
- **Status (factual):** a self-published, non-peer-reviewed hobbyist note by a non-specialist, listed by its own author on the QI advocacy site. It is not evidence for or against QI.

## Related
- Evidence: [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2025-stauffer-qi-experiments](../2025-stauffer-qi-experiments/README.md), [2023-quantizedinertia-website](../../07-media/2023-quantizedinertia-website/README.md), [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md), [2026-nextbigfuture-ivo-review](../../07-media/2026-nextbigfuture-ivo-review/README.md), [2024-provatidis-inertial-propulsion-review](../2024-provatidis-inertial-propulsion-review/README.md)
