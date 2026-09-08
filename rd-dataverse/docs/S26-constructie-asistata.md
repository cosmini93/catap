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
