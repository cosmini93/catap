# Sectiunea 24 - Stabilizare, capabilitate de proces si sanatatea proiectului

Trei adaugiri din blueprintul Enterprise (22.2.6, 22.2.7, 22.2.11) care acopera intervalul
dintre productia 0 si revizuirea de la 30 de zile - intervalul in care, azi, produsul intra
in serie fara sa fi demonstrat ca se poate face repetat.

## 24.1 Stabilizarea

### 24.1.1 Golul pe care il acopera

In blueprintul de baza, proiectul trecea din `Productie 0` direct in `Finalizat`, imediat
ce decizia productiei 0 era `Validat`. Adica pe baza **unui singur lot**, facut cu
tehnologul prezent, cu atentia maxima a echipei si, de regula, cu materie prima aleasa.

In bakery industrial, primul lot reusit nu dovedeste nimic despre al zecelea. Variabilitatea
fainii intre loturi, curba de invatare a operatorilor de pe celelalte doua schimburi si
comportamentul liniei la incarcare completa apar abia dupa. Regula celor trei loturi
consecutive conforme este practica standard si se preia ca atare.

### 24.1.2 Regula

Proiectul nu trece in `Finalizat` decat dupa **trei loturi de productie consecutive
conforme**, produse in conditii normale de serie.

| Conditie | Detaliu |
|---|---|
| Consecutive | Nu se aleg trei loturi bune dintre sase. Un lot neconform reseteaza numaratoarea |
| Conforme | Gramaj in toleranta, zero neconformitati HACCP, rebut sub prag, fara reclamatii interne |
| In conditii normale | Fara tehnolog permanent la linie, pe schimburi diferite daca produsul se face pe mai multe |
| Interval maxim | Daca cele trei loturi nu se produc in 90 de zile, stabilizarea se inchide cu status `Neconcludenta` si decizia urca la Managerul R&D |

24.1.3 PROPUNERE: cele trei loturi trebuie sa acopere **minimum doua schimburi diferite**
pentru produsele care se fac pe mai multe schimburi. Motiv: cea mai frecventa cauza de
variatie in serie, dupa materia prima, este diferenta dintre echipe, iar validarea pe un
singur schimb ascunde exact acest lucru.

24.1.4 Statusul `Stabilizare` se adauga in lista din 2.2.1, intre `Productie 0` (8) si
`In revizuire` (10). Etapa corespunzatoare este ETP-12, adaugata dupa ETP-10.

### 24.1.5 TBL-51 `rd_stabilizare`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar | rd_name | Autonumber | Da | STB-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Productie 0 sursa | rd_productie0 | Lookup (rd_productie0) | Da | - | Referential | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | - | - |
| Data inceperii | rd_datainceput | Date Only | Da | - | Prima productie de serie | - |
| Numar loturi necesare | rd_loturinecesare | Whole Number | Da | 1 - 10, implicit 3 | Configurabil pe categorie de produs | Variabila de mediu |
| Loturi produse | rd_loturiproduse | Rollup (Count) | Nu | 0 - 99 | Din rd_lotstabilizare | - |
| Loturi conforme consecutive | rd_loturiconforme | Whole Number | Nu | 0 - 99 | Se reseteaza la primul neconform | Scris de FLX-31 |
| Schimburi acoperite | rd_schimburi | Whole Number | Nu | 1 - 3 | Distinct pe loturi conforme | Vezi 24.1.3 |
| Randament mediu in serie (%) | rd_randamentmediu | Decimal (2) | Nu | 0 - 120 | Media loturilor conforme | - |
| Randament la productia 0 (%) | rd_randamentprod0 | Decimal (2) | Nu | - | Preluat automat | Baza de comparatie |
| Diferenta de randament (pp) | rd_diferentarandament | Calculated (Decimal) | Nu | - | serie - productie 0 | Vezi 24.1.7 |
| Rebut mediu in serie (%) | rd_rebutmediu | Decimal (2) | Nu | 0 - 100 | - | - |
| Giveaway mediu (%) | rd_giveawaymediu | Decimal (2) | Nu | -50 - 50 | Supraumplerea in serie | Vezi 7.6.7 |
| Viteza medie realizata (%) | rd_vitezamedie | Decimal (2) | Nu | 0 - 150 | Fata de viteza nominala | - |
| Reclamatii interne | rd_reclamatiiinterne | Whole Number | Nu | 0 - 99 | - | - |
| Variabilitate acceptabila | rd_variabilitateok | Yes/No | Nu | - | CV al gramajului sub prag pe toate loturile | Vezi 6.2.3 |
| Actiuni deschise | rd_actiunideschise | Rollup (Count) | Nu | - | Din rd_actiune | Blocheaza inchiderea |
| Status | rd_statusstabilizare | Choice | Da | In curs / Reusita / Neconcludenta / Esuata | - | Choice global STATUSSTAB |
| Data finalizarii | rd_datafinalizare | Date Only | Nu | - | La al treilea lot conform consecutiv | Declanseaza G7 |
| Decizie | rd_deciziestabilizare | Choice | Nu | Release / Release cu monitorizare / Se prelungeste / Se reia productia 0 | - | - |
| Motivul deciziei | rd_motivdecizie | Text Area (2000) | Nu | - | Obligatoriu pentru tot ce nu e Release | - |
| Responsabil | rd_responsabil | Lookup (systemuser) | Da | - | - | - |

### 24.1.6 TBL-52 `rd_lotstabilizare`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Numarul lotului de productie | - | Coloana primara |
| Stabilizare | rd_stabilizare | Lookup (rd_stabilizare) | Da | - | Parental | Cascade All |
| Numar de ordine | rd_numarordine | Whole Number | Da | 1 - 99 | Succesiv | - |
| Data productiei | rd_dataproductie | Date Only | Da | - | - | - |
| Schimb | rd_schimb | Choice | Da | Choice SCHIMB | - | - |
| Cantitate produsa (kg) | rd_cantitate | Decimal (2) | Da | > 0 | - | - |
| Randament (%) | rd_randament | Decimal (2) | Nu | 0 - 120 | - | - |
| Rebut (%) | rd_rebut | Decimal (2) | Nu | 0 - 100 | - | - |
| Greutate medie (g) | rd_greutatemedie | Decimal (2) | Nu | - | Minimum 20 de bucati | - |
| CV gramaj (%) | rd_cvgramaj | Decimal (2) | Nu | 0 - 100 | - | Vezi 6.2.3 |
| Giveaway (%) | rd_giveaway | Decimal (2) | Nu | -50 - 50 | - | - |
| Viteza realizata (%) | rd_viteza | Decimal (2) | Nu | 0 - 150 | - | - |
| Conformitate HACCP | rd_haccpok | Yes/No | Da | - | O neconformitate = lot neconform | - |
| Reclamatii sau neconformitati | rd_neconformitati | Whole Number | Nu | 0 - 99 | - | - |
| Lot conform | rd_conform | Yes/No | Da | - | Vezi 24.1.2 | Scris de FLX-31 |
| Motivul neconformitatii | rd_motivneconform | Text Area (1000) | Nu | - | Obligatoriu daca lot conform = Nu | - |
| Problema generata | rd_problema | Lookup (rd_problema) | Nu | - | Un lot neconform creeaza automat o problema | FLX-31 |

### 24.1.7 Ce se face cu diferenta de randament

Diferenta dintre randamentul in serie si cel de la productia 0 este prima informatie
economica reala a produsului. Se propaga automat in doua locuri: in `rd_antecalcul.rd_costreal`,
ca sa se vada marja adevarata, si in revizuirea de la 30 de zile (8.2.7), ca punct de
pornire, nu ca descoperire.

24.1.8 O diferenta mai mare de 3 puncte procentuale in minus declanseaza automat o problema
(TBL-48) de categorie Financiar, cu severitate Majora. Motiv: la un produs de volum, 3
puncte de randament sunt mai multi bani decat toate economiile pe care le va face proiectul
de optimizare care urmeaza.

## 24.2 Capabilitatea de proces

### 24.2.1 Ce adauga fata de statistica existenta

Blueprintul de baza calcula media, abaterea standard, CV, minimul si maximul (6.1.4).
Acestea descriu esantionul. Capabilitatea raspunde la o intrebare diferita si mai utila:
**procesul, asa cum se comporta, poate sta in limitele de specificatie pe termen lung?**

### 24.2.2 Formulele

```
Cp  = (LSS - LIS) / (6 x sigma)
Cpk = MIN( (LSS - medie) / (3 x sigma), (medie - LIS) / (3 x sigma) )

unde LSS = limita superioara de specificatie = tinta + toleranta plus
      LIS = limita inferioara de specificatie = tinta - toleranta minus
      sigma = abaterea standard a procesului
```

24.2.3 Interpretarea, cu pragurile uzuale:

| Cpk | Interpretare | Ce se face |
|---|---|---|
| sub 1.00 | Proces incapabil. Produce neconformitati sistematic | Nu se accepta la stabilizare; se reia setarea |
| 1.00 - 1.32 | Marginal capabil | Acceptabil cu monitorizare si control in proces |
| 1.33 - 1.66 | Capabil | Tinta normala pentru gramaj in bakery |
| peste 1.67 | Foarte capabil | Se poate reduce frecventa controlului |

24.2.4 **Cp fata de Cpk**: Cp spune daca imprastierea incape in tolerante; Cpk spune daca
incape **si este centrata**. Un Cp de 2.0 cu Cpk de 0.8 inseamna un proces precis dar
deplasat - se corecteaza prin reglaj, ieftin. Un Cp de 0.7 inseamna imprastiere prea mare
- se corecteaza doar prin schimbarea procesului, scump. Distinctia decide ce se face
luni dimineata.

### 24.2.5 Conditii de calcul

| Conditie | Valoare | Motiv |
|---|---|---|
| Numar minim de valori | 30 | Sub 30, sigma este prea instabila pentru un indice de capabilitate |
| Loturi diferite | Minimum 3 | Altfel se masoara variatia din interiorul unui lot, nu a procesului |
| Limite de specificatie declarate | Obligatorii | Fara tolerante nu exista capabilitate |
| Date fara valori excluse arbitrar | Da | Excluderile scad artificial sigma si umfla Cpk |

24.2.6 Sub 30 de valori, sistemul afiseaza `Date insuficiente`, nu un numar. Un Cpk
calculat pe 10 bucati este o cifra cu doua zecimale care nu inseamna nimic si care va fi
citata in sedinte.

### 24.2.7 TBL-53 `rd_capabilitateproces`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | {produs}_{parametru} | Generata | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Stabilizare | rd_stabilizare | Lookup (rd_stabilizare) | Nu | - | Referential | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | Capabilitatea este a perechii produs-linie | - |
| Parametru | rd_parametru | Choice | Da | Choice TIPMASURATOARE | Tipuri numerice | - |
| Perioada de la | rd_perioadadela | Date Only | Da | - | - | - |
| Perioada pana la | rd_perioadapanala | Date Only | Da | - | - | - |
| Numar de valori | rd_n | Whole Number | Da | 1 - 9999 | Sub 30 = Date insuficiente | Vezi 24.2.5 |
| Numar de loturi | rd_numarloturi | Whole Number | Da | 1 - 99 | Minimum 3 | - |
| Media | rd_medie | Decimal (4) | Da | - | - | - |
| Abaterea standard | rd_sigma | Decimal (5) | Da | > 0 | Esantion, n-1 | - |
| Tinta | rd_tinta | Decimal (4) | Da | - | Din specificatie | - |
| Limita inferioara | rd_lis | Decimal (4) | Da | - | tinta - toleranta minus | - |
| Limita superioara | rd_lss | Decimal (4) | Da | - | tinta + toleranta plus | - |
| Cp | rd_cp | Decimal (3) | Nu | 0 - 10 | Vezi 24.2.2 | - |
| Cpk | rd_cpk | Decimal (3) | Nu | -5 - 10 | Poate fi negativ daca media e in afara limitelor | - |
| Deplasare fata de tinta (%) | rd_deplasare | Decimal (2) | Nu | -100 - 100 | (medie - tinta) / tinta x 100 | Arata daca e reglaj sau imprastiere |
| Verdict | rd_verdict | Choice | Da | Date insuficiente / Incapabil / Marginal / Capabil / Foarte capabil | Vezi 24.2.3 | - |
| Recomandare | rd_recomandare | Text Area (1000) | Nu | - | Generata din combinatia Cp / Cpk | Vezi 24.2.4 |
| Data calculului | rd_datacalcul | Date and Time | Da | - | - | Scris de FLX-32 |

24.2.8 Capabilitatea se calculeaza pentru gramaj obligatoriu, si optional pentru dimensiuni
si pentru temperatura in centru la congelare. Pentru ultimul, limita este unilaterala
(doar maximum -18 C), deci se calculeaza numai Cpk superior.

## 24.3 Sanatatea proiectului in timp

### 24.3.1 De ce snapshot si nu doar un camp calculat

Un scor de sanatate calculat la cerere spune cum sta proiectul acum. Nu spune ca acum
trei saptamani era verde si a coborat constant. Tendinta este informatia care permite
interventia inainte de criza; valoarea instantanee permite doar constatarea ei.

### 24.3.2 Formula

Preluata din Enterprise 14.1, cu ponderile adaptate la ce exista efectiv in model:

| Componenta | Pondere | Sursa | Cum se puncteaza |
|---|---|---|---|
| Riscuri | 20 | TBL-47 | 20 fara riscuri Ridicat sau Critic deschise; minus 5 pentru fiecare Ridicat; 0 daca exista Critic |
| Livrabile | 20 | TBL-03 | Procentul de livrabile scadente si realizate, scalat la 20 |
| Termen | 15 | TBL-02 | 15 daca forecast <= negociat; scade proportional cu depasirea |
| Pregatire de aprovizionare | 15 | TBL-07 | Procentul de materii prime critice cu ETA confirmat si neexpirat |
| Pregatire de productie | 10 | TBL-32 | Procentul de conditii IPN indeplinite; 10 daca IPN nu e inca aplicabil |
| Calitate | 10 | TBL-16b, TBL-17 | Conformitatea ultimelor masuratori si verdictul senzorial |
| Capacitate | 10 | TBL-37 | 10 daca tehnologul e sub 100% incarcare; scade peste |

```
sanatate = suma componentelor          [0 - 100]

Verde     90 - 100
Galben    75 - 89
Portocaliu 60 - 74
Rosu      sub 60
```

24.3.3 Un proiect `Blocat` nu primeste automat rosu. Blocajul extern este deja masurat
separat si nu este vina proiectului; ce conteaza este daca, dupa deblocare, mai poate
recupera. Se marcheaza distinct, cu pastila proprie.

### 24.3.4 TBL-58 `rd_snapshotsanatate`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {cod proiect}_{AAAALLZZ} | Generata | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Data snapshot | rd_data | Date Only | Da | - | Saptamanal, luni | Unic impreuna cu proiectul |
| Status la data | rd_status | Choice | Da | Choice STATUSPROIECT | Copiat, nu referit | Ca sa ramana istoric corect |
| Etapa la data | rd_etapa | Text (100) | Nu | - | Copiata ca text | Idem |
| Scor sanatate | rd_scorsanatate | Whole Number | Da | 0 - 100 | Vezi 24.3.2 | - |
| Nivel | rd_nivel | Choice | Da | Verde / Galben / Portocaliu / Rosu / Blocat | - | - |
| Componenta riscuri | rd_compriscuri | Whole Number | Nu | 0 - 20 | - | - |
| Componenta livrabile | rd_complivrabile | Whole Number | Nu | 0 - 20 | - | - |
| Componenta termen | rd_comptermen | Whole Number | Nu | 0 - 15 | - | - |
| Componenta aprovizionare | rd_compaprovizionare | Whole Number | Nu | 0 - 15 | - | - |
| Componenta productie | rd_compproductie | Whole Number | Nu | 0 - 10 | - | - |
| Componenta calitate | rd_compcalitate | Whole Number | Nu | 0 - 10 | - | - |
| Componenta capacitate | rd_compcapacitate | Whole Number | Nu | 0 - 10 | - | - |
| Variatie fata de saptamana trecuta | rd_variatie | Whole Number | Nu | -100 - 100 | - | Semnalul cel mai util |
| Zile de la ultima activitate | rd_zileinactiv | Whole Number | Nu | 0 - 999 | Din rd_ultimaactivitate | Detecteaza proiecte uitate |
| Riscuri deschise | rd_riscurideschise | Whole Number | Nu | 0 - 99 | - | - |
| Probleme deschise | rd_problemedeschise | Whole Number | Nu | 0 - 99 | - | - |
| Actiuni restante | rd_actiunirestante | Whole Number | Nu | 0 - 99 | - | - |
| Livrabile depasite | rd_livrabiledepasite | Whole Number | Nu | 0 - 99 | - | - |

24.3.5 Snapshot-ul se scrie saptamanal de FLX-29, pentru toate proiectele active, si nu se
mai modifica niciodata. Este singura tabela din model care creste liniar cu timpul fara
sa fie stearsa; la 180 de proiecte pe an si 20 de saptamani medii de viata, inseamna
aproximativ 3600 de randuri pe an, ceea ce este neglijabil.

24.3.6 **Alerta de degradare**: o scadere de peste 15 puncte intr-o saptamana, sau trei
saptamani consecutive de scadere, genereaza o notificare catre Managerul R&D. Este
mecanismul care prinde proiectele care se strica lent, tipul de proiect care azi se
descopera cu doua saptamani inainte de termen.

## 24.4 Project Success Score

### 24.4.1 Cand se calculeaza

O singura data, la revizuirea de 90 de zile (Sectiunea 8), cu revizuire optionala la 180
de zile pentru proiectele importante. Nu este un indicator operational, ci unul de
invatare: raspunde la intrebarea "ce fel de proiecte ne ies bine".

### 24.4.2 Formula

| Componenta | Puncte | Sursa |
|---|---|---|
| Volum realizat fata de estimat | 20 | TBL-35 |
| Respectarea termenului negociat | 15 | TBL-02, abaterea de termen |
| Rezultatul productiei 0 | 20 | TBL-33, decizia si numarul de repetari |
| Cost real fata de antecalcul | 15 | TBL-35, abaterea de cost |
| Calitate si reclamatii | 20 | TBL-35, rata de reclamatii |
| Stabilitate post-implementare | 10 | TBL-51, diferenta de randament |

| Clasificare | Scor |
|---|---|
| Champion | 90 - 100 |
| Success | 80 - 89 |
| Acceptable | 70 - 79 |
| Weak | 60 - 69 |
| Failed | sub 60 |

24.4.3 Scorul se stocheaza pe `rd_revizuire` (TBL-35), ca doua coloane noi:
`rd_scorsucces` (Whole Number) si `rd_clasificaresucces` (Choice). Nu are nevoie de tabela
proprie.

24.4.4 NOTA: indicele de sanatate al produsului din 8.4 si acest scor de succes masoara
lucruri apropiate, dar diferite - primul spune daca produsul isi tine promisiunile
comerciale, al doilea daca proiectul a fost bine condus. Un produs poate fi Champion cu un
proiect Weak, daca piata l-a salvat, si invers. Se pastreaza ambele, iar diferenta dintre
ele este ea insasi informatie: proiectele bine conduse cu produse slabe arata o problema de
selectie la triaj, nu de executie.
