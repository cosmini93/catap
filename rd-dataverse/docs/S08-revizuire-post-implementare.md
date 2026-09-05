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
