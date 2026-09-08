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
