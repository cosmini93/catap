# Blueprint Suita Digitala R&D
## Dataverse / Power Apps / SharePoint / Power Automate

**Export complet al documentatiei. Generat 09.09.2026.**

---

## Context pentru cine citeste acest document fara istoricul discutiei

### Ce este

Blueprint de arhitectura si constructie pentru digitalizarea procesului R&D intr-o
companie FMCG de panificatie si patiserie congelata: 2 amplasamente, 9 linii de productie,
aproximativ 400 de angajati, intre 130 si 180 de proiecte de dezvoltare de produs pe an.

Situatia de plecare: evidenta se tine intr-un formular Excel cu aproximativ 30 de coloane
care sunt bife de existenta a livrabilelor, plus foldere in SharePoint. Formatul este
mostenit si nu este considerat satisfacator.

### Cine il construieste

Head of R&D, inginer, **singur, fara echipa IT**, in paralel cu functia de baza. Aceasta
constrangere este cea mai importanta din tot documentul si explica majoritatea deciziilor
de secventiere: solutia trebuie sa fie utila si daca se opreste la jumatate.

### Deciziile de arhitectura care nu se renegociaza

1. Baza de date: **Dataverse**. Motiv: relatii parinte-copil reale, tipuri stricte, reguli
   in date, audit nativ, fara limita de delegare.
2. Constructia incepe intr-un mediu **Developer** personal, cu tot ce se construieste
   intr-o **Solution unica**, exportata periodic.
3. Interfata: o aplicatie **model-driven** pentru birou si una **canvas** pentru mobil,
   folosita la linie si in laborator.
4. Documentele raman in **SharePoint**, un folder per proiect, generat automat, legat de
   inregistrarea de proiect prin integrarea nativa de documente.
5. **Power Automate** pentru aprobari, alerte, generarea folderului si a documentelor.
6. Raportare: **Power BI** sau vizualizari native, read-only.
7. Integrarea cu **SAP**: import, export sau citire. **Niciodata scriere.**

### Ce contine documentul

| Zona | Sectiuni |
|---|---|
| Model de date si documentatie | S00-S05 |
| Procese de business | S06-S15 |
| Roadmap, riscuri, acceptanta | S16-S21, A1 |
| Sinteza cu un al doilea blueprint, extensii, operare | S22-S28, A2 |

Cifrele modelului: **60 de tabele, 985 de coloane, 151 de relatii, 31 de seturi de optiuni
globale, 43 de livrabile de proiect, 35 de fluxuri, 13 roluri de securitate.**

### Ce mai exista, in afara acestui document

Repository-ul contine si artefactele prelucrabile, care nu sunt incluse aici pentru ca
sunt redundante cu textul: modelul ca JSON (`data/`), fisierele CSV de import, scripturile
de provizionare care creeaza componentele in Dataverse prin Web API, cele 12 sabloane Word
si o macheta HTML a ecranelor.

### Conventii de referinta

`TBL-nn` tabela &middot; `REL-nn` relatie &middot; `LIV-nn` livrabil &middot; `ETP-nn`
etapa &middot; `FLX-nn` flux &middot; `ECR-nn` ecran &middot; `ROL-nn` rol &middot;
`RSC-nn` risc &middot; `CA-nn` criteriu de acceptanta &middot; `DOC-nn` document generat
&middot; `RAP-nn` raport &middot; `M-nn` modul &middot; `IQ-nn` intrebare deschisa

`PROPUNERE` marcheaza un element propus de arhitect, care nu venea din cerinta initiala.
`NOTA` marcheaza un conflict intre cerinta si buna practica de platforma.

### Limba

Romana **fara diacritice**, cerinta explicita a briefingului initial. Numerotarea este
consecventa in tot documentul si se foloseste pentru trimiteri interne.

### Ce merita stiut inainte de a optimiza acest document

1. **Efortul.** Estimarea curenta este de 78-94 zile-om, dupa ce generarea automata a
   redus partea de constructie de la 138 la circa 41. La o disponibilitate de 1.5 zile pe
   saptamana inseamna 12-14 luni. Aceasta ipoteza este cea mai fragila din tot documentul.
2. **Calea critica nu mai este constructia**, ci obtinerea datelor de la Sales, Productie
   si Calitate. Vezi S26.
3. **Zece intrebari deschise** raman fara raspuns, in S20. Fiecare are o valoare implicita
   ca sa nu blocheze constructia, dar IQ-01 si IQ-10 schimba calendarul.
4. **S22 este un document de decizie**, nu de arhitectura: explica ce s-a preluat dintr-un
   al doilea blueprint mai ambitios, ce s-a respins si de ce, si rezolva cinci
   contradictii intre cele doua.

---


## Cuprinsul exportului

- **S00-sumar-executiv** &mdash; Sectiunea 0 - Sumar executiv
- **S01-harta-modulelor** &mdash; Sectiunea 1 - Harta modulelor
- **S02-model-date** &mdash; Sectiunea 2 - Modelul de date Dataverse
- **S03-relatii** &mdash; Sectiunea 3 - Diagrama relatiilor
- **S04-livrabile** &mdash; Sectiunea 4 - Livrabilele de proiect
- **S05-documentatie** &mdash; Sectiunea 5 - Structura documentatiei
- **S06-masuratori-senzorial** &mdash; Sectiunea 6 - Masuratori si evaluare senzoriala
- **S07-productie-0** &mdash; Sectiunea 7 - Productie 0
- **S08-revizuire-post-implementare** &mdash; Sectiunea 8 - Revizuirea post-implementare
- **S09-alergeni-nutritionale** &mdash; Sectiunea 9 - Alergeni si valori nutritionale
- **S10-ecrane** &mdash; Sectiunea 10 - Ecranele aplicatiilor
- **S11-securitate-roluri** &mdash; Sectiunea 11 - Securitate si roluri
- **S12-automatizari** &mdash; Sectiunea 12 - Automatizari
- **S13-indicatori** &mdash; Sectiunea 13 - Indicatori si raportare
- **S14-durate-etape** &mdash; Sectiunea 14 - Duratele etapelor
- **S15-migrare** &mdash; Sectiunea 15 - Migrarea
- **S16-roadmap** &mdash; Sectiunea 16 - Roadmap pe valuri
- **S17-trecere-productie** &mdash; Sectiunea 17 - Trecerea in productie
- **S18-riscuri** &mdash; Sectiunea 18 - Riscuri
- **S19-criterii-acceptanta** &mdash; Sectiunea 19 - Criterii de acceptanta
- **S20-intrebari-deschise** &mdash; Sectiunea 20 - Intrebari deschise
- **S21-prompturi-continuare** &mdash; Sectiunea 21 - Prompturi de continuare
- **S22-sinteza-enterprise** &mdash; Sectiunea 22 - Sinteza celor doua blueprinturi
- **S23-guvernanta-proiect** &mdash; Sectiunea 23 - Guvernanta de proiect
- **S24-stabilizare-capabilitate** &mdash; Sectiunea 24 - Stabilizare, capabilitate de proces si sanatatea proiectului
- **S25-cunoastere** &mdash; Sectiunea 25 - Cunoastere organizationala
- **S26-constructie-asistata** &mdash; Sectiunea 26 - Constructia asistata: ce se genereaza si ce nu
- **S27-unde-traieste-ce** &mdash; Sectiunea 27 - Unde traieste ce
- **S28-acces-si-licentiere** &mdash; Sectiunea 28 - Acces si licentiere
- **A1-prioritizare-si-termene** &mdash; Anexa A1 - Prioritizarea si calculul termenelor
- **A2-backlog-enterprise** &mdash; Anexa A2 - Backlog enterprise, cu criterii de activare

- **README** &mdash; Index si sinteza
- **V0-ghid-constructie** &mdash; Ghid de constructie, Valul 0
- **README** &mdash; Provizionarea modelului


<!-- ==================== S00-sumar-executiv.md ==================== -->

---

# Sectiunea 0 - Sumar executiv

0.1 Se inlocuieste centralizatorul Excel F-PS-LID-10.01 si evidenta pe foldere cu o
baza de date Dataverse in care proiectul CDI este radacina, iar cele ~30 de bife de azi
devin inregistrari de livrabil generate automat din sablon la acceptarea proiectului.

0.2 Datele stau in Dataverse, fisierele raman in SharePoint intr-un arbore pe faze
generat automat, legat de proiect prin integrarea nativa de documente.

0.3 Doua interfete: o aplicatie model-driven pentru birou (triaj, alocare, coada,
aprobari, rapoarte) si o aplicatie canvas pentru hala si laborator (masuratori la linie,
evaluare senzoriala, receptie mostra, checklist productie 0).

0.4 Prioritizarea devine un scor automat pe 100 de puncte, recalculat saptamanal, cu
buget de urgenta pe KAM si imbatranire in coada, suprascriabil doar cu motiv si urma
in audit.

0.5 Termenul are trei valori distincte - propus de sistem, negociat cu KAM, realizat -
iar blocajele externe opresc ceasul indicatorului R&D fara sa opreasca termenul catre
client.

0.6 Doua procese care azi nu exista se nasc din blueprint: inregistrarea structurata a
productiei 0 si revizuirea post-implementare declansata automat la 30, 60 si 90 de zile.

0.7 Alergenii si valorile nutritionale se calculeaza din reteta, cu recalculare automata
la orice schimbare de materie prima sau de versiune de reteta.

0.8 Trasabilitatea IFS / ISO / HACCP se obtine din audit nativ Dataverse plus versionare
SharePoint, astfel incat dosarul de produs sa fie reconstituibil la orice data din trecut.

0.9 Constructia se face intr-un mediu Developer, intr-o Solution unica exportata
periodic pe OneDrive, in patru valuri: Val 0 fundatie, Val 1 MVP la 30 de zile, Val 2 la
90 de zile, Val 3 la 6 luni.

0.10 Rezultatul masurabil la 6 luni: T-Total, Q-Corect si Q-Complet calculate automat pe
activitate, rol si persoana, cu tinte de 95-98%, si o coada de proiecte vizibila intregii
companii fara instruire.


<!-- ==================== S01-harta-modulelor.md ==================== -->

---

# Sectiunea 1 - Harta modulelor

## 1.1 Tabelul modulelor

Prioritate: 1 = fara el nu functioneaza nimic; 2 = necesar pentru operare completa;
3 = valoare adaugata dupa stabilizare.

| Cod | Modul | Proces acoperit | Rol principal | Tip aplicatie | Prioritate | Val |
|---|---|---|---|---|---|---|
| M01 | Fundatie si nomenclatoare | Mediu, Solution, prefix editor, linii, clienti, tipuri de documente, roluri | Head of R&D (constructor) | Model-driven (configurare) | 1 | Val 0 |
| M02 | Solicitare (SCP) | Deschiderea cererii de catre KAM, varianta de rezerva pe mail | KAM | Model-driven + formular canvas simplificat | 1 | Val 1 |
| M03 | Triaj si generare proiect | Acceptat / respins / amanat cu motiv, generare cod {AA}{NNN}, creare folder | Manager R&D | Model-driven | 1 | Val 1 |
| M04 | Proiect CDI si versiuni | Radacina proiectului, proiecte-copil cu sufix .1, mostenire referinte | Manager R&D, tehnolog | Model-driven | 1 | Val 1 |
| M05 | Livrabile de proiect | Generarea din sablon a celor 43 de livrabile, termen, responsabil, status | Tehnolog | Model-driven | 1 | Val 1 |
| M06 | Etape si durate | Sablon de etape, durata standard 2 saptamani, data estimata de finalizare | Manager R&D | Model-driven | 2 | Val 1 |
| M07 | Alocare si incarcare | Alocarea tehnologului, incarcarea pe tehnolog si pe linie, praguri vizuale | Manager R&D | Model-driven (dashboard) | 1 | Val 1 |
| M08 | Prioritizare | Scor 100 de puncte, benzi P1-P4, buget de urgenta, imbatranire, suprascriere | Manager operational / vanzari | Model-driven + flux programat | 2 | Val 2 |
| M09 | Materii prime si aprovizionare | Lista MP pe proiect, ciclul MP noua, iteratii de furnizor, lead time, ETA | Achizitii | Model-driven | 2 | Val 2 |
| M10 | Mostre | Cerere de mostra, miscari, receptie, evidenta livrarilor la client | Suport R&D | Canvas (receptie) + model-driven | 2 | Val 2 |
| M11 | Blocaje si oprirea ceasului | Cine blocheaza, din ce data, impact in zile, efect asupra T-Total | Manager R&D | Model-driven | 2 | Val 2 |
| M12 | Testare si masuratori | Fisa de testare, trial, masuratori la linie, statistica, conformitate | Tehnolog | Canvas mobil | 1 | Val 1 |
| M13 | Evaluare senzoriala | Grila ponderata 1-5, defecte, verdict, comparatie cu referinta | Tehnolog, panel | Canvas mobil | 2 | Val 2 |
| M14 | Reteta si antecalcul | Versiuni de reteta, linii de reteta, antecalcul si linii de antecalcul | Tehnolog | Model-driven | 2 | Val 2 |
| M15 | Alergeni si nutritionale | Calcul din reteta, urme si contaminare incrucisata, recalculare automata | Tehnolog, Calitate | Model-driven (rollup + flux) | 3 | Val 3 |
| M16 | Specificatii si SDP | ST draft / final / intern MP, SDP ca suport pentru IL | Tehnolog, Calitate | Model-driven | 2 | Val 2 |
| M17 | Etichete | Eticheta punga, bax, EPC, fisier de imprimanta Colos / Zebra | Suport R&D | Model-driven | 3 | Val 3 |
| M18 | Implementare (IPN) | Conditii IPN, plan IPN, IL productie, plan HACCP | Tehnolog, Calitate, Productie | Model-driven | 2 | Val 2 |
| M19 | Productie 0 | Checklist la linie, randament, rebut, parametri reali, decizie finala | Tehnolog, Productie | Canvas mobil | 2 | Val 2 |
| M20 | Revizuire post-implementare | Declansare automata la 30 / 60 / 90 de zile, decizie de mentinere | Manager R&D, KAM | Model-driven + flux programat | 3 | Val 3 |
| M21 | Documente si sabloane | Arbore de foldere, denumire, metadate, versionare, generare din Word | Suport R&D | SharePoint + Power Automate | 1 | Val 1 |
| M22 | Indicatori si raportare | T-Total, Q-Corect, Q-Complet, rapoarte operationale si anuale | Head of R&D | Power BI + vizualizari native | 3 | Val 3 |
| M23 | Ecran public de status | Status vizibil intregii companii, read-only, fara instruire | Toata compania | Model-driven dashboard partajat | 2 | Val 2 |
| M24 | Securitate si roluri | Matrice Rol x Tabela, roluri externe R&D, rol de cititor global | Head of R&D | Configurare | 1 | Val 0 |
| M25 | Migrare | Import din centralizator si din foldere, curatare, proiecte in curs | Head of R&D | Dataflow / import Excel | 2 | Val 1 |
| M26 | Gate-uri | Stage-gate cu criterii, decizii GO / conditii / HOLD / REWORK / STOP | Manager R&D | Model-driven | 1 | Val 1 |
| M27 | Actiuni centralizate | O singura coada de actiuni, din toate sursele | Toti | Model-driven | 1 | Val 1 |
| M28 | Riscuri si probleme | Registru de riscuri cu RPN, registru de probleme cu cauza radacina | Manager R&D, tehnolog | Model-driven | 2 | Val 2 |
| M29 | Jurnal de decizii | Context, alternative, motiv, ipoteze, reevaluare | Manager R&D | Model-driven | 3 | Val 2 |
| M30 | Stabilizare | Trei loturi consecutive conforme inainte de release | Tehnolog, Productie | Model-driven + canvas | 2 | Val 3 |
| M31 | Capabilitate de proces | Cp si Cpk pe gramaj si parametri critici | Tehnolog, Calitate | Model-driven | 3 | Val 3 |
| M32 | Lectii invatate | Generare de drafturi, aprobare, recomandare, urmarirea reutilizarii | Toti | Model-driven | 3 | Val 3 |
| M33 | Sanatatea proiectului | Snapshot saptamanal, tendinta, alerta de degradare | Manager R&D | Dashboard | 3 | Val 3 |
| M34 | Validare si feedback de client | Validari, feedback pe mostra si lansare | KAM | Model-driven | 3 | Val 4 |
| M35 | Reclamatii | Legate de produs, lot si proiect | Calitate | Model-driven | 3 | Val 4 |
| M36 | Neconformitati si CAPA | Cu evaluarea eficacitatii la 30 de zile | Calitate | Model-driven | 3 | Val 4 |
| M37 | Performanta furnizorilor | Scorecard, incidente, OTIF, acuratetea ETA | Achizitii | Model-driven | 3 | Val 4 |
| M38 | Business case si buget | Buget pe proiect, urmarirea consumului | Head of R&D | Model-driven | 3 | Val 5 |
| M39 | Cost real de productie | Cost real, giveaway, comparatie cu antecalculul | Head of R&D | Power BI | 3 | Val 5 |
| M40 | Realizarea beneficiilor | La 3, 6, 12 si 24 de luni | Head of R&D | Model-driven | 3 | Val 5 |
| M41 | Registru de documente tehnice | Ciclu de viata si harta de dependente | Suport R&D | Model-driven | 3 | Val 5 |

## 1.2 Dependente intre module

| Modul | Depinde de | Motiv |
|---|---|---|
| M03 | M01, M02 | Codul de proiect are nevoie de an si de nomenclatorul de tipuri |
| M05 | M04, M06 | Livrabilul se ataseaza proiectului si isi ia termenul din etapa |
| M07 | M04, M06 | Incarcarea se calculeaza din proiectele active si din etape |
| M08 | M04, M07, M09 | Scorul foloseste volum, client, efort si riscul de MP noua |
| M11 | M04, M06 | Blocajul opreste ceasul pe etapa curenta |
| M12 | M04, M14 | Trialul se face pe o versiune de reteta |
| M15 | M14, M09 | Alergenii se calculeaza din linii de reteta si date de MP |
| M18 | M16 | Planul IPN presupune ST finala aprobata |
| M19 | M18 | Productia 0 se face pe conditiile IPN aprobate |
| M20 | M19 | Revizuirea compara seria cu productia 0 |
| M22 | M06, M11 | T-Total are nevoie de etape si de blocaje pentru oprirea ceasului |
| M26 | M04, M05, M06 | Gate-ul verifica livrabilele si se aseaza la iesirea dintr-o etapa |
| M28 | M04, M27 | Riscul si problema genereaza actiuni in tabela centrala |
| M30 | M19 | Stabilizarea porneste de la productia 0 validata |
| M31 | M30, M12 | Capabilitatea are nevoie de minimum 30 de masuratori pe 3 loturi |
| M32 | M28, M19 | Drafturile de lectii se genereaza din probleme si din productia 0 |
| M33 | M28, M05, M09 | Scorul de sanatate agrega riscuri, livrabile si aprovizionare |

## 1.3 Ce nu face aceasta solutie

1.3.1 Nu inlocuieste SAP si nu scrie in SAP. Codurile de material se creeaza in SAP de
catre rolurile actuale si se inregistreaza in Dataverse ca text, cu data si autorul
inregistrarii.

1.3.2 Nu inlocuieste aplicatia interna de planificare a productiei. Coada pe linie din
R&D este o estimare negociabila; planificarea reala ramane in aplicatia existenta.
Legatura se face prin codul liniei si prin slotul de testare propus.

1.3.3 Nu defineste formatul intern al ST. Blueprintul defineste doar inregistrarea,
statusul, versiunea si legatura documentului ST cu proiectul.

1.3.4 Nu contine cod si nu contine formule Power Fx, cu exceptia regulilor de calcul
care nu pot fi exprimate altfel (scor de prioritate, statistica de masuratori, alergeni,
RPN, Cp si Cpk, scor de sanatate).

1.3.5 Nu construieste modulele din Anexa A2 pana cand criteriile lor de activare nu sunt
indeplinite. Modulele M26-M41 provin din sinteza cu blueprintul Enterprise (Sectiunea 22);
tot ce nu apare in tabelul de mai sus a fost amanat sau respins explicit, cu motiv.


<!-- ==================== S02-model-date.md ==================== -->

---

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
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascada la stergere |
| Tip referinta | rd_tipreferinta | Choice | Da | Produs concurenta / Produs actual / Mostra client / Specificatie client / Inexistenta | - | Choice global TIPREFERINTA |
| Client asociat | rd_client | Lookup (rd_client) | Nu | - | - | - |
| Producator | rd_producator | Text (150) | Nu | - | Pentru produs concurenta | - |
| Cod produs actual | rd_codprodusactual | Text (20) | Nu | - | Cod SAP daca este produs propriu | - |
| Gramaj (g) | rd_gramaj | Decimal (2) | Nu | - | Gramajul nominal, de pe eticheta | - |
| Gramaj masurat real (g) | rd_gramajmasurat | Decimal (2) | Nu | - | Minimum 5 bucati la produs concurenta | Vezi 6.4.4 |
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
| TBL-20a | Defect (nomenclator) | rd_defect | Nomenclator | 2 |
| TBL-20b | Defect constatat | rd_defectconstatat | Copil | 2 |
| TBL-21 | Referinta de comparatie | rd_referinta | Copil | 1 |
| TBL-22 | Antecalcul | rd_antecalcul | Copil | 2 |
| TBL-23 | Linie de antecalcul | rd_linieantecalcul | Copil | 2 |
| TBL-24 | Reteta | rd_reteta | Copil | 2 |
| TBL-25 | Versiune de reteta | rd_versiunereteta | Copil | 2 |
| TBL-26 | Linie de reteta | rd_liniereteta | Copil | 2 |
| TBL-27 | Alergen | rd_alergen | Nomenclator | 3 |
| TBL-28 | (valorile nutritionale sunt coloane pe TBL-25, nu tabela separata - vezi 2.15) | - | - | - |
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


<!-- ==================== S03-relatii.md ==================== -->

---

# Sectiunea 3 - Diagrama relatiilor

## 3.1 Conventii

3.1.1 Relatie **parentala**: copilul nu are sens fara parinte. Comportament la stergere
`Cascade All` sau `Parental`; drepturile de securitate se mostenesc de la parinte, deci
cine vede proiectul vede si copiii.

3.1.2 Relatie **referentiala**: cele doua inregistrari exista independent. Comportament
`Restrict Delete` pentru nomenclatoare (nu se sterge o linie de productie folosita in
proiecte) sau `Remove Link` acolo unde legatura este informativa.

3.1.3 NOTA de platforma: relatia parentala transmite si atribuirea (Assign) si partajarea
(Share). Din acest motiv, `rd_proiect` -> `rd_livrabil` este parentala (livrabilul urmeaza
proiectul cand acesta se reatribuie altui tehnolog), dar `rd_proiect` ->
`rd_proiectparinte` este referentiala (proiectul-copil are propriul responsabil si nu
trebuie sa isi schimbe proprietarul odata cu parintele).

3.1.4 Cascade Delete se foloseste doar unde stergerea are sens de business. In rest,
stergerea este interzisa prin rol de securitate: inregistrarile se dezactiveaza, nu se
sterg. Pentru un mediu certificat IFS, stergerea fizica a unei inregistrari de proiect
este un risc de audit, nu o facilitate.

## 3.2 Arborele principal

```
rd_solicitare (SCP)
  |
  +-- 1:N referential --> rd_proiect                      [Remove Link]
                            |
  rd_proiect (RADACINA)     |
  |                         |
  +-- 1:N PARENTAL --> rd_livrabil                        [Cascade All]
  +-- 1:N PARENTAL --> rd_etapa                           [Cascade All]
  +-- 1:N PARENTAL --> rd_mpproiect                       [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_iteratiefurnizor   [Cascade All]
  +-- 1:N PARENTAL --> rd_blocaj                          [Cascade All]
  +-- 1:N PARENTAL --> rd_ceremostra                      [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_miscaremostra      [Cascade All]
  +-- 1:N PARENTAL --> rd_fisatestare                     [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_trial             [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_masuratoare      [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_statisticatrial  [Cascade All]
  +-- 1:N PARENTAL --> rd_evaluaresenzoriala              [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_scorsenzorial      [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_defectconstatat    [Cascade All]
  +-- 1:N PARENTAL --> rd_referinta                       [Cascade All]
  +-- 1:N PARENTAL --> rd_reteta                          [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_versiunereteta     [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_liniereteta      [Cascade All]
  +-- 1:N PARENTAL --> rd_antecalcul                      [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_linieantecalcul    [Cascade All]
  +-- 1:N PARENTAL --> rd_specificatie                    [Cascade All]
  +-- 1:N PARENTAL --> rd_sdp                             [Cascade All]
  +-- 1:N PARENTAL --> rd_eticheta                        [Cascade All]
  +-- 1:N PARENTAL --> rd_implementare                    [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_productie0         [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_inregistrareprod0 [Cascade All]
  +-- 1:N PARENTAL --> rd_revizuire                       [Cascade All]
  +-- 1:N REFERENTIAL (auto) --> rd_proiect (copil .1)    [Remove Link]
```

## 3.3 Relatiile catre nomenclatoare (toate referentiale)

| Cod | Parinte | Copil | Coloana lookup | Comportament la stergere | Tip |
|---|---|---|---|---|---|
| REL-01 | rd_client | rd_solicitare | rd_client | Restrict | Referential |
| REL-02 | rd_client | rd_proiect | rd_client | Restrict | Referential |
| REL-03 | rd_client | rd_referinta | rd_client | Remove Link | Referential |
| REL-04 | rd_linie | rd_proiect | rd_linie | Restrict | Referential |
| REL-05 | rd_linie | rd_trial | rd_linie | Restrict | Referential |
| REL-06 | rd_linie | rd_fisatestare | rd_linie | Remove Link | Referential |
| REL-07 | rd_linie | rd_antecalcul | rd_linie | Restrict | Referential |
| REL-08 | rd_linie | rd_implementare | rd_linie | Restrict | Referential |
| REL-09 | rd_linie | rd_productie0 | rd_linie | Restrict | Referential |
| REL-10 | rd_materieprima | rd_mpproiect | rd_materieprima | Restrict | Referential |
| REL-11 | rd_materieprima | rd_liniereteta | rd_materieprima | Restrict | Referential |
| REL-12 | rd_materieprima | rd_linieantecalcul | rd_materieprima | Restrict | Referential |
| REL-13 | rd_materieprima | rd_specificatie | rd_materieprima | Remove Link | Referential |
| REL-14 | rd_furnizor | rd_materieprima | rd_furnizor | Remove Link | Referential |
| REL-15 | rd_furnizor | rd_mpproiect | rd_furnizor | Remove Link | Referential |
| REL-16 | rd_furnizor | rd_iteratiefurnizor | rd_furnizor | Restrict | Referential |
| REL-17 | rd_motiv | rd_solicitare | rd_motivtriaj | Restrict | Referential |
| REL-18 | rd_motiv | rd_proiect | rd_motivstatus | Restrict | Referential |
| REL-19 | rd_motiv | rd_iteratiefurnizor | rd_motivrespingere | Restrict | Referential |
| REL-20 | rd_criteriusenzorial | rd_scorsenzorial | rd_criteriu | Restrict | Referential |
| REL-21 | rd_defect | rd_defectconstatat | rd_defect | Restrict | Referential |
| REL-22 | rd_sablonlivrabil | rd_livrabil | rd_sablon | Remove Link | Referential |
| REL-23 | rd_sablonetapa | rd_etapa | rd_sablon | Remove Link | Referential |
| REL-24 | rd_sablonetapa | rd_sablonlivrabil | rd_etapa | Remove Link | Referential |
| REL-25 | rd_indicator | rd_masurareindicator | rd_indicator | Cascade All | Parental |

## 3.4 Relatiile transversale (referentiale, in interiorul proiectului)

Aceste relatii leaga copii ai aceluiasi proiect intre ei. Toate sunt referentiale cu
`Remove Link`, ca stergerea unui trial sa nu distruga evaluarea senzoriala facuta pe el.

| Cod | De la | La | Coloana | Motiv |
|---|---|---|---|---|
| REL-30 | rd_fisatestare | rd_versiunereteta | rd_versiunereteta | Ce reteta se testeaza |
| REL-31 | rd_evaluaresenzoriala | rd_trial | rd_trial | Ce s-a degustat |
| REL-32 | rd_evaluaresenzoriala | rd_referinta | rd_referinta | Comparatia |
| REL-33 | rd_antecalcul | rd_versiunereteta | rd_versiunereteta | Pe ce reteta s-a calculat |
| REL-34 | rd_linieantecalcul | rd_mpproiect | rd_mpproiect | MP fara cod SAP inca |
| REL-35 | rd_liniereteta | rd_mpproiect | rd_mpproiect | Idem |
| REL-36 | rd_sdp | rd_versiunereteta | rd_versiunereteta | Ce reteta se implementeaza |
| REL-37 | rd_blocaj | rd_etapa | rd_etapa | Pe ce etapa se opreste ceasul |
| REL-38 | rd_ceremostra | rd_mpproiect | rd_mpproiect | Mostra pentru ce MP |
| REL-39 | rd_productie0 | rd_implementare | rd_implementare | Pe ce IPN |
| REL-40 | rd_specificatie | rd_specificatie | rd_inlocuieste | Lantul de versiuni |
| REL-41 | rd_reteta | rd_versiunereteta | rd_versiunecurenta | Care versiune este in vigoare |
| REL-42 | rd_proiect | rd_referinta | rd_referinta | Referinta activa a proiectului |
| REL-43 | rd_trial | rd_proiect | rd_proiect | Denormalizare pentru raportare |

3.4.1 REL-41 si REL-42 sunt referinte "inapoi", de la parinte la un copil anume. Sunt
necesare pentru ca formularul de proiect trebuie sa arate versiunea curenta si referinta
activa fara sa parcurga o subgrila. Se scriu de flux, nu manual.

3.4.2 REL-43 duplica informatia disponibila prin fisa de testare. Este acceptata
constient: raportarea pe trialuri la nivel de departament ar cere altfel un join pe doua
niveluri, ceea ce in vizualizarile native Dataverse nu se poate.

## 3.5 Relatiile catre systemuser

Toate lookup-urile catre `systemuser` sunt referentiale cu `Remove Link`. Nu se sterge
niciodata un utilizator din Dataverse; se dezactiveaza. Coloanele afectate:
`rd_kam`, `rd_tehnolog`, `rd_manager`, `rd_responsabil`, `rd_aprobator`, `rd_autor`,
`rd_evaluator`, `rd_masuratde`, `rd_solicitant`, `rd_persoana`, `rd_preluatde`,
`rd_aprobatorcalitate`.

3.5.1 Proprietarul inregistrarii (`ownerid`) este intotdeauna tehnologul alocat pentru
proiect si copiii lui, ca sa functioneze securitatea la nivel de User / Business Unit
descrisa in Sectiunea 11. Reatribuirea proiectului reatribuie toti copiii, prin
comportamentul parental Cascade All pe Assign.

## 3.6 Relatia cu SharePoint

3.6.1 Legatura documentelor se face prin integrarea nativa Dataverse - SharePoint, care
creeaza automat, pentru tabela `rd_proiect`, o relatie catre entitatea de sistem
`SharePointDocumentLocation`. Nu se construieste o tabela proprie de documente.

3.6.2 Locatia se personalizeaza in FLX-02 astfel incat folderul sa nu fie generat de
platforma in formatul implicit `{nume}_{guid}`, ci in formatul cerut la 5.1:
`/PRODUSE IN DEZVOLTARE/{an}/{cod}_{nume produs}/`.

3.6.3 NOTA: integrarea nativa creeaza implicit un singur folder per inregistrare, fara
subfoldere. Arborele pe faze din 5.1 se creeaza cu FLX-02 (actiune SharePoint "Creeaza
folder"), iar `SharePointDocumentLocation` se seteaza catre folderul radacina al
proiectului. Subfolderele sunt vizibile in controlul de documente din formular.

## 3.7 Diagrama compacta a fluxului de date

```
SCP --triaj--> PROIECT --sablon--> LIVRABILE + ETAPE
                 |
                 +--> MP PROIECT --> ITERATII FURNIZOR --> (ETA) --> recalcul termen
                 |
                 +--> RETETA --> VERSIUNE --> LINII --> ALERGENI + NUTRITIONALE
                 |                    |
                 |                    +--> ANTECALCUL --> MARJA
                 |                    |
                 |                    +--> FISA TESTARE --> TRIAL --> MASURATORI --> STATISTICA
                 |                                            |
                 |                                            +--> EVALUARE SENZORIALA --> VERDICT
                 |
                 +--> SPECIFICATIE (ST) --> SDP --> ETICHETA
                 |                            |
                 |                            +--> IMPLEMENTARE (IPN) --> PRODUCTIE 0
                 |                                                            |
                 |                                                            +--> REVIZUIRE 30/60/90
                 |
                 +--> BLOCAJE --> oprirea ceasului --> T-TOTAL
```


<!-- ==================== S04-livrabile.md ==================== -->

---

# Sectiunea 4 - Livrabilele de proiect

## 4.1 Principiul

4.1.1 Cele ~30 de coloane din centralizatorul F-PS-LID-10.01 nu devin coloane. Devin
inregistrari in `rd_livrabil` (TBL-03), generate automat din `rd_sablonlivrabil`
(TBL-04) la acceptarea proiectului, prin FLX-05.

4.1.2 Motivul, in trei randuri: o coloana-bifa spune doar "exista sau nu", in timp ce o
inregistrare de livrabil spune cine il datoreaza, pana cand, in ce stadiu, cu ce document
si de ce nu se aplica. Numai a doua forma permite alertele, indicatorul Q-Complet si
raportul "livrabilele care intarzie cel mai des".

4.1.3 Fiecare livrabil are: denumire, cod stabil, faza, responsabil (rol si persoana),
termen, data realizarii, status, document atasat, obligatoriu sau optional, conditie de
aplicabilitate.

## 4.2 Conditiile de aplicabilitate

| Cod conditie | Se evalueaza pe | Livrabilul apare cand |
|---|---|---|
| C0 Intotdeauna | - | Mereu |
| C1 Doar MP noua | rd_proiect.rd_aremp | Proiectul are cel putin o materie prima noua |
| C2 Doar eticheta noua | rd_proiect.rd_tipproiect + cerinte client | Produsul primeste eticheta proprie (nu marca proprie a clientului cu eticheta lui) |
| C3 Doar client nou | rd_client.rd_proiecteactive = 0 la deschidere | Primul proiect cu acest client |
| C4 Doar ambalaj nou | Camp pe proiect `rd_ambalajnou` | Se schimba materialul sau formatul de ambalaj |
| C5 Doar linie nesetata | rd_linie.rd_capabilitati vs. cerinta produsului | Produsul cere o capabilitate pe care linia nu o are inca setata |
| C6 Doar export | rd_client.rd_tara != Romania | Cerinte suplimentare de eticheta si documentatie |
| C7 Doar produs nou | rd_tipproiect = Produs nou | Nu se aplica la reformulari sau abateri |

4.2.1 Conditiile se reevalueaza si dupa generare. Daca la doua saptamani de la acceptare
tehnologul marcheaza o materie prima ca noua, FLX-05 adauga livrabilele C1 lipsa, cu
termen recalculat, si notifica responsabilul. Livrabilele nu se sterg niciodata la
reevaluare: daca o conditie devine falsa, livrabilul trece in status `Nu se aplica`, cu
urma in audit.

## 4.3 Ce inseamna "obligatoriu"

4.3.1 Un livrabil marcat obligatoriu si aplicabil trebuie sa fie in status `Realizat`
pentru ca proiectul sa poata trece in `Finalizat`. Business rule pe `rd_proiect`
blocheaza tranzitia si afiseaza lista celor lipsa.

4.3.2 Minimul cerut explicit de blueprint - antecalcul, ST draft, ST finala, plan IPN,
dosarul de mostra, TDV validat - este acoperit de LIV-11, LIV-16, LIV-21, LIV-26,
LIV-09 si LIV-34.

4.3.3 Un livrabil obligatoriu poate fi marcat `Nu se aplica` numai de Managerul R&D, cu
motiv din nomenclator si comentariu. Aceasta este singura poarta de iesire si este
auditata.

## 4.4 Sablonul complet de livrabile

Legenda: Ob. = obligatoriu; Doc = necesita document atasat; Cond. = conditie de
aplicabilitate; Offset = zile de la data acceptarii, pe durata standard de 14 zile
lucratoare (vezi Sectiunea 14).

### Faza 00 - Solicitare

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent in centralizator |
|---|---|---|---|---|---|---|---|---|
| LIV-01 | SCP completat si trimis | KAM | Manager R&D | Da | Da | C0 | 0 | (nou, azi este mail) |
| LIV-02 | Eticheta produs client (EPC) primita | KAM | - | Nu | Da | C2 | 2 | (nou) |
| LIV-03 | Referinta de comparatie inregistrata | KAM | Tehnolog | Da | Nu | C0 | 1 | (nou) |
| LIV-04 | Cerinte de eticheta si ambalaj de la client | KAM | - | Nu | Da | C0 | 2 | (nou) |
| LIV-05 | Decizie de triaj cu motiv | Manager R&D | - | Da | Nu | C0 | 1 | (nou) |

### Faza 01 - Plan

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-06 | Plan de dezvoltare produs | Tehnolog | Manager R&D | Da | Da | C0 | 2 | PLAN DEZVOLTARE PRODUS |
| LIV-07 | Cerere achizitii mostra MP noua | Tehnolog | Achizitii | Da | Da | C1 | 3 | CERERE ACHIZITII MOSTRA MP NOUA |
| LIV-08 | Lista materiilor prime cu marcarea celor noi | Tehnolog | - | Da | Nu | C0 | 3 | (implicit azi) |
| LIV-09 | Slot de testare propus si negociat | Manager R&D | Planificare | Nu | Nu | C0 | 3 | (nou) |

### Faza 02 - Testare

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-10 | Fisa de test | Tehnolog | Manager R&D | Da | Da | C0 | 5 | FISA DE TEST |
| LIV-11 | Testare realizata (cel putin un trial reusit) | Tehnolog | - | Da | Nu | C0 | 8 | TESTARE REALIZATA |
| LIV-12 | Raport de testare cu masuratori si statistica | Tehnolog | Manager R&D | Da | Da | C0 | 9 | (partial: formularele Excel de masuratori) |
| LIV-13 | Evaluare produs (fisa de evaluare senzoriala) | Tehnolog | Manager R&D | Da | Da | C0 | 9 | EVALUARE PRODUS |
| LIV-14 | Test comparativ fata de referinta | Tehnolog | - | Nu | Nu | C0 | 9 | (nou) |

### Faza 03 - Mostre

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-15 | Mostre de produs pregatite si livrate | Suport R&D | - | Da | Nu | C0 | 10 | MOSTRE |
| LIV-16 | Dosar de mostra (fisa, poze, dovada livrarii) | Suport R&D | Tehnolog | Da | Da | C0 | 10 | (nou, cerut explicit ca obligatoriu) |
| LIV-17 | Feedback client la mostra | KAM | - | Da | Da | C0 | 12 | (nou) |

### Faza 04 - Antecalcul

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-18 | Antecalcul | Tehnolog | Manager R&D | Da | Da | C0 | 7 | ANTECALCUL |
| LIV-19 | Confirmare de pret de la client | KAM | - | Nu | Da | C0 | 12 | (nou) |

### Faza 05 - Specificatii

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-20 | Conditii ST | Tehnolog | Calitate | Da | Da | C0 | 6 | CONDITII ST |
| LIV-21 | ST draft | Tehnolog | Calitate | Da | Da | C0 | 10 | ST DRAFT |
| LIV-22 | ST interna pentru MP noua | Calitate | Calitate | Da | Da | C1 | 8 | ST INTERN MP NOUA |
| LIV-23 | Material SAP creat pentru MP noua | Achizitii | - | Da | Nu | C1 | 9 | MATERIAL SAP |
| LIV-24 | ST finala | Tehnolog | Calitate | Da | Da | C0 | 13 | ST FINAL |
| LIV-25 | SDP - specificatie de produs | Tehnolog | Calitate | Da | Da | C0 | 14 | SDP |
| LIV-26 | Material SAP creat pentru produsul finit | Tehnolog | Manager R&D | Da | Nu | C0 | 13 | MATERIAL SAP |
| LIV-27 | Alergeni si valori nutritionale calculate | Tehnolog | Calitate | Da | Nu | C0 | 12 | (nou) |

### Faza 06 - Eticheta

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-28 | Eticheta realizata (punga si bax) | Suport R&D | Calitate | Da | Da | C2 | 14 | ETICHETA REALIZATA |
| LIV-29 | Fisier de imprimanta Colos / Zebra | Suport R&D | - | Nu | Da | C2 | 15 | (implicit azi) |
| LIV-30 | Eticheta implementata pe linie | Productie | Tehnolog | Da | Nu | C2 | 18 | ETICHETA IMPLEMENTATA |

### Faza 07 - Implementare

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-31 | Conditii IPN | Tehnolog | Manager R&D | Da | Da | C0 | 15 | CONDITII IPN |
| LIV-32 | Plan IPN | Tehnolog | Manager R&D | Da | Da | C0 | 15 | PLAN IPN |
| LIV-33 | IL productie creata | Tehnolog | Productie | Da | Da | C0 | 16 | CREAZA IL PROD |
| LIV-34 | Plan HACCP actualizat si aprobat | Calitate | Calitate | Da | Da | C0 | 16 | PLAN HACCP |
| LIV-35 | Instruire operatori efectuata | Productie | Tehnolog | Da | Da | C0 | 17 | (nou, cerinta IFS) |
| LIV-36 | Productie 0 realizata si inregistrata | Tehnolog | Manager R&D | Da | Da | C0 | 18 | PROD 0 |
| LIV-37 | Raport de productie 0 cu decizie | Tehnolog | Manager R&D si Calitate | Da | Da | C0 | 19 | (nou, vezi Sectiunea 7) |

### Faza 08 - Dosar validat

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-38 | Dosar validat complet | Suport R&D | Manager R&D | Da | Da | C0 | 20 | DOSAR VALIDAT |
| LIV-39 | TDV validat, semnat R&D si Calitate | Manager R&D | Calitate | Da | Da | C0 | 20 | TDV VALIDAT |
| LIV-40 | Predare catre productie si comercial | Manager R&D | - | Da | Nu | C0 | 20 | (nou) |

### Faza 09 - Post-implementare (nu blocheaza inchiderea)

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-41 | Revizuire la 30 de zile | Manager R&D | - | Nu | Da | C0 | +30 | (nou, Sectiunea 8) |
| LIV-42 | Revizuire la 60 de zile | Manager R&D | - | Nu | Da | C0 | +60 | (nou) |
| LIV-43 | Revizuire la 90 de zile cu decizie finala | Manager R&D | Head of R&D | Da | Da | C0 | +90 | (nou) |

## 4.5 Acoperirea coloanelor din centralizatorul actual

| Coloana actuala | Livrabil nou | Observatie |
|---|---|---|
| PLAN DEZVOLTARE PRODUS | LIV-06 | Devine document generat din date, vezi 5.5.2 |
| CERERE ACHIZITII MOSTRA MP NOUA | LIV-07 | Conditionat C1 |
| FISA DE TEST | LIV-10 | Devine inregistrare TBL-14, nu fisier |
| ANTECALCUL | LIV-18 | Devine TBL-22 cu linii |
| TESTARE REALIZATA | LIV-11 | Se bifeaza automat la primul trial cu rezultat Reusit |
| EVALUARE PRODUS | LIV-13 | Devine TBL-17 cu grila din 6.5 |
| DOSAR VALIDAT | LIV-38 | - |
| ST DRAFT | LIV-21 | - |
| MOSTRE | LIV-15 | Plus dosarul de mostra LIV-16 |
| CONDITII ST | LIV-20 | - |
| ETICHETA REALIZATA | LIV-28 | Conditionat C2 |
| ST INTERN MP NOUA | LIV-22 | Conditionat C1 |
| MATERIAL SAP | LIV-23 si LIV-26 | Se separa MP de produs finit; azi sunt confundate |
| ST FINAL | LIV-24 | - |
| CONDITII IPN | LIV-31 | - |
| PLAN IPN | LIV-32 | - |
| ETICHETA IMPLEMENTATA | LIV-30 | Conditionat C2 |
| CREAZA IL PROD | LIV-33 | - |
| PLAN HACCP | LIV-34 | - |
| PROD 0 | LIV-36 | Plus raportul LIV-37 |
| SDP | LIV-25 | - |
| TDV VALIDAT | LIV-39 | - |

4.5.1 Sase coloane devin doua livrabile fiecare, pentru ca astazi acopera doua obligatii
diferite sub o singura bifa (MATERIAL SAP, MOSTRE, PROD 0). Aceasta este principala
sursa de "bifat, dar incomplet" din evidenta actuala.

4.5.2 Livrabile complet noi, adaugate ca expert: LIV-01 - LIV-05 (faza de solicitare, azi
inexistenta ca evidenta), LIV-12, LIV-14, LIV-17, LIV-19, LIV-27, LIV-35, LIV-37, LIV-40,
LIV-41 - LIV-43. Motiv: fara ele nu se poate calcula Q-Complet si nu se poate demonstra
la audit lantul cerinta - testare - validare.

## 4.6 Generarea si termenele

4.6.1 FLX-05 genereaza livrabilele la trecerea proiectului in `Acceptat - planificat`,
filtrand sablonul dupa `rd_tipproiect` si evaluand conditiile din 4.2.

4.6.2 Termenul fiecarui livrabil = data acceptarii + offset in zile lucratoare, ajustat
proportional daca durata standard a proiectului difera de 14 zile:
`termen = data_acceptare + ROUND(offset * durata_proiect / 14)` zile lucratoare.

4.6.3 Livrabilele post-implementare (LIV-41 - LIV-43) se genereaza separat, de FLX-15, la
completarea `rd_implementare.rd_dataimplementare`, cu offset fata de acea data.

4.6.4 Reatribuirea proiectului catre alt tehnolog reatribuie toate livrabilele cu rol
responsabil `Tehnolog` care nu sunt inca in status `Realizat`. Cele realizate isi pastreaza
responsabilul istoric, ca sa nu se rescrie trecutul.

## 4.7 Sabloane pe tip de proiect

| Tip proiect | Livrabile excluse din sablon | Motiv |
|---|---|---|
| Produs nou | - | Sablonul complet |
| Reformulare | LIV-03, LIV-26 | Referinta este produsul actual; codul SAP exista deja |
| Abatere (.1) | LIV-06, LIV-18, LIV-26, LIV-38 | Mosteneste de la parinte, se refac doar testarea si specificatia |
| Transfer pe alta linie | LIV-18, LIV-20, LIV-21, LIV-24, LIV-28 | Reteta si eticheta raman; se reface doar implementarea |
| Optimizare cost | LIV-02, LIV-03, LIV-28, LIV-30 | Eticheta nu se schimba daca lista de ingrediente ramane identica |
| Ambalaj nou | LIV-08, LIV-10 - LIV-14, LIV-27 | Produsul nu se schimba; se reface eticheta si IPN-ul |

4.7.1 NOTA: exceptia de la 4.7 este alergenul. Orice optimizare de cost care schimba o
materie prima reactiveaza LIV-27 si LIV-28, chiar daca sablonul le excludea, pentru ca
declaratia de pe eticheta trebuie sa ramana corecta. Regula se implementeaza in FLX-13, nu
in sablon.


<!-- ==================== S05-documentatie.md ==================== -->

---

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


<!-- ==================== S06-masuratori-senzorial.md ==================== -->

---

# Sectiunea 6 - Masuratori si evaluare senzoriala

## 6.1 Masuratorile obligatorii

6.1.1 La fiecare trial se inregistreaza obligatoriu: greutate, dimensiuni, aspect,
alveolare, miros, gust. Primele doua sunt numerice, ultimele patru sunt calitative pe
scala Conform / Minor neconform / Neconform, plus scorul senzorial detaliat din 6.5.

6.1.2 Se masoara intre 2 si 5 bucati, sau mai multe pentru gramaj si dimensiuni. Numarul
minim pe tip de verificare este in 6.2.1.

6.1.3 Sistemul calculeaza automat, la fiecare salvare de masuratoare, in tabela
`rd_statisticatrial` (TBL-16b): media, abaterea standard de esantion, coeficientul de
variatie, minimul, maximul, numarul de neconforme si conformitatea fata de toleranta
declarata in fisa de testare.

6.1.4 Formulele, exprimate ca reguli de calcul pentru ca nu pot fi exprimate altfel:

```
medie          = SUMA(valori neexcluse) / n
abatere std    = RADICAL( SUMA((valoare - medie)^2) / (n - 1) )      [esantion, n-1]
CV %           = abatere std / medie * 100
conform bucata = valoare >= (tinta - tol_minus) SI valoare <= (tinta + tol_plus)
conformitate % = numar conforme / n * 100
```

6.1.5 Se foloseste abaterea standard de esantion (n-1), nu de populatie. La 3-5 bucati
diferenta este semnificativa, iar estimarea cu n-1 este cea corecta pentru un esantion
extras dintr-o productie.

## 6.2 Dimensiunea esantionului si valorile aberante

### 6.2.1 PROPUNERE: dimensiunea minima de esantion pe tip de verificare

| Tip de verificare | Esantion minim la trial | Esantion minim la productie 0 | Motiv |
|---|---|---|---|
| Greutate bucata | 10 | 20, in 4 prelevari de cate 5 | Gramajul este cerinta legala si contractuala; la n=5 abaterea standard este prea instabila pentru a decide conformitatea |
| Greutate ambalaj / bax | 3 | 5 | Variabilitate mult mai mica, se cumuleaza erorile individuale |
| Lungime, latime, inaltime | 5 | 10 | Dimensiunea deriva din setarea liniei, nu din variatia bucatii |
| Diametru, grosime | 5 | 10 | Idem |
| Volum sau inaltime dupa coacere | 5 | 10 | Indicator de dospire, foarte sensibil |
| Aspect exterior | 10 (vizual, bucata cu bucata) | 20 | Defectele de aspect apar rar; la n mic nu se detecteaza |
| Alveolare (sectiune) | 3 | 5 | Necesita taierea produsului, e distructiv |
| Miros, gust | 2 | 3 | Evaluare senzoriala separata acopera detaliul |
| Temperatura in centru la congelare | 3 | 5 | Punct critic HACCP; se masoara in zonele cele mai reci ale sarjei |
| Umiditate, Aw, pH | 2 | 3 | Analize de laborator, cost mare pe determinare |

Argument in trei randuri: gramajul si aspectul cer esantioane mari pentru ca sunt
variabile si au consecinte legale sau comerciale; determinarile distructive sau de
laborator cer esantioane mici pentru ca sunt scumpe si au variabilitate intrinseca mica.
Pragurile de mai sus sunt cele uzuale in bakery industrial si se pot ajusta din
nomenclator dupa primele 6 luni de date reale.

### 6.2.2 Ce se intampla sub minimul de esantion

Statistica se calculeaza oricum, dar `rd_verdict` din TBL-16b devine
`Esantion insuficient` si nu poate sustine trecerea livrabilului LIV-11 in `Realizat`.
Tehnologul poate continua, dar nu poate declara testarea realizata. Blocajul este pe
livrabil, nu pe ecran: in hala nu se blocheaza nimeni la jumatatea unei masuratori.

### 6.2.3 Praguri de coeficient de variatie

PROPUNERE, pentru interpretarea automata:

| Tip de masuratoare | CV bun | CV acceptabil | CV problematic |
|---|---|---|---|
| Greutate bucata (produs depus sau injectat) | sub 2% | 2 - 4% | peste 4% |
| Greutate bucata (produs laminat si taiat) | sub 3% | 3 - 5% | peste 5% |
| Dimensiuni liniare | sub 3% | 3 - 6% | peste 6% |
| Inaltime dupa coacere | sub 5% | 5 - 10% | peste 10% |

Argument: un CV bun spune ca procesul este capabil, chiar daca media este deplasata -
media se corecteaza prin setare, imprastierea nu. Un lot cu media perfecta si CV de 8% la
gramaj va produce neconformitati in serie.

### 6.2.4 Tratarea valorilor aberante

6.2.4.1 Regula: **nicio valoare nu se sterge**. Se marcheaza `rd_exclus = Da`, cu motiv
obligatoriu, si ramane vizibila in raport, taiata, cu motivul afisat.

6.2.4.2 Detectarea automata: sistemul semnaleaza vizual, cu pictograma de avertizare,
orice valoare aflata la mai mult de 2 abateri standard de medie, si orice valoare aflata
in afara intervalului [mediana - 1.5 x IQR, mediana + 1.5 x IQR] cand n >= 8. La n < 8,
se semnaleaza doar valorile in afara tolerantei declarate; testele statistice de
aberanta nu au putere la esantioane atat de mici.

6.2.4.3 Motivele admise de excludere sunt din nomenclator: bucata deteriorata la
prelevare; eroare de citire a cantarului; bucata de la pornirea liniei, inainte de
stabilizare; bucata de capat de banda; masuratoare dublata din greseala. Nu exista
motivul "valoare prea diferita". O valoare corect masurata pe o bucata reala nu se
exclude niciodata: ea este exact informatia pentru care se face trialul.

6.2.4.4 Daca dupa excludere raman sub minimul din 6.2.1, verdictul devine
`Esantion insuficient` si se cer masuratori suplimentare.

## 6.3 Conformitatea fata de toleranta

6.3.1 Toleranta se declara in fisa de testare (TBL-14, `rd_tolerante`) si se propaga in
fiecare masuratoare ca tinta, toleranta minus si toleranta plus. Conformitatea pe bucata
este o coloana Calculated.

6.3.2 Verdictul pe tip de masuratoare, in TBL-16b:

| Verdict | Conditie |
|---|---|
| Conform | Conformitate 100% si media in interval si CV in banda "bun" sau "acceptabil" |
| Conform cu observatii | Conformitate >= 90% sau CV in banda "problematic", cu media inca in interval |
| Neconform | Conformitate sub 90%, sau media in afara intervalului de toleranta |
| Esantion insuficient | n sub minimul din 6.2.1 dupa excluderi |

6.3.3 NOTA: pentru gramajul produsului preambalat exista si cerinta legala de cantitate
nominala, care nu este aceeasi cu toleranta tehnologica interna. Toleranta interna trebuie
sa fie mai stransa decat cea legala; verificarea legala se face la ambalare, in productie,
si se documenteaza in SDP la sectiunea 7, nu aici.

## 6.4 Referinta de comparatie

6.4.1 Referinta este obligatorie la deschiderea proiectului. Se alege din: produs al
concurentei, produs actual, mostra de la client, specificatie de la client, sau
inexistenta. `Inexistenta` este o alegere explicita, nu un camp lasat gol.

6.4.2 Cand exista referinta, evaluarea senzoriala se face comparativ: aceleasi criterii,
aceeasi scala, aplicate si produsului dezvoltat, si referintei, in aceeasi sesiune, cu
probele codificate. Diferentele se inregistreaza in `rd_diferenta` si se comenteaza in
raport.

6.4.3 Pentru referinta se inregistreaza si datele obiective disponibile: gramaj, pret de
raft, lista de ingrediente de pe eticheta, valorile nutritionale declarate, poza. Acestea
sustin pozitionarea si sunt necesare la discutia de pret cu clientul.

6.4.4 PROPUNERE: la referinta de tip "Produs al concurentei" se masoara si greutatea si
dimensiunile reale, pe minimum 5 bucati. Motiv: eticheta declara gramajul nominal, iar
produsul concurentei livreaza frecvent sub el; fara masuratoare proprie, tinta de
dezvoltare se fixeaza gresit de la inceput.

## 6.5 Evaluarea senzoriala

### 6.5.1 PROPUNERE: grila profesionala cu criterii ponderate

Scala 1-5, ancorata descriptiv. Ponderile difera pe categorie de produs; suma este 100
pe fiecare categorie. Mai jos, grila pentru foietaj congelat, cea mai relevanta pentru
portofoliul companiei.

**Foietaj (croissant, produse laminate)**

| Cod | Criteriu | Grupa | Pondere | Eliminatoriu sub |
|---|---|---|---|---|
| CR-01 | Volum si inaltime dupa coacere | Aspect exterior | 15 | 2 |
| CR-02 | Forma si regularitate | Aspect exterior | 10 | - |
| CR-03 | Culoarea si uniformitatea cojii | Aspect exterior | 10 | 2 |
| CR-04 | Straturi vizibile in sectiune (foietare) | Structura interna | 20 | 2 |
| CR-05 | Alveolare si uniformitatea miezului | Structura interna | 10 | - |
| CR-06 | Crocanta la exterior | Textura | 10 | - |
| CR-07 | Elasticitate si moliciune la interior | Textura | 10 | - |
| CR-08 | Aroma de unt sau grasime | Aroma si gust | 10 | 2 |
| CR-09 | Gust general si echilibru | Aroma si gust | 5 | 2 |

**Aluat dospit (cozonac, brioche, produse cu umplutura)**

| Cod | Criteriu | Grupa | Pondere | Eliminatoriu sub |
|---|---|---|---|---|
| CR-11 | Volum si dezvoltare | Aspect exterior | 15 | 2 |
| CR-12 | Culoarea cojii | Aspect exterior | 10 | - |
| CR-13 | Structura miezului si uniformitatea alveolelor | Structura interna | 20 | 2 |
| CR-14 | Distributia si cantitatea umpluturii | Structura interna | 15 | 2 |
| CR-15 | Moliciune si revenire la apasare | Textura | 15 | 2 |
| CR-16 | Aroma de fermentare | Aroma si gust | 10 | - |
| CR-17 | Gust general si echilibru dulce | Aroma si gust | 10 | 2 |
| CR-18 | Comportament dupa decongelare la 4 ore | Comportament la utilizare | 5 | - |

Argument in trei randuri: ponderile mari merg la criteriile care decid reclamatia
clientului (foietarea la laminate, structura si umplutura la produsele dospite), nu la
cele usor de masurat. Criteriile eliminatorii sunt cele la care un scor de 1 face
produsul nevandabil indiferent de restul grilei. Grilele se tin in nomenclator si se
ajusteaza dupa un an de date, nu se cimenteaza in aplicatie.

### 6.5.2 Ancorele descriptive

Fiecare criteriu are text pentru 1, 3 si 5. Scorurile 2 si 4 sunt intermediare, fara
text propriu, ca sa nu se ceara evaluatorului o precizie pe care nu o are. Exemplu pe
CR-04:

| Scor | Ancora pentru "Straturi vizibile in sectiune" |
|---|---|
| 1 | Straturile nu se disting; sectiune compacta, aspect de aluat nelaminat sau grasime absorbita complet |
| 3 | Straturi vizibile, dar neuniforme; zone lipite, foietare partiala pe una din laturi |
| 5 | Straturi numeroase, subtiri, clar separate, uniform distribuite pe toata sectiunea |

6.5.2.1 Toate cele 17 criterii au ancore complete in `data/nomenclatoare.json`, sub
`criterii_senzoriale`. Ancorele sunt cea mai importanta parte a grilei: fara ele, doi
evaluatori dau note diferite aceluiasi produs si dezacordul nu este interpretabil.

### 6.5.3 PROPUNERE: numarul de evaluatori

| Situatie | Numar minim | Compozitie |
|---|---|---|
| Trial de rutina, iteratie intermediara | 2 | Tehnolog + inca o persoana din R&D |
| Trial care sustine decizia de a merge mai departe | 3 | Tehnolog, Manager R&D sau alt tehnolog, Calitate |
| Evaluare finala inainte de mostra la client | 5 | R&D (2), Calitate, Productie, KAM sau comercial |
| Evaluare comparativa cu referinta | 5 | Idem, obligatoriu cu probe codificate oarb |
| Panel extins pentru produs de volum mare | 8 - 12 | Panel intern instruit, din mai multe departamente |

Argument: sub 3 evaluatori nu se poate vorbi de dezacord, deci nici de incredere in
verdict; peste 5 evaluatori costul organizarii creste mai repede decat precizia, in afara
lansarilor mari. Numarul se inregistreaza automat, ca Rollup pe evaluarile distincte.

### 6.5.4 Tratarea dezacordurilor

6.5.4.1 Sistemul calculeaza `rd_dezacord` = amplitudinea maxima a scorurilor pe un
singur criteriu (maxim minus minim, intre evaluatori).

| Dezacord maxim | Interpretare | Ce se intampla |
|---|---|---|
| 0 - 1 | Consens | Se trece mai departe |
| 2 | Dezacord normal | Se noteaza, fara actiune |
| 3 sau mai mult | Dezacord semnificativ | Criteriul se marcheaza rosu; se cere o a doua runda pe acel criteriu, cu discutie prealabila despre ancora |

6.5.4.2 Nu se face media peste un dezacord de 3 sau mai mult. O medie de 3 obtinuta din
notele 1 si 5 nu inseamna produs mediu, inseamna ca doi oameni au evaluat lucruri
diferite sau au inteles altfel ancora.

6.5.4.3 Daca dezacordul persista dupa a doua runda, decizia o ia Managerul R&D, cu motiv
scris in `rd_actiuni`. Se pastreaza ambele runde.

### 6.5.5 Verdictul final

Regula de calcul, aplicata automat, cu posibilitatea de a fi inasprita manual, niciodata
inmuiata:

```
scor_ponderat = SUMA(scor_mediu_criteriu * pondere_criteriu) / 100

verdict:
  Respins                  daca exista criteriu eliminatoriu cu scor mediu sub prag
                           SAU exista defect cu severitate Critic
                           SAU scor_ponderat < 3.0
  Acceptat cu observatii   daca scor_ponderat intre 3.0 si 3.9
                           SAU exista defect cu severitate Major
                           SAU dezacord maxim >= 3 nerezolvat
  Acceptat                 daca scor_ponderat >= 4.0 si niciuna din conditiile de mai sus
```

6.5.5.1 La evaluarea comparativa se adauga o conditie: daca `rd_diferenta` (produs minus
referinta) este mai mica de -0.5, verdictul nu poate fi mai bun de `Acceptat cu
observatii`, indiferent de scorul absolut. Motiv: un produs care scoate 4.2 dar sta sub o
referinta de 4.8 nu castiga listarea.

6.5.5.2 Verdictul `Acceptat cu observatii` obliga la completarea campului `rd_actiuni`,
cu ce se modifica si cine raspunde. Fara acel text, evaluarea nu se poate salva ca
finalizata.

## 6.6 Ce se intampla cu formularele Excel actuale

6.6.1 Formularele de masuratori de azi (formular gol greutate, formular masuratori)
dispar ca fisiere. Devin ecrane pe telefon, completate la linie, cu poze atasate:
ECR-11 (masuratori la linie) si ECR-12 (evaluare senzoriala), descrise in Sectiunea 10.

6.6.2 Fisierul se genereaza la cerere din date, prin butonul "Genereaza raport de
testare" (FLX-12), daca cineva il vrea pe hartie sau il trimite clientului. Nu exista
drum invers: nu se incarca fisiere Excel de masuratori inapoi in sistem.

6.6.3 NOTA: exceptia este importul de volume mari, cerut in constrangeri. Pentru
prelevarile de la productia 0, unde se cantaresc 20 de bucati de doua-trei ori pe
schimb, ecranul mobil ramane varianta principala, dar se accepta si un import din Excel
cu doua coloane (numar bucata, valoare), pentru cazul in care cantarul liniei exporta
direct. Formulele in engleza, separator virgula.


<!-- ==================== S07-productie-0.md ==================== -->

---

# Sectiunea 7 - Productie 0

Compania nu inregistreaza azi nimic structurat la productia 0. Toata sectiunea este
PROPUNERE, construita pe practica de bakery industrial si pe cerintele IFS Food de
validare a procesului (cap. 4.4 si 5.6).

Argument in trei randuri: productia 0 este singurul moment in care se afla daca produsul
dezvoltat in laborator si pe trial este si producibil in conditii reale, la viteza
reala, cu operatorii reali. Fara inregistrari structurate, informatia ramane la
tehnologul care a fost prezent, iar IL-ul si SDP-ul se scriu din memorie. Cu inregistrari,
productia 0 devine sursa de adevar pentru parametrii de proces si baza de comparatie a
revizuirii de la 30 de zile.

## 7.1 Structura inregistrarii

O productie 0 = o inregistrare `rd_productie0` (TBL-33) + N inregistrari
`rd_inregistrareprod0` (TBL-34), pe cinci tipuri: parametru de proces, rebut pe cauza,
problema, masuratoare de ambalare, verificare HACCP. Completarea se face pe telefon, la
linie, in ECR-14.

## 7.2 Cantitati si randament

| Nr | Ce se inregistreaza | Camp | Cum |
|---|---|---|---|
| 7.2.1 | Cantitate planificata (kg si bucati) | rd_cantitateplanificata | Din planul IPN |
| 7.2.2 | Cantitate de aluat introdusa (kg) | rd_aluatintrodus | Cantarire la malaxor, pe sarje |
| 7.2.3 | Numar de sarje | rd_numarsarje | - |
| 7.2.4 | Bucati bune obtinute | rd_bucatibune | Numarate la ambalare |
| 7.2.5 | Cantitate realizata (kg) | rd_cantitaterealizata | bucati bune x gramaj / 1000 |
| 7.2.6 | Randament aluat (%) | rd_randamentaluat | (cantitate realizata / aluat introdus) x 100 |
| 7.2.7 | Randament fata de trial (%) | rd_randamentvstrial | randament productie 0 / randament trial x 100 |
| 7.2.8 | Realizat fata de planificat (%) | rd_realizatvsplan | cantitate realizata / planificata x 100 |

7.2.9 Randamentul aluatului este indicatorul central. Un randament sub 92% la produse
laminate sau sub 95% la produse depuse inseamna, aproape intotdeauna, ca antecalculul a
folosit o pierdere tehnologica prea optimista si ca marja reala este mai mica decat cea
promisa. Diferenta se raporteaza automat catre antecalcul (`rd_costreal`).

## 7.3 Rebutul pe cauze

7.3.1 Rebutul se inregistreaza in kg si in procente, cu cauza din lista predefinita. Nu
exista camp de rebut fara cauza.

| Cod | Cauza | Grupa | Observatii |
|---|---|---|---|
| RB-01 | Capat de banda si pornire de linie | Proces normal | Se asteapta la orice pornire; se urmareste sa nu creasca |
| RB-02 | Setare de linie in curs | Setup | Se cumuleaza cu timpul de setup |
| RB-03 | Greutate in afara tolerantei | Calitate | Semnaleaza probleme de divizare sau laminare |
| RB-04 | Forma sau dimensiune neconforma | Calitate | - |
| RB-05 | Lipire pe banda sau pe forme | Proces | Tipic la aluat prea moale sau ungere insuficienta |
| RB-06 | Rupere sau destramare la manipulare | Proces | - |
| RB-07 | Umplutura iesita sau distribuita neuniform | Proces | Specific produselor injectate |
| RB-08 | Coacere neuniforma sau ardere | Coacere | - |
| RB-09 | Congelare incompleta sau aglomerare | Congelare | Punct critic HACCP |
| RB-10 | Ambalare defectuoasa (sudura, etichetare) | Ambalare | - |
| RB-11 | Corp strain sau contaminare | Siguranta alimentelor | Declanseaza procedura de neconformitate |
| RB-12 | Oprire de linie neplanificata | Mentenanta | Se coreleaza cu timpul de oprire |
| RB-13 | Materie prima neconforma | Materie prima | Se leaga de MP si de furnizor |
| RB-14 | Eroare de operare | Personal | Semnaleaza nevoia de instruire suplimentara |

7.3.2 Se calculeaza automat: rebut total in kg, rebut in procente din cantitatea
introdusa, si distributia pe cauze. Cauza cu ponderea cea mai mare se afiseaza in raport
ca "cauza dominanta".

7.3.3 PROPUNERE de prag: rebut total peste 5% la productia 0 pentru produse laminate,
peste 3% pentru produse depuse. Peste prag, decizia finala nu poate fi `Validat`, ci cel
mult `Validat conditionat`, cu plan de reducere. Motiv: un rebut mare la productia 0, cu
tehnologul prezent si atentia maxima, va fi si mai mare in serie, cand nu mai este nimeni
langa linie.

## 7.4 Viteza si timpii

| Nr | Ce se inregistreaza | Camp | Observatii |
|---|---|---|---|
| 7.4.1 | Viteza nominala a liniei (buc/h) | rd_vitezanominala | Din nomenclatorul de linie |
| 7.4.2 | Viteza reala medie (buc/h) | rd_vitezareala | Bucati / timp efectiv de productie |
| 7.4.3 | Eficienta de viteza (%) | rd_eficientaviteza | reala / nominala x 100 |
| 7.4.4 | Timp de setup (min) | rd_timpsetup | De la eliberarea liniei pana la prima bucata buna |
| 7.4.5 | Timp de schimb de sortiment (min) | rd_timpschimb | Comparat cu cele 120 de minute implicite |
| 7.4.6 | Timp total de ocupare a liniei (min) | rd_timpocupare | Setup + productie + curatare |
| 7.4.7 | Opriri neplanificate (numar si minute) | Inregistrari de tip Problema | Cu cauza |

7.4.8 Eficienta de viteza intra direct in antecalculul revizuit: daca linia merge la 70%
din viteza nominala, costul de manopera si de energie pe kilogram creste cu aproximativ
43%, iar marja calculata initial nu mai este reala. Aceasta este a doua sursa de eroare
de antecalcul, dupa randament.

## 7.5 Parametrii reali de proces fata de cei specificati

7.5.1 Pentru fiecare faza se inregistreaza valoarea specificata (din SDP), valoarea reala
si abaterea. Abaterea in afara tolerantei se marcheaza automat si intra in numarul de
abateri.

| Faza | Parametri urmariti | Tolerante tipice |
|---|---|---|
| Framantare | Timp la viteza 1 si 2, temperatura finala a aluatului, consistenta | Temperatura +/- 1 C |
| Fermentare | Timp, temperatura, umiditate | Timp +/- 10%, temperatura +/- 1 C |
| Laminare | Numar de ture, grosime finala, temperatura grasimii, temperatura camerei | Grosime +/- 0.2 mm |
| Formare si divizare | Greutate la divizare, dimensiuni, viteza de taiere | Greutate conform 6.2.1 |
| Dospire | Timp, temperatura, umiditate, inaltime atinsa | Timp +/- 10%, temperatura +/- 1 C |
| Coacere | Temperatura pe zone, timp, aburire, viteza benzii | Temperatura +/- 5 C |
| Congelare | Temperatura tunelului, timp, temperatura in centrul produsului la iesire | Centru sub -18 C, obligatoriu |
| Ambalare | Greutate neta, sudura, etichetare, temperatura in zona de ambalare | Vezi 7.6 |

7.5.2 Temperatura in centrul produsului la iesirea din congelator este punct critic
HACCP. Se masoara pe minimum 5 bucati, din zonele cele mai defavorabile ale sarjei, si
este eliminatorie: o singura valoare peste -18 C opreste validarea, indiferent de restul
raportului.

7.5.3 Parametrii reali confirmati la productia 0 sunt cei care intra in SDP si in IL-ul
de productie. Daca parametrii reali difera semnificativ de cei din SDP, SDP-ul se
actualizeaza cu versiune noua inainte de inchiderea proiectului - nu se lasa specificatia
sa contrazica realitatea de pe linie.

## 7.6 Greutatea la ambalare si toleranta

| Nr | Ce se inregistreaza | Observatii |
|---|---|---|
| 7.6.1 | Greutate medie pe bucata | Minimum 20 de bucati, in 4 prelevari |
| 7.6.2 | Abatere standard si CV | Vezi 6.2.3 |
| 7.6.3 | Abatere de la gramajul declarat (%) | (medie - declarat) / declarat x 100 |
| 7.6.4 | Numar de bucati sub gramajul minim admis | Cerinta legala |
| 7.6.5 | Greutate neta pe ambalaj | Minimum 5 ambalaje |
| 7.6.6 | Supraumplere medie (%) | Cat se da gratis clientului |

7.6.7 Supraumplerea este un cost ascuns semnificativ. La un produs de 80 g cu 3%
supraumplere si 500 de tone pe an, se dau gratis 15 tone de produs. Se raporteaza explicit
in raportul de productie 0 si in revizuirea de la 90 de zile.

## 7.7 Conformitatea cu punctele critice HACCP

7.7.1 Se inregistreaza, ca inregistrari de tip `Verificare HACCP`, fiecare CCP si oPRP
din planul HACCP actualizat pentru produs, cu: valoarea limita, valoarea masurata,
momentul, cine a verificat, conform da / nu, actiunea corectiva la deviatie.

7.7.2 Punctele critice tipice pentru bakery congelat: temperatura in centru la iesirea
din congelare; detectia de metale sau raze X, daca linia are; temperatura camerei de
ambalare; integritatea sitelor la faina; controlul alergenilor la schimbarea de sortiment.

7.7.3 O singura neconformitate HACCP nerezolvata blocheaza decizia `Validat` si
declanseaza procedura de neconformitate a companiei. Sistemul nu permite inchiderea
productiei 0 cu un CCP neconform si fara actiune corectiva completata.

## 7.8 Problemele aparute

7.8.1 Fiecare problema se inregistreaza separat, cu: descriere, momentul aparitiei, faza
afectata, impact (oprire, rebut, calitate), actiune corectiva imediata, actiune
preventiva propusa, responsabil, termen, status. Poza este incurajata si se ataseaza din
telefon.

7.8.2 Problemele cu actiune deschisa la momentul deciziei finale fac imposibila decizia
`Validat`. Se accepta `Validat conditionat`, cu lista actiunilor si termenele lor.

## 7.9 Decizia finala

| Decizie | Conditii | Consecinta |
|---|---|---|
| Validat | Randament peste prag, rebut sub prag, zero abateri HACCP, zero probleme deschise, gramaj conform, evaluare senzoriala Acceptat | Produsul intra in serie; SDP si IL raman ca la productia 0 |
| Validat conditionat | Toate conditiile de siguranta indeplinite, dar exista abateri de proces, rebut peste prag sau actiuni deschise | Produsul intra in serie sub urmarire; lista de conditii cu responsabil si termen; revizuirea de la 30 de zile devine obligatorie |
| Se repeta | Neconformitate HACCP, evaluare senzoriala Respins, randament sub prag critic, sau imposibilitatea de a produce la viteza acceptabila | Nu intra in serie; se planifica o noua productie 0, cu ce se schimba |

7.9.1 Decizia se ia de Managerul R&D impreuna cu Calitatea si Productia. Se
inregistreaza cine a decis si pe ce baza. Decizia `Validat conditionat` fara lista de
conditii nu se poate salva.

## 7.10 Ce indicatori rezulta si cum alimenteaza IL-ul si SDP-ul

### 7.10.1 Indicatori care rezulta din productia 0

| Indicator | Formula | Unde se foloseste |
|---|---|---|
| Randament de proces (%) | Cantitate realizata / aluat introdus | Antecalcul revizuit, comparatie la 30 de zile |
| Rebut la lansare (%) | Rebut / cantitate introdusa | Prag de comparatie pentru serie |
| Eficienta de viteza (%) | Viteza reala / nominala | Costul real de manopera, planificarea capacitatii |
| Timp de setup real (min) | Masurat | Corectia celor 120 de minute implicite din planificare |
| Capabilitate de gramaj | CV al greutatii la ambalare | Decizia de reglare a divizorului |
| Supraumplere (%) | Media reala fata de gramajul declarat | Costul ascuns, urmarit la revizuire |
| Rata de conformitate HACCP (%) | Verificari conforme / total | Intra in Q-Corect |
| Numar de abateri de proces | Numarate | Calitatea specificatiei initiale |

### 7.10.2 Cum alimenteaza IL-ul de productie

Instructiunea de lucru se scrie din parametrii **reali** confirmati la productia 0, nu
din cei teoretici din trial. Concret, IL-ul preia: valorile de proces pe faze cu
tolerantele confirmate; punctele de verificare si frecventa lor, derivate din unde au
aparut abaterile; setarile de linie efective (grosimi, viteze, temperaturi pe zone);
timpul de setup real; cauzele de rebut cele mai frecvente, ca puncte de atentie pentru
operator; si actiunile corective pentru problemele care s-au manifestat.

### 7.10.3 Cum alimenteaza SDP-ul

SDP-ul se actualizeaza cu versiune noua dupa productia 0, daca exista diferente. Preia:
parametrii reali (sectiunea 4 din DOC-07), controalele in proces derivate din 7.7,
randamentul real ca referinta, si datele de ambalare confirmate. Un SDP care nu a fost
confruntat cu o productie 0 este o ipoteza; dupa productia 0 devine specificatie.

7.10.4 NOTA: exista o tentatie de a lasa SDP-ul asa cum a fost aprobat inainte de
implementare, ca sa nu se reia aprobarea. Este exact greseala care produce, peste sase
luni, un IL care contrazice specificatia si o neconformitate la audit. Blueprintul cere
explicit versiune noua de SDP la orice diferenta semnificativa constatata la productia 0,
inainte de trecerea proiectului in `Finalizat`.


<!-- ==================== S08-revizuire-post-implementare.md ==================== -->

---

# Sectiunea 8 - Revizuirea post-implementare

Nu exista azi ca proces formal. Toata sectiunea este PROPUNERE.

Argument in trei randuri: intre 130 si 180 de proiecte pe an inseamna ca R&D preda
produse in serie fara sa afle niciodata daca ipotezele de cost, randament si volum s-au
confirmat. Revizuirea la 30, 60 si 90 de zile este singurul mecanism care inchide bucla si
alimenteaza cu date reale antecalculul urmatorului proiect. Se declanseaza automat,
altfel nu se face niciodata.

## 8.1 De ce trei momente si nu unul

| Moment | Ce se poate sti deja | Ce nu se poate sti inca |
|---|---|---|
| 30 de zile | Daca produsul se poate produce repetat; primele reclamatii de calitate; randamentul in primele serii; rebutul | Volumul real, comportamentul in raft, costul stabilizat |
| 60 de zile | Daca randamentul s-a stabilizat dupa curba de invatare a operatorilor; costul real pe cateva serii | Sezonalitatea, reactia clientului final |
| 90 de zile | Volumul real fata de estimare; costul real; reclamatiile de la consumator; decizia de continuare | Comportamentul pe un ciclu complet de sezon |

8.1.1 Cele trei momente au greutate diferita. La 30 de zile se verifica productibilitatea;
la 60 costul; la 90 se ia decizia. Numai revizuirea de la 90 de zile este livrabil
obligatoriu (LIV-43).

## 8.2 Ce se inregistreaza la fiecare revizuire

| Nr | Element | Sursa | Obligatoriu la |
|---|---|---|---|
| 8.2.1 | Cantitate produsa cumulat (kg si bucati) | Manual sau import din SAP / planificare | 30, 60, 90 |
| 8.2.2 | Numar de loturi produse | Idem | 30, 60, 90 |
| 8.2.3 | Reclamatii de la client (numar, tip, cantitate afectata) | Calitate | 30, 60, 90 |
| 8.2.4 | Neconformitati interne (numar, tip) | Calitate | 30, 60, 90 |
| 8.2.5 | Randament mediu in serie (%) | Din productie | 30, 60, 90 |
| 8.2.6 | Randament la productia 0 (%) | Automat, din TBL-33 | 30, 60, 90 |
| 8.2.7 | Diferenta de randament (puncte procentuale) | Calculat | 30, 60, 90 |
| 8.2.8 | Rebut mediu in serie (%) | Din productie | 30, 60, 90 |
| 8.2.9 | Rebut la productia 0 (%) | Automat | 30, 60, 90 |
| 8.2.10 | Cost real pe kg | Din controlling sau calculat din consumuri | 60, 90 |
| 8.2.11 | Cost din antecalcul pe kg | Automat, din TBL-22 | 60, 90 |
| 8.2.12 | Abatere de cost (%) | Calculat | 60, 90 |
| 8.2.13 | Volum realizat fata de estimat (%) | KAM | 90 |
| 8.2.14 | Feedback de la client | KAM | 30, 90 |
| 8.2.15 | Feedback de la KAM (pozitionare, pret, concurenta) | KAM | 90 |
| 8.2.16 | Feedback de la Productie (usurinta de operare) | Productie | 30 |
| 8.2.17 | Numar de modificari de reteta sau proces dupa lansare | Automat, din versiuni | 60, 90 |
| 8.2.18 | Decizie | Manager R&D | 90 |

8.2.19 Campurile marcate "Automat" se preiau fara interventie umana din inregistrarile
existente. Numai 6 campuri raman de completat manual la revizuirea de 30 de zile si 9 la
cea de 90. Este limita peste care procesul nu se mai face.

## 8.3 Indicatorii calculati

```
diferenta_randament (pp) = randament_serie - randament_productie_0
abatere_cost (%)         = (cost_real - cost_antecalcul) / cost_antecalcul * 100
realizare_volum (%)      = volum_realizat_anualizat / volum_estimat_anual * 100
rata_reclamatii (ppm)    = cantitate_reclamata / cantitate_produsa * 1.000.000
indice_sanatate          = vezi 8.4
```

8.3.1 Volumul realizat se anualizeaza liniar la 90 de zile (`x 4`) numai pentru produsele
fara sezonalitate declarata. Pentru cele sezoniere, comparatia se face cu volumul estimat
pentru perioada respectiva, nu cu cel anual - altfel un produs de Craciun lansat in
septembrie apare intotdeauna ca subperformant.

## 8.4 PROPUNERE: indicele de sanatate al produsului

Un numar unic, pe 100 de puncte, care spune daca produsul lansat isi tine promisiunile:

| Componenta | Puncte | Cum se acorda |
|---|---|---|
| Cost | 30 | 30 daca abaterea de cost <= 0%; 20 pana la +5%; 10 pana la +10%; 0 peste |
| Volum | 25 | 25 daca realizarea >= 90%; 15 pana la 70%; 5 pana la 50%; 0 sub |
| Calitate | 25 | 25 daca zero reclamatii; 15 la sub 100 ppm; 5 la sub 500 ppm; 0 peste |
| Producibilitate | 20 | 20 daca diferenta de randament >= -1 pp; 10 pana la -3 pp; 0 sub |

Argument: fara un numar unic, revizuirea produce zece cifre pe care nimeni nu le compara
intre produse. Cu el, se poate face lista celor 10 produse lansate anul trecut care merita
optimizate si a celor 3 care ar trebui retrase.

8.4.1 Interpretare: peste 75 = mentinere; 50-75 = optimizare; sub 50 = candidat la
retragere. Indicele este orientativ, nu decide singur; decizia ramane la Managerul R&D.

## 8.5 Decizia

| Decizie | Cand | Ce declanseaza |
|---|---|---|
| Mentinere | Produsul isi tine promisiunile de cost, volum si calitate | Se inchide revizuirea; produsul iese din urmarirea R&D |
| Optimizare | Abatere de cost peste 5%, sau randament sub asteptari, sau reclamatii recurente | Se deschide automat un proiect nou de tip `Optimizare cost` sau `Reformulare`, legat de proiectul initial, cu prioritate mostenita |
| Retragere | Volum sub 50% din estimare, sau cost care face marja negativa, sau probleme de calitate nerezolvabile | Se notifica KAM si comercialul; decizia de retragere se ia in afara R&D, dar se inregistreaza aici |

8.5.1 Decizia `Optimizare` care creeaza automat un proiect nou este mecanismul prin care
revizuirea nu ramane un document. Proiectul nou mosteneste clientul, linia, reteta si
referinta, si intra in coada cu scorul calculat normal.

## 8.6 Declansarea automata

8.6.1 Ceasul porneste de la `rd_implementare.rd_dataimplementare`, adica data primei
productii in serie (nu data productiei 0).

8.6.2 FLX-15 se executa zilnic si:

| Pas | Actiune |
|---|---|
| 1 | Cauta implementarile cu data completata si fara revizuire creata pentru pragul curent |
| 2 | Creeaza inregistrarea `rd_revizuire` cu etapa (30 / 60 / 90) si data scadenta |
| 3 | Creeaza livrabilul corespunzator (LIV-41 / 42 / 43) |
| 4 | Precompleteaza toate campurile automate din 8.2 |
| 5 | Trimite sarcina catre Managerul R&D si cererile de date catre KAM, Calitate si Productie |
| 6 | Trece proiectul in status `In revizuire` daca era `Finalizat` |

8.6.3 Reamintiri: la data scadenta, la +7 zile si la +14 zile. La +21 de zile,
escaladare catre Head of R&D. O reviziune ramasa neefectuata mai mult de 30 de zile se
inchide automat cu status `Sarita` si motiv, si intra in raportul anual - se vede ca nu
s-a facut, nu dispare.

## 8.7 Cine raspunde

| Element | Responsabil de furnizare | Termen |
|---|---|---|
| Cantitate produsa, loturi, randament, rebut | Productie / Planificare | 5 zile de la cerere |
| Reclamatii si neconformitati | Calitate | 5 zile |
| Cost real | Controlling / Financiar | 10 zile |
| Volum realizat si feedback client | KAM | 5 zile |
| Sinteza, indice, decizie | Manager R&D | 15 zile de la data scadenta |
| Aprobarea deciziei la 90 de zile | Head of R&D | 20 de zile |

8.7.1 NOTA: revizuirea depinde de date din afara R&D (cost real, cantitati produse,
reclamatii). Daca aceste date nu vin, revizuirea nu se poate face si vina nu este a R&D.
Din acest motiv, campurile nefurnizate se marcheaza explicit ca `Date indisponibile`, cu
departamentul care nu le-a furnizat, si apar ca atare in raportul anual. Este singurul
mod in care lipsa de cooperare devine vizibila fara sedinte.

## 8.8 Ce se vede in aplicatie

8.8.1 Un tablou de bord `Produse lansate`, cu: produsul, data implementarii, indicele de
sanatate, abaterea de cost, realizarea de volum, numarul de reclamatii, decizia. Sortabil
si filtrabil pe an, client, linie si tehnolog.

8.8.2 Un raport anual `Ce am invatat`, care agrega abaterile de cost si de randament pe
categorie de produs si pe linie. Acesta este documentul care corecteaza, dupa un an,
ipotezele implicite de antecalcul si pierderea tehnologica din 5.5.6.


<!-- ==================== S09-alergeni-nutritionale.md ==================== -->

---

# Sectiunea 9 - Alergeni si valori nutritionale

Principiul: se calculeaza din reteta, nu se copiaza din ST-urile furnizorilor. ST-ul
furnizorului este sursa de date pentru **materia prima**; declaratia produsului finit este
rezultatul calculului pe reteta.

## 9.1 Datele necesare la nivel de materie prima

9.1.1 Fara datele de mai jos, complete, materia prima nu poate intra intr-o reteta care
sustine o eticheta. Se valideaza la aprobarea materiei prime de catre Calitate.

| Nr | Data | Camp in TBL-09 | Sursa | Obligatoriu |
|---|---|---|---|---|
| 9.1.1.1 | Alergeni continuti | rd_alergeni | ST furnizor, declaratie de alergeni | Da |
| 9.1.1.2 | Alergeni prezenti ca urme | rd_alergeniurme | Declaratie de contaminare incrucisata a furnizorului | Da |
| 9.1.1.3 | Energie (kcal si kJ / 100 g) | rd_energie | ST furnizor | Da |
| 9.1.1.4 | Grasimi (g / 100 g) | rd_grasimi | ST furnizor | Da |
| 9.1.1.5 | Acizi grasi saturati | rd_saturate | ST furnizor | Da |
| 9.1.1.6 | Glucide | rd_glucide | ST furnizor | Da |
| 9.1.1.7 | Zaharuri | rd_zaharuri | ST furnizor | Da |
| 9.1.1.8 | Fibre | rd_fibre | ST furnizor | Nu (optional pe eticheta) |
| 9.1.1.9 | Proteine | rd_proteine | ST furnizor | Da |
| 9.1.1.10 | Sare | rd_sare | ST furnizor | Da |
| 9.1.1.11 | Umiditate | rd_umiditate | ST furnizor sau determinare interna | Da, pentru calculul pierderii la coacere |
| 9.1.1.12 | Denumirea legala pentru lista de ingrediente | rd_denumirelegala | Reglementare + ST | Da |
| 9.1.1.13 | Ingrediente compuse (daca MP este un compus) | rd_ingredientecompuse | ST furnizor | Da, daca este cazul |
| 9.1.1.14 | Data ST-ului furnizorului | rd_datast | - | Da |
| 9.1.1.15 | Origine | rd_origine | ST furnizor | Nu, doar unde se declara |

9.1.2 Validare de plauzibilitate la salvare: suma grasimi + glucide + fibre + proteine +
sare + umiditate trebuie sa fie intre 95 si 105 g / 100 g. In afara acestui interval,
sistemul avertizeaza - de obicei inseamna o eroare de transcriere din ST.

9.1.3 ST-ul furnizorului mai vechi de 24 de luni marcheaza materia prima cu semnal galben
si o raporteaza in lista `Materii prime cu specificatie expirata`. Este cerinta IFS de
actualizare a specificatiilor de intrare.

9.1.4 Ingredientele compuse (de exemplu un ameliorator care contine faina de malt, enzime
si acid ascorbic) se inregistreaza cu componentele lor, pentru ca lista de ingrediente de
pe eticheta trebuie sa le declare in paranteza, nu sub numele comercial.

## 9.2 Modul de calcul

### 9.2.1 Valori nutritionale

```
Pentru fiecare nutrient N si fiecare linie de reteta i:
  contributie_i(N) = cantitate_i (kg/100 kg) * valoare_i(N) / 100

Valoare in aluat (per 100 g de aluat):
  valoare_aluat(N) = SUMA(contributie_i(N))

Corectie de pierdere la coacere (concentrare prin evaporarea apei):
  factor_randament = masa_produs_finit / masa_aluat        [din trial sau productia 0]
  valoare_finit(N) = valoare_aluat(N) / factor_randament

Exceptie pentru apa si umiditate:
  umiditate_finit = (masa_apa_aluat - apa_evaporata) / masa_produs_finit * 100
```

9.2.1.1 Energia nu se preia ca suma directa, ci se recalculeaza din macronutrienti, cu
factorii legali de conversie: grasimi 9 kcal/g, glucide 4, proteine 4, fibre 2,
polioli 2.4, alcool 7, acizi organici 3. Motiv: sumarea energiilor declarate de furnizori
propaga rotunjirile lor si produce, tipic, o abatere de 3-5% fata de valoarea corecta.

9.2.1.2 Factorul de randament este cel mai delicat element al calculului. Se preia, in
ordinea de preferinta: din productia 0 daca exista; altfel din trialul validat; altfel
din valoarea implicita pe categorie de produs, din nomenclator, marcata explicit ca
estimare. Valorile nutritionale calculate cu factor estimat se marcheaza vizual si nu pot
sustine o eticheta aprobata.

9.2.1.3 Rotunjirea pe eticheta urmeaza regulile din ghidul de aplicare a Reg. 1169/2011:
energia la numar intreg; grasimi, saturate, glucide, zaharuri, fibre si proteine la o
zecimala sub 10 g si la numar intreg peste; sarea la doua zecimale sub 1 g. Rotunjirea se
aplica la afisare, nu la stocare - in baza de date raman valorile complete.

### 9.2.2 Alergeni

```
alergeni_produs = REUNIUNEA( alergeni_continuti(MP_i) ) pentru toate liniile de reteta

urme_produs = REUNIUNEA( urme_declarate(MP_i) )
              + alergeni introdusi de linia de productie (vezi 9.4)
              MINUS alergenii deja continuti (un alergen continut nu se declara si ca urma)
```

9.2.2.1 Calculul alergenilor este o reuniune, nu o suma: nu exista prag sub care un
alergen continut nu se declara. Un gram de faina de grau intr-o tona de produs face
produsul purtator de gluten.

9.2.2.2 Alergenii se propaga si prin ingredientele compuse. Daca un ameliorator contine
faina de malt de orz, alergenul `Cereale cu gluten` se propaga chiar daca eticheta
comerciala a amelioratorului nu il scoate in evidenta.

## 9.3 Declaratia pe eticheta

9.3.1 Lista de ingrediente se genereaza automat, in ordine descrescatoare a cantitatii in
aluat, cu denumirile legale, cu ingredientele compuse in paranteza si cu alergenii
evidentiati tipografic (majuscule sau bold, consecvent pe toata eticheta).

9.3.2 Ordinea se calculeaza pe cantitatile din reteta, la momentul framantarii, nu pe
cele din produsul finit. Apa adaugata se declara daca depaseste 5% din produsul finit.

9.3.3 Textul generat este propunere, nu eticheta finala. Aprobarea ramane la Calitate,
care verifica formularea legala. Sistemul genereaza continutul; responsabilitatea juridica
ramane umana.

9.3.4 NOTA: solutia nu inlocuieste o baza de date de specificatii de alergeni certificata
si nu emite declaratii legale. Genereaza propunerea din datele introduse; corectitudinea
datelor de intrare este responsabilitatea celui care le introduce, iar acest lucru se
declara explicit in procedura.

## 9.4 Contaminarea incrucisata si urmele

9.4.1 Urmele au trei surse, tratate distinct:

| Sursa | Cum se determina | Unde se stocheaza |
|---|---|---|
| Urme declarate de furnizor pentru materia prima | Din declaratia furnizorului | rd_materieprima.rd_alergeniurme |
| Urme din linia de productie (produse anterioare pe aceeasi linie) | Din analiza de linie a Calitatii | Camp `rd_alergeniilinie` pe TBL-36 |
| Urme din amplasament (praf de faina, manipulare comuna) | Din evaluarea de risc a amplasamentului | Parametru global pe amplasament |

9.4.2 Declaratia `Poate contine` se genereaza din reuniunea celor trei, minus alergenii
deja declarati ca fiind continuti. Este supusa aprobarii Calitatii si nu se genereaza
automat pe eticheta fara aceasta aprobare.

9.4.3 PROPUNERE: declaratia de urme se face numai dupa o evaluare de risc documentata, nu
preventiv. Motiv: declararea defensiva a tuturor celor 14 alergeni ca posibile urme
inchide accesul la clienti si contrazice practica IFS, care cere ca declaratia sa fie
justificata de un risc real, evaluat, si gestionata prin curatare si secventiere, nu prin
text pe ambalaj.

9.4.4 Matricea de secventiere pe linie: pentru fiecare linie se retine ce alergeni au fost
prelucrati si ce protocol de curatare exista intre sortimente. Cand un produs nou intra pe
o linie, sistemul semnaleaza ce alergeni ar putea aparea ca urme si cere decizia
Calitatii, in cadrul livrabilului LIV-34 (plan HACCP).

## 9.5 Recalcularea automata

9.5.1 FLX-13 recalculeaza alergenii si valorile nutritionale, in urmatoarele situatii:

| Declansator | Ce se recalculeaza | Ce se notifica |
|---|---|---|
| Se adauga, se modifica sau se sterge o linie de reteta | Versiunea de reteta afectata | Tehnologul |
| Se modifica datele nutritionale sau de alergeni ale unei materii prime din catalog | Toate versiunile de reteta nevalidate care o folosesc | Tehnologii proiectelor afectate |
| Idem, pe o materie prima folosita intr-o reteta **validata** | Nimic automat: se genereaza o alerta de impact | Calitate si Head of R&D, vezi 9.5.2 |
| Se schimba factorul de randament (productie 0 finalizata) | Versiunea de reteta a produsului | Tehnologul |
| Se schimba furnizorul unei materii prime | Se compara alergenii vechi cu cei noi | Calitate, daca difera |

9.5.2 Regula critica: o reteta validata nu se recalculeaza tacit. Daca datele unei
materii prime se schimba dupa validare, sistemul nu modifica valorile de pe eticheta
aprobata; genereaza o alerta de impact care listeaza toate produsele afectate si cere o
decizie explicita: reteta noua, eticheta noua, sau confirmarea ca schimbarea nu afecteaza
declaratia. Recalcularea automata a unei etichete deja tiparite ar face imposibila
reconstituirea a ceea ce era declarat pe produsul livrat la o data din trecut.

9.5.3 Alerta de impact este cel mai valoros mecanism din aceasta sectiune: la schimbarea
unui furnizor de ameliorator care introduce faina de malt de orz, sistemul spune imediat
care dintre cele 400 de produse din portofoliu isi schimba declaratia de alergeni. Astazi
raspunsul la aceasta intrebare cere zile de munca manuala.

9.5.4 Fiecare recalculare scrie `rd_datacalcul` pe versiunea de reteta. O versiune al carei
calcul este mai vechi decat ultima modificare a unei materii prime componente se
marcheaza `Calcul invechit` si nu poate sustine aprobarea unei etichete.

## 9.6 Ce se afiseaza in aplicatie

9.6.1 Pe formularul versiunii de reteta, o fila `Alergeni si nutritionale` cu: tabelul
nutritional calculat pe 100 g de produs finit; lista alergenilor continuti, cu materia
prima care ii aduce pe fiecare (trasabilitatea alergenului); lista urmelor, cu sursa;
factorul de randament folosit si de unde provine; data ultimului calcul.

9.6.2 Trasabilitatea alergenului - "de ce apare soia in acest produs" - se raspunde cu un
click, pana la linia de reteta si materia prima care il introduce. Este intrebarea cea mai
frecventa la audit si la reclamatie.

9.6.3 Un raport transversal `Portofoliu pe alergeni`, care raspunde la intrebarea inversa:
care produse contin un anumit alergen. Necesar la orice cerinta de client care exclude un
alergen, si la orice retragere de produs.


<!-- ==================== S10-ecrane.md ==================== -->

---

# Sectiunea 10 - Ecranele aplicatiilor

Doua aplicatii: `R&D Birou` (model-driven) si `R&D Linie` (canvas, mobil). Regula de
departajare: daca activitatea se face stand jos, cu tastatura, este model-driven; daca se
face in picioare, cu manusi, este canvas.

## 10.1 Aplicatia model-driven `R&D Birou`

### 10.1.1 Harta de site

| Grup | Element | Tabela / tip | Cine il foloseste |
|---|---|---|---|
| **Lucrul meu** | Proiectele mele | rd_proiect, vizualizare filtrata | Tehnolog |
| | Livrabilele mele scadente | rd_livrabil | Toti |
| | Solicitarile mele | rd_solicitare | KAM |
| | Aprobarile mele | Vizualizare de sarcini | Manager R&D, Calitate |
| **Solicitari** | Solicitari in triaj | rd_solicitare | Manager R&D |
| | Toate solicitarile | rd_solicitare | KAM, Manager R&D |
| | Solicitari amanate | rd_solicitare | Manager R&D |
| **Proiecte** | Proiecte active | rd_proiect | Toti |
| | Coada pe prioritate | rd_proiect, grupat pe banda | Manager R&D, comercial |
| | Coada pe linie | rd_proiect, grupat pe linie | Manager R&D, Planificare |
| | Proiecte blocate | rd_proiect | Manager R&D |
| | Proiecte in intarziere | rd_proiect | Manager R&D, Head of R&D |
| | Arhiva (respinse, abandonate) | rd_proiect | Toti |
| **Executie** | Fise de testare | rd_fisatestare | Tehnolog |
| | Trialuri | rd_trial | Tehnolog |
| | Evaluari senzoriale | rd_evaluaresenzoriala | Tehnolog |
| | Retete si versiuni | rd_reteta | Tehnolog |
| | Antecalcule | rd_antecalcul | Tehnolog, Manager R&D |
| **Materii prime** | MP de proiect in asteptare | rd_mpproiect | Achizitii, Tehnolog |
| | Catalog de materii prime | rd_materieprima | Toti |
| | Furnizori | rd_furnizor | Achizitii, Calitate |
| | Iteratii de furnizor | rd_iteratiefurnizor | Achizitii |
| | MP cu specificatie expirata | rd_materieprima | Calitate |
| **Mostre** | Cereri de mostra | rd_ceremostra | Suport R&D |
| | Livrari in curs | rd_miscaremostra | Suport R&D |
| **Implementare** | IPN in pregatire | rd_implementare | Tehnolog, Productie |
| | Productii 0 | rd_productie0 | Tehnolog, Productie |
| | Revizuiri scadente | rd_revizuire | Manager R&D |
| **Specificatii** | Specificatii tehnice | rd_specificatie | Calitate |
| | SDP | rd_sdp | Calitate, Productie |
| | Etichete | rd_eticheta | Suport R&D, Calitate |
| **Tablouri de bord** | Tablou operational R&D | Dashboard | Manager R&D |
| | Incarcare tehnologi | Dashboard | Manager R&D |
| | Status public | Dashboard | Toata compania |
| | Indicatori | Dashboard | Head of R&D |
| **Configurare** | Sabloane de livrabile | rd_sablonlivrabil | Head of R&D |
| | Sabloane de etape | rd_sablonetapa | Head of R&D |
| | Linii de productie | rd_linie | Head of R&D |
| | Clienti | rd_client | Head of R&D, comercial |
| | Profiluri de tehnolog | rd_profiltehnolog | Head of R&D |
| | Criterii senzoriale | rd_criteriusenzorial | Head of R&D |
| | Motive si nomenclatoare | rd_motiv, rd_tipdocument | Head of R&D |
| | Parametri de prioritizare | Setari de mediu | Head of R&D |

### 10.1.2 ECR-01 Formularul de proiect

Formularul principal, cu antet permanent vizibil si file. Antetul (maximum 5 campuri,
limita platformei): cod proiect, status, tehnolog, termen negociat, banda de prioritate.

| Fila | Continut | Note |
|---|---|---|
| Sinteza | Client, produs, tip, linie, gramaj, volum, referinta, cele trei termene, urmatorul livrabil si cine il datoreaza, procentul de livrabile realizate, zilele blocate | Ecranul pe care il vede toata lumea |
| Livrabile | Subgrila cu livrabilele aplicabile, grupate pe faza, cu status colorat, termen si responsabil | Editare rapida in grila |
| Etape | Subgrila cu etapele, planificat fata de real, cu bara vizuala | - |
| Materii prime | Subgrila MP de proiect, cu status de ciclu, ETA si semnal de intarziere | Achizitii lucreaza aici |
| Testare | Fise de testare, trialuri, sinteza statistica a ultimului trial | - |
| Senzorial | Evaluari, scor ponderat, verdict, comparatie cu referinta | - |
| Reteta si cost | Versiunea curenta de reteta, antecalculul aprobat, marja | - |
| Specificatii | ST-uri, SDP, etichete, cu status si versiune | Calitate lucreaza aici |
| Implementare | IPN, conditii, productie 0, decizie | - |
| Documente | Controlul de documente SharePoint, cu arborele de foldere | Integrare nativa |
| Blocaje | Subgrila de blocaje, cu impactul cumulat | - |
| Istoric | Audit history si cronologia proiectului | Pentru audit |

10.1.2.1 Butoane pe bara de comenzi: `Accepta proiectul` (genereaza cod, folder,
livrabile, etape, termen propus), `Creeaza proiect-copil`, `Adauga blocaj`,
`Genereaza dosar TDV`, `Genereaza document` (alege sablonul), `Recalculeaza termenul`,
`Reatribuie tehnologul`.

### 10.1.3 ECR-02 Ecranul de triaj

Vizualizare de solicitari in status `Trimisa`, cu formular lateral care arata tot SCP-ul
pe un ecran, fara derulare. Trei butoane mari: Accepta, Respinge, Amana. Fiecare deschide
un dialog care cere motivul (obligatoriu la respingere si amanare) si, la acceptare,
propune tehnologul si termenul calculate de sistem, cu posibilitatea de a le schimba.

10.1.3.1 In dialogul de acceptare se afiseaza, langa fiecare tehnolog propus: numarul de
proiecte active, cate sunt P1, gradul de incarcare cu semnal color, si specializarea.
Aceasta este cerinta din 4.2: la alocare, managerul vede incarcarea.

### 10.1.4 ECR-03 Tabloul de bord operational R&D

| Componenta | Continut |
|---|---|
| Proiecte pe status | Grafic de bare, click pentru drill-down |
| Coada pe banda de prioritate | P1-P4, cu numarul si volumul cumulat |
| Incarcarea pe tehnolog | Bare orizontale cu prag, colorate verde / galben / rosu |
| Coada pe linie | Cele 9 linii, cu numarul de proiecte si primul slot liber estimat |
| Livrabile scadente in 7 zile | Lista, cu responsabil |
| Livrabile depasite | Lista, sortata dupa zile de intarziere |
| Proiecte blocate | Cu sursa blocajului si zilele cumulate |
| Materii prime cu ETA depasit | Lista, cu furnizorul |

### 10.1.5 ECR-04 Ecranul public de status

Cerinta: vizibil intregii companii, read-only, lizibil de oricine, fara instruire.

10.1.5.1 Un singur ecran, cu o singura lista si patru filtre mari (client, linie,
tehnolog, status). Coloanele: cod proiect, produs, client, status cu pastila colorata,
termen catre client, responsabil, urmatorul pas. Fara jargon: statusurile se afiseaza cu
denumirile din 2.2.1, care sunt deja in limbaj natural.

10.1.5.2 Sus, patru numere mari: proiecte active, proiecte finalizate luna aceasta,
proiecte in intarziere, proiecte blocate. Fara grafice complicate.

10.1.5.3 Regula de proiectare: cineva din productie sau din financiar trebuie sa poata
raspunde la intrebarea "unde este produsul X pentru clientul Y" in mai putin de 15
secunde, fara sa fi vazut vreodata aplicatia. Se testeaza cu doi oameni din afara R&D
inainte de publicare (criteriu de acceptanta CA-42).

10.1.5.4 NOTA: ecranul public este o aplicatie model-driven separata, cu un singur tabel
si un rol de securitate de citire. Nu se da acces la aplicatia principala cu drepturi
reduse - riscul de a expune accidental costuri si marje este prea mare.

### 10.1.6 ECR-05 Ecranul de prioritizare

Lista proiectelor cu scorul detaliat pe componente (volum, client, termen, efort, risc
MP, reutilizare), banda rezultata, si butonul `Suprascrie scorul` disponibil doar rolului
de manager operational / vanzari. Suprascrierea deschide un dialog care cere scorul nou
si motivul, si afiseaza bugetul de urgenta consumat de KAM-ul respectiv.

### 10.1.7 Alte ecrane model-driven

| Cod | Ecran | Continut |
|---|---|---|
| ECR-06 | Formular de solicitare (SCP) | Cele 10 sectiuni din 5.5.1, in trei file |
| ECR-07 | Formular de materie prima de proiect | Ciclul MP cu bara de progres pe cele 11 statusuri, campurile de Achizitii separate vizual |
| ECR-08 | Formular de antecalcul | Liniile de cost in grila editabila, cu totalul si marja recalculate live |
| ECR-09 | Formular de versiune de reteta | Liniile de reteta cu totalul de 100 kg validat, plus fila de alergeni si nutritionale |
| ECR-10 | Formular de revizuire post-implementare | Campurile automate precompletate, cele manuale grupate pe furnizorul de date |

## 10.2 Aplicatia canvas `R&D Linie`

### 10.2.1 Principii de proiectare pentru hala

| Principiu | Aplicare concreta |
|---|---|
| Tinta de atins cu manusi | Butoane de minimum 64 x 64 px, spatiere de minimum 12 px |
| Contrast ridicat | Text de minimum 18 px, contrast peste 7:1, fara gri pe gri |
| Minim de tastare | Numere din tastatura numerica mare; alegeri din butoane, nu din liste derulante |
| Conexiune slaba | Colectie locala, salvare in coada, sincronizare cand revine semnalul |
| O mana libera | Toate actiunile principale in treimea de jos a ecranului |
| Fara derulare la introducere | Un ecran = o intrebare sau un set scurt |
| Confirmare vizibila | Dupa salvare, confirmare mare, verde, 2 secunde |

10.2.1.1 Modul offline: aplicatia foloseste `SaveData` / `LoadData` pentru colectiile de
masuratori si pentru contextul proiectului. La pornire incarca proiectele active ale
utilizatorului si nomenclatoarele necesare. Fiecare salvare merge intr-o coada locala; un
indicator permanent arata cate inregistrari asteapta sincronizarea.

10.2.1.2 NOTA de platforma: Power Apps canvas nu poate crea offline inregistrari care au
nevoie de un ID generat de server (Autonumber). Din acest motiv, trialul si evaluarea se
creeaza online, in birou sau la intrarea in hala, iar in offline se adauga doar copii
(masuratori, scoruri, inregistrari de productie 0) la inregistrari care exista deja.
Aceasta constrangere trebuie respectata in proiectarea ecranelor, altfel sincronizarea
esueaza tacit.

### 10.2.2 ECR-11 Masuratori la linie

| Ecran | Continut | Actiuni |
|---|---|---|
| 11.1 Selectie | Lista proiectelor active ale utilizatorului, cu cod si produs, cautare rapida | Alege proiectul |
| 11.2 Selectie trial | Trialurile deschise; buton mare `Trial nou` | Alege sau creeaza |
| 11.3 Alege ce masor | Sase butoane mari: Greutate, Dimensiuni, Aspect, Alveolare, Miros, Gust | - |
| 11.4 Introducere numerica | Numarul bucatii afisat mare; tastatura numerica; tinta si toleranta afisate deasupra; culoare verde / rosu instantaneu; contor "bucata 3 din 10" | Salveaza si urmatoarea; Poza; Inapoi |
| 11.5 Introducere calitativa | Trei butoane: Conform, Minor neconform, Neconform; camp de observatie optional | Salveaza; Poza |
| 11.6 Sinteza | Media, abaterea standard, min, max, conformitatea, cu semnal color; lista valorilor, cu cele semnalate ca posibil aberante marcate | Exclude o valoare (cere motiv); Finalizeaza |

10.2.2.1 Ecranul 11.4 este cel mai folosit din toata solutia. Fluxul optim: se citeste
valoarea de pe cantar, se tasteaza, se apasa un singur buton, se trece automat la bucata
urmatoare. Trei atingeri pe bucata, nu mai mult.

### 10.2.3 ECR-12 Evaluare senzoriala

| Ecran | Continut |
|---|---|
| 12.1 Selectie | Proiect si trial; daca exista referinta, se anunta ca evaluarea este comparativa |
| 12.2 Instructiuni | Conditiile de degustare, codificarea probelor |
| 12.3 Criteriu | Un criteriu pe ecran: denumirea mare, ancorele pentru 1, 3 si 5 afisate ca text scurt, cinci butoane mari de scor; camp de comentariu care apare automat la scor 1 sau 2 |
| 12.4 Comparativ | Acelasi criteriu, aplicat referintei, imediat dupa; cele doua scoruri raman vizibile |
| 12.5 Defecte | Lista de defecte bifabile, grupate, cu severitate si procent |
| 12.6 Sinteza | Scor ponderat, comparatia cu referinta, verdictul propus de sistem, camp de actiuni |

10.2.3.1 Ancorele descriptive se afiseaza pe ecran, la fiecare criteriu. Este singura
modalitate prin care grila din 6.5 functioneaza in practica: un evaluator nu retine 17
seturi de ancore, dar le citeste in doua secunde daca sunt in fata lui.

### 10.2.4 ECR-13 Receptie de mostra

| Ecran | Continut |
|---|---|
| 13.1 Scanare sau selectie | Cerere de mostra din lista celor asteptate; scanare de cod de bare de pe AWB daca exista |
| 13.2 Verificare | Cantitate primita, temperatura la receptie (obligatorie pentru congelat), stare a ambalajului |
| 13.3 Conformitate | Conform / Neconform, cu motiv si poza obligatorie la neconform |
| 13.4 Confirmare | Salvare, cu actualizarea automata a statusului MP si notificarea tehnologului |

### 10.2.5 ECR-14 Checklist de productie 0

| Ecran | Continut |
|---|---|
| 14.1 Selectie | Productia 0 planificata pentru azi, pe linia utilizatorului |
| 14.2 Conditii IPN | Cele 13 conditii din 5.5.8, ca lista bifabila; nu se poate porni pana nu sunt toate bifate sau derogate cu motiv |
| 14.3 Cantitati | Aluat introdus pe sarje, bucati obtinute; tastatura numerica |
| 14.4 Parametri | Pe faze: valoarea specificata afisata, camp pentru valoarea reala, semnal automat de abatere |
| 14.5 Rebut | Cantitate si cauza din cele 14 predefinite, ca butoane; se pot adauga mai multe inregistrari |
| 14.6 Gramaj la ambalare | Ca ECR-11, cu esantion de 20 |
| 14.7 HACCP | Punctele critice, cu valoarea limita afisata, valoarea masurata si conform da / nu |
| 14.8 Probleme | Descriere, poza, actiune imediata, responsabil |
| 14.9 Sinteza si decizie | Randament, rebut pe cauze, abateri, conformitate HACCP; propunerea de decizie a sistemului; decizia se ia numai online, de Managerul R&D |

10.2.5.1 Ecranele 14.3 - 14.8 functioneaza offline. Ecranul 14.9 cere conexiune, pentru
ca decizia declanseaza fluxuri si nu poate ramane in coada locala.

### 10.2.6 ECR-15 Consultare rapida

Un ecran de cautare pentru cine este in hala si vrea doar sa vada: cauta dupa cod de
proiect, produs sau client, si afiseaza statusul, tehnologul, urmatorul pas si termenul.
Este versiunea mobila a ecranului public.

## 10.3 Ce nu se pune in canvas

10.3.1 Nu se pun in aplicatia mobila: triajul, alocarea, antecalculul, editarea retetei,
aprobarile de specificatii, configurarea. Acestea cer context si atentie, iar un ecran de
telefon garanteaza greseli.

10.3.2 NOTA: exista presiunea previzibila de a face "totul in canvas, ca e mai frumos".
Se rezista. Aplicatia model-driven da gratuit ceea ce in canvas ar cere saptamani de
lucru si intretinere permanenta: vizualizari filtrabile, cautare avansata, export in
Excel, audit, securitate pe coloana, formulare responsive. Canvas se foloseste exact
acolo unde model-driven nu poate: hala, manusi, poze, offline.


<!-- ==================== S11-securitate-roluri.md ==================== -->

---

# Sectiunea 11 - Securitate si roluri

## 11.1 Structura de business units

11.1.1 Se pastreaza o singura Business Unit radacina, cu numele companiei. Motiv: firma
are 400 de oameni si un singur departament R&D; o ierarhie de business units ar complica
securitatea fara sa rezolve nimic, iar separarea pe amplasamente nu este necesara pentru
ca proiectele circula intre ele.

11.1.2 Separarea se face pe echipe (Teams) si pe proprietar de inregistrare, nu pe
business units:

| Echipa | Membri | Rol |
|---|---|---|
| Echipa R&D | Tehnologi, suport, manager | Acces complet la proiecte |
| Echipa Comercial | KAM, manager operational vanzari | Acces la solicitari si la statusul proiectelor |
| Echipa Achizitii | Achizitii, aprovizionare | Acces la materii prime si furnizori |
| Echipa Calitate | Managementul calitatii | Acces la specificatii, alergeni, HACCP, aprobari |
| Echipa Planificare si Productie | Planificare, sefi de linie | Acces la implementare si productie 0 |
| Toata compania | Toti utilizatorii | Citire pe ecranul public |

## 11.2 Rolurile de securitate

| Cod | Rol | Cine il primeste | Numar estimat de utilizatori |
|---|---|---|---|
| ROL-01 | RD Head | Head of R&D | 1 |
| ROL-02 | RD Manager | Manager R&D | 1-2 |
| ROL-03 | RD Tehnolog | Tehnologi dezvoltare produs si solutii tehnice | 4-6 |
| ROL-04 | RD Suport | Suport / asistent R&D, pregatire si livrare mostre | 2-3 |
| ROL-05 | KAM | Key Account Manageri | 5-6 |
| ROL-06 | Comercial Manager | Manager operational / vanzari | 1 |
| ROL-07 | Achizitii | Achizitii si aprovizionare | 2-3 |
| ROL-08 | Calitate | Managementul calitatii, tehnicieni de calitate | 3-4 |
| ROL-09 | Planificare | Planificarea productiei | 2 |
| ROL-10 | Productie | Sefi de tura, sefi de linie | 8-12 |
| ROL-11 | Cititor companie | Toti angajatii cu cont | ~200 |
| ROL-12 | RD Auditor | Auditor extern, temporar | 0-2, activat la audit |
| ROL-13 | RD Administrator | Head of R&D (al doilea rol) | 1 |

## 11.3 Nivelurile de acces Dataverse

Notatie: `U` = User (doar inregistrarile proprii), `BU` = Business Unit (toata organizatia,
in configuratia noastra), `-` = fara drept, `Org` = organizational.

## 11.4 Matricea Rol x Tabela

Fiecare celula are formatul `Creare / Citire / Scriere / Stergere / Atribuire`.

### 11.4.1 Tabelele de proces

| Tabela | RD Head | RD Manager | RD Tehnolog | RD Suport | KAM | Comercial Mgr | Achizitii | Calitate | Planificare | Productie | Cititor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rd_solicitare | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | -/BU/-/-/- | BU/BU/BU/-/- | BU/BU/U/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- |
| rd_proiect | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | -/BU/BU/-/- | -/BU/BU/-/- | -/BU/-/-/- | -/BU/BU*/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU**/-/-/- |
| rd_livrabil | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | -/BU/BU/-/- | BU/BU/BU/-/- | -/BU/BU***/-/- | -/BU/-/-/- | -/BU/BU***/-/- | -/BU/BU***/-/- | -/BU/-/-/- | -/BU/BU***/-/- | -/-/-/-/- |
| rd_etapa | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | -/BU/BU/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- |
| rd_blocaj | BU/BU/BU/BU/BU | BU/BU/BU/BU/BU | BU/BU/BU/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_referinta | BU/BU/BU/BU/BU | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- |

`*` Comercial Manager scrie numai in coloanele de suprascriere a scorului (11.5).
`**` Cititorul companiei vede numai coloanele publice (11.5).
`***` Fiecare rol scrie numai livrabilele al caror `rd_rolresponsabil` este propriul rol.

### 11.4.2 Tabelele de executie tehnica

| Tabela | RD Head | RD Manager | RD Tehnolog | RD Suport | KAM | Achizitii | Calitate | Productie | Cititor |
|---|---|---|---|---|---|---|---|---|---|
| rd_fisatestare | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_trial | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_masuratoare | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | BU/BU/U/-/- | -/-/-/-/- |
| rd_statisticatrial | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_evaluaresenzoriala | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_scorsenzorial | BU/BU/BU/BU/- | BU/BU/U/-/- | BU/BU/U/-/- | BU/BU/U/-/- | BU/BU/U/-/- | -/-/-/-/- | BU/BU/U/-/- | BU/BU/U/-/- | -/-/-/-/- |
| rd_defectconstatat | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- |
| rd_reteta | BU/BU/BU/BU/BU | BU/BU/BU/-/BU | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_versiunereteta | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_liniereteta | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_antecalcul | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- |
| rd_linieantecalcul | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- |

11.4.2.1 Antecalculul si liniile lui nu sunt vizibile KAM-ului, Productiei si companiei.
Costul si marja sunt informatie sensibila; expunerea lor catre comercial schimba
negocierea interna, iar catre productie nu aduce nimic.

### 11.4.3 Tabelele de materii prime si mostre

| Tabela | RD Head | RD Manager | RD Tehnolog | RD Suport | KAM | Achizitii | Calitate | Cititor |
|---|---|---|---|---|---|---|---|---|
| rd_mpproiect | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | BU/BU/BU/-/- | -/BU/BU*/-/- | -/-/-/-/- |
| rd_iteratiefurnizor | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | BU/BU/BU/-/- | -/BU/BU*/-/- | -/-/-/-/- |
| rd_materieprima | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- |
| rd_furnizor | BU/BU/BU/BU/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- | BU/BU/BU/-/- | -/BU/BU*/-/- | -/-/-/-/- |
| rd_ceremostra | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/U/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_miscaremostra | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- |

`*` Calitatea scrie numai coloanele de aprobare (aprobat, data aprobarii, alergeni).

### 11.4.4 Tabelele de specificatii si implementare

| Tabela | RD Head | RD Manager | RD Tehnolog | RD Suport | Calitate | Planificare | Productie | Cititor |
|---|---|---|---|---|---|---|---|---|
| rd_specificatie | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | BU/BU/BU/BU/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_sdp | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_eticheta | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/BU*/-/- | -/-/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_implementare | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/BU/BU*/-/- | -/BU/BU*/-/- | -/BU/BU*/-/- | -/-/-/-/- |
| rd_productie0 | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/BU/BU*/-/- | -/BU/-/-/- | BU/BU/BU/-/- | -/-/-/-/- |
| rd_inregistrareprod0 | BU/BU/BU/BU/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | BU/BU/BU/-/- | -/-/-/-/- | BU/BU/BU/-/- | -/-/-/-/- |
| rd_revizuire | BU/BU/BU/BU/- | BU/BU/BU/-/- | -/BU/BU/-/- | -/BU/-/-/- | -/BU/BU*/-/- | -/BU/-/-/- | -/BU/BU*/-/- | -/-/-/-/- |

`*` Fiecare rol scrie numai campurile care ii revin (bifele proprii, feedbackul propriu).

### 11.4.5 Nomenclatoare si configurare

| Tabela | RD Head | RD Administrator | RD Manager | Comercial Mgr | Achizitii | Calitate | Toti ceilalti |
|---|---|---|---|---|---|---|---|
| rd_linie | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/BU/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- |
| rd_client | BU/BU/BU/-/- | BU/BU/BU/BU/- | -/BU/-/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- |
| rd_profiltehnolog | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- |
| rd_sablonlivrabil | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/-/-/-/- |
| rd_sablonetapa | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- |
| rd_criteriusenzorial | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- |
| rd_defect | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/BU/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/BU/-/- | -/BU/-/-/- |
| rd_motiv | BU/BU/BU/BU/- | BU/BU/BU/BU/- | BU/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- |
| rd_tipdocument | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/BU/-/-/- | -/BU/-/-/- |
| rd_alergen | BU/BU/BU/-/- | BU/BU/BU/-/- | -/BU/-/-/- | -/-/-/-/- | -/BU/-/-/- | BU/BU/BU/-/- | -/BU/-/-/- |
| rd_indicator | BU/BU/BU/BU/- | BU/BU/BU/BU/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- |
| rd_masurareindicator | BU/BU/BU/BU/- | -/BU/-/-/- | -/BU/-/-/- | -/BU/-/-/- | -/-/-/-/- | -/-/-/-/- | -/-/-/-/- |

## 11.5 Securitatea pe coloana

Se folosesc profiluri de securitate pe coloana (Column Security Profiles) pentru
informatia care nu trebuie sa ajunga la toata lumea care are drept de citire pe tabela.

| Coloana | Tabela | Cine citeste | Cine scrie | Motiv |
|---|---|---|---|---|
| rd_scorsuprascris | rd_proiect | RD Head, RD Manager, Comercial Mgr | Comercial Mgr | Suprascrierea este a comercialului, dar trebuie vazuta de R&D |
| rd_motivsuprascriere | rd_proiect | Idem | Comercial Mgr | Idem |
| rd_costtotal, rd_marja | rd_antecalcul | RD Head, RD Manager, RD Tehnolog | RD Tehnolog | Cost si marja |
| rd_pret | rd_materieprima | RD Head, RD Manager, RD Tehnolog, Achizitii | Achizitii | Pret de achizitie |
| rd_pret | rd_iteratiefurnizor | Idem | Achizitii | Idem |
| rd_prettinta | rd_antecalcul | RD Head, RD Manager, KAM, Comercial Mgr | KAM | Pretul negociat cu clientul |
| rd_clasificare | rd_client | Toti cei cu citire pe client | Comercial Mgr, RD Head | Clasificarea A/B/C se stabileste de Sales |
| rd_capacitatemax, rd_incarcare | rd_profiltehnolog | RD Head, RD Manager | RD Head | Datele de incarcare individuala nu se expun companiei |

11.5.1 Coloanele publice pentru ROL-11 (Cititor companie) pe `rd_proiect` sunt exact
acestea: cod proiect, nume produs, client, status, termen negociat, tehnolog alocat,
linie, urmatorul livrabil, data ultimei activitati. Restul coloanelor sunt ascunse prin
profil de securitate pe coloana. Aceasta este implementarea concreta a cerintei
"vizibil pentru toata compania, read-only".

11.5.2 NOTA de platforma: securitatea pe coloana se aplica si in Power BI si in exportul
in Excel, dar NU se aplica in fluxurile Power Automate care ruleaza cu o conexiune de
serviciu. Fluxurile care trimit notificari catre roluri largi nu trebuie sa includa in
corpul mesajului coloane protejate. Este cea mai frecventa scurgere de informatie
sensibila intr-o solutie Power Platform.

## 11.6 Documentele in SharePoint

11.6.1 Permisiunile de SharePoint se administreaza separat de cele Dataverse. Structura:

| Grup SharePoint | Membri | Drept pe biblioteca `PRODUSE IN DEZVOLTARE` |
|---|---|---|
| RD Proprietari | Head of R&D, Manager R&D | Control complet |
| RD Contribuitori | Tehnologi, suport R&D | Editare |
| Calitate | Managementul calitatii | Editare pe folderele 05, 06, 07; citire pe restul |
| Achizitii | Achizitii | Editare pe folderele 01, 03; citire pe restul |
| Productie si Planificare | Sefi de linie, planificare | Citire pe folderele 07, 08 |
| Comercial | KAM, manager vanzari | Citire pe folderele 00, 03, 08 |
| Toata compania | Toti | Fara acces la biblioteca |

11.6.2 Compania nu primeste acces la biblioteca de documente. Vede statusul in aplicatie;
documentele contin costuri, retete si specificatii, care sunt cel mai valoros activ
tehnic al firmei.

11.6.3 Fisierele marcate `Confidential = Da` (retete complete, antecalcule, ST-uri de
client cu clauza de confidentialitate) primesc permisiuni unice, restranse la RD
Proprietari, RD Contribuitori si Calitate. Se aplica de FLX-19 la incarcare.

11.6.4 NOTA: permisiunile unice pe fisier sunt costisitoare in SharePoint si greu de
intretinut la scara. Se folosesc numai pentru fisierele marcate confidential, nu ca
mecanism general - restul se rezolva prin permisiuni pe folder, mostenite.

## 11.7 Reguli generale de securitate

11.7.1 **Nimeni nu are drept de stergere pe tabelele de proces**, in afara RD Head si RD
Administrator. Inregistrarile gresite se dezactiveaza sau se marcheaza cu status
`Anulat`. Motiv: intr-un mediu certificat, stergerea unei inregistrari este un risc de
audit mai mare decat prezenta unei inregistrari gresite si marcate ca atare.

11.7.2 **Atribuirea (Assign) este limitata la RD Head si RD Manager.** Reatribuirea unui
proiect muta toti copiii lui, prin comportamentul parental, si nu trebuie sa fie o
operatie de rutina.

11.7.3 **Rolul de administrator de sistem nu se da nimanui in afara Head of R&D.** Rolul
RD Administrator, mai restrans, acopera intretinerea curenta a nomenclatoarelor si a
sabloanelor.

11.7.4 **Rolul RD Auditor** (ROL-12) se creeaza dinainte, cu drept de citire pe toate
tabelele plus drept de citire pe jurnalul de audit, si se atribuie numai pe durata
auditului. Nu se creeaza in graba, in dimineata auditului.

11.7.5 Conturile din aplicatia canvas folosite in hala: fiecare tehnolog si sef de tura
are cont nominal. Nu se folosesc conturi partajate de dispozitiv. Motiv: toate
inregistrarile de masuratori si de productie 0 trebuie sa aiba autor identificabil, altfel
nu au valoare la audit.

11.7.6 NOTA: cerinta "datele nu parasesc tenantul companiei" se respecta prin: mediu
Dataverse in regiunea tenantului; conectori limitati prin politica DLP la Microsoft 365 si
Dataverse; interdictia conectorilor de tip social, storage extern si servicii AI publice;
si absenta oricarei integrari externe in aceasta solutie. Politica DLP se defineste
inainte de Val 1, nu dupa.


<!-- ==================== S12-automatizari.md ==================== -->

---

# Sectiunea 12 - Automatizari

## 12.1 Principii

12.1.1 Toate fluxurile sunt solution-aware, in Solution `RDSuitaDigitala`, si folosesc
referinte de conexiune (connection references) si variabile de mediu (environment
variables). Fara acestea, exportul in productie cere reconfigurarea manuala a fiecarui
flux.

12.1.2 Parametrii de business (ponderile scorului, pragurile, duratele implicite, adresa
site-ului SharePoint) stau in variabile de mediu sau in nomenclatoare, niciodata
codificati in flux. Motiv: schimbarea unei ponderi nu trebuie sa insemne editarea si
retestarea unui flux.

12.1.3 Fiecare flux are tratare de eroare: scope `Try / Catch`, iar in catch o notificare
catre Head of R&D cu numele fluxului, inregistrarea afectata si mesajul de eroare. Un flux
esuat tacit este mai rau decat un flux care nu exista.

12.1.4 Fluxurile care modifica multe inregistrari se ruleaza cu concurenta limitata la 1,
pentru a nu declansa limitarea de API a Dataverse.

## 12.2 Lista fluxurilor

| Cod | Flux | Tip | Val |
|---|---|---|---|
| FLX-01 | Generarea codului de proiect si a inregistrarii la acceptare | Automat (la modificare) | 1 |
| FLX-02 | Generarea arborelui de foldere SharePoint | Automat | 1 |
| FLX-03 | Propunerea datei estimate de finalizare | Automat + la cerere | 1 |
| FLX-04 | Crearea proiectului-copil cu mostenirea referintelor | La cerere | 2 |
| FLX-05 | Generarea si reevaluarea livrabilelor din sablon | Automat | 1 |
| FLX-06 | Recalcularea incarcarii pe tehnolog si pe linie | Programat (orar) | 1 |
| FLX-07 | Recalcularea la modificarea unui ETA | Automat | 2 |
| FLX-08 | Alerte de termen (3 zile inainte si la depasire) | Programat (zilnic) | 1 |
| FLX-09 | Calculul impactului blocajelor | Automat | 2 |
| FLX-10 | Recalcularea saptamanala a scorului de prioritate | Programat (saptamanal) | 2 |
| FLX-11 | Calculul statisticii de trial si al scorului senzorial | Automat | 1 |
| FLX-12 | Generarea documentelor din sabloane Word | La cerere | 2 |
| FLX-13 | Recalcularea alergenilor si a valorilor nutritionale | Automat | 3 |
| FLX-14 | Reintroducerea solicitarilor amanate in triaj | Programat (zilnic) | 1 |
| FLX-15 | Declansarea revizuirii post-implementare | Programat (zilnic) | 3 |
| FLX-16 | Calculul T-Total si al indicatorilor | Programat (zilnic si lunar) | 3 |
| FLX-17 | Propunerea de corectie a duratelor de etapa | Programat (lunar) | 3 |
| FLX-18 | Aprobarea planului si a antecalculului | Automat (aprobare) | 2 |
| FLX-19 | Gestionarea documentelor la incarcare si aprobare | Automat (SharePoint) | 2 |
| FLX-20 | Arhivarea jurnalului de audit | Programat (lunar) | 3 |
| FLX-21 | Alerte de materie prima si de furnizor | Programat (zilnic) | 2 |
| FLX-22 | Notificarea schimbarii de status a proiectului | Automat | 1 |

## 12.3 Detalierea fluxurilor

### FLX-01 Generarea codului de proiect si a inregistrarii la acceptare

| Element | Continut |
|---|---|
| Declansator | `rd_solicitare` modificata, filtru pe `rd_rezultattriaj` |
| Conditii | Rezultat = `Acceptata` SI `rd_proiect` este gol |
| Actiuni | 1. Creeaza `rd_proiect`, copiind client, KAM, produs, gramaj, ambalare, volum, referinta, cerinte. 2. Codul se genereaza prin Autonumber `{AA}{SEQ:000}`. 3. Seteaza status `Acceptat - planificat`, data acceptarii = azi. 4. Copiaza referinta de comparatie ca inregistrare `rd_referinta`. 5. Leaga solicitarea de proiect. 6. Apeleaza FLX-02, FLX-03 si FLX-05 (fluxuri copil) |
| Notificari | KAM: "Solicitarea a fost acceptata, cod proiect X". Tehnolog alocat: "Ti s-a alocat proiectul X" |
| Erori | Daca crearea proiectului esueaza, solicitarea revine in status `In triaj` si Managerul R&D este notificat |

12.3.1.1 NOTA: Autonumber Dataverse garanteaza unicitatea, dar nu garanteaza absenta
golurilor in serie - un import esuat consuma numere. Formatul `{AA}{SEQ:000}` (exemplu
26025) se reseteaza anual prin modificarea semintei la 1 ianuarie, operatiune manuala de
un minut, trecuta in procedura anuala. Nu exista resetare automata in platforma.

### FLX-02 Generarea arborelui de foldere

| Element | Continut |
|---|---|
| Declansator | Apelat de FLX-01, sau la cerere din butonul de pe formular |
| Actiuni | 1. Creeaza `/PRODUSE IN DEZVOLTARE/{an}/` daca nu exista. 2. Creeaza folderul de proiect `{cod}_{nume produs}`, cu numele curatat de caractere interzise. 3. Creeaza cele 10 subfoldere din 5.1.1. 4. Seteaza metadatele implicite pe folder. 5. Creeaza `SharePointDocumentLocation` catre folderul radacina. 6. Scrie URL-ul in `rd_folderurl` |
| Conditii | Nu ruleaza daca `rd_folderurl` este deja completat |
| Erori | Caracterele interzise in numele produsului (`" * : < > ? / \ |`) se inlocuiesc cu `-`; numele mai lung de 100 de caractere se trunchiaza |

### FLX-03 Propunerea datei estimate de finalizare

Regula de calcul este in Anexa A1, sectiunea A1.2. Fluxul:

| Element | Continut |
|---|---|
| Declansator | La acceptare (din FLX-01); la modificarea tehnologului sau a liniei; la cerere |
| Actiuni | 1. Citeste durata standard din sablonul de etape pentru tipul de proiect. 2. Aplica factorii de corectie din A1.2 (incarcarea tehnologului, coada pe linie, sezonalitatea, materiile prime noi). 3. Scrie `rd_termenpropus`. 4. Daca `rd_termennegociat` este gol, il precompleteaza cu valoarea propusa. 5. Genereaza datele de start si final planificate pe etape |
| Notificari | Manager R&D, la orice recalculare care muta termenul propus cu mai mult de 3 zile |
| Observatii | Termenul propus nu suprascrie niciodata termenul negociat. Negociatul se schimba numai manual |

### FLX-04 Crearea proiectului-copil

| Element | Continut |
|---|---|
| Declansator | Butonul `Creeaza proiect-copil` |
| Actiuni | 1. Creeaza `rd_proiect` cu `rd_proiectparinte` completat si sufixul urmator disponibil (.1, .2). 2. Copiaza client, KAM, linia, tipul, referinta, tehnologul. 3. Copiaza versiunea curenta de reteta ca versiune 1 a copilului, cu toate liniile. 4. Creeaza folderul ca subfolder al parintelui. 5. Genereaza livrabilele conform sablonului de tip `Abatere` (4.7). 6. Leaga documentele parintelui prin referinta, fara copiere fizica |
| Notificari | Tehnolog si KAM |

### FLX-05 Generarea si reevaluarea livrabilelor

| Element | Continut |
|---|---|
| Declansator | Apelat de FLX-01; automat la modificarea `rd_aremp`, `rd_tipproiect`, `rd_client`; zilnic pentru actualizarea campurilor derivate |
| Actiuni la generare | 1. Citeste sabloanele active filtrate pe tipul de proiect. 2. Evalueaza conditia de aplicabilitate din 4.2. 3. Creeaza cate o inregistrare `rd_livrabil` pentru fiecare, cu termen calculat conform 4.6.2. 4. Rezolva responsabilul din rol: tehnologul proiectului pentru rolul Tehnolog, KAM-ul pentru KAM, si asa mai departe din `rd_profiltehnolog` |
| Actiuni la reevaluare | 1. Adauga livrabilele nou aplicabile. 2. Trece in `Nu se aplica` livrabilele a caror conditie a devenit falsa (fara stergere). 3. Recalculeaza `rd_procentlivrabile` si `rd_livrabileok` pe proiect. 4. Scrie urmatorul livrabil scadent si responsabilul lui pe proiect |
| Notificari | La adaugarea de livrabile noi dupa generarea initiala: responsabilul si Managerul R&D |

### FLX-06 Recalcularea incarcarii

| Element | Continut |
|---|---|
| Declansator | Programat, la fiecare ora, in intervalul 06:00 - 20:00 |
| Actiuni | 1. Pentru fiecare `rd_profiltehnolog` activ: numara proiectele in statusuri active (4-9), numara cele in banda P1, calculeaza gradul de incarcare si seteaza semnalul. 2. Pentru fiecare `rd_linie` activa: numara proiectele active care o vizeaza. 3. Pentru fiecare `rd_client`: numara proiectele active |
| Observatii | Se ruleaza orar, nu la fiecare modificare, ca sa nu declanseze bucle de recalculare |

### FLX-07 Recalcularea la modificarea unui ETA

| Element | Continut |
|---|---|
| Declansator | `rd_mpproiect` modificata, filtru pe `rd_eta` |
| Conditii | ETA modificat SI materia prima este marcata critica |
| Actiuni | 1. Daca `rd_etainitial` este gol, il completeaza si iese. 2. Altfel incrementeaza `rd_modificarieta`. 3. Recalculeaza data estimata a proiectului: daca noul ETA depaseste data planificata a etapei de testare, muta termenul propus cu diferenta. 4. Scrie o inregistrare de blocaj daca intarzierea depaseste 5 zile lucratoare. 5. Actualizeaza etapele afectate |
| Notificari | KAM si tehnolog, obligatoriu, cu vechea si noua data si cu impactul asupra termenului. Manager R&D daca termenul catre client este depasit |

12.3.7.1 Aceasta este cea mai vizibila automatizare pentru comercial: astazi, o alunecare
de ETA la un furnizor se afla cu doua saptamani intarziere, prin telefon.

### FLX-08 Alerte de termen

| Element | Continut |
|---|---|
| Declansator | Programat, zilnic la 07:00 |
| Actiuni | 1. Livrabile cu termen peste 3 zile lucratoare, neincepute sau in lucru: notificare catre responsabil. 2. Livrabile cu termen depasit: notificare catre responsabil si Manager R&D, cu numarul de zile de intarziere; se scrie `rd_zileintarziere`. 3. Livrabile depasite cu peste 10 zile: escaladare catre Head of R&D. 4. Proiecte al caror termen negociat expira in 5 zile si care nu sunt in status de implementare: notificare catre tehnolog, Manager R&D si KAM |
| Observatii | O singura notificare pe zi pe persoana, cu toate elementele grupate. Nu se trimite cate un mail pe livrabil - este cel mai sigur mod de a face oamenii sa ignore alertele |

### FLX-09 Calculul impactului blocajelor

| Element | Continut |
|---|---|
| Declansator | `rd_blocaj` creata sau modificata; plus rulare zilnica pentru blocajele active |
| Actiuni | 1. Calculeaza zilele lucratoare intre start si sfarsit (sau azi, pentru cele active). 2. Scrie `rd_impactzile`. 3. Recalculeaza `rd_zileblocate` pe proiect si pe etapa. 4. La deschiderea unui blocaj cu `rd_oprsteceas`, trece proiectul in status `Blocat`, pastrand statusul anterior intr-un camp ascuns. 5. La inchiderea ultimului blocaj activ, readuce proiectul in statusul anterior |
| Notificari | La deschidere: Manager R&D si KAM. La 10 zile de blocaj activ: Head of R&D |

### FLX-10 Recalcularea scorului de prioritate

| Element | Continut |
|---|---|
| Declansator | Programat, luni la 06:00; plus la cerere din ECR-05 |
| Actiuni | Conform algoritmului din Anexa A1.1: calculeaza cele sase componente, adauga imbatranirea, aplica bugetul de urgenta, scrie `rd_scorprioritate` si `rd_banda`. Nu suprascrie proiectele cu `rd_scorsuprascris` completat |
| Notificari | Manager R&D si Comercial Manager: lista proiectelor care si-au schimbat banda in saptamana respectiva |
| Observatii | Se pastreaza istoricul scorului prin audit, ca sa se poata explica de ce un proiect a urcat |

### FLX-11 Statistica de trial si scorul senzorial

| Element | Continut |
|---|---|
| Declansator | `rd_masuratoare` creata sau modificata; `rd_scorsenzorial` creat sau modificat |
| Actiuni pentru masuratori | 1. Grupeaza masuratorile trialului pe tip, excluzand cele marcate excluse. 2. Calculeaza media, abaterea standard, CV, min, max, numarul de neconforme, conformitatea. 3. Creeaza sau actualizeaza `rd_statisticatrial`. 4. Seteaza verdictul conform 6.3.2 |
| Actiuni pentru senzorial | 1. Calculeaza media pe criteriu intre evaluatori, separat pentru produs si referinta. 2. Calculeaza scorul ponderat. 3. Calculeaza dezacordul maxim. 4. Aplica regula de verdict din 6.5.5 |
| Observatii | Se ruleaza cu o intarziere de 60 de secunde dupa ultima modificare, ca sa nu recalculeze de 20 de ori in timpul introducerii unui set de masuratori |

### FLX-12 Generarea documentelor din sabloane Word

| Element | Continut |
|---|---|
| Declansator | Butonul `Genereaza document`, cu alegerea sablonului |
| Actiuni | 1. Citeste sablonul din biblioteca `Sabloane` (fisier .docx cu content controls). 2. Citeste datele din Dataverse conform mapei documentului (5.5). 3. Populeaza sablonul cu actiunea Word Online `Populate a Microsoft Word template`. 4. Converteste in PDF. 5. Salveaza in folderul de faza corect, cu numele conform 5.2.1. 6. Scrie metadatele. 7. Leaga fisierul de livrabil |
| Sabloane | DOC-01 ... DOC-11 din 5.5, plus dosarul TDV |
| Erori | Sablon lipsa sau content control neregasit: notificare catre Head of R&D cu numele campului |

12.3.12.1 NOTA de platforma: actiunea `Populate a Microsoft Word template` are limitari
reale la tabele repetitive imbricate (un tabel in interiorul unui rand repetitiv). Dosarul
TDV, care contine mai multe astfel de structuri, se genereaza in doua etape: mai intai
sectiunile simple din sablon, apoi anexele ca fisiere separate, unite in PDF. Alternativa,
daca volumul o justifica, este un conector de generare de documente din AppSource, dar
acesta trebuie verificat inainte fata de politica DLP si de cerinta ca datele sa nu
paraseasca tenantul.

### FLX-13 Recalcularea alergenilor si a valorilor nutritionale

| Element | Continut |
|---|---|
| Declansator | `rd_liniereteta` creata, modificata sau stearsa; `rd_materieprima` modificata pe campurile nutritionale sau de alergeni; `rd_productie0` finalizata (pentru factorul de randament) |
| Actiuni | Conform algoritmului din 9.2. Pentru retetele nevalidate: recalculare directa. Pentru cele validate: nu se modifica nimic, se genereaza alerta de impact conform 9.5.2 |
| Notificari | Tehnolog, la recalculare. Calitate si Head of R&D, la alerta de impact, cu lista produselor afectate |

### FLX-14 Solicitari amanate

Programat zilnic: solicitarile cu `rd_amanatapanala` <= azi si status `Amanata` revin in
status `Trimisa` si reapar in lista de triaj, cu notificare catre Manager R&D si KAM.

### FLX-15 Declansarea revizuirii post-implementare

Detaliat in 8.6. Programat zilnic; creeaza inregistrarile de revizuire la 30, 60 si 90 de
zile de la `rd_dataimplementare`, precompleteaza datele automate, creeaza livrabilele si
trimite cererile de date catre departamentele responsabile.

### FLX-16 Calculul indicatorilor

| Element | Continut |
|---|---|
| Declansator | Programat: zilnic pentru campurile de pe proiect, lunar pentru `rd_masurareindicator` |
| Actiuni zilnice | Pe fiecare proiect activ: `rd_zilecoada`, `rd_ttotalnet`, `rd_abateretermen`, `rd_ultimaactivitate` |
| Actiuni lunare | Calculeaza T-Total, Q-Corect si Q-Complet conform Sectiunii 13, la nivel de activitate, rol si persoana, si creeaza inregistrarile de masurare |
| Notificari | Head of R&D: sinteza lunara |

### FLX-17 Propunerea de corectie a duratelor

Programat lunar, dupa acumularea a cel putin 20 de proiecte finalizate: calculeaza
mediana duratei reale nete pe fiecare etapa si scrie `rd_duratapropusa` in sablon.
**Nu modifica `rd_duratastandard`.** Detaliat in Sectiunea 14.

### FLX-18 Aprobarea planului si a antecalculului

| Element | Continut |
|---|---|
| Declansator | `rd_livrabil` trece in status `Trimis spre aprobare`, pentru LIV-06 si LIV-18; sau `rd_antecalcul` trece in `Trimis spre aprobare` |
| Actiuni | 1. Trimite o aprobare (Approvals) catre aprobatorul din livrabil. 2. La aprobare: status `Realizat`, data si aprobatorul completate; pentru antecalcul, status `Aprobat`. 3. La respingere: status `Respins`, cu motivul obligatoriu din raspuns, si notificare catre responsabil |
| Conditii speciale | Daca marja din antecalcul este sub pragul companiei (variabila de mediu), aprobarea se trimite in doua trepte: Manager R&D, apoi Head of R&D |
| Observatii | Se foloseste conectorul Approvals, nu mail cu link. Aprobarea trebuie sa fie trasabila si sa functioneze din Teams si din mobil |

### FLX-19 Gestionarea documentelor

| Element | Continut |
|---|---|
| Declansator | Fisier creat sau modificat in biblioteca `PRODUSE IN DEZVOLTARE` |
| Actiuni | 1. Extrage codul de proiect si tipul de document din numele fisierului. 2. Completeaza metadatele din 5.3 din inregistrarea de proiect. 3. Leaga fisierul de livrabilul corespunzator si trece livrabilul in `In lucru` daca era `Neinceput`. 4. La trecerea metadatei `Status document` in `Aprobat`: publica versiune majora, aplica blocarea conform 5.4.3, scrie data aprobarii in Dataverse. 5. Pentru fisierele marcate confidential: aplica permisiuni unice conform 11.6.3 |
| Erori | Nume de fisier neconform cu 5.2.1: fisierul ramane, dar se marcheaza `Neclasificat` si se notifica autorul cu formatul corect |

### FLX-20 Arhivarea jurnalului de audit

Programat lunar: exporta jurnalul de audit al tabelelor critice (proiect, reteta, versiune
de reteta, specificatie, eticheta, productie 0) in fisiere CSV, in biblioteca `Arhiva
audit R&D`, cu retentie de 10 ani. Motivul este in 5.6.3.3.

### FLX-21 Alerte de materie prima si de furnizor

Programat zilnic: materii prime critice cu ETA depasit si fara receptie; materii prime cu
ST-ul furnizorului mai vechi de 24 de luni; furnizori cu certificarea expirata sau care
expira in 60 de zile; materii prime blocate de Calitate care sunt folosite in retete
active. Notificari catre Achizitii si Calitate, grupate intr-un singur mesaj zilnic.

### FLX-22 Notificarea schimbarii de status

| Element | Continut |
|---|---|
| Declansator | `rd_proiect` modificata pe `rd_status` |
| Actiuni | Trimite notificarea catre destinatarii relevanti pentru fiecare tranzitie, cu link direct catre proiect |
| Destinatari pe tranzitie | Catre `In testare`: KAM. Catre `In asteptare materie prima` sau `Blocat`: KAM si Manager R&D. Catre `In implementare`: Productie, Planificare, Calitate. Catre `Productie 0`: Productie, Calitate, sef de linie. Catre `Finalizat`: KAM, comercial, Productie. Catre `Suspendat`, `Abandonat` sau `Respins`: KAM, Manager R&D, Comercial Manager |
| Observatii | Notificarile merg in Teams, nu doar pe mail. In Teams se citesc |

## 12.4 Ce nu se automatizeaza

12.4.1 Nu se automatizeaza: decizia de triaj, alocarea tehnologului, aprobarea
specificatiilor si a etichetelor, decizia de la productia 0, decizia de revizuire.
Sistemul propune, omul decide, si decizia se inregistreaza cu autor.

12.4.2 Nu se genereaza automat comenzi de achizitie si nu se scrie in SAP. Sistemul
semnaleaza ce trebuie comandat; comanda se plaseaza in sistemele existente.

12.4.3 NOTA: exista tentatia de a automatiza trecerile de status pe baza de conditii
("daca toate livrabilele fazei sunt gata, treci automat in faza urmatoare"). Se evita, cu
o singura exceptie: trecerea in `Blocat` si revenirea din ea, care sunt mecanice. In rest,
statusul este o declaratie de responsabilitate a tehnologului, nu o consecinta a bifelor;
automatizarea lui produce proiecte care avanseaza pe hartie fara sa avanseze in realitate.


<!-- ==================== S13-indicatori.md ==================== -->

---

# Sectiunea 13 - Indicatori si raportare

## 13.1 Cei trei indicatori

| Indicator | Ce masoara | Tinta |
|---|---|---|
| T-Total | Respectarea timpului | 95% |
| Q-Corect | Corectitudinea a ceea ce se livreaza | 98% |
| Q-Complet | Completitudinea a ceea ce se livreaza | 98% |

13.1.1 Tintele se seteaza in `rd_indicator` si sunt parametrizabile. Valorile de mai sus
sunt punctul de pornire recomandat: T-Total mai jos decat cele de calitate, pentru ca
timpul depinde partial de factori externi, in timp ce corectitudinea si completitudinea
depind aproape integral de R&D.

## 13.2 T-Total

### 13.2.1 Definitia

T-Total masoara procentul de activitati finalizate in termenul stabilit, dupa scaderea
timpului in care ceasul a fost oprit de blocaje externe.

```
Pentru fiecare activitate masurabila (livrabil sau etapa):

durata_bruta  = data_realizarii - data_inceperii              [zile lucratoare]
zile_blocate  = suma zilelor de blocaj activ cu rd_oprsteceas = Da,
                suprapuse peste intervalul activitatii
durata_neta   = durata_bruta - zile_blocate

termen_efectiv = termen_planificat + zile_blocate

la_termen = data_realizarii <= termen_efectiv

T-Total (%) = numar activitati la_termen / numar activitati finalizate * 100
```

13.2.2 Suprapunerea blocajelor se calculeaza pe intervale, nu prin insumare simpla. Doua
blocaje care se suprapun partial in timp contribuie cu reuniunea intervalelor lor, nu cu
suma zilelor. Aceasta este singura parte a calculului care se implementeaza gresit tipic
si care produce, dupa un an, indicatori peste 100%.

### 13.2.3 Oprirea ceasului

| Situatie | Ceas R&D | Termen catre client |
|---|---|---|
| Blocaj cu sursa Furnizor, Client, Calitate, Planificare, Productie, Achizitii, Extern reglementar | Oprit | Curge |
| Blocaj cu sursa Intern R&D | Curge | Curge |
| Status `In asteptare materie prima` | Oprit, daca exista blocaj activ deschis | Curge |
| Status `Suspendat` | Oprit | Se renegociaza; se raporteaza separat |
| Concediul tehnologului | Curge | Curge |

13.2.3.1 Concediul nu opreste ceasul. Este o problema de alocare a Managerului R&D, nu o
cauza externa. Daca ar opri ceasul, indicatorul ar deveni nefalsificabil.

13.2.3.2 Termenul catre client continua sa curga in orice situatie si se raporteaza
separat, ca `abatere fata de termenul negociat`. Aceasta este dubla masurare ceruta
explicit: R&D nu este penalizat pentru asteptarea unei mostre de la furnizor, dar compania
stie ca a livrat cu 12 zile intarziere catre client si de ce.

### 13.2.4 Nivelurile de masurare

| Nivel | Unitatea numarata | Cine il vede |
|---|---|---|
| Activitate | Fiecare livrabil si etapa finalizata | Manager R&D |
| Rol | Toate activitatile cu `rd_rolresponsabil` = rolul respectiv | Head of R&D |
| Persoana | Toate activitatile cu responsabilul = persoana | Persoana, Manager R&D, Head of R&D |
| Departament | Toate activitatile R&D | Head of R&D, conducere |

13.2.4.1 T-Total pe rol este cel mai util indicator dintre cele patru: arata daca
intarzierile vin din R&D, din Achizitii, din Calitate sau din Productie. Astazi aceasta
intrebare nu are raspuns cu cifre.

13.2.4.2 T-Total pe persoana se raporteaza persoanei si Managerului R&D, nu se afiseaza
public. Motiv: un indicator individual afisat public produce, in trei luni, declararea
selectiva a datelor de realizare, nu imbunatatirea performantei.

## 13.3 Q-Corect

### 13.3.1 Definitia

Q-Corect masoara procentul de livrabile acceptate din prima, fara respingere si fara
corectie ceruta de aprobator.

```
respins = livrabilul a trecut prin status Respins cel putin o data
          SAU documentul asociat a primit versiune noua dupa respingere

Q-Corect (%) = livrabile aprobate fara respingere / livrabile aprobate total * 100
```

13.3.2 Se numara numai livrabilele care au aprobator. Un livrabil fara aprobare nu poate
fi masurat pe corectitudine.

13.3.3 Componente suplimentare, care intra in Q-Corect cu pondere:

| Componenta | Pondere | Sursa |
|---|---|---|
| Livrabile aprobate din prima | 60% | Din statusul livrabilelor |
| Trialuri cu rezultat Reusit din prima incercare | 15% | Din TBL-15 |
| Masuratori conforme fata de toleranta declarata | 10% | Din TBL-16b |
| Verificari HACCP conforme la productia 0 | 10% | Din TBL-34 |
| Antecalcule aprobate fara revizuire | 5% | Din TBL-22 |

13.3.4 Argument pentru ponderare: un Q-Corect construit doar pe aprobari masoara cat de
indulgent este aprobatorul. Adaugand trialurile reusite din prima si conformitatea
masuratorilor, indicatorul masoara si calitatea tehnica, nu doar cea documentara.

## 13.4 Q-Complet

### 13.4.1 Definitia

Q-Complet masoara procentul de livrabile obligatorii si aplicabile care sunt realizate la
momentul inchiderii proiectului sau la data de raportare.

```
Q-Complet la inchidere (%) =
    livrabile obligatorii aplicabile realizate / livrabile obligatorii aplicabile * 100

Q-Complet in curs (%) =
    livrabile scadente si realizate / livrabile scadente * 100
```

13.4.2 Livrabilele marcate `Nu se aplica` de Managerul R&D nu intra la numitor, dar se
raporteaza separat: numarul de derogari pe proiect si pe an. Un numar mare de derogari
inseamna ca sablonul de livrabile nu corespunde realitatii si trebuie corectat, nu ca
oamenii sunt neglijenti.

13.4.3 Q-Complet la nivel de departament, calculat lunar pe proiectele finalizate in luna
respectiva, este indicatorul care raspunde direct la problema centralizatorului actual:
astazi nimeni nu poate spune cate dosare sunt complete fara sa le deschida unul cate unul.

## 13.5 Cum se calculeaza si cand

| Indicator | Frecventa | Flux | Ce se scrie |
|---|---|---|---|
| Campuri de proiect (zile in coada, T-Total net, abatere de termen) | Zilnic | FLX-16 | Coloane pe `rd_proiect` |
| T-Total, Q-Corect, Q-Complet pe activitate, rol, persoana | Lunar, in prima zi lucratoare | FLX-16 | Inregistrari in `rd_masurareindicator` |
| Sinteza trimestriala si anuala | Trimestrial, anual | FLX-16 | Idem, cu perioada corespunzatoare |

13.5.1 Masuratorile lunare se congeleaza: odata scrisa, o inregistrare de masurare nu se
recalculeaza. Motiv: altfel, o inregistrare corectata retroactiv in martie schimba
indicatorul din ianuarie, iar raportarea isi pierde credibilitatea.

## 13.6 Rapoartele

### 13.6.1 Lista rapoartelor

| Cod | Raport | Continut | Cine il vede | Frecventa |
|---|---|---|---|---|
| RAP-01 | Durata medie reala pe etapa | Mediana si media duratei nete pe fiecare etapa, comparata cu durata standard, pe ultimele 12 luni | Head of R&D, Manager R&D | Lunar |
| RAP-02 | Livrabilele care intarzie cel mai des | Top 10 livrabile dupa procentul de intarziere si dupa media zilelor de intarziere, cu rolul responsabil | Head of R&D, Manager R&D, sefii rolurilor implicate | Lunar |
| RAP-03 | Incarcarea pe tehnolog | Proiecte active, distributia pe benzi, gradul de incarcare, evolutie pe 12 luni | Manager R&D, Head of R&D | Saptamanal |
| RAP-04 | Coada pe linie | Proiecte pe fiecare linie, primul slot estimat, gradul de supraincarcare | Manager R&D, Planificare | Saptamanal |
| RAP-05 | Rata de acceptare a solicitarilor pe KAM | Solicitari trimise, acceptate, respinse, amanate, cu motivele; rata de acceptare | Head of R&D, Comercial Manager, fiecare KAM pentru el | Lunar |
| RAP-06 | Proiecte abandonate cu motive | Lista, cu motivul, faza in care s-au oprit si costul estimat al efortului pierdut | Head of R&D, conducere | Trimestrial |
| RAP-07 | T-Total pe rol si pe persoana | Cu detaliul zilelor blocate si al sursei blocajelor | Head of R&D | Lunar |
| RAP-08 | Q-Corect si Q-Complet | Pe departament, rol si persoana | Head of R&D | Lunar |
| RAP-09 | Blocaje pe sursa | Zile de blocaj cumulate pe sursa (furnizor, client, Calitate, Planificare), cu top 10 cauze | Head of R&D, conducere | Trimestrial |
| RAP-10 | Termen propus fata de negociat fata de realizat | Pe KAM si pe tehnolog | Head of R&D, Comercial Manager | Trimestrial |
| RAP-11 | Produse lansate si indicele de sanatate | Din revizuirea post-implementare | Head of R&D, conducere, comercial | Trimestrial |
| RAP-12 | Materii prime si furnizori | Lead time real fata de asumat, rata de respingere pe furnizor, numarul de modificari de ETA | Achizitii, Head of R&D | Lunar |
| RAP-13 | Portofoliu pe alergeni | Ce produse contin fiecare alergen | Calitate, R&D | La cerere |
| RAP-14 | Suprascrieri de prioritate | Cine, ce, de ce, cand | Head of R&D, conducere | Lunar |
| RAP-15 | Ce am invatat (anual) | Abateri de cost si de randament pe categorie si pe linie; corectii propuse pentru antecalcul | Head of R&D, conducere | Anual |

### 13.6.2 Unde traiesc rapoartele

| Tip de raport | Implementare | Motiv |
|---|---|---|
| RAP-03, RAP-04, si listele operationale | Vizualizari si tablouri de bord native Dataverse | Sunt liste filtrabile, nu au nevoie de Power BI; sunt disponibile in Val 1, fara licente suplimentare |
| RAP-01, RAP-02, RAP-05 ... RAP-15 | Power BI, cu conexiune la Dataverse | Cer agregari pe perioade, comparatii istorice si grafice |
| RAP-13 | Vizualizare Dataverse cu filtru pe Choice multi-select | Se cere ad-hoc, la audit sau la cerinta de client |

13.6.2.1 Raportarea este read-only, conform deciziei de arhitectura. Nicio actiune nu se
declanseaza dintr-un raport.

13.6.2.2 NOTA: raportarea in Power BI cere licente Pro pentru cei care publica si
consuma continut in spatii de lucru, sau capacitate dedicata. Pentru cei ~200 de cititori
din companie, ecranul public de status (ECR-04) este in aplicatia model-driven, nu in
Power BI, tocmai ca sa nu genereze cerinta de licentiere pentru toata firma.

## 13.7 Ce se face cu indicatorii

13.7.1 Indicatorii nu sunt scop in sine. Regula de folosire, scrisa in procedura:

| Indicator sub tinta | Prima intrebare | Actiune tipica |
|---|---|---|
| T-Total pe departament | Care rol si care etapa trag in jos? | Corectia duratelor standard (Sectiunea 14) sau realocarea |
| T-Total pe rol extern R&D | Care sursa de blocaj domina? | Discutie cu departamentul respectiv, cu RAP-09 pe masa |
| Q-Corect | Ce livrabile se resping cel mai des si de ce? | Sablon de document mai clar, sau instruire, sau aprobator prea vag |
| Q-Complet | Ce livrabile lipsesc sistematic la inchidere? | Sablonul cere ceva ce nu se face niciodata: se elimina sau se face obligatoriu real |

13.7.2 Un indicator care sta trei luni sub tinta fara actiune declarata este un indicator
care trebuie eliminat sau retintit. Se revizuiesc anual, impreuna cu ponderile de
prioritizare si cu duratele standard.


<!-- ==================== S14-durate-etape.md ==================== -->

---

# Sectiunea 14 - Duratele etapelor

## 14.1 Principiul

14.1.1 Duratele standard se seteaza **o singura data, la configurare**, pornind de la
durata de referinta de 2 saptamani pe proiect. Nu se ajusteaza ad-hoc, la fiecare proiect
care intarzie.

14.1.2 Sistemul masoara duratele reale de la primul proiect si, dupa 6-12 luni de date,
**propune** corectia sabloanelor. Propunerea nu se aplica automat.

14.1.3 Argument pentru propunere in loc de aplicare automata: o durata standard nu este
doar o masuratoare, ci si un angajament. Daca sistemul ridica automat durata etapei de
testare de la 3 la 5 zile pentru ca asa a fost realitatea, procesul se auto-justifica si
nimeni nu mai intreaba de ce a devenit mai lent. Corectia trebuie sa fie o decizie a Head
of R&D, luata cu datele in fata.

## 14.2 Duratele de pornire

Sablonul standard, pentru tipul `Produs nou`, pe 14 zile lucratoare. Etapele se pot
suprapune; suma duratelor este mai mare decat durata proiectului.

| Cod | Etapa | Durata standard (zile lucratoare) | Start (zi) | Rol responsabil |
|---|---|---|---|---|
| ETP-01 | Triaj si acceptare | 1 | 0 | Manager R&D |
| ETP-02 | Planificare si alocare | 2 | 1 | Manager R&D, Tehnolog |
| ETP-03 | Aprovizionare materii prime | 5 (paralel) | 2 | Achizitii |
| ETP-04 | Dezvoltare reteta si antecalcul | 4 | 2 | Tehnolog |
| ETP-05 | Testare si trialuri | 4 | 5 | Tehnolog |
| ETP-06 | Evaluare senzoriala si decizie | 1 | 9 | Tehnolog, panel |
| ETP-07 | Mostre catre client si feedback | 3 (paralel) | 10 | Suport R&D, KAM |
| ETP-08 | Specificatii si eticheta | 4 | 10 | Tehnolog, Calitate |
| ETP-09 | Pregatirea implementarii (IPN) | 2 | 15 | Tehnolog |
| ETP-10 | Productie 0 | 1 | 18 | Tehnolog, Productie |
| ETP-11 | Validare si dosar TDV | 2 | 19 | Manager R&D, Calitate |

14.2.1 Etapa ETP-03 (aprovizionare) ruleaza in paralel si nu prelungeste proiectul decat
daca depaseste momentul in care este nevoie de materie prima. Modelarea ei ca etapa
separata este necesara ca sa se poata masura si atribui intarzierea corect.

14.2.2 Termenul propus rezulta din durata totala a lantului critic (ETP-01, 02, 04, 05,
06, 08, 09, 10, 11 = 21 de zile calendaristice cu suprapuneri, adica 14 zile lucratoare
efective in cazul standard), ajustat cu factorii din Anexa A1.2.

14.2.3 Duratele pe celelalte tipuri de proiect, ca punct de pornire:

| Tip proiect | Durata standard totala | Etape eliminate |
|---|---|---|
| Produs nou | 14 zile lucratoare | - |
| Reformulare | 10 zile | ETP-07 scurtat |
| Abatere (.1) | 5 zile | ETP-02, ETP-03, ETP-08 partial |
| Transfer pe alta linie | 8 zile | ETP-04, ETP-08 |
| Optimizare cost | 12 zile | ETP-07 optional |
| Ambalaj nou | 8 zile | ETP-04, ETP-05, ETP-06 |

## 14.3 Mecanismul de masurare

14.3.1 Pentru fiecare etapa a fiecarui proiect se inregistreaza: data de start planificata
si reala, data de final planificata si reala, durata bruta, zilele de blocaj suprapuse, si
durata neta (TBL-05, coloanele `rd_duratabruta`, `rd_zileblocate`, `rd_duratanet`).

14.3.2 Durata **neta** este cea folosita pentru propunerea de corectie. Durata bruta
include asteptarea din cauze externe si ar duce la umflarea artificiala a standardelor.

14.3.3 Startul real al unei etape se inregistreaza la prima activitate reala pe ea
(crearea unui trial pentru ETP-05, salvarea primului scor senzorial pentru ETP-06), nu la
o bifa manuala. Motiv: bifele manuale de start se fac retroactiv, cu ochiul pe indicator.

## 14.4 Propunerea de corectie

### 14.4.1 Cand se face

FLX-17 ruleaza lunar si genereaza propuneri numai daca sunt indeplinite toate conditiile:

| Conditie | Valoare | Motiv |
|---|---|---|
| Numar de proiecte finalizate cu etapa masurata | minimum 20 | Sub 20 de observatii, mediana nu este stabila |
| Perioada acoperita | minimum 6 luni | Sa se prinda cel putin doua sezoane diferite |
| Abaterea propusa fata de standardul curent | minimum 20% | Sub 20%, corectia nu merita perturbarea |

### 14.4.2 Ce se propune

```
durata_propusa = MEDIANA(durata_neta a etapei, pe proiectele finalizate
                         in ultimele 12 luni, de acelasi tip de proiect)
```

14.4.2.1 Se foloseste mediana, nu media. Motiv: distributia duratelor reale are coada
lunga la dreapta (cateva proiecte care s-au tarat luni de zile), iar media ar fi trasa de
ele. Mediana descrie proiectul tipic, care este exact ce trebuie sa fie un standard.

14.4.2.2 Se calculeaza si percentila 80, afisata alaturi: "8 din 10 proiecte termina
aceasta etapa in cel mult X zile". Este cifra utila pentru a promite termene cu marja, nu
pentru a seta standardul.

### 14.4.3 Ce se afiseaza pentru comparatie

Ecranul `Calibrarea duratelor`, in zona de configurare, cu un rand pe etapa si pe tip de
proiect:

| Coloana | Continut |
|---|---|
| Etapa | Denumirea si codul |
| Tip proiect | Pentru care se face comparatia |
| Durata standard curenta | Valoarea din sablon |
| Numar de observatii | Cate proiecte au contribuit |
| Mediana duratei nete | Valoarea propusa |
| Percentila 80 | Pentru promisiuni cu marja |
| Minim si maxim | Sa se vada imprastierea |
| Abatere fata de standard | In zile si in procente |
| Tendinta ultimelor 3 luni | Sageata sus / jos / stabil |
| Actiune | Buton `Aplica propunerea` (numai Head of R&D) |

14.4.3.1 Ecranul afiseaza si un grafic simplu de distributie pe fiecare etapa: cate
proiecte au terminat in 1 zi, in 2 zile si asa mai departe. O distributie cu doua varfuri
(bimodala) semnaleaza ca etapa acopera de fapt doua situatii diferite si ca sablonul
trebuie despartit, nu recalibrat.

### 14.4.4 Aplicarea

| Pas | Ce se intampla |
|---|---|
| 1 | Head of R&D apasa `Aplica propunerea` pe o etapa |
| 2 | Sistemul cere confirmarea si un comentariu (de ce se schimba) |
| 3 | `rd_duratastandard` se actualizeaza in sablon; valoarea veche ramane in audit |
| 4 | Proiectele **existente** nu se recalculeaza. Numai cele acceptate de acum inainte folosesc noua durata |
| 5 | Se noteaza data schimbarii, ca sa se poata separa in rapoarte proiectele de dinainte si de dupa |

14.4.4.1 Pasul 4 este esential. Recalcularea retroactiva a termenelor ar rescrie
indicatorii istorici si ar face imposibila compararea anilor.

## 14.5 Ce se face cu abaterile mari

| Situatie constatata | Interpretare probabila | Actiune |
|---|---|---|
| Durata reala mult peste standard, constant | Standardul a fost optimist de la inceput | Se aplica propunerea |
| Durata reala mult peste standard, doar la un tehnolog | Problema de alocare sau de instruire, nu de standard | Nu se schimba standardul |
| Durata reala mult peste standard, doar in septembrie-decembrie | Sezonalitate | Se ajusteaza factorul de sezonalitate din A1.2.4, nu durata standard |
| Durata reala mult sub standard | Etapa se sare in practica, nu se face mai repede | Se verifica daca etapa mai are sens; poate ca livrabilele ei se fac in alta etapa |
| Imprastiere foarte mare (min 1 zi, max 40) | Etapa acopera doua procese diferite | Se desparte etapa in doua, pe tipuri de proiect diferite |

14.5.1 A patra situatie este cea mai frecventa in practica si cea mai periculoasa: o
etapa care se termina sistematic in jumatate din timpul standard nu inseamna, de obicei,
eficienta, ci ca cineva bifeaza finalul fara sa fi facut continutul. Se verifica intai
livrabilele etapei, apoi se ajusteaza durata.

## 14.6 Prima calibrare

14.6.1 Calendarul realist:

| Moment | Ce se intampla |
|---|---|
| Val 0 | Se seteaza duratele din 14.2, prin discutie cu Managerul R&D si tehnologii |
| Luna 1-6 | Se colecteaza date. Nu se schimba nimic |
| Luna 6 | Prima privire asupra ecranului de calibrare, fara aplicare. Se verifica daca datele au sens si daca startul si finalul etapelor se inregistreaza corect |
| Luna 9-12 | Prima calibrare reala, cu aplicarea propunerilor care indeplinesc conditiile din 14.4.1 |
| Anual | Revizuire, impreuna cu ponderile de prioritizare si cu tintele de indicatori |

14.6.2 NOTA: in primele 3 luni datele vor arata durate mai mari decat realitatea, pentru
ca oamenii inregistreaza cu intarziere si invata sistemul in acelasi timp in care il
folosesc. Aceasta perioada se exclude explicit din prima calibrare - se noteaza data de la
care datele sunt considerate valide si se filtreaza dupa ea.


<!-- ==================== S15-migrare.md ==================== -->

---

# Sectiunea 15 - Migrarea

## 15.1 Principiul

15.1.1 Se migreaza cat este nevoie ca sistemul nou sa fie utilizabil si ca istoricul sa
ramana consultabil. Nu se migreaza tot, si nu se curata tot.

15.1.2 Regula de departajare:

| Categorie | Ce se face |
|---|---|
| Nomenclatoare (linii, clienti, materii prime, furnizori, persoane) | Se importa complet si curat. Fara ele nu functioneaza nimic |
| Proiecte in curs la punerea in functiune | Se introduc integral, manual sau prin import, cu toate datele |
| Proiecte finalizate in ultimele 24 de luni | Se importa la nivel de antet, fara livrabile detaliate |
| Proiecte finalizate mai vechi de 24 de luni | Se importa doar ca lista, ca istoric consultabil |
| Proiecte respinse si abandonate | Se pastreaza integral, ca istoric consultabil, cu motiv |
| Documente | Raman in SharePoint, se reorganizeaza conform 5.1.3, nu se migreaza in alta parte |

## 15.2 Ordinea de import

Ordinea este obligatorie: fiecare pas depinde de cele dinainte.

| Pas | Ce se importa | Sursa | Volum estimat | Cine |
|---|---|---|---|---|
| 1 | Nomenclatoare fixe: alergeni, tipuri de documente, motive, unitati de masura, faze, roluri | Din blueprint, `data/nomenclatoare.json` | ~200 de randuri | Head of R&D |
| 2 | Linii de productie (9) cu capabilitati, gramaje, viteze, tarife | Discutie cu Productia si Planificarea | 9 randuri | Head of R&D |
| 3 | Persoane si profiluri de tehnolog | Entra ID + configurare manuala | ~30 de randuri | Head of R&D |
| 4 | Clienti, cu clasificarea A/B/C | Export SAP + clasificare de la Sales | 100-300 de randuri | Head of R&D + comercial |
| 5 | Furnizori | Export SAP | 100-200 de randuri | Achizitii |
| 6 | Catalog de materii prime, cu date nutritionale si alergeni | Export SAP pentru coduri si denumiri; ST-uri furnizor pentru restul | 500-1500 de randuri | Tehnolog + Calitate |
| 7 | Sabloane de etape si de livrabile | Din blueprint, `data/sablon-*.json` | ~60 de randuri | Head of R&D |
| 8 | Criterii senzoriale si defecte | Din blueprint | ~40 de randuri | Head of R&D |
| 9 | Proiecte istorice (antet) | Centralizatorul Excel F-PS-LID-10.01 | 300-500 de randuri | Suport R&D |
| 10 | Proiecte in curs (complet) | Centralizator + interviu cu tehnologii | 20-40 de randuri | Tehnologi |
| 11 | Reorganizarea folderelor SharePoint | Biblioteca existenta | Toate proiectele | Flux + Suport R&D |

15.2.1 Pasul 6 este cel mai costisitor si cel mai important. Fara date nutritionale si de
alergeni complete pe materiile prime, Sectiunea 9 nu functioneaza. Se face in doua
transe: intai materiile prime folosite in proiectele active si in produsele de volum mare
(tipic 150-250 de coduri, care acopera 90% din utilizare), apoi restul, treptat, pe masura
ce fiecare este folosita intr-un proiect nou.

15.2.2 PROPUNERE: se introduce o regula de completare la utilizare - o materie prima fara
date nutritionale complete nu poate fi adaugata intr-o linie de reteta; sistemul cere
completarea in acel moment. Motiv: migrarea completa a 1500 de coduri deodata nu se va
face niciodata; completarea la utilizare se face de la sine, in fluxul normal de lucru.

## 15.3 Ce se importa din centralizatorul Excel

### 15.3.1 Maparea coloanelor

| Coloana din centralizator | Camp tinta | Transformare |
|---|---|---|
| Cod proiect | rd_codproiect | Se importa ca valoare, nu prin Autonumber (vezi 15.3.2) |
| Nume produs | rd_numeprodus | Curatare de spatii si caractere |
| Client | rd_client | Potrivire dupa nume cu nomenclatorul; nepotrivirile se rezolva manual |
| An | Se deduce din cod | - |
| Tehnolog | rd_tehnolog | Potrivire dupa nume cu utilizatorii |
| KAM | rd_kam | Idem |
| Data deschiderii | rd_dataacceptare | - |
| Data finalizarii | rd_termenrealizat | - |
| Status | rd_status | Mapare pe cele 14 statusuri din 2.2.1 |
| Cele ~30 de coloane-bifa | rd_livrabil | Vezi 15.3.3 |
| Observatii | rd_observatii | Text liber, se importa ca atare |

15.3.2 Codul de proiect istoric se importa ca valoare in coloana Autonumber. Dataverse
permite scrierea explicita a unei valori de Autonumber la import; sementa se seteaza dupa
import la primul numar liber al anului curent. Se verifica dupa import ca nu exista
duplicate.

### 15.3.3 Ce se face cu cele 30 de bife

| Situatie | Decizie |
|---|---|
| Proiecte in curs | Se genereaza livrabilele complete din sablon, iar bifele existente se traduc in status `Realizat` pe livrabilul corespunzator, conform mapei din 4.5. Data realizarii ramane goala, cu observatia "importat, data necunoscuta" |
| Proiecte finalizate in ultimele 24 de luni | Nu se genereaza livrabile individuale. Se importa un camp text de sinteza cu bifele originale, pentru consultare, si `rd_procentlivrabile` calculat din numarul de bife |
| Proiecte mai vechi | Nici atat. Doar antetul si observatiile |

15.3.3.1 Argument: generarea a 30 de inregistrari de livrabil pentru 500 de proiecte
istorice inseamna 15.000 de inregistrari fara data, fara responsabil si fara document,
care ar polua toate rapoartele si toti indicatorii. Bifele istorice se pastreaza ca text,
lizibil, si atat.

15.3.3.2 Toate proiectele importate primesc un camp `rd_importat = Da` si sunt excluse
implicit din calculul indicatorilor. Se pot include explicit intr-un raport, cu filtru.

## 15.4 Curatarea datelor

### 15.4.1 Ce se curata inainte de import

| Problema tipica | Cum se rezolva |
|---|---|
| Acelasi client scris in 4 feluri | Deduplicare manuala inainte de import, cu tabel de corespondenta; se pastreaza denumirea din SAP ca referinta |
| Coduri de proiect duplicate sau lipsa | Se rezolva manual; codurile lipsa primesc un cod de forma `{AA}900+n`, marcat ca reconstituit |
| Date in formate diferite (text, numar serial Excel) | Normalizare la ISO in fisierul de import |
| Nume de tehnolog cu diacritice, prescurtari, initiale | Tabel de corespondenta manual, cu utilizatorii din Entra ID |
| Bife cu valori diverse (x, X, DA, 1, data) | Normalizare la Da / Nu |
| Randuri goale, subtotaluri, randuri de comentarii | Se elimina |
| Proiecte fara status | Se marcheaza `Abandonat` cu motivul `Status necunoscut la migrare` |

15.4.2 Curatarea se face **in Excel, inainte de import**, nu in Dataverse dupa. Motiv:
in Excel se vede tot deodata si se corecteaza in masa; in Dataverse fiecare corectie este
o inregistrare deschisa separat.

15.4.3 Se pastreaza fisierul original al centralizatorului, nemodificat, intr-o
biblioteca de arhiva, plus fisierul curatat folosit la import si un raport de import cu ce
a esuat. Fara acestea, la prima intrebare de audit despre un proiect din 2024 nu se mai
poate spune de unde vine informatia.

### 15.4.4 Ce se lasa in urma

| Element | Motiv |
|---|---|
| Coloanele de urmarire ad-hoc adaugate in timp in centralizator | Nu au definitie si nu se pot interpreta |
| Comentariile din celule | Nu se pot importa structurat; se pastreaza in fisierul arhivat |
| Formatarea conditionala si codurile de culoare | Semnificatia lor nu este documentata nicaieri |
| Foile de lucru auxiliare (calcule intermediare, liste vechi) | Se arhiveaza, nu se importa |
| Fisierele Excel de masuratori | Se arhiveaza. Datele istorice de masuratori nu se importa - vezi 15.4.5 |

15.4.5 Masuratorile istorice nu se importa. Argument in trei randuri: sunt in fisiere
neuniforme, fara tolerante declarate si fara legatura clara cu un trial anume, deci
statistica pe ele ar fi falsa. Fisierele raman in folderul `02_Testare` al proiectului,
consultabile. Datele reale incep de la punerea in functiune.

## 15.5 Proiectele in curs la punerea in functiune

15.5.1 Sunt tipic 20-40 de proiecte. Se trateaza individual, nu prin import automat.

| Pas | Actiune |
|---|---|
| 1 | Se inventariaza toate proiectele active, cu tehnologul lor, cu doua saptamani inainte de punerea in functiune |
| 2 | Fiecare tehnolog completeaza, pentru proiectele lui, un formular scurt: faza reala, ce livrabile sunt gata, ce materii prime asteapta, ce blocaje exista, termenul asumat catre client |
| 3 | Se creeaza inregistrarile de proiect, cu codul istoric pastrat |
| 4 | Se genereaza livrabilele din sablon si se marcheaza ca realizate cele deja facute |
| 5 | Se creeaza etapele, cu datele reale de start pentru cele incepute |
| 6 | Se creeaza blocajele active |
| 7 | Se leaga folderul SharePoint existent, reorganizat conform 5.1.3 |
| 8 | Tehnologul confirma ca inregistrarea reflecta realitatea |

15.5.2 Pasul 8 nu este formalitate. Un proiect migrat gresit produce, in prima luna,
convingerea ca "sistemul nou are date gresite", care este cea mai greu de dizolvat
rezistenta la schimbare.

15.5.3 Proiectele in curs se marcheaza `rd_importat = Da` si se exclud din indicatori
timp de 6 luni, pentru ca durata lor a inceput inainte de existenta sistemului.

15.5.4 Data punerii in functiune este o taietura neta: proiectele acceptate de la acea
data se deschid **numai** in sistem. Nu exista perioada de functionare in paralel a
centralizatorului Excel. Argument: functionarea in paralel garanteaza ca ambele sisteme
sunt incomplete si ca nimeni nu are incredere in niciunul; taietura neta forteaza
adoptarea, cu conditia ca migrarea proiectelor in curs sa fie facuta corect.

## 15.6 Proiectele respinse si abandonate

15.6.1 Se pastreaza **integral**, ca istoric consultabil, cu motiv. Nu se sterg si nu se
arhiveaza in afara sistemului.

15.6.2 Pentru cele istorice, unde motivul nu este inregistrat, se importa cu motivul
`Necunoscut, anterior migrarii`. Este mai onest decat sa se ghiceasca.

15.6.3 Se creeaza o vizualizare dedicata `Arhiva - proiecte respinse si abandonate`, cu
filtre pe an, client, KAM si motiv. Este sursa pentru RAP-06 si pentru intrebarea "am mai
incercat produsul asta?", care astazi se raspunde din memoria a doua-trei persoane.

## 15.7 Verificarea dupa migrare

| Verificare | Criteriu de trecere |
|---|---|
| Numar de proiecte importate | Egal cu numarul de randuri valide din centralizator |
| Coduri de proiect duplicate | Zero |
| Proiecte fara client | Zero |
| Proiecte fara status | Zero |
| Proiecte active fara tehnolog | Zero |
| Foldere SharePoint nelegate de un proiect | Se listeaza si se rezolva manual |
| Proiecte fara folder | Se listeaza; se creeaza folder gol pentru cele active |
| Materii prime folosite in proiecte active, fara date nutritionale | Se listeaza; se completeaza inainte de Val 3 |
| Fisiere in `99_Neclasificat` | Se listeaza; se clasifica in 30 de zile |
| Confirmarea tehnologilor pentru proiectele in curs | 100% |

15.7.1 Raportul de verificare se pastreaza semnat de Head of R&D. Este dovada de audit ca
tranzitia s-a facut controlat.


<!-- ==================== S16-roadmap.md ==================== -->

---

# Sectiunea 16 - Roadmap pe valuri

## 16.0 Ipoteze de efort

16.0.1 Efortul este exprimat in zile-om ale constructorului (Head of R&D), care
construieste singur, fara echipa IT. Se presupune o disponibilitate realista de 1-2 zile
pe saptamana pentru constructie, in paralel cu functia de baza.

16.0.2 Estimarile includ constructia, testarea proprie si documentarea. Nu includ timpul
celorlalti (introducerea datelor de nomenclator, instruirea, testarea de acceptanta).

## 16.1 Val 0 - Fundatia

**Durata**: 2-3 saptamani. **Efort**: 8-10 zile-om.

| Ce se livreaza | Detaliu |
|---|---|
| Mediul Developer | Mediu personal, cu Dataverse activat |
| Solution `RDSuitaDigitala` | Editor `RD Digital`, prefix `rd`, versiune 0.1 |
| Politica DLP | Conectori limitati la Microsoft 365 si Dataverse |
| Nomenclatoarele din blueprint | TBL-41 motive, TBL-42 tipuri de documente, TBL-27 alergeni, TBL-20a defecte, TBL-18 criterii senzoriale, TBL-36 linii, TBL-37 profiluri, Choice-uri globale |
| Tabelele create, populate in Val 1 | TBL-38 clienti, TBL-10 furnizori, TBL-09 materii prime - vezi 16.1.1 |
| Sabloanele | TBL-04 livrabile (43 de randuri), TBL-06 etape (11 randuri) |
| Rolurile de securitate | ROL-01 ... ROL-13, cu matricea din Sectiunea 11 |
| Echipele | Cele 6 echipe din 11.1.2 |
| Biblioteca SharePoint | `PRODUSE IN DEZVOLTARE` cu coloanele de metadate si setarile de versionare |
| Procedura de export | Export saptamanal pe OneDrive, cu conventia de denumire din 2.0.2 |

**Cine il foloseste**: numai constructorul. Nu se da acces nimanui.

**Cum se masoara ca a functionat**:
- Solutia se exporta si se importa intr-un al doilea mediu, fara erori.
- Toate nomenclatoarele contin date reale, nu de test.
- Un utilizator de test din fiecare rol vede exact ce trebuie sa vada si nimic in plus.

**Riscul principal**: tentatia de a sari peste roluri si de a le face "la sfarsit".
Retrofitarea securitatii intr-o solutie construita fara ea costa de trei ori mai mult.

16.1.1 **Linia de demarcatie fata de migrarea din Valul 1.** Valul 0 populeaza
nomenclatoarele care vin din blueprint si din discutia interna; pasii 4-6 din 15.2
(clienti, furnizori, materii prime) raman in Valul 1, ca parte a migrarii, pentru ca cer
extragere de date din SAP si depind de alti oameni. Tabelele se creeaza insa in Valul 0,
ca structura, pentru ca lookup-urile din Valul 1 sa aiba ce sa refere. Fara aceasta
separare, Valul 0 nu se termina in 2-3 saptamani si tot roadmap-ul aluneca.

## 16.2 Val 1 - MVP utilizabil (30 de zile)

**Durata**: 5-6 saptamani de la finalul Valului 0. **Efort**: 23-28 de zile-om.

| Ce se livreaza | Module | Detaliu |
|---|---|---|
| Solicitarea si triajul | M02, M03 | TBL-01, ECR-02, ECR-06, FLX-01 |
| Proiectul | M04 | TBL-02, ECR-01 cu filele Sinteza, Livrabile, Etape, Documente |
| Livrabilele si etapele | M05, M06 | TBL-03, TBL-05, FLX-05 |
| Documentele | M21 | Arborele de foldere, FLX-02, FLX-19, conventia de denumire |
| Termenul propus | M06 | FLX-03, cu factorii din A1.2 |
| Incarcarea si alocarea | M07 | FLX-06, ECR-03 partial |
| Testarea si masuratorile | M12 | TBL-14, TBL-15, TBL-16, TBL-16b, FLX-11, ECR-11 in canvas |
| Alertele | - | FLX-08, FLX-14, FLX-22, FLX-30 (digest consolidat) |
| **Gate-urile** | M26 | TBL-43 ... TBL-46, FLX-23. Vezi 22.8.2 |
| **Actiunile centralizate** | M27 | TBL-49, FLX-27. Vezi 22.8.3 |
| **Logul de erori** | - | TBL-59, plus alternate keys pe codurile de business (22.6) |
| Migrarea | M25 | Pasii 1-10 din 15.2 |

**Cine il foloseste**: echipa R&D completa (manager, tehnologi, suport) si KAM-ii pentru
SCP. Achizitiile si Calitatea au acces de citire.

**Cum se masoara ca a functionat**, la 30 de zile de la punerea in functiune:

| Criteriu | Tinta |
|---|---|
| Proiecte noi deschise exclusiv in sistem | 100% |
| SCP-uri completate direct de KAM (nu prin suport R&D) | peste 50% |
| Proiecte cu folder generat automat | 100% |
| Masuratori introduse pe telefon, nu in Excel | peste 70% din trialuri |
| Centralizatorul Excel actualizat in paralel | 0 (nu se mai actualizeaza) |
| Timp mediu de deschidere a unui proiect | sub 5 minute, de la SCP la folder generat |

16.2.1 Val 1 este singurul val cu termen ferm. Argument: o solutie construita de o
singura persoana, in paralel cu functia de baza, moare daca nu ajunge in mainile
utilizatorilor in prima luna. Tot ce nu incape in Val 1 se amana; nimic din Val 1 nu se
amana.

16.2.2 Ce **nu** intra in Val 1, desi ar parea necesar: prioritizarea automata (se
foloseste ordonarea manuala), materiile prime cu ciclu complet (se noteaza in text),
evaluarea senzoriala (ramane pe hartie o luna in plus), antecalculul (ramane in Excel).
Toate acestea functioneaza si azi fara sistem; livrabilele si termenele nu.

## 16.3 Val 2 - Operare completa (90 de zile)

**Durata**: 7-9 saptamani de la Val 1. **Efort**: 30-35 de zile-om.

| Ce se livreaza | Module | Detaliu |
|---|---|---|
| Materii prime si aprovizionare | M09 | TBL-07, TBL-08, TBL-09, TBL-10, ECR-07, FLX-07, FLX-21 |
| Mostre | M10 | TBL-12, TBL-13, ECR-13 |
| Blocaje | M11 | TBL-11, FLX-09 |
| Prioritizarea | M08 | FLX-10, ECR-05, A1.1 complet |
| Evaluarea senzoriala | M13 | TBL-17 - TBL-20, ECR-12 |
| Reteta si antecalcul | M14 | TBL-22 - TBL-26, ECR-08, ECR-09 |
| Specificatii si SDP | M16 | TBL-29, TBL-30 |
| Implementare si productie 0 | M18, M19 | TBL-32 - TBL-34, ECR-14 |
| Generarea documentelor | M21 | FLX-12, sabloanele Word DOC-01 ... DOC-09 |
| Aprobarile | - | FLX-18 |
| Ecranul public | M23 | ECR-04 |
| **Riscuri si probleme** | M28 | TBL-47, TBL-48, FLX-24, FLX-25 |
| **Jurnalul de decizii** | M29 | TBL-50 |
| **Lead time inteligent** | M09 | TBL-57, FLX-28 |

**Cine il foloseste**: toata compania. Achizitiile, Calitatea, Planificarea si Productia
devin utilizatori activi, nu doar cititori.

**Cum se masoara ca a functionat**, la 90 de zile:

| Criteriu | Tinta |
|---|---|
| ETA-uri introduse de Achizitii direct in sistem | peste 80% din materiile prime noi |
| Evaluari senzoriale facute in aplicatie | 100% |
| Blocaje inregistrate cu sursa si impact | 100% din proiectele intarziate |
| Productii 0 cu checklist complet | 100% |
| Antecalcule facute in sistem | peste 80% |
| Accesari ale ecranului public de utilizatori din afara R&D | peste 30 de persoane distincte pe luna |
| Q-Complet pe proiectele finalizate in luna | peste 90% |

16.3.1 Val 2 este valul care aduce celelalte departamente in sistem. Este si valul cu cel
mai mare risc de rezistenta: Achizitiile si Productia nu au cerut aceasta solutie.
Argumentul de vanzare pentru fiecare trebuie pregatit dinainte - pentru Achizitii,
scaparea de mailurile de urmarire; pentru Productie, IL-uri corecte si mai putine
surprize la lansare.

## 16.4 Val 3 - Maturitate (6 luni)

**Durata**: 10-12 saptamani de la Val 2. **Efort**: 28-33 de zile-om.

| Ce se livreaza | Module | Detaliu |
|---|---|---|
| Alergeni si valori nutritionale | M15 | TBL-27, calculul din 9.2, FLX-13, alerta de impact |
| Etichete | M17 | TBL-31, generarea listei de ingrediente |
| Revizuirea post-implementare | M20 | TBL-35, FLX-15, ECR-10 |
| Indicatorii | M22 | TBL-39, TBL-40, FLX-16 |
| Raportarea Power BI | M22 | RAP-01, RAP-02, RAP-05 ... RAP-15 |
| Calibrarea duratelor | M06 | FLX-17, ecranul din 14.4.3 |
| Arhivarea auditului | - | FLX-20 |
| Dosarul TDV generat automat | M21 | DOC-10, cu toate anexele |
| **Stabilizarea pe 3 loturi** | M30 | TBL-51, TBL-52, FLX-31, etapa ETP-12 |
| **Capabilitatea de proces** | M31 | TBL-53, FLX-32 |
| **Lectiile invatate** | M32 | TBL-54 ... TBL-56, FLX-26, FLX-33 ... FLX-35 |
| **Sanatatea proiectului in timp** | M33 | TBL-58, FLX-29 |

**Cine il foloseste**: Head of R&D si conducerea, pentru indicatori si rapoarte; Calitatea,
pentru alergeni si etichete.

**Cum se masoara ca a functionat**, la 6 luni:

| Criteriu | Tinta |
|---|---|
| T-Total calculat automat, fara interventie manuala | Da |
| Dosare TDV generate cu un click | 100% din proiectele finalizate |
| Alergeni calculati din reteta pentru produsele noi | 100% |
| Prima calibrare a duratelor, cu date reale | Efectuata |
| Timp de raspuns la o intrebare de audit despre un proiect | sub 5 minute |
| Revizuiri la 30 de zile efectuate la termen | peste 80% |

## 16.5 Val 4 - Client, calitate si furnizor (9-12 luni)

**Durata**: 8-10 saptamani de la Val 3. **Efort**: 18-22 de zile-om.

| Ce se livreaza | Module | Detaliu |
|---|---|---|
| Validare si feedback de client | M34 | `rd_validareclient`, `rd_feedbackclient` |
| Reclamatii | M35 | `rd_reclamatie`, legate de proiect si de lot |
| Neconformitati si CAPA | M36 | `rd_neconformitate`, `rd_capa`, cu evaluarea eficacitatii |
| Performanta furnizorilor | M37 | `rd_performantafurnizor`, `rd_incidentfurnizor`, scorecard din 23.6.3 |

**Criteriile de activare** sunt in A2.2. Valul 4 **nu incepe** daca ele nu sunt
indeplinite; se trece direct la intretinere si la consolidarea Valurilor 1-3.

**Cum se masoara**: reclamatiile se leaga de produsul si lotul care le-a generat, in peste
80% din cazuri; scorecardul de furnizor se foloseste efectiv in cel putin o negociere.

## 16.6 Val 5 - Cost real si beneficii (12-15 luni)

**Durata**: 8-10 saptamani de la Val 4. **Efort**: 18-22 de zile-om.

| Ce se livreaza | Module | Detaliu |
|---|---|---|
| Business case si buget de proiect | M38 | `rd_businesscase`, `rd_bugetproiect` |
| Cost real de productie | M39 | `rd_costproductie`, `rd_giveaway` |
| Realizarea beneficiilor | M40 | `rd_beneficiu`, la 3, 6, 12 si 24 de luni |
| Registrul de documente tehnice | M41 | `rd_documenttehnic`, cu ciclu de viata si harta de dependente (22.5.1) |

**Criteriul critic**: costul real pe produs, furnizat lunar de Controlling, demonstrat trei
luni la rand. Este intrebarea deschisa IQ-05. Fara el, jumatate din Valul 5 nu are date.

## 16.7 Ce ramane dupa Val 5

Tot ce este in Anexa A2, cu criteriile de activare corespunzatoare: predictie, simulare,
Copilot, sustenabilitate, cost extins, portofoliu, front-end de inovatie.

16.7.1 Regula din A2.5.2: **cel mult doua module pe an dupa Valul 5**, si numai daca
intretinerea celor existente nu a fost amanata.

## 16.8 Sinteza efortului

| Val | Durata | Efort (zile-om) | Cumulat | Tabele cumulate |
|---|---|---|---|---|
| Val 0 | 2-3 saptamani | 8-10 | 8-10 | 12 |
| Val 1 | 5-6 saptamani | 23-28 | 31-38 | 26 |
| Val 2 | 7-9 saptamani | 30-35 | 61-73 | 43 |
| Val 3 | 10-12 saptamani | 28-33 | 89-106 | 60 |
| Trecerea in productie | 2 saptamani | 5-8 | 94-114 | 60 |
| Val 4 | 8-10 saptamani | 18-22 | 112-136 | 66 |
| Val 5 | 8-10 saptamani | 18-22 | 130-158 | 73 |

16.8.1 **Ipoteza de disponibilitate, repetata pentru ca de ea depinde tot**: la 1.5 zile pe
saptamana, cele 130-158 de zile-om inseamna aproximativ 20 de luni pana la finalul Valului
5, nu 15. La 3 zile pe saptamana, aproximativ 11 luni.

16.8.2 Calendarul din titlurile de mai sus (9-12 luni pentru Val 4, 12-15 pentru Val 5)
presupune perioade de constructie concentrata in Valurile 0-1 si un ritm sustinut ulterior.
Este ipoteza cea mai fragila din tot blueprintul si trebuie confirmata explicit inainte de
start - intrebarea IQ-10.

16.8.3 **Punctul de oprire acceptabil.** Daca ritmul nu se poate sustine, solutia se poate
opri dupa Valul 3 si ramane completa si utila: acopera intreg procesul R&D de la SCP la
revizuire, cu gate-uri, riscuri, stabilizare si lectii. Valurile 4 si 5 adauga vederea
financiara si pe cea de client, care sunt valoroase, dar nu conditioneaza functionarea
zilnica. Aceasta este singura proprietate care conteaza intr-un plan executat de o singura
persoana: **sa fie util si daca se opreste la jumatate.**

## 16.9 Ce nu se schimba fata de planul initial

16.9.1 Valurile 0 si 1 raman neschimbate ca domeniu, in ciuda adaugirilor din sinteza.
Gate-urile si tabela de actiuni intra in Val 1 pentru ca sunt ieftine si pentru ca fara
ele modulele urmatoare ar construi fiecare propriul mecanism (22.8.2, 22.8.3). Nimic
altceva nu se adauga acolo.

16.9.2 Termenul ferm de 30 de zile pentru Valul 1 se mentine. Regula din 16.2.1 ramane:
tot ce nu incape se amana, nimic din Val 1 nu se amana.


<!-- ==================== S17-trecere-productie.md ==================== -->

---

# Sectiunea 17 - Trecerea in productie

## 17.1 Ce se cere concret de la IT

Lista de mai jos se transmite ca atare, ca cerere formala. Este scrisa astfel incat sa
poata fi evaluata de un IT care nu cunoaste Power Platform.

### 17.1.1 Medii

| Cerinta | Detaliu | Motiv |
|---|---|---|
| Mediu de productie Dataverse | Tip `Production`, cu baza de date Dataverse, in regiunea tenantului (Europa) | Aici traieste solutia finala |
| Mediu de test Dataverse | Tip `Sandbox`, cu baza de date, copie a productiei | Testarea importurilor inainte de productie |
| Mediul Developer existent | Ramane, ca mediu de constructie | Constructia continua dupa punerea in functiune |
| Grup de securitate pe mediu | Un grup Entra ID care controleaza cine are acces la mediul de productie | Fara el, toti utilizatorii tenantului apar in mediu |

17.1.1.1 Capacitate necesara, estimata pentru 3 ani de functionare:

| Resursa | Estimare | Baza de calcul |
|---|---|---|
| Dataverse Database | 3-5 GB | ~500 de proiecte pe an x ~2000 de inregistrari copil x ~2 KB, plus audit |
| Dataverse File | sub 1 GB | Numai imaginile din masuratori si evaluari; documentele stau in SharePoint |
| Dataverse Log (audit) | 2-4 GB | Auditul pe tabelele critice; vezi FLX-20 pentru arhivare |
| SharePoint | 50-150 GB | ~30 de fisiere pe proiect, medie 3 MB, plus versiuni |

17.1.1.2 NOTA: capacitatea de Log Dataverse este cea care creste cel mai imprevizibil si
este cea mai scumpa pe gigabyte. Se monitorizeaza lunar in primul an. FLX-20 (arhivarea in
SharePoint) exista tocmai pentru a permite scaderea retentiei de audit in Dataverse fara
pierderea informatiei.

### 17.1.2 Licente

| Rol | Licenta necesara | Numar estimat |
|---|---|---|
| Constructor (Head of R&D) | Power Apps Premium (per user) sau licenta care include Dataverse si conectori premium | 1 |
| Utilizatori care creeaza si modifica date (R&D, Achizitii, Calitate, Planificare, Productie, KAM) | Power Apps Premium (per user) | 25-35 |
| Cititori (restul companiei, ecranul public) | Vezi 17.1.2.1 | ~200 |
| Power Automate | Inclus in Power Apps Premium pentru fluxurile din contextul aplicatiei | - |
| Power BI | Power BI Pro pentru cei care publica si consuma rapoarte | 5-8 |

17.1.2.1 Accesul de citire pentru toata compania este punctul de decizie cel mai
costisitor. Trei variante, in ordinea recomandarii:

| Varianta | Cum | Cost | Observatii |
|---|---|---|---|
| A. Licenta per utilizator pentru toti | Power Apps Premium pentru ~200 de persoane | Cel mai mare | Nejustificabil pentru citire |
| B. Plan per aplicatie (per app) pentru ecranul public | O licenta ieftina, limitata la o singura aplicatie | Mediu | Recomandat; ecranul public este o aplicatie separata tocmai pentru asta |
| C. Publicarea statusului intr-o pagina SharePoint | Un flux exporta zilnic o lista de status intr-o lista SharePoint, vizibila tuturor | Zero suplimentar | Nu este in timp real; pierde filtrele; acceptabil daca varianta B este refuzata |

17.1.2.2 Se cere IT-ului o decizie explicita intre B si C **inainte de Val 2**, pentru ca
ECR-04 se construieste diferit in cele doua cazuri. Aceasta este si intrebarea deschisa
IQ-03 din Sectiunea 20.

### 17.1.3 Alte cerinte

| Cerinta | Detaliu |
|---|---|
| Site SharePoint dedicat | Site de tip Team, cu biblioteca `PRODUSE IN DEZVOLTARE` si biblioteca `Sabloane` |
| Politica DLP | Politica dedicata mediilor R&D, care permite Microsoft 365, Dataverse, Approvals si Teams, si blocheaza restul |
| Conturi de serviciu | Un cont de serviciu pentru conexiunile fluxurilor, cu licenta proprie, ca fluxurile sa nu depinda de contul unei persoane |
| Grupuri Entra ID | Sase grupuri, corespunzatoare echipelor din 11.1.2, intretinute de IT sau de HR |
| Backup si restaurare | Confirmarea politicii native de backup Dataverse (7 zile pentru Production) si a procedurii de restaurare |
| Mediu de test reimprospatat | Posibilitatea de a copia productia in sandbox, la cerere |

17.1.3.1 Contul de serviciu este cerinta cea mai des omisa si cea mai costisitoare cand
lipseste: daca fluxurile ruleaza pe contul personal al constructorului, plecarea sau
schimbarea parolei acelei persoane opreste intreaga automatizare. Se cere de la inceput.

## 17.2 Exportul si importul solutiei

### 17.2.1 Regulile de baza

| Regula | Motiv |
|---|---|
| Se lucreaza intr-o singura Solution, `RDSuitaDigitala` | O a doua solutie creeaza dependente greu de urmarit |
| Se exporta si `managed`, si `unmanaged` | Unmanaged pentru arhiva si pentru un eventual mediu de constructie nou; managed pentru test si productie |
| In test si productie se importa **numai managed** | Importul unmanaged in productie face imposibila dezinstalarea si stergerea componentelor |
| Versionarea solutiei | `major.minor.build.revision`, incrementat la fiecare export catre test |
| Referinte de conexiune si variabile de mediu | Obligatorii pentru toate fluxurile si conexiunile |
| Datele de nomenclator | Nu se exporta cu solutia; se muta separat, cu Configuration Migration Tool sau prin import Excel |

17.2.1.1 NOTA de platforma: componentele nesolutionate (vizualizari personale, aplicatii
canvas create in afara solutiei, fluxuri create direct in mediu) nu pleaca la export si
sunt cea mai frecventa cauza de "merge la mine, nu merge in productie". Regula: nimic nu
se creeaza in afara solutiei, de la prima zi.

### 17.2.2 Procedura de promovare

| Pas | Actiune | Mediu |
|---|---|---|
| 1 | Se incrementeaza versiunea solutiei | Developer |
| 2 | Export managed si unmanaged; se salveaza pe OneDrive cu conventia din 2.0.2 | Developer |
| 3 | Import managed in mediul de test | Test |
| 4 | Se configureaza referintele de conexiune si variabilele de mediu pentru test | Test |
| 5 | Se ruleaza lista de verificare din 17.3 | Test |
| 6 | Se muta datele de nomenclator, daca s-au schimbat | Test |
| 7 | La rezultat curat: import managed in productie | Productie |
| 8 | Se configureaza referintele de conexiune si variabilele de mediu pentru productie | Productie |
| 9 | Se activeaza fluxurile, in ordinea din 12.2 | Productie |
| 10 | Se verifica pe un proiect real, de la SCP la generarea folderului | Productie |
| 11 | Se noteaza in registrul de versiuni ce s-a livrat si cand | - |

17.2.2.1 Pasul 3 nu se sare niciodata, nici pentru "o modificare mica". Cele mai multe
incidente de productie in Power Platform vin din modificari considerate prea mici pentru a
merita un test.

### 17.2.3 Registrul de versiuni

Se tine un fisier simplu, in biblioteca `Sabloane`, cu: versiunea, data, ce contine, cine
a facut importul, si daca a fost nevoie de actiuni manuale dupa import. Este documentul pe
care il citeste prima data cineva care preia solutia.

## 17.3 Ce se testeaza inainte de punerea in functiune

### 17.3.1 Testare functionala

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 1 | KAM completeaza si trimite un SCP | Solicitarea apare in lista de triaj a Managerului R&D |
| 2 | Manager R&D accepta solicitarea | Se genereaza cod, proiect, folder cu 10 subfoldere, livrabile, etape si termen propus |
| 3 | Manager R&D respinge o solicitare fara motiv | Sistemul nu permite salvarea |
| 4 | Se aloca un tehnolog | Se vede incarcarea lui inainte de alocare; livrabilele lui se reatribuie |
| 5 | Se marcheaza o materie prima ca noua, dupa acceptare | Apar livrabilele conditionate C1, cu termene |
| 6 | Achizitiile schimba un ETA | Termenul propus se recalculeaza; KAM si tehnolog sunt notificati |
| 7 | Se introduc 10 masuratori de greutate pe telefon, offline | Se sincronizeaza la revenirea conexiunii; statistica se calculeaza corect |
| 8 | Se exclude o masuratoare fara motiv | Sistemul nu permite |
| 9 | Se face o evaluare senzoriala cu 3 evaluatori si dezacord de 3 puncte | Criteriul se marcheaza; verdictul nu poate fi `Acceptat` |
| 10 | Se deschide si se inchide un blocaj de 5 zile cu sursa Furnizor | Proiectul trece in `Blocat` si revine; zilele blocate se cumuleaza; T-Total se ajusteaza |
| 11 | Se deschide un blocaj cu sursa Intern R&D | Ceasul nu se opreste |
| 12 | Se incarca un document cu nume conform si unul neconform | Primul primeste metadate automat; al doilea se marcheaza `Neclasificat` si autorul e notificat |
| 13 | Se aproba o ST finala | Documentul se blocheaza; versiunea majora se publica; data aprobarii ajunge in Dataverse |
| 14 | Se incearca inchiderea unui proiect cu livrabile obligatorii nerealizate | Sistemul refuza si listeaza ce lipseste |
| 15 | Se genereaza dosarul TDV | PDF complet, cu toate sectiunile din 5.5.10 |
| 16 | Se schimba datele de alergeni ale unei materii prime folosite intr-o reteta validata | Nu se modifica nimic automat; se genereaza alerta de impact |
| 17 | Se creeaza un proiect-copil | Mosteneste referintele, reteta si legatura cu documentele parintelui |
| 18 | Se completeaza o productie 0 cu o neconformitate HACCP | Decizia `Validat` nu este disponibila |
| 19 | Se ruleaza recalcularea saptamanala a scorului | Benzile se actualizeaza; proiectele cu scor suprascris raman neatinse |
| 20 | Un KAM incearca sa promoveze un al treilea proiect in P1 | Sistemul cere retrogradarea altuia |

### 17.3.2 Testare de securitate

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 21 | Un utilizator cu rol Cititor deschide un proiect | Vede numai cele 9 coloane publice din 11.5.1 |
| 22 | Un KAM incearca sa deschida un antecalcul | Nu are acces |
| 23 | Un tehnolog incearca sa suprascrie un scor de prioritate | Campul nu este editabil |
| 24 | Un utilizator din Productie incearca sa stearga un trial | Nu are drept de stergere |
| 25 | Un utilizator din afara companiei este adaugat la mediu | Grupul de securitate pe mediu il blocheaza |
| 26 | Se verifica ce coloane apar in notificarile trimise de fluxuri | Nicio coloana protejata prin securitate pe coloana |
| 27 | Se incearca exportul in Excel de catre un rol restrans | Exportul respecta securitatea pe coloana |

### 17.3.3 Testare de performanta si volum

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 28 | Se incarca 500 de proiecte si 5000 de livrabile in mediul de test | Vizualizarile se deschid in sub 3 secunde |
| 29 | Biblioteca SharePoint depaseste 5000 de elemente | Vizualizarile filtrate functioneaza (coloane indexate) |
| 30 | Se ruleaza FLX-06 si FLX-10 pe volumul complet | Se termina fara limitare de API |
| 31 | Aplicatia canvas se deschide pe telefonul cel mai vechi din dotare | Sub 10 secunde pana la primul ecran utilizabil |
| 32 | Aplicatia canvas functioneaza in zona cu semnal slab din hala | Introducerea si salvarea locala functioneaza offline |

### 17.3.4 Testare de acceptanta cu utilizatorii

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 33 | Un KAM completeaza un SCP fara instruire, doar cu ecranul in fata | Reuseste in sub 10 minute |
| 34 | Un tehnolog introduce un set complet de masuratori cu manusi | Reuseste fara ajutor |
| 35 | Doua persoane din afara R&D gasesc statusul unui produs pe ecranul public | Sub 15 secunde fiecare |
| 36 | Un sef de tura completeaza checklistul de productie 0 | Reuseste fara ajutor |

17.3.4.1 Testele 33-36 sunt cele care decid daca solutia se foloseste sau nu. Se fac cu
oameni reali, nu cu constructorul care simuleaza. Un test picat aici inseamna reproiectarea
ecranului, nu instruire suplimentara.

## 17.4 Punerea in functiune

| Pas | Cand | Actiune |
|---|---|---|
| 1 | -2 saptamani | Inventarul proiectelor in curs (15.5) |
| 2 | -1 saptamana | Instruire: 2 ore pentru R&D, 1 ora pentru KAM, 30 de minute pentru celelalte roluri |
| 3 | -3 zile | Migrarea nomenclatoarelor si a proiectelor istorice in productie |
| 4 | -1 zi | Migrarea proiectelor in curs, cu confirmarea tehnologilor |
| 5 | Ziua 0 | Taietura neta: proiectele noi se deschid numai in sistem (15.5.4) |
| 6 | Zilele 1-10 | Prezenta zilnica a constructorului langa utilizatori, 30 de minute pe zi |
| 7 | Ziua 30 | Evaluarea criteriilor din 16.2 |

17.4.1 Se alege ca zi 0 o luni din prima jumatate a lunii, in afara varfului de
septembrie-decembrie. Punerea in functiune in sezonul de varf este cea mai sigura cale
catre respingerea solutiei.

## 17.5 Documentarea pentru preluare

Constrangerea din brief: solutia trebuie sa poata fi preluata de altcineva. Concret, se
pastreaza in biblioteca `Sabloane`, actualizate la fiecare val:

| Document | Continut |
|---|---|
| Acest blueprint | Sursa de adevar pentru arhitectura si decizii |
| Registrul de versiuni | Ce s-a livrat, cand, cu ce actiuni manuale |
| Lista fluxurilor | Cod, scop, declansator, conexiuni folosite, variabile de mediu |
| Lista variabilelor de mediu | Nume, tip, valoare in fiecare mediu, ce controleaza |
| Procedura de export si import | Pasii din 17.2.2, cu capturi de ecran |
| Procedura anuala | Resetarea semintei de Autonumber, revizuirea clasificarilor de client, revizuirea ponderilor si a duratelor |
| Lista de verificare de testare | Cele 36 de scenarii din 17.3 |
| Contactele | Cine raspunde pentru fiecare zona de business |

17.5.1 NOTA: documentatia se scrie in timpul constructiei, nu la sfarsit. Un blueprint
actualizat si un registru de versiuni tinut la zi sunt singura diferenta intre o solutie
preluabila si una care moare odata cu plecarea constructorului. Aceasta este si RSC-02 din
Sectiunea 18, riscul cel mai probabil al intregului proiect.


<!-- ==================== S18-riscuri.md ==================== -->

---

# Sectiunea 18 - Riscuri

Probabilitate si impact pe scala Mica / Medie / Mare. Riscurile sunt ordonate dupa
produsul celor doua, descrescator.

## 18.1 Registrul de riscuri

| Cod | Risc | Prob. | Impact | Masura |
|---|---|---|---|---|
| RSC-01 | **Mediul Developer**: solutia se construieste intr-un mediu personal, legat de licenta si de contul unei persoane. Mediul Developer poate fi dezactivat automat dupa o perioada de inactivitate, iar la plecarea persoanei dispare impreuna cu contul | Mare | Mare | Export saptamanal, managed si unmanaged, pe OneDrive **si** intr-o biblioteca SharePoint a companiei, nu doar pe OneDrive personal. Trecerea in mediu de productie real cel tarziu dupa Val 2, nu dupa Val 3. Cerere formala catre IT pentru mediu de productie inca din Val 0, chiar daca se foloseste mai tarziu |
| RSC-02 | **Dependenta de o singura persoana**: intreaga solutie este construita, cunoscuta si intretinuta de Head of R&D. Fara el, nimeni nu stie de ce o regula este cum este si cum se face o modificare | Mare | Mare | Blueprintul acesta, tinut la zi, este masura principala. In plus: registrul de versiuni; conturi de serviciu pentru fluxuri (17.1.3.1); un al doilea utilizator cu rol RD Administrator, instruit pe nomenclatoare si sabloane; documentarea in timpul constructiei, nu dupa |
| RSC-03 | **Rezistenta la schimbare a utilizatorilor**: tehnologii revin la Excel, mai ales sub presiune de timp; se creeaza evidenta paralela | Mare | Mare | Taietura neta la punerea in functiune (15.5.4); prezenta zilnica in primele 10 zile; ecrane cu numar minim de campuri; livrarea in Val 1 a ceea ce doare cel mai tare azi (livrabile si termene), nu a ceea ce este mai spectaculos; masurarea explicita a criteriului "centralizatorul Excel nu se mai actualizeaza" |
| RSC-04 | **Adoptarea SCP-ului de catre KAM**: KAM-ii continua sa trimita cereri pe mail, iar suportul R&D le introduce; SCP-ul in aplicatie ramane o formalitate | Mare | Medie | Varianta de rezerva ramane, dar se marcheaza explicit ca `Mail preluat de suport R&D` si se raporteaza lunar pe KAM (RAP-05); formularul SCP se proiecteaza sa se completeze in sub 10 minute (test 33 din 17.3.4); triajul se face numai pe SCP-uri din sistem, deci un mail nu produce niciodata un cod de proiect |
| RSC-05 | **Datele de materie prima incomplete**: catalogul nu are date nutritionale si de alergeni, deci Sectiunea 9 nu functioneaza si etichetele nu se pot genera | Mare | Medie | Completare la utilizare (15.2.2): o materie prima fara date complete nu poate intra intr-o linie de reteta; migrare in doua transe, incepand cu cele 150-250 de coduri care acopera 90% din utilizare; raport permanent de materii prime incomplete |
| RSC-06 | **Scorul de prioritate se erodeaza**: toti KAM-ii suprascriu totul in banda maxima si sistemul redevine "cine striga mai tare" | Medie | Mare | Buget de urgenta pe KAM (A1.1.10); expirarea automata a suprascrierilor la 90 de zile; raport lunar cu toate suprascrierile si autorii (RAP-14); dreptul de suprascriere limitat la un singur rol |
| RSC-07 | **Efortul de constructie depaseste disponibilitatea reala**: 78-98 de zile-om la 1-2 zile pe saptamana inseamna peste un an, nu 6 luni; proiectul se opreste la jumatate | Mare | Medie | Confirmarea explicita a disponibilitatii inainte de start (16.6.1); Val 1 cu domeniu strict limitat si termen ferm; tot ce nu incape se amana, nimic din Val 1 nu se amana; livrare in valuri care aduc valoare separat, astfel incat o oprire dupa Val 2 sa lase totusi o solutie utila |
| RSC-08 | **Costul licentelor pentru cititorii din companie**: accesul de citire pentru ~200 de persoane poate fi refuzat pe motive de cost, iar cerinta de vizibilitate pentru toata compania cade | Medie | Medie | Ecranul public construit ca aplicatie separata, tocmai pentru licentierea per aplicatie (17.1.2.1); varianta de rezerva C (export zilnic intr-o lista SharePoint) pregatita din proiectare; decizie ceruta de la IT inainte de Val 2 |
| RSC-09 | **Capacitatea Dataverse depasita**, mai ales pe Log: auditul creste imprevizibil si costa scump pe gigabyte | Medie | Medie | Audit activat selectiv, pe tabele si coloane, nu pe tot; auditul de citire numai unde e nevoie; FLX-20 arhiveaza in SharePoint, permitand retentie scurta in Dataverse; monitorizare lunara a capacitatii in primul an |
| RSC-10 | **Departamentele externe nu intra in sistem**: Achizitiile nu introduc ETA-uri, Calitatea nu aproba in aplicatie, Productia nu completeaza productia 0; sistemul ramane o unealta doar de R&D | Medie | Mare | Argument de vanzare pregatit separat pentru fiecare departament (16.3.1); ecrane dedicate, cu campurile lor separate vizual; masurarea explicita a adoptiei pe departament in criteriile Valului 2; escaladare catre conducere daca la 90 de zile ETA-urile nu se introduc |
| RSC-11 | **Aplicatia canvas nu functioneaza in hala**: semnal slab, telefoane vechi, manusi, ecrane greu de citit | Medie | Medie | Proiectare explicita pentru hala (10.2.1); mod offline cu coada de sincronizare; testare de acceptanta cu utilizatori reali, in hala, nu la birou (testele 31, 32, 34); pastrarea posibilitatii de a genera formularul pe hartie ca varianta de avarie |
| RSC-12 | **Datele migrate gresit erodeaza increderea**: proiectele in curs apar cu date incorecte in prima saptamana, iar concluzia devine "sistemul nou are date gresite" | Medie | Mare | Confirmarea individuala a fiecarui tehnolog pentru proiectele lui (15.5.1, pasul 8); excluderea proiectelor importate din indicatori (15.3.3.2); raport de verificare dupa migrare, semnat (15.7) |
| RSC-13 | **Modificarile in productie fara test**: "e o schimbare mica" duce la fluxuri oprite si formulare rupte | Medie | Medie | Procedura de promovare in 11 pasi, fara exceptii (17.2.2); mediu de test permanent; registrul de versiuni; nicio componenta creata in afara solutiei |
| RSC-14 | **Sablonul de livrabile nu corespunde realitatii**: prea multe derogari `Nu se aplica`, oamenii bifeaza formal ca sa treaca mai departe | Medie | Medie | Numarul de derogari se raporteaza explicit (13.4.2); revizuirea sablonului dupa primele 50 de proiecte; regula ca un livrabil derogat sistematic se elimina sau se face obligatoriu real |
| RSC-15 | **Automatizarea trecerilor de status ascunde realitatea**: proiectele avanseaza pe hartie fara sa avanseze in fapt | Mica | Mare | Statusul nu se automatizeaza, cu exceptia blocajelor (12.4.3); startul real al etapelor se inregistreaza din activitate reala, nu din bife (14.3.3) |
| RSC-16 | **Scurgere de informatie sensibila prin fluxuri**: securitatea pe coloana nu se aplica in Power Automate, iar o notificare include costul sau marja | Mica | Mare | Regula explicita: fluxurile nu includ in corpul mesajelor coloane protejate (11.5.2); verificare dedicata la testare (testul 26 din 17.3.2) |
| RSC-17 | **Generarea documentelor Word esueaza la structuri complexe**: dosarul TDV nu se poate genera dintr-un singur sablon | Mica | Medie | Generare in doua etape, cu anexe unite in PDF (12.3.12.1); dosarul TDV este in Val 3, deci exista timp pentru o alternativa; conector din AppSource ca varianta, verificat fata de politica DLP |
| RSC-18 | **Autonumber cu goluri sau resetare uitata**: codurile de proiect sar numere sau continua seria din anul precedent | Mica | Mica | Resetarea semintei la 1 ianuarie, trecuta in procedura anuala (12.3.1.1); verificarea duplicatelor dupa import; golurile in serie se accepta explicit, nu se corecteaza |
| RSC-19 | **Pierderea jurnalului de audit prin retentia mediului**, tacit, dupa perioada configurata | Mica | Mare | FLX-20, arhivare lunara in SharePoint cu retentie de 10 ani (5.6.3.3); verificarea explicita a setarii de retentie la trecerea in productie |
| RSC-20 | **Reteta validata se modifica tacit** la schimbarea datelor unei materii prime, iar eticheta livrata nu mai corespunde | Mica | Mare | Regula din 9.5.2: retetele validate nu se recalculeaza automat, se genereaza alerta de impact; versiunile validate se blocheaza (2.14.4) |

## 18.2 Riscurile care merita cea mai multa atentie

18.2.1 RSC-01, RSC-02 si RSC-03 sunt in acelasi timp cele mai probabile si cele mai grave.
Toate trei au aceeasi natura: solutia depinde de o singura persoana si de un mediu
personal, iar utilizatorii au o alternativa care functioneaza (Excelul).

18.2.2 Masura cu cel mai bun raport efort-beneficiu pentru toate trei este aceeasi:
livrarea rapida a Valului 1, cu domeniu strict limitat, urmata de trecerea intr-un mediu
de productie real. O solutie folosita zilnic de zece oameni intr-un mediu al companiei nu
mai poate fi abandonata; una construita perfect intr-un mediu personal, timp de un an,
poate disparea intr-o zi.

18.2.3 NOTA: riscul cel mai putin discutat in astfel de proiecte este cel de succes
partial - solutia functioneaza pentru R&D, dar celelalte departamente nu intra in ea
(RSC-10). Rezultatul este ca R&D face acum si munca de urmarire pe care o faceau altii,
prin telefon. Adoptia pe departament trebuie masurata explicit si escaladata, nu sperata.


<!-- ==================== S19-criterii-acceptanta.md ==================== -->

---

# Sectiunea 19 - Criterii de acceptanta

Lista verificabila, pe modul. Fiecare criteriu se verifica prin observatie directa in
aplicatie, nu prin declaratie. `Val` indica valul in care criteriul devine aplicabil.

## M01 Fundatie si nomenclatoare

| Cod | Criteriu | Val |
|---|---|---|
| CA-01 | Toate componentele sunt intr-o singura Solution, cu prefixul `rd` | 0 |
| CA-02 | Solutia se exporta si se importa intr-un mediu curat, fara erori | 0 |
| CA-03 | Toate cele 9 linii de productie exista, cu capabilitati, gramaje si viteze reale | 0 |
| CA-04 | Toate statusurile sunt Choice; nu exista niciun camp de status ca text liber | 0 |
| CA-05 | Toate fluxurile folosesc referinte de conexiune si variabile de mediu | 1 |
| CA-06 | Nicio componenta nu exista in afara solutiei | 0 |

## M02, M03 Solicitare si triaj

| Cod | Criteriu | Val |
|---|---|---|
| CA-07 | Un KAM completeaza si trimite un SCP fara ajutor, in sub 10 minute | 1 |
| CA-08 | Solicitarea nu se poate respinge sau amana fara motiv din nomenclator | 1 |
| CA-09 | Solicitarile venite pe mail se inregistreaza si se marcheaza explicit ca atare | 1 |
| CA-10 | O solicitare amanata reapare automat in triaj la data stabilita | 1 |
| CA-11 | Solicitarile respinse raman consultabile, cu motiv, dupa un an | 1 |

## M04 Proiect

| Cod | Criteriu | Val |
|---|---|---|
| CA-12 | Codul de proiect se genereaza automat, in formatul `{AA}{NNN}`, succesiv pe an | 1 |
| CA-13 | Codul nu se poate modifica dupa generare | 1 |
| CA-14 | Modificarea gramajului sau a dimensiunii pe un proiect avansat propune crearea unui proiect-copil | 2 |
| CA-15 | Proiectul-copil mosteneste client, KAM, referinta, linia si reteta parintelui | 2 |
| CA-16 | Fiecare status afiseaza data planificata, responsabilul, urmatorul livrabil si cine il datoreaza | 1 |
| CA-17 | Cele trei termene (propus, negociat, realizat) sunt inregistrate distinct si vizibile simultan | 1 |

## M05 Livrabile

| Cod | Criteriu | Val |
|---|---|---|
| CA-18 | La acceptare se genereaza automat livrabilele din sablon, filtrate pe tipul de proiect | 1 |
| CA-19 | Livrabilele conditionate de materie prima noua apar numai daca proiectul are MP noua, si apar si retroactiv daca conditia devine adevarata | 1 |
| CA-20 | Un livrabil devenit neaplicabil trece in `Nu se aplica` si ramane vizibil, nu se sterge | 1 |
| CA-21 | Un livrabil care necesita document nu poate trece in `Realizat` fara fisier atasat | 1 |
| CA-22 | Proiectul nu se poate inchide cu livrabile obligatorii aplicabile nerealizate; sistemul listeaza ce lipseste | 1 |
| CA-23 | Derogarea de la un livrabil obligatoriu este posibila numai pentru Managerul R&D, cu motiv, si apare in audit | 1 |
| CA-24 | Cele 22 de coloane-bifa din centralizatorul actual au corespondent identificabil in sablon | 1 |

## M06 Etape si durate

| Cod | Criteriu | Val |
|---|---|---|
| CA-25 | Etapele se genereaza cu date planificate la acceptarea proiectului | 1 |
| CA-26 | Startul real al unei etape se inregistreaza din activitate reala, nu dintr-o bifa | 1 |
| CA-27 | Durata neta exclude zilele de blocaj suprapuse | 2 |
| CA-28 | Ecranul de calibrare afiseaza mediana, percentila 80 si numarul de observatii pe etapa | 3 |
| CA-29 | Aplicarea unei corectii de durata nu modifica proiectele existente | 3 |

## M07 Alocare si incarcare

| Cod | Criteriu | Val |
|---|---|---|
| CA-30 | La alocare, managerul vede pentru fiecare tehnolog: proiecte active, cate sunt P1, gradul de incarcare | 1 |
| CA-31 | Pragurile de supraincarcare se semnaleaza vizual, verde / galben / rosu | 1 |
| CA-32 | Incarcarea pe fiecare linie de productie este vizibila la alocare | 1 |
| CA-33 | Sistemul propune o data estimata de finalizare la acceptare, calculata din durata, incarcare, coada pe linie, sezonalitate si materii prime noi | 1 |
| CA-34 | Termenul propus nu suprascrie niciodata termenul negociat | 1 |

## M08 Prioritizare

| Cod | Criteriu | Val |
|---|---|---|
| CA-35 | Scorul se calculeaza pe cele 6 componente, cu ponderi parametrizabile fara modificarea fluxului | 2 |
| CA-36 | Scorul se recalculeaza saptamanal, automat | 2 |
| CA-37 | Volumul se puncteaza pe benzi, nu liniar | 2 |
| CA-38 | Scorul creste cu timpul de asteptare, plafonat, si numai cat proiectul nu este in lucru | 2 |
| CA-39 | Un KAM nu poate avea simultan mai mult de 2 proiecte in banda maxima fara sa retrogradeze altul | 2 |
| CA-40 | Suprascrierea este posibila numai pentru rolul de manager operational / vanzari, cere motiv si apare in audit | 2 |
| CA-41 | Coada se vede si global, si pe fiecare dintre cele 9 linii, separat | 2 |
| CA-42 | Benzile P1-P4 sunt afisate ca atare, in toate vizualizarile de proiect | 2 |

## M09, M10 Materii prime si mostre

| Cod | Criteriu | Val |
|---|---|---|
| CA-43 | Fiecare materie prima de proiect este marcata ca existenta sau noua | 2 |
| CA-44 | Ciclul MP noua parcurge cele 11 statusuri, de la mostra ceruta la receptionata | 2 |
| CA-45 | Cererea de mostra poate fi initiata si de R&D, si de Achizitii | 2 |
| CA-46 | Lead time-ul implicit se completeaza din tip si este editabil de Achizitii | 2 |
| CA-47 | Modificarea unui ETA recalculeaza automat data estimata si notifica KAM-ul si tehnologul | 2 |
| CA-48 | Fiecare iteratie de furnizor se pastreaza, cu motivul respingerii | 2 |
| CA-49 | Receptia de mostra congelata cere temperatura si o inregistreaza | 2 |

## M11 Blocaje

| Cod | Criteriu | Val |
|---|---|---|
| CA-50 | Blocajul inregistreaza cine blocheaza, din ce data, pana cand si impactul in zile | 2 |
| CA-51 | Blocajul extern opreste ceasul T-Total al R&D | 2 |
| CA-52 | Termenul catre client continua sa curga in timpul blocajului si se raporteaza separat | 2 |
| CA-53 | Blocajul cu sursa `Intern R&D` nu opreste ceasul | 2 |

## M12, M13 Testare, masuratori, senzorial

| Cod | Criteriu | Val |
|---|---|---|
| CA-54 | Masuratorile se introduc pe telefon, la linie, cu maximum 3 atingeri pe bucata | 1 |
| CA-55 | Sistemul calculeaza automat media, abaterea standard, minimul, maximul si conformitatea | 1 |
| CA-56 | Conformitatea se evalueaza fata de toleranta declarata in fisa de testare | 1 |
| CA-57 | Sub dimensiunea minima de esantion, verdictul devine `Esantion insuficient` | 1 |
| CA-58 | O valoare nu se poate sterge; se exclude, cu motiv, si ramane vizibila | 1 |
| CA-59 | Valorile posibil aberante se semnaleaza vizual | 2 |
| CA-60 | Se pot atasa poze la masuratori si la defecte | 1 |
| CA-61 | Grila senzoriala afiseaza ancorele descriptive pentru 1, 3 si 5 pe ecran, la fiecare criteriu | 2 |
| CA-62 | Un scor de 1 sau 2 cere comentariu obligatoriu | 2 |
| CA-63 | Dezacordul de 3 puncte sau mai mult marcheaza criteriul si blocheaza verdictul `Acceptat` | 2 |
| CA-64 | Cand exista referinta, evaluarea se face comparativ, in aceeasi sesiune | 2 |
| CA-65 | Referinta de comparatie este obligatorie la deschiderea proiectului, cu optiunea explicita `Inexistenta` | 1 |
| CA-66 | Formularele Excel de masuratori nu se mai folosesc; fisierul se genereaza din date, la cerere | 1 |

## M14, M15 Reteta, antecalcul, alergeni

| Cod | Criteriu | Val |
|---|---|---|
| CA-67 | Suma liniilor de reteta este validata la 100 kg | 2 |
| CA-68 | O versiune de reteta validata nu se mai poate edita | 2 |
| CA-69 | Versiunea noua cere motivul modificarii | 2 |
| CA-70 | Antecalculul calculeaza costul pe kg si pe bucata si marja fata de pretul tinta | 2 |
| CA-71 | Alergenii se calculeaza din reteta, ca reuniune, nu se copiaza din ST-ul furnizorului | 3 |
| CA-72 | Valorile nutritionale se calculeaza din reteta, cu corectia de randament | 3 |
| CA-73 | Se poate raspunde cu un click la intrebarea "care materie prima aduce acest alergen" | 3 |
| CA-74 | Schimbarea datelor unei materii prime nu modifica automat o reteta validata; genereaza alerta de impact cu lista produselor afectate | 3 |
| CA-75 | O materie prima fara date nutritionale complete nu poate fi adaugata intr-o linie de reteta | 3 |

## M16, M17, M18, M19 Specificatii, etichete, implementare, productie 0

| Cod | Criteriu | Val |
|---|---|---|
| CA-76 | ST-urile au versiune, status si aprobator; ST-ul aprobat se blocheaza | 2 |
| CA-77 | Lista de ingrediente se genereaza din reteta, in ordine descrescatoare, cu alergenii evidentiati | 3 |
| CA-78 | Conditiile IPN sunt un checklist de 13 pozitii; statusul `Gata de productie 0` cere toate bifele | 2 |
| CA-79 | La productia 0 se inregistreaza randamentul, rebutul pe cauze, viteza reala, timpul de setup, parametrii reali si conformitatea HACCP | 2 |
| CA-80 | O neconformitate HACCP nerezolvata face imposibila decizia `Validat` | 2 |
| CA-81 | Decizia `Validat conditionat` cere lista de conditii cu responsabil si termen | 2 |
| CA-82 | Checklistul de productie 0 functioneaza offline, pe telefon | 2 |
| CA-83 | Diferentele constatate la productia 0 obliga la versiune noua de SDP inainte de inchiderea proiectului | 2 |

## M20 Revizuire post-implementare

| Cod | Criteriu | Val |
|---|---|---|
| CA-84 | Revizuirile la 30, 60 si 90 de zile se creeaza automat de la data implementarii | 3 |
| CA-85 | Campurile disponibile automat sunt precompletate; raman maximum 9 campuri manuale | 3 |
| CA-86 | Cererile de date pleaca automat catre Calitate, Productie, KAM si Controlling | 3 |
| CA-87 | Datele nefurnizate se marcheaza `Date indisponibile`, cu departamentul responsabil | 3 |
| CA-88 | Decizia `Optimizare` creeaza automat un proiect nou, legat de cel initial | 3 |
| CA-89 | O revizuire neefectuata dupa 30 de zile de la scadenta se inchide ca `Sarita` si apare in raportul anual | 3 |

## M21 Documente

| Cod | Criteriu | Val |
|---|---|---|
| CA-90 | La acceptare se genereaza automat arborele de 10 foldere, in formatul `{an}/{cod}_{nume produs}` | 1 |
| CA-91 | Fisierele generate primesc automat numele conform conventiei `{cod}_{tip}_{vNN}_{AAAALLZZ}` | 2 |
| CA-92 | Metadatele se completeaza automat la incarcare; utilizatorul nu completeaza 13 coloane | 1 |
| CA-93 | Coloanele Cod proiect, Tip document si Faza sunt indexate | 1 |
| CA-94 | Documentele aprobate se blocheaza si primesc versiune majora | 2 |
| CA-95 | Documentele proiectelor abandonate se pastreaza, mutate si marcate ca atare | 2 |
| CA-96 | Dosarul TDV se genereaza integral din date, cu un click | 3 |
| CA-97 | Un fisier cu nume neconform este acceptat, marcat `Neclasificat`, iar autorul este notificat cu formatul corect | 2 |

## M22, M23 Indicatori si vizibilitate

| Cod | Criteriu | Val |
|---|---|---|
| CA-98 | T-Total, Q-Corect si Q-Complet se calculeaza automat, la nivel de activitate, rol si persoana | 3 |
| CA-99 | T-Total exclude zilele de blocaj extern, prin reuniune de intervale, nu prin suma | 3 |
| CA-100 | Masuratorile lunare de indicatori nu se recalculeaza retroactiv | 3 |
| CA-101 | Proiectele importate sunt excluse implicit din indicatori | 1 |
| CA-102 | Cele 15 rapoarte din 13.6.1 exista si sunt accesibile rolurilor indicate | 3 |
| CA-103 | Statusul proiectelor este vizibil intregii companii, read-only | 2 |
| CA-104 | Doua persoane din afara R&D gasesc statusul unui produs pe ecranul public in sub 15 secunde, fara instruire | 2 |
| CA-105 | Cititorul companiei vede numai cele 9 coloane publice; costul si marja nu sunt accesibile | 2 |

## M24 Securitate

| Cod | Criteriu | Val |
|---|---|---|
| CA-106 | Matricea Rol x Tabela din Sectiunea 11 este implementata si verificata pentru fiecare rol | 0 |
| CA-107 | Nimeni in afara Head of R&D si RD Administrator nu poate sterge inregistrari de proces | 0 |
| CA-108 | Notificarile trimise de fluxuri nu contin coloane protejate prin securitate pe coloana | 2 |
| CA-109 | Rolul RD Auditor exista, cu drept de citire pe tot, inclusiv pe audit, si este dezactivat in mod normal | 1 |
| CA-110 | Fiecare utilizator din hala are cont nominal; nu exista conturi partajate de dispozitiv | 1 |
| CA-111 | Politica DLP blocheaza conectorii din afara Microsoft 365 si Dataverse | 0 |

## M25 Migrare

| Cod | Criteriu | Val |
|---|---|---|
| CA-112 | Toate proiectele in curs sunt in sistem si confirmate de tehnologul lor | 1 |
| CA-113 | Proiectele respinse si abandonate sunt pastrate integral, cu motiv, si consultabile | 1 |
| CA-114 | Nu exista coduri de proiect duplicate dupa import | 1 |
| CA-115 | Fisierul original al centralizatorului, fisierul curatat si raportul de import sunt arhivate | 1 |
| CA-116 | Dupa data punerii in functiune, centralizatorul Excel nu se mai actualizeaza | 1 |

## Trasabilitate si audit

| Cod | Criteriu | Val |
|---|---|---|
| CA-117 | Auditul este activ pe toate tabelele de proces si pe coloanele de status, termen, decizie si aprobare | 1 |
| CA-118 | Se poate arata, pentru orice inregistrare, cine a modificat ce, cu valoarea veche si noua, si cand | 1 |
| CA-119 | Dosarul de produs se poate reconstitui la orice data din trecut, din Dataverse si din versiunile SharePoint | 3 |
| CA-120 | Jurnalul de audit al tabelelor critice se arhiveaza lunar in SharePoint, cu retentie de 10 ani | 3 |


<!-- ==================== S20-intrebari-deschise.md ==================== -->

---

# Sectiunea 20 - Intrebari deschise

Zece intrebari. Numai cele care blocheaza o decizie de constructie. Fiecare are impactul
declarat si o valoare implicita, folosita daca raspunsul intarzie, ca sa nu se opreasca
constructia.

---

**IQ-01. Cine detine mediul de productie si cand se obtine?**

*Ce blocheaza*: RSC-01, cel mai grav risc al proiectului. Constructia intr-un mediu
Developer personal este acceptabila pentru Val 0 si Val 1, dar nu pentru un sistem folosit
de 30 de oameni.

*Ce trebuie decis*: daca IT-ul aloca un mediu de productie Dataverse si pana cand; cine
este proprietarul lui administrativ; cine plateste capacitatea.

*Valoare implicita daca nu vine raspuns*: se continua in Developer pana la finalul Valului
1, cu export dublu (OneDrive si biblioteca SharePoint a companiei), si se escaladeaza
formal catre conducere inainte de Val 2.

---

**IQ-02. Cate licente Power Apps Premium se aproba si pentru cine?**

*Ce blocheaza*: domeniul Valului 2. Daca Achizitiile si Productia nu primesc licente,
modulele M09 si M19 nu au utilizatori si nu are sens sa fie construite in forma
proiectata.

*Ce trebuie decis*: numarul de licente pentru utilizatorii care creeaza si modifica date
(estimat 25-35).

*Valoare implicita*: se construieste pentru 30 de utilizatori. Daca se aproba mai putine,
prioritatea este: R&D complet, apoi Calitate, apoi Achizitii, apoi Productie.

*RASPUNS PARTIAL, Sectiunea 28*: costul este cunoscut - 30 de licente Power Apps Premium
inseamna aproximativ 7 200 USD pe an la pretul de lista. Se pot cumpara etapizat, 10-12
pentru Val 1 si restul la Val 2. Ce ramane deschis este aprobarea, nu cifra.

---

**IQ-03. Cum se rezolva accesul de citire pentru cei ~200 de angajati?**

*Ce blocheaza*: constructia ecranului public (ECR-04). Variantele B si C din 17.1.2.1 se
construiesc diferit si nu se pot schimba usor una in alta.

*Ce trebuie decis*: licenta per aplicatie pentru ecranul public, sau export zilnic intr-o
lista SharePoint.

*Valoare implicita*: se construieste varianta B (aplicatie separata, licenta per
aplicatie), pentru ca varianta C se poate deriva din ea in doua zile, dar nu si invers.

*RASPUNS REVIZUIT, Sectiunea 28.5.6*: aplicatia separata se construieste, ca in
recomandarea initiala, dar **lansarea se face prin varianta C**, cu lista SharePoint,
la cost zero. Motivul: accesul de citire pentru cei 200 costa aproximativ 12 000 USD pe
an, adica mai mult decat licentele intregului departament care lucreaza efectiv in sistem.
Se masoara intai cati oameni deschid ecranul, apoi se cumpara licentele, pe aplicatia
deja construita.

---

**IQ-04. Cine stabileste si revizuieste clasificarea A/B/C a clientilor, si cand?**

*Ce blocheaza*: 20 din cele 100 de puncte ale scorului de prioritate. Fara o clasificare
asumata si actualizata, scorul se contesta la fiecare proiect.

*Ce trebuie decis*: persoana responsabila (Comercial Manager sau Director de vanzari),
frecventa revizuirii, si daca clasificarea existenta in SAP sau in comercial poate fi
preluata ca punct de pornire.

*Valoare implicita*: se preia clasificarea existenta din comercial, se atribuie
responsabilitatea revizuirii Comercial Managerului, cu revizuire anuala in ianuarie.

---

**IQ-05. Cine furnizeaza costul real pe kilogram pentru revizuirea post-implementare, si
in ce format?**

*Ce blocheaza*: doua dintre cele patru componente ale indicelui de sanatate (8.4) si
raportul anual `Ce am invatat` (RAP-15). Fara cost real, revizuirea masoara doar calitatea
si volumul.

*Ce trebuie decis*: daca Controllingul poate furniza costul real pe produs, la 60 si 90 de
zile, si daca poate fi automatizat sau ramane manual.

*Valoare implicita*: se construieste ca introducere manuala, cu camp `Date indisponibile`
si raportare a departamentului care nu a furnizat datele.

---

**IQ-06. Aplicatia interna de planificare poate expune un API pentru sloturile de linie?**

*Ce blocheaza*: gradul de realism al slotului de testare propus si al cozii pe linie. Fara
integrare, coada pe linie din R&D este o estimare paralela cu planificarea reala, si cele
doua vor diverge.

*Ce trebuie decis*: daca aplicatia (variantele HTML si API Python) poate expune, chiar si
read-only, ocuparea liniilor pe schimburi.

*Valoare implicita*: fara integrare in Valurile 0-3. Coada pe linie se calculeaza doar din
proiectele R&D, iar slotul ramane o estimare negociabila comunicata manual planificarii
(A1.2.7.3).

---

**IQ-07. Cine raspunde pentru completarea datelor nutritionale si de alergeni ale celor
~1500 de materii prime?**

*Ce blocheaza*: intreaga Sectiune 9 si generarea etichetelor. Este cel mai mare efort de
introducere de date din tot proiectul si nu poate fi facut de constructor singur.

*Ce trebuie decis*: daca responsabilitatea este a Calitatii, a tehnologilor sau a
Achizitiilor, si daca se aloca timp dedicat pentru primele 150-250 de coduri.

*Valoare implicita*: completare la utilizare (15.2.2), cu prima transa in sarcina
Calitatii pentru materiile prime din proiectele active. Modulul M15 ramane in Val 3, cu
riscul de a aluneca.

---

**IQ-08. Sunt corecte pragurile propuse pentru randament si rebut la productia 0?**

*Ce blocheaza*: regula automata de decizie de la productia 0 (7.3.3, 7.9). Un prag gresit
face ca fie totul sa treaca, fie nimic.

*Ce trebuie decis*: confirmarea sau corectarea pragurilor: rebut sub 5% la laminate si sub
3% la depuse; randament peste 92% la laminate si peste 95% la depuse.

*Valoare implicita*: se folosesc valorile propuse, marcate ca PROPUNERE, si se
recalibreaza dupa primele 10 productii 0, cu datele reale.

---

**IQ-09. Cine sunt evaluatorii panelului senzorial si sunt disponibili?**

*Ce blocheaza*: grila din 6.5 cere 3 evaluatori pentru deciziile de continuare si 5 pentru
evaluarea finala. Daca nu exista oameni disponibili, grila ramane teoretica si evaluarea
se face tot de o singura persoana.

*Ce trebuie decis*: lista nominala a panelului, cu inlocuitori, si acordul sefilor lor
pentru timpul alocat.

*Valoare implicita*: se construieste pentru numarul de evaluatori din 6.5.3, dar sistemul
accepta si evaluari cu un singur evaluator, marcate explicit ca `Evaluare individuala` si
raportate ca atare.

---

**IQ-10. Care este disponibilitatea reala de timp a constructorului, in zile pe
saptamana?**

*Ce blocheaza*: intreg calendarul din Sectiunea 16. La 1.5 zile pe saptamana, cele 78-98
de zile-om inseamna peste un an, nu 6-7 luni (16.6.1).

*Ce trebuie decis*: un angajament explicit, asumat de conducere, pentru perioadele de
constructie concentrata din Valurile 0 si 1.

*Valoare implicita*: se planifica pe 1.5 zile pe saptamana si se comunica termenele
corespunzatoare, mai lungi. Este mai bine decat sa se promita 6 luni si sa se livreze in
14.

---

## Ce nu este intrebare deschisa

Urmatoarele nu apar mai sus pentru ca raspunsul este deja dat in blueprint si nu se
renegociaza: alegerea Dataverse; cele doua tipuri de aplicatii; pastrarea documentelor in
SharePoint; interdictia de scriere in SAP; formatul codului de proiect; regula ca orice
diferenta de gramaj, dimensiune sau reteta inseamna proiect nou; faptul ca cele 30 de bife
devin inregistrari de livrabil.


<!-- ==================== S21-prompturi-continuare.md ==================== -->

---

# Sectiunea 21 - Prompturi de continuare

Cate un prompt gata de folosit pentru constructia fiecarui modul. Fiecare se transmite
integral, impreuna cu sectiunile din blueprint la care face referire.

Preambul comun, de pus inaintea fiecarui prompt:

> Esti arhitect de solutii Microsoft Power Platform pentru R&D in industria alimentara
> (frozen bakery, FMCG), specializat pe Dataverse, Power Apps model-driven si canvas,
> Power Automate si SharePoint, intr-o companie certificata IFS Food si ISO, cu plan
> HACCP. Lucrezi cu un Head of R&D inginer, care construieste singur solutia, fara echipa
> IT. Nu explica notiuni de baza, nu propune alternative de platforma, nu renegocia
> deciziile de arhitectura. Raspunde in limba romana fara diacritice, structurat, cu
> tabele acolo unde se enumera sau se compara structuri. Blueprintul de referinta este
> atasat; foloseste numerotarea lui pentru trimiteri.

---

## P-01. Modulul M01 - Fundatie si nomenclatoare (Val 0)

> Construieste ghidul pas cu pas pentru Valul 0: crearea mediului Developer, a Solution
> `RDSuitaDigitala` cu editorul `RD Digital` si prefixul `rd`, si a tuturor
> nomenclatoarelor din Sectiunea 2.25 si din `data/nomenclatoare.json`.
> Livreaza: (a) ordinea exacta de creare a componentelor, cu dependentele intre ele; (b)
> definitia fiecarui Choice global din Sectiunea 2.25.3, cu valorile numerice si
> etichetele; (c) fisierele de import pentru linii, clienti, materii prime, furnizori,
> motive si tipuri de documente, in formatul asteptat de importul Dataverse; (d)
> configurarea auditului conform 5.6.1; (e) procedura de export si de arhivare pe
> OneDrive din 2.0.2; (f) politica DLP din 11.7.6.
> Referinte: Sectiunile 2.0, 2.21 - 2.25, 11, 16.1, 17.2.

---

## P-02. Modulele M02 si M03 - Solicitare si triaj (Val 1)

> Construieste modulul de solicitare si triaj. Livreaza: (a) definitia completa a tabelei
> `rd_solicitare` din 2.1, gata de creat, coloana cu coloana; (b) formularul principal cu
> cele 10 sectiuni din 5.5.1, organizat in trei file, optimizat pentru completare de catre
> un KAM in sub 10 minute; (c) regulile de business pentru campurile conditionate (motiv
> obligatoriu, preluat de, tip termen impus, detalii referinta); (d) vizualizarile
> `Solicitari in triaj`, `Solicitarile mele`, `Solicitari amanate`; (e) ecranul de triaj
> ECR-02 cu cele trei actiuni si dialogurile lor; (f) fluxul FLX-01 in detaliu, pas cu pas,
> cu tratarea erorilor; (g) fluxul FLX-14 pentru solicitarile amanate.
> Verifica rezultatul fata de criteriile CA-07 ... CA-11 din Sectiunea 19.
> Referinte: Sectiunile 2.1, 2.2, 4.1, 5.5.1, 10.1.3, 12.3, 19.

---

## P-03. Modulele M04, M05 si M06 - Proiect, livrabile si etape (Val 1)

> Construieste nucleul solutiei. Livreaza: (a) tabelele `rd_proiect`, `rd_livrabil`,
> `rd_sablonlivrabil`, `rd_etapa`, `rd_sablonetapa`, complet definite; (b) cele 43 de
> inregistrari de sablon de livrabil din Sectiunea 4.4, ca fisier de import, cu faza,
> ordinea, rolurile, offsetul, obligativitatea si conditia de aplicabilitate; (c) cele 11
> etape din 14.2, ca fisier de import; (d) formularul de proiect ECR-01 cu antetul si cele
> 12 file din 10.1.2; (e) regulile de business pentru tranzitiile de status din 2.2.1 si
> pentru regula "proiect nou, nu varianta" din 2.2.3; (f) fluxul FLX-05 in detaliu,
> inclusiv reevaluarea conditiilor si calculul termenelor din 4.6.2; (g) fluxul FLX-04
> pentru proiectele-copil.
> Verifica fata de CA-12 ... CA-29.
> Referinte: Sectiunile 2.2 - 2.6, 3.2, 4, 10.1.2, 12.3, 14.2, 19.

---

## P-04. Modulul M21 - Documente si sabloane (Val 1 si Val 2)

> Construieste integrarea documentara. Livreaza: (a) configurarea site-ului si a
> bibliotecii `PRODUSE IN DEZVOLTARE`, cu cele 13 coloane de metadate din 5.3 si cu
> indexarea din 5.3.1; (b) setarile de versionare din 5.4.1; (c) fluxul FLX-02 pentru
> generarea arborelui de 10 foldere, cu tratarea caracterelor interzise si a numelor lungi;
> (d) configurarea integrarii native Dataverse - SharePoint din 3.6; (e) fluxul FLX-19
> pentru metadate, legatura cu livrabilul, blocarea la aprobare si permisiunile
> confidentiale; (f) fluxul FLX-12 pentru generarea documentelor din sabloane Word, cu
> maparea campurilor pentru DOC-01 ... DOC-09; (g) sabloanele Word ca structura de content
> controls, pentru fiecare document din 5.5; (h) procedura de migrare a folderelor
> existente din 5.1.3.
> Verifica fata de CA-90 ... CA-97.
> Referinte: Sectiunile 3.6, 5 integral, 12.3, 19.

---

## P-05. Modulul M12 - Testare si masuratori (Val 1)

> Construieste modulul de testare si aplicatia canvas de masuratori. Livreaza: (a) tabelele
> `rd_fisatestare`, `rd_trial`, `rd_masuratoare`, `rd_statisticatrial`; (b) aplicatia
> canvas `R&D Linie`, ecranul ECR-11, cu toate cele 6 sub-ecrane din 10.2.2, respectand
> principiile de proiectare pentru hala din 10.2.1; (c) implementarea modului offline, cu
> `SaveData` / `LoadData` si coada de sincronizare, respectand limitarea din 10.2.1.2; (d)
> fluxul FLX-11 cu formulele de statistica din 6.1.4; (e) dimensiunile minime de esantion
> din 6.2.1 ca nomenclator parametrizabil; (f) regulile de semnalare a valorilor aberante
> din 6.2.4.2 si motivele admise de excludere din 6.2.4.3; (g) verdictul pe tip de
> masuratoare din 6.3.2.
> Verifica fata de CA-54 ... CA-60.
> Referinte: Sectiunile 2.10, 6.1 - 6.3, 10.2, 12.3, 19.

---

## P-06. Modulul M07 si Anexa A1 - Alocare, incarcare si termen propus (Val 1)

> Construieste mecanismul de alocare si de calcul al termenului. Livreaza: (a) tabela
> `rd_profiltehnolog` cu campurile de incarcare din 2.22; (b) fluxul FLX-06 pentru
> recalcularea orara a incarcarii pe tehnolog, pe linie si pe client; (c) fluxul FLX-03 cu
> algoritmul complet din A1.2, inclusiv cei patru factori si adaosul pentru materii prime
> noi; (d) dialogul de alocare din 10.1.3.1, care arata incarcarea fiecarui tehnolog; (e)
> tabloul de bord ECR-03 cu cele 8 componente din 10.1.4; (f) pragurile de supraincarcare
> din 2.22.1, ca variabile de mediu.
> Explica explicit cum se pastreaza distinctia dintre termenul propus, negociat si realizat
> (A1.2.6) si de ce termenul propus nu il suprascrie niciodata pe cel negociat.
> Verifica fata de CA-30 ... CA-34.
> Referinte: Sectiunile 2.2, 2.21, 2.22, 10.1.3, 10.1.4, 12.3, A1.2, 19.

---

## P-07. Modulul M08 - Prioritizare (Val 2)

> Construieste sistemul de prioritizare. Livreaza: (a) implementarea algoritmului complet
> din A1.1, cu cele sase componente, benzile de volum, imbatranirea si plafonul ei; (b)
> toate ponderile si pragurile ca variabile de mediu, cu valorile de pornire; (c) fluxul
> FLX-10 saptamanal; (d) mecanismul bugetului de urgenta pe KAM din A1.1.10, cu cei 5 pasi
> ai schimbului; (e) ecranul ECR-05 cu scorul detaliat pe componente si cu suprascrierea;
> (f) securitatea pe coloana pentru campurile de suprascriere, conform 11.5; (g) expirarea
> automata a suprascrierilor la 90 de zile; (h) vizualizarile de coada globala si de coada
> pe fiecare linie din A1.1.11; (i) raportul RAP-14.
> Verifica fata de CA-35 ... CA-42.
> Referinte: Anexa A1.1, Sectiunile 2.2.4, 10.1.6, 11.5, 12.3, 13.6, 19.

---

## P-08. Modulele M09 si M10 - Materii prime, aprovizionare si mostre (Val 2)

> Construieste modulul de materii prime. Livreaza: (a) tabelele `rd_mpproiect`,
> `rd_iteratiefurnizor`, `rd_materieprima`, `rd_furnizor`, `rd_ceremostra`,
> `rd_miscaremostra`; (b) formularul ECR-07 cu bara de progres pe cele 11 statusuri ale
> ciclului MP si cu campurile de Achizitii separate vizual; (c) fluxul FLX-07 pentru
> recalcularea la modificarea unui ETA, cu notificarile obligatorii catre KAM si tehnolog;
> (d) lead time-urile implicite pe tip din 2.6.2, ca nomenclator; (e) fluxul FLX-21 cu
> cele patru categorii de alerte; (f) ecranul canvas ECR-13 pentru receptia de mostra, cu
> temperatura obligatorie la congelat; (g) raportul RAP-12 cu lead time real fata de
> asumat si rata de respingere pe furnizor.
> Verifica fata de CA-43 ... CA-49.
> Referinte: Sectiunile 2.6, 2.7, 2.9, 4.4 (LIV-07, LIV-22, LIV-23), 10.1.7, 10.2.4,
> 12.3, 19.

---

## P-09. Modulul M11 - Blocaje si oprirea ceasului (Val 2)

> Construieste modulul de blocaje. Livreaza: (a) tabela `rd_blocaj` din 2.8; (b) fluxul
> FLX-09, inclusiv calculul zilelor lucratoare, trecerea automata in status `Blocat` si
> revenirea la statusul anterior; (c) regula de oprire a ceasului din 2.8.1 si 13.2.3,
> inclusiv tratarea corecta a blocajelor suprapuse prin reuniune de intervale, nu prin
> suma (13.2.2); (d) separarea raportarii: T-Total al R&D fata de termenul catre client;
> (e) vizualizarea `Proiecte blocate` si raportul RAP-09 pe surse de blocaj.
> Explica de ce blocajele cu sursa `Intern R&D` nu opresc ceasul si de ce concediul nu il
> opreste.
> Verifica fata de CA-50 ... CA-53.
> Referinte: Sectiunile 2.8, 12.3, 13.2, 13.6, 19.

---

## P-10. Modulul M13 - Evaluare senzoriala (Val 2)

> Construieste modulul senzorial. Livreaza: (a) tabelele `rd_evaluaresenzoriala`,
> `rd_criteriusenzorial`, `rd_scorsenzorial`, `rd_defect`, `rd_defectconstatat`; (b) cele
> doua grile din 6.5.1 ca inregistrari de import, cu ponderile si pragurile eliminatorii;
> (c) ancorele descriptive complete pentru toate criteriile, pentru scorurile 1, 3 si 5,
> in stilul exemplului din 6.5.2; (d) lista de defecte pentru bakery congelat, pe cele 7
> grupe din 2.11.4, cu descriere, severitate implicita si cauza probabila; (e) ecranul
> canvas ECR-12, cu un criteriu pe ecran si ancorele afisate; (f) fluxul de calcul al
> scorului ponderat, al dezacordului si al verdictului, conform 6.5.4 si 6.5.5; (g)
> regulile de comparatie cu referinta din 6.4 si 6.5.5.1.
> Verifica fata de CA-61 ... CA-66.
> Referinte: Sectiunile 2.11, 2.12, 6.4, 6.5, 10.2.3, 19.

---

## P-11. Modulul M14 - Reteta si antecalcul (Val 2)

> Construieste modulul de reteta si cost. Livreaza: (a) tabelele `rd_reteta`,
> `rd_versiunereteta`, `rd_liniereteta`, `rd_antecalcul`, `rd_linieantecalcul`; (b)
> formularele ECR-08 si ECR-09, cu grile editabile si totaluri recalculate live; (c)
> validarea sumei liniilor de reteta la 100 kg; (d) mecanismul de blocare a versiunilor
> validate din 2.14.4, implementat si prin business rule, si prin securitate; (e) structura
> de calcul a antecalculului conform DOC-06 din 5.5.6, inclusiv sectiunea de sensibilitate;
> (f) fluxul FLX-18 pentru aprobarea in doua trepte cand marja este sub prag.
> Verifica fata de CA-67 ... CA-70.
> Referinte: Sectiunile 2.13, 2.14, 5.5.6, 10.1.7, 12.3, 19.

---

## P-12. Modulele M18 si M19 - Implementare si productie 0 (Val 2)

> Construieste modulul de implementare. Livreaza: (a) tabelele `rd_implementare`,
> `rd_productie0`, `rd_inregistrareprod0`, cu toate campurile din 2.18, 2.19 si Sectiunea
> 7; (b) checklistul de conditii IPN cu cele 13 pozitii din 5.5.8, cu responsabil si
> dovada pentru fiecare; (c) structura planului IPN si a raportului de productie 0; (d)
> ecranul canvas ECR-14 cu cele 9 sub-ecrane din 10.2.5, functionand offline pentru
> 14.3 - 14.8; (e) lista celor 14 cauze de rebut din 7.3.1 ca nomenclator; (f) parametrii
> urmariti pe faze din 7.5.1, ca sablon pe categorie de produs; (g) regulile de decizie din
> 7.9, inclusiv blocarea deciziei `Validat` la neconformitate HACCP sau la actiuni deschise;
> (h) mecanismul prin care parametrii reali alimenteaza SDP-ul si IL-ul, conform 7.10.
> Verifica fata de CA-78 ... CA-83.
> Referinte: Sectiunile 2.18, 2.19, 5.5.8, 5.5.9, 7 integral, 10.2.5, 19.

---

## P-13. Modulele M15, M16 si M17 - Alergeni, specificatii si etichete (Val 3)

> Construieste modulul de alergeni, specificatii si etichete. Livreaza: (a) tabelele
> `rd_alergen`, `rd_specificatie`, `rd_sdp`, `rd_eticheta`; (b) implementarea algoritmului
> de calcul din 9.2, inclusiv recalcularea energiei din macronutrienti si corectia de
> randament; (c) fluxul FLX-13 cu cele cinci declansatoare din 9.5.1; (d) mecanismul de
> alerta de impact din 9.5.2 si 9.5.3, cu lista produselor afectate; (e) generarea listei
> de ingrediente si a declaratiei de alergeni conform 9.3; (f) tratarea urmelor din cele
> trei surse, conform 9.4, inclusiv matricea de secventiere pe linie; (g) fila `Alergeni si
> nutritionale` din 9.6.1, cu trasabilitatea alergenului pana la materia prima; (h)
> raportul `Portofoliu pe alergeni` (RAP-13); (i) structura SDP conform DOC-07 din 5.5.7.
> Verifica fata de CA-71 ... CA-77.
> Referinte: Sectiunile 2.15 - 2.17, 5.5.7, 9 integral, 13.6, 19.

---

## P-14. Modulul M20 - Revizuirea post-implementare (Val 3)

> Construieste procesul de revizuire post-implementare. Livreaza: (a) tabela
> `rd_revizuire` din 2.20; (b) fluxul FLX-15 cu cei 6 pasi din 8.6.2 si cu reamintirile si
> escaladarea din 8.6.3; (c) formularul ECR-10, cu campurile automate precompletate si cele
> manuale grupate pe departamentul furnizor; (d) indicele de sanatate din 8.4, cu cele
> patru componente; (e) mecanismul prin care decizia `Optimizare` creeaza automat un proiect
> nou legat de cel initial (8.5.1); (f) tratarea datelor nefurnizate din 8.7.1; (g)
> tabloul de bord `Produse lansate` si raportul RAP-11.
> Verifica fata de CA-84 ... CA-89.
> Referinte: Sectiunile 2.20, 8 integral, 10.1.7, 12.3, 13.6, 19.

---

## P-15. Modulele M22 si M23 - Indicatori, raportare si ecranul public (Val 2 si Val 3)

> Construieste raportarea. Livreaza: (a) tabelele `rd_indicator` si `rd_masurareindicator`;
> (b) implementarea celor trei indicatori conform 13.2, 13.3 si 13.4, cu atentie speciala
> la reuniunea de intervale de blocaj din 13.2.2; (c) fluxul FLX-16, zilnic si lunar, cu
> congelarea masuratorilor din 13.5.1; (d) cele 15 rapoarte din 13.6.1, cu precizarea
> pentru fiecare daca traieste in Dataverse sau in Power BI; (e) modelul de date Power BI,
> cu tabelele necesare si relatiile; (f) aplicatia model-driven separata pentru ecranul
> public ECR-04, conform 10.1.5, cu profilul de securitate pe coloana din 11.5.1.
> Verifica fata de CA-98 ... CA-105, in special CA-104 (15 secunde, fara instruire).
> Referinte: Sectiunile 10.1.5, 11.5, 12.3, 13 integral, 19.

---

## P-16. Modulul M24 - Securitate si roluri (Val 0, revizuit la fiecare val)

> Construieste securitatea. Livreaza: (a) cele 13 roluri de securitate din 11.2, cu
> drepturile exacte pe fiecare tabela, conform matricelor din 11.4; (b) cele 6 echipe din
> 11.1.2 si maparea lor pe grupuri Entra ID; (c) profilurile de securitate pe coloana din
> 11.5; (d) structura de permisiuni SharePoint din 11.6; (e) procedura de verificare a
> securitatii, cu cele 7 scenarii de test din 17.3.2; (f) rolul RD Auditor si procedura de
> activare si dezactivare a lui.
> Atentie speciala la 11.5.2: securitatea pe coloana nu se aplica in fluxuri; verifica ce
> coloane apar in corpul notificarilor.
> Verifica fata de CA-106 ... CA-111.
> Referinte: Sectiunile 11 integral, 17.3.2, 19.

---

## P-17. Modulul M25 - Migrarea (Val 1)

> Construieste migrarea. Livreaza: (a) planul de import in cei 11 pasi din 15.2, cu
> fisierul de import pentru fiecare; (b) maparea coloanelor din centralizatorul Excel
> conform 15.3.1; (c) regulile de tratare a celor 30 de bife, diferentiate pe cele trei
> categorii de proiecte din 15.3.3; (d) lista de curatare din 15.4.1, cu instructiuni
> concrete de aplicat in Excel inainte de import; (e) procedura pentru proiectele in curs,
> cu cei 8 pasi din 15.5.1 si cu formularul scurt pentru tehnologi; (f) fluxul de
> reorganizare a folderelor SharePoint din 5.1.3; (g) lista de verificare de dupa migrare
> din 15.7.
> Verifica fata de CA-112 ... CA-116.
> Referinte: Sectiunile 5.1.3, 15 integral, 19.

---

## P-18. Trecerea in productie

> Pregateste trecerea in productie. Livreaza: (a) cererea formala catre IT, scrisa astfel
> incat sa fie evaluabila de cineva care nu cunoaste Power Platform, pe baza sectiunii
> 17.1; (b) procedura de export si import in cei 11 pasi din 17.2.2, cu capturi de ecran;
> (c) lista completa de testare, cele 36 de scenarii din 17.3, ca document de lucru cu
> coloane de rezultat; (d) planul de punere in functiune din 17.4; (e) pachetul de
> documentare pentru preluare din 17.5; (f) materialele de instruire: 2 ore pentru R&D, 1
> ora pentru KAM, 30 de minute pentru celelalte roluri.
> Referinte: Sectiunile 15.5, 16, 17 integral, 18.

---

## P-19. Recalibrarea dupa primul an

> Se foloseste dupa 12 luni de functionare. Analizeaza datele acumulate si propune
> corectiile: (a) duratele standard pe etapa, conform mecanismului din 14.4, cu mediana,
> percentila 80 si distributia; (b) ponderile si pragurile scorului de prioritate din
> A1.1, pe baza distributiei reale a volumelor si a deciziilor de suprascriere; (c)
> factorii de incarcare si de sezonalitate din A1.2.2 si A1.2.4; (d) pragurile de randament
> si rebut de la productia 0 din 7.3.3; (e) tintele indicatorilor din 13.1; (f) sablonul de
> livrabile, pe baza numarului de derogari `Nu se aplica` din 13.4.2.
> Pentru fiecare propunere: valoarea curenta, valoarea propusa, numarul de observatii pe
> care se bazeaza, si ce se schimba in practica daca se aplica.
> Referinte: Sectiunile 7.3, 13, 14.4, A1, si datele reale din sistem.


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


<!-- ==================== A1-prioritizare-si-termene.md ==================== -->

---

# Anexa A1 - Prioritizarea si calculul termenelor

Anexa detaliaza mecanismele cerute in sectiunile 4.2 si 4.3 din brief. Sunt singurele
locuri din blueprint unde regulile de calcul se exprima ca formule, pentru ca nu pot fi
exprimate altfel.

## A1.1 Scorul de prioritate

### A1.1.1 Componentele

Scor pe 100 de puncte, recalculat saptamanal de FLX-10. Ponderile sunt variabile de
mediu, parametrizabile fara modificarea fluxului.

| Componenta | Puncte | Sens |
|---|---|---|
| Volum anual estimat | 30 | Pe benzi, nu liniar |
| Importanta clientului (A/B/C) | 20 | Clasificare stabilita de Sales / KAM |
| Termen impus extern | 20 | Listare, sezon, licitatie |
| Efort de dezvoltare | 10 | Invers proportional |
| Risc de materie prima noua | -10 | Scade scorul |
| Reutilizare de reteta sau de linie setata | 10 | Creste scorul |
| **Total teoretic** | **100** (minim 0, maxim 100) | |

### A1.1.2 Volum anual estimat - 30 de puncte, pe benzi

| Banda | Volum estimat (tone/an) | Puncte |
|---|---|---|
| V1 | peste 500 | 30 |
| V2 | 200 - 500 | 25 |
| V3 | 80 - 200 | 19 |
| V4 | 30 - 80 | 13 |
| V5 | 10 - 30 | 7 |
| V6 | sub 10 | 3 |

Argument: benzile, nu o functie liniara, pentru ca diferenta dintre 400 si 450 de tone nu
schimba nicio decizie, dar diferenta dintre 30 si 300 o schimba pe toate. Pragurile se
stabilesc la configurare din distributia reala a ultimilor doi ani si se revizuiesc anual.

### A1.1.3 Importanta clientului - 20 de puncte

| Clasificare | Puncte |
|---|---|
| A | 20 |
| B | 12 |
| C | 5 |
| Client nou, neclasificat inca | 12 (se trateaza ca B pana la clasificare) |

A1.1.3.1 Clasificarea este stabilita si revizuita de Sales / KAM, nu de R&D. R&D o
consuma, nu o negociaza. Revizuirea este anuala; data ultimei clasificari este vizibila,
iar o clasificare mai veche de 18 luni se semnaleaza.

### A1.1.4 Termen impus extern - 20 de puncte

Punctajul depinde de tipul termenului si de cat de aproape este:

| Situatie | Puncte |
|---|---|
| Listare la retail cu data ferma, in mai putin de 60 de zile | 20 |
| Listare la retail cu data ferma, in 60 - 120 de zile | 15 |
| Sezon (Craciun, Paste, vara) cu data de livrare ferma | 15 |
| Licitatie sau caiet de sarcini cu termen de depunere | 15 |
| Lansare anuntata de client, fara data ferma | 8 |
| Cerinta de reglementare cu termen legal | 20 |
| Fara termen impus | 0 |

A1.1.4.1 Termenul impus se documenteaza: cine l-a impus si prin ce document. Un termen
impus declarat verbal de KAM, fara dovada, primeste jumatate din punctaj. Motiv: fara
aceasta regula, toate proiectele devin "listare urgenta" in prima luna de folosire.

### A1.1.5 Efort de dezvoltare - 10 puncte, invers proportional

| Efort estimat | Descriere | Puncte |
|---|---|---|
| Foarte mic | Schimbare de ambalaj sau eticheta, reteta identica | 10 |
| Mic | Reformulare partiala, linie deja setata, MP existente | 8 |
| Mediu | Produs nou pe tehnologie cunoscuta, linie setata | 5 |
| Mare | Tehnologie noua sau linie care necesita setare | 2 |
| Foarte mare | Produs care cere echipament, capabilitate sau validare noua | 0 |

Efortul se estimeaza de tehnolog sau de Managerul R&D la triaj, pe aceasta scala de
cinci trepte, nu in ore. Estimarea in ore la triaj este o iluzie de precizie.

### A1.1.6 Risc de materie prima noua - minus 10 puncte

| Situatie | Puncte |
|---|---|
| Fara materii prime noi | 0 |
| O materie prima noua, din portofoliul unui furnizor aprobat | -3 |
| O materie prima noua, furnizor nou sau achizitie noua | -6 |
| Doua sau mai multe materii prime noi | -8 |
| Materie prima de import sau caz special | -10 |

Argument: materia prima noua este cea mai frecventa cauza de intarziere si de blocaj
extern. Penalizarea nu spune ca proiectul e mai putin important, spune ca este mai putin
probabil sa se termine repede, deci nu trebuie sa blocheze coada.

### A1.1.7 Reutilizare - 10 puncte

| Situatie | Puncte |
|---|---|
| Reteta existenta, doar gramaj sau ambalaj diferit | 10 |
| Reteta derivata dintr-un produs existent, linie deja setata | 7 |
| Linie deja setata pentru acest tip de produs | 4 |
| Nimic reutilizabil | 0 |

### A1.1.8 Formula finala

```
scor_baza = puncte_volum + puncte_client + puncte_termen + puncte_efort
            + puncte_risc_mp + puncte_reutilizare

scor_cu_imbatranire = scor_baza + bonus_imbatranire        (vezi A1.1.9)

scor_final = MIN(100, MAX(0, scor_cu_imbatranire))

banda = P1 daca scor_final >= 80
        P2 daca scor_final intre 60 si 79
        P3 daca scor_final intre 35 si 59
        P4 daca scor_final sub 35
```

Daca `rd_scorsuprascris` este completat, el inlocuieste `scor_final` la calculul benzii,
dar scorul calculat ramane vizibil alaturi, pentru comparatie.

### A1.1.9 Mecanismul de imbatranire in coada

PROPUNERE: bonus de imbatranire care creste cu timpul de asteptare, ca proiectele mici sa
nu ramana blocate la infinit in spatele celor mari.

```
zile_coada = zile lucratoare de la data acceptarii, cat timp proiectul
             nu a intrat in status In dezvoltare

bonus_imbatranire = MIN(20, INTREG(zile_coada / 10) * 2)
```

Adica 2 puncte la fiecare 10 zile lucratoare de asteptare, plafonat la 20 de puncte, deci
la 100 de zile lucratoare.

Argument in trei randuri: fara imbatranire, un proiect P4 pentru un client C cu volum mic
nu ajunge niciodata sa fie lucrat, iar KAM-ul respectiv inceteaza sa mai foloseasca
sistemul. Cu plafon la 20 de puncte, un proiect nu poate urca din P4 in P1 doar prin
asteptare, dar poate urca din P3 in P2, ceea ce este suficient ca sa intre in coada reala.
Ceasul de imbatranire se opreste cand proiectul intra in lucru, si se opreste si pe durata
blocajelor externe, ca sa nu premieze proiectele blocate din vina furnizorului.

### A1.1.10 Bugetul de urgenta pe KAM

PROPUNERE, conform cerintei: fiecare KAM poate avea simultan un numar limitat de proiecte
in banda maxima.

| Element | Valoare |
|---|---|
| Buget implicit pe KAM | 2 proiecte simultan in banda P1 |
| Buget pentru Comercial Manager (arbitru) | 1 proiect suplimentar, pentru arbitraj |
| Ce se numara | Proiecte in statusuri active (4-9) cu banda P1, indiferent daca banda vine din scor sau din suprascriere |

Mecanismul, la incercarea de a promova un al treilea proiect in P1:

| Pas | Ce se intampla |
|---|---|
| 1 | Sistemul refuza promovarea automata si afiseaza cele doua proiecte P1 existente ale KAM-ului |
| 2 | KAM-ul (sau Comercial Managerul) trebuie sa aleaga explicit unul dintre ele pentru retrogradare in P2 |
| 3 | Retrogradarea cere motiv obligatoriu si se inregistreaza in audit |
| 4 | Daca refuza, proiectul nou ramane in P2, cu scorul calculat vizibil |
| 5 | Managerul R&D primeste notificare la fiecare schimb de acest tip |

A1.1.10.1 Argument: fara buget de urgenta, scorul se erodeaza in trei luni - toti KAM-ii
suprascriu totul in banda maxima si sistemul redevine "cine striga mai tare". Cu buget,
urgenta devine o resursa rara pe care fiecare KAM o gestioneaza singur, iar arbitrajul
intre KAM-i ramane, conform cerintei, la Managerul R&D.

A1.1.10.2 Bugetul nu se aplica proiectelor cu termen impus extern documentat de tip
reglementare. Acelea intra in P1 fara sa consume buget.

### A1.1.11 Coada pe linie

A1.1.11.1 Cele 9 linii nu concureaza intre ele. Coada se vede in doua feluri:

| Vedere | Ce arata | Cine o foloseste |
|---|---|---|
| Coada globala | Toate proiectele active, ordonate dupa scor | Comercial, Head of R&D |
| Coada pe linie | Proiectele care vizeaza fiecare linie, ordonate dupa scor, cu primul slot liber estimat | Manager R&D, Planificare |

A1.1.11.2 Un proiect P1 pe linia L03 nu are prioritate fata de un proiect P2 pe linia L07:
sunt resurse diferite. Prioritatea conteaza numai in interiorul aceleiasi linii si in
alocarea timpului de tehnolog.

A1.1.11.3 Supraincarcarea unei linii (peste `rd_pragsupraincarcare`) se semnaleaza vizual
si intra ca factor in calculul termenului propus (A1.2), nu in scorul de prioritate.

### A1.1.12 Suprascrierea

| Element | Regula |
|---|---|
| Cine poate | Numai Comercial Manager (ROL-06), prin securitate pe coloana |
| Ce cere | Scorul nou (0-100) si motivul, ambele obligatorii |
| Ce se pastreaza | Scorul calculat ramane vizibil alaturi; suprascrierea nu il sterge |
| Audit | Coloanele de suprascriere sunt auditate; data si autorul se scriu automat |
| Expirare | PROPUNERE: suprascrierea expira dupa 90 de zile si scorul revine la cel calculat, cu notificare cu 7 zile inainte |
| Raportare | Raport lunar cu toate suprascrierile, motivele si autorii |

A1.1.12.1 Argument pentru expirare: o suprascriere facuta pentru o situatie reala din
martie nu mai are sens in septembrie, dar nimeni nu se intoarce sa o retraga. Expirarea
automata pastreaza sistemul curat fara sedinte de curatare.

## A1.2 Calculul termenului propus

### A1.2.1 Formula

```
durata_baza = durata standard din sablonul de etape, pentru tipul de proiect
              (implicit 14 zile lucratoare)

durata_ajustata = durata_baza
                  * factor_incarcare_tehnolog
                  * factor_coada_linie
                  * factor_sezonalitate
                  + adaos_materii_prime_noi
                  + zile_indisponibilitate_tehnolog

termen_propus = data_acceptarii + durata_ajustata zile lucratoare
```

### A1.2.2 Factorul de incarcare a tehnologului

| Proiecte active ale tehnologului | Factor |
|---|---|
| 1 - 2 | 0.9 |
| 3 - 4 | 1.0 |
| 5 - 6 | 1.2 |
| 7 - 8 | 1.5 |
| 9 - 10 | 1.9 |
| peste 10 | 2.4, cu avertizare de supraincarcare la alocare |

Argument: un tehnolog cu 8 proiecte active nu lucreaza de 8 ori mai incet la fiecare, dar
nici nu lucreaza la fel de repede ca unul cu 2. Factorii de mai sus sunt punctul de
pornire; se recalibreaza dupa 6-12 luni din duratele reale, conform Sectiunii 14.

### A1.2.3 Factorul de coada pe linie

| Proiecte active care vizeaza linia | Factor |
|---|---|
| 0 - 2 | 1.0 |
| 3 - 5 | 1.1 |
| 6 - 8 | 1.25 |
| peste 8 | 1.4 |

Se aplica numai daca proiectul are linie stabilita la acceptare. Daca nu are, se foloseste
media liniilor compatibile cu tipul de produs.

### A1.2.4 Factorul de sezonalitate

| Perioada de acceptare | Factor | Motiv |
|---|---|---|
| Ianuarie - martie | 1.0 | Perioada normala |
| Aprilie - mai | 1.1 | Pregatirea sezonului de vara |
| Iunie - august | 1.2 | Concedii, capacitate redusa |
| Septembrie - octombrie | 1.3 | Varful de dezvoltare pentru Craciun; linii ocupate |
| Noiembrie - decembrie | 1.25 | Productie de varf, acces greu la linii |

A1.2.4.1 Factorii de sezonalitate sunt PROPUNERE si trebuie confirmati cu date reale din
ultimii doi ani, la configurare. Sunt intre primele care se recalibreaza dupa un an de
masuratori.

### A1.2.5 Adaosul pentru materii prime noi

| Situatie | Zile adaugate |
|---|---|
| Fara materii prime noi | 0 |
| MP noua, pe stoc la furnizor | +5 zile lucratoare |
| MP noua, in portofoliul furnizorului | +5 zile lucratoare |
| MP noua, achizitie noua | +20 de zile lucratoare |
| MP de import sau caz special | +30 de zile lucratoare sau ETA declarat, care e mai mare |
| Mai multe MP noi | Se ia cea mai mare valoare, nu suma |

A1.2.5.1 Se ia maximul, nu suma, pentru ca aprovizionarea materiilor prime se face in
paralel. Daca ETA-ul confirmat exista deja, el inlocuieste estimarea.

### A1.2.6 Cele trei termene

| Termen | Cine il stabileste | Cand se schimba | Ce masoara |
|---|---|---|---|
| Propus | Sistemul, prin FLX-03 | La orice recalculare (schimbare de tehnolog, linie, ETA) | Ce poate livra R&D in conditiile date |
| Negociat | Managerul R&D impreuna cu KAM | Numai manual, cu urma in audit | Angajamentul catre client |
| Realizat | Sistemul, la trecerea in `Finalizat` | O singura data | Realitatea |

A1.2.6.1 Diferenta `negociat - propus` masoara cat de des se promite mai mult decat se
poate. Diferenta `realizat - negociat` masoara respectarea angajamentului. Ambele se
raporteaza, separat, pe KAM si pe tehnolog. Sunt cele doua cifre care schimba discutia
anuala dintre R&D si comercial dintr-una despre impresii intr-una despre date.

### A1.2.7 Slotul de testare

A1.2.7.1 Slotul de testare pe linie este o **estimare negociabila, nu o constrangere
blocanta**. Sistemul propune primul slot disponibil pe linia vizata, pe baza cozii, dar nu
rezerva nimic in aplicatia de planificare a productiei si nu impiedica nimic.

A1.2.7.2 Arbitrajul intre doi KAM care vor acelasi slot il face Managerul R&D. Sistemul ii
arata: cele doua proiecte cu scorurile lor detaliate, bugetul de urgenta consumat de
fiecare KAM, si impactul asupra termenului fiecarui proiect daca este mutat. Decizia si
motivul se inregistreaza pe proiectul care pierde slotul.

A1.2.7.3 NOTA: legatura cu aplicatia interna de planificare (9 linii, 3 schimburi, sarje,
paleti, Gantt) ramane manuala in Valurile 0-3. Slotul propus de R&D se comunica
planificarii, care il confirma sau il muta. O integrare reala ar cere un API stabil pe
partea de planificare si este candidat pentru un val ulterior, nu pentru acest blueprint.


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


<!-- ==================== README.md ==================== -->

---

# Blueprint Suita Digitala R&D - Dataverse / Power Apps / SharePoint / Power Automate

Document de arhitectura pentru digitalizarea procesului R&D intr-o companie FMCG de
panificatie si patiserie congelata (2 amplasamente, 9 linii, ~400 persoane, 130-180
proiecte CDI pe an).

Rezultatul este un blueprint de constructie, nu cod. Se construieste modul cu modul,
fara alte decizii de arhitectura.

> **Acest repository nu este produsul. Este schela din care se construieste produsul.**
> Solutia finala ruleaza integral in tenantul companiei, pe Dataverse, Power Apps,
> Power Automate, SharePoint si Power BI. Fisierele de aici sunt blueprintul, modelul
> exprimat ca date si scripturile care creeaza componentele in Dataverse prin Web API.
> Python-ul nu ruleaza in tenant si nu face parte din solutia livrata.
> Vezi [Sectiunea 27](docs/S27-unde-traieste-ce.md).

Documentul rezulta din sinteza a doua surse: blueprintul operational construibil
(Sectiunile 0-21) si arhitectura tinta "R&D Suite Enterprise", din care s-au preluat 11
elemente de fond si s-au amanat explicit restul. Deciziile de fuziune, cu motive, sunt in
[Sectiunea 22](docs/S22-sinteza-enterprise.md); ce s-a amanat, cu criterii de activare,
in [Anexa A2](docs/A2-backlog-enterprise.md).

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
| A1 | [A1-prioritizare-si-termene.md](docs/A1-prioritizare-si-termene.md) | Anexa: algoritmul scorului de prioritate si al termenului propus |
| 22 | [S22-sinteza-enterprise.md](docs/S22-sinteza-enterprise.md) | Sinteza cu blueprintul Enterprise: ce s-a preluat, ce s-a respins, contradictii rezolvate |
| 23 | [S23-guvernanta-proiect.md](docs/S23-guvernanta-proiect.md) | Gate-uri, riscuri, probleme, actiuni, decizii, lead time inteligent, alerte |
| 24 | [S24-stabilizare-capabilitate.md](docs/S24-stabilizare-capabilitate.md) | Stabilizare pe 3 loturi, Cp si Cpk, sanatatea proiectului in timp |
| 25 | [S25-cunoastere.md](docs/S25-cunoastere.md) | Lectii invatate, reutilizare, recomandare |
| A2 | [A2-backlog-enterprise.md](docs/A2-backlog-enterprise.md) | Anexa: backlogul amanat, cu criterii de activare |
| 26 | [S26-constructie-asistata.md](docs/S26-constructie-asistata.md) | Ce se genereaza automat, ce nu, si efortul recalculat |
| 27 | [S27-unde-traieste-ce.md](docs/S27-unde-traieste-ce.md) | Ce ruleaza in Microsoft, ce este schela, unde se face trecerea |
| 28 | [S28-acces-si-licentiere.md](docs/S28-acces-si-licentiere.md) | Cum ajunge echipa la aplicatie, cine are nevoie de licenta, cat costa |

## Artefacte pentru constructie

Fisierele din `data/` sunt reprezentarea prelucrabila a blueprintului. Se folosesc la
crearea tabelelor, a nomenclatoarelor si a sabloanelor, si pot fi importate in Excel
sau consumate de un script de provizionare.

| Fisier | Continut |
|---|---|
| [data/tabele.json](data/tabele.json) | Cele 60 de tabele si 985 de coloane din Sectiunile 2, 23, 24 si 25 |
| [data/relatii.json](data/relatii.json) | Cele 111 relatii din Sectiunea 3, cu comportament la stergere |
| [data/choices.json](data/choices.json) | Cele 31 de seturi de optiuni globale, cu valori si etichete |
| [data/sablon-livrabile.json](data/sablon-livrabile.json) | Cele 43 de livrabile standard, cu faza, rol, termen si conditie de aplicabilitate |
| [data/sablon-etape.json](data/sablon-etape.json) | Cele 11 etape standard, duratele de pornire si mecanismul de calibrare |
| [data/prioritizare.json](data/prioritizare.json) | Ponderi, benzi, buget de urgenta si factorii de calcul al termenului |
| [data/nomenclatoare.json](data/nomenclatoare.json) | Tipuri de documente, motive, criterii senzoriale cu ancore, defecte, cauze de rebut, praguri |

## Constructia

`build/` contine materialele cu care se executa efectiv Valul 0.

| Fisier | Continut |
|---|---|
| [build/V0-ghid-constructie.md](build/V0-ghid-constructie.md) | Ghid pas cu pas pentru Valul 0: mediu, DLP, solutie, variabile, Choice-uri, nomenclatoare, sabloane, roluri, SharePoint, export, verificare |
| [build/import/](build/import/) | 8 fisiere CSV gata de importat in Dataverse plus 5 sabloane de completat cu datele companiei |
| [build/genereaza-import.py](build/genereaza-import.py) | Regenereaza fisierele CSV din `data/*.json`, ca sa ramana sincronizate cu blueprintul |
| [build/genereaza-model.py](build/genereaza-model.py) | Sursa unica pentru `data/tabele.json`: cele 60 de tabele si 985 de coloane |
| [build/deploy/](build/deploy/) | Provizionarea modelului in Dataverse prin Web API: 31 de optionsets, 60 de tabele, 738 de coloane, 151 de relatii |
| [build/deploy/genereaza-ui.py](build/deploy/genereaza-ui.py) | 59 de formulare, 155 de vizualizari, harta de site, 13 roluri cu 2931 de privilegii |
| [build/deploy/genereaza-fluxuri.py](build/deploy/genereaza-fluxuri.py) | Scheletele celor 35 de fluxuri, cu correlation id, Try/Catch si retry |
| [build/deploy/genereaza-sabloane-word.py](build/deploy/genereaza-sabloane-word.py) | Cele 12 sabloane .docx cu 249 de content controls |
| [build/preview-ecrane.html](build/preview-ecrane.html) | Preview vizual al celor 5 ecrane principale, desenat din artefactele generate |

Fisierele de import gata de folosit: 40 de motive, 31 de tipuri de documente, 14
alergeni, 22 de defecte, 17 criterii senzoriale cu ancore, 11 etape, 43 de livrabile cu
tipurile de proiect aplicabile deja calculate, si cele 178 de valori ale Choice-urilor
globale. Sabloanele de completat: linii de productie, clienti, furnizori, materii prime,
profiluri de tehnolog.

## Conventii de referinta

| Prefix | Inseamna |
|---|---|
| `TBL-nn` | Tabela Dataverse |
| `REL-nn` | Relatie intre tabele |
| `LIV-nn` | Livrabil de proiect din sablon |
| `FLX-nn` | Flux Power Automate |
| `ECR-nn` | Ecran de aplicatie |
| `ROL-nn` | Rol de securitate |
| `RSC-nn` | Risc |
| `CA-nn` | Criteriu de acceptanta |
| `DOC-nn` | Document generat din date |
| `RAP-nn` | Raport |
| `M-nn` | Modul |
| `ETP-nn` | Etapa de proiect |
| `PROPUNERE` | Element propus de arhitect, care nu exista in cerinta initiala |
| `NOTA` | Conflict intre cerinta din context si buna practica de platforma |

## Verificarea artefactelor

Fisierele din `data/` sunt verificate incrucisat: fiecare relatie refera o tabela si o
coloana care exista, fiecare faza si rol din sablonul de livrabile exista in Choice-ul
corespunzator, fiecare sablon Word are un tip de document, iar ponderile grilelor
senzoriale insumeaza 100 pe categorie de produs.

## Ce urmeaza

Blueprintul este complet si se poate construi din el, modul cu modul, fara alte decizii
de arhitectura. Pasii imediati:

1. Raspunsuri la cele 10 intrebari din [Sectiunea 20](docs/S20-intrebari-deschise.md).
   Fiecare are o valoare implicita, deci constructia poate incepe si fara ele, dar IQ-01
   (mediul de productie) si IQ-10 (disponibilitatea reala de timp) schimba calendarul.
2. Valul 0, dupa [build/V0-ghid-constructie.md](build/V0-ghid-constructie.md), cu
   fisierele de import din `build/import/`. Efort 8-10 zile-om, durata 2-3 saptamani.
3. Fiecare modul se construieste cu promptul lui din Sectiunea 21 si se verifica fata de
   criteriile din [Sectiunea 19](docs/S19-criterii-acceptanta.md).

## Constructia asistata

Metadatele Dataverse sunt date, deci se genereaza. `build/deploy/provisioning.py` creeaza
prin Web API 961 din cele 985 de coloane ale modelului - restul de 24, de tip Calculated si
Rollup, se configureaza manual pentru ca formula nu se poate seta fiabil prin API.

| | Estimare initiala | Revizuita |
|---|---|---|
| Constructie | 138 zile-om | **41** |
| Colectare de date, testare, instruire | nedetaliat | **37-53** |
| Total | 130-158 | **78-94** |

Constructia se comprima de 3,4 ori; proiectul de 1,7 ori. Diferenta este ca peste jumatate
din efortul ramas nu este constructie, ci colectare de date de la celelalte departamente,
testare cu oameni reali si asteptarea realitatii. Detaliat in
[Sectiunea 26](docs/S26-constructie-asistata.md).

**Consecinta de planificare**: calea critica nu mai este constructia, ci obtinerea datelor.
Cererile catre Sales, Productie si Calitate trebuie sa plece in prima saptamana, nu cand
ajunge constructia la ele.

## Domeniul: cele trei niveluri

| Nivel | Tabele | Valuri | Criteriu de existenta |
|---|---|---|---|
| Core | 60 | Val 0-3, lunile 1-9 | Fara ele procesul R&D nu functioneaza digital |
| Extins | 13 | Val 4-5, lunile 9-15 | Se activeaza cand procesul core produce date consecvent |
| Amanat | ~80 din inventarul Enterprise | Dupa Val 5 | Fiecare cu criteriu de activare in A2 |

Solutia este utila si daca se opreste dupa Valul 3: acopera intreg procesul R&D, de la SCP
la revizuire, cu gate-uri, riscuri, stabilizare si lectii invatate. Vezi 16.8.3.


<!-- ==================== build/V0-ghid-constructie.md ==================== -->

---

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


<!-- ==================== build/deploy/README.md ==================== -->

---

# Provizionarea modelului de date

Creeaza in Dataverse, prin Web API, cele 31 de seturi de optiuni globale, 60 de tabele,
738 de coloane si 151 de relatii definite in `data/`.

Inlocuieste aproximativ 45 de zile de click-uri in interfata Power Apps cu o rulare de
sub o ora.

## Ce acopera

| Element | Numar | Cum |
|---|---|---|
| Seturi de optiuni globale | 31 | Generat integral |
| Tabele | 60 | Generat integral, cu coloana primara si audit activat |
| Coloane | 738 | Generat integral |
| Coloane de tip Lookup | 163 | Create prin relatii, nu separat |
| Relatii | 151 | Generat integral, cu comportamentul la stergere din `relatii.json` |
| **Coloane Calculated si Rollup** | **24** | **Manual, in interfata** - vezi mai jos |

Total: 985 din 985 de coloane ale modelului sunt acoperite, dintre care 961 automat.

## Ce ramane manual si de ce

Cele 24 de coloane Calculated si Rollup nu se pot crea complet prin API: definitia formulei
este o structura interna pe care API-ul de metadate nu o accepta fiabil. Lista lor completa
este in `payloaduri/coloane-manuale.json`, cu tabela, numele si regula de calcul din
blueprint.

Se creeaza in interfata, in aproximativ 2 ore, dupa ce restul modelului exista - ceea ce
este si ordinea corecta, pentru ca formulele refera coloane care trebuie sa existe deja.

## Cerinte

1. Un mediu Dataverse (Developer sau Sandbox).
2. O inregistrare de aplicatie in Entra ID (app registration) cu drept de a scrie metadate,
   adaugata ca utilizator de aplicatie in mediu, cu rolul System Customizer sau System
   Administrator.
3. Solutia `RDSuitaDigitala` creata in prealabil, cu editorul `RD Digital` si prefixul `rd`
   (pasul 3 din `build/V0-ghid-constructie.md`). Scriptul adauga componentele in ea prin
   antetul `MSCRM.SolutionUniqueName`.

## Utilizare

```bash
# 1. Verifica ce se va crea, fara sa atinga serverul
python3 build/deploy/provisioning.py --dry-run

# 2. Salveaza payloadurile ca JSON, pentru inspectie sau pentru alt instrument
python3 build/deploy/provisioning.py --dry-run --scrie-payload

# 3. Configureaza autentificarea
export DV_URL=https://organizatie.crm4.dynamics.com
export DV_TENANT_ID=...
export DV_CLIENT_ID=...
export DV_CLIENT_SECRET=...

# 4. Ruleaza pe etape, in aceasta ordine
python3 build/deploy/provisioning.py --etapa optionsets
python3 build/deploy/provisioning.py --etapa entities
python3 build/deploy/provisioning.py --etapa attributes
python3 build/deploy/provisioning.py --etapa relationships
```

Ordinea este obligatorie: coloanele de tip Choice refera seturi globale care trebuie sa
existe, iar relatiile refera tabele care trebuie sa existe.

## Idempotenta si reluare

Scriptul retine ce a creat in `build/deploy/stare.json`. O rulare intrerupta - din cauza
limitei de API, a expirarii tokenului sau a unei erori - se reia cu aceeasi comanda si
continua de unde a ramas.

Pentru a reporni de la zero intr-un mediu curat, se sterge `stare.json`.

## Ce se intampla la erori

Scriptul nu se opreste la prima eroare. Afiseaza tabela si coloana afectata, plus raspunsul
serverului, si continua. La final raporteaza cate elemente s-au creat, cate existau deja si
cate au esuat.

Erorile raman de rezolvat una cate una, dar sunt tipic de trei feluri:

| Tip de eroare | Cauza obisnuita | Rezolvare |
|---|---|---|
| Nume prea lung sau invalid | Un nume logic care depaseste limita cu prefixul aplicat | Se scurteaza in `build/genereaza-model.py` si se regenereaza |
| Interval invalid | O valoare de tip Decimal cu precizie mai mare decat permite tipul | Se corecteaza in model |
| Dependenta lipsa | O relatie catre o tabela care nu s-a creat inca | Se reia etapa anterioara |

## Avertisment onest

**Payloadurile sunt validate structural, nu impotriva unui tenant real.** Nu am putut testa
scriptul contra unui mediu Dataverse. Verificarile facute sunt: unicitatea numelor,
lungimile maxime, coerenta intervalelor, existenta seturilor de optiuni referite si a
tabelelor tinta ale relatiilor.

Dataverse va respinge, cu mare probabilitate, cateva elemente pentru motive care nu se pot
anticipa din afara: rezervari de nume, particularitati de versiune, restrictii de mediu.
Estimarea realista este de **2 pana la 4 cicluri de rulare si corectie**, adica 2-3 zile,
nu o rulare perfecta din prima.

Aceasta este totusi de aproximativ 15 ori mai putin decat crearea manuala a acelorasi
componente in interfata.

## Dupa provizionare

1. Cele 24 de coloane Calculated si Rollup, din `payloaduri/coloane-manuale.json`.
2. Cheile alternative pe codurile de business (22.6): `rd_codproiect` pe proiect,
   `rd_codsap` pe materie prima si client, `rd_codlivrabil` plus proiect pe livrabil.
3. Importul datelor de nomenclator, cu fisierele din `build/import/`.
4. Exportul solutiei, conform pasului 9 din ghidul Valului 0.
