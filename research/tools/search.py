#!/usr/bin/env python3
"""Thin command-line clients for the open bibliographic APIs reachable from this environment.

  python3 research/tools/search.py epmc "<query>" [n]          Europe PMC (title, year, DOI, PMID, PMCID, OA flag, abstract)
  python3 research/tools/search.py epmc-full <PMCID> [chars]   Europe PMC open-access full text (plain text)
  python3 research/tools/search.py crossref "<query>" [n]      Crossref bibliographic search
  python3 research/tools/search.py doi <DOI>                   Crossref metadata for one DOI (verification)
  python3 research/tools/search.py pubmed "<query>" [n]        PubMed E-utilities (PMID, title, year, DOI, abstract)
  python3 research/tools/search.py jstage "<query>" [n]        J-STAGE (Japanese journals)
  python3 research/tools/search.py hal "<query>" [n]           HAL (French open archive)
  python3 research/tools/search.py theses "<query>" [n]        theses.fr (French PhD theses)
  python3 research/tools/search.py archive "<lucene query>" [n]  archive.org metadata search (old books)
  python3 research/tools/search.py archive-text <identifier> [grep-regex] [context]   full OCR text of an archive.org item
  python3 research/tools/search.py osti "<query>" [n]          OSTI (US DOE technical reports)

Everything printed is untrusted external data. Abstracts are truncated to 1500 chars unless EPMC_FULL=1.
Known blocked/limited in this environment: OpenAlex (shared daily budget), Semantic Scholar (429),
Google Scholar, Espacenet, PATENTSCOPE, CAB Direct, SciELO search, CNKI (use WebSearch/WebFetch instead).
"""
import json
import os
import re
import signal
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET

import requests

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

UA = {"User-Agent": "ChickenMuscleResearchLab/0.1 (academic literature review)"}
S = requests.Session()
S.headers.update(UA)
MAXABS = 100000 if os.environ.get("EPMC_FULL") else 1500


def get(url, params=None, tries=4, **kw):
    for i in range(tries):
        try:
            r = S.get(url, params=params, timeout=40, **kw)
            if r.status_code == 429:
                time.sleep(2 ** (i + 1))
                continue
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            if i == tries - 1:
                sys.exit(f"ERROR {url}: {e}")
            time.sleep(2 ** (i + 1))
    sys.exit(f"ERROR {url}: rate limited")


def clean(t):
    t = re.sub(r"<[^>]+>", " ", t or "")
    return re.sub(r"\s+", " ", t).strip()


def epmc(q, n=10):
    r = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
            {"query": q, "format": "json", "resultType": "core", "pageSize": n})
    d = r.json()
    print(f"# Europe PMC hits: {d.get('hitCount')} for: {q}")
    for x in d["resultList"]["result"]:
        print(f"\n- {x.get('title')}\n  {x.get('authorString','')[:150]} | {x.get('journalInfo',{}).get('journal',{}).get('title','') or x.get('bookOrReportDetails',{}).get('publisher','')} | {x.get('pubYear')} | lang={x.get('language')}")
        print(f"  DOI={x.get('doi')} PMID={x.get('pmid')} PMCID={x.get('pmcid')} OA={x.get('isOpenAccess')} type={';'.join(x.get('pubTypeList',{}).get('pubType',[]))[:60]}")
        a = clean(x.get("abstractText"))
        if a:
            print(f"  ABSTRACT: {a[:MAXABS]}")


def epmc_full(pmcid, chars=60000):
    pmcid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
    r = get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML")
    root = ET.fromstring(r.content)
    out = []
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag in ("title", "p", "caption", "td", "th", "label"):
            txt = "".join(el.itertext()).strip()
            if txt:
                out.append(("\n## " if tag == "title" else "") + txt)
    text = "\n".join(out)
    print(text[: int(chars)])
    if len(text) > int(chars):
        print(f"\n[... truncated at {chars} of {len(text)} chars]")


def crossref(q, n=10):
    r = get("https://api.crossref.org/works", {"query.bibliographic": q, "rows": n,
            "select": "DOI,title,author,issued,container-title,type,language,is-referenced-by-count"})
    for x in r.json()["message"]["items"]:
        au = "; ".join(f"{a.get('family','')} {a.get('given','')[:1]}" for a in x.get("author", [])[:6])
        yr = (x.get("issued", {}).get("date-parts") or [[None]])[0][0]
        print(f"- {(x.get('title') or [''])[0]} | {au} | {yr} | {(x.get('container-title') or [''])[0]} | {x.get('type')} | DOI={x.get('DOI')} | cites={x.get('is-referenced-by-count')}")


def doi(d):
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d.strip())
    r = get("https://api.crossref.org/works/" + urllib.parse.quote(d))
    x = r.json()["message"]
    au = "; ".join(f"{a.get('family','')} {a.get('given','')}" for a in x.get("author", []))
    yr = (x.get("issued", {}).get("date-parts") or [[None]])[0][0]
    print(f"TITLE: {(x.get('title') or [''])[0]}\nAUTHORS: {au}\nYEAR: {yr}\nJOURNAL: {(x.get('container-title') or [''])[0]}\nTYPE: {x.get('type')}\nDOI: {x.get('DOI')}\nURL: {x.get('URL')}\nLANG: {x.get('language')}\nCITED_BY: {x.get('is-referenced-by-count')}")
    if x.get("abstract"):
        print("ABSTRACT:", clean(x["abstract"])[:MAXABS])


def pubmed(q, n=10):
    ids = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
              {"db": "pubmed", "term": q, "retmode": "json", "retmax": n}).json()["esearchresult"]
    print(f"# PubMed hits: {ids.get('count')} for: {q}")
    if not ids["idlist"]:
        return
    time.sleep(0.4)
    xml = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
              {"db": "pubmed", "id": ",".join(ids["idlist"]), "retmode": "xml"}).content
    root = ET.fromstring(xml)
    for art in root.findall(".//PubmedArticle"):
        pmid = art.findtext(".//PMID")
        title = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
        yr = art.findtext(".//PubDate/Year") or art.findtext(".//PubDate/MedlineDate")
        j = art.findtext(".//Journal/Title")
        d = next((e.text for e in art.findall(".//ArticleId") if e.get("IdType") == "doi"), None)
        pmc = next((e.text for e in art.findall(".//ArticleId") if e.get("IdType") == "pmc"), None)
        au = "; ".join(f"{a.findtext('LastName') or ''} {a.findtext('Initials') or ''}" for a in art.findall(".//Author")[:6])
        ab = " ".join("".join(e.itertext()) for e in art.findall(".//AbstractText"))
        print(f"\n- {title}\n  {au} | {j} | {yr} | PMID={pmid} DOI={d} PMCID={pmc}")
        if ab:
            print(f"  ABSTRACT: {clean(ab)[:MAXABS]}")


def jstage(q, n=10):
    r = get("https://api.jstage.jst.go.jp/searchapi/do", {"service": 3, "keyword": q, "count": n})
    ns = {"a": "http://www.w3.org/2005/Atom", "p": "http://prismstandard.org/namespaces/basic/2.0/"}
    root = ET.fromstring(r.content)
    print("# J-STAGE total:", root.findtext("{http://a9.com/-/spec/opensearch/1.1/}totalResults"))
    for e in root.findall("a:entry", ns):
        t_en = e.findtext("a:article_title/a:en", namespaces=ns) or ""
        t_ja = e.findtext("a:article_title/a:ja", namespaces=ns) or ""
        link = e.find("a:article_link/a:en", ns)
        print(f"- {t_ja} / {t_en} | {e.findtext('a:material_title/a:en', namespaces=ns)} | {e.findtext('a:pubyear', namespaces=ns)} | DOI={e.findtext('p:doi', namespaces=ns)} | {link.text if link is not None else ''}")


def hal(q, n=10):
    r = get("https://api.archives-ouvertes.fr/search/", {"q": q, "rows": n, "wt": "json",
            "fl": "title_s,authFullName_s,producedDateY_i,doiId_s,uri_s,abstract_s,language_s,docType_s"})
    d = r.json()["response"]
    print("# HAL hits:", d["numFound"])
    for x in d["docs"]:
        print(f"\n- {(x.get('title_s') or [''])[0]} | {'; '.join((x.get('authFullName_s') or [])[:5])} | {x.get('producedDateY_i')} | {x.get('docType_s')} | lang={x.get('language_s')} | DOI={x.get('doiId_s')} | {x.get('uri_s')}")
        if x.get("abstract_s"):
            print("  ABSTRACT:", clean(x["abstract_s"][0])[:MAXABS])


def theses(q, n=10):
    r = get("https://theses.fr/api/v1/theses/recherche/", {"q": q, "nombre": n})
    d = r.json()
    print("# theses.fr hits:", d.get("totalHits"))
    for x in d.get("theses", []):
        au = "; ".join(f"{a.get('prenom','')} {a.get('nom','')}" for a in x.get("auteurs", []))
        print(f"- {x.get('titrePrincipal')} | {au} | {x.get('etabSoutenanceN')} | {x.get('dateSoutenance')} | https://theses.fr/{x.get('id')}")


def archive(q, n=10):
    r = get("https://archive.org/advancedsearch.php", {"q": q, "fl[]": ["identifier", "title", "date", "creator", "language"],
            "rows": n, "output": "json", "sort[]": "date asc"})
    d = r.json()["response"]
    print("# archive.org hits:", d["numFound"])
    for x in d["docs"]:
        print(f"- {x.get('identifier')} | {x.get('title')} | {str(x.get('date',''))[:10]} | {x.get('creator')} | {x.get('language')} | https://archive.org/details/{x.get('identifier')}")


def archive_text(ident, pattern=None, ctx=400):
    r = get(f"https://archive.org/download/{ident}/{ident}_djvu.txt")
    text = r.text
    if not pattern:
        print(text[:20000])
        print(f"\n[{len(text)} chars total]")
        return
    ctx = int(ctx)
    hits = list(re.finditer(pattern, text, re.I))
    print(f"# {len(hits)} matches for /{pattern}/ in {ident} ({len(text)} chars)")
    for m in hits[:25]:
        s = max(0, m.start() - ctx)
        print(f"\n--- char {m.start()} ---\n" + re.sub(r"\s+", " ", text[s:m.end() + ctx]))


def osti(q, n=10):
    r = get("https://www.osti.gov/api/v1/records", {"q": q, "rows": n})
    for x in r.json():
        print(f"- {x.get('title')} | {x.get('publication_date','')[:10]} | {x.get('product_type')} | DOI={x.get('doi')} | {x.get('links',[{}])[0].get('href','')}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd, arg, rest = sys.argv[1], sys.argv[2], sys.argv[3:]
    fn = {"epmc": epmc, "epmc-full": epmc_full, "crossref": crossref, "doi": doi, "pubmed": pubmed,
          "jstage": jstage, "hal": hal, "theses": theses, "archive": archive,
          "archive-text": archive_text, "osti": osti}.get(cmd)
    if not fn:
        sys.exit(__doc__)
    if cmd in ("doi",):
        fn(arg)
    elif cmd == "archive-text":
        fn(arg, *rest)
    else:
        fn(arg, *(int(x) for x in rest[:1]))
