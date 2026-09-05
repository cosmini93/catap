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
