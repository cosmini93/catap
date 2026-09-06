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
| Nomenclatoarele | TBL-36 linii, TBL-38 clienti, TBL-37 profiluri, TBL-41 motive, TBL-42 tipuri de documente, alergeni, Choice-uri globale |
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

## 16.2 Val 1 - MVP utilizabil (30 de zile)

**Durata**: 4-5 saptamani de la finalul Valului 0. **Efort**: 20-25 de zile-om.

| Ce se livreaza | Module | Detaliu |
|---|---|---|
| Solicitarea si triajul | M02, M03 | TBL-01, ECR-02, ECR-06, FLX-01 |
| Proiectul | M04 | TBL-02, ECR-01 cu filele Sinteza, Livrabile, Etape, Documente |
| Livrabilele si etapele | M05, M06 | TBL-03, TBL-05, FLX-05 |
| Documentele | M21 | Arborele de foldere, FLX-02, FLX-19, conventia de denumire |
| Termenul propus | M06 | FLX-03, cu factorii din A1.2 |
| Incarcarea si alocarea | M07 | FLX-06, ECR-03 partial |
| Testarea si masuratorile | M12 | TBL-14, TBL-15, TBL-16, TBL-16b, FLX-11, ECR-11 in canvas |
| Alertele | - | FLX-08, FLX-14, FLX-22 |
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

**Durata**: 6-8 saptamani de la Val 1. **Efort**: 25-30 de zile-om.

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

**Durata**: 8-10 saptamani de la Val 2. **Efort**: 20-25 de zile-om.

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

## 16.5 Ce ramane dupa Val 3

16.5.1 Candidate pentru valuri ulterioare, in ordinea probabila a valorii:

| Candidat | De ce nu acum |
|---|---|
| Integrarea cu aplicatia de planificare a productiei (sloturi reale de linie) | Cere un API stabil pe partea de planificare; dependenta externa |
| Import automat de preturi de materie prima din SAP | Cere acces la un export SAP programat; dependenta de IT |
| Portal pentru clienti (status si mostre) | Cere licentiere Power Pages si o discutie de securitate proprie |
| Shelf life si planuri de studiu de valabilitate | Proces distinct, cu propriile cerinte de laborator |
| Managementul ambalajelor ca modul propriu | Astazi se acopera suficient prin livrabile si etichete |
| Aplicatie de panel senzorial pentru consumatori | Alta populatie de utilizatori, alta discutie |

16.5.2 NOTA: dupa Val 3, prioritatea numarul unu nu este un modul nou, ci trecerea in
mediul de productie (Sectiunea 17) si documentarea suficienta pentru ca solutia sa poata
fi preluata de altcineva (constrangerea din brief). Ambele se amana usor si costa scump
cand se amana.

## 16.6 Sinteza efortului

| Val | Durata | Efort (zile-om) | Cumulat |
|---|---|---|---|
| Val 0 | 2-3 saptamani | 8-10 | 8-10 |
| Val 1 | 4-5 saptamani | 20-25 | 28-35 |
| Val 2 | 6-8 saptamani | 25-30 | 53-65 |
| Val 3 | 8-10 saptamani | 20-25 | 73-90 |
| Trecerea in productie | 2 saptamani | 5-8 | 78-98 |
| **Total** | **~6-7 luni** | **78-98 zile-om** | |

16.6.1 La o disponibilitate de 1.5 zile pe saptamana, 90 de zile-om inseamna aproximativ
60 de saptamani, adica un an si doua luni - nu 6 luni. Calendarul de mai sus presupune
perioade de constructie concentrata (2-3 zile pe saptamana) in Valurile 0 si 1, cand
efortul este cel mai dens. Aceasta este cea mai importanta ipoteza a intregului roadmap si
trebuie confirmata explicit inainte de start, altfel termenele de mai sus sunt fictiune.
