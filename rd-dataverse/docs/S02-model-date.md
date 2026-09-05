# Sectiunea 2 - Modelul de date Dataverse

## 2.0 Reguli generale de modelare

2.0.1 Prefix de editor: `rd`. Toate tabelele si coloanele au nume logic `rd_...`, fara
diacritice, fara spatii, cu cuvinte lipite sau separate prin `_` doar acolo unde
lizibilitatea o cere. Prefixul nu se schimba niciodata dupa primul export de solutie.

2.0.2 Solution unica: `RDSuitaDigitala`, editor `RD Digital (rd)`. Tot ce se construieste
intra in ea, de la primul tabel. Export saptamanal, managed si unmanaged, pe OneDrive,
in `/RD_Solutions/{AAAALLZZ}_RDSuitaDigitala_v{n}.zip`.

2.0.3 Coloana primara: fiecare tabela are o coloana primara de tip Text cu rol de
identificator lizibil. Unde exista numar de document, coloana primara este Autonumber.
Unde nu, coloana primara se completeaza automat prin flux sau regula de business, ca sa
nu ramana niciodata "Nou".

2.0.4 Toate statusurile sunt Choice, niciodata text liber. Toate seturile de optiuni
folosite in mai multe tabele sunt Choice globale (Global Option Set), definite o singura
data.

2.0.5 Se folosesc doua campuri de stare native: `statecode` (Active / Inactive) si
`statuscode`. Statusul de business al proiectului este o coloana Choice proprie
`rd_status`, nu `statuscode`, pentru ca ciclul de business nu se suprapune peste ciclul
tehnic al inregistrarii.

2.0.6 Datele fara ora se modeleaza `Date Only`, cu comportament `User Local` doar acolo
unde ora conteaza (masuratori, trial, miscari de mostra); in rest `Date Only` cu
comportament `Time Zone Independent`, ca sa nu apara decalaje de o zi intre amplasamente.

2.0.7 Auditul se activeaza la nivel de mediu si, explicit, pe toate tabelele din 2.1-2.9
si pe coloanele de status, termen, cantitate, decizie si aprobare.

2.0.8 Rollup-urile Dataverse se recalculeaza la interval de o ora. Unde valoarea trebuie
sa fie exacta in momentul citirii (scor de prioritate, conformitate), se foloseste o
coloana obisnuita scrisa de flux, nu Rollup.

2.0.9 NOTA de platforma: Calculated si Rollup nu pot referi decat relatii 1:N directe si
nu accepta filtre pe campuri de tip lookup din alta tabela. Toate calculele pe mai multe
niveluri (alergeni din reteta, scor de prioritate, T-Total cu oprirea ceasului) se fac cu
flux Power Automate programat sau declansat, si se scriu in coloane simple.

2.0.10 Zecimale: pretul si costul in `Currency` cu 4 zecimale (materiile prime au costuri
sub 1 leu pe kilogram in unele cazuri); cantitatile in `Decimal` cu 4 zecimale; procentele
in `Decimal` cu 2 zecimale, interval 0-100.

## 2.1 TBL-01 Solicitare (SCP)

Nume: `rd_solicitare`. Rol: cererea deschisa de KAM, inainte de a exista proiect.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar SCP | rd_numarscp | Autonumber | Da | SCP-{AA}-{SEQ:0000} | Se genereaza la salvare | Coloana primara |
| Client | rd_client | Lookup (rd_client) | Da | - | Clientul din nomenclator | Nu se accepta client liber |
| Lant sau canal | rd_canal | Choice | Da | Retail modern / Retail traditional / HoReCa / Industrial / Export / Marca proprie | - | Choice global CANAL |
| KAM solicitant | rd_kam | Lookup (systemuser) | Da | - | Implicit utilizatorul curent | Se pastreaza si daca omul pleaca |
| Sursa solicitarii | rd_sursa | Choice | Da | Aplicatie / Mail preluat de suport R&D / Sedinta comerciala | Implicit Aplicatie | Varianta de rezerva se marcheaza explicit |
| Preluat de | rd_preluatde | Lookup (systemuser) | Nu | - | Obligatoriu daca sursa = Mail preluat | Business rule |
| Produs dorit | rd_produsdorit | Text (200) | Da | - | - | Denumire de lucru |
| Descriere cerinta | rd_descriere | Text Area (4000) | Da | - | - | Text liber de la client |
| Gramaj (g) | rd_gramaj | Decimal (2) | Da | 1 - 20000 | - | Pe bucata |
| Numar bucati pe ambalaj | rd_bucatiambalaj | Whole Number | Nu | 1 - 500 | - | - |
| Dimensiuni cerute | rd_dimensiuni | Text (100) | Nu | LxlxH mm | - | Text structurat, validat vizual |
| Tip ambalare | rd_tipambalare | Choice | Da | Punga / Tava / Bax direct / Vrac / Flow-pack / Termoformat | - | Choice global AMBALARE |
| Volum estimat anual (kg) | rd_volumanual | Decimal (2) | Da | 0 - 10000000 | Intra in scorul de prioritate | Banda, nu liniar |
| Termen dorit de client | rd_termendorit | Date Only | Da | >= azi | - | Nu este angajament |
| Termen impus extern | rd_termenimpus | Yes/No | Da | Implicit Nu | Da doar cu tip si data | Listare, sezon |
| Tip termen impus | rd_tiptermenimpus | Choice | Nu | Listare retail / Sezon / Licitatie / Lansare client / Altul | Obligatoriu daca rd_termenimpus = Da | - |
| Motivul cererii | rd_motivcerere | Choice | Da | Client nou / Extindere portofoliu / Inlocuire produs / Cerere de pret / Reformulare / Reactie la concurenta / Reglementare | - | Choice global MOTIVCERERE |
| Referinta de comparatie | rd_tipreferinta | Choice | Da | Produs concurenta / Produs actual / Mostra client / Specificatie client / Inexistenta | Obligatoriu la deschidere | Vezi 6.4 |
| Detalii referinta | rd_detaliireferinta | Text (300) | Nu | - | Obligatoriu daca referinta != Inexistenta | - |
| Cerinte de eticheta | rd_cerinteeticheta | Text Area (2000) | Nu | - | - | Limba, logo, declaratii |
| Cerinte de ambalaj | rd_cerinteambalaj | Text Area (2000) | Nu | - | - | Material, print, dimensiune bax |
| Rezultat triaj | rd_rezultattriaj | Choice | Nu | Acceptata / Respinsa / Amanata | Se completeaza doar de Manager R&D | Vezi 2.1.1 |
| Motiv triaj | rd_motivtriaj | Lookup (rd_motiv) | Nu | - | Obligatoriu daca rezultat != Acceptata | Nomenclator de motive |
| Comentariu triaj | rd_comentariutriaj | Text Area (2000) | Nu | - | Obligatoriu daca rezultat = Respinsa | - |
| Data triaj | rd_datatriaj | Date and Time | Nu | - | Se scrie automat la salvarea rezultatului | User Local |
| Amanata pana la | rd_amanatapanala | Date Only | Nu | > azi | Obligatoriu daca rezultat = Amanata | Reintra automat in coada |
| Proiect generat | rd_proiect | Lookup (rd_proiect) | Nu | - | Se completeaza de flux la acceptare | Referential |
| Status solicitare | rd_statussolicitare | Choice | Da | Ciorna / Trimisa / In triaj / Acceptata / Respinsa / Amanata | Implicit Ciorna | Choice local |

2.1.1 Regula de triaj: `rd_rezultattriaj` nu poate fi modificat decat de rolul Manager
R&D (ROL-02). O solicitare respinsa nu se sterge niciodata; ramane consultabila ca
istoric, conform 15.5.

2.1.2 O solicitare amanata reintra in lista de triaj automat la data din
`rd_amanatapanala`, prin fluxul FLX-14.

## 2.2 TBL-02 Proiect CDI

Nume: `rd_proiect`. Rol: radacina intregii solutii. Aproape toate celelalte tabele sunt
copii ai acestei tabele.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Cod proiect | rd_codproiect | Autonumber | Da | {AA}{SEQ:000}, exemplu 26025 | Se genereaza la acceptare, succesiv pe an | Coloana primara, imutabila |
| Nume produs | rd_numeprodus | Text (200) | Da | - | - | Intra in numele folderului |
| Denumire completa | rd_denumire | Calculated (Text) | Da | {rd_codproiect}_{rd_numeprodus} | Calculata | Folosita in denumirea fisierelor |
| Solicitare sursa | rd_solicitare | Lookup (rd_solicitare) | Nu | - | - | Referential |
| Proiect parinte | rd_proiectparinte | Lookup (rd_proiect) | Nu | - | Doar pentru versiuni cu sufix .1 | Auto-referential, vezi 2.2.2 |
| Sufix versiune | rd_sufixversiune | Text (10) | Nu | .1, .2, ... | Obligatoriu daca exista parinte | - |
| Tip proiect | rd_tipproiect | Choice | Da | Produs nou / Reformulare / Abatere / Transfer pe alta linie / Optimizare cost / Ambalaj nou | - | Choice global TIPPROIECT |
| Client | rd_client | Lookup (rd_client) | Da | - | Se preia din solicitare | - |
| KAM | rd_kam | Lookup (systemuser) | Da | - | Se preia din solicitare | - |
| Tehnolog alocat | rd_tehnolog | Lookup (systemuser) | Nu | - | Obligatoriu la trecerea in Acceptat - planificat | Vezi 2.20 |
| Manager R&D | rd_manager | Lookup (systemuser) | Da | - | Implicit managerul de departament | - |
| Linie de productie vizata | rd_linie | Lookup (rd_linie) | Nu | - | Obligatoriu la trecerea in In dezvoltare | Una din cele 9 |
| Amplasament | rd_amplasament | Choice | Da | Amplasament 1 / Amplasament 2 | Se preia din linie | Choice global AMPLASAMENT |
| Status | rd_status | Choice | Da | Vezi 4.6 / lista din 2.2.1 | Tranzitii controlate de business rule | Choice global STATUSPROIECT |
| Motiv status | rd_motivstatus | Lookup (rd_motiv) | Nu | - | Obligatoriu pentru Respins, Suspendat, Abandonat, Blocat | - |
| Gramaj (g) | rd_gramaj | Decimal (2) | Da | 1 - 20000 | Diferenta de gramaj = proiect nou | Vezi 2.2.3 |
| Dimensiuni | rd_dimensiuni | Text (100) | Nu | - | Diferenta de dimensiune = proiect nou | - |
| Tip ambalare | rd_tipambalare | Choice | Da | Choice AMBALARE | - | - |
| Volum estimat anual (kg) | rd_volumanual | Decimal (2) | Da | 0 - 10000000 | Intra in scor | - |
| Are materie prima noua | rd_aremp | Yes/No | Da | Implicit Nu | Se scrie de flux din liniile de MP | Conditioneaza livrabile |
| Numar MP noi | rd_numarmpnoi | Rollup (Count) | Nu | 0 - n | Numara rd_mpproiect cu rd_esteno = Da | Rollup |
| Termen propus | rd_termenpropus | Date Only | Nu | - | Generat de sistem la acceptare, FLX-03 | Nu se editeaza manual |
| Termen negociat | rd_termennegociat | Date Only | Nu | - | Rezultatul discutiei cu KAM | Termenul catre client |
| Termen realizat | rd_termenrealizat | Date Only | Nu | - | Se scrie la trecerea in Finalizat | - |
| Abatere fata de termen (zile) | rd_abateretermen | Whole Number | Nu | -999 - 999 | rd_termenrealizat - rd_termennegociat | Scris de flux |
| Data acceptare | rd_dataacceptare | Date Only | Nu | - | Se scrie la generarea codului | Start ceas |
| Durata standard (zile) | rd_duratastandard | Whole Number | Da | 1 - 365, implicit 14 | Din sablonul de etape | Vezi Sectiunea 14 |
| Zile blocate cumulat | rd_zileblocate | Rollup (Sum) | Nu | 0 - 999 | Suma impactului din rd_blocaj inchise | Vezi 2.11 |
| T-Total zile nete | rd_ttotalnet | Whole Number | Nu | - | (realizat - acceptare) - zile blocate | Scris de FLX-16 |
| Scor prioritate | rd_scorprioritate | Whole Number | Nu | 0 - 100 | Recalculat saptamanal, FLX-10 | Nu se editeaza manual |
| Banda prioritate | rd_banda | Choice | Nu | P1 / P2 / P3 / P4 | Derivata din scor, vezi 2.2.4 | Choice global BANDA |
| Scor suprascris | rd_scorsuprascris | Whole Number | Nu | 0 - 100 | Doar rol Manager operational vanzari | Audit obligatoriu |
| Motiv suprascriere | rd_motivsuprascriere | Text Area (1000) | Nu | - | Obligatoriu daca exista scor suprascris | Business rule |
| Data suprascrierii | rd_datasuprascriere | Date and Time | Nu | - | Automat | - |
| Zile in coada | rd_zilecoada | Whole Number | Nu | 0 - 999 | azi - data acceptare, cat timp nu e In dezvoltare | Alimenteaza imbatranirea |
| Referinta de comparatie | rd_referinta | Lookup (rd_referinta) | Nu | - | Obligatorie la deschidere | Vezi 2.13 |
| Cod material SAP produs finit | rd_codsapfinit | Text (20) | Nu | - | Se introduce dupa creare in SAP | Niciodata scriere in SAP |
| Data cod SAP | rd_datacodsap | Date Only | Nu | - | - | - |
| Slot testare propus | rd_slottestare | Date Only | Nu | - | Estimare negociabila, nu blocanta | Vezi 4.2 |
| Schimb propus | rd_schimb | Choice | Nu | 07-15 / 15-23 / 23-07 | - | Choice global SCHIMB |
| Folder SharePoint | rd_folderurl | Text (500) | Nu | URL | Scris de FLX-02 | - |
| Procent livrabile realizate | rd_procentlivrabile | Decimal (2) | Nu | 0 - 100 | Livrabile realizate / obligatorii aplicabile | Scris de FLX-05 |
| Toate livrabilele obligatorii OK | rd_livrabileok | Yes/No | Nu | - | Conditie pentru trecerea in Finalizat | Business rule |
| Data ultimei activitati | rd_ultimaactivitate | Date and Time | Nu | - | Scris la orice modificare de copil | Detecteaza proiecte uitate |

### 2.2.1 Statusurile proiectului

Lista finala, pornind de la propunerea din 4.6, cu doua completari argumentate:

| Nr | Status | Cine il seteaza | Conditie de intrare | Ceas T-Total |
|---|---|---|---|---|
| 1 | Solicitat | Sistem, la trimiterea SCP | SCP trimis | Nu porneste |
| 2 | In evaluare | Manager R&D | Triaj inceput | Nu porneste |
| 3 | Acceptat - planificat | Sistem la acceptare | Cod generat, tehnolog si termen propus | Porneste |
| 4 | In dezvoltare | Tehnolog | Linie stabilita, plan de dezvoltare aprobat | Curge |
| 5 | In asteptare materie prima | Sistem sau tehnolog | Exista MP noua fara receptie | Oprit |
| 6 | In testare | Tehnolog | Exista cel putin un trial deschis | Curge |
| 7 | Blocat | Manager R&D | Exista blocaj activ extern | Oprit |
| 8 | In implementare | Tehnolog | ST finala aprobata | Curge |
| 9 | Productie 0 | Tehnolog | Plan IPN aprobat | Curge |
| 10 | In revizuire | Sistem | La 30 de zile de la implementare | Nu conteaza |
| 11 | Finalizat | Manager R&D | Toate livrabilele obligatorii realizate | Se opreste definitiv |
| 12 | Respins | Manager R&D | Din triaj, cu motiv | Nu porneste |
| 13 | Suspendat | Manager R&D | Decizie interna, cu motiv si data de reluare | Oprit |
| 14 | Abandonat | Manager R&D | Cu motiv obligatoriu | Se opreste definitiv |

PROPUNERE: s-au adaugat statusurile "In revizuire" (10) si s-a separat "Suspendat" de
"Blocat". Motiv: revizuirea post-implementare din Sectiunea 8 are responsabil si termen
propriu si nu poate trai sub "Finalizat"; iar "Blocat" este cauzat extern si opreste
ceasul, in timp ce "Suspendat" este o decizie interna si trebuie sa se vada separat la
analiza anuala.

2.2.1.1 Fiecare status afiseaza intotdeauna, in formular si in vizualizare: data
planificata (`rd_termennegociat`), responsabilul (`rd_tehnolog`), urmatorul livrabil
scadent si cine il datoreaza. Ultimele doua se obtin din TBL-03 prin coloanele
`rd_urmatorullivrabil` si `rd_urmatorulresponsabil`, scrise de FLX-05.

### 2.2.2 Proiecte-copil

Relatia `rd_proiectparinte` este referentiala, nu parentala. Motiv: un proiect-copil are
ciclu de viata propriu si nu trebuie sters odata cu parintele. La crearea copilului,
FLX-04 copiaza: client, KAM, referinta de comparatie, linia, reteta curenta ca versiune
noua si legatura catre folderul parintelui. Documentele parintelui raman accesibile prin
lookup, nu se dubleaza fizic.

### 2.2.3 Regula "proiect nou, nu varianta"

Orice diferenta de gramaj, dimensiune sau reteta inseamna proiect nou. Se implementeaza
ca business rule pe formular: la modificarea `rd_gramaj`, `rd_dimensiuni` sau la crearea
unei versiuni de reteta cu alt set de ingrediente pe un proiect aflat in status >= 8, se
blocheaza salvarea si se propune butonul "Creeaza proiect-copil". Sufixul `.1` se
foloseste doar pentru abateri sau versiuni ale aceluiasi proiect.

### 2.2.4 Benzile de prioritate

| Banda | Scor | Semnificatie operationala |
|---|---|---|
| P1 | 80 - 100 | Se lucreaza acum, are slot rezervat |
| P2 | 60 - 79 | Se lucreaza in urmatoarele 2 saptamani |
| P3 | 35 - 59 | In coada, fara slot rezervat |
| P4 | 0 - 34 | Se lucreaza cand exista capacitate libera |

## 2.3 TBL-03 Livrabil de proiect

Nume: `rd_livrabil`. Rol: inlocuieste cele ~30 de coloane-bifa din centralizatorul actual.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire livrabil | rd_name | Text (150) | Da | - | Se preia din sablon | Coloana primara |
| Cod livrabil | rd_codlivrabil | Text (10) | Da | LIV-01 ... LIV-34 | Din sablon | Pentru raportare stabila |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascada la stergere |
| Sablon sursa | rd_sablon | Lookup (rd_sablonlivrabil) | Nu | - | - | Trasabilitate |
| Faza | rd_faza | Choice | Da | 00 Solicitare ... 08 Dosar validat | Din sablon | Choice global FAZA |
| Ordine in faza | rd_ordine | Whole Number | Da | 1 - 99 | Din sablon | Sortare |
| Responsabil rol | rd_rolresponsabil | Choice | Da | Choice global ROL | Din sablon | Cine datoreaza livrabilul |
| Responsabil persoana | rd_responsabil | Lookup (systemuser) | Nu | - | Se rezolva din rol la generare | Poate fi reatribuit |
| Obligatoriu | rd_obligatoriu | Yes/No | Da | - | Din sablon | Vezi 4.3 |
| Conditie de aplicabilitate | rd_conditie | Choice | Da | Intotdeauna / Doar MP noua / Doar eticheta noua / Doar client nou / Doar ambalaj nou / Doar linie nesetata / Doar export | Din sablon | Vezi 4.2 |
| Aplicabil | rd_aplicabil | Yes/No | Da | Implicit Da | Evaluat de FLX-05 la generare si la schimbarea conditiei | Livrabilele neaplicabile raman vizibile, gri |
| Termen | rd_termen | Date Only | Nu | - | Calculat din etapa si offset din sablon | Editabil de manager |
| Data realizarii | rd_datarealizare | Date Only | Nu | - | Se scrie la trecerea in Realizat | - |
| Status livrabil | rd_statuslivrabil | Choice | Da | Neinceput / In lucru / Trimis spre aprobare / Realizat / Respins / Nu se aplica | Implicit Neinceput | Choice global STATUSLIVRABIL |
| Document atasat | rd_document | Text (500) | Nu | URL SharePoint | Se completeaza la incarcarea fisierului | Vezi 2.3.1 |
| Necesita document | rd_necesitadocument | Yes/No | Da | Din sablon | Nu poate trece in Realizat fara document | Business rule |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | Din sablon (rol) | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Zile intarziere | rd_zileintarziere | Whole Number | Nu | 0 - 999 | max(0, azi - termen) daca nu e realizat | Scris de FLX-08 |
| Observatii | rd_observatii | Text Area (2000) | Nu | - | - | - |

2.3.1 Documentul nu se stocheaza in Dataverse. Coloana `rd_document` retine URL-ul
fisierului din biblioteca SharePoint a proiectului. Motiv: fisierele trebuie sa ramana in
SharePoint pentru versionare, co-editare si retentie, iar stocarea in Dataverse consuma
capacitate File scumpa si dubleaza sursa de adevar.

2.3.2 NOTA: livrabilele care "nu se aplica" nu se sterg si nu se ascund. Raman in lista
cu status `Nu se aplica`, pentru ca la audit trebuie demonstrat ca decizia de
neaplicabilitate a fost luata constient, nu ca livrabilul a fost omis.

## 2.4 TBL-04 Sablon de livrabil

Nume: `rd_sablonlivrabil`. Rol: sursa din care se genereaza TBL-03 la acceptarea
proiectului. Continutul complet este in Sectiunea 4 si in `data/sablon-livrabile.json`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | - | - | Coloana primara |
| Cod livrabil | rd_codlivrabil | Text (10) | Da | LIV-nn | Unic | - |
| Tip proiect aplicabil | rd_tipproiect | Choice (multi) | Da | Choice TIPPROIECT | Sablonul se filtreaza pe tipul proiectului | Multi-select |
| Faza | rd_faza | Choice | Da | Choice FAZA | - | - |
| Ordine | rd_ordine | Whole Number | Da | 1 - 99 | - | - |
| Etapa asociata | rd_etapa | Lookup (rd_sabloneteapa) | Nu | - | Din ea se ia termenul | - |
| Offset termen (zile) | rd_offsettermen | Whole Number | Da | 0 - 365 | Zile de la data de acceptare | - |
| Rol responsabil | rd_rolresponsabil | Choice | Da | Choice ROL | - | - |
| Rol aprobator | rd_rolaprobator | Choice | Nu | Choice ROL | - | - |
| Obligatoriu | rd_obligatoriu | Yes/No | Da | - | Vezi 4.3 | - |
| Necesita document | rd_necesitadocument | Yes/No | Da | - | - | - |
| Conditie de aplicabilitate | rd_conditie | Choice | Da | Ca in TBL-03 | - | - |
| Sablon Word | rd_sablonword | Text (300) | Nu | Nume fisier | Pentru generarea documentului | Vezi FLX-12 |
| Activ | rd_activ | Yes/No | Da | Implicit Da | Sablonul dezactivat nu mai genereaza | Istoricul ramane |

## 2.5 TBL-05 Etapa de proiect si TBL-06 Sablon de etapa

Nume: `rd_etapa`, `rd_sablonetapa`. Rol: masurarea duratelor reale pe etapa si baza
pentru T-Total.

### 2.5.1 rd_sablonetapa

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire etapa | rd_name | Text (100) | Da | - | - | Coloana primara |
| Cod etapa | rd_codetapa | Text (10) | Da | ETP-nn | Unic | - |
| Ordine | rd_ordine | Whole Number | Da | 1 - 20 | - | - |
| Tip proiect | rd_tipproiect | Choice (multi) | Da | Choice TIPPROIECT | - | - |
| Durata standard (zile lucratoare) | rd_duratastandard | Whole Number | Da | 1 - 90 | Vezi Sectiunea 14 | Setata o data la configurare |
| Durata propusa de sistem | rd_duratapropusa | Decimal (1) | Nu | - | Mediana duratelor reale, dupa 6-12 luni | Scrisa de FLX-17, nu se aplica automat |
| Rol responsabil | rd_rolresponsabil | Choice | Da | Choice ROL | - | - |
| Opreste ceasul la blocaj | rd_oprsteceasul | Yes/No | Da | Implicit Da | - | - |
| Activ | rd_activ | Yes/No | Da | - | - | - |

### 2.5.2 rd_etapa

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (100) | Da | - | Din sablon | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Sablon | rd_sablon | Lookup (rd_sablonetapa) | Nu | - | - | - |
| Ordine | rd_ordine | Whole Number | Da | 1 - 20 | - | - |
| Data start planificata | rd_startplanificat | Date Only | Da | - | Din offset | - |
| Data final planificata | rd_finalplanificat | Date Only | Da | - | Start + durata | - |
| Data start reala | rd_startreal | Date Only | Nu | - | La prima activitate pe etapa | - |
| Data final reala | rd_finalreal | Date Only | Nu | - | La inchiderea etapei | - |
| Durata reala bruta (zile) | rd_duratabruta | Whole Number | Nu | - | final real - start real | Scris de flux |
| Zile blocate pe etapa | rd_zileblocate | Rollup (Sum) | Nu | 0 - 999 | Din blocaje legate de etapa | - |
| Durata reala neta (zile) | rd_duratanet | Whole Number | Nu | - | bruta - blocate | Baza pentru T-Total |
| Abatere fata de standard | rd_abatere | Whole Number | Nu | -99 - 999 | neta - durata standard | Alimenteaza Sectiunea 14 |
| Status etapa | rd_statusetapa | Choice | Da | Neinceputa / In lucru / Blocata / Finalizata / Sarita | - | Choice global STATUSETAPA |
| Motiv sarire | rd_motivsarire | Text (300) | Nu | - | Obligatoriu daca status = Sarita | - |

## 2.6 TBL-07 Materie prima de proiect si TBL-08 Iteratie de furnizor

### 2.6.1 rd_mpproiect (Materie prima de proiect)

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Materie prima catalog | rd_materieprima | Lookup (rd_materieprima) | Nu | - | Gol daca este MP complet noua | - |
| Este noua | rd_estenoua | Yes/No | Da | Implicit Nu | Da declanseaza livrabilele conditionate | Scrie rd_aremp pe proiect |
| Categorie | rd_categorie | Choice | Da | Faina / Grasimi / Zaharuri / Lactate / Oua / Drojdie si afanatori / Amelioratori / Umpluturi / Fructe / Ciocolata / Arome / Aditivi / Ambalaje / Altele | - | Choice global CATEGORIEMP |
| Cantitate in reteta (kg/100kg) | rd_cantitate | Decimal (4) | Nu | 0 - 100 | - | Redundant cu linia de reteta, tinut pentru faza de plan |
| Furnizor propus | rd_furnizor | Lookup (rd_furnizor) | Nu | - | - | - |
| Status ciclu MP | rd_statusmp | Choice | Da | Identificata / Mostra ceruta / Mostra primita / In testare / Conditii ST emise / ST interna MP / Aprobata Calitate / Respinsa / Cod SAP creat / Comanda plasata / Receptionata | Vezi 4.4 | Choice global STATUSMP |
| Initiator cerere mostra | rd_initiator | Choice | Nu | R&D / Achizitii | - | Ambele pot initia |
| Tip lead time | rd_tipleadtime | Choice | Nu | Pe stoc / In portofoliu furnizor / Achizitie noua / Import sau caz special | Determina lead time implicit | Vezi 2.6.2 |
| Lead time asumat (zile) | rd_leadtime | Whole Number | Nu | 0 - 365 | Implicit din tip, editabil de Achizitii | - |
| ETA confirmat | rd_eta | Date Only | Nu | - | Se introduce doar de Achizitii | Modificarea declanseaza FLX-07 |
| ETA initial | rd_etainitial | Date Only | Nu | - | Primul ETA confirmat, nu se mai schimba | Masoara alunecarea |
| Numar modificari ETA | rd_modificarieta | Whole Number | Nu | 0 - 99 | Incrementat de flux | Indicator de furnizor |
| Data receptiei | rd_datareceptie | Date Only | Nu | - | - | - |
| Cod SAP MP | rd_codsapmp | Text (20) | Nu | - | Creat de Achizitii in SAP | Niciodata scriere in SAP |
| Numar iteratii | rd_numariteratii | Rollup (Count) | Nu | 0 - 99 | Din rd_iteratiefurnizor | - |
| Critica pentru proiect | rd_critica | Yes/No | Da | Implicit Da | Daca Da, intarzierea ei opreste proiectul | - |
| Observatii | rd_observatii | Text Area (2000) | Nu | - | - | - |

2.6.2 Lead time implicit pe tip, editabil de Achizitii: Pe stoc = 7 zile; In portofoliu
furnizor = 7 zile; Achizitie noua = 30 de zile; Import sau caz special = fara implicit,
data se declara explicit si campul `rd_eta` devine obligatoriu.

### 2.6.3 rd_iteratiefurnizor

Rol: pastreaza fiecare bucla de respingere / reluare, cu motiv. Fara aceasta tabela,
istoricul incercarilor cu furnizori se pierde.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {MP}_{Furnizor}_it{n} | Generata | Coloana primara |
| Materie prima de proiect | rd_mpproiect | Lookup (rd_mpproiect) | Da | - | Parental | - |
| Numar iteratie | rd_numar | Whole Number | Da | 1 - 99 | Succesiv pe MP | - |
| Furnizor | rd_furnizor | Lookup (rd_furnizor) | Da | - | - | - |
| Denumire comerciala oferta | rd_denumireoferta | Text (200) | Nu | - | - | Varianta furnizorului |
| Data cererii de mostra | rd_datacerere | Date Only | Nu | - | - | - |
| Data primirii mostrei | rd_dataprimire | Date Only | Nu | - | - | - |
| Rezultat | rd_rezultat | Choice | Da | In curs / Acceptata tehnic / Respinsa tehnic / Respinsa de Calitate / Respinsa pe cost / Retrasa de furnizor | - | Choice global REZULTATITERATIE |
| Motiv respingere | rd_motivrespingere | Lookup (rd_motiv) | Nu | - | Obligatoriu daca rezultat contine Respinsa | - |
| Detalii respingere | rd_detalii | Text Area (2000) | Nu | - | - | - |
| Pret oferit | rd_pret | Currency (4) | Nu | - | - | - |
| Data deciziei | rd_datadecizie | Date Only | Nu | - | - | - |

## 2.7 TBL-09 Materie prima (catalog) si TBL-10 Furnizor

### 2.7.1 rd_materieprima

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Cod SAP | rd_codsap | Text (20) | Nu | - | Unic daca exista | Import din SAP, read-only |
| Categorie | rd_categorie | Choice | Da | Choice CATEGORIEMP | - | - |
| Furnizor principal | rd_furnizor | Lookup (rd_furnizor) | Nu | - | - | - |
| Unitate de masura | rd_um | Choice | Da | kg / g / l / ml / buc | - | Choice global UM |
| Pret curent | rd_pret | Currency (4) | Nu | - | Actualizat manual sau prin import | Alimenteaza antecalculul |
| Data pretului | rd_datapret | Date Only | Nu | - | - | Semnaleaza preturi vechi |
| Alergeni continuti | rd_alergeni | Choice (multi) | Da | Cei 14 alergeni din Anexa II Reg. 1169/2011 | - | Vezi Sectiunea 9 |
| Alergeni pe urme | rd_alergeniurme | Choice (multi) | Nu | Idem | Din declaratia furnizorului | Vezi 9.4 |
| Energie (kcal/100g) | rd_energie | Decimal (2) | Nu | 0 - 900 | Din ST furnizor | - |
| Grasimi (g/100g) | rd_grasimi | Decimal (2) | Nu | 0 - 100 | - | - |
| din care acizi grasi saturati | rd_saturate | Decimal (2) | Nu | 0 - 100 | <= rd_grasimi | - |
| Glucide (g/100g) | rd_glucide | Decimal (2) | Nu | 0 - 100 | - | - |
| din care zaharuri | rd_zaharuri | Decimal (2) | Nu | 0 - 100 | <= rd_glucide | - |
| Fibre (g/100g) | rd_fibre | Decimal (2) | Nu | 0 - 100 | - | - |
| Proteine (g/100g) | rd_proteine | Decimal (2) | Nu | 0 - 100 | - | - |
| Sare (g/100g) | rd_sare | Decimal (4) | Nu | 0 - 100 | - | - |
| Umiditate (%) | rd_umiditate | Decimal (2) | Nu | 0 - 100 | Necesara pentru randament | - |
| Suma macronutrienti | rd_summacro | Calculated (Decimal) | Nu | 0 - 105 | grasimi + glucide + fibre + proteine + sare + umiditate | Validare de plauzibilitate |
| Data ultimei ST furnizor | rd_datast | Date Only | Nu | - | ST mai veche de 24 de luni se semnaleaza | Cerinta IFS |
| Status | rd_statusmp | Choice | Da | Activa / In evaluare / Blocata / Iesita din uz | - | - |
| Bio / ecologic | rd_bio | Yes/No | Nu | - | - | - |
| Origine | rd_origine | Text (100) | Nu | - | Pentru declaratii de origine | - |

### 2.7.2 rd_furnizor

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Cod SAP furnizor | rd_codsap | Text (20) | Nu | - | - | Import |
| Tip | rd_tipfurnizor | Choice | Da | Producator / Distribuitor / Broker / Intern | - | - |
| Aprobat Calitate | rd_aprobat | Yes/No | Da | Implicit Nu | Nu se comanda de la furnizor neaprobat | Cerinta IFS |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Certificari | rd_certificari | Choice (multi) | Nu | IFS / BRC / FSSC 22000 / ISO 22000 / Bio / Halal / Kosher | - | - |
| Expirare certificare | rd_expirarecertificare | Date Only | Nu | - | Alerta cu 60 de zile inainte | - |
| Persoana de contact | rd_contact | Text (150) | Nu | - | - | - |
| Email contact | rd_email | Text (150) | Nu | Format email | - | - |
| Lead time mediu real (zile) | rd_leadtimemediu | Decimal (1) | Nu | - | Calculat din iteratii incheiate | Indicator de furnizor |
| Rata de respingere (%) | rd_ratarespingere | Decimal (2) | Nu | 0 - 100 | Iteratii respinse / total | Scris de flux |

## 2.8 TBL-11 Blocaj

Nume: `rd_blocaj`. Rol: sursa principala de explicatie a intarzierilor la analiza anuala.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | - | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Etapa afectata | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | Pentru durata neta pe etapa |
| Cine blocheaza | rd_sursablocaj | Choice | Da | Furnizor / Client / Calitate / Planificare / Productie / Achizitii / Intern R&D / Extern reglementar | - | Choice global SURSABLOCAJ |
| Categorie blocaj | rd_categorie | Choice | Da | Asteptare mostra / Asteptare decizie / Asteptare aprobare / Indisponibilitate linie / Indisponibilitate MP / Lipsa specificatie / Lipsa ambalaj / Altul | - | - |
| Data start | rd_datastart | Date Only | Da | <= azi | - | - |
| Data sfarsit | rd_datasfarsit | Date Only | Nu | >= data start | Gol = blocaj activ | - |
| Impact in zile | rd_impactzile | Whole Number | Nu | 0 - 999 | Zile lucratoare intre start si sfarsit | Scris de FLX-09 |
| Opreste ceasul R&D | rd_oprsteceas | Yes/No | Da | Implicit Da pentru surse externe | Intern R&D = Nu | Vezi 2.8.1 |
| Termen client afectat | rd_afecteazaclient | Yes/No | Da | Implicit Da | Termenul catre client curge oricum | Vezi 4.5 |
| Descriere | rd_descriere | Text Area (2000) | Da | - | - | - |
| Actiune de deblocare | rd_actiune | Text Area (2000) | Nu | - | - | - |
| Responsabil deblocare | rd_responsabil | Lookup (systemuser) | Nu | - | - | - |
| Activ | rd_activ | Calculated (Yes/No) | Nu | - | Da daca rd_datasfarsit este gol | - |

2.8.1 Regula de oprire a ceasului: cat timp exista cel putin un blocaj activ cu
`rd_oprsteceas = Da`, ceasul indicatorului T-Total al R&D se opreste. Termenul catre
client (`rd_termennegociat`) continua sa curga si se raporteaza separat. Blocajele cu
sursa "Intern R&D" nu opresc ceasul niciodata - altfel indicatorul devine
nefalsificabil.

## 2.9 TBL-12 Cerere de mostra si TBL-13 Miscare de mostra

### 2.9.1 rd_ceremostra

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar cerere | rd_name | Autonumber | Da | CM-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Tip mostra | rd_tipmostra | Choice | Da | Materie prima / Produs finit intern / Produs concurenta / Mostra client / Ambalaj | - | Choice global TIPMOSTRA |
| Materie prima de proiect | rd_mpproiect | Lookup (rd_mpproiect) | Nu | - | Obligatoriu daca tip = Materie prima | - |
| Solicitant | rd_solicitant | Lookup (systemuser) | Da | - | - | - |
| Rol solicitant | rd_rolsolicitant | Choice | Da | R&D / Achizitii | Ambele pot initia | - |
| Destinatar | rd_destinatar | Choice | Da | Intern laborator / Client / Furnizor / Panel senzorial | - | - |
| Cantitate ceruta | rd_cantitate | Decimal (2) | Da | > 0 | - | - |
| Unitate de masura | rd_um | Choice | Da | Choice UM | - | - |
| Data ceruta | rd_dataceruta | Date Only | Da | >= azi | - | - |
| Status cerere | rd_statuscerere | Choice | Da | Ciorna / Trimisa / Confirmata / In transport / Livrata / Anulata | - | - |
| Data livrarii | rd_datalivrare | Date Only | Nu | - | - | - |
| Adresa de livrare | rd_adresa | Text Area (500) | Nu | - | Obligatorie daca destinatar = Client | - |
| Curier si AWB | rd_awb | Text (100) | Nu | - | - | - |
| Observatii | rd_observatii | Text Area (2000) | Nu | - | - | - |

### 2.9.2 rd_miscaremostra

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Generata | - | Coloana primara |
| Cerere de mostra | rd_ceremostra | Lookup (rd_ceremostra) | Da | - | Parental | - |
| Tip miscare | rd_tipmiscare | Choice | Da | Pregatita / Predata la transport / Expediata / Receptionata / Returnata / Distrusa | - | - |
| Data si ora | rd_datamiscare | Date and Time | Da | - | Implicit acum | User Local |
| Persoana | rd_persoana | Lookup (systemuser) | Da | - | Implicit utilizator curent | - |
| Cantitate | rd_cantitate | Decimal (2) | Nu | > 0 | - | - |
| Temperatura la receptie (C) | rd_temperatura | Decimal (1) | Nu | -40 - 40 | Obligatorie la receptie de congelat | Cerinta HACCP |
| Conform | rd_conform | Yes/No | Nu | - | Obligatoriu la receptie | - |
| Motiv neconformitate | rd_motiv | Text (300) | Nu | - | Obligatoriu daca conform = Nu | - |
| Poza | rd_poza | Image | Nu | - | Din canvas mobil | Vezi ECR-13 |

## 2.10 TBL-14 Fisa de testare, TBL-15 Trial, TBL-16 Masuratoare

### 2.10.1 rd_fisatestare

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar fisa | rd_name | Autonumber | Da | FT-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Obiectivul testarii | rd_obiectiv | Text Area (2000) | Da | - | - | - |
| Versiune reteta testata | rd_versiunereteta | Lookup (rd_versiunereteta) | Da | - | - | - |
| Linie | rd_linie | Lookup (rd_linie) | Nu | - | - | - |
| Data planificata | rd_dataplanificata | Date Only | Da | - | - | - |
| Parametri de proces tinta | rd_parametritinta | Text Area (4000) | Nu | - | - | Preluati in trial |
| Tolerante declarate | rd_tolerante | Text Area (2000) | Da | - | Baza pentru conformitatea masuratorilor | Vezi 6.3 |
| Status fisa | rd_statusfisa | Choice | Da | Ciorna / Aprobata / In executie / Finalizata / Anulata | - | - |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | - | - |
| Concluzie | rd_concluzie | Text Area (4000) | Nu | - | Obligatorie la Finalizata | - |

### 2.10.2 rd_trial

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar trial | rd_name | Autonumber | Da | TR-{AA}-{SEQ:0000} | - | Coloana primara |
| Fisa de testare | rd_fisatestare | Lookup (rd_fisatestare) | Da | - | Parental | - |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Denormalizat pentru raportare | Scris de flux |
| Numar incercare | rd_numarincercare | Whole Number | Da | 1 - 99 | Succesiv pe fisa | - |
| Data si ora start | rd_start | Date and Time | Da | - | - | User Local |
| Data si ora final | rd_final | Date and Time | Nu | - | - | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | - | - |
| Schimb | rd_schimb | Choice | Da | Choice SCHIMB | - | - |
| Operator | rd_operator | Text (150) | Nu | - | Nu toti operatorii au cont | Text, nu lookup |
| Cantitate aluat (kg) | rd_cantitatealuat | Decimal (2) | Nu | > 0 | - | - |
| Bucati obtinute | rd_bucatiobtinute | Whole Number | Nu | >= 0 | - | - |
| Randament (%) | rd_randament | Decimal (2) | Nu | 0 - 120 | (bucati x gramaj) / (aluat x 1000) x 100 | Vezi 7.2 |
| Temperatura aluat (C) | rd_tempaluat | Decimal (1) | Nu | 0 - 40 | - | Parametru critic la laminare |
| Timp framantare (min) | rd_timpframantare | Decimal (1) | Nu | 0 - 120 | - | - |
| Timp fermentare (min) | rd_timpfermentare | Decimal (1) | Nu | 0 - 600 | - | - |
| Grosime laminare (mm) | rd_grosimelaminare | Decimal (2) | Nu | 0 - 100 | - | Fritsch / Rademaker |
| Timp dospire (min) | rd_timpdospire | Decimal (1) | Nu | 0 - 600 | - | - |
| Temperatura dospire (C) | rd_tempdospire | Decimal (1) | Nu | 0 - 60 | - | - |
| Temperatura coacere (C) | rd_tempcoacere | Decimal (1) | Nu | 0 - 350 | - | WP tunel |
| Timp coacere (min) | rd_timpcoacere | Decimal (1) | Nu | 0 - 120 | - | - |
| Temperatura congelare (C) | rd_tempcongelare | Decimal (1) | Nu | -45 - 0 | - | JBT shockfreezer |
| Timp congelare (min) | rd_timpcongelare | Decimal (1) | Nu | 0 - 300 | - | - |
| Temperatura in centru la iesire (C) | rd_tempcentru | Decimal (1) | Nu | -40 - 20 | Punct critic HACCP | Vezi 7.5 |
| Rezultat trial | rd_rezultat | Choice | Da | In curs / Reusit / Reusit cu observatii / Nereusit | - | Choice global REZULTATTRIAL |
| Observatii | rd_observatii | Text Area (4000) | Nu | - | Obligatorii daca rezultat = Nereusit | - |
| Numar masuratori | rd_numarmasuratori | Rollup (Count) | Nu | - | - | - |

### 2.10.3 rd_masuratoare

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Generata | - | Coloana primara |
| Trial | rd_trial | Lookup (rd_trial) | Da | - | Parental | - |
| Tip masuratoare | rd_tipmasuratoare | Choice | Da | Greutate / Lungime / Latime / Inaltime / Diametru / Grosime / Volum / Aspect / Alveolare / Miros / Gust / Culoare / Umiditate / Aw / pH / Temperatura | - | Choice global TIPMASURATOARE |
| Numar bucata | rd_numarbucata | Whole Number | Da | 1 - 50 | Succesiv in cadrul tipului | - |
| Valoare numerica | rd_valoare | Decimal (3) | Nu | - | Obligatorie pentru tipuri numerice | - |
| Valoare calitativa | rd_valoarecalitativa | Choice | Nu | Conform / Minor neconform / Neconform | Obligatorie pentru aspect, miros, gust, alveolare | - |
| Unitate de masura | rd_um | Choice | Da | g / mm / ml / C / % / scor | Implicit din tip | - |
| Valoare tinta | rd_tinta | Decimal (3) | Nu | - | Din fisa de testare | - |
| Toleranta minus | rd_tolminus | Decimal (3) | Nu | - | Din fisa de testare | - |
| Toleranta plus | rd_tolplus | Decimal (3) | Nu | - | Din fisa de testare | - |
| Conform | rd_conform | Calculated (Yes/No) | Nu | - | valoare intre tinta-tolminus si tinta+tolplus | Vezi 6.3 |
| Data si ora | rd_datamasurare | Date and Time | Da | Implicit acum | - | User Local |
| Masurat de | rd_masuratde | Lookup (systemuser) | Da | Implicit utilizator curent | - | - |
| Poza | rd_poza | Image | Nu | - | Din canvas mobil | Comprimata la 1024px |
| Exclus din statistica | rd_exclus | Yes/No | Da | Implicit Nu | Doar cu motiv, vezi 6.2.4 | - |
| Motiv excludere | rd_motivexcludere | Text (300) | Nu | - | Obligatoriu daca exclus = Da | - |
| Observatii | rd_observatii | Text (500) | Nu | - | - | - |

### 2.10.4 rd_statisticatrial (sinteza pe tip de masuratoare)

PROPUNERE: tabela separata de sinteza, scrisa de FLX-11 dupa fiecare salvare de
masuratoare. Motiv: Rollup-ul Dataverse calculeaza numai Sum, Count, Min, Max - nu
calculeaza abatere standard, deci sinteza ceruta in 6.1 nu poate trai in coloane de
proiect.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {Trial}_{Tip} | - | Coloana primara |
| Trial | rd_trial | Lookup (rd_trial) | Da | - | Parental | - |
| Tip masuratoare | rd_tipmasuratoare | Choice | Da | Choice TIPMASURATOARE | Unic pe trial | - |
| Numar valori | rd_n | Whole Number | Da | 1 - 50 | Fara cele excluse | - |
| Media | rd_medie | Decimal (3) | Da | - | - | - |
| Abatere standard | rd_abaterestandard | Decimal (4) | Nu | >= 0 | Esantion, n-1 | - |
| Coeficient de variatie (%) | rd_cv | Decimal (2) | Nu | 0 - 100 | abatere / medie x 100 | Vezi 6.2.3 |
| Minim | rd_minim | Decimal (3) | Da | - | - | - |
| Maxim | rd_maxim | Decimal (3) | Da | - | - | - |
| Numar neconforme | rd_neconforme | Whole Number | Da | 0 - 50 | - | - |
| Conformitate lot (%) | rd_conformitate | Decimal (2) | Da | 0 - 100 | conforme / n x 100 | - |
| Verdict | rd_verdict | Choice | Da | Conform / Conform cu observatii / Neconform / Esantion insuficient | Vezi 6.2 | - |

## 2.11 TBL-17 Evaluare senzoriala, TBL-18 Criteriu, TBL-19 Scor, TBL-20 Defect

### 2.11.1 rd_evaluaresenzoriala

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar evaluare | rd_name | Autonumber | Da | ES-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Trial evaluat | rd_trial | Lookup (rd_trial) | Nu | - | Referential | - |
| Tip evaluare | rd_tipevaluare | Choice | Da | Interna R&D / Panel extins / Cu clientul / Comparativa cu referinta / Shelf life | - | - |
| Data | rd_data | Date Only | Da | - | - | - |
| Numar evaluatori | rd_numarevaluatori | Rollup (Count) | Nu | 1 - 20 | Distinct pe rd_scor | Vezi 6.5.3 |
| Referinta comparata | rd_referinta | Lookup (rd_referinta) | Nu | - | Obligatorie daca tip = Comparativa | - |
| Scor total ponderat | rd_scortotal | Decimal (2) | Nu | 1 - 5 | Media ponderata a scorurilor | Scris de FLX-11 |
| Scor referinta | rd_scorreferinta | Decimal (2) | Nu | 1 - 5 | Idem, pe referinta | - |
| Diferenta fata de referinta | rd_diferenta | Decimal (2) | Nu | -4 - 4 | scor total - scor referinta | - |
| Dezacord maxim | rd_dezacord | Decimal (2) | Nu | 0 - 4 | Amplitudinea maxima pe un criteriu | Vezi 6.5.4 |
| Verdict | rd_verdict | Choice | Da | Acceptat / Acceptat cu observatii / Respins | Vezi 6.5.5 | Choice global VERDICT |
| Actiuni cerute | rd_actiuni | Text Area (4000) | Nu | - | Obligatorii daca verdict != Acceptat | - |
| Conditii de degustare | rd_conditii | Text Area (1000) | Nu | - | Temperatura, timp de la coacere | Cerinta de repetabilitate |

### 2.11.2 rd_criteriusenzorial (nomenclator)

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire criteriu | rd_name | Text (100) | Da | - | - | Coloana primara |
| Cod | rd_cod | Text (10) | Da | CR-nn | Unic | - |
| Grupa | rd_grupa | Choice | Da | Aspect exterior / Structura interna / Textura / Aroma si gust / Comportament la utilizare | - | - |
| Pondere (%) | rd_pondere | Decimal (2) | Da | 0 - 100 | Suma pe categoria de produs = 100 | Vezi 6.5.1 |
| Categorie produs | rd_categorieprodus | Choice | Da | Foietaj / Aluat dospit / Patiserie cu umplutura / Paine / Produs gata copt / Produs bake-off | Grile diferite pe categorie | - |
| Ancora scor 1 | rd_ancora1 | Text (300) | Da | - | Descriere, nu cifra | Vezi 6.5.2 |
| Ancora scor 3 | rd_ancora3 | Text (300) | Da | - | - | - |
| Ancora scor 5 | rd_ancora5 | Text (300) | Da | - | - | - |
| Eliminatoriu sub | rd_eliminatoriusub | Whole Number | Nu | 1 - 5 | Scor sub prag = respins automat | Vezi 6.5.5 |
| Activ | rd_activ | Yes/No | Da | - | - | - |

### 2.11.3 rd_scorsenzorial

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Generata | - | Coloana primara |
| Evaluare | rd_evaluare | Lookup (rd_evaluaresenzoriala) | Da | - | Parental | - |
| Criteriu | rd_criteriu | Lookup (rd_criteriusenzorial) | Da | - | - | - |
| Evaluator | rd_evaluator | Lookup (systemuser) | Da | - | Unic impreuna cu criteriu si tinta | - |
| Tinta scorului | rd_tintascor | Choice | Da | Produs dezvoltat / Referinta | Permite comparatia pe acelasi ecran | - |
| Scor | rd_scor | Whole Number | Da | 1 - 5 | - | - |
| Comentariu | rd_comentariu | Text (500) | Nu | - | Obligatoriu daca scor <= 2 | Business rule |

### 2.11.4 rd_defect (nomenclator) si rd_defectconstatat

`rd_defect`: Denumire (Text, primara), Cod (Text, DF-nn), Grupa (Choice: Aluat /
Laminare / Dospire / Coacere / Congelare / Ambalare / Materie prima), Descriere (Text
Area), Severitate implicita (Choice: Minor / Major / Critic), Cauza probabila (Text
Area), Activ (Yes/No).

`rd_defectconstatat`: Evaluare (Lookup, parental), Defect (Lookup), Severitate (Choice),
Numar bucati afectate (Whole Number), Procent afectat (Decimal 2), Poza (Image),
Observatii (Text Area).

## 2.12 TBL-21 Referinta de comparatie

Nume: `rd_referinta`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Tip referinta | rd_tipreferinta | Choice | Da | Produs concurenta / Produs actual / Mostra client / Specificatie client / Inexistenta | - | Choice global TIPREFERINTA |
| Client asociat | rd_client | Lookup (rd_client) | Nu | - | - | - |
| Producator | rd_producator | Text (150) | Nu | - | Pentru produs concurenta | - |
| Cod produs actual | rd_codprodusactual | Text (20) | Nu | - | Cod SAP daca este produs propriu | - |
| Gramaj (g) | rd_gramaj | Decimal (2) | Nu | - | - | - |
| Pret raft | rd_pretraft | Currency (2) | Nu | - | Pentru pozitionare | - |
| Data achizitiei referintei | rd_dataachizitie | Date Only | Nu | - | - | - |
| Lista de ingrediente | rd_ingrediente | Text Area (4000) | Nu | - | De pe eticheta | - |
| Valori nutritionale declarate | rd_nutritionale | Text Area (2000) | Nu | - | - | - |
| Poza | rd_poza | Image | Nu | - | - | - |
| Documente | rd_documenteurl | Text (500) | Nu | - | Folder in 00_Solicitare | - |

## 2.13 TBL-22 Antecalcul si TBL-23 Linie de antecalcul

### 2.13.1 rd_antecalcul

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar antecalcul | rd_name | Autonumber | Da | AC-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Versiune reteta | rd_versiunereteta | Lookup (rd_versiunereteta) | Da | - | - | - |
| Versiune antecalcul | rd_versiune | Whole Number | Da | 1 - 99 | Succesiv pe proiect | - |
| Data calculului | rd_datacalcul | Date Only | Da | - | - | - |
| Linie de productie | rd_linie | Lookup (rd_linie) | Da | - | Determina tariful si viteza | - |
| Gramaj (g) | rd_gramaj | Decimal (2) | Da | - | Din proiect | - |
| Cost materii prime / kg | rd_costmp | Currency (4) | Nu | - | Suma liniilor de antecalcul | Rollup |
| Pierdere tehnologica (%) | rd_pierdere | Decimal (2) | Da | 0 - 30, implicit 3 | Din date de linie | - |
| Cost MP ajustat / kg | rd_costmpajustat | Decimal (4) | Nu | - | cost MP / (1 - pierdere/100) | - |
| Cost ambalaj / buc | rd_costambalaj | Currency (4) | Nu | - | - | - |
| Cost manopera / kg | rd_costmanopera | Currency (4) | Nu | - | Tarif linie x timp / cantitate | - |
| Cost energie si utilitati / kg | rd_costenergie | Currency (4) | Nu | - | Din tariful liniei | Congelarea este semnificativa |
| Cost congelare / kg | rd_costcongelare | Currency (4) | Nu | - | Separat, pentru comparabilitate | PROPUNERE |
| Regie / kg | rd_regie | Currency (4) | Nu | - | Procent din costul direct | - |
| Cost total / kg | rd_costtotal | Currency (4) | Nu | - | Suma componentelor | - |
| Cost total / buc | rd_costbuc | Currency (4) | Nu | - | cost/kg x gramaj / 1000 + ambalaj | - |
| Pret tinta client | rd_prettinta | Currency (4) | Nu | - | Din solicitare sau negociere | - |
| Marja bruta (%) | rd_marja | Decimal (2) | Nu | -100 - 100 | (pret - cost) / pret x 100 | - |
| Status | rd_statusantecalcul | Choice | Da | Ciorna / Trimis spre aprobare / Aprobat / Respins / Inlocuit | - | - |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | - | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Cost real la revizuire | rd_costreal | Currency (4) | Nu | - | Din Sectiunea 8 | Compara antecalcul cu realitate |

### 2.13.2 rd_linieantecalcul

Coloane: Antecalcul (Lookup, parental), Materie prima (Lookup rd_materieprima), Materie
prima de proiect (Lookup, pentru MP fara cod), Cantitate kg/100kg (Decimal 4), Pret
unitar (Currency 4), Cost linie (Calculated Currency = cantitate x pret / 100), Sursa
pretului (Choice: Catalog / Oferta furnizor / Estimare), Data pretului (Date Only),
Observatii (Text 500).

## 2.14 TBL-24 Reteta, TBL-25 Versiune de reteta, TBL-26 Linie de reteta

### 2.14.1 rd_reteta (antet)

Coloane: Denumire (Text 200, primara), Proiect (Lookup, parental), Cod reteta (Text 20),
Categorie produs (Choice), Versiune curenta (Lookup rd_versiunereteta, referential),
Status (Choice: In dezvoltare / Validata / Inlocuita / Retrasa), Observatii (Text Area).

### 2.14.2 rd_versiunereteta

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {Reteta} v{n} | Generata | Coloana primara |
| Reteta | rd_reteta | Lookup (rd_reteta) | Da | - | Parental | - |
| Numar versiune | rd_numarversiune | Whole Number | Da | 1 - 99 | Succesiv | - |
| Data versiunii | rd_dataversiune | Date Only | Da | - | - | - |
| Autor | rd_autor | Lookup (systemuser) | Da | - | - | - |
| Motivul modificarii | rd_motivmodificare | Text Area (1000) | Da | - | Obligatoriu de la versiunea 2 | Cerinta IFS |
| Total cantitate (kg/100kg) | rd_total | Rollup (Sum) | Nu | - | Suma liniilor, trebuie sa fie 100 | Validare |
| Blocata | rd_blocata | Yes/No | Da | Implicit Nu | Versiunea validata nu se mai editeaza | Vezi 2.14.4 |
| Status | rd_statusversiune | Choice | Da | Ciorna / In testare / Validata / Inlocuita | - | - |
| Energie (kcal/100g) | rd_energie | Decimal (2) | Nu | - | Calculat, vezi Sectiunea 9 | Scris de FLX-13 |
| Grasimi | rd_grasimi | Decimal (2) | Nu | - | Idem | - |
| Saturate | rd_saturate | Decimal (2) | Nu | - | Idem | - |
| Glucide | rd_glucide | Decimal (2) | Nu | - | Idem | - |
| Zaharuri | rd_zaharuri | Decimal (2) | Nu | - | Idem | - |
| Fibre | rd_fibre | Decimal (2) | Nu | - | Idem | - |
| Proteine | rd_proteine | Decimal (2) | Nu | - | Idem | - |
| Sare | rd_sare | Decimal (4) | Nu | - | Idem | - |
| Alergeni continuti | rd_alergeni | Choice (multi) | Nu | - | Reuniunea alergenilor din linii | Scris de FLX-13 |
| Alergeni pe urme | rd_alergeniurme | Choice (multi) | Nu | - | Vezi 9.4 | - |
| Data ultimului calcul | rd_datacalcul | Date and Time | Nu | - | - | Semnaleaza calcule invechite |

### 2.14.3 rd_liniereteta

Coloane: Versiune reteta (Lookup, parental), Materie prima (Lookup rd_materieprima),
Materie prima de proiect (Lookup rd_mpproiect, pentru MP inca fara cod), Faza de retetare
(Choice: Aluat de baza / Grasime de laminare / Umplutura / Decor / Glazura / Presarare),
Cantitate kg/100kg (Decimal 4), Ordine (Whole Number), Procent din total (Calculated
Decimal), Pierdere la proces (%) (Decimal 2), Observatii (Text 500).

2.14.4 Regula de blocare: la trecerea versiunii in `Validata`, `rd_blocata` devine Da si
toate liniile devin read-only prin business rule si prin rol de securitate (drept Write
retras pe status validat). O modificare ulterioara obliga la versiune noua cu motiv.
Motiv: reconstituirea dosarului de produs la orice data din trecut, cerinta IFS.

## 2.15 TBL-27 Alergen si TBL-28 Valoare nutritionala

`rd_alergen` (nomenclator fix, 14 pozitii): Denumire (Text, primara), Cod (Text: GLU,
CRU, OUA, PES, ARA, SOI, LAP, FRC, TEL, MUS, SUS, SO2, LUP, MOL), Denumire legala pe
eticheta (Text 150), Grupa (Choice: Cereale cu gluten / Fructe cu coaja / Altele),
Necesita evidentiere pe eticheta (Yes/No, implicit Da), Prag de declarare (Text 100),
Observatii.

`rd_valoarenutritionala` este modelata ca set de coloane pe `rd_versiunereteta`
(2.14.2), nu ca tabela separata. Motiv: valorile sunt intotdeauna exact 8, fixe prin
Reg. 1169/2011, si o tabela separata ar adauga un join fara nicio flexibilitate reala.
NOTA: daca in viitor se cer si micronutrienti sau declaratii voluntare, se adauga tabela
`rd_nutrientsuplimentar` cu Lookup catre versiune.

## 2.16 TBL-29 Specificatie tehnica si TBL-30 SDP

### 2.16.1 rd_specificatie

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar specificatie | rd_name | Autonumber | Da | ST-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Nu | - | Gol pentru ST de MP din catalog | Referential |
| Tip specificatie | rd_tipspecificatie | Choice | Da | Conditii ST / ST draft / ST finala / ST interna MP noua | - | Choice global TIPST |
| Materie prima | rd_materieprima | Lookup (rd_materieprima) | Nu | - | Obligatorie daca tip = ST interna MP | - |
| Versiune | rd_versiune | Text (10) | Da | v01, v02 | - | - |
| Status | rd_statusst | Choice | Da | Ciorna / In aprobare / Aprobata / Inlocuita / Retrasa | - | - |
| Autor | rd_autor | Lookup (systemuser) | Da | - | - | - |
| Aprobator Calitate | rd_aprobatorcalitate | Lookup (systemuser) | Nu | - | Obligatoriu pentru Aprobata | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Valabila de la | rd_valabiladela | Date Only | Nu | - | - | - |
| Document | rd_documenturl | Text (500) | Nu | - | Fisier in 05_Specificatii | Formatul intern al ST nu face obiectul acestui blueprint |
| Inlocuieste | rd_inlocuieste | Lookup (rd_specificatie) | Nu | - | Auto-referential | Lant de versiuni |

### 2.16.2 rd_sdp (Specificatie de produs)

Coloane: Numar SDP (Autonumber SDP-{AA}-{SEQ:0000}, primara), Proiect (Lookup,
parental), Versiune reteta (Lookup), Versiune (Text 10), Status (Choice: Ciorna / In
aprobare / Aprobata / Inlocuita), Linie (Lookup), Parametri de proces (Text Area 8000,
preluati din trialul validat), Puncte critice HACCP (Text Area 4000), Ambalare si
etichetare (Text Area 4000), Conditii de depozitare (Text 300), Termen de valabilitate
(Whole Number, luni), Conditii de decongelare si coacere la client (Text Area 2000),
Aprobator R&D (Lookup), Aprobator Calitate (Lookup), Data aprobarii (Date Only), Document
(Text 500).

## 2.17 TBL-31 Eticheta

Nume: `rd_eticheta`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Tip eticheta | rd_tipeticheta | Choice | Da | Punga / Bax / EPC eticheta produs client / Fisier imprimanta | - | Choice global TIPETICHETA |
| Format fisier imprimanta | rd_formatimprimanta | Choice | Nu | Colos / Zebra ZPL / Altul | Obligatoriu daca tip = Fisier imprimanta | - |
| Versiune | rd_versiune | Text (10) | Da | v01 | - | - |
| Status | rd_statuseticheta | Choice | Da | De realizat / In lucru / Trimisa spre aprobare / Aprobata / Implementata / Inlocuita | Vezi livrabilele ETICHETA REALIZATA si ETICHETA IMPLEMENTATA | - |
| Limba | rd_limba | Choice (multi) | Da | RO / EN / HU / BG / DE / FR / IT | - | - |
| Denumire legala produs | rd_denumirelegala | Text (300) | Da | - | Preluata din SDP | - |
| Lista de ingrediente | rd_ingrediente | Text Area (8000) | Nu | - | Generata din reteta, ordine descrescatoare | Vezi 9.5 |
| Declaratie alergeni | rd_declaratiealergeni | Text Area (2000) | Nu | - | Generata, alergenii evidentiati | Vezi 9.3 |
| Declaratie urme | rd_declaratieurme | Text (500) | Nu | - | Vezi 9.4 | - |
| Tabel nutritional | rd_tabelnutritional | Text Area (2000) | Nu | - | Generat din versiunea de reteta | - |
| Gramaj declarat | rd_gramajdeclarat | Text (50) | Da | - | - | - |
| Termen de valabilitate | rd_valabilitate | Text (100) | Da | - | - | - |
| Conditii de pastrare | rd_pastrare | Text (300) | Da | - | - | - |
| Cod EAN | rd_ean | Text (20) | Nu | 13 cifre | Validare de lungime | - |
| Aprobator Calitate | rd_aprobator | Lookup (systemuser) | Nu | - | Obligatoriu pentru Aprobata | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Fisier | rd_fisierurl | Text (500) | Nu | - | In 06_Eticheta | - |

## 2.18 TBL-32 Implementare (IPN)

Nume: `rd_implementare`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar IPN | rd_name | Autonumber | Da | IPN-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental, 1:1 in practica | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | - | - |
| Data planificata productie 0 | rd_dataprod0 | Date Only | Da | - | - | - |
| Conditii IPN completate | rd_conditiiok | Yes/No | Da | Implicit Nu | Checklist de conditii, vezi 5.5.8 | - |
| Plan IPN aprobat | rd_planok | Yes/No | Da | Implicit Nu | - | - |
| IL productie emisa | rd_ilok | Yes/No | Da | Implicit Nu | - | - |
| Numar IL | rd_numaril | Text (30) | Nu | - | - | - |
| Plan HACCP actualizat | rd_haccpok | Yes/No | Da | Implicit Nu | Aprobare Calitate obligatorie | Cerinta IFS |
| Data actualizarii HACCP | rd_datahaccp | Date Only | Nu | - | - | - |
| Puncte critice noi identificate | rd_ccpnoi | Text Area (4000) | Nu | - | - | - |
| Necesita validare shelf life | rd_shelflife | Yes/No | Da | Implicit Da pentru produs nou | - | - |
| Termen de valabilitate propus (luni) | rd_valabilitate | Whole Number | Nu | 1 - 36 | - | - |
| Instruire operatori efectuata | rd_instruireok | Yes/No | Da | Implicit Nu | Data si lista de participanti in document | Cerinta IFS |
| Ambalaj disponibil | rd_ambalajok | Yes/No | Da | Implicit Nu | Blocheaza productia 0 | - |
| Status implementare | rd_statusipn | Choice | Da | In pregatire / Gata de productie 0 / In derulare / Finalizata / Amanata | Gata doar cu toate bifele Da | Business rule |
| Data implementarii | rd_dataimplementare | Date Only | Nu | - | Porneste ceasul revizuirii | Vezi Sectiunea 8 |

## 2.19 TBL-33 Productie 0 si TBL-34 Inregistrare de productie 0

Structura completa este in Sectiunea 7. Rezumat de coloane:

`rd_productie0`: Numar (Autonumber P0-{AA}-{SEQ:0000}, primara), Proiect (Lookup,
parental), Implementare (Lookup), Data (Date Only), Linie (Lookup), Schimb (Choice),
Cantitate planificata kg (Decimal 2), Cantitate realizata kg (Decimal 2), Randament aluat
% (Decimal 2), Rebut kg (Decimal 2), Rebut % (Decimal 2), Viteza nominala buc/h (Decimal
2), Viteza reala buc/h (Decimal 2), Eficienta viteza % (Decimal 2), Timp setup min (Whole
Number), Timp de schimb sortiment min (Whole Number), Greutate medie la ambalare g
(Decimal 2), Abatere de la gramaj % (Decimal 2), Conformitate HACCP (Yes/No), Numar
abateri de proces (Rollup Count), Decizie finala (Choice: Validat / Validat conditionat /
Se repeta), Conditii de validare (Text Area 4000), Responsabil decizie (Lookup), Data
deciziei (Date Only).

`rd_inregistrareprod0`: Productie 0 (Lookup, parental), Tip inregistrare (Choice:
Parametru de proces / Rebut pe cauza / Problema / Masuratoare de ambalare / Verificare
HACCP), Denumire (Text 150), Valoare specificata (Decimal 3), Valoare reala (Decimal 3),
Unitate (Choice), Abatere (Calculated Decimal), In toleranta (Yes/No), Cauza rebut
(Choice, vezi 7.3), Cantitate kg (Decimal 2), Procent (Decimal 2), Descriere problema
(Text Area), Actiune corectiva (Text Area), Responsabil (Lookup), Termen (Date Only),
Status actiune (Choice), Poza (Image).

## 2.20 TBL-35 Revizuire post-implementare

Nume: `rd_revizuire`. Structura completa in Sectiunea 8.

Coloane: Numar (Autonumber RPI-{AA}-{SEQ:0000}, primara), Proiect (Lookup, parental),
Etapa revizuire (Choice: 30 de zile / 60 de zile / 90 de zile), Data scadenta (Date
Only), Data efectuarii (Date Only), Status (Choice: Programata / In lucru / Finalizata /
Sarita), Numar reclamatii (Whole Number), Numar neconformitati interne (Whole Number),
Cantitate produsa cumulat kg (Decimal 2), Randament in serie % (Decimal 2), Randament la
productia 0 % (Decimal 2), Diferenta de randament (Calculated Decimal), Rebut in serie %
(Decimal 2), Cost real / kg (Currency 4), Cost din antecalcul / kg (Currency 4), Abatere
de cost % (Calculated Decimal), Feedback client (Text Area 4000), Feedback KAM (Text Area
4000), Volum realizat fata de estimat % (Decimal 2), Decizie (Choice: Mentinere /
Optimizare / Retragere), Actiuni (Text Area 4000), Responsabil (Lookup), Aprobator
(Lookup).

## 2.21 TBL-36 Linie de productie

Nume: `rd_linie`. Nomenclator cu cele 9 linii.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire linie | rd_name | Text (100) | Da | - | - | Coloana primara |
| Cod linie | rd_codlinie | Text (10) | Da | L01 - L09 | Unic | - |
| Amplasament | rd_amplasament | Choice | Da | Choice AMPLASAMENT | - | - |
| Tip linie | rd_tiplinie | Choice | Da | Laminare / Aluat dospit / Paine / Patiserie cu umplutura / Mixta | - | - |
| Echipament principal | rd_echipament | Text (200) | Nu | Fritsch / Rademaker / VMI / WP Bakery / JBT | - | - |
| Capabilitati | rd_capabilitati | Choice (multi) | Da | Laminare / Impletire / Injectare umplutura / Depunere / Presarare / Glazurare / Coacere tunel / Congelare rapida / Ambalare flow-pack / Ambalare tava | Filtreaza liniile compatibile cu produsul | Vezi 2.21.1 |
| Gramaj minim (g) | rd_gramajmin | Decimal (2) | Nu | - | Validare la alocarea liniei | - |
| Gramaj maxim (g) | rd_gramajmax | Decimal (2) | Nu | - | Idem | - |
| Latime banda (mm) | rd_latimebanda | Whole Number | Nu | - | Constrangere de dimensiune | - |
| Viteza nominala (buc/h) | rd_vitezanominala | Decimal (2) | Nu | - | Referinta pentru productia 0 | - |
| Timp schimb sortiment (min) | rd_timpschimb | Whole Number | Da | Implicit 120 | Din aplicatia de planificare | - |
| Tarif orar | rd_tariforar | Currency (2) | Nu | - | Pentru antecalcul | - |
| Numar proiecte active | rd_proiecteactive | Whole Number | Nu | 0 - 99 | Scris de FLX-06 | Coada pe linie |
| Prag de supraincarcare | rd_pragsupraincarcare | Whole Number | Da | Implicit 6 | Peste prag, semnalizare vizuala | Vezi 2.21.2 |
| Activa | rd_activa | Yes/No | Da | - | - | - |

2.21.1 Capabilitatile filtreaza liniile propuse la alocare. Un proiect de foietaj laminat
nu poate primi decat linii cu capabilitatea Laminare, iar gramajul trebuie sa intre in
intervalul liniei. Validarea este avertisment, nu blocaj: se poate forta cu motiv, pentru
ca dezvoltarea presupune uneori si incercari in afara plicului declarat.

2.21.2 Coada pe linie se vede si global, si pe fiecare linie. Cele 9 linii nu concureaza
intre ele: supraincarcarea liniei L03 nu retrogradeaza proiectele de pe L07.

## 2.22 TBL-37 Profil de tehnolog

Nume: `rd_profiltehnolog`. Extinde `systemuser` fara sa il inlocuiasca.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Numele persoanei | - | Coloana primara |
| Utilizator | rd_utilizator | Lookup (systemuser) | Da | - | Unic | Sursa de adevar ramane Entra ID |
| Rol principal | rd_rolprincipal | Choice | Da | Choice ROL | - | - |
| Amplasament | rd_amplasament | Choice | Da | Choice AMPLASAMENT | - | - |
| Specializare | rd_specializare | Choice (multi) | Nu | Foietaj / Aluat dospit / Paine / Patiserie / Umpluturi / Ambalaje / Solutii tehnice | Filtreaza propunerea de alocare | - |
| Linii pe care lucreaza | rd_linii | Text (100) | Nu | Coduri de linie separate prin virgula | - | NOTA: N:N ar fi mai curat, dar se citeste mai greu in formular |
| Capacitate maxima proiecte | rd_capacitatemax | Whole Number | Da | 1 - 10, implicit 6 | Vezi 4.2 | - |
| Proiecte active | rd_proiecteactive | Whole Number | Nu | 0 - 99 | Scris de FLX-06 | - |
| Proiecte active P1 | rd_activep1 | Whole Number | Nu | 0 - 99 | Scris de FLX-06 | - |
| Grad de incarcare (%) | rd_incarcare | Decimal (2) | Nu | 0 - 300 | active / capacitate max x 100 | Vezi 2.22.1 |
| Semnal incarcare | rd_semnal | Choice | Nu | Verde / Galben / Rosu | Vezi 2.22.1 | Afisat in dashboard |
| Disponibil | rd_disponibil | Yes/No | Da | Implicit Da | Concediu, delegatie | - |
| Indisponibil pana la | rd_indisponibilpanala | Date Only | Nu | - | - | Intra in calculul termenului propus |
| Activ | rd_activ | Yes/No | Da | - | - | - |

2.22.1 Praguri de supraincarcare: Verde sub 80%; Galben 80-100%; Rosu peste 100%.
Suplimentar, un tehnolog cu mai mult de 2 proiecte in banda P1 se marcheaza Rosu
indiferent de gradul de incarcare, pentru ca P1 inseamna lucru simultan real, nu coada.

## 2.23 TBL-38 Client

Nume: `rd_client`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire client | rd_name | Text (200) | Da | - | - | Coloana primara |
| Cod SAP client | rd_codsap | Text (20) | Nu | - | - | Import |
| Clasificare | rd_clasificare | Choice | Da | A / B / C | Stabilita si revizuita de Sales / KAM | 20 de puncte in scor |
| Data ultimei clasificari | rd_dataclasificare | Date Only | Nu | - | Revizuire anuala | - |
| Canal | rd_canal | Choice | Da | Choice CANAL | - | - |
| Tara | rd_tara | Text (100) | Da | Implicit Romania | - | Determina cerintele de eticheta |
| KAM responsabil | rd_kam | Lookup (systemuser) | Da | - | - | - |
| Cerinte specifice de eticheta | rd_cerinteeticheta | Text Area (4000) | Nu | - | - | Se preiau automat in proiect |
| Cerinte de audit sau certificare | rd_cerinteaudit | Text Area (2000) | Nu | - | - | - |
| Numar proiecte active | rd_proiecteactive | Whole Number | Nu | - | Scris de FLX-06 | - |
| Activ | rd_activ | Yes/No | Da | - | - | - |

## 2.24 TBL-39 Indicator si TBL-40 Masurare de indicator

`rd_indicator` (definitie): Denumire (Text, primara), Cod (Text: T-TOTAL, Q-CORECT,
Q-COMPLET), Tip (Choice: Timp / Calitate / Volum), Nivel de masurare (Choice: Activitate
/ Rol / Persoana / Departament), Formula de calcul (Text Area 2000, descriptiva), Tinta
% (Decimal 2, intre 95 si 98), Prag de alerta % (Decimal 2), Unitate (Choice), Frecventa
(Choice: Saptamanal / Lunar / Trimestrial / Anual), Activ (Yes/No).

`rd_masurareindicator`: Indicator (Lookup, parental), Perioada (Choice: Luna / Trimestru
/ An), Data de inceput (Date Only), Data de sfarsit (Date Only), Nivel (Choice), Persoana
(Lookup systemuser), Rol (Choice), Linie (Lookup), Valoare realizata (Decimal 2), Tinta
(Decimal 2), Atins (Calculated Yes/No), Numar cazuri (Whole Number), Numar conforme
(Whole Number), Observatii (Text Area). Detaliile de calcul sunt in Sectiunea 13.

## 2.25 Nomenclatoare comune

### 2.25.1 rd_motiv (motive unificate)

Coloane: Denumire (Text 200, primara), Cod (Text 10), Tip motiv (Choice: Respingere
solicitare / Amanare / Respingere materie prima / Suspendare proiect / Abandon proiect /
Suprascriere prioritate / Blocaj / Respingere livrabil), Descriere (Text Area), Necesita
comentariu (Yes/No), Activ (Yes/No).

Motiv pentru o singura tabela de motive in loc de sase: motivele se raporteaza impreuna
la analiza anuala ("de ce nu s-au terminat proiectele"), iar o tabela unica cu tip
permite o singura vizualizare de analiza si o singura intretinere.

### 2.25.2 rd_tipdocument

Coloane: Denumire (Text 100, primara), Cod (Text 10, folosit in numele fisierului),
Faza (Choice FAZA), Extensie asteptata (Text 20), Necesita aprobare (Yes/No), Rol
aprobator (Choice ROL), Retentie (ani) (Whole Number), Sablon Word (Text 300), Activ
(Yes/No). Continutul complet in `data/nomenclatoare.json`.

### 2.25.3 Choice-uri globale

Lista completa, cu valori si etichete, in `data/choices.json`: AMPLASAMENT, CANAL,
AMBALARE, MOTIVCERERE, TIPPROIECT, STATUSPROIECT, STATUSLIVRABIL, STATUSETAPA,
STATUSMP, CATEGORIEMP, SURSABLOCAJ, TIPMOSTRA, TIPMASURATOARE, REZULTATTRIAL,
REZULTATITERATIE, VERDICT, TIPST, TIPETICHETA, TIPREFERINTA, FAZA, ROL, BANDA, SCHIMB,
UM, ALERGEN.

## 2.26 Rezumatul tabelelor

| Cod | Tabela | Nume logic | Tip | Val |
|---|---|---|---|---|
| TBL-01 | Solicitare (SCP) | rd_solicitare | Tranzactionala | 1 |
| TBL-02 | Proiect CDI | rd_proiect | Radacina | 1 |
| TBL-03 | Livrabil de proiect | rd_livrabil | Copil | 1 |
| TBL-04 | Sablon de livrabil | rd_sablonlivrabil | Configurare | 0 |
| TBL-05 | Etapa de proiect | rd_etapa | Copil | 1 |
| TBL-06 | Sablon de etapa | rd_sablonetapa | Configurare | 0 |
| TBL-07 | Materie prima de proiect | rd_mpproiect | Copil | 2 |
| TBL-08 | Iteratie de furnizor | rd_iteratiefurnizor | Copil | 2 |
| TBL-09 | Materie prima (catalog) | rd_materieprima | Nomenclator | 1 |
| TBL-10 | Furnizor | rd_furnizor | Nomenclator | 2 |
| TBL-11 | Blocaj | rd_blocaj | Copil | 2 |
| TBL-12 | Cerere de mostra | rd_ceremostra | Copil | 2 |
| TBL-13 | Miscare de mostra | rd_miscaremostra | Copil | 2 |
| TBL-14 | Fisa de testare | rd_fisatestare | Copil | 1 |
| TBL-15 | Trial | rd_trial | Copil | 1 |
| TBL-16 | Masuratoare | rd_masuratoare | Copil | 1 |
| TBL-16b | Statistica de trial | rd_statisticatrial | Derivata | 1 |
| TBL-17 | Evaluare senzoriala | rd_evaluaresenzoriala | Copil | 2 |
| TBL-18 | Criteriu senzorial | rd_criteriusenzorial | Nomenclator | 2 |
| TBL-19 | Scor senzorial | rd_scorsenzorial | Copil | 2 |
| TBL-20 | Defect / Defect constatat | rd_defect / rd_defectconstatat | Nomenclator / Copil | 2 |
| TBL-21 | Referinta de comparatie | rd_referinta | Copil | 1 |
| TBL-22 | Antecalcul | rd_antecalcul | Copil | 2 |
| TBL-23 | Linie de antecalcul | rd_linieantecalcul | Copil | 2 |
| TBL-24 | Reteta | rd_reteta | Copil | 2 |
| TBL-25 | Versiune de reteta | rd_versiunereteta | Copil | 2 |
| TBL-26 | Linie de reteta | rd_liniereteta | Copil | 2 |
| TBL-27 | Alergen | rd_alergen | Nomenclator | 3 |
| TBL-29 | Specificatie tehnica | rd_specificatie | Copil | 2 |
| TBL-30 | SDP | rd_sdp | Copil | 2 |
| TBL-31 | Eticheta | rd_eticheta | Copil | 3 |
| TBL-32 | Implementare (IPN) | rd_implementare | Copil | 2 |
| TBL-33 | Productie 0 | rd_productie0 | Copil | 2 |
| TBL-34 | Inregistrare de productie 0 | rd_inregistrareprod0 | Copil | 2 |
| TBL-35 | Revizuire post-implementare | rd_revizuire | Copil | 3 |
| TBL-36 | Linie de productie | rd_linie | Nomenclator | 0 |
| TBL-37 | Profil de tehnolog | rd_profiltehnolog | Nomenclator | 0 |
| TBL-38 | Client | rd_client | Nomenclator | 0 |
| TBL-39 | Indicator | rd_indicator | Configurare | 3 |
| TBL-40 | Masurare de indicator | rd_masurareindicator | Derivata | 3 |
| TBL-41 | Motiv | rd_motiv | Nomenclator | 0 |
| TBL-42 | Tip document | rd_tipdocument | Nomenclator | 0 |
