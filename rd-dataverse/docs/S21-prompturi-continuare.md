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
