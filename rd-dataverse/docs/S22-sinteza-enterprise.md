# Sectiunea 22 - Sinteza celor doua blueprinturi

Document de decizie. Explica ce s-a preluat din blueprintul "R&D Suite Enterprise", ce
s-a respins, ce contradictii au fost rezolvate si cum arata modelul tinta rezultat.

Se citeste inaintea oricarei constructii, pentru ca stabileste **ce se construieste si in
ce ordine**, nu doar ce ar fi frumos sa existe.

## 22.1 Ce este fiecare document

| Criteriu | Blueprintul de baza (S00-S21) | R&D Suite Enterprise |
|---|---|---|
| Natura | Model fizic construibil | Arhitectura tinta si inventar de ambitie |
| Tabele | 43, cu 676 de coloane tipate | 150 de nume de tabele |
| Coloane definite | 676, cu tip Dataverse, obligativitate, regula | 0 |
| Tipuri Dataverse mentionate | Toate | Niciunul |
| Relatii cu comportament la stergere | 68 | Nespecificate |
| Fisiere de import | 8 CSV gata de folosit | Niciunul |
| Efort declarat | 78-98 zile-om, cu ipoteza explicita | Nedeclarat |
| Orizont | 6-7 luni (ipoteza optimista, vezi 16.6.1) | 10-15 luni |
| Acoperire de proces | R&D end-to-end, de la SCP la revizuire | R&D plus finance, sustenabilitate, predictie, Copilot |

22.1.1 Documentul Enterprise recunoaste el insusi acest lucru: "Documentul nu inlocuieste
dictionarul fizic de date, matricea de securitate sau catalogul detaliat de flow-uri" si
se incheie anuntand ca urmatorul artefact necesar este chiar dictionarul fizic de date.

22.1.2 Concluzia nu este ca unul este bun si celalalt slab. Sunt doua artefacte diferite
din acelasi lant: **Enterprise defineste unde vrem sa ajungem, blueprintul de baza
defineste ce se poate construi luni.** Sinteza pastreaza ambele roluri, explicit separate.

## 22.2 Ce s-a preluat din Enterprise - lacune reale in blueprintul de baza

Cele 11 elemente de mai jos sunt adaugiri de fond, nu cosmetice. Fiecare acopera o lacuna
pe care blueprintul de baza o avea.

| Nr | Element preluat | Ce lipsea | Unde intra acum |
|---|---|---|---|
| 22.2.1 | **Gate-uri formale** cu criterii si decizii GO / GO CU CONDITII / HOLD / REWORK / STOP | Aveam statusuri si livrabile, dar nicio poarta care sa opreasca un proiect incomplet. Statusul se schimba pentru ca cineva il schimba | S23.1, TBL-43 ... TBL-46 |
| 22.2.2 | **Registru de riscuri** cu probabilitate, impact, detectabilitate si RPN | Aveam doar blocaje, adica evenimente deja produse. Nu exista notiunea de risc anticipat | S23.2, TBL-47 |
| 22.2.3 | **Registru de probleme**, separat de riscuri si de blocaje | Problemele traiau ca text liber in observatii sau in inregistrarile de productie 0 | S23.3, TBL-48 |
| 22.2.4 | **Tabela centrala de actiuni**, alimentata din risc, problema, gate, CAPA, reclamatie, productie 0 | Actiunile erau imprastiate in cinci locuri, fara vedere unica "ce am de facut" | S23.4, TBL-49 |
| 22.2.5 | **Jurnal de decizii**, cu context, alternative si autoritate | Deciziile se pierdeau. La sase luni nimeni nu mai stia de ce s-a ales varianta B | S23.5, TBL-50 |
| 22.2.6 | **Stabilizare cu regula celor trei loturi conforme** | Proiectul trecea direct din Productie 0 in Finalizat. In bakery, un singur lot reusit nu dovedeste repetabilitate | S24.1, TBL-51, TBL-52 |
| 22.2.7 | **Capabilitate de proces (Cp, Cpk)** | Calculam media, abaterea si CV, dar nu capabilitatea fata de limitele de specificatie | S24.2, TBL-53 |
| 22.2.8 | **Lectii invatate cu urmarirea reutilizarii** | Nu exista nimic. Cunoasterea ramanea in capul tehnologului | S25, TBL-54 ... TBL-56 |
| 22.2.9 | **Lead time inteligent**: contractual, declarat, media ultimelor 3 si 12 livrari, acuratetea ETA | Aveam o singura valoare de lead time asumat, care nu invata din istoric | S23.6, TBL-57 |
| 22.2.10 | **Protectie impotriva alert fatigue**: deduplicare, prag de 24 de ore, digest, amanare cu motiv | Aveam gruparea zilnica a notificarilor, dar nu un mecanism sistematic | S23.7 |
| 22.2.11 | **Scoruri compuse de sanatate** a proiectului si de succes la 90 de zile | Aveam indicele de sanatate al produsului (8.4), dar nimic la nivel de proiect in derulare | S24.3, TBL-58 |

22.2.12 Doua adaugiri tehnice minore, dar corecte, tot din Enterprise: **alternate keys**
pe codurile de business (cod proiect, cod SAP, cod livrabil), care fac importurile
idempotente; si **correlation id plus retry policy** pe fiecare flux, care fac
diagnosticarea posibila. Ambele intra in 22.6.

## 22.3 Ce s-a respins si de ce

Respingerea nu inseamna ca elementul e gresit. Inseamna ca nu intra acum, cu motivul
declarat si cu conditia in care ar intra.

| Element din Enterprise | Decizie | Motiv |
|---|---|---|
| Cele 150 de tabele ca tinta de constructie | **Respins ca plan** | Vezi 22.4. Pastrat ca backlog in Anexa A2, cu criterii de activare |
| Idea Management, Technology Scouting, TRL, Innovation Portfolio | Amanat | Compania are 130-180 de proiecte pe an venite din cereri comerciale, nu un pipeline de inovatie deschisa. Un modul de idei fara idei este un ecran gol care erodeaza increderea |
| Predictive Models, Project Predictions, Scenario Simulator | Amanat, cu conditie | Documentul Enterprise spune el insusi: se activeaza dupa 6-12 luni de date curate. Conditia de activare este in A2 |
| Copilot pe cele patru roluri | Amanat, cu conditie | Fara datele de la Val 1-3 nu are ce raspunde. Un Copilot care da raspunsuri gresite despre proiecte reale se dezactiveaza dupa o saptamana si nu se mai reactiveaza niciodata |
| Executive Digital Twin ca tabela | Respins ca tabela, pastrat ca ecran | `rdcdi_ProjectDigitalTwin` este o vizualizare agregata, nu date noi. O tabela care dubleaza date existente creeaza probleme de sincronizare |
| ProjectHealthSnapshot ca tabela separata plus scor calculat | Partial | Snapshot-ul intra (TBL-58), pentru ca tendinta in timp nu se poate reconstitui altfel. Restul scorurilor raman coloane calculate |
| Sustainability, Carbon Factor, ESG | Amanat | Documentul Enterprise recunoaste ca "datele sunt optionale pana cand exista o metoda interna validata". Fara metodologie aprobata, scorurile de mediu sunt un risc de reputatie, nu un beneficiu |
| Cost-to-Serve, TCO, Distribution Cost, Energy Cost, Maintenance Cost | Amanat | Depind de date din Controlling si Logistica pe care R&D nu le are si nu le poate cere lunar. Intra dupa ce revizuirea post-implementare demonstreaza ca fluxul de cost real functioneaza |
| Portfolio, Program, ProgramProject | Amanat | La un singur departament R&D cu un manager, portofoliul este o vizualizare filtrata, nu o ierarhie de obiecte |
| NPS, CSAT, CES ca module complete | Redus | Se pastreaza feedbackul de client legat de proiect si mostra (Val 4). Sondajele NPS periodice catre clienti sunt proces comercial, nu R&D, si se trimit de Sales |
| Separarea `rdcdi_Person` de `systemuser` | Respins | Dataverse are deja `systemuser`. O tabela paralela de persoane creeaza doua surse de adevar si probleme de securitate. Se pastreaza `rd_profiltehnolog`, care extinde, nu duplica |
| `rdcdi_Role`, `rdcdi_Department` ca tabele | Respins | Sunt Choice-uri. O tabela cu 10 randuri care nu au relatii proprii este overhead |

## 22.4 Problema de fond: efortul

22.4.1 Documentul Enterprise nu declara nicaieri efortul in zile-om. Este singura omisiune
grava din el, pentru ca de ea depinde daca planul e realizabil sau e fictiune.

22.4.2 Calculul, pornind de la datele masurate in blueprintul de baza:

| Element | Blueprint de baza | Enterprise | Sinteza |
|---|---|---|---|
| Tabele | 43 | 150 | 57 core + 13 extins |
| Efort estimat | 78-98 zile-om | 270-350 zile-om (extrapolat liniar) | 100-125 zile-om |
| La 1.5 zile pe saptamana | ~14 luni | ~45 luni | ~17 luni |
| La 3 zile pe saptamana | ~7 luni | ~22 luni | ~9 luni |

22.4.3 Extrapolarea liniara este chiar generoasa: efortul creste supraliniar cu numarul de
tabele, din cauza relatiilor, a formularelor si a testarii. 150 de tabele construite de o
singura persoana, fara echipa IT, in 10-15 luni, nu este un plan optimist. Este un plan
imposibil.

22.4.4 Documentul Enterprise stie asta. Propriul lui registru de riscuri contine
"Prea multe tabele construite prematur | Ridicat | Core first, advanced analytics
ulterior" si nota de rationalizare din 15.10: "Inventarul complet reprezinta tinta
enterprise. Nu toate tabelele se construiesc in primul val." Sinteza doar duce aceasta
observatie pana la capat si stabileste explicit unde este taietura.

22.4.5 **Regula care rezulta**: nicio tabela nu se construieste pentru ca apare intr-un
inventar. Se construieste cand exista un proces care o umple cu date si un om care le
citeste. Criteriile de activare pentru tot ce a fost amanat sunt in Anexa A2.

## 22.5 Contradictii rezolvate

Cele doua documente se contrazic in cinci puncte. Fiecare are o decizie, cu motiv.

### 22.5.1 Documentele in SharePoint - contradictie cu briefingul initial

| Sursa | Ce spune |
|---|---|
| Briefingul initial, decizia de arhitectura 4 | "Documentele raman in SharePoint, un folder per proiect, legat de inregistrarea de proiect prin integrarea nativa de documente." Marcata explicit "nu se renegociaza" |
| Enterprise, 0.1 punctul 2 si capitolul 13.1 | "Documentele existente din OneDrive si SharePoint nu sunt modificate automat de solutie. Legatura cu acestea ramane optionala si se face ulterior" |

**Decizie: se pastreaza varianta din briefingul initial.** Generarea automata a arborelui
de foldere si legarea nativa raman in Val 1, ca in Sectiunea 5.

Motiv: este o decizie de arhitectura declarata nenegociabila de catre beneficiar, iar
argumentul din spatele ei este solid - fara folder generat automat, structura pe faze nu
se aplica niciodata consecvent, si exact asta e problema din situatia actuala. Un registru
de documente fara automatizarea folderului reproduce problema de azi intr-o baza de date
mai frumoasa.

**Ce se preia totusi din Enterprise**: registrul tehnic de documente cu ciclu de viata
(Draft, In Review, Pending Approval, Approved, Effective, Superseded, Archived, Obsolete)
si harta de dependente intre documente, care spune ce trebuie revizuit cand se schimba ST
finala. Acestea completeaza Sectiunea 5, nu o inlocuiesc. Intra in Val 3.

### 22.5.2 Prefixul de editor

| Sursa | Prefix |
|---|---|
| Blueprint de baza | `rd_` |
| Enterprise | `rdcdi_` |

**Decizie: `rd_`.**

Motiv: prefixul apare in fiecare dintre cele 676 de nume de coloane deja definite, in cele
8 fisiere de import si in numele fiecarei relatii. `rdcdi_` adauga trei caractere la
fiecare nume logic, fara niciun castig de claritate - solutia este oricum una singura.
Mai important: prefixul nu se mai poate schimba dupa primul export de solutie (2.0.1),
deci decizia trebuie luata acum si o singura data.

### 22.5.3 Banda de prioritate P3 / P4

| Sursa | P3 | P4 |
|---|---|---|
| Blueprint de baza | 35-59 | sub 35 |
| Enterprise | 40-59 | sub 40 |

**Decizie: 35-59 si sub 35.** Diferenta este nesemnificativa tehnic, dar pragul mai jos
lasa mai mult loc mecanismului de imbatranire din A1.1.9 sa scoata proiectele mici din
coada. Valoarea este oricum variabila de mediu si se recalibreaza la un an.

### 22.5.4 Grila senzoriala

| Sursa | Structura |
|---|---|
| Blueprint de baza | Doua grile pe categorie de produs (foietaj, aluat dospit), 17 criterii cu ancore descriptive complete pentru 1, 3 si 5 |
| Enterprise | O grila unica: aspect exterior 15, interior si alveolare 20, miros 10, gust 30, textura 20, aftertaste 5 |

**Decizie: se pastreaza grilele pe categorie**, dar se preia din Enterprise criteriul
**aftertaste**, care lipsea si care conteaza la produsele cu umplutura si cu grasimi.

Motiv: o grila unica pentru foietaj si pentru paine masoara lucruri diferite cu aceeasi
rigla. Ponderea de 30% pe gust este defensabila comercial, dar la un croissant congelat
foietarea decide reclamatia, nu gustul. Ancorele descriptive sunt partea care face grila
utilizabila de doi oameni diferiti si nu se poate renunta la ele.

### 22.5.5 Dimensiunea esantionului

| Sursa | Greutate |
|---|---|
| Blueprint de baza | 10 la trial, 20 la productia 0, in 4 prelevari |
| Enterprise | minimum 5, preferabil 10 la productia 0 |

**Decizie: se pastreaza pragurile mai stranse din blueprintul de baza.** La n=5, abaterea
standard este prea instabila ca sa sustina o decizie de conformitate, iar gramajul are
consecinta legala. Pragul de 20 la productia 0 se recalibreaza dupa primele 10 productii 0
reale (IQ-08).

## 22.6 Elementele tehnice adaugate

Trei practici din Enterprise care nu erau in blueprintul de baza si care se adopta ca
standard, pentru toate tabelele si fluxurile:

| Practica | Ce inseamna concret | Unde se aplica |
|---|---|---|
| **Alternate keys** | Cheie alternativa pe codurile de business: `rd_codproiect` pe proiect, `rd_codsap` pe materie prima si client, `rd_codlivrabil` plus proiect pe livrabil | Face importurile si upsert-urile idempotente. Fara ele, un import rulat de doua ori creeaza duplicate |
| **Correlation ID pe fluxuri** | Fiecare executie de flux scrie un identificator unic in log si in inregistrarile pe care le atinge | Fara el, la un lant de 4 fluxuri nu se poate spune care executie a produs ce |
| **Retry policy si error log explicit** | Politica de reincercare configurata pe fiecare actiune care atinge un serviciu extern, plus o tabela de log de erori | Completeaza tratarea de eroare din 12.1.3, care trimitea doar notificare |

22.6.1 Se adauga tabela tehnica `rd_logeroare` (TBL-59): flux, correlation id, data,
inregistrare afectata, mesaj, numar de reincercari, status. Este singura tabela din
sinteza care nu are valoare de business directa, dar fara ea intretinerea unei solutii cu
25 de fluxuri devine ghicitoare.

## 22.7 Modelul tinta rezultat

### 22.7.1 Cele trei niveluri

| Nivel | Tabele | Cand | Criteriu de existenta |
|---|---|---|---|
| **Core** | 57 | Val 0-3, lunile 1-9 | Fara ele procesul R&D nu functioneaza digital |
| **Extins** | 13 | Val 4-5, lunile 9-15 | Se activeaza cand procesul core produce date consecvent |
| **Amanat** | ~80 din inventarul Enterprise | Dupa Val 5, cu criterii de activare | Vezi Anexa A2 |

### 22.7.2 Cele 14 tabele noi din Core, fata de blueprintul de baza

| Cod | Tabela | Domeniu | Val | Sursa |
|---|---|---|---|---|
| TBL-43 | `rd_sablongate` | Gate-uri | 1 | Enterprise |
| TBL-44 | `rd_criteriugate` | Gate-uri | 1 | Enterprise |
| TBL-45 | `rd_gate` | Gate-uri | 1 | Enterprise |
| TBL-46 | `rd_verificaregate` | Gate-uri | 1 | Enterprise |
| TBL-47 | `rd_risc` | Guvernanta | 2 | Enterprise |
| TBL-48 | `rd_problema` | Guvernanta | 2 | Enterprise |
| TBL-49 | `rd_actiune` | Guvernanta | 1 | Enterprise |
| TBL-50 | `rd_decizie` | Guvernanta | 2 | Enterprise |
| TBL-51 | `rd_stabilizare` | Industrializare | 3 | Enterprise |
| TBL-52 | `rd_lotstabilizare` | Industrializare | 3 | Enterprise |
| TBL-53 | `rd_capabilitateproces` | Industrializare | 3 | Enterprise |
| TBL-54 | `rd_lectie` | Cunoastere | 3 | Enterprise |
| TBL-55 | `rd_utilizarelectie` | Cunoastere | 3 | Enterprise |
| TBL-56 | `rd_recomandarelectie` | Cunoastere | 3 | Enterprise |
| TBL-57 | `rd_leadtimeistoric` | Supply | 2 | Enterprise |
| TBL-58 | `rd_snapshotsanatate` | Guvernanta | 3 | Enterprise |
| TBL-59 | `rd_logeroare` | Tehnic | 1 | Enterprise |

Sunt 17 coduri pentru 14 concepte, pentru ca gate-urile si lectiile cer fiecare mai multe
tabele.

### 22.7.3 Cele 13 tabele din nivelul Extins (Val 4-5)

`rd_feedbackclient`, `rd_validareclient`, `rd_reclamatie`, `rd_neconformitate`, `rd_capa`,
`rd_performantafurnizor`, `rd_incidentfurnizor`, `rd_businesscase`, `rd_bugetproiect`,
`rd_costproductie`, `rd_giveaway`, `rd_beneficiu`, `rd_documenttehnic`.

Definitiile lor sunt in Sectiunea 26. Nu se construiesc pana cand criteriile din A2.2 nu
sunt indeplinite.

## 22.8 Ce se schimba in roadmap

22.8.1 Structura trece de la 4 valuri la 6, dar **primele patru raman neschimbate ca
domeniu**. Nu se adauga nimic in Val 0-1: acolo termenul este ferm si orice adaugire
omoara livrarea.

| Val | Blueprint de baza | Sinteza | Diferenta |
|---|---|---|---|
| Val 0 | Fundatie | Fundatie, plus `rd_logeroare` si alternate keys | Neschimbat ca domeniu |
| Val 1 | MVP 30 de zile | MVP, plus gate-uri si tabela de actiuni | +4 tabele, +3 zile-om |
| Val 2 | Operare completa | Operare, plus riscuri, probleme, decizii, lead time istoric | +4 tabele, +5 zile-om |
| Val 3 | Maturitate | Maturitate, plus stabilizare, capabilitate, lectii, snapshot | +6 tabele, +8 zile-om |
| Val 4 | - | Client, furnizor, neconformitati si CAPA | Nou |
| Val 5 | - | Cost real, beneficii, registru de documente | Nou |

22.8.2 Gate-urile intra in Val 1, desi sunt o adaugire, pentru un motiv precis: sunt
mecanismul care face livrabilele obligatorii sa conteze. Fara gate, un proiect trece mai
departe pentru ca cineva ii schimba statusul. Costul lor este mic (4 tabele simple,
majoritatea sabloane), iar beneficiul este exact cel pentru care se construieste sistemul.

22.8.3 Tabela de actiuni intra tot in Val 1, pentru ca fiecare modul construit ulterior ar
crea altfel propriul mecanism de actiuni, si consolidarea ulterioara ar insemna migrarea a
cinci structuri diferite.

22.8.4 Roadmap-ul actualizat, cu efortul recalculat, este in Sectiunea 16, revizuita.

## 22.9 Ce ramane valabil fara modificare din blueprintul de baza

Ca sa fie clar ce **nu** s-a schimbat:

- modelul de date de baza, cele 43 de tabele cu 676 de coloane;
- sablonul de 43 de livrabile si maparea lui pe cele 22 de coloane-bifa din centralizator;
- structura documentatiei pe faze, cu generarea automata a folderelor;
- algoritmul scorului de prioritate si al termenului propus (Anexa A1);
- grilele senzoriale pe categorie, cu ancore;
- setul de inregistrari de la productia 0;
- calculul alergenilor si al valorilor nutritionale din reteta;
- matricea de securitate Rol x Tabela;
- cele 8 fisiere de import si ghidul Valului 0.

22.9.1 Sinteza este aditiva. Nimic din ce era construibil nu s-a pierdut, iar ghidul
Valului 0 ramane valabil ca atare, cu o singura completare: alternate keys si tabela de
log de erori.
