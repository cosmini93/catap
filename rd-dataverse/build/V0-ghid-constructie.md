# Valul 0 - Ghid de constructie pas cu pas

Executarea promptului P-01 din Sectiunea 21. Rezultatul Valului 0: mediul, solutia,
nomenclatoarele, sabloanele si rolurile, gata pentru ca Valul 1 sa poata incepe.

**Efort estimat**: 8-10 zile-om. **Durata**: 2-3 saptamani.
**Cine il foloseste**: numai constructorul. Nu se da acces nimanui in acest val.

---

## Inainte de a incepe

| Verificare | De ce conteaza |
|---|---|
| Ai licenta care include Dataverse si conectori premium | Fara ea nu se poate crea mediul Developer |
| Ai decis prefixul de editor: `rd` | Nu se mai poate schimba dupa primul export (2.0.1) |
| Ai citit Sectiunea 20, intrebarile IQ-01 si IQ-10 | Ambele schimba calendarul, nu si continutul Valului 0 |
| Ai la indemana datele celor 9 linii de productie | Pasul 5.2 se blocheaza fara ele |

Valul 0 se poate construi integral fara raspunsurile la intrebarile deschise. Toate
folosesc valorile implicite din Sectiunea 20.

---

## Pasul 1 - Mediul Developer

1.1 Din Power Platform admin center, creeaza un mediu de tip **Developer**, cu baza de
date Dataverse, in regiunea tenantului (Europa). Limba: romana sau engleza, consecvent.

1.2 Noteaza URL-ul mediului. Va aparea in toate procedurile ulterioare.

1.3 **Nu** activa inca niciun grup de securitate pe mediu. In Valul 0 esti singurul
utilizator.

1.4 NOTA: mediul Developer se dezactiveaza automat dupa o perioada de inactivitate si
dispare odata cu contul tau. Este RSC-01, riscul cel mai grav din blueprint. Masura de
la pasul 8 (exportul dublu) nu este optionala.

---

## Pasul 2 - Politica DLP

Se face **inainte** de a construi ceva, nu dupa. O politica aplicata peste fluxuri
existente le opreste, iar diagnosticarea este neplacuta.

2.1 Creeaza o politica DLP dedicata mediilor R&D.

| Grup | Conectori |
|---|---|
| Business (permisi) | Dataverse, SharePoint, Office 365 Outlook, Office 365 Users, Approvals, Microsoft Teams, Excel Online, Word Online, OneDrive for Business |
| Blocati | Tot restul, in special: conectorii de retele sociale, storage extern (Dropbox, Box, Google Drive), servicii AI publice, HTTP generic |

2.2 Motivul, pe scurt: cerinta din brief este ca datele sa nu paraseasca tenantul
companiei (11.7.6). Conectorul HTTP generic si serviciile externe sunt singurele cai
prin care s-ar putea intampla accidental.

---

## Pasul 3 - Solutia si editorul

3.1 Creeaza editorul (publisher):

| Camp | Valoare |
|---|---|
| Nume afisat | RD Digital |
| Nume | rddigital |
| Prefix | **rd** |
| Prefix valoare optiune | 10000 |

3.2 Creeaza solutia:

| Camp | Valoare |
|---|---|
| Nume afisat | RD Suita Digitala |
| Nume | RDSuitaDigitala |
| Editor | RD Digital |
| Versiune | 0.1.0.0 |

3.3 **Regula absoluta de la acest moment inainte**: nimic nu se creeaza in afara
solutiei. Nici o tabela, nici un flux, nici o aplicatie, nici o vizualizare. Componentele
create direct in mediu nu pleaca la export si sunt cea mai frecventa cauza de "merge la
mine, nu merge in productie" (17.2.1.1).

3.4 Creeaza variabilele de mediu (environment variables) din tabelul de mai jos, in
solutie. Toate valorile de business stau aici, niciodata codificate in fluxuri (12.1.2).

| Nume | Tip | Valoare implicita | Ce controleaza |
|---|---|---|---|
| rd_SiteSharePoint | Text | URL-ul site-ului | Unde se creeaza folderele |
| rd_BibliotecaProiecte | Text | PRODUSE IN DEZVOLTARE | Numele bibliotecii |
| rd_DurataStandardZile | Whole Number | 14 | Durata de referinta a proiectului |
| rd_CapacitateImplicitaTehnolog | Whole Number | 6 | Praguri de incarcare |
| rd_BugetUrgentaKAM | Whole Number | 2 | Proiecte P1 simultane pe KAM |
| rd_ExpirareSuprascriereZile | Whole Number | 90 | Expirarea suprascrierii de scor |
| rd_PragMarjaAprobareDubla | Decimal | valoarea companiei | Cand antecalculul cere doua aprobari |
| rd_PondereVolum | Whole Number | 30 | Componenta de scor |
| rd_PondereClient | Whole Number | 20 | Componenta de scor |
| rd_PondereTermen | Whole Number | 20 | Componenta de scor |
| rd_PondereEfort | Whole Number | 10 | Componenta de scor |
| rd_PondereRiscMP | Whole Number | 10 | Componenta de scor (se scade) |
| rd_PondereReutilizare | Whole Number | 10 | Componenta de scor |
| rd_PlafonImbatranire | Whole Number | 20 | Plafonul bonusului de asteptare |
| rd_EmailAdministrator | Text | adresa ta | Unde ajung erorile de flux |

---

## Pasul 4 - Choice-urile globale

4.1 Se creeaza **inaintea tabelelor**. O coloana Choice creata inainte de setul global
ramane locala si nu se mai poate converti.

4.2 Sursa: `data/choices.json` si `build/import/choices-globale.csv` (178 de valori,
25 de seturi). Fisierul CSV este pentru verificare si documentare; seturile se creeaza
in interfata Dataverse, unde nu exista import de option sets.

4.3 Ordinea nu conteaza intre ele, dar toate 25 trebuie sa existe inainte de pasul 6.
Verificare: numarul de seturi din solutie = 25.

4.4 Atentie la doua dintre ele:

| Set | Ce are special |
|---|---|
| `rd_alergen` | Este multi-select (Choices, nu Choice). 14 valori fixe, din Anexa II Reg. 1169/2011 |
| `rd_statusproiect` | 14 valori, in ordinea din 2.2.1. Ordinea conteaza pentru afisare |

---

## Pasul 5 - Nomenclatoarele

Ordinea este obligatorie: fiecare depinde de cele dinainte (15.2).

### 5.1 Tabelele care nu depind de nimic

Creeaza tabelele, apoi importa fisierele:

| Ordine | Tabela | Fisier de import | Randuri | Stare |
|---|---|---|---|---|
| 1 | `rd_motiv` (TBL-41) | `nomenclator-motive.csv` | 40 | Gata |
| 2 | `rd_tipdocument` (TBL-42) | `nomenclator-tipuri-document.csv` | 31 | Gata |
| 3 | `rd_alergen` (TBL-27) | `nomenclator-alergeni.csv` | 14 | Gata |
| 4 | `rd_defect` (TBL-20a) | `nomenclator-defecte.csv` | 22 | Gata |
| 5 | `rd_criteriusenzorial` (TBL-18) | `nomenclator-criterii-senzoriale.csv` | 17 | Gata |

### 5.2 Liniile de productie

| Ordine | Tabela | Fisier | Randuri | Stare |
|---|---|---|---|---|
| 6 | `rd_linie` (TBL-36) | `nomenclator-linii_SABLON.csv` | 9 | **De completat** |

Sablonul are codurile L01-L09 si valorile implicite (timp de schimb 120 de minute,
pierdere tehnologica 3%, prag de supraincarcare 6). Restul se completeaza in discutie cu
Productia si Planificarea.

Campurile pe care nu le poti completa singur, si de la cine le iei:

| Camp | De la cine |
|---|---|
| Capabilitati, tip linie, echipament | Productie |
| Gramaj minim si maxim, latime banda | Productie / Tehnic |
| Viteza nominala | Productie / Planificare |
| Timp real de schimb sortiment | Planificare (cele 120 de minute sunt implicitul) |
| Tarif orar | Controlling / Financiar |
| Alergeni prelucrati pe linie | Calitate (necesar pentru 9.4.4) |

Capabilitatile se scriu separate prin `;` din lista: Laminare, Impletire, Injectare
umplutura, Depunere, Presarare, Glazurare, Coacere tunel, Congelare rapida, Ambalare
flow-pack, Ambalare tava.

### 5.3 Profilurile de tehnolog

| Ordine | Tabela | Fisier | Randuri | Stare |
|---|---|---|---|---|
| 7 | `rd_profiltehnolog` (TBL-37) | `nomenclator-profiluri-tehnolog_SABLON.csv` | ~30 | **De completat** |

Sursa: utilizatorii din Entra ID, plus configurarea manuala a rolului principal, a
specializarii si a capacitatii maxime. Este singurul nomenclator care cere date din
afara blueprintului si care totusi intra in Valul 0, pentru ca fara el nu se poate testa
matricea de securitate la pasul 10.

### 5.4 Tabelele care se creeaza acum, dar se populeaza in Valul 1

| Ordine | Tabela | Fisier pregatit | Cand se populeaza | Sursa datelor |
|---|---|---|---|---|
| 8 | `rd_client` (TBL-38) | `nomenclator-clienti_SABLON.csv` | Val 1, pasul 4 din 15.2 | Export SAP + clasificare de la Sales |
| 9 | `rd_furnizor` (TBL-10) | `nomenclator-furnizori_SABLON.csv` | Val 1, pasul 5 din 15.2 | Export SAP |
| 10 | `rd_materieprima` (TBL-09) | `nomenclator-materii-prime_SABLON.csv` | Val 1, pasul 6 din 15.2 | SAP pentru coduri, ST-uri furnizor pentru restul |

5.4.1 **Linia de demarcatie intre Valul 0 si migrarea din Valul 1**: in Valul 0 se
populeaza nomenclatoarele care vin din blueprint si din discutia interna (motive, tipuri
de documente, alergeni, defecte, criterii senzoriale, sabloane, linii, profiluri). In
Valul 1 se populeaza cele care vin din sistemele companiei si cer extragere de date
(clienti, furnizori, materii prime, proiecte istorice).

5.4.2 Motivul demarcatiei este calendarul, nu eleganta. Extragerea si curatarea datelor
din SAP depinde de alti oameni si de disponibilitatea lor; daca intra in Valul 0, Valul 0
nu se mai termina in 2-3 saptamani si tot roadmap-ul aluneca. Tabelele se creeaza insa
acum, ca structura, pentru ca lookup-urile din Valul 1 sa aiba ce sa refere.

5.4.3 Pentru materiile prime, cand se ajunge la ele: **nu incerca sa le introduci pe
toate**. Prima transa este de 150-250 de coduri, cele folosite in proiectele active si in
produsele de volum mare, care acopera aproximativ 90% din utilizare. Restul se
completeaza la utilizare, prin regula din 15.2.2.

5.4.4 Clasificarea A/B/C a clientilor nu o stabilesti tu. O ceri de la Sales, in scris,
cu numele persoanei care raspunde de ea (intrebarea IQ-04). Cererea se face **acum**, in
Valul 0, chiar daca importul se face in Valul 1 - este exact genul de raspuns care
intarzie trei saptamani. Daca nu vine la timp, importa clientii cu clasificarea goala;
sistemul ii trateaza ca B pana la clasificare (A1.1.3).

---

## Pasul 6 - Sabloanele

| Ordine | Tabela | Fisier de import | Randuri | Stare |
|---|---|---|---|---|
| 11 | `rd_sablonetapa` (TBL-06) | `sablon-etape.csv` | 11 | Gata |
| 12 | `rd_sablonlivrabil` (TBL-04) | `sablon-livrabile.csv` | 43 | Gata |

6.1 Sablonul de etape se importa primul: sablonul de livrabile are lookup catre el
(REL-24).

6.2 Coloana `Tip proiect aplicabil` din ambele fisiere este multi-select, cu valorile
separate prin `;`. Excluderile din 4.7 si 14.2.3 sunt deja aplicate in fisiere - de
exemplu, LIV-18 (antecalcul) nu apare la tipurile Abatere si Transfer pe alta linie.

6.3 Dupa import, verifica: 43 de randuri in sablonul de livrabile, dintre care 35
obligatorii. Numarul de livrabile aplicabile unui proiect de tip Produs nou este 43;
pentru Abatere este 39.

6.4 Coloana `Sablon Word` contine codul tipului de document (SCP, PLAN, FTEST...). Este
o referinta text catre `rd_tipdocument`, folosita de FLX-12 in Valul 2. In Valul 0 este
suficient sa existe.

---

## Pasul 7 - Rolurile de securitate

7.1 Se construiesc **acum**, nu la sfarsit. Retrofitarea securitatii intr-o solutie
construita fara ea costa de trei ori mai mult (16.1).

7.2 Creeaza cele 6 echipe din 11.1.2 si leaga-le de grupuri Entra ID:

| Echipa | Grup Entra ID de cerut de la IT |
|---|---|
| Echipa R&D | RD-Departament |
| Echipa Comercial | RD-Comercial |
| Echipa Achizitii | RD-Achizitii |
| Echipa Calitate | RD-Calitate |
| Echipa Planificare si Productie | RD-Productie |
| Toata compania | grupul existent de toti angajatii |

7.3 Creeaza cele 13 roluri din 11.2, cu drepturile din matricele 11.4.1 - 11.4.5.

7.4 Trei reguli care se aplica tuturor rolurilor:

| Regula | Unde |
|---|---|
| Dreptul de stergere pe tabelele de proces: numai RD Head si RD Administrator | 11.7.1 |
| Dreptul de atribuire (Assign): numai RD Head si RD Manager | 11.7.2 |
| Rolul RD Auditor se creeaza acum, dar nu se atribuie nimanui | 11.7.4 |

7.5 Profilurile de securitate pe coloana (11.5) se pot amana pana la Valul 1, cand exista
tabelele care le folosesc. Noteaza-le ca datorie, nu le uita: coloanele de cost, marja,
pret si incarcare individuala nu trebuie sa ajunga la toata lumea.

---

## Pasul 8 - SharePoint

8.1 Cere de la IT un site de tip Team, dedicat. Creeaza in el:

| Biblioteca | Continut |
|---|---|
| `PRODUSE IN DEZVOLTARE` | Folderele de proiect |
| `Sabloane` | Sabloanele Word, registrul de versiuni, documentatia de preluare |
| `Arhiva audit R&D` | Exporturile lunare de jurnal de audit (FLX-20, Val 3) |

8.2 In biblioteca `PRODUSE IN DEZVOLTARE`, creeaza cele 13 coloane de metadate din 5.3.

8.3 **Indexeaza** coloanele Cod proiect, Tip document si Faza. La 130-180 de proiecte pe
an cu 20-30 de fisiere fiecare, biblioteca depaseste pragul de 5000 de elemente in mai
putin de doi ani, iar vizualizarile filtrate se opresc cu eroare (5.3.1).

8.4 Aplica setarile de versionare din 5.4.1: versionare majora si minora, 50 de versiuni
majore, 10 ciorne, check-out obligatoriu pe folderele 05, 06, 07, 08.

8.5 Configureaza permisiunile pe grupuri, conform 11.6.1. Compania **nu** primeste acces
la biblioteca; vede statusul in aplicatie.

---

## Pasul 9 - Procedura de export

9.1 Exporta solutia, in ambele forme:

```
RD_Solutions/{AAAALLZZ}_RDSuitaDigitala_v{n}_unmanaged.zip
RD_Solutions/{AAAALLZZ}_RDSuitaDigitala_v{n}_managed.zip
```

9.2 Salveaza in **doua** locuri: OneDrive (cum cere 2.0.2) si o biblioteca SharePoint a
companiei. OneDrive-ul personal dispare odata cu contul; este exact riscul RSC-01.

9.3 Pune-ti o recurenta saptamanala in calendar pentru export. 15 minute pe saptamana.

9.4 Deschide registrul de versiuni in biblioteca `Sabloane`, cu coloanele: versiune,
data, ce contine, cine a facut importul, actiuni manuale necesare dupa import (17.2.3).

---

## Pasul 10 - Verificarea Valului 0

Criteriile de acceptanta aplicabile: CA-01 ... CA-06, CA-106, CA-107, CA-111.

| Nr | Verificare | Criteriu de trecere |
|---|---|---|
| 1 | Toate componentele sunt in solutie | Zero componente in afara ei |
| 2 | Exportul si importul intr-un al doilea mediu | Fara erori |
| 3 | Numarul de Choice-uri globale | 25 |
| 4 | Numarul de tabele create | 12 (9 populate, 3 create si goale) |
| 5 | Nomenclatorul de motive | 40 de randuri |
| 6 | Tipurile de documente | 31 de randuri |
| 7 | Criteriile senzoriale | 17 randuri, suma ponderilor = 100 pe fiecare categorie |
| 8 | Cele 9 linii de productie | Toate cu capabilitati si gramaje reale, nu goale |
| 8b | Profilurile de tehnolog | Fiecare persoana din R&D, cu rol si capacitate |
| 9 | Sablonul de livrabile | 43 de randuri, 35 obligatorii |
| 10 | Sablonul de etape | 11 randuri, suma lantului critic = 21 |
| 11 | Rolurile de securitate | 13, cu matricea aplicata |
| 12 | Un utilizator de test din fiecare rol | Vede exact ce trebuie si nimic in plus |
| 13 | Politica DLP | Activa pe mediu, cu conectorii din pasul 2 |
| 14 | Biblioteca SharePoint | Coloane create, cele trei indexate, versionare setata |
| 15 | Exportul de solutie | Salvat in ambele locatii, cu registrul deschis |

10.1 Verificarea 12 este cea care se sare cel mai des si cea care doare cel mai tare mai
tarziu. Cere-i unui coleg din fiecare departament 10 minute, atribuie-i rolul, si uita-te
impreuna cu el la ce vede.

10.2 Verificarea 2 nu este optionala. Un export care nu se importa curat intr-un mediu
gol inseamna ca solutia nu se poate muta in productie, si afli asta acum, nu peste sase
luni.

---

## Ce urmeaza

Valul 1 incepe cu promptul P-02 din Sectiunea 21 (solicitare si triaj), apoi P-03
(proiect, livrabile, etape), P-04 (documente), P-05 (testare si masuratori), P-06
(alocare si termen), P-17 (migrarea).

Termenul Valului 1 este ferm: 30 de zile. Tot ce nu incape se amana, nimic din el nu se
amana (16.2.1).

---

## Regenerarea fisierelor de import

Fisierele din `build/import/` se genereaza din `data/*.json`:

```
python3 build/genereaza-import.py
```

Nu edita CSV-urile direct daca vrei sa pastrezi sincronizarea cu blueprintul. Modifica
JSON-ul si regenereaza. Exceptie: fisierele cu sufixul `_SABLON`, care se completeaza
manual cu datele companiei si nu se regenereaza peste.
