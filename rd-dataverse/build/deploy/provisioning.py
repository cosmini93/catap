#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provizionarea modelului de date Dataverse din artefactele blueprintului.

Creeaza, prin Dataverse Web API: seturile de optiuni globale, tabelele, coloanele si
relatiile definite in data/choices.json, data/tabele.json si data/relatii.json.

Este idempotent si reluabil: verifica existenta inainte de creare si retine progresul
in build/deploy/stare.json. O rulare intrerupta se reia de unde a ramas.

UTILIZARE
    python3 provisioning.py --dry-run                 genereaza si valideaza payloadurile
    python3 provisioning.py --dry-run --scrie-payload salveaza payloadurile ca JSON
    python3 provisioning.py --etapa optionsets        ruleaza o singura etapa
    python3 provisioning.py                           ruleaza tot, in ordine

AUTENTIFICARE (variabile de mediu)
    DV_URL           https://organizatie.crm4.dynamics.com
    DV_CLIENT_ID     app registration cu drept de a scrie metadate
    DV_CLIENT_SECRET
    DV_TENANT_ID

NU se poate testa fara un tenant real. Rularea cu --dry-run valideaza structura
payloadurilor si dependentele, nu si acceptarea lor de catre server.
"""
import argparse, json, os, re, sys, time
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data"
STARE = Path(__file__).parent / "stare.json"
PAYLOADURI = Path(__file__).parent / "payloaduri"

PREFIX = "rd"
SOLUTIE = "RDSuitaDigitala"
LCID = 1048  # romana


# ---------------------------------------------------------------- utilitare

def incarca(nume):
    with open(DATA / nume, encoding="utf-8") as f:
        return json.load(f)


def eticheta(text):
    return {"@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [{"@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
                                 "Label": text, "LanguageCode": LCID}]}


def schema(nume_logic):
    """rd_codproiect -> rd_CodProiect. Dataverse cere SchemaName in PascalCase."""
    if "_" not in nume_logic:
        return nume_logic
    p, rest = nume_logic.split("_", 1)
    return p + "_" + rest[:1].upper() + rest[1:]


def parse_interval(valori):
    """'1 - 20000' sau '0 - 100' -> (min, max). Returneaza None daca nu e interval."""
    if not valori:
        return None
    m = re.match(r"^\s*(-?\d+(?:\.\d+)?)\s*-\s*(-?\d+(?:\.\d+)?)", valori)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None


def parse_lungime(tip, implicit=100):
    m = re.search(r"\((\d+)\)", tip)
    return int(m.group(1)) if m else implicit


def choice_referit(valori):
    """'Choice CATEGORIERISC' -> 'rd_categorierisc'"""
    if not valori:
        return None
    m = re.search(r"Choice\s+([A-Z]+)", valori)
    return PREFIX + "_" + m.group(1).lower() if m else None


def tinta_lookup(tip):
    m = re.match(r"Lookup \((\w+)\)", tip)
    return m.group(1) if m else None


# ---------------------------------------------- constructia payloadurilor

def payload_optionset(ch):
    return {
        "@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
        "Name": ch["nume"],
        "DisplayName": eticheta(ch["eticheta"]),
        "IsGlobal": True,
        "OptionSetType": "Picklist",
        "Options": [{"Value": v["v"], "Label": eticheta(v["e"])} for v in ch["valori"]],
    }


def payload_entitate(t):
    primara = next((c for c in t["coloane"] if c["nume_logic"] == t["coloana_primara"]),
                   t["coloane"][0])
    # coloana primara este intotdeauna Text in Dataverse, chiar daca modelul zice Autonumber
    lungime = parse_lungime(primara["tip"], 200)
    attr_primar = {
        "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
        "SchemaName": schema(primara["nume_logic"]),
        "LogicalName": primara["nume_logic"],
        "DisplayName": eticheta(primara["nume"]),
        "RequiredLevel": {"Value": "ApplicationRequired"},
        "MaxLength": min(lungime, 4000),
        "FormatName": {"Value": "Text"},
        "IsPrimaryName": True,
    }
    if primara["tip"].startswith("Autonumber"):
        format_auto = (primara.get("valori") or "").split("|")[0].strip()
        if format_auto:
            attr_primar["AutoNumberFormat"] = format_auto

    proprietate = "UserOwned" if t["categorie"] in (
        "Radacina", "Copil", "Tranzactionala", "Derivata", "Cunoastere") else "OrganizationOwned"

    return {
        "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",
        "SchemaName": schema(t["nume_logic"]),
        "LogicalName": t["nume_logic"],
        "DisplayName": eticheta(t["nume"]),
        "DisplayCollectionName": eticheta(t["nume"]),
        "Description": eticheta(f"{t['cod']} - {t['categorie']}, val {t['val']}"),
        "OwnershipType": proprietate,
        "IsActivity": False,
        "HasNotes": False,
        "HasActivities": False,
        "IsAuditEnabled": {"Value": True},
        "Attributes": [attr_primar],
    }


def payload_atribut(c, tabela):
    """Returneaza (payload, nota) sau (None, motiv) daca se sare."""
    tip = c["tip"]
    baza = tip.split(" (")[0]
    nume = c["nume_logic"]
    comun = {
        "SchemaName": schema(nume),
        "LogicalName": nume,
        "DisplayName": eticheta(c["nume"]),
        "RequiredLevel": {"Value": "ApplicationRequired" if c["obligatoriu"] else "None"},
        "IsAuditEnabled": {"Value": True},
    }
    if c.get("observatii"):
        comun["Description"] = eticheta(c["observatii"][:500])

    if baza == "Lookup":
        return None, "lookup - se creeaza prin relatie"

    if baza in ("Calculated", "Rollup"):
        return None, f"{baza} - formula se configureaza manual in UI"

    if baza == "Text":
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
                "MaxLength": min(parse_lungime(tip, 100), 4000),
                "FormatName": {"Value": "Text"}}, None

    if baza == "Text Area":
        lg = parse_lungime(tip, 2000)
        if lg > 4000:
            return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.MemoAttributeMetadata",
                    "MaxLength": lg, "Format": "TextArea"}, None
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
                "MaxLength": lg, "FormatName": {"Value": "TextArea"}}, None

    if baza == "Whole Number":
        iv = parse_interval(c.get("valori")) or (-2147483648, 2147483647)
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.IntegerAttributeMetadata",
                "MinValue": int(iv[0]), "MaxValue": int(iv[1]),
                "Format": "None"}, None

    if baza == "Decimal":
        iv = parse_interval(c.get("valori")) or (-100000000000, 100000000000)
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.DecimalAttributeMetadata",
                "Precision": parse_lungime(tip, 2),
                "MinValue": iv[0], "MaxValue": iv[1]}, None

    if baza == "Currency":
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.MoneyAttributeMetadata",
                "Precision": parse_lungime(tip, 2), "PrecisionSource": 2,
                "MinValue": -922337203685477.0, "MaxValue": 922337203685477.0}, None

    if baza == "Yes/No":
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.BooleanAttributeMetadata",
                "OptionSet": {"@odata.type": "Microsoft.Dynamics.CRM.BooleanOptionSetMetadata",
                              "TrueOption": {"Value": 1, "Label": eticheta("Da")},
                              "FalseOption": {"Value": 0, "Label": eticheta("Nu")}}}, None

    if baza == "Date Only":
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.DateTimeAttributeMetadata",
                "Format": "DateOnly",
                "DateTimeBehavior": {"Value": "DateOnly"}}, None

    if baza == "Date and Time":
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.DateTimeAttributeMetadata",
                "Format": "DateAndTime",
                "DateTimeBehavior": {"Value": "UserLocal"}}, None

    if baza == "Image":
        return {**comun, "@odata.type": "Microsoft.Dynamics.CRM.ImageAttributeMetadata",
                "MaxSizeInKB": 1024, "IsPrimaryImage": False}, None

    if baza == "Autonumber":
        format_auto = (c.get("valori") or "").split("|")[0].strip()
        p = {**comun, "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
             "MaxLength": 100, "FormatName": {"Value": "Text"}}
        if format_auto and "{" in format_auto:
            p["AutoNumberFormat"] = format_auto
        return p, None

    if baza == "Choice":
        gs = choice_referit(c.get("valori"))
        multi = "(multi)" in tip
        tip_odata = ("Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata" if multi
                     else "Microsoft.Dynamics.CRM.PicklistAttributeMetadata")
        if gs:
            return {**comun, "@odata.type": tip_odata,
                    "GlobalOptionSet@odata.bind": f"/GlobalOptionSetDefinitions(Name='{gs}')"}, None
        # choice local: valorile sunt enumerate cu " / "
        brut = (c.get("valori") or "").split("|")[0]
        optiuni = [o.strip() for o in brut.split("/") if o.strip() and not o.strip().startswith("Implicit")]
        if not optiuni:
            return None, "choice fara valori enumerate - se completeaza manual"
        return {**comun, "@odata.type": tip_odata,
                "OptionSet": {"@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
                              "IsGlobal": False, "OptionSetType": "Picklist",
                              "Options": [{"Value": 100000000 + i, "Label": eticheta(o)}
                                          for i, o in enumerate(optiuni)]}}, None

    return None, f"tip nesuportat: {tip}"


CASCADA = {
    "Cascade All": {"Assign": "Cascade", "Delete": "Cascade", "Merge": "Cascade",
                    "Reparent": "Cascade", "Share": "Cascade", "Unshare": "Cascade"},
    "Restrict": {"Assign": "NoCascade", "Delete": "Restrict", "Merge": "NoCascade",
                 "Reparent": "NoCascade", "Share": "NoCascade", "Unshare": "NoCascade"},
    "Remove Link": {"Assign": "NoCascade", "Delete": "RemoveLink", "Merge": "NoCascade",
                    "Reparent": "NoCascade", "Share": "NoCascade", "Unshare": "NoCascade"},
}


def payload_relatie(r, tabele):
    parinte = r.get("parinte") or r.get("la")
    copil = r.get("copil") or r.get("de_la")
    col = r["coloana"]
    nume_rel = f"{PREFIX}_{copil.replace(PREFIX + '_','')}_{parinte.replace(PREFIX + '_','')}_{col.replace(PREFIX + '_','')}"
    et_copil = tabele.get(copil)
    coloana = None
    if et_copil:
        coloana = next((c for c in et_copil["coloane"] if c["nume_logic"] == col), None)
    return {
        "@odata.type": "Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata",
        "SchemaName": schema(nume_rel)[:100],
        "ReferencedEntity": parinte,
        "ReferencingEntity": copil,
        "CascadeConfiguration": CASCADA.get(r.get("stergere", "Remove Link"), CASCADA["Remove Link"]),
        "Lookup": {
            "@odata.type": "Microsoft.Dynamics.CRM.LookupAttributeMetadata",
            "SchemaName": schema(col),
            "LogicalName": col,
            "DisplayName": eticheta(coloana["nume"] if coloana else col),
            "RequiredLevel": {"Value": "ApplicationRequired" if (coloana and coloana["obligatoriu"]) else "None"},
            "IsAuditEnabled": {"Value": True},
        },
        "AssociatedMenuConfiguration": {
            "Behavior": "UseCollectionName", "Group": "Details", "Order": 10000,
        },
    }


# ------------------------------------------------------------ generarea

def construieste():
    choices = incarca("choices.json")
    tabele_doc = incarca("tabele.json")
    relatii = incarca("relatii.json")
    tabele = {t["nume_logic"]: t for t in tabele_doc["tabele"]}

    out = {"optionsets": [], "entities": [], "attributes": [], "relationships": []}
    sarite = []

    for ch in choices["choices"]:
        out["optionsets"].append(payload_optionset(ch))

    for t in tabele_doc["tabele"]:
        out["entities"].append(payload_entitate(t))
        for c in t["coloane"]:
            if c["nume_logic"] == t["coloana_primara"]:
                continue
            p, motiv = payload_atribut(c, t)
            if p:
                out["attributes"].append({"entitate": t["nume_logic"], "payload": p})
            else:
                sarite.append({"tabela": t["nume_logic"], "coloana": c["nume_logic"],
                               "tip": c["tip"], "motiv": motiv})

    toate_rel = (relatii["arbore_principal"] + relatii["relatii_nomenclatoare"]
                 + relatii["relatii_transversale"])
    vazute = set()
    for r in toate_rel:
        copil = r.get("copil") or r.get("de_la")
        cheie = (copil, r["coloana"])
        if cheie in vazute:
            continue
        vazute.add(cheie)
        out["relationships"].append(payload_relatie(r, tabele))

    # lookup-uri catre systemuser, care nu apar in relatii.json
    for t in tabele_doc["tabele"]:
        for c in t["coloane"]:
            if tinta_lookup(c["tip"]) == "systemuser":
                cheie = (t["nume_logic"], c["nume_logic"])
                if cheie in vazute:
                    continue
                vazute.add(cheie)
                out["relationships"].append(payload_relatie(
                    {"parinte": "systemuser", "copil": t["nume_logic"],
                     "coloana": c["nume_logic"], "stergere": "Remove Link"}, tabele))

    return out, sarite


# --------------------------------------------------------------- executia

def token():
    import urllib.parse, urllib.request
    tenant = os.environ["DV_TENANT_ID"]
    date = urllib.parse.urlencode({
        "client_id": os.environ["DV_CLIENT_ID"],
        "client_secret": os.environ["DV_CLIENT_SECRET"],
        "grant_type": "client_credentials",
        "scope": os.environ["DV_URL"].rstrip("/") + "/.default",
    }).encode()
    url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
    with urllib.request.urlopen(urllib.request.Request(url, data=date)) as r:
        return json.load(r)["access_token"]


def apel(metoda, cale, corp, tk):
    import urllib.request, urllib.error
    url = os.environ["DV_URL"].rstrip("/") + "/api/data/v9.2/" + cale
    date = json.dumps(corp).encode() if corp is not None else None
    cerere = urllib.request.Request(url, data=date, method=metoda)
    for k, v in {"Authorization": f"Bearer {tk}", "Content-Type": "application/json",
                 "OData-MaxVersion": "4.0", "OData-Version": "4.0",
                 "MSCRM.SolutionUniqueName": SOLUTIE}.items():
        cerere.add_header(k, v)
    try:
        with urllib.request.urlopen(cerere) as r:
            corp_raspuns = r.read().decode()
            return True, (json.loads(corp_raspuns) if corp_raspuns else None)
    except urllib.error.HTTPError as e:
        return False, e.read().decode()[:600]


def stare_incarca():
    return json.loads(STARE.read_text()) if STARE.exists() else {"facut": []}


def stare_salveaza(s):
    STARE.write_text(json.dumps(s, ensure_ascii=False, indent=2))


def ruleaza(payloaduri, etape, dry):
    stare = stare_incarca()
    facut = set(stare["facut"])
    tk = None if dry else token()
    stats = {}

    plan = [
        ("optionsets", "GlobalOptionSetDefinitions",
         lambda p: (p["Name"], p)),
        ("entities", "EntityDefinitions",
         lambda p: (p["LogicalName"], p)),
        ("attributes", None,
         lambda p: (f"{p['entitate']}.{p['payload']['LogicalName']}", p)),
        ("relationships", "RelationshipDefinitions",
         lambda p: (p["SchemaName"], p)),
    ]

    for etapa, cale, cheie_fn in plan:
        if etape and etapa not in etape:
            continue
        elemente = payloaduri[etapa]
        ok = sarit = eroare = 0
        print(f"\n=== {etapa} ({len(elemente)}) ===")
        for el in elemente:
            cheie, p = cheie_fn(el)
            marca = f"{etapa}:{cheie}"
            if marca in facut:
                sarit += 1
                continue
            if dry:
                ok += 1
                continue
            if etapa == "attributes":
                c = f"EntityDefinitions(LogicalName='{p['entitate']}')/Attributes"
                corp = p["payload"]
            else:
                c, corp = cale, p
            reusit, raspuns = apel("POST", c, corp, tk)
            if reusit:
                ok += 1
                facut.add(marca)
                stare["facut"] = sorted(facut)
                if ok % 25 == 0:
                    stare_salveaza(stare)
                    print(f"  ... {ok} create")
            else:
                eroare += 1
                print(f"  ! {cheie}: {raspuns}")
            time.sleep(0.06)  # menajeaza limita de API
        stare_salveaza(stare)
        stats[etapa] = {"create": ok, "deja_existente": sarit, "erori": eroare}
        print(f"  create {ok} | sarite {sarit} | erori {eroare}")
    return stats


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="nu apeleaza serverul")
    ap.add_argument("--scrie-payload", action="store_true", help="salveaza payloadurile ca JSON")
    ap.add_argument("--etapa", action="append",
                    choices=["optionsets", "entities", "attributes", "relationships"])
    a = ap.parse_args()

    payloaduri, sarite = construieste()

    print("PAYLOADURI GENERATE")
    for k, v in payloaduri.items():
        print(f"  {k:16} {len(v):5}")
    print(f"\nColoane care NU se creeaza automat: {len(sarite)}")
    grupat = {}
    for s in sarite:
        grupat.setdefault(s["motiv"], []).append(s)
    for motiv, lista in sorted(grupat.items(), key=lambda x: -len(x[1])):
        print(f"  {len(lista):4}  {motiv}")

    if a.scrie_payload:
        PAYLOADURI.mkdir(exist_ok=True)
        for k, v in payloaduri.items():
            (PAYLOADURI / f"{k}.json").write_text(
                json.dumps(v, ensure_ascii=False, indent=2))
        (PAYLOADURI / "coloane-manuale.json").write_text(
            json.dumps(sarite, ensure_ascii=False, indent=2))
        print(f"\nPayloaduri scrise in {PAYLOADURI}")

    if a.dry_run:
        print("\nDRY RUN - nu s-a apelat serverul.")
        return 0

    for v in ("DV_URL", "DV_CLIENT_ID", "DV_CLIENT_SECRET", "DV_TENANT_ID"):
        if not os.environ.get(v):
            print(f"\nLipseste variabila de mediu {v}. Vezi build/deploy/README.md")
            return 1

    ruleaza(payloaduri, a.etapa, dry=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
