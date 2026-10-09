#!/usr/bin/env python3
"""
Refresh the publication, citation, and h-index badges in README.md from
OpenAlex.

Design notes:
  * OpenAlex is used because it is free, official, needs no API key, and
    returns all three numbers. Google Scholar has no public API; scraping it
    breaches its terms and Google blocks data-center addresses, so a scheduled
    job against Scholar would fail within days.
  * The script fails SOFT. If the API is unreachable or returns nothing
    plausible, the README is left exactly as it is and the job exits 0. A
    profile showing yesterday's correct numbers beats one showing "0".
  * Only the block between the METRICS markers is ever rewritten.
"""
import json, os, re, sys, urllib.request, urllib.error
from datetime import datetime, timezone

ORCID   = os.environ.get("ORCID", "0000-0001-9555-1814")
MAILTO  = os.environ.get("OPENALEX_MAILTO", "dr.khaledalamin86@gmail.com")
README  = os.environ.get("README_PATH", "README.md")
SCHOLAR = os.environ.get("SCHOLAR_ID", "oyrk6pwAAAAJ")
SCOPUS  = os.environ.get("SCOPUS_ID", "57797410200")
SCIPROF = os.environ.get("SCIPROFILES_ID", "2153611")
EMAIL   = os.environ.get("CONTACT_EMAIL", "khaled@kumamoto-u.ac.jp")

START, END = "<!--METRICS:START-->", "<!--METRICS:END-->"
UA = {"User-Agent": f"github-profile-metrics (mailto:{MAILTO})"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def fetch():
    """Try the canonical ORCID path, then the filter form."""
    for url in (
        f"https://api.openalex.org/authors/https://orcid.org/{ORCID}",
        f"https://api.openalex.org/authors?filter=orcid:{ORCID}",
    ):
        try:
            d = get(url)
        except Exception as e:
            print(f"  {url} -> {e}", file=sys.stderr)
            continue
        if "results" in d:
            if not d["results"]:
                print("  filter form returned 0 results", file=sys.stderr)
                continue
            d = d["results"][0]
        if d.get("works_count"):
            return d
    return None


def thousands(n):
    return f"{n:,}"


def build(works, cites, h, i10, stamp):
    """The badge block. %2C is a comma; -- is a literal hyphen to shields.io."""
    return "\n".join([
        START,
        f"[![Publications](https://img.shields.io/badge/Publications-{works}-1f4e79?style=flat-square)](https://openalex.org/works?filter=author.orcid:{ORCID})",
        f"[![Citations](https://img.shields.io/badge/Citations-{thousands(cites).replace(',', '%2C')}-1f4e79?style=flat-square)](https://openalex.org/authors/orcid:{ORCID})",
        f"[![h-index](https://img.shields.io/badge/h--index-{h}-1f4e79?style=flat-square)](https://openalex.org/authors/orcid:{ORCID})",
        f"[![i10-index](https://img.shields.io/badge/i10--index-{i10}-1f4e79?style=flat-square)](https://openalex.org/authors/orcid:{ORCID})",
        "[![Lab](https://img.shields.io/badge/Lab-10_researchers-1f4e79?style=flat-square)](#background)",
        "",
        f"[![ORCID](https://img.shields.io/badge/ORCID-{ORCID.replace('-', '--')}-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/{ORCID})",
        f"[![Scopus](https://img.shields.io/badge/Scopus-{SCOPUS}-E9711C?style=flat-square&logo=elsevier&logoColor=white)](https://www.scopus.com/authid/detail.uri?authorId={SCOPUS})",
        f"[![SciProfiles](https://img.shields.io/badge/SciProfiles-{SCIPROF}-004B87?style=flat-square)](https://sciprofiles.com/profile/{SCIPROF})",
        f"[![Google Scholar](https://img.shields.io/badge/Google_Scholar-Profile-4285F4?style=flat-square&logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user={SCHOLAR})",
        f"[![Email](https://img.shields.io/badge/{EMAIL.replace('-', '--')}-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:{EMAIL})",
        "",
        f"<sub>Publication, citation, and index figures from "
        f"[OpenAlex](https://openalex.org/authors/orcid:{ORCID}), "
        f"updated automatically — last refreshed {stamp}.</sub>",
        END,
    ])


def main():
    a = fetch()
    if not a:
        print("No usable OpenAlex record. README unchanged.", file=sys.stderr)
        return 0

    s     = a.get("summary_stats") or {}
    works = a.get("works_count") or 0
    cites = a.get("cited_by_count") or 0
    h     = s.get("h_index") or 0
    i10   = s.get("i10_index") or 0

    # Sanity floor: a plausible record for this author is never near zero.
    # Catches a disambiguation split or a bad response rewriting the badges
    # with nonsense.
    if works < 5 or cites < 10:
        print(f"Implausible: works={works} cites={cites}. README unchanged.",
              file=sys.stderr)
        return 0

    print(f"OpenAlex: {a.get('display_name')} | works={works} "
          f"cites={cites} h={h} i10={i10}")

    p = open(README, encoding="utf-8").read()
    if START not in p or END not in p:
        print(f"Markers {START} / {END} not found in {README}.", file=sys.stderr)
        return 1

    stamp = datetime.now(timezone.utc).strftime("%d %B %Y")
    new   = build(works, cites, h, i10, stamp)
    out   = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: new,
                   p, flags=re.S)

    if out == p:
        print("No change.")
        return 0

    open(README, "w", encoding="utf-8").write(out)
    print("README.md updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
