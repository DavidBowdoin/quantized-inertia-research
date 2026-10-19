#!/usr/bin/env python3
"""Regenerate the top-level INDEX.md listing every note and source. Run from repo root: python3 -I _tools/build_master_index.py"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = [("00-overview", "Overview"), ("02-evidence", "Evidence"), ("05-context", "Context physics"),
            ("06-people-orgs", "People & organisations"), ("08-synthesis", "Synthesis"), ("01-papers", "Papers"),
            ("03-criticism", "Criticism & null results"), ("04-experiments", "Experiments"), ("07-media", "Books, press & media")]


def title(p):
    t = p.read_text()
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', t, re.M) or re.search(r"^#\s+(.*)$", t, re.M)
    return m.group(1) if m else p.stem


out = ["# Master index", "", "Every note and source in the repository. Section tables with year, status and links are in each folder's `INDEX.md`. Regenerate with `python3 -I _tools/build_master_index.py`.", ""]
for d, name in SECTIONS:
    out.append(f"## [{name}]({d}/INDEX.md)")
    ps = sorted((ROOT / d).glob("*/README.md")) or sorted(p for p in (ROOT / d).glob("*.md") if p.name != "INDEX.md")
    out += [f"- [{title(p)}]({p.relative_to(ROOT).as_posix()})" for p in ps] + [""]
out.append("## Assets\n- [Diagrams](assets/diagrams/README.md)\n- [Bibliography (BibTeX)](bibliography.bib)\n- [Source README template](_templates/source-README.md)\n")
(ROOT / "INDEX.md").write_text("\n".join(out))
