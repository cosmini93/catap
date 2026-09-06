# Sectiunea 14 - Duratele etapelor

## 14.1 Principiul

14.1.1 Duratele standard se seteaza **o singura data, la configurare**, pornind de la
durata de referinta de 2 saptamani pe proiect. Nu se ajusteaza ad-hoc, la fiecare proiect
care intarzie.

14.1.2 Sistemul masoara duratele reale de la primul proiect si, dupa 6-12 luni de date,
**propune** corectia sabloanelor. Propunerea nu se aplica automat.

14.1.3 Argument pentru propunere in loc de aplicare automata: o durata standard nu este
doar o masuratoare, ci si un angajament. Daca sistemul ridica automat durata etapei de
testare de la 3 la 5 zile pentru ca asa a fost realitatea, procesul se auto-justifica si
nimeni nu mai intreaba de ce a devenit mai lent. Corectia trebuie sa fie o decizie a Head
of R&D, luata cu datele in fata.

## 14.2 Duratele de pornire

Sablonul standard, pentru tipul `Produs nou`, pe 14 zile lucratoare. Etapele se pot
suprapune; suma duratelor este mai mare decat durata proiectului.

| Cod | Etapa | Durata standard (zile lucratoare) | Start (zi) | Rol responsabil |
|---|---|---|---|---|
| ETP-01 | Triaj si acceptare | 1 | 0 | Manager R&D |
| ETP-02 | Planificare si alocare | 2 | 1 | Manager R&D, Tehnolog |
| ETP-03 | Aprovizionare materii prime | 5 (paralel) | 2 | Achizitii |
| ETP-04 | Dezvoltare reteta si antecalcul | 4 | 2 | Tehnolog |
| ETP-05 | Testare si trialuri | 4 | 5 | Tehnolog |
| ETP-06 | Evaluare senzoriala si decizie | 1 | 9 | Tehnolog, panel |
| ETP-07 | Mostre catre client si feedback | 3 (paralel) | 10 | Suport R&D, KAM |
| ETP-08 | Specificatii si eticheta | 4 | 10 | Tehnolog, Calitate |
| ETP-09 | Pregatirea implementarii (IPN) | 2 | 15 | Tehnolog |
| ETP-10 | Productie 0 | 1 | 18 | Tehnolog, Productie |
| ETP-11 | Validare si dosar TDV | 2 | 19 | Manager R&D, Calitate |

14.2.1 Etapa ETP-03 (aprovizionare) ruleaza in paralel si nu prelungeste proiectul decat
daca depaseste momentul in care este nevoie de materie prima. Modelarea ei ca etapa
separata este necesara ca sa se poata masura si atribui intarzierea corect.

14.2.2 Termenul propus rezulta din durata totala a lantului critic (ETP-01, 02, 04, 05,
06, 08, 09, 10, 11 = 21 de zile calendaristice cu suprapuneri, adica 14 zile lucratoare
efective in cazul standard), ajustat cu factorii din Anexa A1.2.

14.2.3 Duratele pe celelalte tipuri de proiect, ca punct de pornire:

| Tip proiect | Durata standard totala | Etape eliminate |
|---|---|---|
| Produs nou | 14 zile lucratoare | - |
| Reformulare | 10 zile | ETP-07 scurtat |
| Abatere (.1) | 5 zile | ETP-02, ETP-03, ETP-08 partial |
| Transfer pe alta linie | 8 zile | ETP-04, ETP-08 |
| Optimizare cost | 12 zile | ETP-07 optional |
| Ambalaj nou | 8 zile | ETP-04, ETP-05, ETP-06 |

## 14.3 Mecanismul de masurare

14.3.1 Pentru fiecare etapa a fiecarui proiect se inregistreaza: data de start planificata
si reala, data de final planificata si reala, durata bruta, zilele de blocaj suprapuse, si
durata neta (TBL-05, coloanele `rd_duratabruta`, `rd_zileblocate`, `rd_duratanet`).

14.3.2 Durata **neta** este cea folosita pentru propunerea de corectie. Durata bruta
include asteptarea din cauze externe si ar duce la umflarea artificiala a standardelor.

14.3.3 Startul real al unei etape se inregistreaza la prima activitate reala pe ea
(crearea unui trial pentru ETP-05, salvarea primului scor senzorial pentru ETP-06), nu la
o bifa manuala. Motiv: bifele manuale de start se fac retroactiv, cu ochiul pe indicator.

## 14.4 Propunerea de corectie

### 14.4.1 Cand se face

FLX-17 ruleaza lunar si genereaza propuneri numai daca sunt indeplinite toate conditiile:

| Conditie | Valoare | Motiv |
|---|---|---|
| Numar de proiecte finalizate cu etapa masurata | minimum 20 | Sub 20 de observatii, mediana nu este stabila |
| Perioada acoperita | minimum 6 luni | Sa se prinda cel putin doua sezoane diferite |
| Abaterea propusa fata de standardul curent | minimum 20% | Sub 20%, corectia nu merita perturbarea |

### 14.4.2 Ce se propune

```
durata_propusa = MEDIANA(durata_neta a etapei, pe proiectele finalizate
                         in ultimele 12 luni, de acelasi tip de proiect)
```

14.4.2.1 Se foloseste mediana, nu media. Motiv: distributia duratelor reale are coada
lunga la dreapta (cateva proiecte care s-au tarat luni de zile), iar media ar fi trasa de
ele. Mediana descrie proiectul tipic, care este exact ce trebuie sa fie un standard.

14.4.2.2 Se calculeaza si percentila 80, afisata alaturi: "8 din 10 proiecte termina
aceasta etapa in cel mult X zile". Este cifra utila pentru a promite termene cu marja, nu
pentru a seta standardul.

### 14.4.3 Ce se afiseaza pentru comparatie

Ecranul `Calibrarea duratelor`, in zona de configurare, cu un rand pe etapa si pe tip de
proiect:

| Coloana | Continut |
|---|---|
| Etapa | Denumirea si codul |
| Tip proiect | Pentru care se face comparatia |
| Durata standard curenta | Valoarea din sablon |
| Numar de observatii | Cate proiecte au contribuit |
| Mediana duratei nete | Valoarea propusa |
| Percentila 80 | Pentru promisiuni cu marja |
| Minim si maxim | Sa se vada imprastierea |
| Abatere fata de standard | In zile si in procente |
| Tendinta ultimelor 3 luni | Sageata sus / jos / stabil |
| Actiune | Buton `Aplica propunerea` (numai Head of R&D) |

14.4.3.1 Ecranul afiseaza si un grafic simplu de distributie pe fiecare etapa: cate
proiecte au terminat in 1 zi, in 2 zile si asa mai departe. O distributie cu doua varfuri
(bimodala) semnaleaza ca etapa acopera de fapt doua situatii diferite si ca sablonul
trebuie despartit, nu recalibrat.

### 14.4.4 Aplicarea

| Pas | Ce se intampla |
|---|---|
| 1 | Head of R&D apasa `Aplica propunerea` pe o etapa |
| 2 | Sistemul cere confirmarea si un comentariu (de ce se schimba) |
| 3 | `rd_duratastandard` se actualizeaza in sablon; valoarea veche ramane in audit |
| 4 | Proiectele **existente** nu se recalculeaza. Numai cele acceptate de acum inainte folosesc noua durata |
| 5 | Se noteaza data schimbarii, ca sa se poata separa in rapoarte proiectele de dinainte si de dupa |

14.4.4.1 Pasul 4 este esential. Recalcularea retroactiva a termenelor ar rescrie
indicatorii istorici si ar face imposibila compararea anilor.

## 14.5 Ce se face cu abaterile mari

| Situatie constatata | Interpretare probabila | Actiune |
|---|---|---|
| Durata reala mult peste standard, constant | Standardul a fost optimist de la inceput | Se aplica propunerea |
| Durata reala mult peste standard, doar la un tehnolog | Problema de alocare sau de instruire, nu de standard | Nu se schimba standardul |
| Durata reala mult peste standard, doar in septembrie-decembrie | Sezonalitate | Se ajusteaza factorul de sezonalitate din A1.2.4, nu durata standard |
| Durata reala mult sub standard | Etapa se sare in practica, nu se face mai repede | Se verifica daca etapa mai are sens; poate ca livrabilele ei se fac in alta etapa |
| Imprastiere foarte mare (min 1 zi, max 40) | Etapa acopera doua procese diferite | Se desparte etapa in doua, pe tipuri de proiect diferite |

14.5.1 A patra situatie este cea mai frecventa in practica si cea mai periculoasa: o
etapa care se termina sistematic in jumatate din timpul standard nu inseamna, de obicei,
eficienta, ci ca cineva bifeaza finalul fara sa fi facut continutul. Se verifica intai
livrabilele etapei, apoi se ajusteaza durata.

## 14.6 Prima calibrare

14.6.1 Calendarul realist:

| Moment | Ce se intampla |
|---|---|
| Val 0 | Se seteaza duratele din 14.2, prin discutie cu Managerul R&D si tehnologii |
| Luna 1-6 | Se colecteaza date. Nu se schimba nimic |
| Luna 6 | Prima privire asupra ecranului de calibrare, fara aplicare. Se verifica daca datele au sens si daca startul si finalul etapelor se inregistreaza corect |
| Luna 9-12 | Prima calibrare reala, cu aplicarea propunerilor care indeplinesc conditiile din 14.4.1 |
| Anual | Revizuire, impreuna cu ponderile de prioritizare si cu tintele de indicatori |

14.6.2 NOTA: in primele 3 luni datele vor arata durate mai mari decat realitatea, pentru
ca oamenii inregistreaza cu intarziere si invata sistemul in acelasi timp in care il
folosesc. Aceasta perioada se exclude explicit din prima calibrare - se noteaza data de la
care datele sunt considerate valide si se filtreaza dupa ea.
