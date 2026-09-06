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
