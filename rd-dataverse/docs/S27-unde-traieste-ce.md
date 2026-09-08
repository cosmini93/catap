# Sectiunea 27 - Unde traieste ce

Sectiune de clarificare. Explica ce este repository-ul acesta, ce este solutia reala si
unde se face trecerea de la unul la celalalt.

Se citeste prima, de oricine preia proiectul.

## 27.1 Solutia este 100% Microsoft

Nimic din blueprint nu schimba deciziile de arhitectura din briefingul initial. Produsul
final ruleaza integral in tenantul companiei, pe platforma Microsoft:

| Componenta | Unde ruleaza | Ce contine |
|---|---|---|
| Baza de date | **Dataverse** | Cele 60 de tabele, 985 de coloane, 151 de relatii |
| Aplicatia de birou | **Power Apps model-driven** | Harta de site, 59 de formulare, 155 de vizualizari |
| Aplicatia de hala | **Power Apps canvas** | Masuratori, senzorial, receptie mostra, checklist productie 0 |
| Automatizarile | **Power Automate** | Cele 35 de fluxuri |
| Documentele | **SharePoint Online** | Arborele de foldere pe faze, metadate, versionare |
| Aprobarile | **Approvals** in Teams | Planul de dezvoltare, antecalculul, specificatiile |
| Rapoartele | **Power BI** | Cele 15 rapoarte din 13.6.1 |
| Identitatea si rolurile | **Entra ID** + roluri Dataverse | Cele 13 roluri, 6 echipe, 2931 de privilegii |
| Generarea documentelor | **Word Online** prin Power Automate | Cele 12 sabloane |

27.1.1 Nu exista niciun serviciu din afara acestei liste in solutia livrata. Politica DLP
din pasul 2 al ghidului Valului 0 face acest lucru obligatoriu, nu doar o intentie.

## 27.2 Ce este acest repository

**Nu este produsul. Este schela din care se construieste produsul.**

| Ce contine | Rol | Ramane dupa constructie? |
|---|---|---|
| `docs/` | Blueprintul: deciziile de arhitectura, regulile de business, motivele | **Da** - este documentatia solutiei, ceruta de constrangerea de preluare (17.5) |
| `data/` | Modelul exprimat ca date: tabele, coloane, relatii, Choice-uri, sabloane | **Da** - sursa de adevar pentru orice regenerare |
| `build/import/` | Fisierele CSV de import pentru nomenclatoare | Nu - se consuma o singura data |
| `build/deploy/*.py` | Scripturile care creeaza componentele in Dataverse | **Nu** - sunt unelte de constructie |
| `build/deploy/payloaduri*` | Ce trimit scripturile catre Dataverse | Nu - se regenereaza oricand |
| `build/deploy/sabloane-word/` | Cele 12 fisiere .docx | **Da** - se incarca in biblioteca `Sabloane` din SharePoint |
| `build/preview-ecrane.html` | Macheta vizuala | Nu - a servit la validarea aspectului inainte de constructie |

27.2.1 Python-ul nu face parte din solutie. Nu ruleaza in tenant, nu are nevoie de licenta
si nu apare nicaieri in produsul final. Este echivalentul schelei de pe santier: necesar
la constructie, demontat dupa.

27.2.2 Cine preia solutia peste doi ani are nevoie de doua lucruri: **solutia Dataverse
exportata** (fisierul .zip) si **documentele din `docs/`**. Nu are nevoie sa stie Python
si nu are nevoie de acest repository ca sa opereze sistemul. Ii trebuie doar daca vrea sa
regenereze ceva de la zero.

## 27.3 Puntea: unde fisierele devin sistem

Un singur moment, un singur mecanism:

```
   ACEST REPOSITORY                  TENANTUL COMPANIEI
   (fisiere)                         (Microsoft)

   data/tabele.json      ─┐
   data/relatii.json      │
   data/choices.json      ├──▶  provisioning.py  ──HTTPS──▶  Dataverse Web API
   payloaduri-ui/         │      genereaza-ui.py                     │
   payloaduri-fluxuri/   ─┘      (ruleaza pe laptopul                ▼
                                  constructorului)          tabele, coloane, relatii,
                                                            formulare, vizualizari,
   build/import/*.csv    ──────▶  import in Power Apps  ──▶  roluri, fluxuri reale
   sabloane-word/*.docx  ──────▶  incarcare in SharePoint         in solutia
                                                            RDSuitaDigitala
```

27.3.1 Scriptul se autentifica cu o inregistrare de aplicatie din Entra ID a companiei si
trimite cereri HTTP catre `https://organizatie.crm4.dynamics.com/api/data/v9.2/`. Din
acel moment, componentele exista in Dataverse ca si cum ar fi fost create manual in
interfata, sunt parte din solutia `RDSuitaDigitala` si se exporta normal.

27.3.2 **Eu nu pot face acest pas.** Nu am acces la tenantul companiei si nu trebuie sa am.
Scriptul se ruleaza de catre constructor, de pe calculatorul lui, cu credentialele lui.
Este si punctul in care se va vedea daca modelul e corect: cateva componente vor fi
respinse de server si vor cere corectii (26.6.1).

27.3.3 Dupa constructie, ciclul normal de lucru nu mai trece prin acest repository:
se lucreaza in Power Apps, se exporta solutia, se importa in test si productie, conform
procedurii din 17.2.2. Repository-ul se atinge din nou doar la o schimbare mare de model.

## 27.4 Ce a fost macheta HTML

`build/preview-ecrane.html` si versiunea ei publicata sunt o **macheta**, nu o aplicatie.
Rolul ei a fost sa arate cum vor arata ecranele inainte de a fi construite, ca structura
sa poata fi corectata cand corectia e ieftina.

27.4.1 Aplicatia reala arata diferit ca incadrare: Power Apps model-driven isi impune
propriul chrome - bara de comenzi, cautarea, panoul lateral, tema Fluent. Ce se pastreaza
din macheta este ce a fost generat din model: harta de site, filele, campurile si ordinea
lor.

27.4.2 Macheta nu se livreaza, nu se instaleaza si nu are utilizatori. Se poate sterge
fara consecinte.

## 27.5 Raspunsul scurt la "cum construim tool-ul"

| Pas | Cine | Unde | Durata |
|---|---|---|---|
| 1. Mediu Developer, publisher, solutie, DLP | Constructorul | Power Platform admin center | 0,5 zile |
| 2. Inregistrare de aplicatie in Entra ID, cu drept de metadate | IT sau constructorul | Portalul Azure / Entra | 0,5 zile |
| 3. Rularea celor trei scripturi de provizionare | Constructorul | Laptopul lui, catre tenant | 1 zi + 2-4 cicluri de corectie |
| 4. Cele 24 de coloane Calculated si Rollup, cheile alternative | Constructorul | Power Apps, interfata | 0,5 zile |
| 5. Importul nomenclatoarelor din CSV | Constructorul | Power Apps, import | 0,5 zile |
| 6. Incarcarea sabloanelor Word | Constructorul | SharePoint | 0,25 zile |
| 7. Legarea conexiunilor si testarea fluxurilor | Constructorul | Power Automate | 15 zile, pe valuri |
| 8. Aplicatia canvas | Constructorul | Power Apps Studio | 8 zile |
| 9. Datele companiei | Sales, Productie, Calitate | Fisierele sablon, apoi import | 8-12 zile, in paralel |
| 10. Testare, instruire, punere in functiune | Toti | - | 12-16 zile |

27.5.1 Pasii 1-6 sunt cei pe care generarea i-a comprimat: aproximativ 3 zile in loc de 45.
Pasii 7-10 sunt cei care raman, si sunt majoritatea efortului ramas (26.4.2).

27.5.2 Din tot acest lant, singurul lucru care nu s-a facut inca este chiar primul:
**crearea mediului si a inregistrarii de aplicatie.** Fara ele, scripturile nu au unde sa
trimita nimic. Este si raspunsul la intrebarea deschisa IQ-01.
