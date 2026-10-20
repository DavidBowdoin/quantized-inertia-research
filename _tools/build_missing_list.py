#!/usr/bin/env python3
"""Regenerate the table in MISSING-PDFS.md: sources that have no PDF stored yet.

A source counts as missing when its folder holds no *.pdf file. Press items, and
folders listed in NOT_APPLICABLE (sources that are not documents), are skipped.
The table is sorted by priority: [!UNVERIFIED] flags in the README (a rough measure
of how much a full text would add), then by section (criticism and experiments
first, since they test QI directly).

Usage: python3 -I _tools/build_missing_list.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "MISSING-PDFS.md"
BEGIN, END = "<!-- BEGIN AUTO-MISSING -->", "<!-- END AUTO-MISSING -->"
NOT_APPLICABLE = {"07-media/2023-quantizedinertia-website"}
SECTION_RANK = {"03-criticism": 0, "04-experiments": 1, "01-papers": 2, "07-media": 3}

# Where to get it, keyed by DOI prefix or URL fragment. First match wins.
ROUTES = [
    ("10.1016/", "Elsevier (ScienceDirect): pay-per-view, a library, or ask the authors"),
    ("10.1007/", "Springer: pay-per-view, a library, or ask the authors"),
    ("10.1134/", "Pleiades/Springer: pay-per-view, a library, or ask the authors"),
    ("10.1142/9", "World Scientific book: buy, or borrow via interlibrary loan"),
    ("10.1142/", "World Scientific: pay-per-view, a library, or ask the authors"),
    ("10.1209/", "IOP/EPL: pay-per-view, a library, or ask the authors"),
    ("10.31988/", "Page removed and not archived: ask McCulloch"),
    ("researchgate.net", "ResearchGate: download in a browser (free login)"),
    ("bis-space.com", "British Interplanetary Society shop, or ask the author"),
]


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    data = {}
    for line in (m.group(1) if m else "").splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            data[k.strip()] = v.split(" #")[0].strip().strip('"')
    return data


def route(fm, venue):
    key = " ".join(filter(None, [fm.get("doi", ""), fm.get("url", "")])).lower()
    for frag, text in ROUTES:
        if frag in key:
            return text
    if "book" in fm.get("type", "") or "Books" in venue:
        return "Book: buy, or borrow via interlibrary loan"
    return "Ask the author"


def rows():
    out = []
    for readme in ROOT.glob("0[1347]-*/*/README.md"):  # source sections only
        folder = readme.parent
        rel = folder.relative_to(ROOT).as_posix()
        if rel in NOT_APPLICABLE or any(folder.glob("*.pdf")):
            continue
        text = readme.read_text()
        fm = front_matter(text)
        if fm.get("type") == "press":
            continue
        doi = fm.get("doi") if fm.get("doi") not in (None, "", "null") else None
        url = fm.get("url") if fm.get("url") not in (None, "", "null") else None
        link = f"[doi:{doi}](https://doi.org/{doi})" if doi else (f"[link]({url})" if url else "")
        venue = fm.get("venue", "").replace("|", "/")
        flags = text.count("[!UNVERIFIED]")
        out.append((-flags, SECTION_RANK.get(rel.split("/")[0], 9), rel,
                    f"| {flags} | [{fm.get('title', folder.name).replace('|', '/')}]({rel}/README.md) | {fm.get('year', '')} | {venue} | {link} | {route(fm, venue)} |"))
    out.sort()
    return [r[-1] for r in out]


def main():
    lines = rows()
    table = ("| Flags | Source | Year | Venue | Link | How to get it |\n|---|---|---|---|---|---|\n"
             + "\n".join(lines) + f"\n\n_{len(lines)} sources without a PDF. \"Flags\" = `[!UNVERIFIED]` markers in the README; higher means the full text would settle more._")
    text = TARGET.read_text()
    text = re.sub(re.escape(BEGIN) + ".*?" + re.escape(END), lambda _: f"{BEGIN}\n{table}\n{END}", text, flags=re.S)
    TARGET.write_text(text)
    print(f"{len(lines)} missing")


if __name__ == "__main__":
    main()
