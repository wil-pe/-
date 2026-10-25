#!/usr/bin/env python3
"""Comparaison homogène des trois voies par kg de protéine comestible (agent K, mission X2).

Principes
---------
* Aucune valeur numérique n'est écrite en dur dans ce script, à l'exception de constantes
  physiques ou de conversion d'unités (1 lb = 0,4536 kg, 1 kWh = 3,6 MJ, 1 t = 1 000 kg,
  1 g/100 g = 1 %). Toutes les données sont lues dans les lignes ``Q-…`` de la base
  (``research/agents/*/quant.csv``, complétées par ``research/quantitative_data.csv``).
  Les hypothèses de l'agent K sont elles-mêmes des lignes ``Q-K-…`` marquées
  ``model_assumption`` (source SRC-K-0019).
* Base commune : **kg de protéine comestible** = kg de viande désossée crue (voie A), de
  biomasse cellulaire humide ou de produit (voie B), d'ingrédient ou de produit (voie C),
  multiplié par sa teneur en protéines (N × facteur, tables de composition).
* Chaque chiffre porte la nature de ses intrants (statistique, estimation publiée, sortie
  de modèle, prix de marché, déclaration d'entreprise, hypothèse) et ses références.
* Trois scénarios quand les données le permettent : ``prudent`` (défavorable),
  ``intermediaire`` (valeur centrale), ``optimiste`` (favorable). Les plages reflètent
  l'étendue des sources lues, pas une distribution de probabilité.
* Aucune correction d'inflation ; conversions de change BCE de l'année de la donnée.

Exécution : ``python3 research/agents/K/models/comparison.py``
Écrit ``results.md`` et ``results.json`` dans le même dossier.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parents[2]

# Constantes de conversion d'unités (pas des données)
LB_KG = 0.4536
KWH_MJ = 3.6
SCEN = ("prudent", "intermediaire", "optimiste")


# ---------------------------------------------------------------------------
# Lecture de la base
# ---------------------------------------------------------------------------
def load_quant() -> dict:
    rows = {}
    root = RESEARCH / "quantitative_data.csv"
    if root.exists():
        with open(root, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows[r["quant_id"]] = r
    for p in sorted((RESEARCH / "agents").glob("*/quant.csv")):  # tables d'agents = référence
        with open(p, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows[r["quant_id"]] = r
    return rows


Q = load_quant()
USED: dict[str, dict] = {}


def _num(s: str) -> float:
    return float(s.replace(",", ".").replace("−", "-"))


def rng(qid: str, unit_hint: str | None = None, field: str = "value") -> tuple[float, float]:
    """(bas, haut) d'une ligne Q ; vérifie l'unité si `unit_hint` est donné."""
    r = Q[qid]
    if unit_hint and unit_hint.lower() not in (r["unit_original"] + " " + r["unit_normalized"]).lower():
        raise ValueError(f"{qid}: unité inattendue {r['unit_original']!r} (attendu ~{unit_hint!r})")
    s = r[field].strip()
    USED[qid] = {k: r[k] for k in ("parameter", "value", "unit_original", "data_nature", "source_id", "scale")}
    s = s.lstrip("<>≈~ ")
    m = re.fullmatch(r"([0-9.,Ee+]+)\s*-\s*([0-9.,Ee+]+)", s)
    if m:
        a, b = _num(m.group(1)), _num(m.group(2))
        return (min(a, b), max(a, b))
    v = _num(s)
    return (v, v)


def lo(qid, u=None, field="value"):
    return rng(qid, u, field)[0]


def hi(qid, u=None, field="value"):
    return rng(qid, u, field)[1]


def mid(qid, u=None, field="value"):
    a, b = rng(qid, u, field)
    return (a + b) / 2


def nature(*qids) -> str:
    return " + ".join(sorted({Q[q]["data_nature"] for q in qids}))


# ---------------------------------------------------------------------------
# Facteurs de conversion (voie A)
# ---------------------------------------------------------------------------
PCT = 0.01

# Teneur en protéines de la viande désossée crue (kg protéine / kg viande)
PROTEIN_MEAT = {
    "prudent": lo("Q-K-0049", "g/100") * PCT,          # TACO frango inteiro sem pele cru 20,6
    "intermediaire": lo("Q-K-0046", "g/100") * PCT,    # USDA viande seule crue 21,4
    "optimiste": hi("Q-K-0123", "g/100") * PCT,        # USDA viande blanche 23,2 (hypothèse Q-K-0123)
}
PROTEIN_REFS = "Q-K-0049 ; Q-K-0046 ; Q-K-0123"
# Rapport protéine « acides aminés » / protéine « N × facteur » (filet japonais)
AA_RATIO = lo("Q-K-0053", "g/100") / lo("Q-K-0052", "g/100")

# Rendement en viande désossée (kg viande / kg poids vif)
YIELD = {
    "standard": {
        "optimiste": lo("Q-N-0035", "%") * PCT,                                  # 47 % (revue, Laisse 2018)
        "intermediaire": lo("Q-N-0014", "%") * PCT,                              # 43,1 % (Ross 308, déclaration)
        "prudent": (lo("Q-K-0064", "%") + lo("Q-K-0065", "%")) * PCT,             # 41,4 % (WUR 1397, objectifs sélectionneurs)
        "refs": "Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065",
    },
    "certifie": {
        "optimiste": lo("Q-K-0066", "%") * PCT,                                  # BLS 35,3 % (objectifs)
        "intermediaire": (hi("Q-K-0077", "%") + lo("Q-K-0122", "%")) * PCT,       # JA757 16,4 + cuisse 16,1
        "prudent": (lo("Q-K-0077", "%") + lo("Q-K-0122", "%")) * PCT,             # 15,8 + 16,1
        "refs": "Q-K-0066 ; Q-K-0077 + Q-K-0122 (hypothèse)",
    },
    "label_rouge_bio": {
        "optimiste": (hi("Q-K-0076", "%") + lo("Q-K-0122", "%")) * PCT,           # S757N 14,5 + 16,1
        "intermediaire": (hi("Q-K-0076", "%") + lo("Q-K-0122", "%")) * PCT,
        "prudent": (lo("Q-K-0076", "%") + lo("Q-K-0122", "%")) * PCT,             # 14,1 + 16,1
        "refs": "Q-K-0076 + Q-K-0122 (hypothèse)",
    },
}

# Allocation des impacts à la viande désossée (les coûts restent imputés à 100 %)
ALLOC = {"prudent": hi("Q-K-0124", "fraction"), "intermediaire": lo("Q-K-0124", "fraction"),
         "optimiste": lo("Q-K-0124", "fraction")}
assert abs(ALLOC["intermediaire"] - (1 - lo("Q-K-0006", "%") * PCT)) < 1e-9  # 88 % = 1 − 12 % (FAO/Kool)

# Change BCE (USD par EUR) de l'année de la donnée
USD_PER_EUR = {2017: lo("Q-E-0061", "US dollar"), 2021: lo("Q-K-0107", "US dollar"),
               2022: lo("Q-E-0063", "US dollar"), 2023: lo("Q-K-0108", "US dollar"),
               2025: lo("Q-K-0109", "US dollar")}
BRL_PER_EUR_2025 = lo("Q-E-0064", "Brazilian real")


def edible_protein_per_kg_lw(system: str, s: str) -> float:
    return YIELD[system][s] * PROTEIN_MEAT[s]


def per_protein_a(x_per_kg_lw: float, system: str, s: str, alloc: bool) -> float:
    a = ALLOC[s] if alloc else 1.0
    return x_per_kg_lw * a / edible_protein_per_kg_lw(system, s)


def pick(lohi: tuple, s: str, favourable_low: bool = True) -> float:
    """Choisit bas/milieu/haut d'une plage selon le scénario."""
    a, b = lohi
    if s == "intermediaire":
        return (a + b) / 2
    if (s == "optimiste") == favourable_low:
        return a
    return b


# ---------------------------------------------------------------------------
# Voie A — coûts par kg de protéine comestible
# ---------------------------------------------------------------------------
def a_costs():
    """Coût de production (sortie ferme + abattage quand il est sourcé), imputé à 100 % à la viande désossée."""
    cases = [
        # (étiquette, système, année, monnaie, coût ferme (lo,hi) €/kg PV, abattage (lo,hi) €/kg carcasse, rendement carcasse (lo,hi), refs, nature)
        ("UE moyenne 2017, standard", "standard", 2017, "EUR",
         (lo("Q-E-0022", "eurocent") * PCT,) * 2, tuple(x * PCT for x in rng("Q-K-0110", "eurocent")),
         (lo("Q-E-0049", "%") * PCT,) * 2, "Q-E-0022 ; Q-K-0110 ; Q-E-0049", nature("Q-E-0022", "Q-K-0110")),
        ("UE six pays 2021, standard", "standard", 2021, "EUR",
         tuple(x * PCT for x in rng("Q-K-0059", "cents")), tuple(x * PCT for x in rng("Q-K-0060", "cents")),
         (lo("Q-K-0061", "%") * PCT,) * 2, "Q-K-0059 ; Q-K-0060 ; Q-K-0061", nature("Q-K-0059", "Q-K-0060")),
        ("France 2022, standard (ITAVI)", "standard", 2022, "EUR",
         rng("Q-E-0029", "€/kg"), (lo("Q-K-0112", "cents") * PCT,) * 2,
         (lo("Q-K-0061", "%") * PCT,) * 2, "Q-E-0029 ; Q-K-0112 (abattage 2021) ; Q-K-0061", nature("Q-E-0029", "Q-K-0112")),
        ("États-Unis 2023, standard (grande échelle, hors abattage)", "standard", 2023, "USD",
         (lo("Q-K-0080", "USD/lb") / LB_KG,) * 2, (0.0, 0.0), (1.0, 1.0), "Q-K-0080", nature("Q-K-0080")),
        ("Brésil (Paraná) 2025, standard (hors abattage)", "standard", 2025, "BRL",
         (lo("Q-E-0032", "R$/kg"),) * 2, (0.0, 0.0), (1.0, 1.0), "Q-E-0032", nature("Q-E-0032")),
        ("Pays-Bas 2021, certifié ECC", "certifie", 2021, "EUR",
         (lo("Q-K-0056", "cents") * PCT,) * 2, tuple(x * PCT for x in rng("Q-K-0111", "cents")),
         (lo("Q-K-0114", "%") * PCT,) * 2, "Q-K-0056 ; Q-K-0111 ; Q-K-0114", nature("Q-K-0056", "Q-K-0111")),
        ("France 2021, certifié ECC", "certifie", 2021, "EUR",
         (lo("Q-K-0058", "cents") * PCT,) * 2, (lo("Q-K-0113", "cents") * PCT,) * 2,
         (lo("Q-K-0114", "%") * PCT,) * 2, "Q-K-0058 ; Q-K-0113 ; Q-K-0114", nature("Q-K-0058", "Q-K-0113")),
        ("États-Unis 2023, pâturage (hors abattage)", "label_rouge_bio", 2023, "USD",
         (lo("Q-K-0082", "USD/lb") / LB_KG,) * 2, (0.0, 0.0), (1.0, 1.0), "Q-K-0082", nature("Q-K-0082")),
        ("France 2022, Label Rouge (ITAVI)", "label_rouge_bio", 2022, "EUR",
         rng("Q-E-0030", "€/kg"), (lo("Q-K-0128", "cents") * PCT,) * 2,
         tuple(x * PCT for x in rng("Q-K-0121", "%")), "Q-E-0030 ; Q-K-0128 (hyp.) ; Q-K-0121", nature("Q-E-0030", "Q-K-0128")),
        ("France 2022, biologique (ITAVI)", "label_rouge_bio", 2022, "EUR",
         rng("Q-E-0031", "€/kg"), (lo("Q-K-0128", "cents") * PCT,) * 2,
         tuple(x * PCT for x in rng("Q-K-0121", "%")), "Q-E-0031 ; Q-K-0128 (hyp.) ; Q-K-0121", nature("Q-E-0031", "Q-K-0128")),
    ]
    out = []
    for label, system, year, cur, farm, slaughter, cy, refs, nat in cases:
        res = {"label": label, "system": system, "year": year, "currency": cur, "refs": refs,
               "input_nature": nat, "yield_refs": YIELD[system]["refs"], "protein_refs": PROTEIN_REFS}
        for s in SCEN:
            f = pick(farm, s)
            sl = pick(slaughter, s)
            c = pick(cy, s, favourable_low=False)  # rendement carcasse élevé = favorable
            per_lw = f + sl * c                      # coût d'abattage ramené au kg de poids vif
            per_prot = per_protein_a(per_lw, system, s, alloc=False)
            if cur == "EUR":
                usd = per_prot * USD_PER_EUR[year]
            elif cur == "BRL":
                usd = per_prot / BRL_PER_EUR_2025 * USD_PER_EUR[2025]
            else:
                usd = per_prot
            res[s] = {"per_kg_lw": round(per_lw, 3), "per_kg_protein_orig": round(per_prot, 2),
                      "per_kg_protein_usd": round(usd, 2)}
        out.append(res)
    return out


# ---------------------------------------------------------------------------
# Voie A — environnement par kg de protéine comestible
# ---------------------------------------------------------------------------
def a_env():
    slaughter_ghg = lo("Q-K-0115", "kg CO2")
    slaughter_el_mj = lo("Q-K-0074", "kWh/ton") / 1000 * KWH_MJ   # MJ électricité / kg PV
    rows = []

    def add(indic, label, system, per_lw_lohi, unit, refs, alloc=True, note="", boundary="porte"):
        r = {"indicator": indic, "label": label, "system": system, "unit": unit, "refs": refs, "boundary": boundary,
             "input_nature": nature(*[x.strip().split(" ")[0] for x in refs.split(";") if x.strip().startswith("Q-")]),
             "note": note}
        for s in SCEN:
            r[s] = round(per_protein_a(pick(per_lw_lohi, s), system, s, alloc), 1)
        rows.append(r)

    # GES
    add("GES", "France standard, AGRIBALYSE sortie ferme + abattoir", "standard",
        (lo("Q-K-0027", "kg CO2") + slaughter_ghg,) * 2, "kg CO2-eq/kg protéine", "Q-K-0027 ; Q-K-0115")
    add("GES", "Pays-Bas standard avec LUC (WUR 1397)", "standard", rng("Q-K-0069", "kg CO2"), "kg CO2-eq/kg protéine", "Q-K-0069")
    add("GES", "Pays-Bas standard sans LUC (WUR 1397)", "standard", rng("Q-K-0070", "kg CO2"), "kg CO2-eq/kg protéine", "Q-K-0070")
    add("GES", "Pays-Bas Beter Leven 1 étoile avec LUC (WUR 1397)", "certifie", (hi("Q-K-0071", "kg CO2"),) * 2,
        "kg CO2-eq/kg protéine", "Q-K-0071")
    add("GES", "Pays-Bas Beter Leven 1 étoile sans LUC (WUR 1397)", "certifie", (lo("Q-K-0071", "kg CO2"),) * 2,
        "kg CO2-eq/kg protéine", "Q-K-0071")
    add("GES", "France Label Rouge, AGRIBALYSE + abattoir", "label_rouge_bio",
        (lo("Q-K-0031", "kg CO2") + slaughter_ghg,) * 2, "kg CO2-eq/kg protéine", "Q-K-0031 ; Q-K-0115")
    add("GES", "France biologique, AGRIBALYSE (moyenne → systèmes 1-2) + abattoir", "label_rouge_bio",
        (lo("Q-K-0035", "kg CO2") + slaughter_ghg, hi("Q-K-0039", "kg CO2") + slaughter_ghg),
        "kg CO2-eq/kg protéine", "Q-K-0035 ; Q-K-0039 ; Q-K-0115")
    # FAO 2013 : par kg de carcasse → viande sans gras ni os 59 % de la carcasse (Q-K-0005)
    fao = lo("Q-K-0001", "kg CO2")
    meat_cw = lo("Q-K-0005", "%") * PCT
    r = {"indicator": "GES", "label": "Monde, FAO GLEAM 2013 (berceau-détail)", "boundary": "détail", "system": "standard",
         "unit": "kg CO2-eq/kg protéine", "refs": "Q-K-0001 ; Q-K-0005 ; protéine " + PROTEIN_REFS,
         "input_nature": nature("Q-K-0001", "Q-K-0005"), "note": "conversion carcasse → viande de la FAO elle-même"}
    for s in SCEN:
        r[s] = round(fao * ALLOC[s] / (meat_cw * PROTEIN_MEAT[s]), 1)
    rows.append(r)
    rows.append({"indicator": "GES", "label": "Royaume-Uni, FAO GLEAM (déjà par kg de protéine)", "boundary": "détail", "system": "standard",
                 "unit": "kg CO2-eq/kg protéine", "refs": "Q-K-0004", "input_nature": nature("Q-K-0004"),
                 "prudent": lo("Q-K-0004", "protein"), "intermediaire": lo("Q-K-0004", "protein"),
                 "optimiste": lo("Q-K-0004", "protein"), "note": "PAS 2050 : 32,9 (notes)"})
    pn = lo("Q-K-0102", "per 100 g") * 10
    rows.append({"indicator": "GES", "label": "Monde, Poore & Nemecek (moyenne, par kg de protéine)", "boundary": "détail", "system": "standard",
                 "unit": "kg CO2-eq/kg protéine", "refs": "Q-K-0102", "input_nature": nature("Q-K-0102"),
                 "prudent": pn, "intermediaire": pn, "optimiste": pn, "note": "base protéine des auteurs (volaille, produit de détail)"})

    # Produits de détail (toutes étapes) : base kg de viande, protéine des tables
    def prod_row(ind, label, qid, unit_hint, prot_qid, unit, factor=1.0, note=""):
        v = lo(qid, unit_hint) * factor
        p = lo(prot_qid, "g/100") * PCT
        rows.append({"indicator": ind, "label": label, "system": "standard", "unit": unit, "refs": f"{qid} ; {prot_qid}", "boundary": "détail",
                     "input_nature": nature(qid, prot_qid), "prudent": round(v / p, 1), "intermediaire": round(v / p, 1),
                     "optimiste": round(v / p, 1), "note": note})
    prod_row("GES", "France, viande de poulet crue, AGRIBALYSE toutes étapes (produit)", "Q-K-0045", "kg CO2", "Q-K-0046",
             "kg CO2-eq/kg protéine", note="même base que les analogues végétaux AGRIBALYSE (voie C)")
    prod_row("GES", "France, filet de poulet cru, AGRIBALYSE toutes étapes (produit)", "Q-K-0040", "kg CO2", "Q-K-0047", "kg CO2-eq/kg protéine")
    prod_row("Énergie", "France, filet de poulet cru, AGRIBALYSE toutes étapes (MJ non renouvelables)", "Q-K-0041", "MJ", "Q-K-0047",
             "MJ/kg protéine", note="transformation = 47 % ; comparable à l'escalope végétale (voie C)")
    prod_row("GES", "Allemagne, Hähnchen (moyenne), ifeu (produit)", "Q-K-0091", "kg CO2", "Q-K-0046", "kg CO2-eq/kg protéine",
             note="base produit non précisée (os éventuels) : protéine 21,4 % supposée")
    prod_row("Énergie", "Allemagne, Hähnchen (moyenne), ifeu (énergie primaire)", "Q-K-0093", "kWh", "Q-K-0046", "MJ/kg protéine",
             factor=KWH_MJ, note="base produit non précisée")
    prod_row("Surface", "Allemagne, Hähnchen (moyenne), ifeu", "Q-K-0092", "m2", "Q-K-0046", "m2·an/kg protéine", note="base produit non précisée")
    prod_row("GES", "Pays-Bas, filet de poulet au supermarché, RIVM 2024 (agent S)", "Q-S-0085", "kg CO2", "Q-K-0047", "kg CO2-eq/kg protéine",
             note="allocation économique")
    prod_row("Surface", "Pays-Bas, filet de poulet, RIVM 2024 (agent S)", "Q-S-0089", "m2a", "Q-K-0047", "m2·an/kg protéine")

    # Énergie : MJ non renouvelables sortie ferme (EF) + électricité d'abattoir (énergie finale)
    for sysname, qid, label in [("standard", "Q-K-0028", "France standard"), ("label_rouge_bio", "Q-K-0032", "France Label Rouge"),
                                ("label_rouge_bio", "Q-K-0036", "France biologique")]:
        add("Énergie", label + ", AGRIBALYSE (MJ non renouvelables) + électricité d'abattoir", sysname,
            (lo(qid, "MJ") + slaughter_el_mj,) * 2, "MJ/kg protéine", qid + " ; Q-K-0074")

    # Eau bleue (volume) : classes de Mekonnen & Hoekstra, protéine 127 g/kg de leur base produit
    prot_mh = lo("Q-K-0010", "g/kg") / 1000
    for sysname, qid, label in [("standard", "Q-K-0012", "standard ↔ classe industrielle"),
                                ("certifie", "Q-K-0120", "certifié et Label Rouge ↔ classe mixte"),
                                ("label_rouge_bio", "Q-K-0013", "biologique ↔ classe pâturage")]:
        v = lo(qid, "m3/ton") / prot_mh  # m3/t produit ÷ kg protéine/kg = L/kg protéine
        rows.append({"indicator": "Eau bleue", "label": f"Monde, {label} (Mekonnen & Hoekstra)", "system": sysname,
                     "unit": "L/kg protéine", "refs": f"{qid} ; Q-K-0010 ; Q-K-0127 (hyp.)",
                     "input_nature": nature(qid, "Q-K-0010", "Q-K-0127"), "prudent": round(v), "intermediaire": round(v),
                     "optimiste": round(v), "note": "base protéine de la source (127 g/kg), indépendante du rendement désossé"})
    cd = lo("Q-K-0018", "litre") / (lo("Q-K-0024", "%") * PCT)
    rows.append({"indicator": "Eau bleue", "label": "Référence ambitieuse 2030 (CE Delft)", "system": "standard",
                 "unit": "L/kg protéine", "refs": "Q-K-0018 ; Q-K-0024", "input_nature": nature("Q-K-0018", "Q-K-0024"),
                 "prudent": round(cd), "intermediaire": round(cd), "optimiste": round(cd),
                 "note": "même méthode que la voie B (CE Delft)"})
    for sysname, qid, label in [("standard", "Q-K-0030", "France standard"), ("label_rouge_bio", "Q-K-0034", "France Label Rouge"),
                                ("label_rouge_bio", "Q-K-0038", "France biologique")]:
        add("Eau (rareté)", label + ", AGRIBALYSE (m3 privés AWARE)", sysname, (lo(qid, "m3"),) * 2,
            "m3 éq. privés/kg protéine", qid, note="indicateur pondéré par la rareté, pas un volume")

    # Surfaces
    add("Surface", "Pays-Bas standard (WUR 1397)", "standard", rng("Q-K-0072", "m2a"), "m2·an/kg protéine", "Q-K-0072")
    add("Surface", "Pays-Bas Beter Leven 1 étoile (WUR 1397)", "certifie", rng("Q-K-0073", "m2a"), "m2·an/kg protéine", "Q-K-0073")
    add("Surface", "Brésil 2020, maïs + soja sans allocation (calcul K, Embrapa)", "standard", rng("Q-K-0100", "m2"),
        "m2·an/kg protéine", "Q-K-0100", note="surestimé : surface du soja non partagée avec l'huile")
    pl = lo("Q-K-0103", "per 100 g") * 10
    rows.append({"indicator": "Surface", "label": "Monde, Poore & Nemecek (moyenne)", "boundary": "détail", "system": "standard",
                 "unit": "m2·an/kg protéine", "refs": "Q-K-0103", "input_nature": nature("Q-K-0103"),
                 "prudent": pl, "intermediaire": pl, "optimiste": pl, "note": ""})
    cl = lo("Q-K-0016", "m2a") / (lo("Q-K-0024", "%") * PCT)
    rows.append({"indicator": "Surface", "label": "Référence ambitieuse 2030 (CE Delft)", "system": "standard",
                 "unit": "m2·an/kg protéine", "refs": "Q-K-0016 ; Q-K-0024", "input_nature": nature("Q-K-0016", "Q-K-0024"),
                 "prudent": round(cl, 1), "intermediaire": round(cl, 1), "optimiste": round(cl, 1),
                 "note": "même méthode que la voie B (CE Delft)"})
    pt_ratio = {"label_rouge/conventionnel": round(lo("Q-K-0033", "Pt") / lo("Q-K-0029", "Pt"), 2),
                "bio/conventionnel": round(lo("Q-K-0037", "Pt") / lo("Q-K-0029", "Pt"), 2)}
    return rows, pt_ratio


# ---------------------------------------------------------------------------
# Voie B — scénarios publiés, base protéine 21 % (Humbird) et recalcul 9 % (caille mesurée)
# ---------------------------------------------------------------------------
B_PROTEIN = {
    "prudent": lo("Q-C-0021", "g protein") * PCT,       # 8,8 % (bas de la mesure caille)
    "intermediaire": lo("Q-K-0126", "%") * PCT,         # 9 % (moyenne FSANZ, hypothèse Q-K-0126)
    "optimiste": lo("Q-C-0082", "%") * PCT,             # 21 % (hypothèse Humbird)
}
B_PROTEIN_MAX = hi("Q-K-0126", "%") * PCT               # 25 % (borne haute CE Delft, sensibilité)


def b_costs():
    cases = [
        ("Humbird 2021, fed-batch (masse humide)", rng("Q-E-0001", "$/kg"), "Q-E-0001"),
        ("Humbird 2021, perfusion", rng("Q-E-0002", "$/kg"), "Q-E-0002"),
        ("Humbird 2021, fed-batch + hydrolysat 2 $/kg", rng("Q-E-0006", "$/kg"), "Q-E-0006"),
        ("CE Delft 2021, 2030 tous leviers (produit CM)", rng("Q-E-0034", "$/kg"), "Q-E-0034"),
        ("CE Delft 2021, scénario actuel le plus coûteux", rng("Q-E-0033", "$/kg"), "Q-E-0033"),
        ("Risner 2021, limites levées (scénario 4)", rng("Q-E-0011", "USD/kg"), "Q-E-0011"),
        ("Risner 2021, référence 2019", rng("Q-E-0010", "USD/kg"), "Q-E-0010"),
        ("Pasitka 2024, résumé (6,2 $/lb, base non vérifiée)", tuple(x / LB_KG for x in rng("Q-E-0020", "lb")), "Q-E-0020"),
        ("Pasitka 2024 selon la revue Bry-Chevalier", rng("Q-E-0045", "$/kg"), "Q-E-0045"),
        ("Modèle E/X, scénario optimiste (biomasse humide)", (lo("Q-X-0001", "USD/kg protein") * lo("Q-K-0126", "%") * PCT,) * 2, "Q-X-0001 ; Q-K-0126"),
        ("Modèle E/X, scénario intermédiaire", (lo("Q-X-0002", "USD/kg protein") * lo("Q-K-0126", "%") * PCT,) * 2, "Q-X-0002 ; Q-K-0126"),
        ("Modèle E/X, scénario prudent", (lo("Q-X-0003", "USD/kg protein") * lo("Q-K-0126", "%") * PCT,) * 2, "Q-X-0003 ; Q-K-0126"),
    ]
    out = []
    for label, cost, refs in cases:
        c = (cost[0] + cost[1]) / 2
        ids = [x.strip() for x in refs.split(";")]
        out.append({"label": label, "cost_per_kg": round(c, 2), "refs": refs, "input_nature": nature(*ids),
                    "per_kg_protein_21pct": round(c / B_PROTEIN["optimiste"], 1),
                    "per_kg_protein_9pct": round(c / B_PROTEIN["intermediaire"], 1),
                    "per_kg_protein_8.8pct": round(c / B_PROTEIN["prudent"], 1),
                    "protein_refs": "Q-C-0082 (21 %, hypothèse) ; Q-K-0126/Q-C-0021 (9 %, 8,8 %, caille mesurée)"})
    return out


def b_env():
    rows = []
    cases = [
        ("GES", "Sinke 2023, 2030 énergie renouvelable (scopes 1-2 + partie du scope 3)", rng("Q-E-0037", "kg CO2"), "Q-E-0037", "kg CO2-eq/kg protéine"),
        ("GES", "Sinke 2023, 2030 mix électrique mondial", rng("Q-E-0038", "kg CO2"), "Q-E-0038", "kg CO2-eq/kg protéine"),
        ("GES", "CE Delft 2021, plage des scénarios 2030", rng("Q-K-0022", "kg CO2"), "Q-K-0022", "kg CO2-eq/kg protéine"),
        ("GES", "Risner 2025, intrants purifiés (qualité pharmaceutique)", rng("Q-E-0014", "kg CO2"), "Q-E-0014", "kg CO2-eq/kg protéine"),
        ("Énergie", "CE Delft 2021, demande d'énergie 2030", rng("Q-K-0021", "MJ"), "Q-K-0021", "MJ/kg protéine"),
        ("Eau bleue", "CE Delft 2021, eau bleue 2030", rng("Q-K-0017", "litre"), "Q-K-0017", "L/kg protéine"),
        ("Surface", "CE Delft 2021, occupation des sols 2030", rng("Q-K-0015", "m2a"), "Q-K-0015", "m2·an/kg protéine"),
    ]
    for ind, label, v, refs, unit in cases:
        r = {"indicator": ind, "label": label, "refs": refs + " ; Q-K-0126 (hyp. protéine) ; Q-C-0021",
             "input_nature": nature(refs, "Q-K-0126"), "unit": unit,
             "published_basis_25_to_18pct": (round(v[0] / B_PROTEIN_MAX, 1), round(v[1] / (lo("Q-K-0023", "%") * PCT), 1)),
             "recalc_9pct": (round(v[0] / B_PROTEIN["intermediaire"], 1), round(v[1] / B_PROTEIN["intermediaire"], 1))}
        rows.append(r)
    return rows


# ---------------------------------------------------------------------------
# Voie C — ingrédients et produits
# ---------------------------------------------------------------------------
def c_rows():
    out = []
    # Coûts / prix par kg de protéine
    out.append({"indicator": "Coût", "label": "Isolat de soja, prix de marché 2019-2023", "unit": "EUR/kg protéine",
                "values": rng("Q-E-0065", "€/kg protein"), "refs": "Q-E-0065", "input_nature": nature("Q-E-0065"),
                "usd": tuple(round(x * USD_PER_EUR[2022], 2) for x in rng("Q-E-0065")), "note": "prix, pas un coût ; USD au change 2022 (indicatif)"})
    esc = tuple(x / 1000 for x in rng("Q-E-0041", "protein"))
    out.append({"indicator": "Coût", "label": "e-SCP (bactéries H2), sites les moins chers 2028", "unit": "EUR/kg protéine",
                "values": esc, "refs": "Q-E-0041", "input_nature": nature("Q-E-0041"),
                "usd": tuple(round(x * USD_PER_EUR[2025], 2) for x in esc), "note": "sortie de modèle ; co-auteurs Solar Foods (SRC-E-0028)"})
    out.append({"indicator": "Coût", "label": "Mycoprotéine, TEA (Risner 2023)", "unit": "USD/kg protéine",
                "values": rng("Q-K-0085", "protein"), "refs": "Q-K-0085", "input_nature": nature("Q-K-0085"),
                "usd": rng("Q-K-0085"), "note": "3,55 $/kg de mycoprotéine humide à 11-12 % de protéines"})
    # GES
    def per_prot(qid_val, qid_prot, unit_v, unit_p, scale_p=PCT, factor=1.0):
        v = rng(qid_val, unit_v)
        p = rng(qid_prot, unit_p)
        return (round(v[0] * factor / (p[1] * scale_p), 1), round(v[1] * factor / (p[0] * scale_p), 1))
    out.append({"indicator": "GES", "label": "Protéine microbienne H2 (Järviö 2021, mix finlandais)", "unit": "kg CO2-eq/kg protéine",
                "values": tuple(x * 10 for x in rng("Q-K-0089", "100 g")), "refs": "Q-K-0089", "input_nature": nature("Q-K-0089"),
                "note": "hydroélectricité : ~8 fois moins (par kg de produit)"})
    out.append({"indicator": "GES", "label": "Mycoprotéine (Shahid 2024 ÷ 11 % de protéines)", "unit": "kg CO2-eq/kg protéine",
                "values": per_prot("Q-A-0064", "Q-A-0019", "kg CO2", "g/100"), "refs": "Q-A-0064 ; Q-A-0019",
                "input_nature": nature("Q-A-0064", "Q-A-0019"), "note": "co-auteur industriel (CT-11)"})
    out.append({"indicator": "GES", "label": "Tofu, Poore & Nemecek (moyenne)", "unit": "kg CO2-eq/kg protéine",
                "values": (lo("Q-K-0104", "100 g") * 10,) * 2, "refs": "Q-K-0104", "input_nature": nature("Q-K-0104"), "note": ""})
    out.append({"indicator": "GES", "label": "Tofu, ifeu 2020 (÷ 11 % de protéines CE Delft)", "unit": "kg CO2-eq/kg protéine",
                "values": per_prot("Q-K-0094", "Q-K-0025", "kg CO2", "%"), "refs": "Q-K-0094 ; Q-K-0025",
                "input_nature": nature("Q-K-0094", "Q-K-0025"), "note": "deux sources combinées (Allemagne / Pays-Bas)"})
    out.append({"indicator": "GES", "label": "Pois (graine), Poore & Nemecek (moyenne)", "unit": "kg CO2-eq/kg protéine",
                "values": (lo("Q-K-0106", "100 g") * 10,) * 2, "refs": "Q-K-0106", "input_nature": nature("Q-K-0106"), "note": "ingrédient brut"})
    out.append({"indicator": "GES", "label": "Escalope végétale soja, AGRIBALYSE (produit, toutes étapes)", "unit": "kg CO2-eq/kg protéine",
                "values": per_prot("Q-K-0042", "Q-K-0125", "kg CO2", "g/100"), "refs": "Q-K-0042 ; Q-K-0125 (hyp.)",
                "input_nature": nature("Q-K-0042", "Q-K-0125"), "note": "inclut emballage, distribution, consommation"})
    out.append({"indicator": "GES", "label": "Nuggets de soja, AGRIBALYSE (produit)", "unit": "kg CO2-eq/kg protéine",
                "values": per_prot("Q-K-0044", "Q-K-0125", "kg CO2", "g/100"), "refs": "Q-K-0044 ; Q-K-0125 (hyp.)",
                "input_nature": nature("Q-K-0044", "Q-K-0125"), "note": ""})
    # Valeurs de l'agent S (phase 4), lues dans agents/S/quant.csv
    out.append({"indicator": "GES", "label": "Protéine bactérienne FeedKind (méthanotrophe, aliment), biogaz+renouvelable → gaz fossile", "unit": "kg CO2-eq/kg protéine",
                "values": (lo("Q-S-0053", "t protein"), lo("Q-S-0051", "t protein")), "refs": "Q-S-0053 ; Q-S-0051", "input_nature": nature("Q-S-0053", "Q-S-0051"),
                "note": "t/t = kg/kg ; ingrédient pour l'alimentation animale"})
    out.append({"indicator": "GES", "label": "Concentré protéique de soja (référence du rapport FeedKind)", "unit": "kg CO2-eq/kg protéine",
                "values": rng("Q-S-0054", "protein"), "refs": "Q-S-0054", "input_nature": nature("Q-S-0054"), "note": "ingrédient"})
    out.append({"indicator": "GES", "label": "Mycoprotéine Quorn 2018 (Carbon Trust) ÷ 11 % de protéines", "unit": "kg CO2-eq/kg protéine",
                "values": per_prot("Q-S-0019", "Q-A-0019", "kg CO2", "g/100"), "refs": "Q-S-0019 ; Q-A-0019",
                "input_nature": nature("Q-S-0019", "Q-A-0019"), "note": "déclaration d'entreprise"})
    out.append({"indicator": "GES", "label": "Tofu au supermarché, RIVM 2024 (÷ 11 % de protéines)", "unit": "kg CO2-eq/kg protéine",
                "values": per_prot("Q-S-0087", "Q-K-0025", "kg CO2", "%"), "refs": "Q-S-0087 ; Q-K-0025",
                "input_nature": nature("Q-S-0087", "Q-K-0025"), "note": "Pays-Bas"})
    # Énergie
    p65 = lo("Q-K-0090", "%") * PCT
    out.append({"indicator": "Énergie", "label": "Protéine microbienne H2 (Järviö 2021), hydro → mix finlandais", "unit": "MJ/kg protéine",
                "values": (round(lo("Q-K-0116", "MJ") / p65), round(lo("Q-K-0087", "MJ") / p65)), "refs": "Q-K-0116 ; Q-K-0087 ; Q-K-0090",
                "input_nature": nature("Q-K-0116", "Q-K-0087", "Q-K-0090"), "note": "demande cumulée d'énergie (CED)"})
    out.append({"indicator": "Énergie", "label": "e-SCP 2030, électricité seule (Fasihi 2025)", "unit": "MJ/kg protéine",
                "values": tuple(round(x * KWH_MJ) for x in rng("Q-E-0042", "MWh")), "refs": "Q-E-0042", "input_nature": nature("Q-E-0042"),
                "note": "MWh/t = kWh/kg ; électricité finale"})
    out.append({"indicator": "Énergie", "label": "Escalope végétale soja, AGRIBALYSE (MJ non renouvelables, toutes étapes)", "unit": "MJ/kg protéine",
                "values": per_prot("Q-K-0043", "Q-K-0125", "MJ", "g/100"), "refs": "Q-K-0043 ; Q-K-0125 (hyp.)",
                "input_nature": nature("Q-K-0043", "Q-K-0125"), "note": "transformation = 61 % du total"})
    out.append({"indicator": "Énergie", "label": "Tofu, ifeu 2020 (énergie primaire ÷ 11 %)", "unit": "MJ/kg protéine",
                "values": per_prot("Q-K-0118", "Q-K-0025", "kWh", "%", factor=KWH_MJ), "refs": "Q-K-0118 ; Q-K-0025",
                "input_nature": nature("Q-K-0118", "Q-K-0025"), "note": ""})
    # Eau bleue
    out.append({"indicator": "Eau bleue", "label": "Tofu, CE Delft 2021", "unit": "L/kg protéine",
                "values": per_prot("Q-K-0019", "Q-K-0025", "litre", "%"), "refs": "Q-K-0019 ; Q-K-0025",
                "input_nature": nature("Q-K-0019", "Q-K-0025"), "note": "même méthode que B et la référence poulet CE Delft"})
    # Surface
    out.append({"indicator": "Surface", "label": "Tofu, Poore & Nemecek (moyenne)", "unit": "m2·an/kg protéine",
                "values": (lo("Q-K-0105", "100 g") * 10,) * 2, "refs": "Q-K-0105", "input_nature": nature("Q-K-0105"), "note": ""})
    out.append({"indicator": "Surface", "label": "Tofu, CE Delft 2021", "unit": "m2·an/kg protéine",
                "values": per_prot("Q-K-0020", "Q-K-0025", "m2a", "%"), "refs": "Q-K-0020 ; Q-K-0025",
                "input_nature": nature("Q-K-0020", "Q-K-0025"), "note": ""})
    out.append({"indicator": "Surface", "label": "Pois (graine), Poore & Nemecek (moyenne)", "unit": "m2·an/kg protéine",
                "values": (lo("Q-K-0119", "100 g") * 10,) * 2, "refs": "Q-K-0119", "input_nature": nature("Q-K-0119"), "note": ""})
    out.append({"indicator": "Surface", "label": "Soja (graine), rendement protéique mondial", "unit": "m2·an/kg protéine",
                "values": (round(1000 / lo("Q-A-0023", "g prot"), 1),) * 2, "refs": "Q-A-0023", "input_nature": nature("Q-A-0023"), "note": "1/rendement"})
    out.append({"indicator": "Surface", "label": "SCP photovoltaïque (modèle, borne)", "unit": "m2·an/kg protéine",
                "values": (0.0, round(1000 / lo("Q-A-0024", "g prot"), 2)), "refs": "Q-A-0024", "input_nature": nature("Q-A-0024"), "note": "« >1 200 g/m2/an » → < 0,83"})
    return out



# ---------------------------------------------------------------------------
# Base 3 : protéine de qualité équivalente (DIAAS tronqué à 100 %, hypothèse Q-K-0186)
# ---------------------------------------------------------------------------
def diaas_rows(aenv, crow):
    cap = lo("Q-K-0186", "%") * PCT
    f = lambda qid, which=None: min((rng(qid, "%")[0 if which == "lo" else 1] if which else mid(qid, "%")) * PCT, cap)
    factors = {
        "poulet (filet et cuisse, in vitro)": ((f("Q-S-0036"),) * 2, "Q-S-0036"),
        "analogues végétaux de poulet du commerce (in vitro, 5 produits)": ((f("Q-S-0015", "lo"), f("Q-S-0015", "hi")), "Q-S-0015"),
        "biomasse de mycoprotéine (enfant → adulte)": ((f("Q-S-0001"), f("Q-S-0002")), "Q-S-0001 ; Q-S-0002"),
        "poudre Solein (protéine bactérienne H2)": ((f("Q-S-0017"),) * 2, "Q-S-0017"),
    }
    rows = []
    def adj(label, vals, fac, refs_v, refs_f, unit):
        lo_v, hi_v = vals
        rows.append({"label": label, "unit": unit.replace("kg protéine", "kg protéine de qualité équivalente"),
                     "per_kg_protein": f"{lo_v}–{hi_v}" if lo_v != hi_v else f"{lo_v}",
                     "diaas_factor": f"{fac[0]:.2f}–{fac[1]:.2f}" if fac[0] != fac[1] else f"{fac[0]:.2f}",
                     "per_kg_quality_protein": (round(lo_v / fac[1], 1), round(hi_v / fac[0], 1)), "refs": refs_v + " ; " + refs_f})
    ch = factors["poulet (filet et cuisse, in vitro)"]
    retail = [r for r in aenv if r["indicator"] == "GES" and "AGRIBALYSE toutes étapes" in r["label"]]
    adj("Poulet cru, AGRIBALYSE toutes étapes (GES)", (min(r["optimiste"] for r in retail), max(r["prudent"] for r in retail)),
        ch[0], "Q-K-0045 ; Q-K-0040", ch[1], "kg CO2-eq/kg protéine")
    veg = [r for r in crow if r["indicator"] == "GES" and "AGRIBALYSE" in r["label"]]
    an = factors["analogues végétaux de poulet du commerce (in vitro, 5 produits)"]
    adj("Analogues végétaux de soja, AGRIBALYSE (GES)", (min(r["values"][0] for r in veg), max(r["values"][1] for r in veg)),
        an[0], "Q-K-0042 ; Q-K-0044 ; Q-K-0125", an[1], "kg CO2-eq/kg protéine")
    my = factors["biomasse de mycoprotéine (enfant → adulte)"]
    adj("Mycoprotéine, coût TEA", rng("Q-K-0085", "protein"), my[0], "Q-K-0085", my[1], "USD/kg protéine")
    myg = [r for r in crow if r["indicator"] == "GES" and "ycoprotéine" in r["label"]]
    adj("Mycoprotéine, GES (Shahid 2024 ; Quorn 2018)", (min(r["values"][0] for r in myg), max(r["values"][1] for r in myg)),
        my[0], "Q-A-0064 ; Q-S-0019", my[1], "kg CO2-eq/kg protéine")
    so = factors["poudre Solein (protéine bactérienne H2)"]
    esc = [r for r in crow if r["label"].startswith("e-SCP (bactéries H2)")][0]
    adj("Protéine bactérienne H2, coût e-SCP 2028 (USD)", esc["usd"], so[0], "Q-E-0041", so[1], "USD/kg protéine")
    jg = [r for r in crow if r["label"].startswith("Protéine microbienne H2 (Järviö 2021, mix")][0]
    adj("Protéine bactérienne H2, GES (Järviö 2021)", jg["values"], so[0], "Q-K-0089", so[1], "kg CO2-eq/kg protéine")
    return factors, rows

# ---------------------------------------------------------------------------
# Sensibilité (un facteur à la fois autour du scénario intermédiaire)
# ---------------------------------------------------------------------------
def tornado(base_fn, factors):
    base = base_fn({})
    rows = []
    for name, (lo_v, hi_v), refs in factors:
        a, b = base_fn({name: lo_v}), base_fn({name: hi_v})
        rows.append({"factor": name, "low_value": round(lo_v, 4), "high_value": round(hi_v, 4),
                     "result_low": round(a, 1), "result_high": round(b, 1),
                     "ratio_max_min": round(max(a, b) / min(a, b), 2), "refs": refs})
    rows.sort(key=lambda r: -r["ratio_max_min"])
    return round(base, 1), rows


def sensitivity():
    out = {}
    # (1) Coût A standard, UE six pays 2021 (EUR2021/kg protéine)
    farm = rng("Q-K-0059", "cents"); sl = rng("Q-K-0060", "cents"); cy = lo("Q-K-0061", "%") * PCT
    ys = YIELD["standard"]

    def a_cost(o):
        f = o.get("farm", mid("Q-K-0059") * PCT); s_ = o.get("slaughter", mid("Q-K-0060") * PCT)
        y = o.get("yield", ys["intermediaire"]); p = o.get("protein", PROTEIN_MEAT["intermediaire"])
        d = o.get("protein_definition", 1.0)
        return (f + s_ * cy) / (y * p * d)
    out["A_cost_standard_EU6_2021"] = tornado(a_cost, [
        ("farm", (farm[0] * PCT, farm[1] * PCT), "Q-K-0059"),
        ("slaughter", (sl[0] * PCT, sl[1] * PCT), "Q-K-0060"),
        ("yield", (ys["prudent"], ys["optimiste"]), ys["refs"]),
        ("protein", (PROTEIN_MEAT["prudent"], PROTEIN_MEAT["optimiste"]), PROTEIN_REFS),
        ("protein_definition", (AA_RATIO, 1.0), "Q-K-0053/Q-K-0052 (acides aminés vs N×facteur)"),
    ])
    # (1b) Coût A : choix du système (standard → bio), France 2022
    out["A_cost_system_choice_FR2022"] = {
        "standard": round((lo("Q-E-0029") + lo("Q-K-0112") * PCT * cy) / (ys["intermediaire"] * PROTEIN_MEAT["intermediaire"]), 1),
        "label_rouge": round((lo("Q-E-0030") + lo("Q-K-0128") * PCT * hi("Q-K-0121") * PCT) /
                             (YIELD["label_rouge_bio"]["intermediaire"] * PROTEIN_MEAT["intermediaire"]), 1),
        "bio": round((lo("Q-E-0031") + lo("Q-K-0128") * PCT * hi("Q-K-0121") * PCT) /
                     (YIELD["label_rouge_bio"]["intermediaire"] * PROTEIN_MEAT["intermediaire"]), 1),
        "unit": "EUR2022/kg protéine comestible", "refs": "Q-E-0029/0030/0031 ; Q-K-0112 ; Q-K-0128 ; Q-K-0121 ; rendements"}
    # (2) Coût B (USD/kg protéine) : coût de la biomasse et teneur en protéines
    bio_lo = lo("Q-X-0001") * lo("Q-K-0126", "%") * PCT
    bio_hi = lo("Q-X-0003") * lo("Q-K-0126", "%") * PCT
    bio_mid = lo("Q-X-0002") * lo("Q-K-0126", "%") * PCT

    def b_cost(o):
        return o.get("biomass_cost", bio_mid) / o.get("protein", B_PROTEIN["intermediaire"])
    out["B_cost_E_model"] = tornado(b_cost, [
        ("biomass_cost", (bio_lo, bio_hi), "Q-X-0001 / Q-X-0003 (× 0,09)"),
        ("protein", (B_PROTEIN["prudent"], B_PROTEIN_MAX), "Q-C-0021 ; Q-K-0126 (8,8-25 %)"),
    ])
    # (3) GES A standard (NL, WUR 1397) : LUC, allocation, rendement, protéine
    luc = (lo("Q-K-0070"), lo("Q-K-0069"))

    def a_ghg(o):
        g = o.get("LUC", luc[1]); al = o.get("allocation", ALLOC["intermediaire"])
        return g * al / (o.get("yield", ys["intermediaire"]) * o.get("protein", PROTEIN_MEAT["intermediaire"]))
    out["A_GHG_standard_NL"] = tornado(a_ghg, [
        ("LUC", luc, "Q-K-0070 (sans) / Q-K-0069 (avec)"),
        ("allocation", (ALLOC["optimiste"], ALLOC["prudent"]), "Q-K-0124"),
        ("yield", (ys["prudent"], ys["optimiste"]), ys["refs"]),
        ("protein", (PROTEIN_MEAT["prudent"], PROTEIN_MEAT["optimiste"]), PROTEIN_REFS),
    ])
    # (4) GES B : énergie / pureté des intrants / protéine
    s_ren, s_mix = lo("Q-E-0037"), lo("Q-E-0038")

    def b_ghg(o):
        return o.get("energy_and_purity", s_mix) / o.get("protein", B_PROTEIN["intermediaire"])
    out["B_GHG"] = tornado(b_ghg, [
        ("energy_and_purity", (s_ren, hi("Q-E-0014")), "Q-E-0037 (renouvelable) → Q-E-0014 (intrants purifiés, Risner)"),
        ("protein", (B_PROTEIN["prudent"], B_PROTEIN_MAX), "Q-C-0021 ; Q-K-0126"),
    ])
    return out


def parity(a_cost_rows):
    """Coût maximal admissible du kg de biomasse humide (voie B) pour égaler le coût protéique de la voie A."""
    out = []
    for r in a_cost_rows:
        if r["system"] != "standard":
            continue
        t = r["prudent"]["per_kg_protein_usd"]  # haut de plage A (le plus favorable à B)
        out.append({"comparator": r["label"], "A_usd_per_kg_protein_high": t,
                    "max_biomass_usd_per_kg_at_9pct": round(t * B_PROTEIN["intermediaire"], 2),
                    "max_biomass_usd_per_kg_at_21pct": round(t * B_PROTEIN["optimiste"], 2)})
    return out


def ct10():
    """CT-10 : base « animal entier » (EV-A-0042) vs « viande désossée comestible »."""
    whole = lo("Q-N-0034", "g/kg") / 1000                     # kg protéine / kg PV, animal entier
    edible = YIELD["standard"]["intermediaire"] * PROTEIN_MEAT["intermediaire"]
    price = lo("Q-A-0053", "USD")
    return {"protein_whole_animal_kg_per_kg_lw": whole, "edible_protein_kg_per_kg_lw": round(edible, 4),
            "ratio_whole_to_edible": round(whole / edible, 2),
            "EV-A-0042_price_whole_basis_usd_per_kg_protein": price,
            "same_price_on_edible_basis_usd_per_kg_protein": round(price * whole / edible, 1),
            "refs": "Q-N-0034 ; Q-A-0053 ; rendement Q-N-0014 ; protéine Q-K-0046"}



# ---------------------------------------------------------------------------
# Tableau final (synthèse des plages, toutes sources et scénarios confondus)
# ---------------------------------------------------------------------------
def _span(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return "n.d."
    a, b = min(vals), max(vals)
    f = (lambda x: f"{x:.0f}") if b >= 100 else (lambda x: f"{x:.1f}")
    return f(a) if abs(a - b) < 1e-9 else f"{f(a)}–{f(b)}"


def summary(acost, aenv, bcost, benv, crow):
    def a_rows(pred_label, indicator=None):
        return [r for r in aenv if pred_label(r) and (indicator is None or r["indicator"] == indicator)]

    def env_vals(rows):
        return [r[s] for r in rows for s in SCEN]

    def natures(rows):
        return " + ".join(sorted({n for r in rows for n in r["input_nature"].split(" + ")})) or "—"

    def nat_set(strings):
        return " + ".join(sorted({n for x in strings for n in x.split(" + ") if n})) or "—"

    lines = []
    gate = lambda r: r.get("boundary", "porte") == "porte"
    groups = {
        "A standard (porte d'abattoir)": (lambda r: r["system"] == "standard", lambda r: r["system"] == "standard" and gate(r)),
        "A standard (produit au détail, toutes étapes)": (lambda r: False, lambda r: r["system"] == "standard" and not gate(r)),
        "A certifié (ECC / Beter Leven)": (lambda r: r["system"] == "certifie", lambda r: r["system"] == "certifie"),
        "A Label Rouge": (lambda r: "Label Rouge" in r["label"], lambda r: "Label Rouge" in r["label"]),
        "A biologique / pâturage": (lambda r: ("biologique" in r["label"] or "pâturage" in r["label"]),
                                    lambda r: ("biologique" in r["label"] or "pâturage" in r["label"])),
    }
    for name, (pc, pe) in groups.items():
        cr = [r for r in acost if pc(r)]
        row = {"line": name,
               "cost_usd": _span([r[s]["per_kg_protein_usd"] for r in cr for s in SCEN]),
               "cost_cases": "; ".join(r["label"] for r in cr) or "—", "cost_nature": nat_set(r["input_nature"] for r in cr)}
        for ind in ("GES", "Énergie", "Eau bleue", "Surface"):
            rows = a_rows(pe, ind)
            if ind == "Eau bleue" and name == "A biologique / pâturage":
                rows = a_rows(lambda r: "pâturage" in r["label"], ind)
            if ind == "Eau bleue" and name == "A Label Rouge":
                rows = a_rows(lambda r: "classe mixte" in r["label"], ind)
            row[ind] = _span(env_vals(rows)); row[ind + "_nature"] = natures(rows)
        lines.append(row)
    # B : scénarios « à l'échelle » (on exclut les scénarios « actuels » de CE Delft et la référence 2019 de Risner)
    scale = [r for r in bcost if "actuel" not in r["label"] and "référence 2019" not in r["label"]]
    for name, key, envkey in [("B, base publiée (21 % ; 18-25 % pour les ACV)", "per_kg_protein_21pct", "published_basis_25_to_18pct"),
                              ("B, recalcul à 9 % de protéines (caille mesurée)", "per_kg_protein_9pct", "recalc_9pct")]:
        row = {"line": name, "cost_usd": _span([r[key] for r in scale]),
               "cost_cases": "; ".join(r["label"] for r in scale), "cost_nature": "model_output (+ model_assumption)"}
        for ind in ("GES", "Énergie", "Eau bleue", "Surface"):
            rows = [r for r in benv if r["indicator"] == ind and ("Risner" not in r["label"])]
            row[ind] = _span([v for r in rows for v in r[envkey]]); row[ind + "_nature"] = "model_output + model_assumption"
        risner = [r for r in benv if "Risner" in r["label"]][0]
        row["GES"] += f" (intrants purifiés : {_span(list(risner[envkey]))})"
        lines.append(row)
    for name, pred in [("C ingrédients (soja, pois, tofu, mycoprotéine, SCP ; porte d'usine ou détail selon la source)", lambda r: "AGRIBALYSE" not in r["label"]),
                       ("C produits (analogues végétaux AGRIBALYSE, toutes étapes)", lambda r: "AGRIBALYSE" in r["label"])]:
        rr = [r for r in crow if pred(r)]
        cost = [r for r in rr if r["indicator"] == "Coût"]
        row = {"line": name, "cost_usd": _span([v for r in cost for v in r["usd"]]) if cost else "n.d.",
               "cost_cases": "; ".join(r["label"] for r in cost) or "aucun coût de produit trouvé",
               "cost_nature": nat_set(r["input_nature"] for r in cost)}
        for ind in ("GES", "Énergie", "Eau bleue", "Surface"):
            rows = [r for r in rr if r["indicator"] == ind and "borne" not in r["label"]]
            row[ind] = _span([v for r in rows for v in r["values"]]); row[ind + "_nature"] = nat_set(r["input_nature"] for r in rows)
            bounds = [r for r in rr if r["indicator"] == ind and "borne" in r["label"]]
            for b in bounds:
                row[ind] += f" (SCP photovoltaïque modélisée : < {b['values'][1]})"
        lines.append(row)
    return lines


# ---------------------------------------------------------------------------
def fmt3(r, key=None):
    if key:
        return " / ".join(str(r[s][key]) for s in SCEN)
    return " / ".join(str(r[s]) for s in SCEN)


def main():
    acost = a_costs()
    aenv, pt_ratio = a_env()
    bcost = b_costs()
    benv = b_env()
    crow = c_rows()
    sens = sensitivity()
    par = parity(acost)
    c10 = ct10()
    summ = summary(acost, aenv, bcost, benv, crow)
    dfac, drows = diaas_rows(aenv, crow)

    L = ["# Résultats du modèle de comparaison (agent K) — sorties de modèle, pas des mesures", "",
         "Base : **kg de protéine comestible** (N × facteur). Scénarios notés *prudent / intermédiaire / optimiste*. "
         "Aucune correction d'inflation ; USD au change BCE de l'année de la donnée. "
         "Nature des intrants indiquée ligne par ligne (statistical, published_estimate, model_output, company_claim, model_assumption…).", "",
         "## 0. Tableau final — par kg de protéine comestible (plages toutes sources et scénarios confondus)", "",
         "| Ligne | Coût (USD de l'année de la donnée) | GES (kg CO2-eq) | Énergie (MJ) | Eau bleue (L) | Surface (m2·an) |",
         "|---|---|---|---|---|---|"]
    for r in summ:
        L.append(f"| {r['line']} | {r['cost_usd']} | {r['GES']} | {r['Énergie']} | {r['Eau bleue']} | {r['Surface']} |")
    L += ["", "Nature des chiffres par ligne :", ""]
    for r in summ:
        L.append(f"- **{r['line']}** — coût : {r['cost_nature']} ({r['cost_cases']}) ; GES : {r['GES_nature']} ; énergie : {r['Énergie_nature']} ; "
                 f"eau : {r['Eau bleue_nature']} ; surface : {r['Surface_nature']}.")
    L += ["", "Avertissements : (1) les indicateurs d'énergie ne sont pas homogènes (A : MJ non renouvelables EF ou énergie primaire ; B : demande "
          "d'énergie CE Delft ; C : CED ou électricité) ; (2) l'eau bleue de la voie A selon Mekonnen & Hoekstra (1 654-5 780 L) et selon CE Delft (200 L) "
          "diffère d'un facteur 8 à 30 à cause des périmètres et de l'irrigation supposée ; (3) les coûts mélangent des années 2017-2025 sans inflation ; "
          "(4) les coûts de B sont des sorties de TEA, ceux de A des estimations publiées ou statistiques ; (5) les plages ne sont pas des intervalles de confiance.", "",
         "## 1. Facteurs de conversion de la voie A", "",
         "| Facteur | Prudent | Intermédiaire | Optimiste | Réf. |", "|---|---|---|---|---|",
         f"| Protéine de la viande désossée crue (kg/kg) | {PROTEIN_MEAT['prudent']:.3f} | {PROTEIN_MEAT['intermediaire']:.3f} | {PROTEIN_MEAT['optimiste']:.3f} | {PROTEIN_REFS} |"]
    for k, v in YIELD.items():
        L.append(f"| Viande désossée / poids vif — {k} | {v['prudent']:.3f} | {v['intermediaire']:.3f} | {v['optimiste']:.3f} | {v['refs']} |")
    L.append(f"| Allocation des impacts à la viande | {ALLOC['prudent']} | {ALLOC['intermediaire']} | {ALLOC['optimiste']} | Q-K-0124 ; Q-K-0006 |")
    L.append(f"| Rapport protéine acides aminés / N×facteur (filet) | {AA_RATIO:.3f} | | | Q-K-0053 / Q-K-0052 |")
    L += ["", "Protéine comestible par kg de poids vif (rendement × protéine) :", ""]
    for k in YIELD:
        L.append(f"- {k} : " + " / ".join(f"{edible_protein_per_kg_lw(k, s):.3f}" for s in SCEN) + " kg/kg PV")

    L += ["", "## 2. Voie A — coût par kg de protéine comestible (100 % des coûts imputés à la viande désossée)", "",
          "| Cas | Monnaie | Coût par kg PV (ferme + abattage) | Coût / kg protéine (monnaie d'origine) | idem en USD de l'année | Nature des intrants | Réf. |",
          "|---|---|---|---|---|---|---|"]
    for r in acost:
        L.append(f"| {r['label']} | {r['currency']}{r['year']} | {fmt3(r, 'per_kg_lw')} | {fmt3(r, 'per_kg_protein_orig')} | "
                 f"{fmt3(r, 'per_kg_protein_usd')} | {r['input_nature']} | {r['refs']} ; rendement {r['yield_refs']} |")

    L += ["", "## 3. Voie A — environnement par kg de protéine comestible", "",
          "| Indicateur | Cas | Système | Périmètre | Prudent / Intermédiaire / Optimiste | Unité | Nature | Réf. | Remarque |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in aenv:
        L.append(f"| {r['indicator']} | {r['label']} | {r['system']} | {r.get('boundary', 'porte')} | {fmt3(r)} | {r['unit']} | {r['input_nature']} | {r['refs']} | {r.get('note', '')} |")
    L += ["", f"Utilisation du sol AGRIBALYSE (points, non convertibles en m2) : rapport Label Rouge/conventionnel = {pt_ratio['label_rouge/conventionnel']}, "
          f"bio/conventionnel = {pt_ratio['bio/conventionnel']} (Q-K-0029, Q-K-0033, Q-K-0037)."]

    L += ["", "## 4. Voie B — coût par kg de protéine (scénarios publiés ; USD de l'étude, ≈ 2018-2024)", "",
          "| Scénario | Coût publié $/kg (biomasse humide ou produit) | $/kg protéine à 21 % | à 9 % | à 8,8 % | Nature | Réf. |",
          "|---|---|---|---|---|---|---|"]
    for r in bcost:
        L.append(f"| {r['label']} | {r['cost_per_kg']} | {r['per_kg_protein_21pct']} | {r['per_kg_protein_9pct']} | {r['per_kg_protein_8.8pct']} | {r['input_nature']} | {r['refs']} |")
    L += ["", "## 5. Voie B — environnement par kg de protéine", "",
          "| Indicateur | Cas | Base publiée (25 %→18 % de protéines) | Recalcul à 9 % | Unité | Nature | Réf. |", "|---|---|---|---|---|---|---|"]
    for r in benv:
        a, b = r["published_basis_25_to_18pct"]; c, d = r["recalc_9pct"]
        L.append(f"| {r['indicator']} | {r['label']} | {a}–{b} | {c}–{d} | {r['unit']} | {r['input_nature']} | {r['refs']} |")
    L += ["", "Hypothèse forte (Q-K-0126) : l'impact par kg de produit est gardé constant quand la teneur en protéines passe de 18-25 % à 9 %. "
          "Une biomasse plus aqueuse pourrait réduire l'impact par kg de produit ; aucune ACV ne l'a modélisé."]

    L += ["", "## 6. Voie C — ingrédients et produits par kg de protéine", "",
          "| Indicateur | Cas | Valeurs | Unité | idem USD | Nature | Réf. | Remarque |", "|---|---|---|---|---|---|---|---|"]
    for r in crow:
        v = r["values"]; vs = f"{v[0]}–{v[1]}" if v[0] != v[1] else f"{v[0]}"
        u = r.get("usd"); us = (f"{u[0]}–{u[1]}" if u and u[0] != u[1] else (f"{u[0]}" if u else ""))
        L.append(f"| {r['indicator']} | {r['label']} | {vs} | {r['unit']} | {us} | {r['input_nature']} | {r['refs']} | {r['note']} |")
    L += ["", "Aucun coût de **produit fini** de la voie C n'a été trouvé ; seul un prix relatif existe (viandes végétales +77 % au poids vs viande conventionnelle aux États-Unis en 2023, Q-K-0101)."]

    L += ["", "## 6 bis. Base 3 — kg de protéine de qualité équivalente (DIAAS tronqué à 100 %, Q-K-0186)", "",
          "Facteurs (min(DIAAS ; 100)/100) : " + " ; ".join(f"{k} {v[0][0]:.2f}–{v[0][1]:.2f} ({v[1]})" for k, v in dfac.items()) + ".", "",
          "| Cas | Par kg de protéine | Facteur DIAAS | Par kg de protéine de qualité équivalente | Unité | Réf. |", "|---|---|---|---|---|---|"]
    for r in drows:
        a, b = r["per_kg_quality_protein"]
        L.append(f"| {r['label']} | {r['per_kg_protein']} | {r['diaas_factor']} | {a}–{b} | {r['unit']} | {r['refs']} |")
    L += ["", "DIAAS de la biomasse de poulet cultivée : inconnu (aucune mesure) ; la voie B n'est pas ajustée.",
          "", "## 7. Analyse de sensibilité (un facteur à la fois, autour du scénario intermédiaire)", ""]
    for k, v in sens.items():
        if k == "A_cost_system_choice_FR2022":
            L += [f"### {k}", "", f"standard {v['standard']} ; Label Rouge {v['label_rouge']} ; bio {v['bio']} {v['unit']} ({v['refs']})", ""]
            continue
        base, rows = v
        L += [f"### {k} (base {base})", "", "| Facteur | Valeur basse → haute | Résultat bas | Résultat haut | Rapport max/min | Réf. |", "|---|---|---|---|---|---|"]
        for r in rows:
            L.append(f"| {r['factor']} | {r['low_value']} → {r['high_value']} | {r['result_low']} | {r['result_high']} | {r['ratio_max_min']} | {r['refs']} |")
        L.append("")
    L += ["## 8. Seuils de parité (coût maximal de la biomasse humide pour égaler le haut de plage de la voie A standard)", "",
          "| Comparateur A | A, USD/kg protéine (prudent) | Biomasse max. à 9 % | à 21 % |", "|---|---|---|---|"]
    for r in par:
        L.append(f"| {r['comparator']} | {r['A_usd_per_kg_protein_high']} | {r['max_biomass_usd_per_kg_at_9pct']} | {r['max_biomass_usd_per_kg_at_21pct']} |")
    L += ["", "## 9. CT-10 — base « animal entier » vs « protéine comestible »", "",
          f"Protéine de l'animal entier {c10['protein_whole_animal_kg_per_kg_lw']} kg/kg PV contre {c10['edible_protein_kg_per_kg_lw']} kg/kg PV de protéine comestible "
          f"(rapport {c10['ratio_whole_to_edible']}). Le prix de 4,6 USD/kg de protéine (animal entier, EV-A-0042) équivaut à "
          f"{c10['same_price_on_edible_basis_usd_per_kg_protein']} USD/kg de protéine comestible ({c10['refs']}).", "",
          "## 10. Lignes Q utilisées", "", "| Q | Paramètre | Valeur | Unité | Nature | Source |", "|---|---|---|---|---|---|"]
    for k in sorted(USED):
        u = USED[k]
        L.append(f"| {k} | {u['parameter'][:90]} | {u['value']} | {u['unit_original']} | {u['data_nature']} | {u['source_id']} |")

    out = {"summary": summ, "protein_meat": PROTEIN_MEAT, "yield": YIELD, "alloc": ALLOC, "aa_ratio": AA_RATIO, "A_costs": acost, "A_env": aenv,
           "A_landuse_points_ratio": pt_ratio, "B_costs": bcost, "B_env": benv, "C": crow, "sensitivity": sens,
           "parity": par, "CT10": c10, "DIAAS_factors": {k: v[0] for k, v in dfac.items()}, "DIAAS_rows": drows, "Q_used": USED}
    (HERE / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    (HERE / "results.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
