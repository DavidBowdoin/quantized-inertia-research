---
title: "Grokipedia edits"
tags: [synthesis, grokipedia, corrections]
as_of: 2026-10-19
---

# Grokipedia edits

> **Editorial.** Corrections we have found in the [Grokipedia "Quantized inertia" page](https://grokipedia.com/page/quantized-inertia), with suggested-edit text ready to submit. The page was reviewed on 2026-10-19. Each section records its submission status.

## 1. Wide-binary claims cite the wrong paper

**Status:** drafted, not yet submitted.

**Problem.** All three wide-binary claims cite reference [10], "Inertia from an asymmetric Casimir effect" (arXiv:1302.2775). That 2013 paper ([2013-mcculloch-asymmetric-casimir](../01-papers/2013-mcculloch-asymmetric-casimir/README.md)) is not about wide binaries. The 2019 study is [2019-mcculloch-wide-binaries](../01-papers/2019-mcculloch-wide-binaries/README.md). It is already in the reference list (as items 9, 34 and 36, which are duplicates), but it is never cited inline for these claims. The text also states the paper's findings more strongly than the paper does.

The claims appear in these places on the page:
- *History → Development Milestones*: "2019 analyses of wide binary star systems, where quantized inertia better matched observed orbital anomalies … compared to Newtonian predictions." [10]
- *Predictions → Astrophysical Applications*: "In wide binary star systems, QI anticipates that the reduced inertia at low accelerations sustains observed orbital speeds … that would predict wider dispersal." [10]
- *Empirical Support → Binary Star Systems*, first paragraph: "In a 2019 study, QI was applied to wide binary stars from the Gaia catalog, … outperforming Newtonian predictions and providing a better fit than MOND in certain cases." [10]

### Text to submit

---

**Summary of the problem**

All three wide-binary claims cite reference [10], "Inertia from an asymmetric Casimir effect" (arXiv:1302.2775). That 2013 paper is not about wide binaries. The 2019 study is McCulloch & Lucio, "Testing Newton/GR, MoND and quantised inertia on wide binaries", *Astrophysics and Space Science* 364(8), 121 (2019), doi:10.1007/s10509-019-3615-z, arXiv:1908.01434. It is already in the reference list (as items 9, 34 and 36, which are duplicates), but it is never cited inline for these claims. The text also states the paper's findings more strongly than the paper does.

**Suggested changes**

1. *History → Development Milestones.* Change the citation on the 2019 wide-binary sentence from [10] to the McCulloch & Lucio (2019) reference.

2. *Predictions → Astrophysical Applications.* Change the citation from [10] to McCulloch & Lucio (2019).

3. *Empirical Support → Binary Star Systems*, first paragraph. Replace the sentence "In a 2019 study, QI was applied to wide binary stars from the Gaia catalog, … outperforming Newtonian predictions and providing a better fit than MOND in certain cases. [10]" with:

> In a 2019 paper, McCulloch and J. H. Lucio compared the predictions of Newtonian gravity, MOND (with an external field effect) and QI with the root-mean-square relative velocities of 83 Gaia DR2 wide binaries compiled by Hernandez et al. They reported that Newtonian gravity and MOND under-predicted the velocities at separations above about 0.3 pc, and concluded that "QI alone agrees with the data given the error bars", with no adjustable parameter. The authors noted that all the data points lie above the QI prediction, and that some of the data may be contaminated by false binaries.[McCulloch & Lucio 2019] Later analyses of Gaia DR3 wide binaries disagree with each other: Banik et al. (2024) found the data favour Newtonian gravity,[Banik et al. 2024] while Chae (2023) reported a low-acceleration anomaly.[Chae 2023]

**References to add**
- Banik, I. et al. (2024). "Strong constraints on the gravitational law from Gaia DR3 wide binaries". *MNRAS* 527(3), 4573–4615. doi:10.1093/mnras/stad3393 (arXiv:2311.03436)
- Chae, K.-H. (2023). "Breakdown of the Newton–Einstein Standard Gravity at Low Acceleration in Internal Dynamics of Wide Binary Stars". *ApJ* 952(2), 128. doi:10.3847/1538-4357/ace101 (arXiv:2305.04613)

**Housekeeping:** items 34 and 36 duplicate item 9, and items 35 and 3 duplicate each other (Proxima Centauri), so the duplicates could be merged.

**Justification:** reference [10] is a different paper on a different subject. The proposed wording and the quote come from the paper itself (arXiv:1908.01434, p. 6). The Banik and Chae references show that the wide-binary result is still disputed, so the article no longer presents a single co-authored analysis as settled support.

---

### Notes (not for submission)
- The replacement deliberately drops the claim that QI is "providing a better fit than MOND in certain cases". The paper compared QI only with MOND at a₀ = 1.2 × 10⁻¹⁰ m/s². It also says MOND with a₀ = 2 × 10⁻¹⁰ gives "an expression practically equivalent to QI", so "better than MOND" depends on that choice.
- The paper's details were checked against the stored arXiv v1 PDF on 2026-10-19: 83 binaries; Newton and MoND under-predict above about 0.3 pc; "QI alone agrees with the data given the error bars" (p. 6); the data lie above QI and may include false binaries (p. 6). See [2019-mcculloch-wide-binaries](../01-papers/2019-mcculloch-wide-binaries/README.md).
- If Grokipedia's form only allows a short reason, the first two sentences of the summary are enough on their own.
- Related sources: [2023-banik-gaia-dr3-wide-binaries](../03-criticism/2023-banik-gaia-dr3-wide-binaries/README.md), [2023-chae-wide-binaries](../01-papers/2023-chae-wide-binaries/README.md). Evidence note: [wide-binaries](../02-evidence/wide-binaries.md).
