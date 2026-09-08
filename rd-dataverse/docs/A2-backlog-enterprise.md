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
