---
title: "Quantized Inertia: Modified Inertia from a Hubble-scale Casimir effect (quantizedinertia.com)"
authors: [Quantized Inertia GitHub organisation]
year: 2023
type: article
venue: "quantizedinertia.com (advocacy website; GitHub Pages)"
doi:
arxiv:
url: "https://quantizedinertia.com"
open_access: true
license: unknown
files: []
status: supports
tags: [website, advocacy, overview, lab-test, propulsion, galaxy-rotation, wide-binaries, flyby-anomaly, papers-list]
---

# quantizedinertia.com: the QI advocacy website

**Citation:** Quantized Inertia (GitHub organisation `quantizedinertia`). *Quantized Inertia: Modified Inertia from a Hubble-scale Casimir effect*. Website at https://quantizedinertia.com, with pages /about, /tests and /papers (accessed 2026-10-19).

**About this source:** the site is a GitHub Pages site. Its source is public at [github.com/quantizedinertia/quantizedinertia.github.io](https://github.com/quantizedinertia/quantizedinertia.github.io) (home, /about, /tests; MIT-licensed repository; last pushed 2023-09-12). The /papers page is built from `data.json` in [github.com/quantizedinertia/papers](https://github.com/quantizedinertia/papers) (MIT-licensed; last commit 2025-01-18; repository last pushed 2026-08-12). The pages were read from the repositories with `gh api`. **No copy is stored**; only short quotes appear below. The front-matter `license: unknown` is a placeholder, since no file is stored. The repository's MIT licence, as declared by GitHub, covers the site code and text.

**Who runs it (from commit history):** the GitHub organisation was created 2019-08-31. Most commits are by Soumya Deb (2019–2023). The GitHub account `m-e-mcculloch` committed a data update on 2021-05-07, and in September 2023 opened the pull request that edited the home page. The account `RocketSlinger` (Titus Stauffer) added his own two papers to the list on 2025-01-18. The home page links to McCulloch's blog. The /about and /tests text was added on **2021-07-04** and last edited on 2021-11-11 (spelling changes only). So the **Tests page claims date from July 2021**, before Dresden's October 2021 IAC follow-up and McCulloch's January 2022 revision.

**TL;DR:** A small advocacy site for QI. It has a home page with the tagline "Modified Inertia from a Hubble-scale Casimir effect", an explainer (/about), a list of claimed successes (/tests), and a papers table of 30 entries (/papers): 27 papers from 2007 to 2021 by McCulloch (alone or with co-authors), Pickering or Taylor, plus Renda's 2019 critique and Stauffer's two self-published notes. The Tests page claims that QI predicts disc-galaxy rotation "without adjustment", a change in galaxy behaviour with cosmic time, wide binaries, and the flyby anomalies. It also says that of "six labs" testing propellantless thrust, "five have shown some thrust (Perez-Diaz et al., 2021; one has not (Neunzig et al., 2021)". It concedes that later flybys "showed no anomaly".

## What the site says
- **/about:** QI was "first proposed in 2007 by physicist Mike McCulloch". It "explains inertia, for the first time", via Rindler-horizon damping of Unruh radiation, and "predicts galaxy rotation perfectly without the need for dark matter or any adjustment". It "also predicts that we can get thrust and energy from the vacuum".
- **/tests** (five claims, all from July 2021):
  1. Disc-galaxy rotation "simply, without dark matter and without adjustment" (McCulloch 2012, 2017).
  2. "a change in galactic behaviour into the past, not predicted by any other theory which seems to be borne out by recent data" (McCulloch 2017). The 2021 version linked McCulloch & Giné 2017 (information loss); the November 2021 edit relinked it to the 2017 Ap&SS galaxy paper.
  3. Wide binaries are predicted by QI (McCulloch & Lucio 2019). "Dark matter cannot be applied to these systems and MoND does not predict them."
  4. Propellantless thrust from cavities (McCulloch 2018): "Six labs have tested this. So far, five have shown some thrust (Perez-Diaz et al., 2021; one has not (Neunzig et al., 2021)." The citation has no link and an unclosed parenthesis.
  5. The flyby anomalies are predicted by QI (McCulloch 2008), "though later flybys showed no anomaly".
- **/papers:** a table of title, author, year and link. Several links point to `ptep-online.com`, which is now a spam domain (Progress in Physics has moved to progress-in-physics.com; see [AGENTS.md](../../AGENTS.md) gotchas). Entries not previously in this repository: [2019-mcculloch-superluminal-travel](../../01-papers/2019-mcculloch-superluminal-travel/README.md), [2024-stauffer-qi-drive-versions](../../01-papers/2024-stauffer-qi-drive-versions/README.md) and [2025-stauffer-qi-experiments](../../01-papers/2025-stauffer-qi-experiments/README.md).

## Claims compared with this repository's evidence notes

| Site claim | What the repository's evidence says |
|---|---|
| Galaxy rotation "without adjustment", "perfectly" | [galaxy-rotation](../../02-evidence/galaxy-rotation.md) (verdict *supported-by-author-only*): agreement shown by eye only. Θ changed by a factor of about 3 between papers (2.6–2.7 × 10²⁶ m before 2017, 8.8 × 10²⁶ m after). The early version overpredicted spirals by 30–54%, and the later one sits about 30% above the deep-MOND data. No independent quantitative test exists. |
| Change in galaxy behaviour with cosmic time "not predicted by any other theory" | [galaxy-rotation](../../02-evidence/galaxy-rotation.md): the redshift prediction is "only partly consistent" with Übler/Genzel (predicted −0.52 dex at z = 2.3 vs observed −0.2 to −0.47). The observers interpret the data within ΛCDM, and a time-varying a₀ has also been discussed in MOND, so "no other theory" is not accurate. |
| Wide binaries predicted; "MoND does not predict them" | [wide-binaries](../../02-evidence/wide-binaries.md) (verdict *contested*): whether any anomaly exists is disputed (Chae vs Banik et al., 19σ for Newton). The anomaly-favouring analyses match MOND *with* an external-field effect, which QI says it does not have. QI's own support is one comparison with 83 DR2 binaries, co-authored by McCulloch. |
| "Six labs … five have shown some thrust" | [lab-tests](../../02-evidence/lab-tests.md) and [propulsion](../../02-evidence/propulsion.md) (verdicts *refuted-or-null*): the only independent, controlled, peer-reviewed tests (TU Dresden, DARPA-funded) are null at the nN level, including after the set-up changes McCulloch asked for ([2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md), [2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md)). The positive claims are unpublished, blog-reported or non-peer-reviewed; see the next section. The cited "Perez-Diaz et al., 2021" was never published, and in 2022 McCulloch himself called that result "an artefact". |
| Flybys predicted, but later flybys showed no anomaly | [flyby-anomaly](../../02-evidence/flyby-anomaly.md) (verdict *contested*): consistent with the site's own caveat. The QI correlation is not statistically significant, and the predicted EPOXI anomaly was not seen. |
| "explains inertia, for the first time" | [derivation](../../02-evidence/derivation.md): the derivation is disputed ([Renda 2019](../../03-criticism/2019-renda-sceptical/README.md), [Dickmann & Dickmann 2023](../../03-criticism/2023-dickmann-casimir-contradicts/README.md)). |

## The "six labs" and "five positives" (July 2021)
The site does not name the labs. The nearest contemporary sources are McCulloch's blog posts. **Reconstruction (editorial), not confirmed by the site:**

- **Named groups.** "Five Experiments" (blog, 25 Jul 2020) names five groups testing QI thrust:
  1. **Madrid / Universidad de Alcalá** (José Luis Pérez-Díaz): a laser in a many-looped fibre-optic coil on a pendulum. QI predicted 1 µN for 2 W, and 1–4 µN was seen, "inconclusive so far. The pendulum is subject to significant artefacts".
  2. **TU Dresden** (Tajmar): an early 140 nN from 0.35 W with an asymmetric copper cavity, but "later tests though have shown less thrust".
  3. **Poland** (Zbigniew Komala): a "Bart" cavity on a spring with interferometer readout, 30 µN from 20 W. Unpublished.
  4. **California** (Positron Dynamics with USC; Ryan Weed, David Barnhart): CATIE-funded, still setting up in 2020.
  5. **Atlanta** (Jamie Ciomperlik, "monomorphic"): a laser in a mirror cavity on a torsion balance. "At the moment it looks to be thermal."
- **Sixth experiment.** On 9 Aug 2020 ("Minding One's Ps and Qs") McCulloch wrote of "the six quantised inertia experiments that are going on around the world" without naming the sixth.
- **Capacitor tests.** By 2021 the blog also counts the capacitor tests of **Becker & Bhatt** ([2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md); "Horizon Engineers", 6 Feb 2021) and **Richard Mansell / IVO Ltd** ("A Thrust from 'Nothing'", 2 Nov 2021).
- **The null.** The single null ("Neunzig et al., 2021") is most likely the Dresden laser-resonator paper, published online 24 Apr 2021 ([2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md)). McCulloch answered it on his blog on 27 Apr 2021. The Dresden IAC paper ([2022-neunzig-emdrive-thrust](../../03-criticism/2022-neunzig-emdrive-thrust/README.md)) was presented only in October 2021, after the page was written.
- **Likely five positives (editorial).** If Dresden is the one null, the five claimed positives would be drawn from Alcalá, Komala, Becker & Bhatt, Mansell/IVO and one of California, Atlanta or the unnamed sixth group. None of these was a peer-reviewed positive result in July 2021. Becker & Bhatt is an arXiv preprint; the others were unpublished or blog-reported. Two were described by McCulloch himself as inconclusive (Alcalá) or apparently thermal (Atlanta).

> [!UNVERIFIED] Which six labs, and which five positives, the July 2021 Tests page meant. The page gives only the two citations. The identification above is our reconstruction from McCulloch's blog posts.

**What "Perez-Diaz et al., 2021" was.** It is the Alcalá fibre-loop experiment. McCulloch's January 2022 preprint ([2022-mcculloch-qi-thrust-casimir](../../01-papers/2022-mcculloch-qi-thrust-casimir/README.md), reference list) cites it as "Perez-Diaz, JL, J. Corella, M. McCulloch, 2021. Paper submitted." It uses P = 0.129 W and Q = 300, with an observed thrust of 10,000 ± 6,000 nN, and concludes "This suggests that the Spanish positive result was an artefact" (p. 4). McCulloch's blog of 23 Jan 2022 repeats that "the positive Spanish result was an artefact (… unless the electrons in glass were the accelerand)".

> [!UNVERIFIED] No published version of Pérez-Díaz, Corella & McCulloch (2021) was found. Searches covered Crossref, OpenAlex (Pérez-Díaz's Universidad de Alcalá author profile lists no QI or thrust work from 2018 to 2026), a web search, and McCulloch's blog. The Alcalá repository (e_Buah) search API returned 404 and was not searched further. "J. Corella" was not identified.

## Notable quotes
> "Six labs have tested this. So far, five have shown some thrust (Perez-Diaz et al., 2021; one has not (Neunzig et al., 2021)." (/tests, text dated 2021-07-04)

> "Quantised Inertia predicts galaxy rotation perfectly without the need for dark matter or any adjustment" (/about)

> "QI predicts these … though later flybys showed no anomaly." (/tests)

## Criticisms & responses
- **Out of date (factual):** the Tests page was not updated after July 2021. It does not reflect McCulloch's own January 2022 reassessment that photon-based thrusters "did not perform well" and that the Spanish result was "an artefact" ([propulsion](../../02-evidence/propulsion.md)). Nor does it reflect Dresden's follow-up nulls, the Barry-1 failure or the inconclusive OTP-2 flight.
- **Selection (editorial):** the papers list includes one critique (Renda 2019) but none of the Dresden null tests, the [Tajmar & Schreiber capacitor null](../../03-criticism/2020-tajmar-capacitor-thrust/README.md), or the Gaia wide-binary analyses that favour Newton.
- **Independence:** most "tests" cited are McCulloch's own papers, or co-authored ones (Lucio, Giné), and are not independent support (see [AGENTS.md](../../AGENTS.md) editorial rules).

## Related
- Evidence: [lab-tests](../../02-evidence/lab-tests.md), [propulsion](../../02-evidence/propulsion.md), [galaxy-rotation](../../02-evidence/galaxy-rotation.md), [wide-binaries](../../02-evidence/wide-binaries.md), [flyby-anomaly](../../02-evidence/flyby-anomaly.md), [derivation](../../02-evidence/derivation.md)
- Sources: [2018-mcculloch-propellantless-propulsion](../../01-papers/2018-mcculloch-propellantless-propulsion/README.md), [2022-mcculloch-qi-thrust-casimir](../../01-papers/2022-mcculloch-qi-thrust-casimir/README.md), [2019-mcculloch-wide-binaries](../../01-papers/2019-mcculloch-wide-binaries/README.md), [2017-mcculloch-galaxy-rotations-sparc](../../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md), [2008-mcculloch-flyby-anomalies-mnras](../../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md), [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md), [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2019-mcculloch-superluminal-travel](../../01-papers/2019-mcculloch-superluminal-travel/README.md), [2024-stauffer-qi-drive-versions](../../01-papers/2024-stauffer-qi-drive-versions/README.md), [2025-stauffer-qi-experiments](../../01-papers/2025-stauffer-qi-experiments/README.md)
- People: [darpa-2018-award](../../06-people-orgs/darpa-2018-award.md), [jaume-gine](../../06-people-orgs/jaume-gine.md) (note on Pérez-Díaz), [other-researchers](../../06-people-orgs/other-researchers.md)
