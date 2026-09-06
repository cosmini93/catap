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
