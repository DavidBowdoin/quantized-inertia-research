#!/usr/bin/env python3
"""Look up the licence of a source by arXiv id and/or DOI, to decide PUBLIC vs LOCAL.

Usage:
  python3 -I _tools/check_license.py --arxiv 1908.01589
  python3 -I _tools/check_license.py --doi 10.1007/s12567-021-00366-4
  python3 -I _tools/check_license.py --arxiv 1105.1873 --doi 10.1140/epjc/s10052-012-1884-6

arXiv: reads <license> from the OAI-PMH record. No element means arXiv's default
non-exclusive licence, which does not permit redistribution. The licence can differ
between versions; check the abs page for the exact version you store.
DOI: prints Crossref's licence entries (content-version "vor" is the published version)
and OpenAlex's open-access locations.

Always confirm against the licence statement inside the PDF you actually store, then
record the result in _tools/licenses.json and run apply_local_only.py.
"""
import argparse
import json
import re
import urllib.request

UA = {"User-Agent": "quantized-inertia-research licence check (https://github.com/DavidBowdoin/quantized-inertia-research)"}
OPEN = ("creativecommons.org", "publicdomain")


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def arxiv(aid):
    xml = fetch(f"https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:{aid}&metadataPrefix=arXiv")
    m = re.search(r"<license>(.*?)</license>", xml)
    lic = m.group(1) if m else None
    verdict = "PUBLIC" if lic and any(o in lic for o in OPEN) else "LOCAL"
    print(f"arXiv {aid}: {lic or 'no <license> element (arXiv default non-exclusive)'} -> {verdict}")


def doi(d):
    msg = json.loads(fetch(f"https://api.crossref.org/works/{d}"))["message"]
    lics = msg.get("license", [])
    for lic in lics:
        print(f"Crossref {d}: {lic['URL']} ({lic.get('content-version')})")
    if not lics:
        print(f"Crossref {d}: no licence recorded")
    vor_open = any(any(o in lic["URL"] for o in OPEN) and lic.get("content-version") in ("vor", None) for lic in lics)
    try:
        work = json.loads(fetch(f"https://api.openalex.org/works/doi:{d}"))
        for loc in work.get("locations", []):
            print(f"  OpenAlex: {loc.get('license')} {loc.get('version')} {loc.get('pdf_url')}")
    except Exception as e:  # OpenAlex is a convenience; Crossref is the record
        print(f"  OpenAlex lookup failed: {e}")
    print(f"-> published version {'PUBLIC' if vor_open else 'LOCAL (no open licence recorded)'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--arxiv")
    ap.add_argument("--doi")
    args = ap.parse_args()
    if not (args.arxiv or args.doi):
        ap.error("give --arxiv and/or --doi")
    if args.arxiv:
        arxiv(args.arxiv)
    if args.doi:
        doi(args.doi)
