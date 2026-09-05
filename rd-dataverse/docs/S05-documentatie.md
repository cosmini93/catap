# Sectiunea 5 - Structura documentatiei

Aceasta sectiune este centrala. Datele stau in Dataverse, fisierele in SharePoint.
Regula de departajare: daca informatia se cauta, se filtreaza, se aduna sau declanseaza
ceva, este data si sta in Dataverse. Daca informatia se citeste, se semneaza sau se
trimite in afara, este document si sta in SharePoint.

## 5.1 Arborele de foldere

### 5.1.1 Structura generata automat

Se creeaza de FLX-02, in momentul acceptarii proiectului, in biblioteca
`PRODUSE IN DEZVOLTARE`:

```
/PRODUSE IN DEZVOLTARE/{an}/{cod}_{nume produs}/
  00_Solicitare        SCP, EPC, cerinte client, referinta de comparatie
  01_Plan              plan dezvoltare, cerere achizitii mostra MP noua
  02_Testare           fisa de test, rapoarte de testare, poze
  03_Mostre            mostre MP si produs, evidenta livrarilor
  04_Antecalcul
  05_Specificatii      conditii ST, ST draft, ST intern MP, ST final, SDP
  06_Eticheta          eticheta punga, eticheta bax, fisier Colos / Zebra
  07_Implementare      conditii IPN, plan IPN, IL productie, plan HACCP, prod 0
  08_Dosar_validat     TDV validat, dosar final, cod material SAP
```

PROPUNERE: se adauga un al zecelea folder, `09_Revizuire`, pentru rapoartele de la 30,
60 si 90 de zile. Motiv: revizuirea post-implementare produce documente dupa inchiderea
dosarului validat, iar amestecarea lor in `08_Dosar_validat` ar strica principiul ca
dosarul validat este inghetat la data validarii.

### 5.1.2 De ce structura pe faze este superioara celei actuale

| Criteriu | Structura actuala (Antecalcul, Finalizare ST, Implementare, Mostra) | Structura pe faze |
|---|---|---|
| Acoperire | Patru foldere pentru un proces cu noua faze; solicitarea, testarea si eticheta nu au loc propriu si ajung in radacina | Fiecare faza are exact un loc |
| Cautare | "Unde e fisa de test?" nu are raspuns unic | Faza determina folderul, fara ambiguitate |
| Ordine | Numele nu spun ordinea; sortarea alfabetica pune Antecalcul primul, desi este al patrulea in proces | Prefixul numeric ordoneaza folderul in ordinea reala a procesului |
| Audit | Auditorul cere dovezi in ordinea procesului si trebuie ghidat manual | Auditorul parcurge 00 - 08 si vede singur ce lipseste |
| Automatizare | Fisierele din radacina nu se pot lega de un livrabil | Fiecare livrabil are folderul lui tinta, deci incarcarea se poate valida automat |

### 5.1.3 Migrarea folderelor existente

| Pas | Actiune | Cine | Observatie |
|---|---|---|---|
| 1 | Inventar: se listeaza cu un flux toate folderele de proiect si continutul lor, intr-un fisier Excel de lucru | Head of R&D | Fara mutari inca |
| 2 | Maparea folderelor vechi: Antecalcul -> 04, Finalizare ST -> 05, Implementare -> 07, Mostra -> 03 | Head of R&D | Regula fixa |
| 3 | Fisierele din radacina se clasifica dupa nume: cele cu "eticheta" -> 06, cele cu "SAP" sau "material" -> 08, restul -> 00 | Flux + verificare manuala | Vezi 5.1.4 |
| 4 | Se creeaza folderele lipsa (00, 01, 02, 06, 08, 09) in fiecare proiect | Flux | Goale, dar prezente |
| 5 | Se muta fisierele conform mapei, pastrand numele original | Flux | Redenumirea vine la pasul 7 |
| 6 | Se creeaza inregistrarea de proiect in Dataverse si se leaga de folder | Flux de migrare | Vezi Sectiunea 15 |
| 7 | Redenumirea la conventia din 5.2 se face doar pentru proiectele din ultimele 24 de luni | Suport R&D | Vezi 5.1.5 |

5.1.4 Fisierele care nu se pot clasifica automat raman intr-un folder `99_Neclasificat`
din proiect si apar intr-un raport de curatare. Nu se sterge nimic si nu se ghiceste.

5.1.5 NOTA: nu se redenumesc retroactiv toate fisierele istorice. Efortul este de ordinul
a mii de fisiere, castigul este estetic, iar riscul de a rupe legaturi existente este
real. Se redenumesc doar proiectele active si cele din ultimele 24 de luni, care intra
efectiv in audit.

### 5.1.6 Proiectele-copil (.1)

Proiectul-copil primeste folder propriu, `{cod parinte}.1_{nume}`, ca subfolder al
proiectului parinte. Documentele parintelui nu se copiaza; se refera prin legatura din
Dataverse. Motiv: dublarea fizica ar crea doua versiuni ale aceleiasi ST, iar la audit
nu s-ar mai putea spune care este in vigoare.

## 5.2 Conventia de denumire a fisierelor

### 5.2.1 Formatul

```
{cod proiect}_{tip document}_{vNN}_{AAAALLZZ}.{ext}
```

Reguli: fara diacritice; fara spatii (se foloseste `_`); codul de tip document din
nomenclatorul `rd_tipdocument` (5.2.3); versiunea pe doua cifre; data in formatul
AAAALLZZ, care sorteaza cronologic.

### 5.2.2 Exemple reale

| Fisier | Ce este |
|---|---|
| `26025_SCP_v01_20260114.pdf` | Solicitarea initiala pentru proiectul 26025 |
| `26025_PLAN_v01_20260116.docx` | Plan de dezvoltare, prima versiune |
| `26025_PLAN_v02_20260121.docx` | Planul revizuit dupa feedbackul clientului |
| `26025_FTEST_v01_20260119.pdf` | Fisa de test |
| `26025_RTEST_v01_20260122.pdf` | Raport de testare, generat din masuratori |
| `26025_ANTECALC_v03_20260123.xlsx` | A treia varianta de antecalcul |
| `26025_STDRAFT_v01_20260126.pdf` | ST draft |
| `26025_STFINAL_v01_20260202.pdf` | ST finala aprobata |
| `26025_SDP_v01_20260203.pdf` | Specificatia de produs |
| `26025_ETPUNGA_v02_20260204.pdf` | Eticheta de punga, versiunea 2 |
| `26025_PLANIPN_v01_20260206.pdf` | Plan IPN |
| `26025_RPROD0_v01_20260212.pdf` | Raport de productie 0 |
| `26025_TDV_v01_20260215.pdf` | TDV validat, semnat |
| `26025.1_RTEST_v01_20260304.pdf` | Raport de testare pe proiectul-copil |
| `26025_RPI30_v01_20260317.pdf` | Revizuire la 30 de zile |

### 5.2.3 Codurile de tip document

| Cod | Document | Folder | Retentie |
|---|---|---|---|
| SCP | Solicitare cerinta produs | 00 | 5 ani |
| EPC | Eticheta produs client | 00 | 5 ani |
| REF | Documentatie de referinta | 00 | 3 ani |
| PLAN | Plan de dezvoltare produs | 01 | 5 ani |
| CAMP | Cerere achizitii mostra MP | 01 | 3 ani |
| FTEST | Fisa de test | 02 | 5 ani |
| RTEST | Raport de testare | 02 | 5 ani |
| FSENZ | Fisa de evaluare senzoriala | 02 | 5 ani |
| POZA | Documentatie foto | 02 | 3 ani |
| DMOSTRA | Dosar de mostra | 03 | 3 ani |
| ANTECALC | Antecalcul | 04 | 5 ani |
| CONDST | Conditii ST | 05 | 10 ani |
| STDRAFT | ST draft | 05 | 10 ani |
| STFINAL | ST finala | 05 | 10 ani |
| STMP | ST interna materie prima | 05 | 10 ani |
| SDP | Specificatie de produs | 05 | 10 ani |
| ETPUNGA | Eticheta punga | 06 | 10 ani |
| ETBAX | Eticheta bax | 06 | 10 ani |
| ETPRINT | Fisier imprimanta Colos / Zebra | 06 | 5 ani |
| CONDIPN | Conditii IPN | 07 | 10 ani |
| PLANIPN | Plan IPN | 07 | 10 ani |
| IL | Instructiune de lucru | 07 | 10 ani |
| HACCP | Plan HACCP actualizat | 07 | Permanent |
| INSTR | Dovada de instruire | 07 | 5 ani |
| RPROD0 | Raport de productie 0 | 07 | 10 ani |
| TDV | TDV validat | 08 | Permanent |
| DOSAR | Dosar validat complet | 08 | Permanent |
| SAP | Dovada codului de material SAP | 08 | 10 ani |
| RPI30 / RPI60 / RPI90 | Rapoarte de revizuire | 09 | 5 ani |

5.2.4 Denumirea nu se scrie manual. FLX-12 genereaza documentele din sabloane Word cu
numele deja corect; pentru fisierele incarcate manual, aplicatia canvas si formularul
model-driven propun numele prin butonul "Incarca document la livrabil", care primeste
codul de proiect si tipul din contextul livrabilului.

## 5.3 Coloanele de metadate din biblioteca

Biblioteca `PRODUSE IN DEZVOLTARE` primeste urmatoarele coloane de site, cu tipurile
SharePoint corespunzatoare:

| Coloana | Tip SharePoint | Obligatorie | Sursa valorii | Observatii |
|---|---|---|---|---|
| Cod proiect | Text (single line) | Da | Scrisa de flux la incarcare | Indexata |
| Tip document | Choice | Da | Nomenclator 5.2.3 | Indexata |
| Versiune document | Text | Da | Din numele fisierului | Diferita de versiunea SharePoint |
| Status document | Choice: Ciorna / In aprobare / Aprobat / Inlocuit / Retras | Da | Actualizata de fluxul de aprobare | Vezi 5.4 |
| Autor | Person | Da | Utilizatorul care incarca | - |
| Aprobator | Person | Nu | Din livrabilul asociat | - |
| Data aprobarii | Date | Nu | La aprobare | - |
| Produs | Text | Da | Numele produsului din proiect | Pentru cautare libera |
| Linie | Choice | Nu | Codul liniei | - |
| Client | Text | Da | Din proiect | - |
| Faza | Choice: 00 - 09 | Da | Din folderul tinta | Indexata |
| Livrabil asociat | Text | Nu | Codul LIV-nn | Leaga fisierul de inregistrare |
| Confidential | Yes/No | Da | Implicit Nu | Vezi 11.6 |

5.3.1 Coloanele indexate (Cod proiect, Tip document, Faza) sunt obligatorii pentru ca
biblioteca va depasi pragul de 5000 de elemente in mai putin de doi ani la 130-180 de
proiecte pe an cu 20-30 de fisiere fiecare. Fara indexare, vizualizarile filtrate se
opresc cu eroare de prag.

5.3.2 NOTA: metadatele se scriu de flux, nu de utilizator. Un tehnolog cu manusi in hala
nu completeaza 13 coloane. Formularul de incarcare din aplicatie primeste doar fisierul
si tipul de document; restul se deduce din livrabilul si proiectul in context.

## 5.4 Politica de versionare

### 5.4.1 Setari de biblioteca

| Setare | Valoare | Motiv |
|---|---|---|
| Versionare | Majora si minora (publicare) | Ciornele nu trebuie sa fie vizibile companiei |
| Versiuni majore pastrate | 50 | Acopera intreaga viata a unui document de produs |
| Ciorne pastrate per versiune majora | 10 | Suficient pentru un ciclu de revizuire |
| Cine vede ciornele | Autorul si aprobatorii | Restul companiei vede doar versiunile publicate |
| Check-out obligatoriu | Da pentru folderele 05, 06, 07, 08 | Documentele care se aproba nu se editeaza in paralel |
| Cos de reciclare | 93 de zile, plus cos de nivel doi | Recuperare dupa stergere accidentala |

### 5.4.2 Semnificatia versiunilor

| Tip | Cand | Efect |
|---|---|---|
| Minora (0.1, 0.2, ...) | Orice salvare in lucru | Vizibila doar autorului si aprobatorilor |
| Majora (1.0, 2.0, ...) | La publicare, dupa aprobare | Vizibila tuturor; devine versiunea in vigoare |
| Majora noua peste una aprobata | Orice modificare de continut dupa aprobare | Obliga la motivul modificarii si la reaprobare |

### 5.4.3 Ce se blocheaza dupa aprobare

5.4.3.1 La aprobarea unui document (status `Aprobat`), fluxul FLX-19: seteaza versiunea
majora, aplica `Retentie / Nu se poate edita` prin eticheta de retentie Purview daca este
disponibila, altfel seteaza permisiune de citire pe fisier pentru toti in afara de
Calitate si Head of R&D, si scrie data aprobarii in Dataverse.

5.4.3.2 Documentele blocate: ST finala, SDP, eticheta aprobata, plan IPN, plan HACCP,
raport de productie 0, TDV validat. Acestea sunt dovezile de audit; o modificare ulterioara
fara versiune noua ar face dosarul nereconstituibil.

5.4.3.3 Documentele care raman editabile dupa aprobare: planul de dezvoltare (se
actualizeaza in timpul proiectului), dosarul de mostra, documentatia foto.

### 5.4.4 Retentia

Se aplica etichetele de retentie din 5.2.3, la nivel de tip de document. Documentele
`Permanent` (TDV, dosar validat, HACCP) nu se sterg niciodata automat. Restul intra in
revizuire de dispozitie la expirarea termenului, cu aprobarea Head of R&D.

### 5.4.5 Proiectele abandonate si respinse

| Situatie | Ce se intampla cu documentele |
|---|---|
| Solicitare respinsa la triaj | Nu se creeaza folder. SCP-ul ramane ca inregistrare in Dataverse, cu motivul |
| Proiect abandonat dupa acceptare | Folderul se pastreaza integral, se muta in `/PRODUSE IN DEZVOLTARE/{an}/_ABANDONATE/`, cu prefixul `X_` la numele folderului |
| Proiect suspendat | Folderul ramane pe loc. Suspendarea este temporara |
| Proiect respins de client dupa mostra | Se trateaza ca abandonat, cu motivul "Respins de client" |

5.4.5.1 Documentele proiectelor abandonate raman consultabile, read-only, cu retentie de
5 ani. Motiv: peste doi ani, cand acelasi client cere un produs similar, dosarul
abandonat este cea mai ieftina sursa de informatie din companie. Se marcheaza vizibil ca
abandonat, ca sa nu fie confundat cu un produs in productie.

## 5.5 Continutul-cadru al documentelor generate din date

Constructie pe referinta IFS Food v8 (capitolele 4.3 Specificatii, 4.4 Dezvoltare de
produs, 4.5 Achizitii, 5.6 Validare) si practica standard din bakery industrial, nu pe
formularele actuale ale companiei. Formatul intern al ST nu se trateaza aici.

Legenda coloanei "Sursa": [D] = preluat automat din Dataverse; [M] = completat manual;
[C] = calculat.

### 5.5.1 DOC-01 SCP - Solicitare cerinta produs

**Scop**: sa transforme o discutie comerciala intr-o cerinta tehnica evaluabila, astfel
incat triajul sa se poata face fara alte intrebari catre KAM.

**Completeaza**: KAM. **Aproba**: Manager R&D (prin decizia de triaj).

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Numar SCP, data, KAM, client, clasificare client, canal | [D] |
| 2. Produsul cerut | Denumire de lucru, descriere, categorie, gramaj, dimensiuni, bucati pe ambalaj, tip ambalare | [M] |
| 3. Piata | Volum estimat anual, sezonalitate, magazine sau puncte de livrare, pret tinta | [M] |
| 4. Termen | Termen dorit, termen impus extern si tipul lui, data listarii | [M] |
| 5. Motivul cererii | Motiv din nomenclator, context comercial | [M] |
| 6. Referinta de comparatie | Tip, denumire, producator, pret raft, poza, eticheta | [M] |
| 7. Cerinte de eticheta | Limbi, marca, declaratii obligatorii, cerinte de client | [M] + [D] din client |
| 8. Cerinte de ambalaj | Material, format, print, dimensiune bax, paletizare | [M] |
| 9. Restrictii | Alergeni interzisi, aditivi interzisi, cerinte bio / halal, origine | [M] |
| 10. Triaj | Rezultat, motiv, comentariu, data, cod de proiect generat | [D] |

### 5.5.2 DOC-02 Plan de dezvoltare produs

**Scop**: sa fixeze ce se dezvolta, cu ce resurse, in ce pasi si cu ce criterii de
succes, inainte de a consuma materie prima si timp de linie.

**Completeaza**: tehnolog. **Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Cod proiect, produs, client, tehnolog, data, versiune | [D] |
| 2. Obiectiv | Descrierea produsului tinta, in termeni masurabili | [M] |
| 3. Criterii de acceptanta | Gramaj si toleranta, dimensiuni si toleranta, aspect, textura, scor senzorial minim, cost tinta | [M] |
| 4. Abordare tehnologica | Tip de aluat, proces propus, linie vizata, capabilitati necesare | [M] |
| 5. Materii prime | Lista, existente si noi, furnizori propusi, lead time, riscuri | [D] din TBL-07 |
| 6. Plan de testare | Numar de trialuri estimate, ce se varieaza la fiecare, esantioane | [M] |
| 7. Etape si termene | Etapele din sablon, cu date planificate | [D] din TBL-05 |
| 8. Livrabile | Lista livrabilelor aplicabile, cu responsabil si termen | [D] din TBL-03 |
| 9. Riscuri de proiect | Risc, probabilitate, masura | [M] |
| 10. Resurse | Ore de linie estimate, cantitati de MP, cost estimat al dezvoltarii | [M] + [C] |
| 11. Aprobare | Tehnolog, Manager R&D, data | [D] |

### 5.5.3 DOC-03 Fisa de testare

**Scop**: sa defineasca inainte de trial ce se masoara si fata de ce tolerante, astfel
incat rezultatul sa fie interpretabil, nu discutabil.

**Completeaza**: tehnolog. **Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Numar fisa, proiect, produs, versiune de reteta testata, data planificata | [D] |
| 2. Obiectivul testarii | Ce ipoteza se verifica | [M] |
| 3. Reteta | Lista completa de ingrediente cu cantitati, din versiunea testata | [D] din TBL-26 |
| 4. Parametri de proces tinta | Framantare, fermentare, laminare, dospire, coacere, congelare, cu valori si tolerante | [M] |
| 5. Plan de esantionare | Ce se masoara, cate bucati pe tip, in ce moment | [M] + implicit din 6.2.1 |
| 6. Tolerante declarate | Pentru fiecare masuratoare: tinta, toleranta minus, toleranta plus | [M] |
| 7. Criterii senzoriale | Grila aplicabila, scor minim acceptabil, defecte eliminatorii | [D] din TBL-18 |
| 8. Resurse si siguranta | Cantitate de aluat, timp de linie, alergeni prezenti, masuri de separare | [M] |
| 9. Aprobare | Tehnolog, Manager R&D, data | [D] |

### 5.5.4 DOC-04 Raport de testare

**Scop**: sa arate ce a iesit, cu cifre, si sa sustina decizia de a continua sau de a
relua.

**Completeaza**: se genereaza integral din date; tehnologul adauga doar concluzia.
**Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Proiect, fisa de testare, trial, data, linie, schimb, operator | [D] |
| 2. Reteta executata | Ingrediente si cantitati reale | [D] |
| 3. Parametri realizati fata de tinta | Tabel cu specificat, real, abatere, in toleranta | [D] + [C] |
| 4. Randament | Aluat introdus, bucati obtinute, randament calculat, pierderi pe faze | [C] |
| 5. Masuratori | Pe tip: n, media, abaterea standard, CV, min, max, conformitate | [C] din TBL-16b |
| 6. Neconformitati | Masuratorile in afara tolerantei, cu bucata si valoarea | [D] |
| 7. Evaluare senzoriala | Scor ponderat, scor pe criterii, verdict, comparatie cu referinta | [D] din TBL-17 |
| 8. Defecte constatate | Defect, severitate, procent afectat, poza | [D] |
| 9. Documentatie foto | Pozele din masuratori si defecte | [D] |
| 10. Concluzie si decizie | Reusit / Reusit cu observatii / Nereusit, ce se schimba la trialul urmator | [M] |
| 11. Aprobare | Tehnolog, Manager R&D, data | [D] |

### 5.5.5 DOC-05 Fisa de evaluare senzoriala

**Scop**: sa produca un verdict repetabil si aparabil, nu o impresie.

**Completeaza**: evaluatorii, pe telefon. **Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Numar evaluare, proiect, trial, data, tip de evaluare | [D] |
| 2. Conditii de degustare | Temperatura de servire, timp de la coacere, ordinea probelor, codificare oarba | [M] |
| 3. Panel | Evaluatori, rol, experienta | [D] |
| 4. Grila | Criterii cu pondere, ancore descriptive pentru 1, 3 si 5 | [D] din TBL-18 |
| 5. Scoruri individuale | Scor pe evaluator si criteriu, cu comentariu la scor <= 2 | [M] |
| 6. Scoruri comparative | Aceleasi criterii, aplicate referintei | [M] |
| 7. Sinteza | Scor ponderat produs, scor ponderat referinta, diferenta, dezacord maxim | [C] |
| 8. Defecte bifate | Din lista, cu severitate si procent | [M] |
| 9. Verdict | Acceptat / Acceptat cu observatii / Respins, cu regula din 6.5.5 | [C] + [M] |
| 10. Actiuni cerute | Ce se modifica, cine, pana cand | [M] |

### 5.5.6 DOC-06 Antecalcul

**Scop**: sa arate daca produsul are marja la pretul discutat, inainte de a-l promite.

**Completeaza**: tehnolog. **Aproba**: Manager R&D (si Financiar, daca marja este sub
prag).

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Proiect, produs, versiune de antecalcul, versiune de reteta, data, linie | [D] |
| 2. Ipoteze | Lot de referinta, viteza de linie, pierdere tehnologica, randament asumat | [M] + [D] din linie |
| 3. Materii prime | Ingredient, cantitate kg/100kg, pret unitar, sursa pretului, data pretului, cost | [D] + [C] |
| 4. Cost MP | Total MP, ajustat cu pierderea tehnologica | [C] |
| 5. Ambalaj | Punga, bax, eticheta, palet, cost pe bucata | [M] + [C] |
| 6. Manopera | Timp de linie, tarif orar, numar de operatori, cost pe kg | [C] |
| 7. Energie si congelare | Cost de coacere, cost de congelare separat, utilitati | [C] |
| 8. Regie | Procent aplicat, baza de aplicare | [D] parametru |
| 9. Cost total | Pe kg si pe bucata | [C] |
| 10. Pret si marja | Pret tinta, marja bruta, comparatie cu pragul companiei | [C] |
| 11. Sensibilitate | Efectul unei variatii de +/- 10% la cele mai scumpe trei materii prime | [C] |
| 12. Aprobare | Tehnolog, Manager R&D, data | [D] |

PROPUNERE: sectiunea 11 (sensibilitate) nu exista azi. Motiv: la produse de panificatie
congelata, faina si grasimea de laminare fac tipic peste 60% din costul de materie prima,
iar volatilitatea lor decide singura daca marja promisa tine sase luni.

### 5.5.7 DOC-07 SDP - Specificatie de produs

**Scop**: sa fie sursa unica din care se scrie instructiunea de lucru si dupa care se
produce, in timpul si dupa implementare.

**Completeaza**: tehnolog. **Aproba**: Manager R&D si Calitate.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Cod SAP, denumire, versiune, data, linie, aprobatori | [D] |
| 2. Descrierea produsului | Denumire legala, descriere, gramaj, dimensiuni, forma, aspect tinta | [D] |
| 3. Reteta de productie | Ingrediente, cantitati pe sarja de productie, ordinea de adaugare, faza | [D] din TBL-26 |
| 4. Proces pas cu pas | Pentru fiecare faza: parametru, valoare, toleranta, echipament, durata | [D] din trialul validat |
| 5. Puncte critice | CCP si oPRP din planul HACCP, valori limita, monitorizare, actiune la deviatie | [D] + [M] Calitate |
| 6. Controale in proces | Ce se verifica, la ce frecventa, cine, ce se inregistreaza | [M] |
| 7. Ambalare | Tip de ambalaj, numar de bucati, gramaj net, toleranta de cantarire, eticheta aplicata | [D] |
| 8. Paletizare | Bucati pe bax, baxuri pe strat, straturi pe palet, eticheta de palet | [M] |
| 9. Depozitare si transport | Temperatura, umiditate, termen de valabilitate, conditii de transport | [M] |
| 10. Utilizare la client | Decongelare, dospire, coacere, timp si temperatura, randament asteptat | [M] |
| 11. Alergeni | Alergeni continuti, urme, masuri de separare pe linie | [D] din Sectiunea 9 |
| 12. Valori nutritionale | Tabelul pe 100 g si pe portie | [D] |
| 13. Istoricul versiunilor | Versiune, data, modificare, autor, aprobator | [D] |

### 5.5.8 DOC-08 Conditii IPN si Plan IPN

**Scop**: sa garanteze ca nimic nu lipseste inainte de prima productie pe linie, si sa
spuna cine face ce in ziua respectiva.

**Completeaza**: tehnolog. **Aproba**: Manager R&D, Calitate, Productie.

Conditii IPN - checklist, fiecare pozitie cu bifa, responsabil si dovada:

| Nr | Conditie | Responsabil | Dovada |
|---|---|---|---|
| 1 | ST finala aprobata | Tehnolog | LIV-24 |
| 2 | SDP aprobata | Tehnolog | LIV-25 |
| 3 | Cod material SAP creat pentru produsul finit | Tehnolog | LIV-26 |
| 4 | Toate materiile prime receptionate si eliberate de Calitate | Achizitii | TBL-07 |
| 5 | Ambalajul disponibil in cantitate suficienta | Achizitii | LIV-29 |
| 6 | Eticheta aprobata si fisierul de imprimanta incarcat | Suport R&D | LIV-28, LIV-29 |
| 7 | Plan HACCP actualizat si aprobat | Calitate | LIV-34 |
| 8 | IL de productie emisa si afisata la linie | Tehnolog | LIV-33 |
| 9 | Operatorii instruiti, cu lista de prezenta | Productie | LIV-35 |
| 10 | Slotul de linie confirmat in planificare | Planificare | TBL-02 |
| 11 | Setarile de linie pregatite (scule, forme, matrite) | Productie | [M] |
| 12 | Plan de esantionare pentru productia 0 stabilit | Tehnolog | Sectiunea 7 |
| 13 | Decizia de destinatie a productiei 0 (vanzare, mostra, rebut) | Manager R&D | [M] |

Plan IPN:

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Proiect, produs, linie, data, schimb, cantitate planificata | [D] |
| 2. Echipa | Tehnolog, sef de tura, operator-cheie, Calitate, Mentenanta, cine decide oprirea | [M] |
| 3. Program orar | Ora de setup, ora de start, puncte de verificare, ora estimata de final | [M] |
| 4. Parametri de urmarit | Din SDP, cu valorile si tolerantele | [D] |
| 5. Plan de esantionare | Ce, cand, cate bucati, cine masoara | [M] |
| 6. Criterii de oprire | Ce abatere opreste productia si cine decide | [M] |
| 7. Destinatia produsului | Vanzabil / mostra / rebut, cu decizie asumata | [M] |
| 8. Riscuri anticipate | Ce poate merge prost, ce se pregateste dinainte | [M] |
| 9. Aprobare | Trei semnaturi: R&D, Calitate, Productie | [D] |

### 5.5.9 DOC-09 Raport de productie 0

**Scop**: sa transforme prima productie intr-o validare documentata, nu intr-o amintire.
Continutul complet este in Sectiunea 7; structura documentului urmeaza sectiunile 7.2 -
7.9, plus decizia finala si semnaturile.

### 5.5.10 DOC-10 Dosar TDV validat

**Scop**: sa fie dovada unica, la audit si la reclamatie, ca produsul a fost dezvoltat,
testat si validat corect.

**Completeaza**: suport R&D, prin generare automata. **Aproba**: Manager R&D si
Managementul Calitatii.

| Sectiune | Continut | Sursa |
|---|---|---|
| 1. Pagina de garda | Cod proiect, produs, client, cod SAP, data validarii, semnaturi | [D] |
| 2. Cerinta initiala | SCP, cu referinta de comparatie | [D] |
| 3. Traseul proiectului | Etape cu date planificate si reale, blocaje cu motiv | [D] |
| 4. Reteta validata | Versiunea validata, cu istoricul versiunilor | [D] |
| 5. Rezultate de testare | Sinteza trialurilor, statistica, conformitatea | [D] |
| 6. Evaluare senzoriala | Verdictul final si comparatia cu referinta | [D] |
| 7. Antecalcul aprobat | Costul si marja la data validarii | [D] |
| 8. Specificatii | ST finala, SDP, cu versiunile in vigoare | [D] |
| 9. Alergeni si nutritionale | Valorile calculate si baza de calcul | [D] |
| 10. Eticheta aprobata | Imaginea etichetei si data aprobarii | [D] |
| 11. Implementare | Conditii IPN, plan IPN, plan HACCP, IL | [D] |
| 12. Productie 0 | Raportul si decizia | [D] |
| 13. Lista livrabilelor | Toate livrabilele cu status, data si responsabil | [D] |
| 14. Declaratie de validare | Textul de validare, semnat R&D si Calitate | [M] |

5.5.10.1 Dosarul TDV se genereaza integral din date, ca PDF, cu link-uri catre fisierele
sursa. Nimeni nu il asambleaza manual. Aceasta este dovada practica ca "dosarul de produs
este reconstituibil oricand".

### 5.5.11 DOC-11 Raport de revizuire post-implementare

Structura urmeaza Sectiunea 8: identificare, perioada acoperita, reclamatii si
neconformitati, randament in serie fata de productia 0, rebut, feedback client si KAM,
cost real fata de antecalcul, volum realizat fata de estimat, decizie (mentinere,
optimizare, retragere), actiuni cu responsabil si termen, semnaturi.

## 5.6 Trasabilitatea

### 5.6.1 Ce se auditeaza in Dataverse

| Ce | Nivel | Motiv |
|---|---|---|
| Toate tabelele din 2.1 - 2.20 | Creare, modificare, stergere, atribuire | Cerinta IFS de trasabilitate |
| Coloanele de status | Modificare | Cine a mutat proiectul si cand |
| Coloanele de termen (propus, negociat, realizat) | Modificare | Sursa disputelor cu comercialul |
| Scorul si suprascrierea de prioritate | Modificare | Cerinta explicita: urma in audit |
| Aprobarile (aprobator, data aprobarii) | Modificare | Dovada de semnatura |
| Reteta si liniile de reteta | Toate | Reconstituirea produsului la orice data |
| Alergeni si valori nutritionale | Modificare | Raspundere legala |
| Accesul la citire | Doar pe tabelele marcate confidential | Auditul de citire este scump; se aplica selectiv |

### 5.6.2 Cine vede istoricul

| Rol | Ce istoric vede |
|---|---|
| Head of R&D, Manager R&D | Tot, pe toate tabelele |
| Calitate | Tot ce tine de specificatii, alergeni, HACCP, aprobari |
| Tehnolog | Istoricul proiectelor proprii |
| Auditor (rol dedicat, temporar) | Citire pe tot, inclusiv audit, fara drept de modificare |
| KAM, restul companiei | Nu vad istoricul de audit; vad doar starea curenta si datele |

5.6.2.1 PROPUNERE: rol de securitate `RD Auditor`, activat pe durata auditului si
dezactivat dupa. Motiv: auditorul extern are nevoie de acces de citire demonstrabil, dar
nu trebuie sa aiba cont permanent cu drepturi largi.

### 5.6.3 Cum se demonstreaza la audit

5.6.3.1 Intrebarea tipica de audit este "aratati-mi cum a fost dezvoltat produsul X si
cine a aprobat ce". Raspunsul se da in trei pasi, din aplicatie, in fata auditorului:

| Pas | Ecran | Ce arata |
|---|---|---|
| 1 | Formularul de proiect, fila Livrabile | Toate livrabilele, cu responsabil, termen, data realizarii, aprobator, link la document |
| 2 | Butonul "Genereaza dosar TDV" | PDF-ul complet, cu toate documentele in vigoare la data validarii |
| 3 | Fila Audit history, pe inregistrarea sau coloana ceruta | Cine a modificat, ce valoare a fost inainte, ce valoare dupa, la ce data si ora |

5.6.3.2 Pentru documente, versiunea in vigoare la o data din trecut se obtine din
istoricul de versiuni SharePoint al fisierului, care pastreaza autorul si data fiecarei
publicari.

5.6.3.3 NOTA de platforma: auditul Dataverse are retentie configurabila la nivel de
mediu, implicit limitata. Se seteaza explicit retentia de audit la valoarea maxima
disponibila in licenta si, pentru cerinta IFS de pastrare peste acea limita, se ruleaza
lunar FLX-20, care exporta jurnalul de audit al tabelelor critice intr-o biblioteca
SharePoint de arhiva, cu retentie proprie. Fara acest export, jurnalul de audit se pierde
tacit dupa perioada de retentie a mediului.
