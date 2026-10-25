#!/usr/bin/env python3
"""Knowledge-base helper for the Chicken Muscle Research Lab.

Each agent writes ONLY to research/agents/<AGENT>/{sources,evidence,quant}.csv
through this tool, so IDs, columns and controlled vocabularies stay consistent.
The coordinator then runs `merge` to build the deduplicated root tables.

Usage
  python3 research/tools/kb.py add sources  <AGENT> <file.json>   # JSON list of records
  python3 research/tools/kb.py add evidence <AGENT> <file.json>
  python3 research/tools/kb.py add quant    <AGENT> <file.json>
  python3 research/tools/kb.py find <text>                         # search all source titles/DOIs
  python3 research/tools/kb.py check                               # validate every agent table
  python3 research/tools/kb.py merge                               # build root tables + dedup report
  python3 research/tools/kb.py stats

AGENT is one of H N C A E P X (X = coordinator).
"""
import csv
import json
import os
import re
import signal
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

ROOT = Path(__file__).resolve().parents[1]
AGENTS = {
    "H": "history",
    "N": "poultry_nutrition",
    "C": "cultivated_chicken",
    "A": "alternative_proteins",
    "E": "industrialization",
    "P": "patents_and_innovation",
    "X": "coordinator",
}

SOURCE_COLS = [
    "source_id", "title_original", "title_fr", "authors", "year", "language",
    "source_type", "doi", "pmid", "url", "domain", "methodology",
    "access_level", "quality", "limitations", "verification_status",
    "contribution", "found_via", "duplicate_of", "date_accessed", "agent", "notes",
]
EVIDENCE_COLS = [
    "claim_id", "claim_fr", "source_id", "locator", "quote_original",
    "result", "conditions", "species_system", "evidence_type", "confidence",
    "confidence_rationale", "limitations", "contradicts", "pathway", "domain",
    "agent", "notes",
]
QUANT_COLS = [
    "quant_id", "parameter", "value", "unit_original", "value_normalized",
    "unit_normalized", "quantity_basis", "measurement_method", "species_system",
    "scale", "data_nature", "source_id", "locator", "uncertainty",
    "conditions", "pathway", "agent", "notes",
]

TABLES = {
    "sources": ("SRC", SOURCE_COLS, "source_id"),
    "evidence": ("EV", EVIDENCE_COLS, "claim_id"),
    "quant": ("Q", QUANT_COLS, "quant_id"),
}

ENUMS = {
    "source_type": {
        "peer_reviewed_article", "review", "systematic_review", "meta_analysis",
        "thesis", "preprint", "conference", "book", "historical_text",
        "technical_report", "institutional_report", "statistical_database",
        "regulatory_text", "patent", "company_communication", "press",
        "website", "video", "other",
    },
    "access_level": {
        "full_text_read",      # the agent actually read the full text (or the relevant sections)
        "partial_text_read",   # some sections/pages read (state which in notes)
        "abstract_only",       # only the abstract was available/read
        "metadata_only",       # title/authors/year only
        "secondary_report",    # known only through another source (press, review)
        "paywalled_not_read",
    },
    "verification_status": {
        "verified_primary",    # claim checked in the primary document
        "verified_metadata",   # bibliographic data checked (Crossref/PubMed/publisher)
        "secondary_only",      # not checked in primary source
        "unverified",
        "suspect",             # inconsistencies found
    },
    "quality": {"high", "moderate", "low", "very_low", "not_assessed"},
    "evidence_type": {
        "historical_documented", "historical_reconstruction", "experimental",
        "reproduced_experimental", "field_trial", "systematic_review",
        "meta_analysis", "narrative_review", "preliminary", "simulation_model",
        "techno_economic_model", "life_cycle_assessment", "cross_species_extrapolation",
        "theoretical", "commercial_claim", "regulatory_text", "statistical_data",
        "expert_opinion", "patent_claim",
    },
    "confidence": {"high", "moderate", "low", "very_low"},
    "pathway": {"A", "B", "C", "A+B", "A+C", "B+C", "ALL", "cross", "history"},
    "data_nature": {
        "measured", "measured_reported_by_review", "company_claim",
        "published_estimate", "model_assumption", "model_output",
        "statistical", "historical_record", "regulatory_limit",
    },
    "scale": {
        "lab", "bench", "pilot", "demonstration", "industrial", "commercial_farm",
        "field_trial", "national", "global", "model", "historical", "not_applicable",
    },
    "quantity_basis": {
        "wet_cell_biomass", "dry_cell_biomass", "dry_matter", "protein",
        "muscle_tissue", "edible_meat", "carcass", "breast_meat", "live_weight",
        "feed", "medium_volume", "reactor_volume", "facility", "product",
        "currency", "time", "energy", "water", "land", "emissions", "cell_count",
        "concentration", "ratio", "other",
    },
}

REQUIRED = {
    "sources": ["title_original", "year", "language", "source_type", "domain",
                "access_level", "verification_status"],
    "evidence": ["claim_fr", "source_id", "evidence_type", "confidence",
                 "confidence_rationale", "pathway"],
    "quant": ["parameter", "value", "unit_original", "quantity_basis",
              "species_system", "scale", "data_nature", "source_id"],
}


def path_for(table, agent):
    return ROOT / "agents" / agent / f"{table}.csv"


def read_rows(p):
    if not p.exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(p, cols, rows):
    # atomic replace so that agents reading each other's tables never see a half-written file
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(f".tmp{os.getpid()}")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})
    os.replace(tmp, p)


def all_source_ids():
    ids = set()
    for a in AGENTS:
        for r in read_rows(path_for("sources", a)):
            ids.add(r["source_id"])
    return ids


def normalize_title(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9 ]", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d.removeprefix("doi:").strip()


def validate(table, rec, known_sources=None):
    errs = []
    for k in REQUIRED[table]:
        if not str(rec.get(k, "")).strip():
            errs.append(f"missing required field '{k}'")
    for k, allowed in ENUMS.items():
        if k in rec and str(rec[k]).strip() and k in TABLES[table][1]:
            if str(rec[k]).strip() not in allowed:
                errs.append(f"'{k}'='{rec[k]}' not in {sorted(allowed)}")
    unknown = set(rec) - set(TABLES[table][1])
    if unknown:
        errs.append(f"unknown columns {sorted(unknown)}")
    if table in ("evidence", "quant") and known_sources is not None:
        for sid in re.split(r"[;, ]+", str(rec.get("source_id", "")).strip()):
            if sid and sid not in known_sources:
                errs.append(f"source_id '{sid}' not registered")
    if table == "quant":
        v = str(rec.get("value", "")).strip()
        if v and not re.match(r"^[<>~≈≤≥]?\s*-?[\d.,]+(e-?\d+)?(\s*[-–]\s*-?[\d.,]+(e-?\d+)?)?$", v, re.I):
            errs.append(f"value '{v}' is not numeric/range (put qualifiers in notes)")
    return errs


def cmd_add(table, agent, jfile):
    if agent not in AGENTS:
        sys.exit(f"unknown agent {agent}")
    prefix, cols, idcol = TABLES[table]
    recs = json.loads(Path(jfile).read_text(encoding="utf-8"))
    if isinstance(recs, dict):
        recs = [recs]
    p = path_for(table, agent)
    rows = read_rows(p)
    n = 0
    for r in rows:
        m = re.match(rf"{prefix}-{agent}-(\d+)$", r[idcol])
        if m:
            n = max(n, int(m.group(1)))
    known = all_source_ids() if table != "sources" else None
    # allow evidence/quant to reference sources added in the same call? no: sources first.
    existing_dois = {}
    existing_titles = {}
    if table == "sources":
        for a in AGENTS:
            for r in read_rows(path_for("sources", a)):
                if norm_doi(r.get("doi")):
                    existing_dois[norm_doi(r["doi"])] = r["source_id"]
                existing_titles[normalize_title(r["title_original"])] = r["source_id"]
    out, bad = [], 0
    for rec in recs:
        rec = {k: ("" if v is None else str(v)) for k, v in rec.items()}
        errs = validate(table, rec, known)
        if errs:
            bad += 1
            print(f"REJECTED: {rec.get('title_original') or rec.get('claim_fr') or rec.get('parameter','')[:80]}\n   -> " + "; ".join(errs))
            continue
        if table == "sources":
            d = norm_doi(rec.get("doi"))
            dup = existing_dois.get(d) if d else None
            dup = dup or existing_titles.get(normalize_title(rec["title_original"]))
            if dup:
                print(f"ALREADY REGISTERED as {dup}: {rec['title_original'][:90]} (reuse that ID; not added)")
                continue
            rec.setdefault("date_accessed", date.today().isoformat())
            if not rec.get("date_accessed"):
                rec["date_accessed"] = date.today().isoformat()
        n += 1
        rec[idcol] = f"{prefix}-{agent}-{n:04d}"
        rec["agent"] = agent
        rows.append(rec)
        out.append(rec)
        if table == "sources":
            if norm_doi(rec.get("doi")):
                existing_dois[norm_doi(rec["doi"])] = rec[idcol]
            existing_titles[normalize_title(rec["title_original"])] = rec[idcol]
        label = rec.get("title_original") or rec.get("claim_fr") or rec.get("parameter")
        print(f"ADDED {rec[idcol]}: {label[:100]}")
    write_rows(p, cols, rows)
    print(f"{len(out)} added, {bad} rejected -> {p.relative_to(ROOT.parent)}")


def cmd_find(text):
    t = normalize_title(text)
    d = norm_doi(text)
    for a in AGENTS:
        for r in read_rows(path_for("sources", a)):
            if (t and (t in normalize_title(r["title_original"]) or t in normalize_title(r.get("authors", "")))) or (d and d == norm_doi(r.get("doi"))) or text.lower() in (r.get("url") or "").lower():
                print(r["source_id"], "|", r["year"], "|", r["title_original"][:110], "|", r.get("doi"), "|", r["access_level"])


def cmd_check():
    known = all_source_ids()
    total = 0
    for a in AGENTS:
        for table in TABLES:
            rows = read_rows(path_for(table, a))
            for r in rows:
                rec = {k: v for k, v in r.items() if k not in (TABLES[table][2], "agent")}
                rec = {k: v for k, v in rec.items() if v != ""}
                errs = validate(table, rec, known if table != "sources" else None)
                if errs:
                    total += 1
                    print(f"{r[TABLES[table][2]]}: " + "; ".join(errs))
    print(f"check done: {total} rows with problems")


def cmd_merge():
    # Sources: dedup by DOI, PMID, normalized title (+year)
    sources = []
    for a in AGENTS:
        sources += read_rows(path_for("sources", a))
    canon_by_key = {}
    dup_map = {}
    for r in sources:
        keys = []
        if norm_doi(r.get("doi")):
            keys.append("doi:" + norm_doi(r["doi"]))
        if (r.get("pmid") or "").strip():
            keys.append("pmid:" + r["pmid"].strip())
        keys.append("t:" + normalize_title(r["title_original"])[:120] + ":" + (r.get("year") or ""))
        hit = next((canon_by_key[k] for k in keys if k in canon_by_key), None)
        if hit and hit != r["source_id"]:
            dup_map[r["source_id"]] = hit
        else:
            hit = r["source_id"]
        for k in keys:
            canon_by_key.setdefault(k, hit)
    rank = {"full_text_read": 0, "partial_text_read": 1, "abstract_only": 2,
            "metadata_only": 3, "secondary_report": 4, "paywalled_not_read": 5}
    merged = []
    by_id = {r["source_id"]: r for r in sources}
    for r in sources:
        r = dict(r)
        if r["source_id"] in dup_map:
            r["duplicate_of"] = dup_map[r["source_id"]]
            canon = by_id[dup_map[r["source_id"]]]
            # keep the best access level on the canonical record
            if rank.get(r["access_level"], 9) < rank.get(canon["access_level"], 9):
                canon["access_level"] = r["access_level"]
        merged.append(r)
    write_rows(ROOT / "source_registry.csv", SOURCE_COLS, merged)

    ev = []
    for a in AGENTS:
        ev += read_rows(path_for("evidence", a))
    for r in ev:
        r["source_id"] = ";".join(dup_map.get(s, s) for s in re.split(r"[;, ]+", r["source_id"]) if s)
    write_rows(ROOT / "evidence_database.csv", EVIDENCE_COLS, ev)

    q = []
    for a in AGENTS:
        q += read_rows(path_for("quant", a))
    for r in q:
        r["source_id"] = ";".join(dup_map.get(s, s) for s in re.split(r"[;, ]+", r["source_id"]) if s)
    write_rows(ROOT / "quantitative_data.csv", QUANT_COLS, q)

    rep = ["# Rapport de déduplication", "", f"Généré le {date.today().isoformat()} par `kb.py merge`.", "",
           f"- Sources enregistrées (toutes lignes) : {len(sources)}",
           f"- Doublons détectés : {len(dup_map)}",
           f"- Sources uniques : {len(sources) - len(dup_map)}",
           f"- Affirmations : {len(ev)}", f"- Mesures quantitatives : {len(q)}", "",
           "| doublon | canonique | titre |", "|---|---|---|"]
    for d, c in sorted(dup_map.items()):
        rep.append(f"| {d} | {c} | {by_id[d]['title_original'][:90].replace('|', '/')} |")
    (ROOT / "coordination" / "dedup_report.md").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep[:9]))


def cmd_stats():
    for table in TABLES:
        c = Counter()
        for a in AGENTS:
            c[a] = len(read_rows(path_for(table, a)))
        print(table, dict(c), "total", sum(c.values()))
    src = []
    for a in AGENTS:
        src += read_rows(path_for("sources", a))
    for col in ("language", "access_level", "source_type", "verification_status"):
        print(col, dict(Counter(r[col] for r in src).most_common()))
    ev = []
    for a in AGENTS:
        ev += read_rows(path_for("evidence", a))
    print("evidence confidence", dict(Counter(r["confidence"] for r in ev)))
    print("evidence type", dict(Counter(r["evidence_type"] for r in ev).most_common()))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    c = sys.argv[1]
    if c == "add" and len(sys.argv) == 5:
        cmd_add(sys.argv[2], sys.argv[3], sys.argv[4])
    elif c == "find":
        cmd_find(" ".join(sys.argv[2:]))
    elif c == "check":
        cmd_check()
    elif c == "merge":
        cmd_merge()
    elif c == "stats":
        cmd_stats()
    else:
        sys.exit(__doc__)
