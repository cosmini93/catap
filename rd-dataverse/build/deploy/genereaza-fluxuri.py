#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genereaza scheletele celor 35 de fluxuri Power Automate din Sectiunile 12, 23 si 25.

Fiecare flux primeste: declansator configurat, referinte de conexiune, variabile de mediu,
scope Try/Catch cu notificare de eroare si scriere in rd_logeroare, correlation id si
politica de reincercare.

Ce NU se genereaza: logica de business din interiorul scope-ului Try. Aceea este descrisa
ca pasi comentati, din blueprint, si se implementeaza in designer.

Iesire: build/deploy/payloaduri-fluxuri/
"""
import json, uuid
from pathlib import Path

OUT = Path(__file__).parent / "payloaduri-fluxuri"
CR_DV = "shared_commondataserviceforapps"
CR_MAIL = "shared_office365"
CR_APROB = "shared_approvals"
CR_TEAMS = "shared_teams"
CR_SP = "shared_sharepointonline"

# cod, nume, tip declansator, tabela/frecventa, val, pasi de business
FLUXURI = [
 ("FLX-01","Generarea codului de proiect la acceptare","modificare","rd_solicitare",1,
  ["Filtreaza pe rd_rezultattriaj = Acceptata si rd_proiect gol",
   "Creeaza rd_proiect copiind client, KAM, produs, gramaj, ambalare, volum, referinta",
   "Seteaza status Acceptat - planificat si data acceptarii",
   "Creeaza rd_referinta din datele solicitarii",
   "Leaga solicitarea de proiect",
   "Apeleaza FLX-02, FLX-03, FLX-05 ca fluxuri copil"],
  [CR_DV, CR_MAIL]),
 ("FLX-02","Generarea arborelui de foldere SharePoint","apelat","-",1,
  ["Creeaza folderul de an daca nu exista",
   "Curata numele produsului de caractere interzise si trunchiaza la 100",
   "Creeaza folderul de proiect {cod}_{nume produs}",
   "Creeaza cele 10 subfoldere din 5.1.1",
   "Creeaza SharePointDocumentLocation catre folderul radacina",
   "Scrie URL-ul in rd_folderurl"],
  [CR_DV, CR_SP]),
 ("FLX-03","Propunerea datei estimate de finalizare","modificare","rd_proiect",1,
  ["Citeste durata standard din sablonul de etape",
   "Aplica factorul de incarcare a tehnologului (A1.2.2)",
   "Aplica factorul de coada pe linie (A1.2.3)",
   "Aplica factorul de sezonalitate (A1.2.4)",
   "Adauga maximul adaosurilor pentru materii prime noi (A1.2.5)",
   "Scrie rd_termenpropus; precompleteaza rd_termennegociat daca e gol",
   "Genereaza datele planificate pe etape"],
  [CR_DV, CR_MAIL]),
 ("FLX-04","Crearea proiectului-copil","la cerere","rd_proiect",2,
  ["Determina sufixul urmator disponibil",
   "Creeaza proiectul cu rd_proiectparinte completat",
   "Copiaza client, KAM, linie, tip, referinta, tehnolog",
   "Copiaza versiunea curenta de reteta cu toate liniile",
   "Creeaza folderul ca subfolder al parintelui",
   "Genereaza livrabilele conform sablonului de tip Abatere"],
  [CR_DV, CR_SP, CR_MAIL]),
 ("FLX-05","Generarea si reevaluarea livrabilelor","modificare","rd_proiect",1,
  ["Citeste sabloanele active filtrate pe tipul de proiect",
   "Evalueaza cele 8 conditii de aplicabilitate din 4.2",
   "Creeaza rd_livrabil cu termen = acceptare + ROUND(offset * durata / 14) zile lucratoare",
   "Rezolva responsabilul din rol prin rd_profiltehnolog",
   "La reevaluare: adauga livrabilele nou aplicabile, treci in Nu se aplica pe cele devenite false",
   "Recalculeaza rd_procentlivrabile, rd_livrabileok, rd_urmatorullivrabil"],
  [CR_DV, CR_MAIL]),
 ("FLX-06","Recalcularea incarcarii","programat","orar 06-20",1,
  ["Pentru fiecare profil activ: numara proiecte active si P1, calculeaza gradul si semnalul",
   "Pentru fiecare linie activa: numara proiectele care o vizeaza",
   "Pentru fiecare client: numara proiectele active"],
  [CR_DV]),
 ("FLX-07","Recalcularea la modificarea unui ETA","modificare","rd_mpproiect",2,
  ["Daca rd_etainitial e gol, completeaza-l si iesi",
   "Incrementeaza rd_modificarieta",
   "Daca noul ETA depaseste data etapei de testare, muta termenul propus",
   "Creeaza blocaj daca intarzierea depaseste 5 zile lucratoare",
   "Scrie o inregistrare in rd_leadtimeistoric",
   "Notifica obligatoriu KAM si tehnolog cu vechea si noua data"],
  [CR_DV, CR_MAIL, CR_TEAMS]),
 ("FLX-08","Alerte de termen","programat","zilnic 07:00",1,
  ["Livrabile cu termen peste 3 zile lucratoare: scrie in coada de alerte",
   "Livrabile depasite: scrie rd_zileintarziere si adauga in coada",
   "Depasite peste 10 zile: marcheaza pentru escaladare",
   "Proiecte cu termen negociat in 5 zile, fara implementare: adauga in coada",
   "NU trimite direct - FLX-30 consolideaza si trimite"],
  [CR_DV]),
 ("FLX-09","Calculul impactului blocajelor","modificare","rd_blocaj",2,
  ["Calculeaza zilele lucratoare intre start si sfarsit (sau azi)",
   "Scrie rd_impactzile",
   "Recalculeaza rd_zileblocate pe proiect si pe etapa, prin reuniune de intervale",
   "La deschidere cu rd_oprsteceas: treci proiectul in Blocat, pastreaza statusul anterior",
   "La inchiderea ultimului blocaj activ: readu statusul anterior"],
  [CR_DV, CR_MAIL]),
 ("FLX-10","Recalcularea scorului de prioritate","programat","luni 06:00",2,
  ["Calculeaza cele 6 componente din A1.1, cu ponderile din variabilele de mediu",
   "Adauga bonusul de imbatranire, plafonat la 20",
   "Verifica bugetul de urgenta pe KAM inainte de a promova in P1",
   "Scrie rd_scorprioritate si rd_banda; nu suprascrie proiectele cu scor suprascris",
   "Expira suprascrierile mai vechi de 90 de zile",
   "Trimite lista proiectelor care si-au schimbat banda"],
  [CR_DV, CR_MAIL]),
 ("FLX-11","Statistica de trial si scorul senzorial","modificare","rd_masuratoare",1,
  ["Asteapta 60 de secunde de la ultima modificare",
   "Grupeaza masuratorile pe tip, excluzand cele marcate excluse",
   "Calculeaza media, abaterea standard (n-1), CV, min, max, conformitatea",
   "Creeaza sau actualizeaza rd_statisticatrial",
   "Seteaza verdictul conform 6.3.2",
   "Pentru senzorial: media pe criteriu, scorul ponderat, dezacordul maxim, verdictul din 6.5.5"],
  [CR_DV]),
 ("FLX-12","Generarea documentelor din sabloane Word","la cerere","-",2,
  ["Citeste sablonul din biblioteca Sabloane",
   "Citeste datele din Dataverse conform mapei documentului din 5.5",
   "Populeaza sablonul cu Word Online",
   "Converteste in PDF",
   "Salveaza in folderul de faza, cu numele din 5.2.1",
   "Scrie metadatele si leaga fisierul de livrabil"],
  [CR_DV, CR_SP, CR_MAIL]),
 ("FLX-13","Recalcularea alergenilor si a nutritionalelor","modificare","rd_liniereteta",3,
  ["Calculeaza contributia fiecarei linii, per 100 g de aluat",
   "Corecteaza cu factorul de randament (9.2.1.2)",
   "Recalculeaza energia din macronutrienti, cu factorii legali",
   "Reuniunea alergenilor continuti si a urmelor, minus cei deja continuti",
   "Pentru retete validate: NU modifica; genereaza alerta de impact (9.5.2)",
   "Scrie rd_datacalcul"],
  [CR_DV, CR_MAIL]),
 ("FLX-14","Solicitari amanate","programat","zilnic",1,
  ["Cauta solicitarile cu rd_amanatapanala <= azi si status Amanata",
   "Treci in status Trimisa",
   "Notifica Manager R&D si KAM"],
  [CR_DV, CR_MAIL]),
 ("FLX-15","Declansarea revizuirii post-implementare","programat","zilnic",3,
  ["Cauta implementarile cu data completata, fara revizuire pentru pragul curent",
   "Creeaza rd_revizuire cu etapa si data scadenta",
   "Creeaza livrabilul LIV-41 / 42 / 43",
   "Precompleteaza campurile automate din 8.2",
   "Trimite cererile de date catre KAM, Calitate, Productie si Controlling",
   "Treci proiectul in status In revizuire"],
  [CR_DV, CR_MAIL]),
 ("FLX-16","Calculul indicatorilor","programat","zilnic si lunar",3,
  ["Zilnic: rd_zilecoada, rd_ttotalnet, rd_abateretermen, rd_ultimaactivitate",
   "Lunar: T-Total prin reuniune de intervale de blocaj, nu prin suma (13.2.2)",
   "Lunar: Q-Corect ponderat pe cele 5 componente din 13.3.3",
   "Lunar: Q-Complet la inchidere si in curs",
   "Scrie rd_masurareindicator; masuratorile nu se recalculeaza retroactiv"],
  [CR_DV, CR_MAIL]),
 ("FLX-17","Propunerea de corectie a duratelor","programat","lunar",3,
  ["Verifica cele 3 conditii din 14.4.1",
   "Calculeaza mediana duratei nete pe etapa, pe ultimele 12 luni",
   "Calculeaza si percentila 80, minimul, maximul",
   "Scrie rd_duratapropusa in sablon; NU modifica rd_duratastandard"],
  [CR_DV]),
 ("FLX-18","Aprobarea planului si a antecalculului","modificare","rd_livrabil",2,
  ["Trimite aprobare catre aprobatorul din livrabil",
   "Daca marja e sub pragul din variabila de mediu: doua trepte, Manager apoi Head",
   "La aprobare: status Realizat, data si aprobatorul",
   "La respingere: status Respins cu motivul din raspuns, notifica responsabilul"],
  [CR_DV, CR_APROB, CR_MAIL]),
 ("FLX-19","Gestionarea documentelor","creare","SharePoint",2,
  ["Extrage codul de proiect si tipul din numele fisierului",
   "Completeaza cele 13 metadate din inregistrarea de proiect",
   "Leaga fisierul de livrabil si treci livrabilul in In lucru",
   "La status Aprobat: publica versiune majora, aplica blocarea din 5.4.3",
   "Pentru fisierele confidentiale: permisiuni unice",
   "Nume neconform: marcheaza Neclasificat si notifica autorul cu formatul corect"],
  [CR_DV, CR_SP, CR_MAIL]),
 ("FLX-20","Arhivarea jurnalului de audit","programat","lunar",3,
  ["Exporta auditul tabelelor critice in CSV",
   "Salveaza in biblioteca Arhiva audit R&D, cu retentie de 10 ani"],
  [CR_DV, CR_SP]),
 ("FLX-21","Alerte de materie prima si de furnizor","programat","zilnic",2,
  ["MP critice cu ETA depasit si fara receptie",
   "MP cu ST de furnizor mai veche de 24 de luni",
   "Furnizori cu certificare expirata sau care expira in 60 de zile",
   "MP blocate de Calitate folosite in retete active",
   "Scrie in coada de alerte; FLX-30 consolideaza"],
  [CR_DV]),
 ("FLX-22","Notificarea schimbarii de status","modificare","rd_proiect",1,
  ["Determina destinatarii pe tranzitie, conform tabelului din 12.3",
   "Trimite in Teams, nu doar pe mail",
   "Include link direct catre proiect"],
  [CR_DV, CR_TEAMS, CR_MAIL]),
 ("FLX-23","Evaluarea criteriilor automate de gate","modificare","multiplu",1,
  ["Pentru fiecare criteriu cu tip Automata: evalueaza sursa (livrabil, camp, agregare)",
   "Scrie rezultatul in rd_verificaregate",
   "Recalculeaza rd_criteriiok si rd_procentpregatire",
   "Treci gate-ul in Gata de evaluare cand toate criteriile obligatorii sunt indeplinite",
   "Verifica riscurile cu RPN peste pragul sablonului"],
  [CR_DV, CR_MAIL]),
 ("FLX-24","Revizuirea lunara a riscurilor","programat","lunar",2,
  ["Cauta riscurile cu nivel Ridicat sau Critic si status deschis",
   "Creeaza actiune de revizuire pentru proprietar",
   "Marcheaza tendinta prin comparatie cu RPN-ul anterior"],
  [CR_DV, CR_MAIL]),
 ("FLX-25","Materializarea riscului in problema","modificare","rd_risc",2,
  ["La status Produs: creeaza rd_problema precompletata din risc",
   "Leaga in ambele sensuri",
   "NU inchide riscul - ramane inregistrat ca materializat"],
  [CR_DV, CR_MAIL]),
 ("FLX-26","Detectarea cauzelor repetate","programat","saptamanal",3,
  ["Grupeaza problemele inchise pe cauza radacina, pe ultimele 12 luni",
   "Marcheaza rd_esterepetare pe cele cu aceeasi cauza",
   "La a treia aparitie: apeleaza FLX-33 pentru draft de lectie"],
  [CR_DV]),
 ("FLX-27","Escaladarea actiunilor restante","programat","zilnic",1,
  ["Cauta actiunile depasite, neamânate",
   "Aplica cele 4 niveluri de escaladare din 23.7.3, dupa 0, 5, 10 si 15 zile",
   "Scrie rd_nivelescaladare si rd_escaladata",
   "Opreste escaladarea la inchidere sau la amanare cu motiv"],
  [CR_DV]),
 ("FLX-28","Lead time forecast si OTIF","programat","lunar",2,
  ["Pentru fiecare furnizor: media ultimelor 3 si 12 livrari, variabilitatea",
   "Lead time forecast = max(media 3, media 12) + 1 abatere standard",
   "Acuratetea ETA: livrari in +/- 2 zile fata de ETA initial",
   "OTIF: livrari la timp si complete",
   "Sub 3 livrari: pastreaza valoarea implicita pe tip, marcata ca estimare"],
  [CR_DV]),
 ("FLX-29","Snapshot de sanatate a proiectului","programat","luni",3,
  ["Pentru fiecare proiect activ: calculeaza cele 7 componente din 24.3.2",
   "Scrie rd_snapshotsanatate; inregistrarea nu se mai modifica",
   "Calculeaza variatia fata de saptamana trecuta",
   "Alerta la scadere de peste 15 puncte sau 3 saptamani consecutive de scadere"],
  [CR_DV, CR_MAIL]),
 ("FLX-30","Consolidarea alertelor in digest","programat","zilnic 07:00",1,
  ["Citeste coada de alerte scrisa de FLX-08, FLX-21, FLX-27",
   "Aplica regulile din 23.7.2: prag de 24 de ore, escaladare doar la crestere de severitate",
   "Exclude alertele amanate cu motiv si data de revenire",
   "Grupeaza pe persoana si pe tip",
   "Trimite un singur mesaj pe persoana, in Teams",
   "Scrie rd_dataultimaalerta pe inregistrarile atinse"],
  [CR_DV, CR_TEAMS, CR_MAIL]),
 ("FLX-31","Evaluarea loturilor de stabilizare","modificare","rd_lotstabilizare",3,
  ["Evalueaza conformitatea lotului conform 24.1.2",
   "Numara loturile conforme consecutive; reseteaza la primul neconform",
   "Numara schimburile acoperite",
   "La al treilea lot conform: status Reusita, declanseaza gate-ul G7",
   "Lot neconform: creeaza automat o problema",
   "Diferenta de randament sub -3 pp: problema de categorie Financiar, severitate Majora"],
  [CR_DV, CR_MAIL]),
 ("FLX-32","Calculul capabilitatii de proces","programat","lunar",3,
  ["Verifica cele 4 conditii din 24.2.5: minimum 30 de valori, minimum 3 loturi, limite declarate",
   "Calculeaza Cp si Cpk conform 24.2.2",
   "Calculeaza deplasarea fata de tinta",
   "Seteaza verdictul si genereaza recomandarea din combinatia Cp / Cpk",
   "Sub 30 de valori: verdict Date insuficiente, fara cifre"],
  [CR_DV]),
 ("FLX-33","Generarea drafturilor de lectii","modificare","multiplu",3,
  ["Cele 8 declansatoare din 25.2.2",
   "Creeaza rd_lectie cu status Draft si rd_generataauto = Da",
   "Precompleteaza situatia si cauza din sursa",
   "Creeaza actiune pentru responsabil, cu termen de 10 zile lucratoare",
   "NU aproba automat"],
  [CR_DV, CR_MAIL]),
 ("FLX-34","Recomandarea lectiilor","modificare","multiplu",3,
  ["Cele 6 momente din 25.4.2",
   "Calculeaza scorul de potrivire conform 25.4.4",
   "Afiseaza maximum 3 recomandari cu scor peste 40",
   "Scrie motivul potrivirii, ca sa fie credibila",
   "La status Aplicata: creeaza rd_utilizarelectie"],
  [CR_DV]),
 ("FLX-35","Revizuirea lectiilor nereutilizate","programat","semestrial",3,
  ["Cauta lectiile aprobate, nereutilizate de peste 18 luni",
   "Creeaza actiune de revizuire pentru autor",
   "La confirmare: arhiveaza"],
  [CR_DV, CR_MAIL]),
]


def declansator(tip, tinta):
    if tip == "programat":
        return {"Recurrence": {"type": "Recurrence", "recurrence": {
            "frequency": "Day", "interval": 1,
            "schedule": {"hours": ["7"], "minutes": [0]}},
            "metadata": {"frecventa_ceruta": tinta}}}
    if tip == "la cerere":
        return {"manual": {"type": "Request", "kind": "Button",
                           "inputs": {"schema": {"type": "object", "properties": {
                               "recordId": {"type": "string", "title": "ID inregistrare"}}}}}}
    if tip == "apelat":
        return {"manual": {"type": "Request", "kind": "Skill",
                           "inputs": {"schema": {"type": "object", "properties": {
                               "proiectId": {"type": "string"}}}}}}
    if tip == "creare":
        return {"cand_se_creeaza": {"type": "OpenApiConnectionWebhook",
            "inputs": {"host": {"connectionName": "shared_sharepointonline",
                                "operationId": "OnNewFileV2"}},
            "metadata": {"tinta": tinta}}}
    return {"cand_se_modifica": {"type": "OpenApiConnectionWebhook", "inputs": {
        "host": {"connectionName": "shared_commondataserviceforapps",
                 "operationId": "SubscribeWebhookTrigger"},
        "parameters": {"subscriptionRequest/message": 3,
                       "subscriptionRequest/entityname": tinta,
                       "subscriptionRequest/scope": 4}}}}


def flux(cod, nume, tip, tinta, val, pasi, conexiuni):
    corelatie = {"type": "Compose", "runAfter": {},
                 "inputs": "@{guid()}", "description": "Correlation ID pentru trasabilitate (22.6)"}
    business = {}
    for i, p in enumerate(pasi):
        business[f"Pas_{i+1:02d}"] = {
            "type": "Compose",
            "runAfter": {} if i == 0 else {f"Pas_{i:02d}": ["Succeeded"]},
            "inputs": f"DE IMPLEMENTAT: {p}",
            "description": p,
        }
    return {
        "cod": cod, "nume": f"{cod} {nume}", "val": val,
        "conexiuni_necesare": conexiuni,
        "definitie": {
            "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {
                "$connections": {"defaultValue": {}, "type": "Object"},
                "rd_EmailAdministrator": {"type": "String",
                                          "metadata": {"variabila_de_mediu": True}},
            },
            "triggers": declansator(tip, tinta),
            "actions": {
                "Correlation_ID": corelatie,
                "Try": {
                    "type": "Scope", "runAfter": {"Correlation_ID": ["Succeeded"]},
                    "actions": business,
                    "runtimeConfiguration": {"retryPolicy": {
                        "type": "exponential", "count": 4, "interval": "PT10S"}},
                },
                "Catch": {
                    "type": "Scope",
                    "runAfter": {"Try": ["Failed", "Skipped", "TimedOut"]},
                    "actions": {
                        "Scrie_in_log": {
                            "type": "OpenApiConnection", "runAfter": {},
                            "inputs": {"host": {"connectionName": CR_DV,
                                                "operationId": "CreateRecord"},
                                       "parameters": {"entityName": "rd_logeroares",
                                                      "item/rd_flux": f"{cod} {nume}",
                                                      "item/rd_correlationid": "@{outputs('Correlation_ID')}",
                                                      "item/rd_mesaj": "@{result('Try')}",
                                                      "item/rd_statuslog": 100000000}},
                            "description": "TBL-59, cerinta 12.1.3"},
                        "Notifica_administratorul": {
                            "type": "OpenApiConnection",
                            "runAfter": {"Scrie_in_log": ["Succeeded", "Failed"]},
                            "inputs": {"host": {"connectionName": CR_MAIL,
                                                "operationId": "SendEmailV2"},
                                       "parameters": {
                                           "emailMessage/To": "@parameters('rd_EmailAdministrator')",
                                           "emailMessage/Subject": f"Esec {cod}",
                                           "emailMessage/Body": "@{result('Try')}"}}},
                    },
                },
            },
        },
    }


def main():
    OUT.mkdir(exist_ok=True)
    toate = []
    for f in FLUXURI:
        d = flux(*f)
        toate.append(d)
        (OUT / f"{d['cod']}.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=1))
    (OUT / "_index.json").write_text(json.dumps(
        [{"cod": f["cod"], "nume": f["nume"], "val": f["val"],
          "conexiuni": f["conexiuni_necesare"],
          "pasi_de_implementat": len(f["definitie"]["actions"]["Try"]["actions"])}
         for f in toate], ensure_ascii=False, indent=1))

    import collections as c
    pe_val = c.Counter(f["val"] for f in toate)
    conex = c.Counter(x for f in toate for x in f["conexiuni_necesare"])
    print("FLUXURI GENERATE")
    print(f"  fluxuri                {len(toate):5}")
    print(f"  pasi de business       {sum(len(f['definitie']['actions']['Try']['actions']) for f in toate):5}")
    print(f"  pe val                 {dict(sorted(pe_val.items()))}")
    print(f"  conexiuni distincte    {len(conex)}  {dict(conex)}")
    print(f"\nFiecare flux are: correlation id, scope Try/Catch, retry exponential x4,")
    print(f"scriere in rd_logeroare si notificare de esec.")
    print(f"\nIesire: {OUT}")


if __name__ == "__main__":
    main()
