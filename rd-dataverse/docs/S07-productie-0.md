# Sectiunea 7 - Productie 0

Compania nu inregistreaza azi nimic structurat la productia 0. Toata sectiunea este
PROPUNERE, construita pe practica de bakery industrial si pe cerintele IFS Food de
validare a procesului (cap. 4.4 si 5.6).

Argument in trei randuri: productia 0 este singurul moment in care se afla daca produsul
dezvoltat in laborator si pe trial este si producibil in conditii reale, la viteza
reala, cu operatorii reali. Fara inregistrari structurate, informatia ramane la
tehnologul care a fost prezent, iar IL-ul si SDP-ul se scriu din memorie. Cu inregistrari,
productia 0 devine sursa de adevar pentru parametrii de proces si baza de comparatie a
revizuirii de la 30 de zile.

## 7.1 Structura inregistrarii

O productie 0 = o inregistrare `rd_productie0` (TBL-33) + N inregistrari
`rd_inregistrareprod0` (TBL-34), pe cinci tipuri: parametru de proces, rebut pe cauza,
problema, masuratoare de ambalare, verificare HACCP. Completarea se face pe telefon, la
linie, in ECR-14.

## 7.2 Cantitati si randament

| Nr | Ce se inregistreaza | Camp | Cum |
|---|---|---|---|
| 7.2.1 | Cantitate planificata (kg si bucati) | rd_cantitateplanificata | Din planul IPN |
| 7.2.2 | Cantitate de aluat introdusa (kg) | rd_aluatintrodus | Cantarire la malaxor, pe sarje |
| 7.2.3 | Numar de sarje | rd_numarsarje | - |
| 7.2.4 | Bucati bune obtinute | rd_bucatibune | Numarate la ambalare |
| 7.2.5 | Cantitate realizata (kg) | rd_cantitaterealizata | bucati bune x gramaj / 1000 |
| 7.2.6 | Randament aluat (%) | rd_randamentaluat | (cantitate realizata / aluat introdus) x 100 |
| 7.2.7 | Randament fata de trial (%) | rd_randamentvstrial | randament productie 0 / randament trial x 100 |
| 7.2.8 | Realizat fata de planificat (%) | rd_realizatvsplan | cantitate realizata / planificata x 100 |

7.2.9 Randamentul aluatului este indicatorul central. Un randament sub 92% la produse
laminate sau sub 95% la produse depuse inseamna, aproape intotdeauna, ca antecalculul a
folosit o pierdere tehnologica prea optimista si ca marja reala este mai mica decat cea
promisa. Diferenta se raporteaza automat catre antecalcul (`rd_costreal`).

## 7.3 Rebutul pe cauze

7.3.1 Rebutul se inregistreaza in kg si in procente, cu cauza din lista predefinita. Nu
exista camp de rebut fara cauza.

| Cod | Cauza | Grupa | Observatii |
|---|---|---|---|
| RB-01 | Capat de banda si pornire de linie | Proces normal | Se asteapta la orice pornire; se urmareste sa nu creasca |
| RB-02 | Setare de linie in curs | Setup | Se cumuleaza cu timpul de setup |
| RB-03 | Greutate in afara tolerantei | Calitate | Semnaleaza probleme de divizare sau laminare |
| RB-04 | Forma sau dimensiune neconforma | Calitate | - |
| RB-05 | Lipire pe banda sau pe forme | Proces | Tipic la aluat prea moale sau ungere insuficienta |
| RB-06 | Rupere sau destramare la manipulare | Proces | - |
| RB-07 | Umplutura iesita sau distribuita neuniform | Proces | Specific produselor injectate |
| RB-08 | Coacere neuniforma sau ardere | Coacere | - |
| RB-09 | Congelare incompleta sau aglomerare | Congelare | Punct critic HACCP |
| RB-10 | Ambalare defectuoasa (sudura, etichetare) | Ambalare | - |
| RB-11 | Corp strain sau contaminare | Siguranta alimentelor | Declanseaza procedura de neconformitate |
| RB-12 | Oprire de linie neplanificata | Mentenanta | Se coreleaza cu timpul de oprire |
| RB-13 | Materie prima neconforma | Materie prima | Se leaga de MP si de furnizor |
| RB-14 | Eroare de operare | Personal | Semnaleaza nevoia de instruire suplimentara |

7.3.2 Se calculeaza automat: rebut total in kg, rebut in procente din cantitatea
introdusa, si distributia pe cauze. Cauza cu ponderea cea mai mare se afiseaza in raport
ca "cauza dominanta".

7.3.3 PROPUNERE de prag: rebut total peste 5% la productia 0 pentru produse laminate,
peste 3% pentru produse depuse. Peste prag, decizia finala nu poate fi `Validat`, ci cel
mult `Validat conditionat`, cu plan de reducere. Motiv: un rebut mare la productia 0, cu
tehnologul prezent si atentia maxima, va fi si mai mare in serie, cand nu mai este nimeni
langa linie.

## 7.4 Viteza si timpii

| Nr | Ce se inregistreaza | Camp | Observatii |
|---|---|---|---|
| 7.4.1 | Viteza nominala a liniei (buc/h) | rd_vitezanominala | Din nomenclatorul de linie |
| 7.4.2 | Viteza reala medie (buc/h) | rd_vitezareala | Bucati / timp efectiv de productie |
| 7.4.3 | Eficienta de viteza (%) | rd_eficientaviteza | reala / nominala x 100 |
| 7.4.4 | Timp de setup (min) | rd_timpsetup | De la eliberarea liniei pana la prima bucata buna |
| 7.4.5 | Timp de schimb de sortiment (min) | rd_timpschimb | Comparat cu cele 120 de minute implicite |
| 7.4.6 | Timp total de ocupare a liniei (min) | rd_timpocupare | Setup + productie + curatare |
| 7.4.7 | Opriri neplanificate (numar si minute) | Inregistrari de tip Problema | Cu cauza |

7.4.8 Eficienta de viteza intra direct in antecalculul revizuit: daca linia merge la 70%
din viteza nominala, costul de manopera si de energie pe kilogram creste cu aproximativ
43%, iar marja calculata initial nu mai este reala. Aceasta este a doua sursa de eroare
de antecalcul, dupa randament.

## 7.5 Parametrii reali de proces fata de cei specificati

7.5.1 Pentru fiecare faza se inregistreaza valoarea specificata (din SDP), valoarea reala
si abaterea. Abaterea in afara tolerantei se marcheaza automat si intra in numarul de
abateri.

| Faza | Parametri urmariti | Tolerante tipice |
|---|---|---|
| Framantare | Timp la viteza 1 si 2, temperatura finala a aluatului, consistenta | Temperatura +/- 1 C |
| Fermentare | Timp, temperatura, umiditate | Timp +/- 10%, temperatura +/- 1 C |
| Laminare | Numar de ture, grosime finala, temperatura grasimii, temperatura camerei | Grosime +/- 0.2 mm |
| Formare si divizare | Greutate la divizare, dimensiuni, viteza de taiere | Greutate conform 6.2.1 |
| Dospire | Timp, temperatura, umiditate, inaltime atinsa | Timp +/- 10%, temperatura +/- 1 C |
| Coacere | Temperatura pe zone, timp, aburire, viteza benzii | Temperatura +/- 5 C |
| Congelare | Temperatura tunelului, timp, temperatura in centrul produsului la iesire | Centru sub -18 C, obligatoriu |
| Ambalare | Greutate neta, sudura, etichetare, temperatura in zona de ambalare | Vezi 7.6 |

7.5.2 Temperatura in centrul produsului la iesirea din congelator este punct critic
HACCP. Se masoara pe minimum 5 bucati, din zonele cele mai defavorabile ale sarjei, si
este eliminatorie: o singura valoare peste -18 C opreste validarea, indiferent de restul
raportului.

7.5.3 Parametrii reali confirmati la productia 0 sunt cei care intra in SDP si in IL-ul
de productie. Daca parametrii reali difera semnificativ de cei din SDP, SDP-ul se
actualizeaza cu versiune noua inainte de inchiderea proiectului - nu se lasa specificatia
sa contrazica realitatea de pe linie.

## 7.6 Greutatea la ambalare si toleranta

| Nr | Ce se inregistreaza | Observatii |
|---|---|---|
| 7.6.1 | Greutate medie pe bucata | Minimum 20 de bucati, in 4 prelevari |
| 7.6.2 | Abatere standard si CV | Vezi 6.2.3 |
| 7.6.3 | Abatere de la gramajul declarat (%) | (medie - declarat) / declarat x 100 |
| 7.6.4 | Numar de bucati sub gramajul minim admis | Cerinta legala |
| 7.6.5 | Greutate neta pe ambalaj | Minimum 5 ambalaje |
| 7.6.6 | Supraumplere medie (%) | Cat se da gratis clientului |

7.6.7 Supraumplerea este un cost ascuns semnificativ. La un produs de 80 g cu 3%
supraumplere si 500 de tone pe an, se dau gratis 15 tone de produs. Se raporteaza explicit
in raportul de productie 0 si in revizuirea de la 90 de zile.

## 7.7 Conformitatea cu punctele critice HACCP

7.7.1 Se inregistreaza, ca inregistrari de tip `Verificare HACCP`, fiecare CCP si oPRP
din planul HACCP actualizat pentru produs, cu: valoarea limita, valoarea masurata,
momentul, cine a verificat, conform da / nu, actiunea corectiva la deviatie.

7.7.2 Punctele critice tipice pentru bakery congelat: temperatura in centru la iesirea
din congelare; detectia de metale sau raze X, daca linia are; temperatura camerei de
ambalare; integritatea sitelor la faina; controlul alergenilor la schimbarea de sortiment.

7.7.3 O singura neconformitate HACCP nerezolvata blocheaza decizia `Validat` si
declanseaza procedura de neconformitate a companiei. Sistemul nu permite inchiderea
productiei 0 cu un CCP neconform si fara actiune corectiva completata.

## 7.8 Problemele aparute

7.8.1 Fiecare problema se inregistreaza separat, cu: descriere, momentul aparitiei, faza
afectata, impact (oprire, rebut, calitate), actiune corectiva imediata, actiune
preventiva propusa, responsabil, termen, status. Poza este incurajata si se ataseaza din
telefon.

7.8.2 Problemele cu actiune deschisa la momentul deciziei finale fac imposibila decizia
`Validat`. Se accepta `Validat conditionat`, cu lista actiunilor si termenele lor.

## 7.9 Decizia finala

| Decizie | Conditii | Consecinta |
|---|---|---|
| Validat | Randament peste prag, rebut sub prag, zero abateri HACCP, zero probleme deschise, gramaj conform, evaluare senzoriala Acceptat | Produsul intra in serie; SDP si IL raman ca la productia 0 |
| Validat conditionat | Toate conditiile de siguranta indeplinite, dar exista abateri de proces, rebut peste prag sau actiuni deschise | Produsul intra in serie sub urmarire; lista de conditii cu responsabil si termen; revizuirea de la 30 de zile devine obligatorie |
| Se repeta | Neconformitate HACCP, evaluare senzoriala Respins, randament sub prag critic, sau imposibilitatea de a produce la viteza acceptabila | Nu intra in serie; se planifica o noua productie 0, cu ce se schimba |

7.9.1 Decizia se ia de Managerul R&D impreuna cu Calitatea si Productia. Se
inregistreaza cine a decis si pe ce baza. Decizia `Validat conditionat` fara lista de
conditii nu se poate salva.

## 7.10 Ce indicatori rezulta si cum alimenteaza IL-ul si SDP-ul

### 7.10.1 Indicatori care rezulta din productia 0

| Indicator | Formula | Unde se foloseste |
|---|---|---|
| Randament de proces (%) | Cantitate realizata / aluat introdus | Antecalcul revizuit, comparatie la 30 de zile |
| Rebut la lansare (%) | Rebut / cantitate introdusa | Prag de comparatie pentru serie |
| Eficienta de viteza (%) | Viteza reala / nominala | Costul real de manopera, planificarea capacitatii |
| Timp de setup real (min) | Masurat | Corectia celor 120 de minute implicite din planificare |
| Capabilitate de gramaj | CV al greutatii la ambalare | Decizia de reglare a divizorului |
| Supraumplere (%) | Media reala fata de gramajul declarat | Costul ascuns, urmarit la revizuire |
| Rata de conformitate HACCP (%) | Verificari conforme / total | Intra in Q-Corect |
| Numar de abateri de proces | Numarate | Calitatea specificatiei initiale |

### 7.10.2 Cum alimenteaza IL-ul de productie

Instructiunea de lucru se scrie din parametrii **reali** confirmati la productia 0, nu
din cei teoretici din trial. Concret, IL-ul preia: valorile de proces pe faze cu
tolerantele confirmate; punctele de verificare si frecventa lor, derivate din unde au
aparut abaterile; setarile de linie efective (grosimi, viteze, temperaturi pe zone);
timpul de setup real; cauzele de rebut cele mai frecvente, ca puncte de atentie pentru
operator; si actiunile corective pentru problemele care s-au manifestat.

### 7.10.3 Cum alimenteaza SDP-ul

SDP-ul se actualizeaza cu versiune noua dupa productia 0, daca exista diferente. Preia:
parametrii reali (sectiunea 4 din DOC-07), controalele in proces derivate din 7.7,
randamentul real ca referinta, si datele de ambalare confirmate. Un SDP care nu a fost
confruntat cu o productie 0 este o ipoteza; dupa productia 0 devine specificatie.

7.10.4 NOTA: exista o tentatie de a lasa SDP-ul asa cum a fost aprobat inainte de
implementare, ca sa nu se reia aprobarea. Este exact greseala care produce, peste sase
luni, un IL care contrazice specificatia si o neconformitate la audit. Blueprintul cere
explicit versiune noua de SDP la orice diferenta semnificativa constatata la productia 0,
inainte de trecerea proiectului in `Finalizat`.
