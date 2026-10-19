#!/usr/bin/env python3
"""Rebuild INDEX.md tables from source-folder front-matter and check relative links.

Usage: python3 -I _tools/build_index.py [--check-only]
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIRS = ["01-papers", "03-criticism", "04-experiments", "07-media"]
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
BEGIN, END = "<!-- BEGIN AUTO-INDEX -->", "<!-- END AUTO-INDEX -->"


def parse_front_matter(text):
    """Minimal YAML subset: scalar `key: value` and inline `[a, b]` lists."""
    m = FM_RE.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, val = line.split(":", 1)
        val = val.split(" #")[0].strip().strip('"')
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
        data[key.strip()] = val
    return data


def link(url, label):
    return f"[{label}]({url})" if url and url not in ("null", "None") else ""


def build_table(section):
    rows = []
    for readme in sorted((ROOT / section).glob("*/README.md")):
        fm = parse_front_matter(readme.read_text())
        authors = fm.get("authors") or []
        if isinstance(authors, str):
            authors = [authors]
        first = authors[0].split()[-1] if authors else ""
        who = first + (" et al." if len(authors) > 2 else (f" & {authors[1].split()[-1]}" if len(authors) == 2 else ""))
        doi = fm.get("doi")
        arxiv = fm.get("arxiv")
        ids = " ".join(filter(None, [
            link(f"https://doi.org/{doi}" if doi and doi != "null" else None, "DOI"),
            link(f"https://arxiv.org/abs/{arxiv}" if arxiv and arxiv != "null" else None, "arXiv"),
        ]))
        title = fm.get("title", readme.parent.name).replace("|", "\\|")
        oa = "✅" if str(fm.get("open_access")).lower() == "true" else ""
        rows.append((str(fm.get("year", "")), f"| {fm.get('year','')} | [{title}]({readme.parent.name}/README.md) | {who} | {fm.get('venue','').replace('|','/')} | {fm.get('status','')} | {oa} | {ids} |"))
    rows.sort(key=lambda r: r[0])
    head = "| Year | Title | Authors | Venue | Status | OA | Links |\n|---|---|---|---|---|---|---|"
    return f"{head}\n" + "\n".join(r[1] for r in rows) + f"\n\n_{len(rows)} sources._"


def write_index(section):
    idx = ROOT / section / "INDEX.md"
    table = build_table(section)
    text = idx.read_text() if idx.exists() else f"# {section}\n\n{BEGIN}\n{END}\n"
    if BEGIN not in text:
        text += f"\n{BEGIN}\n{END}\n"
    text = re.sub(re.escape(BEGIN) + ".*?" + re.escape(END), f"{BEGIN}\n{table}\n{END}", text, flags=re.S)
    idx.write_text(text)


def check_links():
    broken = []
    for md in ROOT.rglob("*.md"):
        if any(p.startswith((".", "_")) for p in md.relative_to(ROOT).parts):
            continue
        for target in LINK_RE.findall(md.read_text()):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = (md.parent / target.split("#")[0]).resolve()
            if not path.exists():
                broken.append(f"{md.relative_to(ROOT)} -> {target}")
            elif is_git_ignored(path):
                broken.append(f"{md.relative_to(ROOT)} -> {target} (local-only file; broken on GitHub)")
    return broken


def is_git_ignored(path):
    """True if git ignores the path (local-only content that is not published)."""
    r = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", str(path)], capture_output=True)
    return r.returncode == 0


if __name__ == "__main__":
    if "--check-only" not in sys.argv:
        for s in SOURCE_DIRS:
            if (ROOT / s).is_dir():
                write_index(s)
    broken = check_links()
    print("\n".join(broken) if broken else "No broken relative links.")
    sys.exit(1 if broken else 0)
