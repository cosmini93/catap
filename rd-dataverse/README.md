# Blueprint Suita Digitala R&D - Dataverse / Power Apps / SharePoint / Power Automate

Document de arhitectura pentru digitalizarea procesului R&D intr-o companie FMCG de
panificatie si patiserie congelata (2 amplasamente, 9 linii, ~400 persoane, 130-180
proiecte CDI pe an).

Rezultatul este un blueprint de constructie, nu cod. Se construieste modul cu modul,
fara alte decizii de arhitectura.

Limba: romana fara diacritice. Toate sectiunile sunt numerotate consecutiv pentru
referinta ulterioara (exemplu: 2.4.3, TBL-07, LIV-14, FLX-05).

## Cuprins

| Sectiune | Fisier | Continut |
|---|---|---|
| 0 | [S00-sumar-executiv.md](docs/S00-sumar-executiv.md) | Sumar executiv, maximum 10 randuri |
| 1 | [S01-harta-modulelor.md](docs/S01-harta-modulelor.md) | Harta modulelor, tip aplicatie, val de implementare |
| 2 | [S02-model-date.md](docs/S02-model-date.md) | Modelul de date Dataverse, tabela cu tabela |
| 3 | [S03-relatii.md](docs/S03-relatii.md) | Diagrama relatiilor, comportament la stergere |
| 4 | [S04-livrabile.md](docs/S04-livrabile.md) | Sablonul de livrabile pe faze |
| 5 | [S05-documentatie.md](docs/S05-documentatie.md) | Structura documentatiei, denumire, versionare, continut-cadru |
| 6 | [S06-masuratori-senzorial.md](docs/S06-masuratori-senzorial.md) | Masuratori, statistica, grila senzoriala |
| 7 | [S07-productie-0.md](docs/S07-productie-0.md) | Setul de inregistrari la productia 0 |
| 8 | [S08-revizuire-post-implementare.md](docs/S08-revizuire-post-implementare.md) | Revizuire la 30/60/90 de zile |
| 9 | [S09-alergeni-nutritionale.md](docs/S09-alergeni-nutritionale.md) | Calcul din reteta, urme, recalculare |
| 10 | [S10-ecrane.md](docs/S10-ecrane.md) | Ecrane model-driven si canvas mobil |
| 11 | [S11-securitate-roluri.md](docs/S11-securitate-roluri.md) | Matrice Rol x Tabela |
| 12 | [S12-automatizari.md](docs/S12-automatizari.md) | Fluxuri Power Automate |
| 13 | [S13-indicatori.md](docs/S13-indicatori.md) | T-Total, Q-Corect, Q-Complet, rapoarte |
| 14 | [S14-durate-etape.md](docs/S14-durate-etape.md) | Durate standard si autocalibrare |
| 15 | [S15-migrare.md](docs/S15-migrare.md) | Migrarea din Excel si din foldere |
| 16 | [S16-roadmap.md](docs/S16-roadmap.md) | Valuri 0-3, efort, masurare |
| 17 | [S17-trecere-productie.md](docs/S17-trecere-productie.md) | Cerinte catre IT, export/import solutie |
| 18 | [S18-riscuri.md](docs/S18-riscuri.md) | Registru de riscuri |
| 19 | [S19-criterii-acceptanta.md](docs/S19-criterii-acceptanta.md) | Lista verificabila pe modul |
| 20 | [S20-intrebari-deschise.md](docs/S20-intrebari-deschise.md) | Maximum 10 intrebari blocante |
| 21 | [S21-prompturi-continuare.md](docs/S21-prompturi-continuare.md) | Prompturi de constructie pe modul |

## Artefacte pentru constructie

Fisierele din `data/` sunt reprezentarea prelucrabila a blueprintului. Se folosesc la
crearea tabelelor, a nomenclatoarelor si a sabloanelor, si pot fi importate in Excel
sau consumate de un script de provizionare.

| Fisier | Continut |
|---|---|
| [data/tabele.json](data/tabele.json) | Toate tabelele si coloanele din Sectiunea 2 |
| [data/relatii.json](data/relatii.json) | Relatiile din Sectiunea 3, cu comportament la stergere |
| [data/choices.json](data/choices.json) | Toate seturile de optiuni globale |
| [data/sablon-livrabile.json](data/sablon-livrabile.json) | Cele 34 de livrabile standard, cu faza si conditia de aplicabilitate |
| [data/sablon-etape.json](data/sablon-etape.json) | Etapele standard si duratele de pornire |
| [data/prioritizare.json](data/prioritizare.json) | Ponderi, benzi si mecanisme de scor |
| [data/nomenclatoare.json](data/nomenclatoare.json) | Linii de productie, tipuri de documente, motive |

## Conventii de referinta

| Prefix | Inseamna |
|---|---|
| `TBL-nn` | Tabela Dataverse |
| `REL-nn` | Relatie intre tabele |
| `LIV-nn` | Livrabil de proiect din sablon |
| `ETP-nn` | Etapa de proiect |
| `FLX-nn` | Flux Power Automate |
| `ECR-nn` | Ecran de aplicatie |
| `ROL-nn` | Rol de securitate |
| `RSC-nn` | Risc |
| `CA-nn` | Criteriu de acceptanta |
| `DOC-nn` | Document generat din date |
| `PROPUNERE` | Element propus de arhitect, care nu exista in cerinta initiala |
| `NOTA` | Conflict intre cerinta din context si buna practica de platforma |
