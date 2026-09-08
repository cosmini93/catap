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
