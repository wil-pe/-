#!/usr/bin/env python3
"""Coordinator quality audit — independent of the agents that wrote the tables.

  python3 research/tools/audit.py consistency      # rule-based checks on all agent tables
  python3 research/tools/audit.py refs [AGENT]     # resolve every DOI (Crossref) and PMID (PubMed) and compare titles/years
  python3 research/tools/audit.py coverage         # rebuild coordination/coverage_auto.md from search logs and tables

Writes reports to research/coordination/audit_*.md. Never edits agent tables.
"""
import csv
import re
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
AG = ["H", "N", "C", "A", "E", "P", "X"]
S = requests.Session()
S.headers["User-Agent"] = "ChickenMuscleResearchLab-audit/0.1"


def rows(agent, table):
    p = ROOT / "agents" / agent / f"{table}.csv"
    if not p.exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t.lower())).strip()


def sim(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    ta, tb = set(a.split()), set(b.split())
    jac = len(ta & tb) / max(1, len(ta | tb))
    return max(jac, SequenceMatcher(None, a, b).ratio())


def consistency():
    src = {r["source_id"]: r for a in AG for r in rows(a, "sources")}
    issues = defaultdict(list)
    for sid, r in src.items():
        if r["access_level"] in ("full_text_read", "partial_text_read") and not (r.get("url") or r.get("doi") or r.get("pmid")):
            issues["full text claimed without any locator (url/doi/pmid)"].append(sid)
        if r["source_type"] in ("peer_reviewed_article", "review", "systematic_review", "meta_analysis") and not (r.get("doi") or r.get("pmid") or r.get("url")):
            issues["article without DOI/PMID/URL"].append(sid)
        if r["verification_status"] == "verified_primary" and r["access_level"] in ("metadata_only", "secondary_report", "paywalled_not_read"):
            issues["verified_primary but primary text not read"].append(sid)
        if r.get("year") and not re.match(r"^-?\d{1,4}(\s*[-–/]\s*\d{1,4})?$|^(c\.|ca\.|~)", r["year"].strip()):
            issues["non-standard year"].append(f"{sid}={r['year']}")
    for a in AG:
        for e in rows(a, "evidence"):
            ids = [s for s in re.split(r"[;, ]+", e["source_id"]) if s]
            levels = [src[s]["access_level"] for s in ids if s in src]
            if any(s not in src for s in ids):
                issues["evidence citing unknown source"].append(e["claim_id"])
            if levels and all(l == "abstract_only" for l in levels) and re.search(r"\b(table|tableau|fig|figure|p\.\s*\d|page)\b", e.get("locator", ""), re.I):
                issues["abstract-only source but locator cites table/figure/page"].append(e["claim_id"])
            if levels and all(l in ("metadata_only", "secondary_report", "paywalled_not_read") for l in levels) and e["confidence"] in ("high", "moderate"):
                issues["moderate/high confidence resting only on unread/secondary sources"].append(e["claim_id"])
            if e["evidence_type"] in ("commercial_claim", "patent_claim", "expert_opinion", "theoretical") and e["confidence"] == "high":
                issues["high confidence on commercial/patent/opinion/theory"].append(e["claim_id"])
            if not e.get("quote_original") and levels and any(l in ("full_text_read", "partial_text_read", "abstract_only") for l in levels):
                issues["no justifying quote although text was read"].append(e["claim_id"])
        for q in rows(a, "quant"):
            if q["data_nature"] == "measured" and q["scale"] == "model":
                issues["quant measured but scale=model"].append(q["quant_id"])
            if q["data_nature"] in ("model_output", "model_assumption") and q["scale"] in ("industrial", "commercial_farm"):
                issues["model figure labelled industrial scale (check)"].append(q["quant_id"])
            ids = [s for s in re.split(r"[;, ]+", q["source_id"]) if s]
            if any(s not in src for s in ids):
                issues["quant citing unknown source"].append(q["quant_id"])
            levels = [src[s]["access_level"] for s in ids if s in src]
            if levels and all(l in ("secondary_report",) for l in levels) and q["data_nature"] == "measured":
                issues["measured value known only second-hand"].append(q["quant_id"])
    out = [f"# Audit de cohérence — {date.today().isoformat()}", "",
           f"Sources : {len(src)}. Règles appliquées par `tools/audit.py consistency`.", ""]
    for k, v in sorted(issues.items(), key=lambda kv: -len(kv[1])):
        out.append(f"## {k} ({len(v)})\n\n" + ", ".join(v[:200]) + "\n")
    if not issues:
        out.append("Aucun problème détecté.")
    (ROOT / "coordination" / "audit_consistency.md").write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out[:3]))
    for k, v in sorted(issues.items(), key=lambda kv: -len(kv[1])):
        print(f"{len(v):4d}  {k}")


def crossref(doi):
    for i in range(4):
        try:
            r = S.get("https://api.crossref.org/works/" + requests.utils.quote(doi, safe="/:;()<>"), timeout=30)
            if r.status_code == 404:
                return None
            if r.status_code == 429:
                time.sleep(3 * (i + 1))
                continue
            r.raise_for_status()
            m = r.json()["message"]
            yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
            return {"title": (m.get("title") or [""])[0], "year": yr,
                    "authors": "; ".join(a.get("family", "") for a in m.get("author", []))}
        except Exception:
            time.sleep(2 * (i + 1))
    return "error"


def datacite(doi):
    try:
        r = S.get("https://api.datacite.org/dois/" + doi, timeout=30)
        if r.status_code != 200:
            return None
        a = r.json()["data"]["attributes"]
        return {"title": (a.get("titles") or [{}])[0].get("title", ""), "year": a.get("publicationYear"),
                "authors": "; ".join(c.get("familyName", c.get("name", "")) for c in a.get("creators", []))}
    except Exception:
        return None


def handle_exists(doi):
    # DOIs registered with non-Crossref agencies (e.g. ISTIC China, KISTI Korea, JaLC) resolve via the Handle API
    try:
        r = S.get("https://doi.org/api/handles/" + doi, timeout=30)
        return r.status_code == 200 and r.json().get("responseCode") == 1
    except Exception:
        return False


def pubmed_titles(pmids):
    out = {}
    for i in range(0, len(pmids), 150):
        chunk = pmids[i:i + 150]
        r = S.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
                  params={"db": "pubmed", "id": ",".join(chunk), "retmode": "json"}, timeout=60)
        d = r.json().get("result", {})
        for p in chunk:
            if p in d and "title" in d[p]:
                out[p] = {"title": d[p]["title"], "year": (d[p].get("pubdate") or "")[:4]}
        time.sleep(0.5)
    return out


def refs(agent=None):
    agents = [agent] if agent else AG
    src = [r for a in agents for r in rows(a, "sources")]
    lines = [f"# Audit des références — {date.today().isoformat()}", "",
             "Chaque DOI est résolu sur Crossref (puis DataCite) et chaque PMID sur PubMed ; le titre enregistré est comparé au titre officiel.",
             "", "| source_id | problème | titre enregistré | titre officiel | année enr./off. |", "|---|---|---|---|---|"]
    stats = Counter()
    pm = pubmed_titles([r["pmid"].strip() for r in src if r.get("pmid", "").strip().isdigit()])
    for r in src:
        d = re.sub(r"^https?://(dx\.)?doi\.org/", "", (r.get("doi") or "").strip()).removeprefix("doi:").strip()
        if d:
            m = crossref(d)
            if m is None:
                m = datacite(d)
            time.sleep(0.15)
            if m == "error":
                stats["doi_error"] += 1
                continue
            if m is None:
                if handle_exists(d):
                    stats["doi_exists_other_RA_title_unchecked"] += 1
                    continue
                stats["doi_not_found"] += 1
                lines.append(f"| {r['source_id']} | DOI introuvable (Crossref, DataCite, Handle) | {r['title_original'][:70]} | — | {r['year']}/— |")
                continue
            s = sim(r["title_original"], m["title"]) if r["language"] in ("en", "") or norm(m["title"]) else 1
            yr_ok = not r["year"] or not m["year"] or abs(int(re.sub(r'\D', '', r['year'][:4]) or 0) - int(m["year"])) <= 1
            if s < 0.5 and r.get("title_fr", "") and sim(r.get("title_fr", ""), m["title"]) >= 0.5:
                s = 1
            if s < 0.5:
                stats["doi_title_mismatch"] += 1
                lines.append(f"| {r['source_id']} | titre ≠ DOI (sim={s:.2f}) | {r['title_original'][:70]} | {m['title'][:70]} | {r['year']}/{m['year']} |")
            elif not yr_ok:
                stats["doi_year_mismatch"] += 1
                lines.append(f"| {r['source_id']} | année ≠ DOI | {r['title_original'][:70]} | {m['title'][:70]} | {r['year']}/{m['year']} |")
            else:
                stats["doi_ok"] += 1
        p = (r.get("pmid") or "").strip()
        if p.isdigit():
            if p not in pm:
                stats["pmid_not_found"] += 1
                lines.append(f"| {r['source_id']} | PMID introuvable | {r['title_original'][:70]} | — | {r['year']}/— |")
            elif sim(r["title_original"], pm[p]["title"]) < 0.5:
                stats["pmid_title_mismatch"] += 1
                lines.append(f"| {r['source_id']} | titre ≠ PMID | {r['title_original'][:70]} | {pm[p]['title'][:70]} | {r['year']}/{pm[p]['year']} |")
            else:
                stats["pmid_ok"] += 1
    lines += ["", "## Bilan", ""] + [f"- {k} : {v}" for k, v in sorted(stats.items())]
    name = f"audit_refs{'_' + agent if agent else ''}.md"
    (ROOT / "coordination" / name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[-len(stats) - 1:]))


def coverage():
    lang_re = re.compile(r"^\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|")
    out = [f"# Couverture automatique — {date.today().isoformat()}", "",
           "Généré par `tools/audit.py coverage` à partir des journaux de recherche et des tables (complète `coverage_matrix.md`).", "",
           "| Agent | requêtes journalisées | langues des requêtes | bases interrogées | sources | dont texte intégral | langues des sources | affirmations | mesures | recherches 'contraires/négatives' |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for a in AG:
        log = ROOT / "agents" / a / "search_log.md"
        n, langs, bases, neg = 0, Counter(), Counter(), 0
        if log.exists():
            for line in log.read_text(encoding="utf-8").splitlines():
                m = lang_re.match(line)
                if not m or set(m.group(1).strip()) <= set("-: ") or m.group(1).strip().lower() in ("date",):
                    continue
                n += 1
                bases[m.group(2).strip().lower()[:20]] += 1
                langs[m.group(3).strip().lower()[:8]] += 1
                if re.search(r"contra|négat|negat|fail|échec|limit|critique|null|no effect|sans effet", line, re.I):
                    neg += 1
        src = rows(a, "sources")
        ft = sum(r["access_level"] in ("full_text_read", "partial_text_read") for r in src)
        sl = Counter(r["language"] for r in src)
        out.append(f"| {a} | {n} | {', '.join(f'{k}:{v}' for k, v in langs.most_common(12))} | {', '.join(k for k, _ in bases.most_common(8))} | {len(src)} | {ft} | {', '.join(f'{k}:{v}' for k, v in sl.most_common())} | {len(rows(a, 'evidence'))} | {len(rows(a, 'quant'))} | {neg} |")
    (ROOT / "coordination" / "coverage_auto.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else ""
    if c == "consistency":
        consistency()
    elif c == "refs":
        refs(sys.argv[2] if len(sys.argv) > 2 else None)
    elif c == "coverage":
        coverage()
    else:
        sys.exit(__doc__)
