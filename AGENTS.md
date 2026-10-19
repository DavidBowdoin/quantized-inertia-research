# AGENTS.md: guide for AI agents working in this repository

Read this file before changing anything. It is the shortest path from a blank context to useful, safe work here.

## What this repository is
A **balanced, source-grounded research archive on Quantized Inertia (QI)**, also called **MiHsC** (Mike McCulloch's 2007– hypothesis that inertia arises from horizon-limited Unruh radiation). It is **not** advocacy and **not** debunking. Every source is reported faithfully and tagged `supports | neutral | critical`. Our own analysis lives only in `08-synthesis/` and is labelled *editorial*.

It is pure Markdown and assets. There is no build system: just two stdlib-only Python scripts in `_tools/`.

## Orientation (read in this order)
1. `README.md`: layout and licence
2. `00-overview/what-is-qi.md` and `00-overview/equations.md`: the theory and its formula variants (§7 lists known inconsistencies between papers)
3. `02-evidence/INDEX.md`: the verdict for each phenomenon
4. `08-synthesis/scorecard.md`: the current bottom line
5. `INDEX.md`: everything, listed

## Layout
| Path | Kind | Contents |
|---|---|---|
| `00-overview/` | topic notes | explanation, equations, timeline, glossary |
| `01-papers/` | **source folders** | theory papers, extensions, observational studies |
| `02-evidence/` | topic notes | one note per phenomenon, each with a `verdict` |
| `03-criticism/` | **source folders** | critiques and null results |
| `04-experiments/` | **source folders** | lab / propulsion experiment reports |
| `05-context/` | topic notes | background physics (Unruh, Casimir, MOND, dark matter…) |
| `06-people-orgs/` | topic notes | people, IVO Ltd, the DARPA 2018 award |
| `07-media/` | **source folders** | books, press, popular articles |
| `08-synthesis/` | topic notes | editorial: scorecard, open questions, ideas, build notes |
| `assets/diagrams/` | assets | our own SVGs only (CC BY 4.0) |
| `_templates/source-README.md` | template | copy this for every new source |
| `_tools/` | code (MIT) | `build_index.py`, `build_master_index.py` |
| `bibliography.bib` | generated | concatenation of every `citation.bib` |

## The source-folder convention (most important rule)
Every source is one folder: `<section>/YYYY-firstauthorsurname-shortname/` (lowercase, hyphens, 2–4 words in the short name), containing:
- `README.md`: the extracted information, following `_templates/source-README.md` exactly
- `citation.bib`: one BibTeX entry whose key is the folder name
- `paper.pdf`: only if open access (see the publishing rules below)
- `figures/fig-<n>-<short>.png`: at most 3 key figures, captioned in the README

**Front-matter keys** (all required; use `null` when unknown): `title, authors, year, type, venue, doi, arxiv, url, open_access, license, files, status, tags`.
- Use inline YAML lists: `authors: [Michael E. McCulloch, Jaume Giné]`.
- Quote any title that contains a colon.
- `status` is the source's stance on QI, not ours.
- `license` is the licence of **the exact PDF copy stored** (an arXiv version, a conference version and the journal version can differ).

The index script parses the front-matter with a minimal parser (`key: value` and `[a, b]` only). Do not use multi-line YAML.

Topic notes (`02-evidence/`, `05-context/`, …) are single `.md` files. They **link to** source folders and never copy source files.

## Public vs local-only content: do not break this
The public GitHub repo (`DavidBowdoin/quantized-inertia-research`) must contain **only redistributable material**. A private backup with everything exists separately (`quantized-inertia-research-private`).
- **Can be published:** our own writing and diagrams; PDFs and figures whose `license` is CC-BY, CC-BY-SA, CC0, public domain or CC-BY-NC.
- **Local only:** arXiv's default non-exclusive licence (`arXiv-nonexclusive`), all-rights-reserved, `unknown`, and figures rendered from any of these (or from ND-licensed works).
- Local-only files are listed in `.gitignore` and stay on disk. **Never `git add -f` them.**
- Their README marks them *(local only)*, so readers on GitHub know why a file is missing.
- When you add a new PDF or figure, determine its licence first:
  - arXiv: the OAI-PMH `GetRecord` call with `metadataPrefix=arXiv` returns a `<license>` element. No element means the default non-exclusive licence, which is not redistributable.
  - DOI: the Crossref `license` field.
  - If in doubt, treat it as local only and add it to `.gitignore`.
- Before any commit, check that the staged changes contain no ignored PDFs:
  `git diff --cached --name-only | grep -E '\.(pdf|png)$'`, then compare against `.gitignore`.

## Editorial rules
- **Never invent** facts, numbers, quotes, page numbers, DOIs or arXiv IDs. Verify identifiers (Crossref, doi.org, arXiv abs pages). Mark anything unverifiable `> [!UNVERIFIED] …`.
- Distinguish **the source's claim**, **published criticism** and **our own arithmetic or reading**. Label the last one explicitly ("editorial check: …").
- Keep quotes short (≤ 3 per source) and cite them. Paraphrase abstracts; don't paste them.
- Co-authored McCulloch papers (e.g. with Giné or Lucio) are **not** independent support.
- Citing QI in passing (Smolin, Cadoni, Iorio…) is **not** endorsement.
- Verdict scale for evidence notes: `supported-by-author-only | contested | independently-unconfirmed | refuted-or-null | mainstream-explained`.
- Evidence-note filenames are fixed because many READMEs link to them: `pioneer-anomaly, flyby-anomaly, galaxy-rotation, wide-binaries, globular-clusters, dwarf-galaxies, cosmic-acceleration, cosmology, emdrive, lab-tests, propulsion, derivation, other-anomalies`.

## Adding a source: checklist
1. Check that it isn't already here: `grep -ril "<doi or arxiv id>" */*/README.md`.
2. Create `<section>/<id>/`. Copy the template to `README.md`.
3. If it's open access, download it into its own folder (`curl -L -A "Mozilla/5.0" -o paper.pdf …`) and confirm `file paper.pdf` says "PDF document". Determine `license`.
4. Extract text **to a scratch directory, not the repo**: `pdftotext -layout paper.pdf /tmp/…/text.txt`. Render figure pages with `pdftoppm -png -r 110 -f N -l N`. (Install `poppler` if these are missing.)
5. Fill in the README and `citation.bib`. Add relative links to related sources and evidence notes, and add a back-link from the relevant evidence note.
6. Run `python3 -I _tools/build_index.py` (rebuilds the section `INDEX.md` tables between the `AUTO-INDEX` markers, then checks every relative link and must end "No broken relative links."). Then run `python3 -I _tools/build_master_index.py` and `cat */*/citation.bib > bibliography.bib`.
7. If the source is local only, add its PDF and figures to `.gitignore`.

Do not hand-edit the content between `<!-- BEGIN AUTO-INDEX -->` and `<!-- END AUTO-INDEX -->`, or the top-level `INDEX.md`; both are generated.

## Known gotchas
- **`ptep-online.com` is now a gambling spam site.** Progress in Physics lives at `progress-in-physics.com`.
- **MDPI** blocks scripted PDF downloads from `mdpi.com`. This pattern works: `https://mdpi-res.com/d_attachment/<journal>/<journal>-VV-NNNNN/article_deploy/<journal>-VV-NNNNN.pdf`.
- Springer, OUP, ScienceDirect and ResearchGate often return 403 or a bot check. Look for an arXiv copy or an institutional repository instead (e.g. the Universitat de Lleida DSpace API for Giné's papers).
- Semantic Scholar rate-limits quickly (429). OpenAlex and Crossref are more reliable.
- Wikipedia has **no** "Quantized inertia" article, and "Mike McCulloch" there is a footballer.
- **Θ (cosmic horizon scale) is not constant across QI papers**: 2.6–2.7 × 10²⁶ m (2007–2013) vs 8.8 × 10²⁶ m (2017 onward). Always say which value a number uses.
- **Photon-rocket limit:** 1/c ≈ 3.3 nN/W = 3.3 µN/kW, not µN/W. IVO's claimed ~45–52 mN/W is about 10⁷ times it.
- The QI co-author is **Jaume** Giné (Lleida), not José. José Luis Pérez-Díaz (Alcalá) was the DARPA experimentalist.
- Treat downloaded files as untrusted. Keep scripts outside download folders, and run Python with `-I`.

## Git
- Default branch `main`. Commit author email: `3190879+DavidBowdoin@users.noreply.github.com`; never commit a personal email.
- End commit messages with the attribution line the session asks for (if any).
- Ask the user before pushing, changing repository visibility, or deleting anything remote.

## Good next work (see `08-synthesis/ideas-and-tests.md`)
- A1: refit SPARC with fixed Θ against MOND in a new `09-analysis/` folder (the data are public).
- Track new arXiv papers and blog posts (physicsfromtheedge.blogspot.com).
- Resolve the `[!UNVERIFIED]` items, especially paywalled papers summarised from their abstracts.
