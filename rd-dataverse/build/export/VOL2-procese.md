# Volumul 2 - Procesele de business

Parte din blueprintul Suitei Digitale R&D, export din 09.09.2026.
Contine sectiunile: S06-masuratori-senzorial, S07-productie-0, S08-revizuire-post-implementare, S09-alergeni-nutritionale, S10-ecrane, S11-securitate-roluri, S12-automatizari, S13-indicatori, S14-durate-etape, S15-migrare.

Contextul complet al proiectului este in preambulul din `BLUEPRINT-COMPLET.md`.



<!-- ==================== S06-masuratori-senzorial.md ==================== -->

---

# Sectiunea 6 - Masuratori si evaluare senzoriala

## 6.1 Masuratorile obligatorii

6.1.1 La fiecare trial se inregistreaza obligatoriu: greutate, dimensiuni, aspect,
alveolare, miros, gust. Primele doua sunt numerice, ultimele patru sunt calitative pe
scala Conform / Minor neconform / Neconform, plus scorul senzorial detaliat din 6.5.

6.1.2 Se masoara intre 2 si 5 bucati, sau mai multe pentru gramaj si dimensiuni. Numarul
minim pe tip de verificare este in 6.2.1.

6.1.3 Sistemul calculeaza automat, la fiecare salvare de masuratoare, in tabela
`rd_statisticatrial` (TBL-16b): media, abaterea standard de esantion, coeficientul de
variatie, minimul, maximul, numarul de neconforme si conformitatea fata de toleranta
declarata in fisa de testare.

6.1.4 Formulele, exprimate ca reguli de calcul pentru ca nu pot fi exprimate altfel:

```
medie          = SUMA(valori neexcluse) / n
abatere std    = RADICAL( SUMA((valoare - medie)^2) / (n - 1) )      [esantion, n-1]
CV %           = abatere std / medie * 100
conform bucata = valoare >= (tinta - tol_minus) SI valoare <= (tinta + tol_plus)
conformitate % = numar conforme / n * 100
```

6.1.5 Se foloseste abaterea standard de esantion (n-1), nu de populatie. La 3-5 bucati
diferenta este semnificativa, iar estimarea cu n-1 este cea corecta pentru un esantion
extras dintr-o productie.

## 6.2 Dimensiunea esantionului si valorile aberante

### 6.2.1 PROPUNERE: dimensiunea minima de esantion pe tip de verificare

| Tip de verificare | Esantion minim la trial | Esantion minim la productie 0 | Motiv |
|---|---|---|---|
| Greutate bucata | 10 | 20, in 4 prelevari de cate 5 | Gramajul este cerinta legala si contractuala; la n=5 abaterea standard este prea instabila pentru a decide conformitatea |
| Greutate ambalaj / bax | 3 | 5 | Variabilitate mult mai mica, se cumuleaza erorile individuale |
| Lungime, latime, inaltime | 5 | 10 | Dimensiunea deriva din setarea liniei, nu din variatia bucatii |
| Diametru, grosime | 5 | 10 | Idem |
| Volum sau inaltime dupa coacere | 5 | 10 | Indicator de dospire, foarte sensibil |
| Aspect exterior | 10 (vizual, bucata cu bucata) | 20 | Defectele de aspect apar rar; la n mic nu se detecteaza |
| Alveolare (sectiune) | 3 | 5 | Necesita taierea produsului, e distructiv |
| Miros, gust | 2 | 3 | Evaluare senzoriala separata acopera detaliul |
| Temperatura in centru la congelare | 3 | 5 | Punct critic HACCP; se masoara in zonele cele mai reci ale sarjei |
| Umiditate, Aw, pH | 2 | 3 | Analize de laborator, cost mare pe determinare |

Argument in trei randuri: gramajul si aspectul cer esantioane mari pentru ca sunt
variabile si au consecinte legale sau comerciale; determinarile distructive sau de
laborator cer esantioane mici pentru ca sunt scumpe si au variabilitate intrinseca mica.
Pragurile de mai sus sunt cele uzuale in bakery industrial si se pot ajusta din
nomenclator dupa primele 6 luni de date reale.

### 6.2.2 Ce se intampla sub minimul de esantion

Statistica se calculeaza oricum, dar `rd_verdict` din TBL-16b devine
`Esantion insuficient` si nu poate sustine trecerea livrabilului LIV-11 in `Realizat`.
Tehnologul poate continua, dar nu poate declara testarea realizata. Blocajul este pe
livrabil, nu pe ecran: in hala nu se blocheaza nimeni la jumatatea unei masuratori.

### 6.2.3 Praguri de coeficient de variatie

PROPUNERE, pentru interpretarea automata:

| Tip de masuratoare | CV bun | CV acceptabil | CV problematic |
|---|---|---|---|
| Greutate bucata (produs depus sau injectat) | sub 2% | 2 - 4% | peste 4% |
| Greutate bucata (produs laminat si taiat) | sub 3% | 3 - 5% | peste 5% |
| Dimensiuni liniare | sub 3% | 3 - 6% | peste 6% |
| Inaltime dupa coacere | sub 5% | 5 - 10% | peste 10% |

Argument: un CV bun spune ca procesul este capabil, chiar daca media este deplasata -
media se corecteaza prin setare, imprastierea nu. Un lot cu media perfecta si CV de 8% la
gramaj va produce neconformitati in serie.

### 6.2.4 Tratarea valorilor aberante

6.2.4.1 Regula: **nicio valoare nu se sterge**. Se marcheaza `rd_exclus = Da`, cu motiv
obligatoriu, si ramane vizibila in raport, taiata, cu motivul afisat.

6.2.4.2 Detectarea automata: sistemul semnaleaza vizual, cu pictograma de avertizare,
orice valoare aflata la mai mult de 2 abateri standard de medie, si orice valoare aflata
in afara intervalului [mediana - 1.5 x IQR, mediana + 1.5 x IQR] cand n >= 8. La n < 8,
se semnaleaza doar valorile in afara tolerantei declarate; testele statistice de
aberanta nu au putere la esantioane atat de mici.

6.2.4.3 Motivele admise de excludere sunt din nomenclator: bucata deteriorata la
prelevare; eroare de citire a cantarului; bucata de la pornirea liniei, inainte de
stabilizare; bucata de capat de banda; masuratoare dublata din greseala. Nu exista
motivul "valoare prea diferita". O valoare corect masurata pe o bucata reala nu se
exclude niciodata: ea este exact informatia pentru care se face trialul.

6.2.4.4 Daca dupa excludere raman sub minimul din 6.2.1, verdictul devine
`Esantion insuficient` si se cer masuratori suplimentare.

## 6.3 Conformitatea fata de toleranta

6.3.1 Toleranta se declara in fisa de testare (TBL-14, `rd_tolerante`) si se propaga in
fiecare masuratoare ca tinta, toleranta minus si toleranta plus. Conformitatea pe bucata
este o coloana Calculated.

6.3.2 Verdictul pe tip de masuratoare, in TBL-16b:

| Verdict | Conditie |
|---|---|
| Conform | Conformitate 100% si media in interval si CV in banda "bun" sau "acceptabil" |
| Conform cu observatii | Conformitate >= 90% sau CV in banda "problematic", cu media inca in interval |
| Neconform | Conformitate sub 90%, sau media in afara intervalului de toleranta |
| Esantion insuficient | n sub minimul din 6.2.1 dupa excluderi |

6.3.3 NOTA: pentru gramajul produsului preambalat exista si cerinta legala de cantitate
nominala, care nu este aceeasi cu toleranta tehnologica interna. Toleranta interna trebuie
sa fie mai stransa decat cea legala; verificarea legala se face la ambalare, in productie,
si se documenteaza in SDP la sectiunea 7, nu aici.

## 6.4 Referinta de comparatie

6.4.1 Referinta este obligatorie la deschiderea proiectului. Se alege din: produs al
concurentei, produs actual, mostra de la client, specificatie de la client, sau
inexistenta. `Inexistenta` este o alegere explicita, nu un camp lasat gol.

6.4.2 Cand exista referinta, evaluarea senzoriala se face comparativ: aceleasi criterii,
aceeasi scala, aplicate si produsului dezvoltat, si referintei, in aceeasi sesiune, cu
probele codificate. Diferentele se inregistreaza in `rd_diferenta` si se comenteaza in
raport.

6.4.3 Pentru referinta se inregistreaza si datele obiective disponibile: gramaj, pret de
raft, lista de ingrediente de pe eticheta, valorile nutritionale declarate, poza. Acestea
sustin pozitionarea si sunt necesare la discutia de pret cu clientul.

6.4.4 PROPUNERE: la referinta de tip "Produs al concurentei" se masoara si greutatea si
dimensiunile reale, pe minimum 5 bucati. Motiv: eticheta declara gramajul nominal, iar
produsul concurentei livreaza frecvent sub el; fara masuratoare proprie, tinta de
dezvoltare se fixeaza gresit de la inceput.

## 6.5 Evaluarea senzoriala

### 6.5.1 PROPUNERE: grila profesionala cu criterii ponderate

Scala 1-5, ancorata descriptiv. Ponderile difera pe categorie de produs; suma este 100
pe fiecare categorie. Mai jos, grila pentru foietaj congelat, cea mai relevanta pentru
portofoliul companiei.

**Foietaj (croissant, produse laminate)**

| Cod | Criteriu | Grupa | Pondere | Eliminatoriu sub |
|---|---|---|---|---|
| CR-01 | Volum si inaltime dupa coacere | Aspect exterior | 15 | 2 |
| CR-02 | Forma si regularitate | Aspect exterior | 10 | - |
| CR-03 | Culoarea si uniformitatea cojii | Aspect exterior | 10 | 2 |
| CR-04 | Straturi vizibile in sectiune (foietare) | Structura interna | 20 | 2 |
| CR-05 | Alveolare si uniformitatea miezului | Structura interna | 10 | - |
| CR-06 | Crocanta la exterior | Textura | 10 | - |
| CR-07 | Elasticitate si moliciune la interior | Textura | 10 | - |
| CR-08 | Aroma de unt sau grasime | Aroma si gust | 10 | 2 |
| CR-09 | Gust general si echilibru | Aroma si gust | 5 | 2 |

**Aluat dospit (cozonac, brioche, produse cu umplutura)**

| Cod | Criteriu | Grupa | Pondere | Eliminatoriu sub |
|---|---|---|---|---|
| CR-11 | Volum si dezvoltare | Aspect exterior | 15 | 2 |
| CR-12 | Culoarea cojii | Aspect exterior | 10 | - |
| CR-13 | Structura miezului si uniformitatea alveolelor | Structura interna | 20 | 2 |
| CR-14 | Distributia si cantitatea umpluturii | Structura interna | 15 | 2 |
| CR-15 | Moliciune si revenire la apasare | Textura | 15 | 2 |
| CR-16 | Aroma de fermentare | Aroma si gust | 10 | - |
| CR-17 | Gust general si echilibru dulce | Aroma si gust | 10 | 2 |
| CR-18 | Comportament dupa decongelare la 4 ore | Comportament la utilizare | 5 | - |

Argument in trei randuri: ponderile mari merg la criteriile care decid reclamatia
clientului (foietarea la laminate, structura si umplutura la produsele dospite), nu la
cele usor de masurat. Criteriile eliminatorii sunt cele la care un scor de 1 face
produsul nevandabil indiferent de restul grilei. Grilele se tin in nomenclator si se
ajusteaza dupa un an de date, nu se cimenteaza in aplicatie.

### 6.5.2 Ancorele descriptive

Fiecare criteriu are text pentru 1, 3 si 5. Scorurile 2 si 4 sunt intermediare, fara
text propriu, ca sa nu se ceara evaluatorului o precizie pe care nu o are. Exemplu pe
CR-04:

| Scor | Ancora pentru "Straturi vizibile in sectiune" |
|---|---|
| 1 | Straturile nu se disting; sectiune compacta, aspect de aluat nelaminat sau grasime absorbita complet |
| 3 | Straturi vizibile, dar neuniforme; zone lipite, foietare partiala pe una din laturi |
| 5 | Straturi numeroase, subtiri, clar separate, uniform distribuite pe toata sectiunea |

6.5.2.1 Toate cele 17 criterii au ancore complete in `data/nomenclatoare.json`, sub
`criterii_senzoriale`. Ancorele sunt cea mai importanta parte a grilei: fara ele, doi
evaluatori dau note diferite aceluiasi produs si dezacordul nu este interpretabil.

### 6.5.3 PROPUNERE: numarul de evaluatori

| Situatie | Numar minim | Compozitie |
|---|---|---|
| Trial de rutina, iteratie intermediara | 2 | Tehnolog + inca o persoana din R&D |
| Trial care sustine decizia de a merge mai departe | 3 | Tehnolog, Manager R&D sau alt tehnolog, Calitate |
| Evaluare finala inainte de mostra la client | 5 | R&D (2), Calitate, Productie, KAM sau comercial |
| Evaluare comparativa cu referinta | 5 | Idem, obligatoriu cu probe codificate oarb |
| Panel extins pentru produs de volum mare | 8 - 12 | Panel intern instruit, din mai multe departamente |

Argument: sub 3 evaluatori nu se poate vorbi de dezacord, deci nici de incredere in
verdict; peste 5 evaluatori costul organizarii creste mai repede decat precizia, in afara
lansarilor mari. Numarul se inregistreaza automat, ca Rollup pe evaluarile distincte.

### 6.5.4 Tratarea dezacordurilor

6.5.4.1 Sistemul calculeaza `rd_dezacord` = amplitudinea maxima a scorurilor pe un
singur criteriu (maxim minus minim, intre evaluatori).

| Dezacord maxim | Interpretare | Ce se intampla |
|---|---|---|
| 0 - 1 | Consens | Se trece mai departe |
| 2 | Dezacord normal | Se noteaza, fara actiune |
| 3 sau mai mult | Dezacord semnificativ | Criteriul se marcheaza rosu; se cere o a doua runda pe acel criteriu, cu discutie prealabila despre ancora |

6.5.4.2 Nu se face media peste un dezacord de 3 sau mai mult. O medie de 3 obtinuta din
notele 1 si 5 nu inseamna produs mediu, inseamna ca doi oameni au evaluat lucruri
diferite sau au inteles altfel ancora.

6.5.4.3 Daca dezacordul persista dupa a doua runda, decizia o ia Managerul R&D, cu motiv
scris in `rd_actiuni`. Se pastreaza ambele runde.

### 6.5.5 Verdictul final

Regula de calcul, aplicata automat, cu posibilitatea de a fi inasprita manual, niciodata
inmuiata:

```
scor_ponderat = SUMA(scor_mediu_criteriu * pondere_criteriu) / 100

verdict:
  Respins                  daca exista criteriu eliminatoriu cu scor mediu sub prag
                           SAU exista defect cu severitate Critic
                           SAU scor_ponderat < 3.0
  Acceptat cu observatii   daca scor_ponderat intre 3.0 si 3.9
                           SAU exista defect cu severitate Major
                           SAU dezacord maxim >= 3 nerezolvat
  Acceptat                 daca scor_ponderat >= 4.0 si niciuna din conditiile de mai sus
```

6.5.5.1 La evaluarea comparativa se adauga o conditie: daca `rd_diferenta` (produs minus
referinta) este mai mica de -0.5, verdictul nu poate fi mai bun de `Acceptat cu
observatii`, indiferent de scorul absolut. Motiv: un produs care scoate 4.2 dar sta sub o
referinta de 4.8 nu castiga listarea.

6.5.5.2 Verdictul `Acceptat cu observatii` obliga la completarea campului `rd_actiuni`,
cu ce se modifica si cine raspunde. Fara acel text, evaluarea nu se poate salva ca
finalizata.

## 6.6 Ce se intampla cu formularele Excel actuale

6.6.1 Formularele de masuratori de azi (formular gol greutate, formular masuratori)
dispar ca fisiere. Devin ecrane pe telefon, completate la linie, cu poze atasate:
ECR-11 (masuratori la linie) si ECR-12 (evaluare senzoriala), descrise in Sectiunea 10.

6.6.2 Fisierul se genereaza la cerere din date, prin butonul "Genereaza raport de
testare" (FLX-12), daca cineva il vrea pe hartie sau il trimite clientului. Nu exista
drum invers: nu se incarca fisiere Excel de masuratori inapoi in sistem.

6.6.3 NOTA: exceptia este importul de volume mari, cerut in constrangeri. Pentru
prelevarile de la productia 0, unde se cantaresc 20 de bucati de doua-trei ori pe
schimb, ecranul mobil ramane varianta principala, dar se accepta si un import din Excel
cu doua coloane (numar bucata, valoare), pentru cazul in care cantarul liniei exporta
direct. Formulele in engleza, separator virgula.


<!-- ==================== S07-productie-0.md ==================== -->

---

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


<!-- ==================== S08-revizuire-post-implementare.md ==================== -->

---

# Sectiunea 8 - Revizuirea post-implementare

Nu exista azi ca proces formal. Toata sectiunea este PROPUNERE.

Argument in trei randuri: intre 130 si 180 de proiecte pe an inseamna ca R&D preda
produse in serie fara sa afle niciodata daca ipotezele de cost, randament si volum s-au
confirmat. Revizuirea la 30, 60 si 90 de zile este singurul mecanism care inchide bucla si
alimenteaza cu date reale antecalculul urmatorului proiect. Se declanseaza automat,
altfel nu se face niciodata.

## 8.1 De ce trei momente si nu unul

| Moment | Ce se poate sti deja | Ce nu se poate sti inca |
|---|---|---|
| 30 de zile | Daca produsul se poate produce repetat; primele reclamatii de calitate; randamentul in primele serii; rebutul | Volumul real, comportamentul in raft, costul stabilizat |
| 60 de zile | Daca randamentul s-a stabilizat dupa curba de invatare a operatorilor; costul real pe cateva serii | Sezonalitatea, reactia clientului final |
| 90 de zile | Volumul real fata de estimare; costul real; reclamatiile de la consumator; decizia de continuare | Comportamentul pe un ciclu complet de sezon |

8.1.1 Cele trei momente au greutate diferita. La 30 de zile se verifica productibilitatea;
la 60 costul; la 90 se ia decizia. Numai revizuirea de la 90 de zile este livrabil
obligatoriu (LIV-43).

## 8.2 Ce se inregistreaza la fiecare revizuire

| Nr | Element | Sursa | Obligatoriu la |
|---|---|---|---|
| 8.2.1 | Cantitate produsa cumulat (kg si bucati) | Manual sau import din SAP / planificare | 30, 60, 90 |
| 8.2.2 | Numar de loturi produse | Idem | 30, 60, 90 |
| 8.2.3 | Reclamatii de la client (numar, tip, cantitate afectata) | Calitate | 30, 60, 90 |
| 8.2.4 | Neconformitati interne (numar, tip) | Calitate | 30, 60, 90 |
| 8.2.5 | Randament mediu in serie (%) | Din productie | 30, 60, 90 |
| 8.2.6 | Randament la productia 0 (%) | Automat, din TBL-33 | 30, 60, 90 |
| 8.2.7 | Diferenta de randament (puncte procentuale) | Calculat | 30, 60, 90 |
| 8.2.8 | Rebut mediu in serie (%) | Din productie | 30, 60, 90 |
| 8.2.9 | Rebut la productia 0 (%) | Automat | 30, 60, 90 |
| 8.2.10 | Cost real pe kg | Din controlling sau calculat din consumuri | 60, 90 |
| 8.2.11 | Cost din antecalcul pe kg | Automat, din TBL-22 | 60, 90 |
| 8.2.12 | Abatere de cost (%) | Calculat | 60, 90 |
| 8.2.13 | Volum realizat fata de estimat (%) | KAM | 90 |
| 8.2.14 | Feedback de la client | KAM | 30, 90 |
| 8.2.15 | Feedback de la KAM (pozitionare, pret, concurenta) | KAM | 90 |
| 8.2.16 | Feedback de la Productie (usurinta de operare) | Productie | 30 |
| 8.2.17 | Numar de modificari de reteta sau proces dupa lansare | Automat, din versiuni | 60, 90 |
| 8.2.18 | Decizie | Manager R&D | 90 |

8.2.19 Campurile marcate "Automat" se preiau fara interventie umana din inregistrarile
existente. Numai 6 campuri raman de completat manual la revizuirea de 30 de zile si 9 la
cea de 90. Este limita peste care procesul nu se mai face.

## 8.3 Indicatorii calculati

```
diferenta_randament (pp) = randament_serie - randament_productie_0
abatere_cost (%)         = (cost_real - cost_antecalcul) / cost_antecalcul * 100
realizare_volum (%)      = volum_realizat_anualizat / volum_estimat_anual * 100
rata_reclamatii (ppm)    = cantitate_reclamata / cantitate_produsa * 1.000.000
indice_sanatate          = vezi 8.4
```

8.3.1 Volumul realizat se anualizeaza liniar la 90 de zile (`x 4`) numai pentru produsele
fara sezonalitate declarata. Pentru cele sezoniere, comparatia se face cu volumul estimat
pentru perioada respectiva, nu cu cel anual - altfel un produs de Craciun lansat in
septembrie apare intotdeauna ca subperformant.

## 8.4 PROPUNERE: indicele de sanatate al produsului

Un numar unic, pe 100 de puncte, care spune daca produsul lansat isi tine promisiunile:

| Componenta | Puncte | Cum se acorda |
|---|---|---|
| Cost | 30 | 30 daca abaterea de cost <= 0%; 20 pana la +5%; 10 pana la +10%; 0 peste |
| Volum | 25 | 25 daca realizarea >= 90%; 15 pana la 70%; 5 pana la 50%; 0 sub |
| Calitate | 25 | 25 daca zero reclamatii; 15 la sub 100 ppm; 5 la sub 500 ppm; 0 peste |
| Producibilitate | 20 | 20 daca diferenta de randament >= -1 pp; 10 pana la -3 pp; 0 sub |

Argument: fara un numar unic, revizuirea produce zece cifre pe care nimeni nu le compara
intre produse. Cu el, se poate face lista celor 10 produse lansate anul trecut care merita
optimizate si a celor 3 care ar trebui retrase.

8.4.1 Interpretare: peste 75 = mentinere; 50-75 = optimizare; sub 50 = candidat la
retragere. Indicele este orientativ, nu decide singur; decizia ramane la Managerul R&D.

## 8.5 Decizia

| Decizie | Cand | Ce declanseaza |
|---|---|---|
| Mentinere | Produsul isi tine promisiunile de cost, volum si calitate | Se inchide revizuirea; produsul iese din urmarirea R&D |
| Optimizare | Abatere de cost peste 5%, sau randament sub asteptari, sau reclamatii recurente | Se deschide automat un proiect nou de tip `Optimizare cost` sau `Reformulare`, legat de proiectul initial, cu prioritate mostenita |
| Retragere | Volum sub 50% din estimare, sau cost care face marja negativa, sau probleme de calitate nerezolvabile | Se notifica KAM si comercialul; decizia de retragere se ia in afara R&D, dar se inregistreaza aici |

8.5.1 Decizia `Optimizare` care creeaza automat un proiect nou este mecanismul prin care
revizuirea nu ramane un document. Proiectul nou mosteneste clientul, linia, reteta si
referinta, si intra in coada cu scorul calculat normal.

## 8.6 Declansarea automata

8.6.1 Ceasul porneste de la `rd_implementare.rd_dataimplementare`, adica data primei
productii in serie (nu data productiei 0).

8.6.2 FLX-15 se executa zilnic si:

| Pas | Actiune |
|---|---|
| 1 | Cauta implementarile cu data completata si fara revizuire creata pentru pragul curent |
| 2 | Creeaza inregistrarea `rd_revizuire` cu etapa (30 / 60 / 90) si data scadenta |
| 3 | Creeaza livrabilul corespunzator (LIV-41 / 42 / 43) |
| 4 | Precompleteaza toate campurile automate din 8.2 |
| 5 | Trimite sarcina catre Managerul R&D si cererile de date catre KAM, Calitate si Productie |
| 6 | Trece proiectul in status `In revizuire` daca era `Finalizat` |

8.6.3 Reamintiri: la data scadenta, la +7 zile si la +14 zile. La +21 de zile,
escaladare catre Head of R&D. O reviziune ramasa neefectuata mai mult de 30 de zile se
inchide automat cu status `Sarita` si motiv, si intra in raportul anual - se vede ca nu
s-a facut, nu dispare.

## 8.7 Cine raspunde

| Element | Responsabil de furnizare | Termen |
|---|---|---|
| Cantitate produsa, loturi, randament, rebut | Productie / Planificare | 5 zile de la cerere |
| Reclamatii si neconformitati | Calitate | 5 zile |
| Cost real | Controlling / Financiar | 10 zile |
| Volum realizat si feedback client | KAM | 5 zile |
| Sinteza, indice, decizie | Manager R&D | 15 zile de la data scadenta |
| Aprobarea deciziei la 90 de zile | Head of R&D | 20 de zile |

8.7.1 NOTA: revizuirea depinde de date din afara R&D (cost real, cantitati produse,
reclamatii). Daca aceste date nu vin, revizuirea nu se poate face si vina nu este a R&D.
Din acest motiv, campurile nefurnizate se marcheaza explicit ca `Date indisponibile`, cu
departamentul care nu le-a furnizat, si apar ca atare in raportul anual. Este singurul
mod in care lipsa de cooperare devine vizibila fara sedinte.

## 8.8 Ce se vede in aplicatie

8.8.1 Un tablou de bord `Produse lansate`, cu: produsul, data implementarii, indicele de
sanatate, abaterea de cost, realizarea de volum, numarul de reclamatii, decizia. Sortabil
si filtrabil pe an, client, linie si tehnolog.

8.8.2 Un raport anual `Ce am invatat`, care agrega abaterile de cost si de randament pe
categorie de produs si pe linie. Acesta este documentul care corecteaza, dupa un an,
ipotezele implicite de antecalcul si pierderea tehnologica din 5.5.6.


<!-- ==================== S09-alergeni-nutritionale.md ==================== -->

---

# Sectiunea 9 - Alergeni si valori nutritionale

Principiul: se calculeaza din reteta, nu se copiaza din ST-urile furnizorilor. ST-ul
furnizorului este sursa de date pentru **materia prima**; declaratia produsului finit este
rezultatul calculului pe reteta.

## 9.1 Datele necesare la nivel de materie prima

9.1.1 Fara datele de mai jos, complete, materia prima nu poate intra intr-o reteta care
sustine o eticheta. Se valideaza la aprobarea materiei prime de catre Calitate.

| Nr | Data | Camp in TBL-09 | Sursa | Obligatoriu |
|---|---|---|---|---|
| 9.1.1.1 | Alergeni continuti | rd_alergeni | ST furnizor, declaratie de alergeni | Da |
| 9.1.1.2 | Alergeni prezenti ca urme | rd_alergeniurme | Declaratie de contaminare incrucisata a furnizorului | Da |
| 9.1.1.3 | Energie (kcal si kJ / 100 g) | rd_energie | ST furnizor | Da |
| 9.1.1.4 | Grasimi (g / 100 g) | rd_grasimi | ST furnizor | Da |
| 9.1.1.5 | Acizi grasi saturati | rd_saturate | ST furnizor | Da |
| 9.1.1.6 | Glucide | rd_glucide | ST furnizor | Da |
| 9.1.1.7 | Zaharuri | rd_zaharuri | ST furnizor | Da |
| 9.1.1.8 | Fibre | rd_fibre | ST furnizor | Nu (optional pe eticheta) |
| 9.1.1.9 | Proteine | rd_proteine | ST furnizor | Da |
| 9.1.1.10 | Sare | rd_sare | ST furnizor | Da |
| 9.1.1.11 | Umiditate | rd_umiditate | ST furnizor sau determinare interna | Da, pentru calculul pierderii la coacere |
| 9.1.1.12 | Denumirea legala pentru lista de ingrediente | rd_denumirelegala | Reglementare + ST | Da |
| 9.1.1.13 | Ingrediente compuse (daca MP este un compus) | rd_ingredientecompuse | ST furnizor | Da, daca este cazul |
| 9.1.1.14 | Data ST-ului furnizorului | rd_datast | - | Da |
| 9.1.1.15 | Origine | rd_origine | ST furnizor | Nu, doar unde se declara |

9.1.2 Validare de plauzibilitate la salvare: suma grasimi + glucide + fibre + proteine +
sare + umiditate trebuie sa fie intre 95 si 105 g / 100 g. In afara acestui interval,
sistemul avertizeaza - de obicei inseamna o eroare de transcriere din ST.

9.1.3 ST-ul furnizorului mai vechi de 24 de luni marcheaza materia prima cu semnal galben
si o raporteaza in lista `Materii prime cu specificatie expirata`. Este cerinta IFS de
actualizare a specificatiilor de intrare.

9.1.4 Ingredientele compuse (de exemplu un ameliorator care contine faina de malt, enzime
si acid ascorbic) se inregistreaza cu componentele lor, pentru ca lista de ingrediente de
pe eticheta trebuie sa le declare in paranteza, nu sub numele comercial.

## 9.2 Modul de calcul

### 9.2.1 Valori nutritionale

```
Pentru fiecare nutrient N si fiecare linie de reteta i:
  contributie_i(N) = cantitate_i (kg/100 kg) * valoare_i(N) / 100

Valoare in aluat (per 100 g de aluat):
  valoare_aluat(N) = SUMA(contributie_i(N))

Corectie de pierdere la coacere (concentrare prin evaporarea apei):
  factor_randament = masa_produs_finit / masa_aluat        [din trial sau productia 0]
  valoare_finit(N) = valoare_aluat(N) / factor_randament

Exceptie pentru apa si umiditate:
  umiditate_finit = (masa_apa_aluat - apa_evaporata) / masa_produs_finit * 100
```

9.2.1.1 Energia nu se preia ca suma directa, ci se recalculeaza din macronutrienti, cu
factorii legali de conversie: grasimi 9 kcal/g, glucide 4, proteine 4, fibre 2,
polioli 2.4, alcool 7, acizi organici 3. Motiv: sumarea energiilor declarate de furnizori
propaga rotunjirile lor si produce, tipic, o abatere de 3-5% fata de valoarea corecta.

9.2.1.2 Factorul de randament este cel mai delicat element al calculului. Se preia, in
ordinea de preferinta: din productia 0 daca exista; altfel din trialul validat; altfel
din valoarea implicita pe categorie de produs, din nomenclator, marcata explicit ca
estimare. Valorile nutritionale calculate cu factor estimat se marcheaza vizual si nu pot
sustine o eticheta aprobata.

9.2.1.3 Rotunjirea pe eticheta urmeaza regulile din ghidul de aplicare a Reg. 1169/2011:
energia la numar intreg; grasimi, saturate, glucide, zaharuri, fibre si proteine la o
zecimala sub 10 g si la numar intreg peste; sarea la doua zecimale sub 1 g. Rotunjirea se
aplica la afisare, nu la stocare - in baza de date raman valorile complete.

### 9.2.2 Alergeni

```
alergeni_produs = REUNIUNEA( alergeni_continuti(MP_i) ) pentru toate liniile de reteta

urme_produs = REUNIUNEA( urme_declarate(MP_i) )
              + alergeni introdusi de linia de productie (vezi 9.4)
              MINUS alergenii deja continuti (un alergen continut nu se declara si ca urma)
```

9.2.2.1 Calculul alergenilor este o reuniune, nu o suma: nu exista prag sub care un
alergen continut nu se declara. Un gram de faina de grau intr-o tona de produs face
produsul purtator de gluten.

9.2.2.2 Alergenii se propaga si prin ingredientele compuse. Daca un ameliorator contine
faina de malt de orz, alergenul `Cereale cu gluten` se propaga chiar daca eticheta
comerciala a amelioratorului nu il scoate in evidenta.

## 9.3 Declaratia pe eticheta

9.3.1 Lista de ingrediente se genereaza automat, in ordine descrescatoare a cantitatii in
aluat, cu denumirile legale, cu ingredientele compuse in paranteza si cu alergenii
evidentiati tipografic (majuscule sau bold, consecvent pe toata eticheta).

9.3.2 Ordinea se calculeaza pe cantitatile din reteta, la momentul framantarii, nu pe
cele din produsul finit. Apa adaugata se declara daca depaseste 5% din produsul finit.

9.3.3 Textul generat este propunere, nu eticheta finala. Aprobarea ramane la Calitate,
care verifica formularea legala. Sistemul genereaza continutul; responsabilitatea juridica
ramane umana.

9.3.4 NOTA: solutia nu inlocuieste o baza de date de specificatii de alergeni certificata
si nu emite declaratii legale. Genereaza propunerea din datele introduse; corectitudinea
datelor de intrare este responsabilitatea celui care le introduce, iar acest lucru se
declara explicit in procedura.

## 9.4 Contaminarea incrucisata si urmele

9.4.1 Urmele au trei surse, tratate distinct:

| Sursa | Cum se determina | Unde se stocheaza |
|---|---|---|
| Urme declarate de furnizor pentru materia prima | Din declaratia furnizorului | rd_materieprima.rd_alergeniurme |
| Urme din linia de productie (produse anterioare pe aceeasi linie) | Din analiza de linie a Calitatii | Camp `rd_alergeniilinie` pe TBL-36 |
| Urme din amplasament (praf de faina, manipulare comuna) | Din evaluarea de risc a amplasamentului | Parametru global pe amplasament |

9.4.2 Declaratia `Poate contine` se genereaza din reuniunea celor trei, minus alergenii
deja declarati ca fiind continuti. Este supusa aprobarii Calitatii si nu se genereaza
automat pe eticheta fara aceasta aprobare.

9.4.3 PROPUNERE: declaratia de urme se face numai dupa o evaluare de risc documentata, nu
preventiv. Motiv: declararea defensiva a tuturor celor 14 alergeni ca posibile urme
inchide accesul la clienti si contrazice practica IFS, care cere ca declaratia sa fie
justificata de un risc real, evaluat, si gestionata prin curatare si secventiere, nu prin
text pe ambalaj.

9.4.4 Matricea de secventiere pe linie: pentru fiecare linie se retine ce alergeni au fost
prelucrati si ce protocol de curatare exista intre sortimente. Cand un produs nou intra pe
o linie, sistemul semnaleaza ce alergeni ar putea aparea ca urme si cere decizia
Calitatii, in cadrul livrabilului LIV-34 (plan HACCP).

## 9.5 Recalcularea automata

9.5.1 FLX-13 recalculeaza alergenii si valorile nutritionale, in urmatoarele situatii:

| Declansator | Ce se recalculeaza | Ce se notifica |
|---|---|---|
| Se adauga, se modifica sau se sterge o linie de reteta | Versiunea de reteta afectata | Tehnologul |
| Se modifica datele nutritionale sau de alergeni ale unei materii prime din catalog | Toate versiunile de reteta nevalidate care o folosesc | Tehnologii proiectelor afectate |
| Idem, pe o materie prima folosita intr-o reteta **validata** | Nimic automat: se genereaza o alerta de impact | Calitate si Head of R&D, vezi 9.5.2 |
| Se schimba factorul de randament (productie 0 finalizata) | Versiunea de reteta a produsului | Tehnologul |
| Se schimba furnizorul unei materii prime | Se compara alergenii vechi cu cei noi | Calitate, daca difera |

9.5.2 Regula critica: o reteta validata nu se recalculeaza tacit. Daca datele unei
materii prime se schimba dupa validare, sistemul nu modifica valorile de pe eticheta
aprobata; genereaza o alerta de impact care listeaza toate produsele afectate si cere o
decizie explicita: reteta noua, eticheta noua, sau confirmarea ca schimbarea nu afecteaza
declaratia. Recalcularea automata a unei etichete deja tiparite ar face imposibila
reconstituirea a ceea ce era declarat pe produsul livrat la o data din trecut.

9.5.3 Alerta de impact este cel mai valoros mecanism din aceasta sectiune: la schimbarea
unui furnizor de ameliorator care introduce faina de malt de orz, sistemul spune imediat
care dintre cele 400 de produse din portofoliu isi schimba declaratia de alergeni. Astazi
raspunsul la aceasta intrebare cere zile de munca manuala.

9.5.4 Fiecare recalculare scrie `rd_datacalcul` pe versiunea de reteta. O versiune al carei
calcul este mai vechi decat ultima modificare a unei materii prime componente se
marcheaza `Calcul invechit` si nu poate sustine aprobarea unei etichete.

## 9.6 Ce se afiseaza in aplicatie

9.6.1 Pe formularul versiunii de reteta, o fila `Alergeni si nutritionale` cu: tabelul
nutritional calculat pe 100 g de produs finit; lista alergenilor continuti, cu materia
prima care ii aduce pe fiecare (trasabilitatea alergenului); lista urmelor, cu sursa;
factorul de randament folosit si de unde provine; data ultimului calcul.

9.6.2 Trasabilitatea alergenului - "de ce apare soia in acest produs" - se raspunde cu un
click, pana la linia de reteta si materia prima care il introduce. Este intrebarea cea mai
frecventa la audit si la reclamatie.

9.6.3 Un raport transversal `Portofoliu pe alergeni`, care raspunde la intrebarea inversa:
care produse contin un anumit alergen. Necesar la orice cerinta de client care exclude un
alergen, si la orice retragere de produs.


<!-- ==================== S10-ecrane.md ==================== -->

---

# Sectiunea 10 - Ecranele aplicatiilor

Doua aplicatii: `R&D Birou` (model-driven) si `R&D Linie` (canvas, mobil). Regula de
departajare: daca activitatea se face stand jos, cu tastatura, este model-driven; daca se
face in picioare, cu manusi, este canvas.

## 10.1 Aplicatia model-driven `R&D Birou`

### 10.1.1 Harta de site

| Grup | Element | Tabela / tip | Cine il foloseste |
|---|---|---|---|
| **Lucrul meu** | Proiectele mele | rd_proiect, vizualizare filtrata | Tehnolog |
| | Livrabilele mele scadente | rd_livrabil | Toti |
| | Solicitarile mele | rd_solicitare | KAM |
| | Aprobarile mele | Vizualizare de sarcini | Manager R&D, Calitate |
| **Solicitari** | Solicitari in triaj | rd_solicitare | Manager R&D |
| | Toate solicitarile | rd_solicitare | KAM, Manager R&D |
| | Solicitari amanate | rd_solicitare | Manager R&D |
| **Proiecte** | Proiecte active | rd_proiect | Toti |
| | Coada pe prioritate | rd_proiect, grupat pe banda | Manager R&D, comercial |
| | Coada pe linie | rd_proiect, grupat pe linie | Manager R&D, Planificare |
| | Proiecte blocate | rd_proiect | Manager R&D |
| | Proiecte in intarziere | rd_proiect | Manager R&D, Head of R&D |
| | Arhiva (respinse, abandonate) | rd_proiect | Toti |
| **Executie** | Fise de testare | rd_fisatestare | Tehnolog |
| | Trialuri | rd_trial | Tehnolog |
| | Evaluari senzoriale | rd_evaluaresenzoriala | Tehnolog |
| | Retete si versiuni | rd_reteta | Tehnolog |
| | Antecalcule | rd_antecalcul | Tehnolog, Manager R&D |
| **Materii prime** | MP de proiect in asteptare | rd_mpproiect | Achizitii, Tehnolog |
| | Catalog de materii prime | rd_materieprima | Toti |
| | Furnizori | rd_furnizor | Achizitii, Calitate |
| | Iteratii de furnizor | rd_iteratiefurnizor | Achizitii |
| | MP cu specificatie expirata | rd_materieprima | Calitate |
| **Mostre** | Cereri de mostra | rd_ceremostra | Suport R&D |
| | Livrari in curs | rd_miscaremostra | Suport R&D |
| **Implementare** | IPN in pregatire | rd_implementare | Tehnolog, Productie |
| | Productii 0 | rd_productie0 | Tehnolog, Productie |
| | Revizuiri scadente | rd_revizuire | Manager R&D |
| **Specificatii** | Specificatii tehnice | rd_specificatie | Calitate |
| | SDP | rd_sdp | Calitate, Productie |
| | Etichete | rd_eticheta | Suport R&D, Calitate |
| **Tablouri de bord** | Tablou operational R&D | Dashboard | Manager R&D |
| | Incarcare tehnologi | Dashboard | Manager R&D |
| | Status public | Dashboard | Toata compania |
| | Indicatori | Dashboard | Head of R&D |
| **Configurare** | Sabloane de livrabile | rd_sablonlivrabil | Head of R&D |
| | Sabloane de etape | rd_sablonetapa | Head of R&D |
| | Linii de productie | rd_linie | Head of R&D |
| | Clienti | rd_client | Head of R&D, comercial |
| | Profiluri de tehnolog | rd_profiltehnolog | Head of R&D |
| | Criterii senzoriale | rd_criteriusenzorial | Head of R&D |
| | Motive si nomenclatoare | rd_motiv, rd_tipdocument | Head of R&D |
| | Parametri de prioritizare | Setari de mediu | Head of R&D |

### 10.1.2 ECR-01 Formularul de proiect

Formularul principal, cu antet permanent vizibil si file. Antetul (maximum 5 campuri,
limita platformei): cod proiect, status, tehnolog, termen negociat, banda de prioritate.

| Fila | Continut | Note |
|---|---|---|
| Sinteza | Client, produs, tip, linie, gramaj, volum, referinta, cele trei termene, urmatorul livrabil si cine il datoreaza, procentul de livrabile realizate, zilele blocate | Ecranul pe care il vede toata lumea |
| Livrabile | Subgrila cu livrabilele aplicabile, grupate pe faza, cu status colorat, termen si responsabil | Editare rapida in grila |
| Etape | Subgrila cu etapele, planificat fata de real, cu bara vizuala | - |
| Materii prime | Subgrila MP de proiect, cu status de ciclu, ETA si semnal de intarziere | Achizitii lucreaza aici |
| Testare | Fise de testare, trialuri, sinteza statistica a ultimului trial | - |
| Senzorial | Evaluari, scor ponderat, verdict, comparatie cu referinta | - |
| Reteta si cost | Versiunea curenta de reteta, antecalculul aprobat, marja | - |
| Specificatii | ST-uri, SDP, etichete, cu status si versiune | Calitate lucreaza aici |
| Implementare | IPN, conditii, productie 0, decizie | - |
| Documente | Controlul de documente SharePoint, cu arborele de foldere | Integrare nativa |
| Blocaje | Subgrila de blocaje, cu impactul cumulat | - |
| Istoric | Audit history si cronologia proiectului | Pentru audit |

10.1.2.1 Butoane pe bara de comenzi: `Accepta proiectul` (genereaza cod, folder,
livrabile, etape, termen propus), `Creeaza proiect-copil`, `Adauga blocaj`,
`Genereaza dosar TDV`, `Genereaza document` (alege sablonul), `Recalculeaza termenul`,
`Reatribuie tehnologul`.

### 10.1.3 ECR-02 Ecranul de triaj

Vizualizare de solicitari in status `Trimisa`, cu formular lateral care arata tot SCP-ul
pe un ecran, fara derulare. Trei butoane mari: Accepta, Respinge, Amana. Fiecare deschide
un dialog care cere motivul (obligatoriu la respingere si amanare) si, la acceptare,
propune tehnologul si termenul calculate de sistem, cu posibilitatea de a le schimba.

10.1.3.1 In dialogul de acceptare se afiseaza, langa fiecare tehnolog propus: numarul de
proiecte active, cate sunt P1, gradul de incarcare cu semnal color, si specializarea.
Aceasta este cerinta din 4.2: la alocare, managerul vede incarcarea.

### 10.1.4 ECR-03 Tabloul de bord operational R&D

| Componenta | Continut |
|---|---|
| Proiecte pe status | Grafic de bare, click pentru drill-down |
| Coada pe banda de prioritate | P1-P4, cu numarul si volumul cumulat |
| Incarcarea pe tehnolog | Bare orizontale cu prag, colorate verde / galben / rosu |
| Coada pe linie | Cele 9 linii, cu numarul de proiecte si primul slot liber estimat |
| Livrabile scadente in 7 zile | Lista, cu responsabil |
| Livrabile depasite | Lista, sortata dupa zile de intarziere |
| Proiecte blocate | Cu sursa blocajului si zilele cumulate |
| Materii prime cu ETA depasit | Lista, cu furnizorul |

### 10.1.5 ECR-04 Ecranul public de status

Cerinta: vizibil intregii companii, read-only, lizibil de oricine, fara instruire.

10.1.5.1 Un singur ecran, cu o singura lista si patru filtre mari (client, linie,
tehnolog, status). Coloanele: cod proiect, produs, client, status cu pastila colorata,
termen catre client, responsabil, urmatorul pas. Fara jargon: statusurile se afiseaza cu
denumirile din 2.2.1, care sunt deja in limbaj natural.

10.1.5.2 Sus, patru numere mari: proiecte active, proiecte finalizate luna aceasta,
proiecte in intarziere, proiecte blocate. Fara grafice complicate.

10.1.5.3 Regula de proiectare: cineva din productie sau din financiar trebuie sa poata
raspunde la intrebarea "unde este produsul X pentru clientul Y" in mai putin de 15
secunde, fara sa fi vazut vreodata aplicatia. Se testeaza cu doi oameni din afara R&D
inainte de publicare (criteriu de acceptanta CA-42).

10.1.5.4 NOTA: ecranul public este o aplicatie model-driven separata, cu un singur tabel
si un rol de securitate de citire. Nu se da acces la aplicatia principala cu drepturi
reduse - riscul de a expune accidental costuri si marje este prea mare.

### 10.1.6 ECR-05 Ecranul de prioritizare

Lista proiectelor cu scorul detaliat pe componente (volum, client, termen, efort, risc
MP, reutilizare), banda rezultata, si butonul `Suprascrie scorul` disponibil doar rolului
de manager operational / vanzari. Suprascrierea deschide un dialog care cere scorul nou
si motivul, si afiseaza bugetul de urgenta consumat de KAM-ul respectiv.

### 10.1.7 Alte ecrane model-driven

| Cod | Ecran | Continut |
|---|---|---|
| ECR-06 | Formular de solicitare (SCP) | Cele 10 sectiuni din 5.5.1, in trei file |
| ECR-07 | Formular de materie prima de proiect | Ciclul MP cu bara de progres pe cele 11 statusuri, campurile de Achizitii separate vizual |
| ECR-08 | Formular de antecalcul | Liniile de cost in grila editabila, cu totalul si marja recalculate live |
| ECR-09 | Formular de versiune de reteta | Liniile de reteta cu totalul de 100 kg validat, plus fila de alergeni si nutritionale |
| ECR-10 | Formular de revizuire post-implementare | Campurile automate precompletate, cele manuale grupate pe furnizorul de date |

## 10.2 Aplicatia canvas `R&D Linie`

### 10.2.1 Principii de proiectare pentru hala

| Principiu | Aplicare concreta |
|---|---|
| Tinta de atins cu manusi | Butoane de minimum 64 x 64 px, spatiere de minimum 12 px |
| Contrast ridicat | Text de minimum 18 px, contrast peste 7:1, fara gri pe gri |
| Minim de tastare | Numere din tastatura numerica mare; alegeri din butoane, nu din liste derulante |
| Conexiune slaba | Colectie locala, salvare in coada, sincronizare cand revine semnalul |
| O mana libera | Toate actiunile principale in treimea de jos a ecranului |
| Fara derulare la introducere | Un ecran = o intrebare sau un set scurt |
| Confirmare vizibila | Dupa salvare, confirmare mare, verde, 2 secunde |

10.2.1.1 Modul offline: aplicatia foloseste `SaveData` / `LoadData` pentru colectiile de
masuratori si pentru contextul proiectului. La pornire incarca proiectele active ale
utilizatorului si nomenclatoarele necesare. Fiecare salvare merge intr-o coada locala; un
indicator permanent arata cate inregistrari asteapta sincronizarea.

10.2.1.2 NOTA de platforma: Power Apps canvas nu poate crea offline inregistrari care au
nevoie de un ID generat de server (Autonumber). Din acest motiv, trialul si evaluarea se
creeaza online, in birou sau la intrarea in hala, iar in offline se adauga doar copii
(masuratori, scoruri, inregistrari de productie 0) la inregistrari care exista deja.
Aceasta constrangere trebuie respectata in proiectarea ecranelor, altfel sincronizarea
esueaza tacit.

### 10.2.2 ECR-11 Masuratori la linie

| Ecran | Continut | Actiuni |
|---|---|---|
| 11.1 Selectie | Lista proiectelor active ale utilizatorului, cu cod si produs, cautare rapida | Alege proiectul |
| 11.2 Selectie trial | Trialurile deschise; buton mare `Trial nou` | Alege sau creeaza |
| 11.3 Alege ce masor | Sase butoane mari: Greutate, Dimensiuni, Aspect, Alveolare, Miros, Gust | - |
| 11.4 Introducere numerica | Numarul bucatii afisat mare; tastatura numerica; tinta si toleranta afisate deasupra; culoare verde / rosu instantaneu; contor "bucata 3 din 10" | Salveaza si urmatoarea; Poza; Inapoi |
| 11.5 Introducere calitativa | Trei butoane: Conform, Minor neconform, Neconform; camp de observatie optional | Salveaza; Poza |
| 11.6 Sinteza | Media, abaterea standard, min, max, conformitatea, cu semnal color; lista valorilor, cu cele semnalate ca posibil aberante marcate | Exclude o valoare (cere motiv); Finalizeaza |

10.2.2.1 Ecranul 11.4 este cel mai folosit din toata solutia. Fluxul optim: se citeste
valoarea de pe cantar, se tasteaza, se apasa un singur buton, se trece automat la bucata
urmatoare. Trei atingeri pe bucata, nu mai mult.

### 10.2.3 ECR-12 Evaluare senzoriala

| Ecran | Continut |
|---|---|
| 12.1 Selectie | Proiect si trial; daca exista referinta, se anunta ca evaluarea este comparativa |
| 12.2 Instructiuni | Conditiile de degustare, codificarea probelor |
| 12.3 Criteriu | Un criteriu pe ecran: denumirea mare, ancorele pentru 1, 3 si 5 afisate ca text scurt, cinci butoane mari de scor; camp de comentariu care apare automat la scor 1 sau 2 |
| 12.4 Comparativ | Acelasi criteriu, aplicat referintei, imediat dupa; cele doua scoruri raman vizibile |
| 12.5 Defecte | Lista de defecte bifabile, grupate, cu severitate si procent |
| 12.6 Sinteza | Scor ponderat, comparatia cu referinta, verdictul propus de sistem, camp de actiuni |

10.2.3.1 Ancorele descriptive se afiseaza pe ecran, la fiecare criteriu. Este singura
modalitate prin care grila din 6.5 functioneaza in practica: un evaluator nu retine 17
seturi de ancore, dar le citeste in doua secunde daca sunt in fata lui.

### 10.2.4 ECR-13 Receptie de mostra

| Ecran | Continut |
|---|---|
| 13.1 Scanare sau selectie | Cerere de mostra din lista celor asteptate; scanare de cod de bare de pe AWB daca exista |
| 13.2 Verificare | Cantitate primita, temperatura la receptie (obligatorie pentru congelat), stare a ambalajului |
| 13.3 Conformitate | Conform / Neconform, cu motiv si poza obligatorie la neconform |
| 13.4 Confirmare | Salvare, cu actualizarea automata a statusului MP si notificarea tehnologului |

### 10.2.5 ECR-14 Checklist de productie 0

| Ecran | Continut |
|---|---|
| 14.1 Selectie | Productia 0 planificata pentru azi, pe linia utilizatorului |
| 14.2 Conditii IPN | Cele 13 conditii din 5.5.8, ca lista bifabila; nu se poate porni pana nu sunt toate bifate sau derogate cu motiv |
| 14.3 Cantitati | Aluat introdus pe sarje, bucati obtinute; tastatura numerica |
| 14.4 Parametri | Pe faze: valoarea specificata afisata, camp pentru valoarea reala, semnal automat de abatere |
| 14.5 Rebut | Cantitate si cauza din cele 14 predefinite, ca butoane; se pot adauga mai multe inregistrari |
| 14.6 Gramaj la ambalare | Ca ECR-11, cu esantion de 20 |
| 14.7 HACCP | Punctele critice, cu valoarea limita afisata, valoarea masurata si conform da / nu |
| 14.8 Probleme | Descriere, poza, actiune imediata, responsabil |
| 14.9 Sinteza si decizie | Randament, rebut pe cauze, abateri, conformitate HACCP; propunerea de decizie a sistemului; decizia se ia numai online, de Managerul R&D |

10.2.5.1 Ecranele 14.3 - 14.8 functioneaza offline. Ecranul 14.9 cere conexiune, pentru
ca decizia declanseaza fluxuri si nu poate ramane in coada locala.

### 10.2.6 ECR-15 Consultare rapida

Un ecran de cautare pentru cine este in hala si vrea doar sa vada: cauta dupa cod de
proiect, produs sau client, si afiseaza statusul, tehnologul, urmatorul pas si termenul.
Este versiunea mobila a ecranului public.

## 10.3 Ce nu se pune in canvas

10.3.1 Nu se pun in aplicatia mobila: triajul, alocarea, antecalculul, editarea retetei,
aprobarile de specificatii, configurarea. Acestea cer context si atentie, iar un ecran de
telefon garanteaza greseli.

10.3.2 NOTA: exista presiunea previzibila de a face "totul in canvas, ca e mai frumos".
Se rezista. Aplicatia model-driven da gratuit ceea ce in canvas ar cere saptamani de
lucru si intretinere permanenta: vizualizari filtrabile, cautare avansata, export in
Excel, audit, securitate pe coloana, formulare responsive. Canvas se foloseste exact
acolo unde model-driven nu poate: hala, manusi, poze, offline.


<!-- ==================== S11-securitate-roluri.md ==================== -->

---

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


<!-- ==================== S12-automatizari.md ==================== -->

---

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


<!-- ==================== S13-indicatori.md ==================== -->

---

# Sectiunea 13 - Indicatori si raportare

## 13.1 Cei trei indicatori

| Indicator | Ce masoara | Tinta |
|---|---|---|
| T-Total | Respectarea timpului | 95% |
| Q-Corect | Corectitudinea a ceea ce se livreaza | 98% |
| Q-Complet | Completitudinea a ceea ce se livreaza | 98% |

13.1.1 Tintele se seteaza in `rd_indicator` si sunt parametrizabile. Valorile de mai sus
sunt punctul de pornire recomandat: T-Total mai jos decat cele de calitate, pentru ca
timpul depinde partial de factori externi, in timp ce corectitudinea si completitudinea
depind aproape integral de R&D.

## 13.2 T-Total

### 13.2.1 Definitia

T-Total masoara procentul de activitati finalizate in termenul stabilit, dupa scaderea
timpului in care ceasul a fost oprit de blocaje externe.

```
Pentru fiecare activitate masurabila (livrabil sau etapa):

durata_bruta  = data_realizarii - data_inceperii              [zile lucratoare]
zile_blocate  = suma zilelor de blocaj activ cu rd_oprsteceas = Da,
                suprapuse peste intervalul activitatii
durata_neta   = durata_bruta - zile_blocate

termen_efectiv = termen_planificat + zile_blocate

la_termen = data_realizarii <= termen_efectiv

T-Total (%) = numar activitati la_termen / numar activitati finalizate * 100
```

13.2.2 Suprapunerea blocajelor se calculeaza pe intervale, nu prin insumare simpla. Doua
blocaje care se suprapun partial in timp contribuie cu reuniunea intervalelor lor, nu cu
suma zilelor. Aceasta este singura parte a calculului care se implementeaza gresit tipic
si care produce, dupa un an, indicatori peste 100%.

### 13.2.3 Oprirea ceasului

| Situatie | Ceas R&D | Termen catre client |
|---|---|---|
| Blocaj cu sursa Furnizor, Client, Calitate, Planificare, Productie, Achizitii, Extern reglementar | Oprit | Curge |
| Blocaj cu sursa Intern R&D | Curge | Curge |
| Status `In asteptare materie prima` | Oprit, daca exista blocaj activ deschis | Curge |
| Status `Suspendat` | Oprit | Se renegociaza; se raporteaza separat |
| Concediul tehnologului | Curge | Curge |

13.2.3.1 Concediul nu opreste ceasul. Este o problema de alocare a Managerului R&D, nu o
cauza externa. Daca ar opri ceasul, indicatorul ar deveni nefalsificabil.

13.2.3.2 Termenul catre client continua sa curga in orice situatie si se raporteaza
separat, ca `abatere fata de termenul negociat`. Aceasta este dubla masurare ceruta
explicit: R&D nu este penalizat pentru asteptarea unei mostre de la furnizor, dar compania
stie ca a livrat cu 12 zile intarziere catre client si de ce.

### 13.2.4 Nivelurile de masurare

| Nivel | Unitatea numarata | Cine il vede |
|---|---|---|
| Activitate | Fiecare livrabil si etapa finalizata | Manager R&D |
| Rol | Toate activitatile cu `rd_rolresponsabil` = rolul respectiv | Head of R&D |
| Persoana | Toate activitatile cu responsabilul = persoana | Persoana, Manager R&D, Head of R&D |
| Departament | Toate activitatile R&D | Head of R&D, conducere |

13.2.4.1 T-Total pe rol este cel mai util indicator dintre cele patru: arata daca
intarzierile vin din R&D, din Achizitii, din Calitate sau din Productie. Astazi aceasta
intrebare nu are raspuns cu cifre.

13.2.4.2 T-Total pe persoana se raporteaza persoanei si Managerului R&D, nu se afiseaza
public. Motiv: un indicator individual afisat public produce, in trei luni, declararea
selectiva a datelor de realizare, nu imbunatatirea performantei.

## 13.3 Q-Corect

### 13.3.1 Definitia

Q-Corect masoara procentul de livrabile acceptate din prima, fara respingere si fara
corectie ceruta de aprobator.

```
respins = livrabilul a trecut prin status Respins cel putin o data
          SAU documentul asociat a primit versiune noua dupa respingere

Q-Corect (%) = livrabile aprobate fara respingere / livrabile aprobate total * 100
```

13.3.2 Se numara numai livrabilele care au aprobator. Un livrabil fara aprobare nu poate
fi masurat pe corectitudine.

13.3.3 Componente suplimentare, care intra in Q-Corect cu pondere:

| Componenta | Pondere | Sursa |
|---|---|---|
| Livrabile aprobate din prima | 60% | Din statusul livrabilelor |
| Trialuri cu rezultat Reusit din prima incercare | 15% | Din TBL-15 |
| Masuratori conforme fata de toleranta declarata | 10% | Din TBL-16b |
| Verificari HACCP conforme la productia 0 | 10% | Din TBL-34 |
| Antecalcule aprobate fara revizuire | 5% | Din TBL-22 |

13.3.4 Argument pentru ponderare: un Q-Corect construit doar pe aprobari masoara cat de
indulgent este aprobatorul. Adaugand trialurile reusite din prima si conformitatea
masuratorilor, indicatorul masoara si calitatea tehnica, nu doar cea documentara.

## 13.4 Q-Complet

### 13.4.1 Definitia

Q-Complet masoara procentul de livrabile obligatorii si aplicabile care sunt realizate la
momentul inchiderii proiectului sau la data de raportare.

```
Q-Complet la inchidere (%) =
    livrabile obligatorii aplicabile realizate / livrabile obligatorii aplicabile * 100

Q-Complet in curs (%) =
    livrabile scadente si realizate / livrabile scadente * 100
```

13.4.2 Livrabilele marcate `Nu se aplica` de Managerul R&D nu intra la numitor, dar se
raporteaza separat: numarul de derogari pe proiect si pe an. Un numar mare de derogari
inseamna ca sablonul de livrabile nu corespunde realitatii si trebuie corectat, nu ca
oamenii sunt neglijenti.

13.4.3 Q-Complet la nivel de departament, calculat lunar pe proiectele finalizate in luna
respectiva, este indicatorul care raspunde direct la problema centralizatorului actual:
astazi nimeni nu poate spune cate dosare sunt complete fara sa le deschida unul cate unul.

## 13.5 Cum se calculeaza si cand

| Indicator | Frecventa | Flux | Ce se scrie |
|---|---|---|---|
| Campuri de proiect (zile in coada, T-Total net, abatere de termen) | Zilnic | FLX-16 | Coloane pe `rd_proiect` |
| T-Total, Q-Corect, Q-Complet pe activitate, rol, persoana | Lunar, in prima zi lucratoare | FLX-16 | Inregistrari in `rd_masurareindicator` |
| Sinteza trimestriala si anuala | Trimestrial, anual | FLX-16 | Idem, cu perioada corespunzatoare |

13.5.1 Masuratorile lunare se congeleaza: odata scrisa, o inregistrare de masurare nu se
recalculeaza. Motiv: altfel, o inregistrare corectata retroactiv in martie schimba
indicatorul din ianuarie, iar raportarea isi pierde credibilitatea.

## 13.6 Rapoartele

### 13.6.1 Lista rapoartelor

| Cod | Raport | Continut | Cine il vede | Frecventa |
|---|---|---|---|---|
| RAP-01 | Durata medie reala pe etapa | Mediana si media duratei nete pe fiecare etapa, comparata cu durata standard, pe ultimele 12 luni | Head of R&D, Manager R&D | Lunar |
| RAP-02 | Livrabilele care intarzie cel mai des | Top 10 livrabile dupa procentul de intarziere si dupa media zilelor de intarziere, cu rolul responsabil | Head of R&D, Manager R&D, sefii rolurilor implicate | Lunar |
| RAP-03 | Incarcarea pe tehnolog | Proiecte active, distributia pe benzi, gradul de incarcare, evolutie pe 12 luni | Manager R&D, Head of R&D | Saptamanal |
| RAP-04 | Coada pe linie | Proiecte pe fiecare linie, primul slot estimat, gradul de supraincarcare | Manager R&D, Planificare | Saptamanal |
| RAP-05 | Rata de acceptare a solicitarilor pe KAM | Solicitari trimise, acceptate, respinse, amanate, cu motivele; rata de acceptare | Head of R&D, Comercial Manager, fiecare KAM pentru el | Lunar |
| RAP-06 | Proiecte abandonate cu motive | Lista, cu motivul, faza in care s-au oprit si costul estimat al efortului pierdut | Head of R&D, conducere | Trimestrial |
| RAP-07 | T-Total pe rol si pe persoana | Cu detaliul zilelor blocate si al sursei blocajelor | Head of R&D | Lunar |
| RAP-08 | Q-Corect si Q-Complet | Pe departament, rol si persoana | Head of R&D | Lunar |
| RAP-09 | Blocaje pe sursa | Zile de blocaj cumulate pe sursa (furnizor, client, Calitate, Planificare), cu top 10 cauze | Head of R&D, conducere | Trimestrial |
| RAP-10 | Termen propus fata de negociat fata de realizat | Pe KAM si pe tehnolog | Head of R&D, Comercial Manager | Trimestrial |
| RAP-11 | Produse lansate si indicele de sanatate | Din revizuirea post-implementare | Head of R&D, conducere, comercial | Trimestrial |
| RAP-12 | Materii prime si furnizori | Lead time real fata de asumat, rata de respingere pe furnizor, numarul de modificari de ETA | Achizitii, Head of R&D | Lunar |
| RAP-13 | Portofoliu pe alergeni | Ce produse contin fiecare alergen | Calitate, R&D | La cerere |
| RAP-14 | Suprascrieri de prioritate | Cine, ce, de ce, cand | Head of R&D, conducere | Lunar |
| RAP-15 | Ce am invatat (anual) | Abateri de cost si de randament pe categorie si pe linie; corectii propuse pentru antecalcul | Head of R&D, conducere | Anual |

### 13.6.2 Unde traiesc rapoartele

| Tip de raport | Implementare | Motiv |
|---|---|---|
| RAP-03, RAP-04, si listele operationale | Vizualizari si tablouri de bord native Dataverse | Sunt liste filtrabile, nu au nevoie de Power BI; sunt disponibile in Val 1, fara licente suplimentare |
| RAP-01, RAP-02, RAP-05 ... RAP-15 | Power BI, cu conexiune la Dataverse | Cer agregari pe perioade, comparatii istorice si grafice |
| RAP-13 | Vizualizare Dataverse cu filtru pe Choice multi-select | Se cere ad-hoc, la audit sau la cerinta de client |

13.6.2.1 Raportarea este read-only, conform deciziei de arhitectura. Nicio actiune nu se
declanseaza dintr-un raport.

13.6.2.2 NOTA: raportarea in Power BI cere licente Pro pentru cei care publica si
consuma continut in spatii de lucru, sau capacitate dedicata. Pentru cei ~200 de cititori
din companie, ecranul public de status (ECR-04) este in aplicatia model-driven, nu in
Power BI, tocmai ca sa nu genereze cerinta de licentiere pentru toata firma.

## 13.7 Ce se face cu indicatorii

13.7.1 Indicatorii nu sunt scop in sine. Regula de folosire, scrisa in procedura:

| Indicator sub tinta | Prima intrebare | Actiune tipica |
|---|---|---|
| T-Total pe departament | Care rol si care etapa trag in jos? | Corectia duratelor standard (Sectiunea 14) sau realocarea |
| T-Total pe rol extern R&D | Care sursa de blocaj domina? | Discutie cu departamentul respectiv, cu RAP-09 pe masa |
| Q-Corect | Ce livrabile se resping cel mai des si de ce? | Sablon de document mai clar, sau instruire, sau aprobator prea vag |
| Q-Complet | Ce livrabile lipsesc sistematic la inchidere? | Sablonul cere ceva ce nu se face niciodata: se elimina sau se face obligatoriu real |

13.7.2 Un indicator care sta trei luni sub tinta fara actiune declarata este un indicator
care trebuie eliminat sau retintit. Se revizuiesc anual, impreuna cu ponderile de
prioritizare si cu duratele standard.


<!-- ==================== S14-durate-etape.md ==================== -->

---

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


<!-- ==================== S15-migrare.md ==================== -->

---

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
