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
