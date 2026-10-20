# Quantized Inertia — Research Repository

A balanced, source-grounded collection of everything published on **Quantized Inertia (QI)**, also called **MiHsC** (*Modification of inertia from a Hubble-scale Casimir effect*). It is the hypothesis, proposed by Mike McCulloch (University of Plymouth) in 2007, that inertia comes from Unruh radiation being limited by horizons. It covers the theory papers, the observational and laboratory evidence offered for it, independent tests and critiques, null results, and the surrounding physics and history.

> **Stance.** This repository reports what each source says and how it has been tested. Every source is tagged **supports**, **neutral** or **critical**. Our own analysis is kept in [08-synthesis/](08-synthesis/) and [09-analysis/](09-analysis/INDEX.md) and clearly labelled. Anything we could not verify is marked `[!UNVERIFIED]`.

## Start here
1. [What is Quantized Inertia?](00-overview/what-is-qi.md): the mechanism, the formula, the claims and the main objections
2. [Evidence index](02-evidence/INDEX.md): each phenomenon QI claims to explain, with a verdict
3. [Scorecard & synthesis](08-synthesis/scorecard.md): what we can conclude
4. [Master index](INDEX.md): every note and source in one place

Contributing with an AI agent? Start with [AGENTS.md](AGENTS.md). Have access to a paper we're missing? See [MISSING-PDFS.md](MISSING-PDFS.md).

## Layout
| Folder | Contents |
|---|---|
| [00-overview/](00-overview/INDEX.md) | Explanation, [equations](00-overview/equations.md), [timeline](00-overview/timeline.md), [glossary](00-overview/glossary.md) |
| [01-papers/](01-papers/INDEX.md) | Theory papers, extensions and observational studies, **one folder per source** |
| [02-evidence/](02-evidence/INDEX.md) | One note per phenomenon: data, QI prediction, independent checks, verdict |
| [03-criticism/](03-criticism/INDEX.md) | Published critiques and null results, one folder per source |
| [04-experiments/](04-experiments/INDEX.md) | Laboratory / propulsion experiment reports, one folder per source |
| [05-context/](05-context/INDEX.md) | Background physics: Unruh effect, Casimir effect, MOND, dark matter, Mach's principle… |
| [06-people-orgs/](06-people-orgs/INDEX.md) | McCulloch, Tajmar, Giné, IVO Ltd, DARPA 2018 award, others |
| [07-media/](07-media/INDEX.md) | Books, press coverage, popular articles, one folder per source |
| [08-synthesis/](08-synthesis/) | Our analysis: scorecard, open questions, testable predictions |
| [09-analysis/](09-analysis/INDEX.md) | Our own reproducible calculations with public data (e.g. [A1: SPARC refit](09-analysis/a1-sparc-rar-refit/README.md)) |
| [assets/diagrams/](assets/diagrams/README.md) | Self-made SVG / Mermaid diagrams |
| [bibliography.bib](bibliography.bib) | BibTeX for every source (generated from each folder's `citation.bib`) |

## Source-folder convention
Every source (paper, critique, experiment, book or article) has its own folder, `YYYY-firstauthor-shortname/`, containing:
- `README.md`: the extracted information for quick access: front-matter metadata, TL;DR, key claims, equations, data, results, figures, quotes, criticisms, related links
- `paper.pdf`: **only if open access** (arXiv / OA journal). Paywalled sources are linked by DOI only
- `figures/`: key figures rendered from the source
- `citation.bib`: the BibTeX entry

Template: [_templates/source-README.md](_templates/source-README.md).

## Maintenance
```sh
python3 -I _tools/build_index.py          # rebuild section INDEX tables + check links
python3 -I _tools/build_index.py --check-only
python3 -I _tools/build_master_index.py    # rebuild top-level INDEX.md
python3 -I _tools/check_license.py --arxiv <id> --doi <doi>   # licence lookup for a new PDF
python3 -I _tools/apply_local_only.py      # apply _tools/licenses.json: .gitignore + "local only" notes
python3 -I _tools/build_missing_list.py    # refresh MISSING-PDFS.md
cat */*/citation.bib > bibliography.bib    # regenerate the bibliography
```
To add a source, copy the template into a new `YYYY-author-shortname/` folder in the right section, fill in the README, and rerun the script.

## Licence
- **Original content** (notes, READMEs, evidence, synthesis, diagrams in `assets/diagrams/`): [CC BY 4.0](LICENSE) © 2026 David Bowdoin.
- **Code** in `_tools/` and the scripts in `09-analysis/`: [MIT](_tools/LICENSE).
- **Third-party material** (source PDFs and figures rendered from them) is **not** covered by these licences. It keeps its original licence, recorded in each source's `license:` front-matter field. Only openly licensed PDFs and figures are included in this public repository; the rest are kept locally and are marked *local only* in their README. Short quotations are included for commentary and criticism, with citations.
