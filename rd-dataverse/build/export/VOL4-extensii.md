# Volumul 4 - Sinteza Enterprise, extensii si operare

Parte din blueprintul Suitei Digitale R&D, export din 09.09.2026.
Contine sectiunile: S22-sinteza-enterprise, S23-guvernanta-proiect, S24-stabilizare-capabilitate, S25-cunoastere, S26-constructie-asistata, S27-unde-traieste-ce, S28-acces-si-licentiere, A2-backlog-enterprise.

Contextul complet al proiectului este in preambulul din `BLUEPRINT-COMPLET.md`.



<!-- ==================== S22-sinteza-enterprise.md ==================== -->

---

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


<!-- ==================== S23-guvernanta-proiect.md ==================== -->

---

# Sectiunea 23 - Guvernanta de proiect

Stratul preluat din blueprintul Enterprise (vezi 22.2): gate-uri formale, registru de
riscuri, registru de probleme, actiuni centralizate, jurnal de decizii, lead time
inteligent si protectie impotriva alert fatigue.

Formatul coloanelor este cel din Sectiunea 2. Definitiile prelucrabile sunt in
`data/tabele.json`.

## 23.1 Gate-uri

### 23.1.1 De ce

Blueprintul de baza avea statusuri (2.2.1) si livrabile obligatorii (4.3), dar tranzitia
intre ele se facea pentru ca cineva schimba un camp. Livrabilul obligatoriu bloca doar
inchiderea proiectului, la sfarsit, cand costul de a te intoarce este maxim.

Gate-ul muta verificarea la momentul potrivit: **inainte de a consuma resursa urmatoare**.
Nu se cumpara materie prima daca reteta nu e candidata; nu se intra pe linie daca fabrica
nu e pregatita.

### 23.1.2 Cele 9 gate-uri

| Cod | Gate | Dupa etapa | Intreaba | Cine decide |
|---|---|---|---|---|
| G0 | SCP acceptat | S00 Solicitare | Cererea este completa si merita evaluata? | Manager R&D |
| G1 | Concept si plan aprobate | S20 Planificare | Stim ce facem, cine si pana cand? | Manager R&D |
| G2 | Materii prime fezabile | S30 Aprovizionare | Materialele exista, la un pret si un termen acceptabile? | Manager R&D + Achizitii |
| G3 | Reteta si trial validate | S40-S50 Dezvoltare si validare | Produsul functioneaza tehnic si senzorial? | Manager R&D |
| G4 | Cost si comercial aprobate | S60 Fezabilitate economica | Are marja la pretul discutat? | Manager R&D + Comercial |
| G5 | Factory Ready | S80 Implementare | Fabrica poate produce maine dimineata? | Productie + Calitate |
| G6 | Productie 0 validata | S90 Productie 0 | Produsul s-a facut in conditii reale? | Manager R&D + Calitate |
| G7 | Stabilizare si release | S100 Stabilizare | Se face repetat, nu o singura data? | Manager R&D + Productie |
| G8 | Post-review si inchidere | S110-S120 | A livrat ce a promis? | Head of R&D |

23.1.3 Maparea pe etapele existente din 14.2: G0 dupa ETP-01, G1 dupa ETP-02, G2 dupa
ETP-03, G3 dupa ETP-06, G4 dupa ETP-04 si antecalcul aprobat, G5 dupa ETP-09, G6 dupa
ETP-10, G7 dupa stabilizare, G8 dupa ETP-11 si revizuirea de 90 de zile.

NOTA: blueprintul Enterprise propune 13 etape (S00-S120), fata de cele 11 din 14.2.
Diferenta reala este o singura etapa noua - **stabilizarea** - plus separarea validarii de
dezvoltare. Se adauga ETP-12 Stabilizare, dupa ETP-10, si se lasa restul neschimbat.
Renumerotarea completa a etapelor ar invalida sablonul deja importat, fara castig.

### 23.1.4 Deciziile de gate

| Decizie | Ce inseamna | Efect |
|---|---|---|
| GO | Toate criteriile indeplinite | Proiectul trece la etapa urmatoare |
| GO CU CONDITII | Criterii minore neindeplinite | Trece, dar se creeaza obligatoriu actiuni cu proprietar si termen (23.4). Fara actiuni, decizia nu se poate salva |
| HOLD | Se asteapta ceva extern | Proiectul se opreste, se creeaza blocaj (TBL-11), ceasul T-Total se opreste |
| REWORK | Criterii majore neindeplinite | Se intoarce in etapa anterioara, cu motiv. Se incrementeaza contorul de rework |
| STOP | Proiectul nu mai are sens | Proiectul trece in Abandonat, cu motiv obligatoriu |

23.1.5 Un gate nu poate primi GO daca exista un risc cu RPN peste prag sau o problema
critica deschisa, cu exceptia unei derogari documentate si aprobate de autoritatea
stabilita. Derogarea se inregistreaza pe gate, nu intr-un mail.

### 23.1.6 TBL-43 `rd_sablongate`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (100) | Da | - | - | Coloana primara |
| Cod gate | rd_codgate | Text (10) | Da | G0 ... G8 | Unic | Alternate key |
| Ordine | rd_ordine | Whole Number | Da | 0 - 20 | - | - |
| Etapa asociata | rd_sablonetapa | Lookup (rd_sablonetapa) | Da | - | Gate-ul se evalueaza la iesirea din etapa | - |
| Tip proiect | rd_tipproiect | Choice (multi) | Da | Choice TIPPROIECT | Nu toate gate-urile se aplica la toate tipurile | Vezi 23.1.9 |
| Rol decident | rd_roldecident | Choice | Da | Choice ROL | - | - |
| Rol coaprobator | rd_rolcoaprobator | Choice | Nu | Choice ROL | Unele gate-uri cer doua semnaturi | G2, G4, G5, G6, G7 |
| Blocheaza avansarea | rd_blocheaza | Yes/No | Da | Implicit Da | Nu = gate informativ | - |
| Permite GO cu conditii | rd_permiteconditii | Yes/No | Da | Implicit Da | G5 si G6 = Nu | Vezi 23.1.8 |
| Prag RPN blocant | rd_pragrpn | Whole Number | Nu | 1 - 125 | Riscul peste acest RPN blocheaza GO | Implicit 48 |
| Activ | rd_activ | Yes/No | Da | - | - | - |

### 23.1.7 TBL-44 `rd_criteriugate`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire criteriu | rd_name | Text (200) | Da | - | - | Coloana primara |
| Cod | rd_cod | Text (15) | Da | G0-01, G0-02 ... | Unic | - |
| Sablon gate | rd_sablongate | Lookup (rd_sablongate) | Da | - | Parental | Cascade All |
| Ordine | rd_ordine | Whole Number | Da | 1 - 30 | - | - |
| Tip verificare | rd_tipverificare | Choice | Da | Automata / Manuala / Mixta | Vezi 23.1.10 | - |
| Sursa verificarii automate | rd_sursaauto | Text (200) | Nu | - | Obligatorie daca tip = Automata | Livrabil, camp sau agregare |
| Livrabil legat | rd_codlivrabil | Text (10) | Nu | LIV-nn | Criteriul verifica un livrabil anume | - |
| Obligatoriu pentru GO | rd_obligatoriu | Yes/No | Da | Implicit Da | Nu = criteriu de atentionare | - |
| Sever | rd_sever | Yes/No | Da | Implicit Nu | Da = nu admite GO cu conditii | - |
| Rol responsabil | rd_rolresponsabil | Choice | Da | Choice ROL | - | - |
| Activ | rd_activ | Yes/No | Da | - | - | - |

### 23.1.8 TBL-45 `rd_gate`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {cod proiect}_{cod gate} | Generata | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Sablon gate | rd_sablongate | Lookup (rd_sablongate) | Da | - | - | - |
| Etapa | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | - |
| Data planificata | rd_dataplanificata | Date Only | Da | - | Din data de final a etapei | - |
| Data evaluarii | rd_dataevaluare | Date and Time | Nu | - | Automata la salvarea deciziei | - |
| Status gate | rd_statusgate | Choice | Da | Neevaluat / In pregatire / Gata de evaluare / Evaluat / Sarit | Gata de evaluare cand toate criteriile automate sunt indeplinite | Scris de FLX-23 |
| Decizie | rd_decizie | Choice | Nu | GO / GO cu conditii / HOLD / REWORK / STOP | Vezi 23.1.4 | Choice global DECIZIEGATE |
| Decident | rd_decident | Lookup (systemuser) | Nu | - | Trebuie sa aiba rolul din sablon | Business rule |
| Coaprobator | rd_coaprobator | Lookup (systemuser) | Nu | - | Obligatoriu daca sablonul cere | - |
| Criterii indeplinite | rd_criteriiok | Whole Number | Nu | 0 - 30 | Rollup pe verificari | - |
| Criterii totale aplicabile | rd_criteriitotal | Whole Number | Nu | 0 - 30 | - | - |
| Procent pregatire | rd_procentpregatire | Decimal (2) | Nu | 0 - 100 | indeplinite / total x 100 | Afisat ca bara |
| Motivul deciziei | rd_motivdecizie | Text Area (2000) | Nu | - | Obligatoriu pentru tot ce nu e GO | Business rule |
| Numar actiuni deschise | rd_actiunideschise | Rollup (Count) | Nu | - | Din rd_actiune legate de gate | GO cu conditii cere minimum 1 |
| Derogare acordata | rd_derogare | Yes/No | Da | Implicit Nu | Permite GO peste un risc blocant | Vezi 23.1.5 |
| Motivul derogarii | rd_motivderogare | Text Area (2000) | Nu | - | Obligatoriu daca derogare = Da | Auditat |
| Aprobator derogare | rd_aprobatorderogare | Lookup (systemuser) | Nu | - | Obligatoriu daca derogare = Da | Head of R&D |
| Numar reveniri | rd_numarreveniri | Whole Number | Nu | 0 - 20 | Incrementat la fiecare REWORK | Indicator de calitate |
| Zile in gate | rd_zileingate | Whole Number | Nu | 0 - 999 | Data evaluarii - data planificata | Masoara birocratia |

### 23.1.9 TBL-46 `rd_verificaregate`

Instanta unui criteriu pe un gate concret.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | Din criteriu | Coloana primara |
| Gate | rd_gate | Lookup (rd_gate) | Da | - | Parental | Cascade All |
| Criteriu | rd_criteriu | Lookup (rd_criteriugate) | Da | - | - | - |
| Rezultat | rd_rezultat | Choice | Da | Neverificat / Indeplinit / Neindeplinit / Nu se aplica | Implicit Neverificat | - |
| Verificat automat | rd_automat | Yes/No | Da | - | Din tipul criteriului | - |
| Data verificarii | rd_dataverificare | Date and Time | Nu | - | - | - |
| Verificat de | rd_verificatde | Lookup (systemuser) | Nu | - | Gol pentru verificarile automate | - |
| Observatii | rd_observatii | Text Area (1000) | Nu | - | Obligatorii daca rezultat = Neindeplinit | - |
| Actiune generata | rd_actiune | Lookup (rd_actiune) | Nu | - | Referential | Vezi 23.4 |

23.1.10 **Verificarile automate** sunt cele care se pot citi din date, fara ca cineva sa
bifeze. Exemple: "ST finala aprobata" citeste statusul din TBL-29; "toate materiile prime
critice receptionate" numara in TBL-07; "cel putin un trial cu rezultat Reusit" numara in
TBL-15; "marja peste prag" citeste din TBL-22. FLX-23 le reevalueaza la fiecare modificare
relevanta si actualizeaza procentul de pregatire al gate-ului.

23.1.11 Efectul practic: **ecranul de gate arata in orice moment cat mai lipseste pana se
poate trece mai departe, si cine datoreaza fiecare element**. Este raspunsul la intrebarea
"de ce sta proiectul asta", pusa in fiecare sedinta de R&D.

## 23.2 Registrul de riscuri

### 23.2.1 Riscul fata de blocaj fata de problema

| Obiect | Definitie | Timp | Tabela |
|---|---|---|---|
| Risc | Eveniment posibil, care nu s-a produs | Viitor | TBL-47 |
| Problema | Eveniment produs, care cere rezolvare | Prezent | TBL-48 |
| Blocaj | Perioada in care progresul este oprit din cauza externa | Interval | TBL-11 |

23.2.2 Distinctia nu e academica. Riscul se mitigheaza inainte si costa putin; problema se
rezolva dupa si costa mult; blocajul se masoara si opreste ceasul. Confundarea lor este
motivul pentru care, azi, intarzierile nu se pot explica la analiza anuala.

### 23.2.3 TBL-47 `rd_risc`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar risc | rd_name | Autonumber | Da | RSK-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Etapa detectarii | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | Cand a fost vazut |
| Titlu | rd_titlu | Text (200) | Da | - | - | - |
| Descriere | rd_descriere | Text Area (2000) | Da | - | - | - |
| Categorie | rd_categorie | Choice | Da | Tehnic / Reteta / Materie prima / Furnizor / Calitate / Siguranta alimentelor / Reglementare / Etichetare / Ambalaj / Client / Comercial / Financiar / Productie / Planificare / Logistica / SAP | - | Choice global CATEGORIERISC |
| Probabilitate | rd_probabilitate | Whole Number | Da | 1 - 5 | Vezi 23.2.4 | - |
| Impact | rd_impact | Whole Number | Da | 1 - 5 | Vezi 23.2.4 | - |
| Detectabilitate | rd_detectabilitate | Whole Number | Da | 1 - 5 | 1 = se vede imediat, 5 = se afla tarziu | - |
| RPN | rd_rpn | Calculated (Whole Number) | Nu | 1 - 125 | probabilitate x impact x detectabilitate | Vezi 23.2.5 |
| Nivel de risc | rd_nivel | Choice | Nu | Scazut / Mediu / Ridicat / Critic | Derivat din RPN | Scris de flux |
| Impact estimat in zile | rd_impactzile | Whole Number | Nu | 0 - 365 | - | Pentru termenul forecast |
| Expunere financiara | rd_expunere | Currency (2) | Nu | - | Optionala, vezi 23.2.7 | Securitate pe coloana |
| Afecteaza siguranta alimentelor | rd_afecteazafoodsafety | Yes/No | Da | Implicit Nu | Da = nivel Critic automat | Blocheaza gate |
| Afecteaza clientul | rd_afecteazaclient | Yes/No | Da | Implicit Nu | - | - |
| Afecteaza conformitatea | rd_afecteazaconformitate | Yes/No | Da | Implicit Nu | IFS, ISO, legal | - |
| Semnal de declansare | rd_trigger | Text (500) | Nu | - | Ce anume ar arata ca riscul se produce | Face riscul urmaribil |
| Plan de mitigare | rd_mitigare | Text Area (2000) | Nu | - | Obligatoriu pentru nivel Ridicat si Critic | Business rule |
| Plan de contingenta | rd_contingenta | Text Area (2000) | Nu | - | Ce facem daca se produce totusi | - |
| Proprietar | rd_proprietar | Lookup (systemuser) | Da | - | - | O persoana, nu un departament |
| Termen de mitigare | rd_termen | Date Only | Nu | - | Obligatoriu pentru nivel Ridicat si Critic | - |
| Probabilitate reziduala | rd_probabilitatereziduala | Whole Number | Nu | 1 - 5 | Dupa mitigare | - |
| Impact rezidual | rd_impactrezidual | Whole Number | Nu | 1 - 5 | Dupa mitigare | - |
| RPN rezidual | rd_rpnrezidual | Whole Number | Nu | 1 - 125 | - | Ce ramane asumat |
| Status | rd_statusrisc | Choice | Da | Identificat / In evaluare / In mitigare / Mitigat / Acceptat / Produs / Inchis | Produs = se creeaza problema | Vezi 23.2.6 |
| Tendinta | rd_tendinta | Choice | Nu | In crestere / Stabil / In scadere | Comparat cu ultima revizuire | - |
| Problema generata | rd_problema | Lookup (rd_problema) | Nu | - | Se completeaza cand riscul se produce | Trasabilitate |
| Data ultimei revizuiri | rd_dataultimarevizuire | Date Only | Nu | - | Riscurile Ridicat si Critic se revizuiesc lunar | FLX-24 |

### 23.2.4 Scalele

**Probabilitate**: 1 = foarte putin probabil, sub 10%; 2 = putin probabil, 10-30%;
3 = posibil, 30-50%; 4 = probabil, 50-80%; 5 = aproape sigur, peste 80%.

**Impact**: 1 = fara efect asupra termenului sau costului; 2 = intarziere sub 3 zile sau
cost sub 1% din proiect; 3 = intarziere 3-10 zile sau cost 1-5%; 4 = intarziere 10-30 de
zile, cost 5-15%, sau reclamatie de client; 5 = proiectul esueaza, produsul nu se poate
lansa, sau exista risc de siguranta alimentelor.

**Detectabilitate**: 1 = se vede imediat, prin control existent; 3 = se vede la controlul
urmator; 5 = se afla abia la client sau in productie de serie.

### 23.2.5 Pragurile RPN

| Nivel | RPN | Ce se cere |
|---|---|---|
| Scazut | 1 - 15 | Se inregistreaza, se monitorizeaza |
| Mediu | 16 - 47 | Plan de mitigare recomandat |
| Ridicat | 48 - 79 | Plan de mitigare si termen obligatorii; blocheaza GO fara derogare |
| Critic | 80 - 125 | Idem, plus escaladare la Head of R&D si revizuire saptamanala |

23.2.5.1 PROPUNERE: pragul de 48 pentru "blocheaza gate-ul" corespunde unei combinatii de
tipul probabil (4) x impact mare (4) x detectabilitate medie (3). Este configurabil pe
sablonul de gate (`rd_pragrpn`), ca sa poata fi mai strict la G5 si G6, unde consecinta
este productia reala.

23.2.5.2 Orice risc cu `rd_afecteazafoodsafety = Da` devine automat Critic, indiferent de
RPN. Siguranta alimentelor nu se negociaza cu o formula.

### 23.2.6 Cand riscul se produce

Statusul `Produs` declanseaza FLX-25: se creeaza automat o problema (TBL-48), precompletata
din risc, cu legatura in ambele sensuri. Riscul nu se sterge si nu se inchide - ramane
inregistrat ca risc care s-a materializat, pentru ca rata de materializare este un
indicator de calitate a evaluarii de risc.

### 23.2.7 Nota despre expunerea financiara

Campul este optional, deliberat. Documentul Enterprise observa corect: "Campurile
financiare din proiect raman optionale atunci cand datele nu sunt disponibile, pentru a
evita completarea fictiva." Un camp obligatoriu pe care nimeni nu-l poate estima produce
cifre inventate, iar cifrele inventate ajung in rapoarte.

## 23.3 Registrul de probleme

### 23.3.1 TBL-48 `rd_problema`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar problema | rd_name | Autonumber | Da | ISS-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Etapa | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | - |
| Titlu | rd_titlu | Text (200) | Da | - | - | - |
| Descriere | rd_descriere | Text Area (2000) | Da | - | - | - |
| Sursa | rd_sursa | Choice | Da | Trial / Materie prima / Furnizor / Productie 0 / Client / Calitate / Reclamatie / Audit / Risc materializat / Alta | - | - |
| Categorie | rd_categorie | Choice | Da | Choice CATEGORIERISC | Aceleasi categorii ca la risc | Permite analiza comuna |
| Severitate | rd_severitate | Choice | Da | Minora / Majora / Critica / Blocanta | Critica si Blocanta blocheaza gate | - |
| Impact asupra termenului (zile) | rd_impacttermen | Whole Number | Nu | 0 - 365 | - | - |
| Impact asupra costului | rd_impactcost | Currency (2) | Nu | - | Optional | Securitate pe coloana |
| Impact asupra calitatii | rd_impactcalitate | Yes/No | Da | Implicit Nu | - | - |
| Impact asupra clientului | rd_impactclient | Yes/No | Da | Implicit Nu | - | - |
| Siguranta alimentelor | rd_foodsafety | Yes/No | Da | Implicit Nu | Da = severitate Critica automat | Declanseaza neconformitate |
| Cauza radacina | rd_cauzaradacina | Text Area (2000) | Nu | - | Obligatorie la inchidere pentru Critica si Blocanta | Business rule |
| Metoda de analiza | rd_metodaanaliza | Choice | Nu | 5 De ce / Ishikawa / Experienta / Altele | - | - |
| Actiune corectiva | rd_actiunecorectiva | Text Area (2000) | Nu | - | Ce rezolva problema acum | - |
| Actiune preventiva | rd_actiunepreventiva | Text Area (2000) | Nu | - | Ce impiedica repetarea | - |
| Proprietar | rd_proprietar | Lookup (systemuser) | Da | - | - | - |
| Termen | rd_termen | Date Only | Nu | - | Obligatoriu pentru Critica si Blocanta | - |
| Status | rd_statusproblema | Choice | Da | Deschisa / In analiza / In rezolvare / Rezolvata / Verificata / Inchisa / Reaparuta | - | - |
| Data deschiderii | rd_datadeschidere | Date Only | Da | - | Implicit azi | - |
| Data inchiderii | rd_datainchidere | Date Only | Nu | - | - | - |
| Zile deschisa | rd_ziledeschisa | Whole Number | Nu | 0 - 999 | - | Scris de flux |
| Risc sursa | rd_risc | Lookup (rd_risc) | Nu | - | Daca provine dintr-un risc materializat | - |
| Trial legat | rd_trial | Lookup (rd_trial) | Nu | - | Referential | - |
| Materie prima legata | rd_mpproiect | Lookup (rd_mpproiect) | Nu | - | Referential | - |
| Productie 0 legata | rd_productie0 | Lookup (rd_productie0) | Nu | - | Referential | - |
| Lectie generata | rd_lectie | Lookup (rd_lectie) | Nu | - | Vezi 25.2 | - |
| Repetare | rd_esterepetare | Yes/No | Da | Implicit Nu | Aceeasi cauza in ultimele 12 luni | Scris de FLX-26 |

23.3.2 Problemele cu `rd_esterepetare = Da` de trei ori in 12 luni declanseaza automat un
draft de lectie invatata (25.2.2). Este mecanismul prin care sistemul observa ce oamenii
nu mai observa.

## 23.4 Actiuni centralizate

### 23.4.1 De ce o singura tabela

In blueprintul de baza, actiunile existau in trei locuri: inregistrarile de productie 0
(2.19), revizuirea post-implementare (2.20) si campul de actiuni al evaluarii senzoriale
(2.11.1). Fiecare cu propriile campuri, niciuna cu vedere de ansamblu.

O tabela centrala raspunde la intrebarea pe care fiecare o are luni dimineata: **ce am eu
de facut, in toate proiectele, sortat dupa termen.**

### 23.4.2 TBL-49 `rd_actiune`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar actiune | rd_name | Autonumber | Da | ACT-{AA}-{SEQ:00000} | - | Coloana primara |
| Titlu | rd_titlu | Text (200) | Da | - | - | - |
| Descriere | rd_descriere | Text Area (2000) | Nu | - | - | - |
| Proiect | rd_proiect | Lookup (rd_proiect) | Nu | - | Referential; poate fi si actiune fara proiect | Remove Link |
| Sursa | rd_sursaactiune | Choice | Da | Risc / Problema / Conditie de gate / Productie 0 / Revizuire / Evaluare senzoriala / Neconformitate / CAPA / Audit / Reclamatie / Incident furnizor / Decizie de sedinta / Manuala | - | Choice global SURSAACTIUNE |
| Risc | rd_risc | Lookup (rd_risc) | Nu | - | Completat de flux | - |
| Problema | rd_problema | Lookup (rd_problema) | Nu | - | Completat de flux | - |
| Gate | rd_gate | Lookup (rd_gate) | Nu | - | Pentru GO cu conditii | - |
| Productie 0 | rd_productie0 | Lookup (rd_productie0) | Nu | - | - | - |
| Prioritate | rd_prioritate | Choice | Da | Scazuta / Normala / Ridicata / Urgenta | Implicit Normala | - |
| Proprietar | rd_proprietar | Lookup (systemuser) | Da | - | O persoana | - |
| Termen | rd_termen | Date Only | Da | - | - | - |
| Status | rd_statusactiune | Choice | Da | Deschisa / In lucru / In verificare / Inchisa / Anulata | - | - |
| Data inchiderii | rd_datainchidere | Date Only | Nu | - | - | - |
| Zile intarziere | rd_zileintarziere | Whole Number | Nu | 0 - 999 | max(0, azi - termen) daca nu e inchisa | Scris de FLX-08 |
| Dovada | rd_dovada | Text Area (1000) | Nu | - | Obligatorie la inchidere pentru sursele Gate, CAPA si Neconformitate | Business rule |
| Verificator | rd_verificator | Lookup (systemuser) | Nu | - | Cine confirma ca s-a facut | - |
| Data verificarii | rd_dataverificare | Date Only | Nu | - | - | - |
| Eficacitate | rd_eficacitate | Choice | Nu | Eficace / Partial eficace / Neeficace / Prea devreme pentru evaluare | Se evalueaza la 30 de zile de la inchidere | Cerinta IFS pentru CAPA |
| Blocheaza gate | rd_blocheazagate | Yes/No | Da | Implicit Nu | Da = gate-ul nu poate trece pana la inchidere | - |
| Escaladata | rd_escaladata | Yes/No | Da | Implicit Nu | Scris de FLX-27 | - |
| Nivel escaladare | rd_nivelescaladare | Whole Number | Nu | 0 - 4 | Vezi 23.7.3 | - |

23.4.3 Ecranul `Actiunile mele` din aplicatia model-driven este singura vizualizare pe
care un utilizator o vede zilnic. Contine actiunile proprii, sortate dupa termen, cu
sursa si proiectul vizibile, si permite inchiderea din grila.

## 23.5 Jurnalul de decizii

### 23.5.1 De ce

Peste sase luni, cand cineva intreaba de ce produsul are 82 g si nu 80, sau de ce s-a ales
furnizorul B desi era mai scump, raspunsul exista azi doar in memoria a doua persoane.
Jurnalul de decizii costa doua minute pe decizie si raspunde definitiv.

### 23.5.2 TBL-50 `rd_decizie`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar decizie | rd_name | Autonumber | Da | DEC-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Etapa | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | - |
| Titlu | rd_titlu | Text (200) | Da | - | - | - |
| Contextul deciziei | rd_context | Text Area (2000) | Da | - | Ce problema se rezolva | - |
| Alternative considerate | rd_alternative | Text Area (2000) | Nu | - | Ce s-a mai luat in calcul | Partea cea mai valoroasa la recitire |
| Decizia luata | rd_decizie | Text Area (2000) | Da | - | - | - |
| Motivul | rd_motiv | Text Area (2000) | Da | - | - | - |
| Categorie | rd_categorie | Choice | Da | Tehnica / Reteta / Furnizor / Cost / Comerciala / Calitate / Planificare / Scop | - | - |
| Decident | rd_decident | Lookup (systemuser) | Da | - | - | - |
| Data deciziei | rd_datadecizie | Date Only | Da | - | - | - |
| Consultati | rd_consultati | Text (300) | Nu | - | Cine a participat | - |
| Reversibila | rd_reversibila | Yes/No | Da | Implicit Da | Nu = decizie cu consecinte greu de anulat | Merita mai multa atentie |
| Ipoteze asumate | rd_ipoteze | Text Area (2000) | Nu | - | Ce presupunem ca este adevarat | Vezi 23.5.3 |
| Data de reevaluare | rd_datareevaluare | Date Only | Nu | - | Cand se verifica daca ipotezele mai tin | Genereaza actiune |
| Rezultat la reevaluare | rd_rezultat | Choice | Nu | Confirmata / Partial confirmata / Infirmata / Nereevaluata | - | Alimenteaza lectiile |
| Impact asupra costului | rd_impactcost | Currency (2) | Nu | - | Optional | Securitate pe coloana |

23.5.3 Campul de ipoteze este cel care transforma jurnalul dintr-o arhiva intr-un
instrument. O decizie luata pe ipoteza "furnizorul poate livra in 7 zile" se reevalueaza
automat cand ipoteza se dovedeste falsa, si atunci se stie exact ce altceva trebuie
reconsiderat.

## 23.6 Lead time inteligent

### 23.6.1 Problema

Blueprintul de baza avea un singur camp de lead time asumat (2.6.2), setat pe tip, cu
valori implicite de 7 sau 30 de zile. Nu invata nimic din ce se intampla in realitate.

### 23.6.2 TBL-57 `rd_leadtimeistoric`

O inregistrare per livrare efectiva, per furnizor si materie prima.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | Generata | Coloana primara |
| Furnizor | rd_furnizor | Lookup (rd_furnizor) | Da | - | Referential | - |
| Materie prima | rd_materieprima | Lookup (rd_materieprima) | Nu | - | Referential | - |
| Materie prima de proiect | rd_mpproiect | Lookup (rd_mpproiect) | Nu | - | Referential | - |
| Data comenzii | rd_datacomanda | Date Only | Da | - | - | - |
| ETA initial | rd_etainitial | Date Only | Nu | - | Primul ETA confirmat | - |
| ETA final | rd_etafinal | Date Only | Nu | - | Ultimul ETA confirmat | - |
| Data livrarii reale | rd_datalivrare | Date Only | Nu | - | - | - |
| Lead time realizat (zile) | rd_leadtimerealizat | Whole Number | Nu | 0 - 999 | livrare - comanda | - |
| Abatere fata de ETA initial | rd_abatereeta | Whole Number | Nu | -999 - 999 | livrare - ETA initial | Masoara increderea in ETA |
| Numar modificari ETA | rd_modificarieta | Whole Number | Nu | 0 - 99 | - | - |
| Livrat complet | rd_livratcomplet | Yes/No | Nu | - | Pentru OTIF | - |
| Conform la receptie | rd_conform | Yes/No | Nu | - | - | - |
| Tip achizitie | rd_tipachizitie | Choice | Nu | Pe stoc / In portofoliu furnizor / Achizitie noua / Import | Pentru calcul pe categorie | - |

### 23.6.3 Valorile derivate, pe furnizor si materie prima

Scrise de FLX-28, lunar, in coloane pe `rd_furnizor` si `rd_materieprima`:

| Valoare | Formula | Ce spune |
|---|---|---|
| Lead time contractual | Din contract, introdus manual | Ce s-a promis |
| Lead time declarat | Ultimul declarat de furnizor | Ce spune acum |
| Media ultimelor 3 livrari | Media pe `rd_leadtimerealizat` | Comportamentul recent |
| Media ultimelor 12 livrari | Idem | Comportamentul de fond |
| Variabilitate | Abaterea standard a ultimelor 12 | Cat de previzibil este |
| **Lead time forecast** | max(media 3, media 12) + 1 abatere standard | Valoarea folosita in planificare |
| Acuratetea ETA (%) | Livrari in +/- 2 zile fata de ETA initial / total | Increderea in promisiunea lui |
| OTIF (%) | Livrari la timp si complete / total | Indicatorul clasic |

23.6.4 **Planificarea foloseste lead time-ul forecast, nu cel contractual.** Este singura
schimbare din aceasta subsectiune care se vede imediat in practica: termenul propus
(A1.2.5) inceteaza sa mai fie optimist sistematic pentru furnizorii care intarzie mereu.

23.6.5 Pana la acumularea a minimum 3 livrari pentru un furnizor, se foloseste valoarea
implicita pe tip din 2.6.2, marcata explicit ca estimare. Nu se extrapoleaza dintr-o
singura livrare.

## 23.7 Alerte: praguri, deduplicare si escaladare

### 23.7.1 Problema alert fatigue

Un sistem cu 25 de fluxuri care notifica genereaza, in a treia luna, mailuri pe care
nimeni nu le mai deschide. Din acel moment sistemul este mai rau decat inainte: creeaza
iluzia ca oamenii au fost anuntati.

### 23.7.2 Regulile, aplicabile tuturor fluxurilor de notificare

| Regula | Implementare |
|---|---|
| Aceeasi alerta nu se retrimite mai des de 24 de ore | Se retine data ultimei trimiteri pe inregistrare si tip de alerta |
| Se retrimite inainte de 24 de ore doar daca severitatea creste | Compararea nivelului cu cel anterior |
| Alertele similare se consolideaza intr-un digest | Un singur mesaj pe persoana pe zi, grupat pe tip |
| Proprietarul poate amana o alerta, cu motiv si data de revenire | Camp de snooze pe inregistrare |
| Alertele se opresc automat cand cauza dispare | Verificare la fiecare rulare, nu doar la declansare |

23.7.2.1 Se adauga trei coloane pe fiecare tabela care genereaza alerte (`rd_mpproiect`,
`rd_livrabil`, `rd_risc`, `rd_actiune`, `rd_gate`): `rd_dataultimaalerta` (Date and Time),
`rd_amanatpanala` (Date Only) si `rd_motivamanare` (Text 300).

### 23.7.3 Nivelurile de alerta si escaladarea

| Nivel | Cand | Cine primeste |
|---|---|---|
| Verde | In parametri | Nimeni; se vede in tablou |
| Galben | Intarziere forecast de minimum 3 zile sau abatere de 10% | Proprietarul |
| Portocaliu | Minimum 7 zile sau 20% | Proprietarul si Managerul R&D |
| Rosu | Impact asupra termenului negociat catre client | Manager R&D, KAM, Manager Achizitii |
| Critic | Lansare strategica sau material critic in pericol | Head of R&D si conducere |

| Nivel de escaladare | Cine | Dupa cat timp fara raspuns |
|---|---|---|
| 1 | Proprietarul actiunii | La termen |
| 2 | Manager R&D si Manager Achizitii | +5 zile lucratoare |
| 3 | Director Operational si Sales Manager | +10 zile |
| 4 | Conducere executiva | +15 zile, doar pentru Rosu si Critic |

23.7.4 Escaladarea se opreste imediat ce actiunea este inchisa sau amanata cu motiv.
Escaladarea automata fara posibilitate de amanare motivata este a doua cauza de alert
fatigue, dupa volum.

## 23.8 Fluxuri noi

| Cod | Flux | Declansator | Val |
|---|---|---|---|
| FLX-23 | Evaluarea criteriilor automate de gate si actualizarea procentului de pregatire | La modificarea oricarei surse de criteriu | 1 |
| FLX-24 | Revizuirea lunara a riscurilor Ridicat si Critic | Programat, lunar | 2 |
| FLX-25 | Materializarea riscului in problema | `rd_risc.rd_statusrisc` = Produs | 2 |
| FLX-26 | Detectarea cauzelor repetate | Programat, saptamanal | 3 |
| FLX-27 | Escaladarea actiunilor restante | Programat, zilnic | 1 |
| FLX-28 | Calculul lead time-ului forecast si al OTIF pe furnizor | Programat, lunar | 2 |
| FLX-29 | Snapshot de sanatate a proiectului | Programat, saptamanal | 3 |
| FLX-30 | Consolidarea alertelor in digest zilnic | Programat, zilnic 07:00 | 1 |

23.8.1 FLX-30 inlocuieste trimiterile individuale din FLX-08, FLX-21 si FLX-27. Acestea
scriu in coada de alerte; FLX-30 le consolideaza si trimite un singur mesaj pe persoana.
Este singura modificare de arhitectura a fluxurilor fata de Sectiunea 12.


<!-- ==================== S24-stabilizare-capabilitate.md ==================== -->

---

# Sectiunea 24 - Stabilizare, capabilitate de proces si sanatatea proiectului

Trei adaugiri din blueprintul Enterprise (22.2.6, 22.2.7, 22.2.11) care acopera intervalul
dintre productia 0 si revizuirea de la 30 de zile - intervalul in care, azi, produsul intra
in serie fara sa fi demonstrat ca se poate face repetat.

## 24.1 Stabilizarea

### 24.1.1 Golul pe care il acopera

In blueprintul de baza, proiectul trecea din `Productie 0` direct in `Finalizat`, imediat
ce decizia productiei 0 era `Validat`. Adica pe baza **unui singur lot**, facut cu
tehnologul prezent, cu atentia maxima a echipei si, de regula, cu materie prima aleasa.

In bakery industrial, primul lot reusit nu dovedeste nimic despre al zecelea. Variabilitatea
fainii intre loturi, curba de invatare a operatorilor de pe celelalte doua schimburi si
comportamentul liniei la incarcare completa apar abia dupa. Regula celor trei loturi
consecutive conforme este practica standard si se preia ca atare.

### 24.1.2 Regula

Proiectul nu trece in `Finalizat` decat dupa **trei loturi de productie consecutive
conforme**, produse in conditii normale de serie.

| Conditie | Detaliu |
|---|---|
| Consecutive | Nu se aleg trei loturi bune dintre sase. Un lot neconform reseteaza numaratoarea |
| Conforme | Gramaj in toleranta, zero neconformitati HACCP, rebut sub prag, fara reclamatii interne |
| In conditii normale | Fara tehnolog permanent la linie, pe schimburi diferite daca produsul se face pe mai multe |
| Interval maxim | Daca cele trei loturi nu se produc in 90 de zile, stabilizarea se inchide cu status `Neconcludenta` si decizia urca la Managerul R&D |

24.1.3 PROPUNERE: cele trei loturi trebuie sa acopere **minimum doua schimburi diferite**
pentru produsele care se fac pe mai multe schimburi. Motiv: cea mai frecventa cauza de
variatie in serie, dupa materia prima, este diferenta dintre echipe, iar validarea pe un
singur schimb ascunde exact acest lucru.

24.1.4 Statusul `Stabilizare` se adauga in lista din 2.2.1, intre `Productie 0` (8) si
`In revizuire` (10). Etapa corespunzatoare este ETP-12, adaugata dupa ETP-10.

### 24.1.5 TBL-51 `rd_stabilizare`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar | rd_name | Autonumber | Da | STB-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Productie 0 sursa | rd_productie0 | Lookup (rd_productie0) | Da | - | Referential | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | - | - |
| Data inceperii | rd_datainceput | Date Only | Da | - | Prima productie de serie | - |
| Numar loturi necesare | rd_loturinecesare | Whole Number | Da | 1 - 10, implicit 3 | Configurabil pe categorie de produs | Variabila de mediu |
| Loturi produse | rd_loturiproduse | Rollup (Count) | Nu | 0 - 99 | Din rd_lotstabilizare | - |
| Loturi conforme consecutive | rd_loturiconforme | Whole Number | Nu | 0 - 99 | Se reseteaza la primul neconform | Scris de FLX-31 |
| Schimburi acoperite | rd_schimburi | Whole Number | Nu | 1 - 3 | Distinct pe loturi conforme | Vezi 24.1.3 |
| Randament mediu in serie (%) | rd_randamentmediu | Decimal (2) | Nu | 0 - 120 | Media loturilor conforme | - |
| Randament la productia 0 (%) | rd_randamentprod0 | Decimal (2) | Nu | - | Preluat automat | Baza de comparatie |
| Diferenta de randament (pp) | rd_diferentarandament | Calculated (Decimal) | Nu | - | serie - productie 0 | Vezi 24.1.7 |
| Rebut mediu in serie (%) | rd_rebutmediu | Decimal (2) | Nu | 0 - 100 | - | - |
| Giveaway mediu (%) | rd_giveawaymediu | Decimal (2) | Nu | -50 - 50 | Supraumplerea in serie | Vezi 7.6.7 |
| Viteza medie realizata (%) | rd_vitezamedie | Decimal (2) | Nu | 0 - 150 | Fata de viteza nominala | - |
| Reclamatii interne | rd_reclamatiiinterne | Whole Number | Nu | 0 - 99 | - | - |
| Variabilitate acceptabila | rd_variabilitateok | Yes/No | Nu | - | CV al gramajului sub prag pe toate loturile | Vezi 6.2.3 |
| Actiuni deschise | rd_actiunideschise | Rollup (Count) | Nu | - | Din rd_actiune | Blocheaza inchiderea |
| Status | rd_statusstabilizare | Choice | Da | In curs / Reusita / Neconcludenta / Esuata | - | Choice global STATUSSTAB |
| Data finalizarii | rd_datafinalizare | Date Only | Nu | - | La al treilea lot conform consecutiv | Declanseaza G7 |
| Decizie | rd_deciziestabilizare | Choice | Nu | Release / Release cu monitorizare / Se prelungeste / Se reia productia 0 | - | - |
| Motivul deciziei | rd_motivdecizie | Text Area (2000) | Nu | - | Obligatoriu pentru tot ce nu e Release | - |
| Responsabil | rd_responsabil | Lookup (systemuser) | Da | - | - | - |

### 24.1.6 TBL-52 `rd_lotstabilizare`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Numarul lotului de productie | - | Coloana primara |
| Stabilizare | rd_stabilizare | Lookup (rd_stabilizare) | Da | - | Parental | Cascade All |
| Numar de ordine | rd_numarordine | Whole Number | Da | 1 - 99 | Succesiv | - |
| Data productiei | rd_dataproductie | Date Only | Da | - | - | - |
| Schimb | rd_schimb | Choice | Da | Choice SCHIMB | - | - |
| Cantitate produsa (kg) | rd_cantitate | Decimal (2) | Da | > 0 | - | - |
| Randament (%) | rd_randament | Decimal (2) | Nu | 0 - 120 | - | - |
| Rebut (%) | rd_rebut | Decimal (2) | Nu | 0 - 100 | - | - |
| Greutate medie (g) | rd_greutatemedie | Decimal (2) | Nu | - | Minimum 20 de bucati | - |
| CV gramaj (%) | rd_cvgramaj | Decimal (2) | Nu | 0 - 100 | - | Vezi 6.2.3 |
| Giveaway (%) | rd_giveaway | Decimal (2) | Nu | -50 - 50 | - | - |
| Viteza realizata (%) | rd_viteza | Decimal (2) | Nu | 0 - 150 | - | - |
| Conformitate HACCP | rd_haccpok | Yes/No | Da | - | O neconformitate = lot neconform | - |
| Reclamatii sau neconformitati | rd_neconformitati | Whole Number | Nu | 0 - 99 | - | - |
| Lot conform | rd_conform | Yes/No | Da | - | Vezi 24.1.2 | Scris de FLX-31 |
| Motivul neconformitatii | rd_motivneconform | Text Area (1000) | Nu | - | Obligatoriu daca lot conform = Nu | - |
| Problema generata | rd_problema | Lookup (rd_problema) | Nu | - | Un lot neconform creeaza automat o problema | FLX-31 |

### 24.1.7 Ce se face cu diferenta de randament

Diferenta dintre randamentul in serie si cel de la productia 0 este prima informatie
economica reala a produsului. Se propaga automat in doua locuri: in `rd_antecalcul.rd_costreal`,
ca sa se vada marja adevarata, si in revizuirea de la 30 de zile (8.2.7), ca punct de
pornire, nu ca descoperire.

24.1.8 O diferenta mai mare de 3 puncte procentuale in minus declanseaza automat o problema
(TBL-48) de categorie Financiar, cu severitate Majora. Motiv: la un produs de volum, 3
puncte de randament sunt mai multi bani decat toate economiile pe care le va face proiectul
de optimizare care urmeaza.

## 24.2 Capabilitatea de proces

### 24.2.1 Ce adauga fata de statistica existenta

Blueprintul de baza calcula media, abaterea standard, CV, minimul si maximul (6.1.4).
Acestea descriu esantionul. Capabilitatea raspunde la o intrebare diferita si mai utila:
**procesul, asa cum se comporta, poate sta in limitele de specificatie pe termen lung?**

### 24.2.2 Formulele

```
Cp  = (LSS - LIS) / (6 x sigma)
Cpk = MIN( (LSS - medie) / (3 x sigma), (medie - LIS) / (3 x sigma) )

unde LSS = limita superioara de specificatie = tinta + toleranta plus
      LIS = limita inferioara de specificatie = tinta - toleranta minus
      sigma = abaterea standard a procesului
```

24.2.3 Interpretarea, cu pragurile uzuale:

| Cpk | Interpretare | Ce se face |
|---|---|---|
| sub 1.00 | Proces incapabil. Produce neconformitati sistematic | Nu se accepta la stabilizare; se reia setarea |
| 1.00 - 1.32 | Marginal capabil | Acceptabil cu monitorizare si control in proces |
| 1.33 - 1.66 | Capabil | Tinta normala pentru gramaj in bakery |
| peste 1.67 | Foarte capabil | Se poate reduce frecventa controlului |

24.2.4 **Cp fata de Cpk**: Cp spune daca imprastierea incape in tolerante; Cpk spune daca
incape **si este centrata**. Un Cp de 2.0 cu Cpk de 0.8 inseamna un proces precis dar
deplasat - se corecteaza prin reglaj, ieftin. Un Cp de 0.7 inseamna imprastiere prea mare
- se corecteaza doar prin schimbarea procesului, scump. Distinctia decide ce se face
luni dimineata.

### 24.2.5 Conditii de calcul

| Conditie | Valoare | Motiv |
|---|---|---|
| Numar minim de valori | 30 | Sub 30, sigma este prea instabila pentru un indice de capabilitate |
| Loturi diferite | Minimum 3 | Altfel se masoara variatia din interiorul unui lot, nu a procesului |
| Limite de specificatie declarate | Obligatorii | Fara tolerante nu exista capabilitate |
| Date fara valori excluse arbitrar | Da | Excluderile scad artificial sigma si umfla Cpk |

24.2.6 Sub 30 de valori, sistemul afiseaza `Date insuficiente`, nu un numar. Un Cpk
calculat pe 10 bucati este o cifra cu doua zecimale care nu inseamna nimic si care va fi
citata in sedinte.

### 24.2.7 TBL-53 `rd_capabilitateproces`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | {produs}_{parametru} | Generata | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Stabilizare | rd_stabilizare | Lookup (rd_stabilizare) | Nu | - | Referential | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | Capabilitatea este a perechii produs-linie | - |
| Parametru | rd_parametru | Choice | Da | Choice TIPMASURATOARE | Tipuri numerice | - |
| Perioada de la | rd_perioadadela | Date Only | Da | - | - | - |
| Perioada pana la | rd_perioadapanala | Date Only | Da | - | - | - |
| Numar de valori | rd_n | Whole Number | Da | 1 - 9999 | Sub 30 = Date insuficiente | Vezi 24.2.5 |
| Numar de loturi | rd_numarloturi | Whole Number | Da | 1 - 99 | Minimum 3 | - |
| Media | rd_medie | Decimal (4) | Da | - | - | - |
| Abaterea standard | rd_sigma | Decimal (5) | Da | > 0 | Esantion, n-1 | - |
| Tinta | rd_tinta | Decimal (4) | Da | - | Din specificatie | - |
| Limita inferioara | rd_lis | Decimal (4) | Da | - | tinta - toleranta minus | - |
| Limita superioara | rd_lss | Decimal (4) | Da | - | tinta + toleranta plus | - |
| Cp | rd_cp | Decimal (3) | Nu | 0 - 10 | Vezi 24.2.2 | - |
| Cpk | rd_cpk | Decimal (3) | Nu | -5 - 10 | Poate fi negativ daca media e in afara limitelor | - |
| Deplasare fata de tinta (%) | rd_deplasare | Decimal (2) | Nu | -100 - 100 | (medie - tinta) / tinta x 100 | Arata daca e reglaj sau imprastiere |
| Verdict | rd_verdict | Choice | Da | Date insuficiente / Incapabil / Marginal / Capabil / Foarte capabil | Vezi 24.2.3 | - |
| Recomandare | rd_recomandare | Text Area (1000) | Nu | - | Generata din combinatia Cp / Cpk | Vezi 24.2.4 |
| Data calculului | rd_datacalcul | Date and Time | Da | - | - | Scris de FLX-32 |

24.2.8 Capabilitatea se calculeaza pentru gramaj obligatoriu, si optional pentru dimensiuni
si pentru temperatura in centru la congelare. Pentru ultimul, limita este unilaterala
(doar maximum -18 C), deci se calculeaza numai Cpk superior.

## 24.3 Sanatatea proiectului in timp

### 24.3.1 De ce snapshot si nu doar un camp calculat

Un scor de sanatate calculat la cerere spune cum sta proiectul acum. Nu spune ca acum
trei saptamani era verde si a coborat constant. Tendinta este informatia care permite
interventia inainte de criza; valoarea instantanee permite doar constatarea ei.

### 24.3.2 Formula

Preluata din Enterprise 14.1, cu ponderile adaptate la ce exista efectiv in model:

| Componenta | Pondere | Sursa | Cum se puncteaza |
|---|---|---|---|
| Riscuri | 20 | TBL-47 | 20 fara riscuri Ridicat sau Critic deschise; minus 5 pentru fiecare Ridicat; 0 daca exista Critic |
| Livrabile | 20 | TBL-03 | Procentul de livrabile scadente si realizate, scalat la 20 |
| Termen | 15 | TBL-02 | 15 daca forecast <= negociat; scade proportional cu depasirea |
| Pregatire de aprovizionare | 15 | TBL-07 | Procentul de materii prime critice cu ETA confirmat si neexpirat |
| Pregatire de productie | 10 | TBL-32 | Procentul de conditii IPN indeplinite; 10 daca IPN nu e inca aplicabil |
| Calitate | 10 | TBL-16b, TBL-17 | Conformitatea ultimelor masuratori si verdictul senzorial |
| Capacitate | 10 | TBL-37 | 10 daca tehnologul e sub 100% incarcare; scade peste |

```
sanatate = suma componentelor          [0 - 100]

Verde     90 - 100
Galben    75 - 89
Portocaliu 60 - 74
Rosu      sub 60
```

24.3.3 Un proiect `Blocat` nu primeste automat rosu. Blocajul extern este deja masurat
separat si nu este vina proiectului; ce conteaza este daca, dupa deblocare, mai poate
recupera. Se marcheaza distinct, cu pastila proprie.

### 24.3.4 TBL-58 `rd_snapshotsanatate`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {cod proiect}_{AAAALLZZ} | Generata | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Data snapshot | rd_data | Date Only | Da | - | Saptamanal, luni | Unic impreuna cu proiectul |
| Status la data | rd_status | Choice | Da | Choice STATUSPROIECT | Copiat, nu referit | Ca sa ramana istoric corect |
| Etapa la data | rd_etapa | Text (100) | Nu | - | Copiata ca text | Idem |
| Scor sanatate | rd_scorsanatate | Whole Number | Da | 0 - 100 | Vezi 24.3.2 | - |
| Nivel | rd_nivel | Choice | Da | Verde / Galben / Portocaliu / Rosu / Blocat | - | - |
| Componenta riscuri | rd_compriscuri | Whole Number | Nu | 0 - 20 | - | - |
| Componenta livrabile | rd_complivrabile | Whole Number | Nu | 0 - 20 | - | - |
| Componenta termen | rd_comptermen | Whole Number | Nu | 0 - 15 | - | - |
| Componenta aprovizionare | rd_compaprovizionare | Whole Number | Nu | 0 - 15 | - | - |
| Componenta productie | rd_compproductie | Whole Number | Nu | 0 - 10 | - | - |
| Componenta calitate | rd_compcalitate | Whole Number | Nu | 0 - 10 | - | - |
| Componenta capacitate | rd_compcapacitate | Whole Number | Nu | 0 - 10 | - | - |
| Variatie fata de saptamana trecuta | rd_variatie | Whole Number | Nu | -100 - 100 | - | Semnalul cel mai util |
| Zile de la ultima activitate | rd_zileinactiv | Whole Number | Nu | 0 - 999 | Din rd_ultimaactivitate | Detecteaza proiecte uitate |
| Riscuri deschise | rd_riscurideschise | Whole Number | Nu | 0 - 99 | - | - |
| Probleme deschise | rd_problemedeschise | Whole Number | Nu | 0 - 99 | - | - |
| Actiuni restante | rd_actiunirestante | Whole Number | Nu | 0 - 99 | - | - |
| Livrabile depasite | rd_livrabiledepasite | Whole Number | Nu | 0 - 99 | - | - |

24.3.5 Snapshot-ul se scrie saptamanal de FLX-29, pentru toate proiectele active, si nu se
mai modifica niciodata. Este singura tabela din model care creste liniar cu timpul fara
sa fie stearsa; la 180 de proiecte pe an si 20 de saptamani medii de viata, inseamna
aproximativ 3600 de randuri pe an, ceea ce este neglijabil.

24.3.6 **Alerta de degradare**: o scadere de peste 15 puncte intr-o saptamana, sau trei
saptamani consecutive de scadere, genereaza o notificare catre Managerul R&D. Este
mecanismul care prinde proiectele care se strica lent, tipul de proiect care azi se
descopera cu doua saptamani inainte de termen.

## 24.4 Project Success Score

### 24.4.1 Cand se calculeaza

O singura data, la revizuirea de 90 de zile (Sectiunea 8), cu revizuire optionala la 180
de zile pentru proiectele importante. Nu este un indicator operational, ci unul de
invatare: raspunde la intrebarea "ce fel de proiecte ne ies bine".

### 24.4.2 Formula

| Componenta | Puncte | Sursa |
|---|---|---|
| Volum realizat fata de estimat | 20 | TBL-35 |
| Respectarea termenului negociat | 15 | TBL-02, abaterea de termen |
| Rezultatul productiei 0 | 20 | TBL-33, decizia si numarul de repetari |
| Cost real fata de antecalcul | 15 | TBL-35, abaterea de cost |
| Calitate si reclamatii | 20 | TBL-35, rata de reclamatii |
| Stabilitate post-implementare | 10 | TBL-51, diferenta de randament |

| Clasificare | Scor |
|---|---|
| Champion | 90 - 100 |
| Success | 80 - 89 |
| Acceptable | 70 - 79 |
| Weak | 60 - 69 |
| Failed | sub 60 |

24.4.3 Scorul se stocheaza pe `rd_revizuire` (TBL-35), ca doua coloane noi:
`rd_scorsucces` (Whole Number) si `rd_clasificaresucces` (Choice). Nu are nevoie de tabela
proprie.

24.4.4 NOTA: indicele de sanatate al produsului din 8.4 si acest scor de succes masoara
lucruri apropiate, dar diferite - primul spune daca produsul isi tine promisiunile
comerciale, al doilea daca proiectul a fost bine condus. Un produs poate fi Champion cu un
proiect Weak, daca piata l-a salvat, si invers. Se pastreaza ambele, iar diferenta dintre
ele este ea insasi informatie: proiectele bine conduse cu produse slabe arata o problema de
selectie la triaj, nu de executie.


<!-- ==================== S25-cunoastere.md ==================== -->

---

# Sectiunea 25 - Cunoastere organizationala

Preluat integral din blueprintul Enterprise, capitolul 12. Este singurul domeniu in care
blueprintul de baza nu avea absolut nimic, si probabil cel cu cel mai bun raport
efort-beneficiu din toata sinteza.

## 25.1 Problema

25.1.1 La 130-180 de proiecte pe an, timp de zece ani, compania a rezolvat de mai multe ori
aceleasi probleme. Faina care se comporta altfel iarna, furnizorul de umplutura care
livreaza cu vascozitate variabila, linia care nu tine gramajul sub 45 g, clientul care
respinge orice produs cu ulei de palmier. Toate aceste lucruri sunt stiute. Niciunul nu
este scris.

25.1.2 Consecinta practica: un tehnolog nou repeta greselile facute acum trei ani, iar un
tehnolog care pleaca ia cu el cinci ani de context. Costul nu apare nicaieri in contabilitate,
dar este cel mai mare cost ascuns al departamentului.

25.1.3 Ce **nu** rezolva aceasta sectiune: nu transforma un sistem de evidenta intr-un
sistem de management al cunoasterii prin simpla existenta a unei tabele. Lectiile se scriu
numai daca sunt cerute la momentul potrivit si sunt reutilizate numai daca apar
neintrebate, la momentul potrivit. Ambele mecanisme sunt in 25.2 si 25.4.

## 25.2 Lectii invatate

### 25.2.1 TBL-54 `rd_lectie`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar lectie | rd_name | Autonumber | Da | LSN-{AA}-{SEQ:0000} | - | Coloana primara |
| Titlu | rd_titlu | Text (200) | Da | - | Formulat ca afirmatie, nu ca subiect | Vezi 25.2.4 |
| Situatia | rd_situatie | Text Area (2000) | Da | - | Ce s-a intamplat concret | - |
| Cauza radacina | rd_cauzaradacina | Text Area (2000) | Da | - | De ce s-a intamplat | - |
| Lectia | rd_lectie | Text Area (2000) | Da | - | Ce stim acum si nu stiam inainte | - |
| Recomandarea | rd_recomandare | Text Area (2000) | Da | - | Ce sa faca altcineva data viitoare | Partea reutilizabila |
| Actiune preventiva | rd_actiunepreventiva | Text Area (2000) | Nu | - | Ce schimbare de proces ar impiedica repetarea | Poate genera actiune |
| Categorie | rd_categorie | Choice | Da | Reteta / Materie prima / Furnizor / Proces / Echipament / Calitate / Client / Comercial / Cost / Planificare / Ambalaj / Reglementare | - | Choice global CATEGORIELECTIE |
| Severitatea situatiei | rd_severitate | Choice | Da | Minora / Majora / Critica | - | - |
| Nivel de reutilizare | rd_nivelreutilizare | Choice | Da | Proiect / Categorie de produs / Linie / Furnizor / Client / Intreaga companie | Determina cui i se recomanda | Vezi 25.4 |
| Categorie de produs | rd_categorieprodus | Choice | Nu | Foietaj / Aluat dospit / Patiserie cu umplutura / Paine / Toate | Pentru potrivire | - |
| Linie | rd_linie | Lookup (rd_linie) | Nu | - | Referential | - |
| Materie prima | rd_materieprima | Lookup (rd_materieprima) | Nu | - | Referential | - |
| Furnizor | rd_furnizor | Lookup (rd_furnizor) | Nu | - | Referential | - |
| Client | rd_client | Lookup (rd_client) | Nu | - | Referential | - |
| Etichete | rd_etichete | Text (300) | Nu | Cuvinte separate prin `;` | Pentru cautare libera | - |
| Cost potential evitat | rd_costevitat | Currency (2) | Nu | - | Estimare, optionala | Securitate pe coloana |
| Zile potential evitate | rd_zileevitate | Whole Number | Nu | 0 - 365 | Estimare | - |
| Proiect sursa | rd_proiect | Lookup (rd_proiect) | Nu | - | De unde provine | Referential |
| Problema sursa | rd_problema | Lookup (rd_problema) | Nu | - | Referential | - |
| Neconformitate sursa | rd_neconformitate | Lookup (rd_neconformitate) | Nu | - | Val 4 | - |
| Productie 0 sursa | rd_productie0 | Lookup (rd_productie0) | Nu | - | Referential | - |
| Generata automat | rd_generataauto | Yes/No | Da | Implicit Nu | Draft creat de FLX-33 | Vezi 25.2.2 |
| Status | rd_statuslectie | Choice | Da | Draft / In verificare / Aprobata / Respinsa / Arhivata | Numai cele Aprobate se recomanda | - |
| Autor | rd_autor | Lookup (systemuser) | Da | - | - | - |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | Manager R&D | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Numar reutilizari | rd_numarreutilizari | Rollup (Count) | Nu | 0 - 999 | Din rd_utilizarelectie | Vezi 25.3 |
| Data ultimei reutilizari | rd_dataultimareutilizare | Date Only | Nu | - | - | Lectiile nefolosite se revizuiesc |

### 25.2.2 Generarea automata a drafturilor

Nimeni nu se aseaza sa scrie o lectie invatata din proprie initiativa. Sistemul creeaza
**drafturi**, la momentele in care exista material, si cere unei persoane sa le completeze.

| Declansator | Ce se precompleteaza |
|---|---|
| Productie 0 cu decizia `Se repeta` | Proiectul, linia, parametrii care au deviat, problemele deschise |
| Neconformitate critica inchisa | Cauza radacina, actiunea corectiva |
| Aceeasi cauza radacina de 3 ori in 12 luni | Cele trei probleme, cu proiectele lor |
| Abatere de cost peste prag la revizuire | Antecalculul, costul real, componenta care a deviat |
| Iteratie de furnizor respinsa a treia oara pe acelasi proiect | Furnizorul, motivele respingerii |
| Reclamatie critica de client | Reclamatia, produsul, lotul |
| Proiect abandonat dupa etapa de testare | Motivul, faza in care s-a oprit |
| Proiect inchis cu scor de succes sub 70 | Componentele scorului care au tras in jos |

25.2.3 Draftul are status `Draft`, autor = responsabilul proiectului si o actiune generata
automat cu termen de 10 zile lucratoare. **Nu se aproba singur.** O lectie generata automat
si neverificata este zgomot cu aspect de cunoastere.

25.2.4 Regula de formulare a titlului: lectia se scrie ca **afirmatie**, nu ca subiect.
"Faina cu W sub 280 nu tine laminarea la grosimi sub 2 mm" este o lectie. "Probleme cu
faina" este o eticheta de dosar. Regula se pune in ajutorul de camp, unde se citeste.

## 25.3 Urmarirea reutilizarii

### 25.3.1 TBL-55 `rd_utilizarelectie`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | Generata | - | Coloana primara |
| Lectie | rd_lectie | Lookup (rd_lectie) | Da | - | Parental | Cascade All |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Unde s-a folosit | Referential |
| Etapa | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | - |
| Persoana | rd_persoana | Lookup (systemuser) | Da | - | Cine a folosit-o | - |
| Data | rd_data | Date Only | Da | - | Implicit azi | - |
| Cum a fost folosita | rd_mod | Text Area (1000) | Nu | - | - | - |
| Rezultat | rd_rezultat | Choice | Da | A ajutat / Partial / Nu a ajutat / Prea devreme | - | - |
| Cost evitat estimat | rd_costevitat | Currency (2) | Nu | - | Optional | Securitate pe coloana |
| Zile evitate estimate | rd_zileevitate | Whole Number | Nu | 0 - 365 | Optional | - |
| Risc evitat | rd_riscevitat | Text (300) | Nu | - | - | - |

25.3.2 Inregistrarea se face cu un singur click, din recomandarea afisata pe proiect
(25.4). Daca ar cere completarea unui formular, nimeni nu ar face-o si intreaga sectiune ar
deveni decorativa.

25.3.3 Utilitatea reala a acestei tabele nu este raportarea, ci **selectia**: lectiile
folosite frecvent urca in recomandari, cele nefolosite dupa 18 luni intra in revizuire si
se arhiveaza. Fara acest mecanism, biblioteca de lectii creste la 400 de intrari si devine
nefolosibila, adica exact ca un folder de documente.

## 25.4 Recomandarea lectiilor

### 25.4.1 Principiul

O lectie cautata nu se gaseste. O lectie care apare singura, pe ecranul proiectului, in
momentul in care este relevanta, se citeste.

### 25.4.2 Cand se recomanda

| Moment | Ce se potriveste |
|---|---|
| La acceptarea proiectului | Categoria de produs, clientul, tipul de proiect |
| La alocarea liniei | Linia, plus categoria de produs |
| La adaugarea unei materii prime | Materia prima si furnizorul ei |
| La deschiderea unei fise de testare | Categoria de produs si linia |
| La pregatirea IPN | Linia, plus produsele similare implementate pe ea |
| La aparitia unei probleme | Categoria si cauza probabila |

### 25.4.3 TBL-56 `rd_recomandarelectie`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | Generata | - | Coloana primara |
| Lectie | rd_lectie | Lookup (rd_lectie) | Da | - | Referential | - |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Momentul recomandarii | rd_moment | Choice | Da | Acceptare / Alocare linie / Materie prima / Fisa de testare / IPN / Problema | Vezi 25.4.2 | - |
| Scor de potrivire | rd_scorpotrivire | Whole Number | Da | 0 - 100 | Vezi 25.4.4 | - |
| Motivul potrivirii | rd_motivpotrivire | Text (300) | Da | - | "Aceeasi linie si categorie de produs" | Face recomandarea credibila |
| Data recomandarii | rd_datarecomandare | Date and Time | Da | - | - | - |
| Status | rd_statusrecomandare | Choice | Da | Afisata / Acceptata / Aplicata / Respinsa / Ignorata | - | - |
| Motivul respingerii | rd_motivrespingere | Text (300) | Nu | - | Optional, dar util pentru calibrare | - |
| Utilizare generata | rd_utilizare | Lookup (rd_utilizarelectie) | Nu | - | La status Aplicata | - |

### 25.4.4 Scorul de potrivire

```
scor = 0
+ 30  daca categoria de produs coincide
+ 25  daca linia coincide
+ 20  daca materia prima coincide
+ 15  daca furnizorul coincide
+ 10  daca clientul coincide
+ 10  daca severitatea lectiei este Critica
+ min(10, numar_reutilizari x 2)   [lectiile care ajuta urca]
- 15  daca lectia este mai veche de 3 ani si nereutilizata

Se afiseaza maximum 3 recomandari, cu scor peste 40.
```

25.4.5 Plafonul de trei recomandari este deliberat. Zece recomandari relevante inseamna
zero recomandari citite. Pragul de 40 si plafonul de 3 sunt variabile de mediu si se
recalibreaza dupa primele sase luni, urmarind rata de acceptare din `rd_statusrecomandare`.

25.4.6 NOTA: potrivirea este pe reguli, nu pe model de limbaj. Este transparenta,
explicabila si functioneaza de la prima lectie. Un motor semantic peste lectii ar fi mai
bun la 300 de lectii, dar la 15 lectii, cate vor exista in primul an, ar fi doar mai greu
de explicat cand greseste. Trecerea la potrivire semantica este in Anexa A2, cu criteriu
de activare.

## 25.5 Impactul cunoasterii

25.5.1 Nu se creeaza tabela `KnowledgeImpact` din Enterprise. Datele necesare exista deja
in `rd_utilizarelectie`, iar impactul este o agregare, nu o entitate.

25.5.2 Raportul RAP-16 `Impactul cunoasterii`, adaugat la lista din 13.6.1:

| Indicator | Calcul |
|---|---|
| Lectii create in perioada | Count pe `rd_lectie` |
| Lectii aprobate | Count cu status Aprobata |
| Rata de aprobare a drafturilor automate | Aprobate / generate automat |
| Lectii reutilizate cel putin o data | Count distinct pe utilizari |
| Rata de reutilizare | Reutilizate / aprobate |
| Cost total evitat estimat | Suma pe utilizari |
| Zile totale evitate estimate | Suma pe utilizari |
| Top 10 lectii dupa reutilizare | Sortare |
| Lectii nereutilizate de peste 18 luni | Candidate la arhivare |
| Rata de acceptare a recomandarilor | Acceptate / afisate |

25.5.3 Cifrele de cost si zile evitate sunt estimari declarate de oameni, nu masuratori.
Se raporteaza ca atare, cu mentiunea "estimat", si nu se folosesc in justificari
financiare externe. Valoarea lor este comparativa in timp, nu absoluta.

## 25.6 Bibliotecile

25.6.1 Blueprintul Enterprise propune sase biblioteci separate: RootCause, Defect, Failure,
SuccessPattern, BestPractice, Playbook. Se pastreaza doua si se amana patru.

| Biblioteca | Decizie | Motiv |
|---|---|---|
| DefectLibrary | **Exista deja** | TBL-20a, cu 22 de defecte definite in `data/nomenclatoare.json` |
| RootCauseLibrary | **Se adauga**, ca nomenclator | Nomenclator de cauze radacina, folosit in TBL-48. Fara el, cauzele se scriu diferit de fiecare data si detectarea repetarii (25.2.2) nu functioneaza |
| FailureLibrary, SuccessPattern, BestPractice, Playbook | Amanate | Sunt vederi filtrate peste `rd_lectie`, nu entitati noi. Se construiesc ca vizualizari, cand exista suficiente lectii |

25.6.2 `rd_cauzaradacina` devine nomenclator (extindere a TBL-41 `rd_motiv`, cu tipul
`Cauza radacina`), nu tabela noua. Se populeaza initial cu cauzele din biblioteca de
defecte si creste prin utilizare, cu aprobarea Managerului R&D pentru intrari noi.

## 25.7 Fluxuri

| Cod | Flux | Declansator | Val |
|---|---|---|---|
| FLX-33 | Generarea drafturilor de lectii | Cele 8 declansatoare din 25.2.2 | 3 |
| FLX-34 | Potrivirea si afisarea recomandarilor | Cele 6 momente din 25.4.2 | 3 |
| FLX-35 | Revizuirea lectiilor nereutilizate | Programat, semestrial | 3 |

25.7.1 FLX-26 (detectarea cauzelor repetate, din 23.8) alimenteaza FLX-33. Cele doua se
construiesc impreuna.


<!-- ==================== S26-constructie-asistata.md ==================== -->

---

# Sectiunea 26 - Constructia asistata: ce se genereaza si ce nu

Revizuieste estimarea de efort din Sectiunea 16, care presupunea constructie manuala in
interfata Power Apps. Ipoteza aceea era gresita si a fost corectata.

## 26.1 Ipoteza corectata

26.1.1 Estimarea initiala de 130-158 de zile-om presupunea un om care creeaza 60 de tabele
si 985 de coloane facand click, una cate una, in interfata. La un ritm realist de 12-15
coloane pe ora, inclusiv verificarea, numai modelul de date insemna 8-10 zile pline de
click-uri repetitive, iar formularele, vizualizarile si rolurile inca aproximativ 30.

26.1.2 Ipoteza este gresita pentru ca **metadatele Dataverse sunt date**. O tabela, o
coloana, o relatie, un set de optiuni, o vizualizare, un rol de securitate si o definitie
de flux sunt toate obiecte JSON sau XML, create prin API. Ce este text se genereaza.

26.1.3 Dovada este in `build/deploy/`: 31 de seturi de optiuni, 60 de tabele, 738 de
coloane si 151 de relatii, generate din artefactele blueprintului si gata de trimis catre
Dataverse. Acoperirea este de 961 din 985 de coloane, adica 97,6%.

## 26.2 Ce se genereaza integral

| Artefact | Volum | Stare | Efort manual ramas |
|---|---|---|---|
| Seturi de optiuni globale | 31, cu 178 de valori | **Generat** | 0 |
| Tabele | 60 | **Generat** | 0 |
| Coloane | 738 din 985 | **Generat** | 0 |
| Relatii, cu comportament la stergere | 151 | **Generat** | 0 |
| Fisiere de import de nomenclator | 8 CSV | **Generat** | Completarea sabloanelor cu date reale |
| Sablonul de livrabile si de etape | 43 + 11 randuri | **Generat** | 0 |
| Vizualizari si formulare | ~40 vizualizari, ~25 formulare | Generabil, neconstruit inca | Ajustari de aspect |
| Harta de site a aplicatiei | 1 | Generabil, neconstruit inca | 0 |
| Roluri de securitate | 13, cu matricea din S11 | Generabil, neconstruit inca | Verificare cu utilizatori de test |
| Definitii de fluxuri | ~35 | Generabil ca schelet | Legarea conexiunilor si testarea |
| Sabloane Word pentru documente | 11 | Generabil ca structura | Formatarea vizuala |
| Model semantic Power BI | 1 | Generabil | Aspectul rapoartelor |

## 26.3 Ce nu se genereaza, si de ce

Aceasta este partea importanta a sectiunii. Nu tot ce ramane este munca de IT, si tocmai
de aceea nu se comprima.

### 26.3.1 Formulele Calculated si Rollup - 24 de coloane

Definitia formulei nu se poate seta fiabil prin API-ul de metadate. Se creeaza manual, in
aproximativ 2 ore, dupa ce restul modelului exista. Lista completa este generata in
`build/deploy/payloaduri/coloane-manuale.json`.

### 26.3.2 Datele companiei

Nu le pot produce. Nu sunt in niciun document si nu se pot deduce.

| Ce lipseste | De la cine | Volum |
|---|---|---|
| Capabilitatile, gramajele, vitezele si tarifele celor 9 linii | Productie, Planificare, Controlling | 9 randuri, dar 6 campuri fiecare care cer masuratori sau decizii |
| Clasificarea A/B/C a clientilor | Sales | 100-300 de randuri, plus o decizie de responsabilitate (IQ-04) |
| Datele nutritionale si de alergeni ale materiilor prime | Calitate, din ST-urile furnizorilor | 150-250 de coduri in prima transa, fiecare cu 11 valori citite dintr-un PDF |
| Profilurile si capacitatile tehnologilor | Head of R&D | ~30 de randuri |
| Proiectele in curs la punerea in functiune | Fiecare tehnolog, pentru proiectele lui | 20-40, cu confirmare individuala |

26.3.3 Aceasta este, dupa corectarea ipotezei, **cea mai mare pozitie de efort ramasa** si
singura care nu depinde de viteza de constructie. Materiile prime, in particular:
250 de coduri x 11 valori citite manual din specificatii de furnizor inseamna 8-12 zile de
munca umana, indiferent cine construieste sistemul.

26.3.4 Consecinta practica, care schimba ce trebuie facut acum: **calea critica nu mai este
constructia, ci obtinerea datelor.** Cererea catre Sales pentru clasificarea clientilor si
cererea catre Calitate pentru datele de materie prima trebuie facute in prima saptamana,
nu cand ajunge constructia la ele.

### 26.3.5 Deciziile

Cele 10 intrebari din Sectiunea 20 raman deschise indiferent cat de repede se construieste.
IQ-01 (mediul de productie) si IQ-02 (licentele) sunt blocante pentru trecerea in productie,
nu pentru constructie.

### 26.3.6 Testarea in conditii reale

Aplicatia canvas se poate genera ca schelet, dar comportamentul ei cu manusi, pe telefonul
cel mai vechi din dotare, in zona cu semnal slab din hala, se afla doar mergand acolo.
Cele patru teste de acceptanta din 17.3.4 nu se pot simula.

### 26.3.7 Timpul calendaristic care nu este efort

Trei lucruri iau timp fara sa consume zile-om:

| Element | Timp minim | Motiv |
|---|---|---|
| Masurarea adoptiei Valului 1 | 30 de zile | Criteriile din 16.2 se masoara dupa o luna de folosire |
| Stabilizarea pe 3 loturi | 4-12 saptamani | Depinde de cat de des se produce produsul |
| Prima calibrare a duratelor | 6-12 luni | Vezi 14.4.1: minimum 20 de proiecte finalizate |
| Revizuirea la 90 de zile | 90 de zile | Definitia procesului |

26.3.8 Niciunul nu se accelereaza. Un sistem construit in trei saptamani tot are nevoie de
30 de zile ca sa se vada daca este folosit.

## 26.4 Estimarea revizuita

### 26.4.1 Partea de constructie

| Activitate | Estimare initiala | Revizuita | Ce s-a schimbat |
|---|---|---|---|
| Model de date: tabele, coloane, relatii, optionsets | 45 | **3** | Generat; raman ciclurile de import si corectie |
| Formulare, vizualizari, harta de site | 15 | **4** | Generat; raman ajustarile de aspect |
| Roluri de securitate | 5 | **2** | Generat; ramane verificarea cu utilizatori de test |
| Fluxuri Power Automate (35) | 40 | **15** | Scheletele se genereaza; legarea conexiunilor si testarea cu date reale nu |
| Aplicatia canvas | 15 | **8** | Scheletul se genereaza; testarea in hala nu |
| Sabloane Word (11) | 8 | **4** | Structura se genereaza; formatarea nu |
| Power BI | 10 | **5** | Modelul semantic se genereaza; rapoartele cer proiectare vizuala |
| **Subtotal constructie** | **138** | **41** | **factor 3,4** |

### 26.4.2 Partea care nu se comprima

| Activitate | Estimare |
|---|---|
| Cicluri de import si corectie a metadatelor | 3-5 |
| Coloane Calculated si Rollup, chei alternative | 1 |
| Colectarea datelor de la celelalte departamente | 8-12 |
| Migrarea proiectelor in curs, cu confirmarea tehnologilor | 3-4 |
| Testare functionala si de securitate (36 de scenarii) | 5-7 |
| Testare de acceptanta cu utilizatori reali | 3-4 |
| Instruire si punere in functiune | 4-5 |
| Iteratie pe feedback, pe toate cele 6 valuri | 10-15 |
| **Subtotal** | **37-53** |

### 26.4.3 Totalul

| | Initial | Revizuit |
|---|---|---|
| Efort total | 130-158 zile-om | **78-94 zile-om** |
| La 1.5 zile pe saptamana | ~20 luni | **~12-14 luni** |
| La 3 zile pe saptamana | ~11 luni | **~6-7 luni** |

26.4.4 **Constructia se comprima de 3,4 ori. Proiectul se comprima de 1,7 ori.** Diferenta
este exact ceea ce trebuie inteles inainte de a planifica: dupa generare, mai mult de
jumatate din efortul ramas nu este constructie, ci colectare de date, testare cu oameni si
asteptarea realitatii.

26.4.5 Formularea inversa, poate mai utila: din cele 78-94 de zile ramase, **aproximativ 25
sunt lucru pe care il pot face eu** (generare, corectii, regenerari), iar **restul de 53-69
sunt lucru care cere prezenta unui om in companie** - discutii cu Productia despre linii,
citirea specificatiilor de furnizor, testarea cu manusi in hala, instruirea colegilor,
confirmarea proiectelor in curs.

## 26.5 Ce se schimba in modul de lucru

26.5.1 Ordinea recomandata se inverseaza fata de Sectiunea 16. Pana acum, constructia era
calea critica si datele veneau cand ajungea constructia la ele. Acum este invers.

| Saptamana | Ce se face |
|---|---|
| 1 | Se cer datele: clasificarea clientilor de la Sales, capabilitatile liniilor de la Productie, prima transa de materii prime de la Calitate. In scris, cu termen |
| 1 | Se creeaza mediul, solutia, editorul si politica DLP. Jumatate de zi |
| 1-2 | Se ruleaza provizionarea. Cicluri de import si corectie |
| 2 | Se genereaza si se importa vizualizarile, formularele, harta de site si rolurile |
| 2-3 | Formulele Calculated si Rollup, cheile alternative, nomenclatoarele din blueprint |
| 3-4 | Fluxurile Valului 1, cu testare |
| 4-6 | Datele de la departamente incep sa vina; se importa pe masura |
| 6-8 | Migrarea proiectelor in curs, testare de acceptanta, instruire |
| 8 | Punerea in functiune a Valului 1 |

26.5.2 Valul 1 poate fi in mainile utilizatorilor in aproximativ 8 saptamani in loc de 11,
dar **numai daca cererile de date pleaca in prima saptamana**. Daca pleaca in saptamana a
patra, calendarul nu se schimba deloc fata de estimarea initiala, oricat de repede s-ar
genera metadatele.

26.5.3 Aceasta este singura concluzie de actiune a sectiunii: viteza de generare muta
constrangerea de la constructor la organizatie. Cine planifica trebuie sa planifice
organizatia, nu constructia.

## 26.6 Limitele acestei estimari

26.6.1 Scriptul de provizionare nu a fost testat impotriva unui tenant real. Payloadurile
sunt validate structural - unicitatea numelor, lungimile, coerenta intervalelor, existenta
referintelor - dar Dataverse va respinge cateva elemente pentru motive care nu se pot
anticipa din afara. Cele 3-5 zile de cicluri de import si corectie din 26.4.2 sunt tocmai
pentru asta si sunt o estimare, nu o masuratoare.

26.6.2 Estimarea de 15 zile pentru cele 35 de fluxuri este cea mai putin sigura din tabel.
Un flux generat este un schelet corect; ce nu se poate genera este comportamentul lui cand
un ETA se schimba pe un proiect care are deja trei blocaje inchise si un gate in asteptare.
Acolo se duce timpul, si acolo estimarile se dovedesc de obicei optimiste.

26.6.3 Nu s-a inclus timpul de invatare a platformei. Daca este prima solutie Power
Platform construita, se adauga 10-15 zile pentru primele saptamani, care se recupereaza
partial ulterior.


<!-- ==================== S27-unde-traieste-ce.md ==================== -->

---

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


<!-- ==================== S28-acces-si-licentiere.md ==================== -->

---

# Sectiunea 28 - Acces si licentiere

Raspunde la intrebarile deschise IQ-02 si IQ-03 din Sectiunea 20, cu preturile de lista
confirmate in septembrie 2026. Revizuieste recomandarea din 17.1.2.1.

NOTA: preturile sunt de lista, in dolari, si se schimba. Un contract Enterprise sau un
reseller dau de regula altceva. Se confirma inainte de a fi puse intr-un buget.

## 28.1 Da, ruleaza integral cu partajare interna

28.1.1 Toti utilizatorii sunt angajati ai companiei, cu cont in Entra ID-ul companiei.
Nu exista utilizatori externi, invitati sau anonimi. Datele nu parasesc tenantul.

28.1.2 Partajarea se face **pe grupuri, nu pe persoane**. Cele 6 echipe din 11.1.2
corespund la 6 grupuri de securitate Entra ID. Cine intra in grup primeste accesul, cine
iese il pierde, iar administrarea ramane la IT sau HR - nu la constructorul solutiei.

28.1.3 Acest lucru este si o masura pentru RSC-02, dependenta de o singura persoana: daca
accesul s-ar da nominal, de catre constructor, plecarea lui ar bloca orice schimbare de
echipa.

## 28.2 Cum ajunge omul la aplicatie

Patru cai, toate catre aceeasi aplicatie si aceleasi date:

| Cale | Cum | Pentru cine |
|---|---|---|
| **Browser** | Un link direct, de forma `https://organizatie.crm4.dynamics.com/main.aspx?appid=...`, salvat la favorite | Birou: R&D, Calitate, Achizitii, KAM |
| **Teams** | Aplicatia model-driven se adauga ca fila sau ca aplicatie in Teams | Cea mai buna pentru adoptie: oamenii sunt deja acolo |
| **Telefon** | Aplicatia Power Apps din App Store sau Google Play, apoi aplicatia canvas `R&D Linie` | Hala si laborator: masuratori, senzorial, receptie mostra, productie 0 |
| **Ecran fix in hala** | Browser pe un ecran, cu ecranul public deschis permanent | Toata compania, fara autentificare individuala |

28.2.1 Aplicatia canvas functioneaza si offline, cu sincronizare la revenirea semnalului
(10.2.1.1). Este singura care are nevoie de instalarea unei aplicatii pe telefon.

## 28.3 Pasii concreti de acordare a accesului

Pentru fiecare persoana noua, o singura data:

| Pas | Cine il face | Unde |
|---|---|---|
| 1. Se adauga in grupul Entra ID al echipei | IT sau HR | Entra ID |
| 2. Grupul este deja legat de mediu, prin grupul de securitate al mediului | - | Facut o data, in Val 0 |
| 3. Grupul are deja rolul de securitate Dataverse atribuit | - | Facut o data, in Val 0 |
| 4. Aplicatia este deja partajata cu grupul | - | Facut o data, la publicare |
| 5. Primeste linkul | Manager R&D | Mail sau Teams |

28.3.1 Pasii 2-4 se fac o singura data, la constructie. In operare curenta ramane doar
pasul 1: **adaugarea in grup**. Fara aceasta structura, fiecare utilizator nou ar cere
cinci operatiuni manuale de la constructor.

28.3.2 Grupul de securitate al mediului este obligatoriu. Fara el, **orice** utilizator
licentiat din tenant apare ca utilizator in mediu, ceea ce strica si securitatea, si
rapoartele de licentiere.

## 28.4 Constrangerea reala: aplicatiile model-driven cer licenta premium

28.4.1 Aceasta este singura constrangere care nu se poate ocoli si trebuie inteleasa
inainte de orice discutie de buget:

> Aplicatiile model-driven folosesc Dataverse si sunt premium prin definitie. Orice
> utilizator care ruleaza o aplicatie model-driven are nevoie de o licenta cu drepturi
> premium Power Apps.

28.4.2 Consecinta practica: **licentele Microsoft 365 nu sunt suficiente.** E3 sau E5
includ Power Apps si Power Automate numai pentru conectori standard si fara Dataverse.
Nu dau acces la aceasta solutie.

28.4.3 Optiunile disponibile, cu preturile de lista din septembrie 2026:

| Optiune | Pret de lista | Ce da |
|---|---|---|
| **Power Apps Premium** | 20 USD / utilizator / luna (12 USD de la 2000 de licente) | Aplicatii nelimitate, Dataverse, conectori premium |
| **Power Apps per app** | 5 USD / utilizator / aplicatie / luna | O singura aplicatie, intr-un singur mediu |
| **Pay-as-you-go** | Contorizat prin Azure | Se plateste numai pentru utilizatorii care chiar deschid aplicatia intr-o luna |
| **Developer plan** | Gratuit | Numai mediu de dezvoltare, fara productie. Este ce se foloseste in Val 0 |

## 28.5 Cele doua populatii de utilizatori

### 28.5.1 Cei care lucreaza in sistem - aproximativ 30-35 de persoane

| Rol | Numar | De ce are nevoie de premium |
|---|---|---|
| Head of R&D, Manager R&D | 2 | Construiesc si administreaza |
| Tehnologi si suport R&D | 6-9 | Toata munca zilnica |
| KAM | 5-6 | Completeaza SCP-urile |
| Achizitii | 2-3 | Introduc ETA-urile |
| Calitate | 3-4 | Aproba specificatii, alergeni, HACCP |
| Planificare | 2 | Sloturi si blocaje |
| Productie, sefi de tura | 8-12 | Checklist productie 0, masuratori la linie |

**Cost**: 30 de licente Premium = 600 USD / luna, aproximativ **7 200 USD pe an**.

28.5.2 Nu exista varianta mai ieftina pentru acest grup. Per-app nu functioneaza pentru ei:
folosesc si aplicatia de birou, si pe cea de hala, in acelasi flux de lucru.

28.5.3 Cifra merita pusa in context: 7 200 USD pe an pentru departamentul care gestioneaza
130-180 de proiecte anual. Este sub costul unei singure lansari ratate.

### 28.5.4 Cei care doar se uita - aproximativ 200 de persoane

Aici este decizia costisitoare, si aici imi revizuiesc recomandarea.

| Varianta | Cost anual | Ce da | Ce pierde |
|---|---|---|---|
| A. Premium pentru toti | ~48 000 USD | Acces complet | Nejustificabil pentru citire |
| B. Per app pentru ecranul public | ~12 000 USD | Ecranul public real, cu filtre si timp real | - |
| C. Lista SharePoint, exportata zilnic de un flux | **0 USD suplimentar** | Statusul proiectelor, vizibil oricui are M365 | Nu e in timp real; filtrele sunt cele ale SharePoint |
| D. Pay-as-you-go pe ecranul public | Variabil | Ecranul real, dar se plateste numai pentru cine il deschide efectiv | Cost imprevizibil de la o luna la alta |

### 28.5.5 Observatia care schimba recomandarea

**Accesul de citire pentru cei 200 ar costa mai mult decat licentele intregului departament
care chiar lucreaza in sistem.** 12 000 USD pentru a te uita, fata de 7 200 USD pentru a
lucra.

28.5.6 **Recomandarea revizuita**, care inlocuieste 17.1.2.1 si raspunsul implicit la IQ-03:

| Pas | Ce se face | Cand |
|---|---|---|
| 1 | Se **construieste** ecranul public ca aplicatie separata, conform 10.1.5.4 | Val 2, aproximativ 2 zile |
| 2 | Se **lanseaza** prin varianta C: un flux exporta zilnic statusul intr-o lista SharePoint, vizibila oricui are M365, adaugata ca fila in Teams | Val 2 |
| 3 | Se **masoara** cati oameni distincti o deschid lunar | Val 2 si Val 3 |
| 4 | Daca depaseste constant pragul din 16.3, se cumpara per-app sau se activeaza pay-as-you-go pe aplicatia deja construita | Val 3 sau mai tarziu |

28.5.7 Motivul schimbarii: recomandarea initiala din 17.1.2.1 alegea varianta B pentru ca
se poate deriva C din ea, dar nu si invers. Argumentul de constructie ramane valabil -
aplicatia se construieste oricum. Ce se schimba este **momentul cumpararii licentelor**.

28.5.8 Cheltuirea a 12 000 USD pe an pentru un ecran despre care nu stim inca daca il
deschide cineva este exact genul de decizie care erodeaza increderea in proiect la prima
revizuire de buget. Se masoara intai, se plateste dupa. Aplicatia exista de la Val 2,
deci activarea licentelor este o decizie de o zi, nu de doua luni.

## 28.6 Power BI

28.6.1 Rapoartele din Val 3 (RAP-01, RAP-02, RAP-05 ... RAP-15) cer Power BI Pro pentru
cine le publica si le consuma. Sunt 5-8 persoane: Head of R&D, Manager R&D, conducere,
Achizitii pentru RAP-12.

28.6.2 Power BI Pro este inclus in Microsoft 365 E5. Daca aceste persoane au deja E5, nu
apare cost suplimentar. Daca au E3, se adauga licente Pro numai pentru ele.

28.6.3 Ecranul public **nu** se face in Power BI. Motivul este acelasi: consumatorii unui
raport publicat au nevoie de Pro, ceea ce readuce problema celor 200 de licente. Vizualizarea
gratuita pentru utilizatori fara Pro cere capacitate dedicata Fabric, care costa mai mult
decat toate variantele din 28.5.4.

## 28.7 Sinteza de cost

| Element | Cost anual de lista | Nota |
|---|---|---|
| 30 de licente Power Apps Premium | ~7 200 USD | Nenegociabil pentru cine lucreaza in sistem |
| Power BI Pro, 6 persoane | 0 - 1 000 USD | Zero daca au deja E5 |
| Capacitate Dataverse peste cea inclusa | 0 - 2 000 USD | Vezi 17.1.1.1; se monitorizeaza lunar in primul an |
| SharePoint | 0 USD | Inclus in M365 |
| Ecranul public, faza 1 (varianta C) | 0 USD | - |
| Ecranul public, faza 2 (daca se justifica) | ~12 000 USD | Decizie separata, dupa masurare |
| **Total pentru pornire** | **~7 200 - 10 200 USD pe an** | Fara ecranul public licentiat |

28.7.1 Licentele Premium se pot cumpara etapizat, pe valuri: 10-12 pentru Val 1 (R&D si
KAM), restul la Val 2, cand intra Achizitiile, Calitatea si Productia. Nu este nevoie de
toate 30 din prima luna.

28.7.2 Aceasta este si ordinea in care se pot justifica: fiecare val demonstreaza valoare
inainte ca urmatorul set de licente sa fie cerut.

## 28.8 Ce trebuie cerut de la IT

Se adauga la lista din 17.1, ca cerere concreta:

1. Un grup de securitate Entra ID pentru mediu, plus 6 grupuri pentru echipele din 11.1.2.
2. 10-12 licente Power Apps Premium pentru Val 1, cu optiune de extindere la 30-35.
3. Confirmarea ca licentele existente M365 sunt E3 sau E5, pentru a sti daca Power BI Pro
   este deja acoperit.
4. O decizie de principiu asupra variantei de acces pentru cei 200: se accepta pornirea cu
   lista SharePoint, cu reevaluare dupa 6 luni.
5. Un cont de serviciu licentiat, pentru conexiunile fluxurilor (17.1.3.1).

28.8.1 Punctul 5 este cel mai des uitat si cel mai scump cand lipseste: daca fluxurile
ruleaza pe contul personal al constructorului, plecarea lui sau schimbarea parolei opreste
toata automatizarea.


<!-- ==================== A2-backlog-enterprise.md ==================== -->

---

# Anexa A2 - Backlog enterprise, cu criterii de activare

Tot ce exista in blueprintul "R&D Suite Enterprise" si nu intra in Valurile 0-5. Nu este
o lista de lucruri respinse, ci o coada cu conditii de intrare.

## A2.1 Regula

**Nicio pozitie din acest backlog nu se construieste pentru ca apare intr-un inventar.**
Se construieste cand criteriul ei de activare este indeplinit, verificabil, cu date reale
din sistem.

A2.1.1 Criteriul de activare are trei parti: o **conditie de date** (exista suficiente
date reale ca modulul sa aiba ce afisa), o **conditie de proces** (exista cineva care
foloseste rezultatul saptamanal) si o **conditie de capacitate** (exista efortul de
constructie disponibil, fara sa se amane intretinerea a ceea ce exista deja).

A2.1.2 Toate trei trebuie indeplinite. Cea mai des ignorata este a doua: un modul corect
construit, fara un om care sa-l citeasca saptamanal, moare in trei luni si lasa in urma
date pe jumatate completate care strica rapoartele.

## A2.2 Nivelul Extins - Valurile 4 si 5

Cele 13 tabele care au deja loc in roadmap, cu criteriile lor.

| Modul | Tabele | Criteriu de activare | Val |
|---|---|---|---|
| Validare si feedback de client | `rd_validareclient`, `rd_feedbackclient` | Minimum 30 de proiecte au trecut prin etapa de mostra la client, in sistem | 4 |
| Reclamatii | `rd_reclamatie` | Calitatea accepta sa inregistreze reclamatiile aici, nu doar in sistemul propriu | 4 |
| Neconformitati si CAPA | `rd_neconformitate`, `rd_capa` | Minimum 20 de productii 0 inregistrate; Calitatea confirma ca inlocuieste evidenta proprie | 4 |
| Performanta furnizorilor | `rd_performantafurnizor`, `rd_incidentfurnizor` | Minimum 50 de livrari in `rd_leadtimeistoric`; Achizitiile folosesc scorecardul in discutiile de furnizor | 4 |
| Business case si buget | `rd_businesscase`, `rd_bugetproiect` | Financiarul confirma ca aloca buget pe proiect R&D, nu global | 5 |
| Cost de productie real | `rd_costproductie`, `rd_giveaway` | Controllingul furnizeaza costul real pe produs lunar, demonstrat 3 luni la rand (IQ-05) | 5 |
| Realizarea beneficiilor | `rd_beneficiu` | Minimum 20 de produse au trecut de revizuirea de 90 de zile | 5 |
| Registru de documente tehnice | `rd_documenttehnic` | Biblioteca SharePoint depaseste 3000 de fisiere si cautarea dupa metadate nu mai e suficienta | 5 |

## A2.3 Amanate cu conditie - dupa Valul 5

### A2.3.1 Predictie si simulare

| Element | Criteriu de activare |
|---|---|
| Modele predictive de durata si intarziere | Minimum 100 de proiecte inchise, cu etape complet inregistrate, si minimum 12 luni de date. Acuratetea se masoara pe date retinute inainte de a fi expusa cuiva |
| Predictia costului final | Cost real disponibil pentru minimum 50 de produse |
| Predictia intarzierii furnizorului | Minimum 200 de livrari in istoricul de lead time |
| Scenario Simulator | Modelele de mai sus valideaza; altfel simuleaza pe ipoteze inventate |
| Detectarea bottleneck-ului de capacitate | Minimum 12 luni de date de incarcare reala |

A2.3.2 Regula pe care documentul Enterprise o formuleaza corect si care se pastreaza ca
atare: **pana la validarea modelelor se folosesc reguli si scoruri transparente, nu
predictii.** Scorul de sanatate din 24.3 si scorul de prioritate din A1.1 sunt exact acest
lucru: explicabile, verificabile, gresite in mod previzibil.

A2.3.3 O predictie gresita afisata cu doua zecimale distruge increderea in tot sistemul,
nu doar in modul. Costul erorii nu este simetric.

### A2.3.4 Copilot

| Element | Criteriu de activare |
|---|---|
| R&D Copilot | Valurile 1-3 in productie, cu minimum 6 luni de date consecvente. Politica DLP verificata pentru conectorii necesari |
| Supply Chain Copilot | Modulul de materii prime folosit efectiv de Achizitii, cu ETA-uri introduse in peste 80% din cazuri |
| Executive Copilot | Indicatorii din Sectiunea 13 calculati automat si verificati manual timp de un trimestru |

A2.3.5 Conditia care nu apare in documentul Enterprise si care este cea mai importanta:
**Copilotul raspunde din datele existente, deci mosteneste toate golurile lor.** Intrebarea
"de ce intarzie proiectul 26025" primeste un raspuns util numai daca blocajele au fost
inregistrate cu sursa si data. Daca nu, Copilotul va inventa o explicatie plauzibila, ceea
ce e mai rau decat sa nu raspunda.

### A2.3.6 Sustenabilitate

| Element | Criteriu de activare |
|---|---|
| `SustainabilityAssessment` | Exista o metodologie interna aprobata, cu factori de emisie din sursa citabila |
| `CarbonFactor` | Idem, plus o persoana responsabila de actualizarea factorilor |
| Scoruri ESG | Exista cerinta externa reala - client, reglementare sau raportare de grup |

A2.3.7 Documentul Enterprise avertizeaza corect: "Scorurile nu trebuie prezentate extern
drept LCA completa fara metodologie si factori aprobati." Se intareste: pana la
metodologie aprobata, modulul nu se construieste deloc. Un scor de carbon calculat cu
factori luati de pe internet si pus intr-o prezentare catre client este un risc juridic,
nu o initiative de mediu.

### A2.3.8 Cost extins

| Element | Criteriu de activare |
|---|---|
| Cost-to-Serve, Distribution Cost | Logistica furnizeaza costul pe ruta si pe client, lunar |
| Energy Cost, Maintenance Cost | Exista contorizare pe linie, nu doar pe fabrica |
| TCO, Profitability Waterfall | Costul real de productie functioneaza de minimum 6 luni |
| Hidden Cost | Retestarile, rework-ul si blocajele sunt inregistrate consecvent - adica Valurile 2-3 sunt adoptate |
| Cost Reduction Pipeline | Minimum 10 proiecte de tip Optimizare cost generate din revizuiri |

### A2.3.9 Portofoliu si program

| Element | Criteriu de activare |
|---|---|
| `Portfolio`, `PortfolioReview` | Exista mai mult de un manager R&D sau o structura de portofoliu reala |
| `Program`, `ProgramProject` | Exista proiecte grupate care se gestioneaza impreuna, nu doar se raporteaza impreuna |
| `WIPControl` | Limitele de WIP se dovedesc necesare dupa un an de urmarire a incarcarii |

A2.3.10 La un singur departament R&D cu un manager si 6 tehnologi, portofoliul este o
vizualizare filtrata. Devine entitate cand cineva raspunde de el ca functie distincta.

### A2.3.11 Innovation front-end

| Element | Criteriu de activare |
|---|---|
| Idea Management | Exista o sursa de idei in afara cererilor comerciale si cineva care le triaza |
| Opportunity Management | Idem, plus o etapa de evaluare inaintea SCP |
| Technology Scouting, Market Intelligence | Exista un rol care face asta ca sarcina, nu ocazional |
| TRL si Innovation Portfolio | Compania face cercetare cu TRL sub 6, nu doar dezvoltare de produs |

A2.3.12 Aceasta este zona cea mai putin potrivita cu realitatea descrisa in briefingul
initial. Compania primeste cereri de la KAM si le transforma in produse. Un modul de
management al ideilor intr-o organizatie care nu genereaza idei nestructurate este un
ecran gol care erodeaza increderea in restul sistemului.

### A2.3.13 Altele

| Element | Criteriu de activare |
|---|---|
| `Calibration`, `LaboratoryEquipment` | Calitatea confirma ca muta evidenta de calibrare aici din sistemul propriu |
| `ResourceBooking`, `EnterpriseCalendar` | Conflictele de rezervare a laboratorului devin o problema reala si masurabila |
| `Training`, `Competence` | HR confirma ca nu dubleaza sistemul propriu de instruire |
| `TechnicalPlaybook` | Exista minimum 30 de lectii aprobate din care sa se scrie un playbook |
| Potrivire semantica a lectiilor | Minimum 150 de lectii aprobate; potrivirea pe reguli (25.4.4) da sub 50% acceptare |
| Integrare cu aplicatia de planificare | Exista API stabil pe partea de planificare (IQ-06) |
| Import automat de preturi din SAP | IT furnizeaza un export programat |
| Portal pentru clienti | Discutie de licentiere si securitate proprie, separata |

## A2.4 Elemente respinse definitiv

Nu au criteriu de activare. Se resping pe motive de arhitectura, nu de calendar.

| Element | Motiv |
|---|---|
| `Person`, `Role`, `Department` ca tabele proprii | Dataverse are `systemuser`, echipe si roluri de securitate. O ierarhie paralela creeaza doua surse de adevar si o gaura de securitate. Se pastreaza `rd_profiltehnolog`, care extinde `systemuser` fara sa-l duplice |
| `ProjectDigitalTwin` ca tabela | Este o vizualizare agregata peste date existente. Materializarea ei inseamna sincronizare permanenta, fara informatie noua |
| `SupplierHealth`, `CustomerHealth` ca tabele | Sunt scoruri calculate. Devin coloane pe furnizor si client, plus snapshot daca tendinta conteaza |
| Registru de documente **in locul** generarii de foldere | Contrazice decizia de arhitectura 4 din briefingul initial. Vezi 22.5.1. Registrul se adauga peste generare, nu in locul ei |
| Prefixul `rdcdi_` | Vezi 22.5.2 |

## A2.5 Cum se reevalueaza backlogul

A2.5.1 O data pe an, la revizuirea anuala din 13.7.2 si 14.6.1, se parcurge acest backlog
si se verifica, pentru fiecare pozitie, daca cele trei criterii din A2.1.1 sunt
indeplinite.

A2.5.2 Se activeaza **cel mult doua module pe an**, si numai daca intretinerea celor
existente nu a fost amanata. Aceasta este singura regula din tot blueprintul care apara
solutia de propriul ei succes: un sistem care functioneaza atrage cereri de extindere mai
repede decat le poate absorbi o singura persoana.

A2.5.3 Pozitiile care raman trei ani in backlog fara sa fie activate se sterg din el, cu
o nota. Un backlog care creste la nesfarsit inceteaza sa mai fie un instrument de decizie
si devine o lista de dorinte.
