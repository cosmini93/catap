# Volumul 3 - Roadmap, riscuri si constructie

Parte din blueprintul Suitei Digitale R&D, export din 09.09.2026.
Contine sectiunile: S16-roadmap, S17-trecere-productie, S18-riscuri, S19-criterii-acceptanta, S20-intrebari-deschise, S21-prompturi-continuare, A1-prioritizare-si-termene.

Contextul complet al proiectului este in preambulul din `BLUEPRINT-COMPLET.md`.



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
