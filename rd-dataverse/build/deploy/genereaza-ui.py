#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genereaza artefactele de interfata pentru aplicatia model-driven.

Produce, din data/tabele.json si data/relatii.json:
  - vizualizari (SavedQuery) cu fetchXml si layoutXml
  - formulare principale (SystemForm) cu FormXml, organizate pe file
  - harta de site (SiteMap XML) pentru aplicatia model-driven
  - definitiile celor 13 roluri de securitate, cu adancimea privilegiilor

Iesire: build/deploy/payloaduri-ui/
"""
import json, uuid, collections, re
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent / "payloaduri-ui"
LCID = 1048

CLASSID = {
    "Text": "{4273EDBD-AC1D-40d3-9FB2-095C621B552D}",
    "Text Area": "{E0DECE4B-6FC8-4a8f-A065-082708572369}",
    "Whole Number": "{C3EFE0C3-0EC6-42be-8349-CBD9079DFD8E}",
    "Decimal": "{C3EFE0C3-0EC6-42be-8349-CBD9079DFD8E}",
    "Currency": "{533B9E00-756B-4312-95A0-DC888637AC78}",
    "Choice": "{3EF39988-22BB-4f0b-BBBE-64B5A3748AEE}",
    "Yes/No": "{67FAC785-CD58-4f9f-ABB3-4B7DDC6ED5ED}",
    "Date Only": "{5B773807-9FB2-42db-97C3-7A91EFF8ADFF}",
    "Date and Time": "{5B773807-9FB2-42db-97C3-7A91EFF8ADFF}",
    "Lookup": "{270BD3DB-D9AF-4782-9025-509E298DEC0A}",
    "Autonumber": "{4273EDBD-AC1D-40d3-9FB2-095C621B552D}",
    "Calculated": "{4273EDBD-AC1D-40d3-9FB2-095C621B552D}",
    "Rollup": "{C3EFE0C3-0EC6-42be-8349-CBD9079DFD8E}",
    "Image": "{4273EDBD-AC1D-40d3-9FB2-095C621B552D}",
}


def gid():
    return "{" + str(uuid.uuid4()) + "}"


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def baza(tip):
    return tip.split(" (")[0]


# ---------------------------------------------------------------- FILE PE TABELA
# Gruparea coloanelor pe file, dupa rolul lor semantic in model.
GRUPE = [
    ("Identificare", ["name", "cod", "numar", "denumire", "titlu", "proiect", "client",
                      "tip", "categorie", "faza", "ordine"]),
    ("Stare si termene", ["status", "stare", "data", "termen", "zile", "durata",
                          "start", "final", "perioada"]),
    ("Responsabili", ["responsabil", "tehnolog", "manager", "kam", "aprobator", "autor",
                      "proprietar", "decident", "verificator", "operator", "persoana",
                      "evaluator", "solicitant", "masuratde", "coaprobator"]),
    ("Valori si masuratori", ["cantitate", "gramaj", "greutate", "valoare", "randament",
                              "rebut", "viteza", "temperatura", "timp", "procent", "medie",
                              "minim", "maxim", "abatere", "scor", "nivel", "impact",
                              "probabilitate", "rpn", "cp", "sigma", "n"]),
    ("Cost", ["cost", "pret", "marja", "buget", "expunere", "tarif", "regie"]),
    ("Detalii", ["descriere", "observatii", "motiv", "comentariu", "conditii", "actiune",
                 "context", "concluzie", "recomandare", "detalii", "cauza", "plan"]),
]


def fila_pentru(nume_logic):
    n = nume_logic.replace("rd_", "").lower()
    for eticheta, chei in GRUPE:
        for k in chei:
            if n.startswith(k) or n == k:
                return eticheta
    return "Detalii"


def formular(t):
    """Genereaza FormXml pentru formularul principal al unei tabele."""
    coloane = [c for c in t["coloane"] if baza(c["tip"]) != "Image"]
    pe_fila = collections.OrderedDict()
    for c in coloane:
        pe_fila.setdefault(fila_pentru(c["nume_logic"]), []).append(c)

    # antetul: maximum 5 coloane, cele mai importante
    prioritare = ["status", "proiect", "responsabil", "tehnolog", "termen", "scor", "nivel"]
    antet = []
    for p in prioritare:
        for c in coloane:
            if len(antet) < 4 and p in c["nume_logic"] and c not in antet:
                antet.append(c)
                break

    x = ['<form>', '  <tabs>']
    x.append(f'    <tab name="tab_antet" id="{gid()}" IsUserDefined="0" '
             f'showlabel="false" expanded="true">')
    x.append('      <labels><label description="Antet" languagecode="%d"/></labels>' % LCID)
    x.append('      <columns><column width="100%"><sections>')
    x.append(f'        <section name="sec_antet" id="{gid()}" showlabel="false" '
             f'columns="4" labelwidth="115">')
    x.append('          <labels><label description="Antet" languagecode="%d"/></labels>' % LCID)
    x.append('          <rows><row>')
    for c in antet:
        x.append(f'            <cell id="{gid()}"><labels><label '
                 f'description="{esc(c["nume"])}" languagecode="{LCID}"/></labels>'
                 f'<control id="{c["nume_logic"]}" classid="'
                 f'{CLASSID.get(baza(c["tip"]), CLASSID["Text"])}" '
                 f'datafieldname="{c["nume_logic"]}" disabled="false"/></cell>')
    x.append('          </row></rows>')
    x.append('        </section>')
    x.append('      </sections></column></columns>')
    x.append('    </tab>')

    for eticheta, cols in pe_fila.items():
        x.append(f'    <tab name="tab_{re.sub(r"[^a-z]", "", eticheta.lower())}" '
                 f'id="{gid()}" IsUserDefined="0" expanded="true">')
        x.append(f'      <labels><label description="{esc(eticheta)}" '
                 f'languagecode="{LCID}"/></labels>')
        x.append('      <columns><column width="100%"><sections>')
        x.append(f'        <section name="sec_{re.sub(r"[^a-z]", "", eticheta.lower())}" '
                 f'id="{gid()}" showlabel="true" columns="2" labelwidth="150">')
        x.append(f'          <labels><label description="{esc(eticheta)}" '
                 f'languagecode="{LCID}"/></labels>')
        x.append('          <rows>')
        for c in cols:
            x.append('            <row>')
            x.append(f'              <cell id="{gid()}"><labels><label '
                     f'description="{esc(c["nume"])}" languagecode="{LCID}"/></labels>'
                     f'<control id="{c["nume_logic"]}" classid="'
                     f'{CLASSID.get(baza(c["tip"]), CLASSID["Text"])}" '
                     f'datafieldname="{c["nume_logic"]}" '
                     f'disabled="{"true" if c.get("observatii") and "Scris de" in (c["observatii"] or "") else "false"}"/></cell>')
            x.append('            </row>')
        x.append('          </rows>')
        x.append('        </section>')
        x.append('      </sections></column></columns>')
        x.append('    </tab>')

    x.append('  </tabs>')
    x.append('</form>')
    return "\n".join(x), len(pe_fila) + 1


def vizualizari(t, rel_copii):
    """Genereaza vizualizarile standard pentru o tabela."""
    lg = t["nume_logic"]
    prim = t["coloana_primara"]
    # coloanele afisate: primara + primele coloane semnificative
    candidate = [c for c in t["coloane"]
                 if c["nume_logic"] != prim
                 and baza(c["tip"]) in ("Text", "Choice", "Date Only", "Lookup",
                                        "Whole Number", "Decimal", "Yes/No", "Autonumber")]
    afisate = [prim] + [c["nume_logic"] for c in candidate[:7]]

    def fetch(filtru="", ordine=None):
        f = [f'<fetch version="1.0" mapping="logical" no-lock="true">',
             f'  <entity name="{lg}">']
        for a in afisate:
            f.append(f'    <attribute name="{a}"/>')
        if ordine:
            f.append(f'    <order attribute="{ordine}" descending="true"/>')
        if filtru:
            f.append(filtru)
        f.append('  </entity>')
        f.append('</fetch>')
        return "\n".join(f)

    def layout():
        latimi = [200] + [125] * (len(afisate) - 1)
        c = [f'<grid name="resultset" object="1" jump="{prim}" select="1" '
             f'icon="1" preview="1">',
             f'  <row name="result" id="{lg}id">']
        for a, w in zip(afisate, latimi):
            c.append(f'    <cell name="{a}" width="{w}"/>')
        c.append('  </row>')
        c.append('</grid>')
        return "\n".join(c)

    v = [{"nume": f"Toate: {t['nume']}", "querytype": 0, "isdefault": True,
          "fetchxml": fetch(), "layoutxml": layout()}]

    # vizualizare filtrata pe status activ, unde exista
    st = next((c for c in t["coloane"] if c["nume_logic"].startswith("rd_status")), None)
    if st:
        v.append({"nume": f"Active: {t['nume']}", "querytype": 0, "isdefault": False,
                  "fetchxml": fetch('    <filter type="and">\n'
                                    '      <condition attribute="statecode" operator="eq" value="0"/>\n'
                                    '    </filter>'),
                  "layoutxml": layout()})

    # vizualizare "ale mele", unde exista responsabil
    resp = next((c for c in t["coloane"]
                 if c["nume_logic"] in ("rd_responsabil", "rd_tehnolog", "rd_proprietar")), None)
    if resp:
        v.append({"nume": f"Ale mele: {t['nume']}", "querytype": 0, "isdefault": False,
                  "fetchxml": fetch(f'    <filter type="and">\n'
                                    f'      <condition attribute="{resp["nume_logic"]}" '
                                    f'operator="eq-userid"/>\n    </filter>'),
                  "layoutxml": layout()})

    # vizualizare de cautare rapida
    v.append({"nume": f"Cautare: {t['nume']}", "querytype": 4, "isdefault": False,
              "fetchxml": fetch(), "layoutxml": layout()})
    return v


# ---------------------------------------------------------------- HARTA DE SITE
SITEMAP = [
    ("Lucrul meu", "Home", [
        ("Proiectele mele", "rd_proiect"), ("Livrabilele mele", "rd_livrabil"),
        ("Actiunile mele", "rd_actiune"), ("Gate-uri de evaluat", "rd_gate")]),
    ("Solicitari", "Sales", [
        ("Solicitari", "rd_solicitare")]),
    ("Proiecte", "Service", [
        ("Proiecte", "rd_proiect"), ("Etape", "rd_etapa"), ("Livrabile", "rd_livrabil"),
        ("Gate-uri", "rd_gate"), ("Riscuri", "rd_risc"), ("Probleme", "rd_problema"),
        ("Blocaje", "rd_blocaj"), ("Decizii", "rd_decizie"), ("Actiuni", "rd_actiune")]),
    ("Executie", "Marketing", [
        ("Fise de testare", "rd_fisatestare"), ("Trialuri", "rd_trial"),
        ("Evaluari senzoriale", "rd_evaluaresenzoriala"), ("Retete", "rd_reteta"),
        ("Versiuni de reteta", "rd_versiunereteta"), ("Antecalcule", "rd_antecalcul"),
        ("Referinte", "rd_referinta")]),
    ("Materii prime", "Settings", [
        ("MP de proiect", "rd_mpproiect"), ("Catalog MP", "rd_materieprima"),
        ("Furnizori", "rd_furnizor"), ("Iteratii de furnizor", "rd_iteratiefurnizor"),
        ("Istoric lead time", "rd_leadtimeistoric"), ("Cereri de mostra", "rd_ceremostra")]),
    ("Industrializare", "Service", [
        ("Implementari IPN", "rd_implementare"), ("Productii 0", "rd_productie0"),
        ("Stabilizari", "rd_stabilizare"), ("Capabilitate de proces", "rd_capabilitateproces"),
        ("Revizuiri", "rd_revizuire")]),
    ("Specificatii", "Settings", [
        ("Specificatii tehnice", "rd_specificatie"), ("SDP", "rd_sdp"),
        ("Etichete", "rd_eticheta")]),
    ("Cunoastere", "Marketing", [
        ("Lectii invatate", "rd_lectie"), ("Utilizari de lectii", "rd_utilizarelectie"),
        ("Recomandari", "rd_recomandarelectie")]),
    ("Configurare", "Settings", [
        ("Sabloane de livrabile", "rd_sablonlivrabil"), ("Sabloane de etape", "rd_sablonetapa"),
        ("Sabloane de gate", "rd_sablongate"), ("Criterii de gate", "rd_criteriugate"),
        ("Linii de productie", "rd_linie"), ("Clienti", "rd_client"),
        ("Profiluri de tehnolog", "rd_profiltehnolog"),
        ("Criterii senzoriale", "rd_criteriusenzorial"), ("Defecte", "rd_defect"),
        ("Motive", "rd_motiv"), ("Tipuri de documente", "rd_tipdocument"),
        ("Alergeni", "rd_alergen"), ("Indicatori", "rd_indicator"),
        ("Log de erori", "rd_logeroare")]),
]


def sitemap():
    x = ['<SiteMap>']
    for arie, icon, grupuri in SITEMAP:
        aid = re.sub(r"[^A-Za-z]", "", arie)
        x.append(f'  <Area Id="area_{aid}" ResourceId="{icon}" ShowGroups="true">')
        x.append(f'    <Titles><Title LCID="{LCID}" Title="{esc(arie)}"/></Titles>')
        x.append(f'    <Group Id="grp_{aid}">')
        x.append(f'      <Titles><Title LCID="{LCID}" Title="{esc(arie)}"/></Titles>')
        for titlu, ent in grupuri:
            sid = re.sub(r"[^A-Za-z]", "", titlu)[:20]
            x.append(f'        <SubArea Id="sa_{sid}_{ent}" Entity="{ent}">')
            x.append(f'          <Titles><Title LCID="{LCID}" Title="{esc(titlu)}"/></Titles>')
            x.append('        </SubArea>')
        x.append('    </Group>')
        x.append('  </Area>')
    x.append('</SiteMap>')
    return "\n".join(x)


# ---------------------------------------------------------------- ROLURI
# Adancime: 0 fara drept, 1 User, 2 Business Unit, 4 Organizatie
# Ordinea privilegiilor: Create, Read, Write, Delete, Append, AppendTo, Assign, Share
ROLURI = {
    "RD Head":          {"implicit": [4, 4, 4, 4, 4, 4, 4, 4]},
    "RD Administrator": {"implicit": [4, 4, 4, 4, 4, 4, 4, 4]},
    "RD Manager":       {"implicit": [2, 2, 2, 0, 2, 2, 2, 2],
                         "exceptii": {"rd_blocaj": [2, 2, 2, 2, 2, 2, 2, 2]}},
    "RD Tehnolog":      {"implicit": [2, 2, 2, 0, 2, 2, 0, 2],
                         "exceptii": {"rd_solicitare": [0, 2, 0, 0, 0, 2, 0, 0],
                                      "rd_sablonlivrabil": [0, 2, 0, 0, 0, 2, 0, 0],
                                      "rd_sablonetapa": [0, 2, 0, 0, 0, 2, 0, 0],
                                      "rd_sablongate": [0, 2, 0, 0, 0, 2, 0, 0]}},
    "RD Suport":        {"implicit": [2, 2, 2, 0, 2, 2, 0, 0],
                         "exceptii": {"rd_antecalcul": [0, 0, 0, 0, 0, 0, 0, 0],
                                      "rd_linieantecalcul": [0, 0, 0, 0, 0, 0, 0, 0]}},
    "KAM":              {"implicit": [0, 2, 0, 0, 0, 2, 0, 0],
                         "exceptii": {"rd_solicitare": [2, 2, 1, 0, 2, 2, 0, 0],
                                      "rd_referinta": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_ceremostra": [2, 2, 1, 0, 2, 2, 0, 0],
                                      "rd_antecalcul": [0, 0, 0, 0, 0, 0, 0, 0],
                                      "rd_linieantecalcul": [0, 0, 0, 0, 0, 0, 0, 0],
                                      "rd_liniereteta": [0, 0, 0, 0, 0, 0, 0, 0],
                                      "rd_versiunereteta": [0, 0, 0, 0, 0, 0, 0, 0]}},
    "Comercial Manager": {"implicit": [0, 2, 0, 0, 0, 2, 0, 0],
                          "exceptii": {"rd_proiect": [0, 2, 2, 0, 0, 2, 0, 0],
                                       "rd_client": [2, 2, 2, 0, 2, 2, 0, 0]}},
    "Achizitii":        {"implicit": [0, 2, 0, 0, 0, 2, 0, 0],
                         "exceptii": {"rd_mpproiect": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_iteratiefurnizor": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_materieprima": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_furnizor": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_leadtimeistoric": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_ceremostra": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_blocaj": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_actiune": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_antecalcul": [0, 0, 0, 0, 0, 0, 0, 0]}},
    "Calitate":         {"implicit": [0, 2, 0, 0, 0, 2, 0, 0],
                         "exceptii": {"rd_specificatie": [2, 2, 2, 2, 2, 2, 0, 0],
                                      "rd_sdp": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_materieprima": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_alergen": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_defect": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_evaluaresenzoriala": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_problema": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_risc": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_actiune": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_inregistrareprod0": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_antecalcul": [0, 0, 0, 0, 0, 0, 0, 0]}},
    "Planificare":      {"implicit": [0, 2, 0, 0, 0, 2, 0, 0],
                         "exceptii": {"rd_blocaj": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_antecalcul": [0, 0, 0, 0, 0, 0, 0, 0]}},
    "Productie":        {"implicit": [0, 2, 0, 0, 0, 2, 0, 0],
                         "exceptii": {"rd_productie0": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_inregistrareprod0": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_lotstabilizare": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_masuratoare": [2, 2, 1, 0, 2, 2, 0, 0],
                                      "rd_actiune": [2, 2, 2, 0, 2, 2, 0, 0],
                                      "rd_antecalcul": [0, 0, 0, 0, 0, 0, 0, 0]}},
    "Cititor companie": {"implicit": [0, 0, 0, 0, 0, 0, 0, 0],
                         "exceptii": {"rd_proiect": [0, 2, 0, 0, 0, 2, 0, 0],
                                      "rd_client": [0, 2, 0, 0, 0, 2, 0, 0],
                                      "rd_linie": [0, 2, 0, 0, 0, 2, 0, 0]}},
    "RD Auditor":       {"implicit": [0, 4, 0, 0, 0, 4, 0, 0]},
}

PRIVILEGII = ["Create", "Read", "Write", "Delete", "Append", "AppendTo", "Assign", "Share"]


def roluri(tabele):
    out = []
    for nume, cfg in ROLURI.items():
        priv = {}
        for t in tabele:
            lg = t["nume_logic"]
            adancimi = cfg.get("exceptii", {}).get(lg, cfg["implicit"])
            d = {p: a for p, a in zip(PRIVILEGII, adancimi) if a > 0}
            if d:
                priv[lg] = d
        out.append({"nume": nume, "privilegii": priv,
                    "numar_tabele_cu_acces": len(priv)})
    return out


# ---------------------------------------------------------------- MAIN
def main():
    OUT.mkdir(exist_ok=True)
    T = json.loads((BASE / "data" / "tabele.json").read_text())
    R = json.loads((BASE / "data" / "relatii.json").read_text())
    tabele = T["tabele"]
    rel_copii = collections.defaultdict(list)
    for r in R["arbore_principal"]:
        if r.get("tip") == "parental":
            rel_copii[r["parinte"]].append(r["copil"])

    # formulare: pentru tabelele care se editeaza direct
    forms = []
    for t in tabele:
        if t["categorie"] == "Tehnic":
            continue
        xml, nrfile = formular(t)
        forms.append({"entitate": t["nume_logic"], "nume": f"Formular principal - {t['nume']}",
                      "type": 2, "formxml": xml, "numar_file": nrfile,
                      "numar_coloane": len(t["coloane"])})

    # vizualizari
    views = []
    for t in tabele:
        for v in vizualizari(t, rel_copii):
            views.append({"entitate": t["nume_logic"], **v})

    (OUT / "formulare.json").write_text(json.dumps(forms, ensure_ascii=False, indent=1))
    (OUT / "vizualizari.json").write_text(json.dumps(views, ensure_ascii=False, indent=1))
    (OUT / "sitemap.xml").write_text(sitemap())
    rl = roluri(tabele)
    (OUT / "roluri.json").write_text(json.dumps(rl, ensure_ascii=False, indent=1))

    print("ARTEFACTE DE INTERFATA GENERATE")
    print(f"  formulare              {len(forms):5}   ({sum(f['numar_file'] for f in forms)} file in total)")
    print(f"  vizualizari            {len(views):5}")
    print(f"  harta de site            1     ({len(SITEMAP)} arii, "
          f"{sum(len(g[2]) for g in SITEMAP)} subarii)")
    print(f"  roluri de securitate   {len(rl):5}   "
          f"({sum(sum(len(p) for p in r['privilegii'].values()) for r in rl)} privilegii)")
    print(f"\nIesire: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
