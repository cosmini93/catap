#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genereaza fisierele CSV de import pentru Dataverse din artefactele din data/.

Rulare:  python3 build/genereaza-import.py
Iesire:  build/import/*.csv

Antetele CSV folosesc numele afisate ale coloanelor, asa cum le asteapta expertul de
import Dataverse. Separatorul este virgula, codificarea UTF-8 fara diacritice.
Fisierele cu sufixul _SABLON se completeaza manual cu datele reale ale companiei.
"""
import csv, json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
OUT = os.path.join(BASE, "build", "import")


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def scrie(fisier, antet, randuri):
    cale = os.path.join(OUT, fisier)
    with open(cale, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(antet)
        w.writerows(randuri)
    print("  %-42s %3d randuri" % (fisier, len(randuri)))


def da_nu(v):
    return "Da" if v else "Nu"


def main():
    os.makedirs(OUT, exist_ok=True)
    nom = load("nomenclatoare.json")
    liv = load("sablon-livrabile.json")
    eta = load("sablon-etape.json")
    cho = load("choices.json")

    print("Fisiere gata de import:")

    # --- rd_motiv -----------------------------------------------------------
    scrie("nomenclator-motive.csv",
          ["Denumire", "Cod", "Tip motiv", "Necesita comentariu", "Activ"],
          [[m["nume"], m["cod"], m["tip"], da_nu(m["necesita_comentariu"]), "Da"]
           for m in nom["motive"]])

    # --- rd_tipdocument -----------------------------------------------------
    scrie("nomenclator-tipuri-document.csv",
          ["Denumire", "Cod", "Faza", "Extensie asteptata", "Necesita aprobare",
           "Rol aprobator", "Retentie (ani)", "Activ"],
          [[d["nume"], d["cod"], d["faza"], d["extensie"], da_nu(d["necesita_aprobare"]),
            d["rol_aprobator"] or "", d["retentie_ani"] if d["retentie_ani"] else "", "Da"]
           for d in nom["tipuri_document"]])

    # --- rd_criteriusenzorial ----------------------------------------------
    scrie("nomenclator-criterii-senzoriale.csv",
          ["Denumire criteriu", "Cod", "Grupa", "Categorie produs", "Pondere (%)",
           "Eliminatoriu sub", "Ancora scor 1", "Ancora scor 3", "Ancora scor 5", "Activ"],
          [[c["nume"], c["cod"], c["grupa"], c["categorie_produs"], c["pondere"],
            c["eliminatoriu_sub"] or "", c["ancora_1"], c["ancora_3"], c["ancora_5"], "Da"]
           for c in nom["criterii_senzoriale"]])

    # --- rd_defect ----------------------------------------------------------
    scrie("nomenclator-defecte.csv",
          ["Denumire", "Cod", "Grupa", "Severitate implicita", "Cauza probabila",
           "Punct critic HACCP", "Activ"],
          [[d["nume"], d["cod"], d["grupa"], d["severitate"], d["cauza_probabila"],
            da_nu(d.get("punct_critic_haccp") or d.get("declanseaza_neconformitate")), "Da"]
           for d in nom["defecte"]])

    # --- rd_alergen ---------------------------------------------------------
    alerg = next(c for c in cho["choices"] if c["nume"] == "rd_alergen")
    grupa = {"GLU": "Cereale cu gluten", "FRC": "Fructe cu coaja"}
    scrie("nomenclator-alergeni.csv",
          ["Denumire", "Cod", "Denumire legala pe eticheta", "Grupa",
           "Necesita evidentiere pe eticheta", "Prag de declarare"],
          [[v["e"], v["cod"], v["e"], grupa.get(v["cod"], "Altele"), "Da",
            "Fara prag" if v["cod"] != "SO2" else "10 mg/kg sau 10 mg/l"]
           for v in alerg["valori"]])

    # --- rd_sablonetapa -----------------------------------------------------
    scrie("sablon-etape.csv",
          ["Denumire etapa", "Cod etapa", "Ordine", "Tip proiect",
           "Durata standard (zile lucratoare)", "Rol responsabil",
           "Opreste ceasul la blocaj", "Activ"],
          [[e["nume"], e["cod"], e["ordine"],
            ";".join(t for t, d in eta["durate_pe_tip_proiect"].items()
                     if not t.startswith("_") and e["cod"] not in d["etape_eliminate"]),
            e["durata_standard"], e["rol_responsabil"],
            da_nu(e["opreste_ceasul_la_blocaj"]), "Da"]
           for e in eta["etape"]])

    # --- rd_sablonlivrabil --------------------------------------------------
    tipuri = [t for t in liv["excluderi_pe_tip_proiect"] if not t.startswith("_")]
    conditii = {c["cod"]: c["nume"] for c in liv["conditii_aplicabilitate"]}
    randuri = []
    for l in liv["livrabile"]:
        aplicabile = [t for t in tipuri if l["cod"] not in liv["excluderi_pe_tip_proiect"][t]]
        randuri.append([
            l["nume"], l["cod"], ";".join(aplicabile), l["faza"], l["ordine"],
            l["offset"] if l["offset"] is not None else "",
            l.get("offset_implementare", "") or "",
            l["rol_responsabil"], l["rol_aprobator"] or "",
            da_nu(l["obligatoriu"]), da_nu(l["necesita_document"]),
            conditii[l["conditie"]], l["sablon_word"] or "", "Da"])
    scrie("sablon-livrabile.csv",
          ["Denumire", "Cod livrabil", "Tip proiect aplicabil", "Faza", "Ordine",
           "Offset termen (zile)", "Offset fata de implementare", "Rol responsabil",
           "Rol aprobator", "Obligatoriu", "Necesita document",
           "Conditie de aplicabilitate", "Sablon Word", "Activ"], randuri)

    # --- valorile Choice-urilor globale, pentru creare manuala --------------
    randuri = []
    for c in cho["choices"]:
        for v in c["valori"]:
            randuri.append([c["nume"], c["eticheta"], v["v"], v["e"],
                            c.get("referinta", ""), da_nu(c.get("multi_select"))])
    scrie("choices-globale.csv",
          ["Nume logic", "Eticheta set", "Valoare", "Eticheta optiune",
           "Referinta blueprint", "Multi-select"], randuri)

    # --- sabloane de completat manual ---------------------------------------
    print("\nSabloane de completat cu datele reale ale companiei:")
    lin = nom["linii_productie"]
    scrie("nomenclator-linii_SABLON.csv",
          ["Denumire linie", "Cod linie", "Amplasament", "Tip linie", "Echipament principal",
           "Capabilitati", "Alergeni prelucrati pe linie", "Gramaj minim (g)",
           "Gramaj maxim (g)", "Latime banda (mm)", "Viteza nominala (buc/h)",
           "Timp schimb sortiment (min)", "Tarif orar",
           "Pierdere tehnologica implicita (%)", "Prag de supraincarcare", "Activa"],
          [["", "L%02d" % i, "", "", "", "", "", "", "", "", "", 120, "", 3, 6, "Da"]
           for i in range(1, 10)])

    scrie("nomenclator-clienti_SABLON.csv",
          ["Denumire client", "Cod SAP client", "Clasificare", "Data ultimei clasificari",
           "Canal", "Tara", "KAM responsabil", "Activ"], [])

    scrie("nomenclator-furnizori_SABLON.csv",
          ["Denumire", "Cod SAP furnizor", "Tip", "Aprobat Calitate", "Data aprobarii",
           "Certificari", "Expirare certificare", "Persoana de contact", "Email contact"], [])

    scrie("nomenclator-materii-prime_SABLON.csv",
          ["Denumire", "Cod SAP", "Categorie", "Furnizor principal", "Unitate de masura",
           "Pret curent", "Data pretului", "Alergeni continuti", "Alergeni pe urme",
           "Energie (kcal/100g)", "Grasimi (g/100g)", "din care acizi grasi saturati",
           "Glucide (g/100g)", "din care zaharuri", "Fibre (g/100g)", "Proteine (g/100g)",
           "Sare (g/100g)", "Umiditate (%)", "Denumire legala pe eticheta",
           "Ingrediente compuse", "Data ultimei ST furnizor", "Origine", "Status"], [])

    scrie("nomenclator-profiluri-tehnolog_SABLON.csv",
          ["Denumire", "Utilizator", "Rol principal", "Amplasament", "Specializare",
           "Linii pe care lucreaza", "Capacitate maxima proiecte", "Disponibil", "Activ"], [])

    print("\nGata. Fisierele sunt in build/import/")
    print("Ordinea de import este in build/V0-ghid-constructie.md, pasul 5.")


if __name__ == "__main__":
    sys.exit(main())
