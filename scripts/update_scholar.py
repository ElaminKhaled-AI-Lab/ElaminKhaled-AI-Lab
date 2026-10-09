#!/usr/bin/env python3
"""
Refresh the Google Scholar figures in README.md, daily, via SerpAPI.

Why SerpAPI and not direct scraping: Google Scholar has no public API, direct
scraping breaches its terms, and Google blocks data-center address ranges --
which is exactly where GitHub Actions runners live. A direct scraper returns a
CAPTCHA page within days and writes nonsense while looking healthy. SerpAPI
operates the retrieval commercially and absorbs that problem.

Fails SOFT by design. Missing key, dead API, implausible numbers -> the README
is left untouched and the job exits 0. Yesterday's correct figures beat a
badge reading zero.
"""
import json, os, re, sys, urllib.parse, urllib.request
from datetime import datetime, timezone

KEY       = os.environ.get("SERPAPI_KEY", "").strip()
AUTHOR_ID = os.environ.get("SCHOLAR_ID", "oyrk6pwAAAAJ")
README    = os.environ.get("README_PATH", "README.md")

ORCID   = os.environ.get("ORCID", "0000-0001-9555-1814")
SCOPUS  = os.environ.get("SCOPUS_ID", "57797410200")
WOS     = os.environ.get("WOS_ID", "ADL-6823-2022")
SCIPROF = os.environ.get("SCIPROFILES_ID", "2153611")
EMAIL   = os.environ.get("CONTACT_EMAIL", "khaled@kumamoto-u.ac.jp")

START, END = "<!--METRICS:START-->", "<!--METRICS:END-->"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={AUTHOR_ID}"


def soft(msg):
    print(msg, file=sys.stderr)
    return 0


def fetch():
    q = urllib.parse.urlencode({
        "engine": "google_scholar_author",
        "author_id": AUTHOR_ID,
        "api_key": KEY,
        "num": 100,          # one call covers up to 100 articles
        "sort": "pubdate",
    })
    req = urllib.request.Request("https://serpapi.com/search?" + q,
                                 headers={"User-Agent": "profile-metrics"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def parse(d):
    """SerpAPI returns cited_by.table as a list of single-key dicts."""
    out = {}
    for row in ((d.get("cited_by") or {}).get("table") or []):
        for k, v in row.items():
            if isinstance(v, dict) and "all" in v:
                out[k] = v["all"]
    arts = d.get("articles") or []
    # 'articles' is capped at num=100; if it comes back full, there may be more.
    out["publications"] = len(arts)
    out["_articles_maybe_truncated"] = len(arts) >= 100
    return out


def badges(pubs, cites, h, i10, stamp):
    c = f"{cites:,}".replace(",", "%2C")
    return "\n".join([
        START,
        f"[![Publications](https://img.shields.io/badge/Publications-{pubs}-1f4e79?style=flat-square)]({SCHOLAR_URL})",
        f"[![Citations](https://img.shields.io/badge/Citations-{c}-1f4e79?style=flat-square)]({SCHOLAR_URL})",
        f"[![h-index](https://img.shields.io/badge/h--index-{h}-1f4e79?style=flat-square)]({SCHOLAR_URL})",
        f"[![i10-index](https://img.shields.io/badge/i10--index-{i10}-1f4e79?style=flat-square)]({SCHOLAR_URL})",
        "[![Lab](https://img.shields.io/badge/Lab-10_researchers-1f4e79?style=flat-square)](#background)",
        "[![Containment](https://img.shields.io/badge/Containment-BSL--2_%2F_BSL--3-1f4e79?style=flat-square)](#the-full-chain-in-one-group)",
        "",
        f"[![ORCID](https://img.shields.io/badge/ORCID-{ORCID.replace('-','--')}-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/{ORCID})",
        f"[![Scopus](https://img.shields.io/badge/Scopus-{SCOPUS}-E9711C?style=flat-square&logo=elsevier&logoColor=white)](https://www.scopus.com/authid/detail.uri?authorId={SCOPUS})",
        f"[![Web of Science](https://img.shields.io/badge/ResearcherID-{WOS.replace('-','--')}-5E33BF?style=flat-square&logo=clarivate&logoColor=white)](https://www.webofscience.com/wos/author/record/{WOS})",
        f"[![SciProfiles](https://img.shields.io/badge/SciProfiles-{SCIPROF}-004B87?style=flat-square)](https://sciprofiles.com/profile/{SCIPROF})",
        f"[![Google Scholar](https://img.shields.io/badge/Google_Scholar-Profile-4285F4?style=flat-square&logo=googlescholar&logoColor=white)]({SCHOLAR_URL})",
        f"[![Email](https://img.shields.io/badge/{EMAIL.replace('-','--')}-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:{EMAIL})",
        "",
        f"<sub>Figures from [Google Scholar]({SCHOLAR_URL}), refreshed automatically — "
        f"last updated <!--ASOF-->{stamp}<!--/ASOF-->.</sub>",
        END,
    ])


def main():
    if not KEY:
        return soft("SERPAPI_KEY is not set. README unchanged. "
                    "Add it at Settings > Secrets and variables > Actions.")
    try:
        d = fetch()
    except Exception as e:
        return soft(f"SerpAPI request failed: {e}. README unchanged.")

    if d.get("error"):
        return soft(f"SerpAPI error: {d['error']}. README unchanged.")

    m = parse(d)
    pubs  = m.get("publications", 0)
    cites = m.get("citations", 0)
    h     = m.get("h_index", 0)
    i10   = m.get("i10_index", 0)

    # Sanity floors. A bad response or a wrong author id would otherwise
    # rewrite the profile with near-zero figures.
    if pubs < 10 or cites < 100 or h < 5:
        return soft(f"Implausible: pubs={pubs} cites={cites} h={h}. README unchanged.")
    if h > pubs:
        return soft(f"h-index ({h}) exceeds publications ({pubs}). README unchanged.")

    if m.get("_articles_maybe_truncated"):
        print("NOTE: 100 articles returned; the real count may be higher. "
              "Pagination needed if this persists.", file=sys.stderr)

    print(f"Scholar: pubs={pubs} citations={cites} h={h} i10={i10}")

    t = open(README, encoding="utf-8").read()
    if START not in t or END not in t:
        print(f"Markers not found in {README}.", file=sys.stderr)
        return 1

    stamp = datetime.now(timezone.utc).strftime("%-d %B %Y")
    out = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 lambda _: badges(pubs, cites, h, i10, stamp), t, flags=re.S)
    open(README, "w", encoding="utf-8").write(out)
    print("README written." if out != t else "Figures unchanged; stamp refreshed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
