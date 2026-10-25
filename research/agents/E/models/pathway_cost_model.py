#!/usr/bin/env python3
"""Modèle économique transparent comparant trois voies de production de muscle de poulet.

Agent E (Chicken Muscle Research Lab), session du 2026-10-25.

Principes
---------
* Chaque paramètre porte une référence : identifiant `Q-…` de la base (valeur sourcée)
  ou la mention `model_assumption` (hypothèse de l'agent E, à remplacer par une mesure).
* Les résultats sont des SORTIES DE MODÈLE (`model_output`) : ce ne sont pas des coûts
  industriels démontrés. Aucune usine de viande cultivée n'a publié de coûts réels.
* Monnaies : chaque intrant garde sa monnaie et son année. Les conversions de change
  utilisent les moyennes annuelles BCE (Q-E-0061…0064). AUCUNE correction d'inflation
  n'est appliquée : comparer des EUR2017, EUR2022 et USD2020 reste approximatif.
* Bases de calcul : poids vif (PV), carcasse, viande désossée comestible, masse cellulaire
  humide, protéine. Les conversions sont explicites (fonctions ci-dessous).

Voies
-----
A  Élevage conventionnel / label / bio : coûts statistiques ou estimés (données d'enquête
   ou modèles d'exploitation type), convertis en coût par kg de viande désossée puis par kg
   de protéine, en imputant 100 % des coûts à la viande (hypothèse conservatrice : la valeur
   des coproduits est ignorée) et sans coût de découpe (hypothèse optimiste).
B  Viande cultivée : modèle ascendant « à la Humbird » par kg de masse cellulaire humide,
   calibré pour reproduire Humbird 2021 (37 $/kg fed-batch, 51 $/kg perfusion), avec
   trois scénarios (prudent / intermédiaire / optimiste), une analyse de sensibilité
   « tornade » et un tirage Monte-Carlo illustratif.
C  Substituts : uniquement des coûts d'INGRÉDIENT protéique (e-SCP modélisée, prix de marché
   d'isolats de soja) : pas de coût de produit fini disponible dans les sources lues.

Exécution : python3 research/agents/E/models/pathway_cost_model.py
Écrit aussi research/agents/E/models/results.md et results.json.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Change (moyennes annuelles BCE) — Q-E-0061…0064
# ---------------------------------------------------------------------------
USD_PER_EUR = {2017: 1.1297, 2020: 1.1422, 2022: 1.0530}   # Q-E-0061, Q-E-0062, Q-E-0063
BRL_PER_EUR = {2025: 6.3072}                                # Q-E-0064


def eur_to_usd(x_eur: float, year: int) -> float:
    return x_eur * USD_PER_EUR[year]


# ---------------------------------------------------------------------------
# Conversions de base (voie A)
# ---------------------------------------------------------------------------
CONV_A = {
    # Rendement carcasse / poids vif (hypothèse du modèle van Horne) — Q-E-0049
    "carcass_yield": {"value": 0.70, "ref": "Q-E-0049"},
    # Viande désossée / poids vif : 0,431 (Ross 308 mâle 3,0 kg, déclaration d'entreprise, Q-N-0014)
    # à 0,47 (revue, Q-N-0035)
    "boneless_yield": {"low": 0.431, "high": 0.47, "ref": "Q-N-0014 ; Q-N-0035"},
    # Protéine de la viande fraîche : 18-25 % (hypothèse ACV Sinke 2023) — Q-E-0052
    "protein_meat": {"low": 0.18, "mid": 0.215, "high": 0.25, "ref": "Q-E-0052"},
    # Coût d'abattage UE 2017 : 21-38 c€/kg carcasse (tableau 3.3 van Horne) — Q-E-0027 (notes)
    "slaughter_eur_per_kg_carcass": {"low": 0.21, "high": 0.38, "ref": "Q-E-0027"},
}

# Coûts d'élevage par kg de poids vif (monnaie et année d'origine)
FARM_COSTS = [
    # (étiquette, valeur, monnaie, année, réf., nature)
    ("UE moyenne, standard (2017)", 0.825, "EUR", 2017, "Q-E-0022", "published_estimate"),
    ("Pologne, standard (2017)", 0.786, "EUR", 2017, "Q-E-0026", "published_estimate"),
    ("Brésil, standard (2017)", 0.632, "EUR", 2017, "Q-E-0023", "published_estimate"),
    ("États-Unis, standard (2017)", 0.645, "EUR", 2017, "Q-E-0024", "published_estimate"),
    ("France, standard (2022)", 1.264, "EUR", 2022, "Q-E-0029", "statistical"),
    ("France, Label Rouge (2022)", 2.485, "EUR", 2022, "Q-E-0030", "statistical"),
    ("France, biologique (2022)", 3.366, "EUR", 2022, "Q-E-0031", "statistical"),
]


def pathway_a_table():
    """Coût par kg de viande désossée et par kg de protéine (plages bas-haut)."""
    rows = []
    cy = CONV_A["carcass_yield"]["value"]
    s_lo, s_hi = (CONV_A["slaughter_eur_per_kg_carcass"][k] for k in ("low", "high"))
    b_lo, b_hi = (CONV_A["boneless_yield"][k] for k in ("low", "high"))
    p_lo, p_hi = (CONV_A["protein_meat"][k] for k in ("low", "high"))
    for label, v, cur, yr, ref, nature in FARM_COSTS:
        # coût à la sortie d'abattoir par kg de PV : élevage + abattage ramené au PV
        lw_lo = v + s_lo * cy
        lw_hi = v + s_hi * cy
        meat_lo = lw_lo / b_hi          # meilleur cas : abattage bas, rendement haut
        meat_hi = lw_hi / b_lo
        prot_lo = meat_lo / p_hi
        prot_hi = meat_hi / p_lo
        rows.append({
            "label": label, "farm_cost_per_kg_lw": v, "currency": f"{cur}{yr}", "ref": ref,
            "nature_of_input": nature,
            "meat_cost_range": (round(meat_lo, 2), round(meat_hi, 2)),
            "protein_cost_range": (round(prot_lo, 1), round(prot_hi, 1)),
            "protein_cost_range_usd": (round(eur_to_usd(prot_lo, yr), 1), round(eur_to_usd(prot_hi, yr), 1)),
        })
    return rows


# ---------------------------------------------------------------------------
# Voie B : modèle ascendant par kg de masse cellulaire humide (USD ~2018-2020)
# ---------------------------------------------------------------------------
# Chaque paramètre : valeurs prudent / intermédiaire / optimiste + référence.
B_PARAMS = {
    "tci_usd_per_kg_yr": {
        "prudent": 663e6 / 6.9e6,       # Humbird perfusion : 663 M$ / 6,9 kt/an  (Q-E-0004)
        "intermediate": 328e6 / 6.8e6,  # Humbird fed-batch : 328 M$ / 6,8 kt/an  (Q-E-0003)
        "optimistic": 150e6 / 11.8e6,   # Believer Meats : 150 M$ / ~11,8 kt/an annoncés (Q-E-0048, Q-E-0047 ; company_claim, capacité jamais démontrée)
        "unit": "USD par (kg/an) de capacité", "ref": "Q-E-0004 ; Q-E-0003 ; Q-E-0048/Q-E-0047",
    },
    "capital_recovery_factor": {
        "prudent": 48e6 / 328e6,        # charge annuelle implicite de Humbird : 48 M$/an pour 328 M$ (≈14,6 %/an) — dérivé de Q-E-0003
        "intermediate": 0.102,          # model_assumption : WACC 8 %, 20 ans (annuité = 0,1019)
        "optimistic": 1 / 30,           # model_assumption inspirée du délai « social » de 30 ans de CE Delft (SRC-E-0014)
        "unit": "fraction du TCI par an", "ref": "dérivé Q-E-0003 ; model_assumption ; model_assumption (CE Delft)",
    },
    "fixed_om_fraction": {
        "prudent": 0.09, "intermediate": 0.09, "optimistic": 0.09,   # Humbird : 4 % maintenance + 5 % assurance (EV-E-0001, section 2.5)
        "unit": "fraction du TCI par an", "ref": "SRC-E-0001 (section 2.5)",
    },
    "utilization": {
        "prudent": 0.75, "intermediate": 0.90, "optimistic": 0.95,   # model_assumption (Humbird : ~91 % du temps en régime permanent en perfusion)
        "unit": "fraction de la capacité nominale", "ref": "model_assumption",
    },
    "medium_usd_per_kg": {
        "prudent": 22.0,                # Humbird : acides aminés 19 + facteurs de croissance 3 $/kg à 100 kt/an mondial (Q-E-0005 ; EV-E-0004)
        "intermediate": 7.0,            # Humbird avec hydrolysat à 2 $/kg : 37 → 22 $/kg, soit milieu ≈ 22 − 15 = 7 (dérivé de Q-E-0001, Q-E-0006)
        "optimistic": 4.0,              # model_assumption : hydrolysat + facteurs de croissance gratuits (comme Risner sc. 4 / CE Delft sc. 4-8)
        "unit": "USD/kg masse cellulaire humide", "ref": "Q-E-0005 ; dérivé Q-E-0001/Q-E-0006 ; model_assumption",
    },
    "other_opex_usd_per_kg": {
        "prudent": 8.0,                 # Humbird perfusion : consommables 5 + utilités 1 + main-d'œuvre 2 (tableau 2, SRC-E-0001)
        "intermediate": 3.0,            # Humbird fed-batch : 1 + 1 + 1 (tableau 2)
        "optimistic": 2.0,              # model_assumption
        "unit": "USD/kg masse cellulaire humide", "ref": "SRC-E-0001 tableau 2 ; model_assumption",
    },
}

# Protéine de la masse cellulaire humide : 30 % de matière sèche × 70 % de protéines (Q-E-0050, Q-E-0051)
PROTEIN_WET_CELLS = 0.30 * 0.70
SCENARIOS = ("prudent", "intermediate", "optimistic")


def b_cost(p: dict) -> dict:
    """Coût par kg de masse cellulaire humide, décomposé."""
    capex = p["tci_usd_per_kg_yr"] * (p["capital_recovery_factor"] + p["fixed_om_fraction"]) / p["utilization"]
    medium = p["medium_usd_per_kg"]
    other = p["other_opex_usd_per_kg"]  # OPEX variables par kg produit : non affectés par le taux d'utilisation
    total = capex + medium + other
    return {"capital_and_fixed": capex, "medium": medium, "other_opex": other, "total": total,
            "per_kg_protein": total / PROTEIN_WET_CELLS}


def scenario_params(name: str) -> dict:
    return {k: v[name] for k, v in B_PARAMS.items()}


def calibration_check():
    """Reproduit Humbird 2021, tableau 2 (utilisation 100 %, CRF implicite 14,6 %)."""
    crf = 48e6 / 328e6
    fed = b_cost({"tci_usd_per_kg_yr": 328e6 / 6.8e6, "capital_recovery_factor": crf,
                  "fixed_om_fraction": 0.09, "utilization": 1.0,
                  "medium_usd_per_kg": 22.0, "other_opex_usd_per_kg": 3.0})["total"]
    per = b_cost({"tci_usd_per_kg_yr": 663e6 / 6.9e6, "capital_recovery_factor": 97e6 / 663e6,
                  "fixed_om_fraction": 0.09, "utilization": 1.0,
                  "medium_usd_per_kg": 21.0, "other_opex_usd_per_kg": 8.0})["total"]
    return {"fed_batch_model": round(fed, 1), "fed_batch_humbird": 37,
            "perfusion_model": round(per, 1), "perfusion_humbird": 51}


def tornado(base="intermediate"):
    """Variation du coût total quand chaque paramètre passe à sa valeur prudente / optimiste."""
    p0 = scenario_params(base)
    c0 = b_cost(p0)["total"]
    out = []
    for k in B_PARAMS:
        lo = dict(p0, **{k: B_PARAMS[k]["optimistic"]})
        hi = dict(p0, **{k: B_PARAMS[k]["prudent"]})
        clo, chi = b_cost(lo)["total"], b_cost(hi)["total"]
        out.append({"parameter": k, "optimistic_value_cost": round(clo, 1), "prudent_value_cost": round(chi, 1),
                    "swing": round(abs(chi - clo), 1), "ref": B_PARAMS[k]["ref"]})
    out.sort(key=lambda r: -r["swing"])
    return round(c0, 1), out


def monte_carlo(n=20000, seed=42, thresholds_usd_per_kg_protein=()):
    """Tirage triangulaire (min = optimiste, mode = intermédiaire, max = prudent) — ILLUSTRATIF.

    La distribution reflète seulement l'étendue des hypothèses publiées, pas une probabilité
    d'occurrence réelle (paramètres non indépendants en réalité).
    """
    rng = random.Random(seed)
    totals = []
    for _ in range(n):
        p = {}
        for k, v in B_PARAMS.items():
            lo, mode, hi = sorted([v["optimistic"], v["intermediate"], v["prudent"]])
            if hi == lo:
                p[k] = lo
            else:
                p[k] = rng.triangular(lo, hi, v["intermediate"])
        totals.append(b_cost(p)["total"])
    totals.sort()
    q = lambda f: totals[int(f * (n - 1))]
    res = {"p5": round(q(0.05), 1), "p50": round(q(0.50), 1), "p95": round(q(0.95), 1)}
    for label, thr in thresholds_usd_per_kg_protein:
        thr_wet = thr * PROTEIN_WET_CELLS
        res[f"share_below_{label}"] = round(sum(t < thr_wet for t in totals) / n, 3)
    return res


def medium_use_sensitivity():
    """Coût du milieu par kg selon la consommation (L/kg) au prix déclaré de 0,63 $/L (Q-E-0019, company_claim).

    Plancher physique : 1/0,43 ≈ 2,3 L/kg si la biomasse atteint 43 % m/v sans aucun renouvellement
    (Q-C-0004 / Pasitka) ; les volumes de perfusion réels ne sont pas publiés (lacune).
    """
    price = 0.63
    return [(lpk, round(price * lpk, 2)) for lpk in (2.3, 5, 10, 20, 50)]


# ---------------------------------------------------------------------------
# Voie C : coûts d'ingrédients protéiques (pas de produits finis)
# ---------------------------------------------------------------------------
PATHWAY_C = [
    ("e-SCP (H2-oxydantes), meilleurs sites 2028", "5.5-6.1", "EUR/kg protéine", "Q-E-0041", "model_output (COI Solar Foods)"),
    ("e-SCP, Finlande 2028", ">7.3", "EUR/kg protéine", "Q-E-0041 (notes)", "model_output"),
    ("Isolat de soja, prix de marché 2019-2023", "1.8-8.1", "EUR/kg protéine", "Q-E-0065", "prix de marché (pas un coût)"),
    ("Isolat de pois, prix de marché 2020-2023", "3.5-9.3", "EUR/kg protéine", "Q-E-0065 (notes)", "prix de marché (pas un coût)"),
    ("Mycoprotéine (TEA citée par revue, base non précisée)", "3.55", "USD/kg", "Q-E-0066", "model_output, source primaire non identifiée"),
]


# ---------------------------------------------------------------------------
# Émissions par kg de protéine (RQ-X2) — conversions explicites
# ---------------------------------------------------------------------------
def ghg_per_protein():
    rows = []
    p_lo, p_hi = CONV_A["protein_meat"]["low"], CONV_A["protein_meat"]["high"]
    b_lo, b_hi = CONV_A["boneless_yield"]["low"], CONV_A["boneless_yield"]["high"]
    # Mostert 2022 : par kg PV → par kg viande désossée (100 % imputé à la viande) → par kg protéine
    for label, v, ref in [("Poulet conventionnel NL, avec LUC", 3.65, "Q-E-0015"),
                          ("Poulet BLS (croissance lente) NL, avec LUC", 3.55, "Q-E-0016"),
                          ("Poulet conventionnel NL, soja faible LUC", 1.37, "Q-E-0017")]:
        rows.append((label, f"{v} /kg PV", round(v / b_hi / p_hi, 1), round(v / b_lo / p_lo, 1), ref,
                     "100 % imputé à la viande désossée (surestimation)"))
    for label, v, ref in [("Poulet 2030 « ambitieux » (Sinke)", 2.7, "Q-E-0039"),
                          ("Poulet actuel « ambitieux » (Sinke, Agri-footprint)", 6.0, "Q-E-0039 (notes)"),
                          ("Poulet moyenne mondiale 2018 (Poore & Nemecek via Sinke)", 9.0, "Q-E-0039 (notes)")]:
        rows.append((label, f"{v} /kg viande", round(v / p_hi, 1), round(v / p_lo, 1), ref, "base kg de viande"))
    for label, v, ref in [("Viande cultivée 2030, renouvelable total (Sinke)", 2.8, "Q-E-0037"),
                          ("Viande cultivée 2030, renouvelable sur site (Sinke)", 4.0, "Q-E-0037 (notes)"),
                          ("Viande cultivée 2030, mix mondial (Sinke)", 14.3, "Q-E-0038")]:
        rows.append((label, f"{v} /kg viande", round(v / p_hi, 1), round(v / p_lo, 1), ref, "base kg de viande"))
    rows.append(("Viande cultivée, Risner 2025 (tous scénarios)", "12-1508 /kg", round(12 / PROTEIN_WET_CELLS),
                 round(1508 / PROTEIN_WET_CELLS), "Q-E-0013", "protéine = 21 % (Q-E-0050/0051)"))
    return rows


# ---------------------------------------------------------------------------
def fmt_range(r):
    return f"{r[0]}–{r[1]}"


def main():
    out = {}
    lines = ["# Résultats du modèle économique (agent E) — sorties de modèle, pas des coûts démontrés", ""]

    # A
    a = pathway_a_table()
    out["pathway_A"] = a
    lines += ["## Voie A — coût par kg de viande désossée et par kg de protéine", "",
              "| Système | Coût élevage /kg PV | Monnaie | Réf. | Coût /kg viande désossée | Coût /kg protéine | idem en USD (même année) |",
              "|---|---|---|---|---|---|---|"]
    for r in a:
        lines.append(f"| {r['label']} | {r['farm_cost_per_kg_lw']} | {r['currency']} | {r['ref']} | "
                     f"{fmt_range(r['meat_cost_range'])} | {fmt_range(r['protein_cost_range'])} | {fmt_range(r['protein_cost_range_usd'])} |")
    lines += ["", "Hypothèses : abattage 0,21-0,38 €/kg carcasse (UE 2017, Q-E-0027) appliqué à tous les systèmes ; rendement carcasse 0,70 (Q-E-0049) ; "
              "viande désossée 43,1-47 % du PV (Q-N-0014, Q-N-0035 ; probablement surestimé pour Label Rouge/bio) ; protéine 18-25 % (Q-E-0052) ; "
              "100 % des coûts imputés à la viande ; découpe, emballage, distribution exclus.", ""]

    # B
    cal = calibration_check()
    out["calibration"] = cal
    lines += ["## Voie B — modèle ascendant par kg de masse cellulaire humide (USD ≈ 2018-2020)", "",
              f"Contrôle de calibration (Humbird 2021, tableau 2) : fed-batch modèle {cal['fed_batch_model']} $/kg vs {cal['fed_batch_humbird']} ; "
              f"perfusion modèle {cal['perfusion_model']} $/kg vs {cal['perfusion_humbird']}.", "",
              "| Scénario | Capital + frais fixes | Milieu | Autres OPEX | Total $/kg humide | Total $/kg protéine | Total €2020/kg protéine |",
              "|---|---|---|---|---|---|---|"]
    out["pathway_B"] = {}
    for s in SCENARIOS:
        c = b_cost(scenario_params(s))
        out["pathway_B"][s] = {k: round(v, 2) for k, v in c.items()}
        lines.append(f"| {s} | {c['capital_and_fixed']:.1f} | {c['medium']:.1f} | {c['other_opex']:.1f} | {c['total']:.1f} | "
                     f"{c['per_kg_protein']:.0f} | {c['per_kg_protein'] / USD_PER_EUR[2020]:.0f} |")
    lines += ["", "Paramètres et références :", "", "| Paramètre | Prudent | Intermédiaire | Optimiste | Unité | Référence |", "|---|---|---|---|---|---|"]
    for k, v in B_PARAMS.items():
        lines.append(f"| {k} | {v['prudent']:.3g} | {v['intermediate']:.3g} | {v['optimistic']:.3g} | {v['unit']} | {v['ref']} |")

    base, tor = tornado()
    out["tornado"] = {"base_intermediate": base, "rows": tor}
    lines += ["", f"### Sensibilité (tornade) autour du scénario intermédiaire ({base} $/kg humide)", "",
              "| Paramètre | Coût si valeur optimiste | Coût si valeur prudente | Amplitude | Réf. |", "|---|---|---|---|---|"]
    for r in tor:
        lines.append(f"| {r['parameter']} | {r['optimistic_value_cost']} | {r['prudent_value_cost']} | {r['swing']} | {r['ref']} |")

    # Seuils de comparaison : coût protéine voie A en USD de l'année d'origine (pas d'inflation)
    eu17 = next(r for r in a if r["label"].startswith("UE moyenne"))
    lr22 = next(r for r in a if "Label Rouge" in r["label"])
    bio22 = next(r for r in a if "biologique" in r["label"])
    thr = [("EU_standard_2017_high", eu17["protein_cost_range_usd"][1]),
           ("FR_label_rouge_2022_high", lr22["protein_cost_range_usd"][1]),
           ("FR_bio_2022_high", bio22["protein_cost_range_usd"][1])]
    mc = monte_carlo(thresholds_usd_per_kg_protein=thr)
    out["monte_carlo"] = mc
    lines += ["", "### Monte-Carlo illustratif (20 000 tirages triangulaires, graine 42)", "",
              f"P5 / P50 / P95 = {mc['p5']} / {mc['p50']} / {mc['p95']} $/kg humide.", "",
              "Part des tirages dont le coût par kg de protéine est inférieur au haut de la plage de la voie A "
              "(coût de la viande désossée, même base protéine, sans correction d'inflation) :", ""]
    for label, t in thr:
        lines.append(f"- {label} ({t} $/kg protéine) : {mc['share_below_' + label]:.1%}")
    lines += ["", "Avertissement : ces parts mesurent la position des hypothèses publiées, pas une probabilité réelle ; "
              "le coût de la masse cellulaire humide exclut la mise en forme, l'emballage, la distribution et la marge.", ""]

    # Seuils de parité : coût maximal admissible de la masse cellulaire humide
    opt = scenario_params("optimistic")
    floor_no_capex = opt["medium_usd_per_kg"] + opt["other_opex_usd_per_kg"]
    parity = [(label, t, round(t * PROTEIN_WET_CELLS, 2)) for label, t in thr]
    out["parity_thresholds"] = {"rows": parity, "optimistic_floor_without_capex": floor_no_capex}
    lines += ["### Seuils de parité (base protéine)", "",
              "| Comparateur (haut de plage voie A) | $/kg protéine | Coût max. admissible de la masse humide $/kg |", "|---|---|---|"]
    lines += [f"| {l} | {t} | {w} |" for l, t, w in parity]
    lines += ["", f"Plancher du scénario optimiste sans aucun coût en capital (milieu + autres OPEX) : {floor_no_capex} $/kg humide.", ""]

    ms = medium_use_sensitivity()
    out["medium_use_sensitivity"] = ms
    lines += ["### Sensibilité à la consommation de milieu au prix déclaré de 0,63 $/L (Q-E-0019, company_claim)", "",
              "| L de milieu par kg humide | Coût du milieu $/kg |", "|---|---|"]
    lines += [f"| {l} | {c} |" for l, c in ms]

    # C
    out["pathway_C"] = PATHWAY_C
    lines += ["", "## Voie C — coûts d'ingrédients protéiques disponibles (pas de produit fini)", "",
              "| Ingrédient | Valeur | Unité | Réf. | Nature |", "|---|---|---|---|---|"]
    lines += [f"| {a_} | {b_} | {c_} | {d_} | {e_} |" for a_, b_, c_, d_, e_ in PATHWAY_C]

    # GES
    g = ghg_per_protein()
    out["ghg_per_kg_protein"] = g
    lines += ["", "## Émissions par kg de protéine (RQ-X2)", "",
              "| Système | Valeur source | kg CO2-eq/kg protéine (bas) | (haut) | Réf. | Conversion |", "|---|---|---|---|---|---|"]
    lines += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |" for r in g]

    (HERE / "results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (HERE / "results.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
