#!/usr/bin/env python3
"""Apply the public / local-only split recorded in _tools/licenses.json.

For every entry classified LOCAL it:
  1. lists the files in the LOCAL-ONLY block of .gitignore (regenerated each run),
  2. turns image embeds / links to those files in the folder's README into plain
     "(local only)" text, so nothing renders as broken on GitHub,
  3. inserts or refreshes a "📁 Local only" note under the README's H1.

Safe to rerun. After a change, run build_index.py; its link check also flags any
remaining link to an ignored file.

Usage: python3 -I _tools/apply_local_only.py

licenses.json entries look like:
  {"folder": "01-papers/<id>", "pdf_license": "arXiv-nonexclusive",
   "evidence_url": "...", "classification": "PUBLIC" | "LOCAL",
   "files": ["01-papers/<id>/paper.pdf", "01-papers/<id>/figures/fig-1-x.png"], "note": "..."}
A folder may have one PUBLIC and one LOCAL entry (e.g. PDF public, figures local).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LICENSES = ROOT / "_tools" / "licenses.json"
MARK = "<!-- local-only-note -->"
GI_START = "# BEGIN LOCAL-ONLY (licence does not permit redistribution; see AGENTS.md)"
GI_END = "# END LOCAL-ONLY"


def front_matter_value(fm, key):
    m = re.search(rf"^{key}:[ \t]*\"?([^\"\s]+)", fm, re.M)
    return m.group(1) if m and m.group(1) not in ("null", '""') else None


def read_links(fm):
    links = []
    if arxiv := front_matter_value(fm, "arxiv"):
        links.append(f"[arXiv:{arxiv}](https://arxiv.org/abs/{arxiv})")
    if doi := front_matter_value(fm, "doi"):
        links.append(f"[doi:{doi}](https://doi.org/{doi})")
    if not links and (url := front_matter_value(fm, "url")):
        links.append(f"[source]({url})")
    return " · ".join(links) or "the publisher"


def local_note(names, lic, fm):
    if "paper.pdf" in names:
        why = ('NTRS\'s "public use permitted" is not an open licence' if lic.startswith("NTRS")
               else f"this copy's licence (`{lic}`) does not permit redistribution")
        return (f"> 📁 **Local only:** the stored PDF and its rendered figures are kept out of the public "
                f"repository because {why}. Read the paper at {read_links(fm)}.")
    if any(n.startswith("figures/") for n in names):
        return (f"> 📁 **Local only:** the figures rendered from this paper are kept out of the public repository "
                f"(`{lic}` does not permit derivatives). The PDF itself is included; each figure caption below "
                f"links to its page in the PDF.")
    others = ", ".join(f"`{n}`" for n in sorted(names))
    return (f"> 📁 **Local only:** {others} (licence `{lic}`) is kept out of the public repository. "
            f"The openly licensed `paper.pdf` is included.")


def update_gitignore(paths):
    gi = ROOT / ".gitignore"
    text = gi.read_text() if gi.exists() else ""
    block = "\n".join([GI_START, *sorted(paths), GI_END])
    if GI_START in text:
        text = re.sub(re.escape(GI_START) + ".*?" + re.escape(GI_END), lambda _: block, text, flags=re.S)
    else:
        text = text.rstrip("\n") + "\n\n" + block + "\n"
    gi.write_text(text)


def update_readme(folder, names, lic):
    readme = ROOT / folder / "README.md"
    text = readme.read_text()
    fm = re.match(r"^---\n.*?\n---\n", text, re.S).group(0)

    def neutralise(m):
        if m.group(2) not in names:
            return m.group(0)
        return f"*Figure (local only): {m.group(1)}*" if m.group(0).startswith("!") else f"{m.group(1)} *(local only)*"

    text = re.sub(r"!?\[([^\]]*)\]\(([^)\s]+)\)", neutralise, text)
    note = local_note(names, lic, fm)
    if MARK in text:
        text = re.sub(re.escape(MARK) + r"\n> .*\n", lambda _: f"{MARK}\n{note}\n", text, count=1)
    else:
        text = re.sub(r"^(# .+\n)", lambda m: f"{m.group(1)}\n{MARK}\n{note}\n", text, count=1, flags=re.M)
    readme.write_text(text)


def main():
    local = {}
    for entry in json.loads(LICENSES.read_text()):
        if entry["classification"] == "LOCAL":
            slot = local.setdefault(entry["folder"], {"files": set(), "license": entry["pdf_license"]})
            slot["files"].update(entry["files"])
    update_gitignore(f for v in local.values() for f in v["files"])
    for folder, v in local.items():
        update_readme(folder, {Path(f).relative_to(folder).as_posix() for f in v["files"]}, v["license"])
    print(f"{len(local)} folders marked; {sum(len(v['files']) for v in local.values())} files local-only")


if __name__ == "__main__":
    main()
