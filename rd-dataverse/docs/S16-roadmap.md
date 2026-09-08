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
