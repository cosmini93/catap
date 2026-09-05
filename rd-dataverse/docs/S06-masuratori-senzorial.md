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
