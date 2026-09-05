# Anexa A1 - Prioritizarea si calculul termenelor

Anexa detaliaza mecanismele cerute in sectiunile 4.2 si 4.3 din brief. Sunt singurele
locuri din blueprint unde regulile de calcul se exprima ca formule, pentru ca nu pot fi
exprimate altfel.

## A1.1 Scorul de prioritate

### A1.1.1 Componentele

Scor pe 100 de puncte, recalculat saptamanal de FLX-10. Ponderile sunt variabile de
mediu, parametrizabile fara modificarea fluxului.

| Componenta | Puncte | Sens |
|---|---|---|
| Volum anual estimat | 30 | Pe benzi, nu liniar |
| Importanta clientului (A/B/C) | 20 | Clasificare stabilita de Sales / KAM |
| Termen impus extern | 20 | Listare, sezon, licitatie |
| Efort de dezvoltare | 10 | Invers proportional |
| Risc de materie prima noua | -10 | Scade scorul |
| Reutilizare de reteta sau de linie setata | 10 | Creste scorul |
| **Total teoretic** | **100** (minim 0, maxim 100) | |

### A1.1.2 Volum anual estimat - 30 de puncte, pe benzi

| Banda | Volum estimat (tone/an) | Puncte |
|---|---|---|
| V1 | peste 500 | 30 |
| V2 | 200 - 500 | 25 |
| V3 | 80 - 200 | 19 |
| V4 | 30 - 80 | 13 |
| V5 | 10 - 30 | 7 |
| V6 | sub 10 | 3 |

Argument: benzile, nu o functie liniara, pentru ca diferenta dintre 400 si 450 de tone nu
schimba nicio decizie, dar diferenta dintre 30 si 300 o schimba pe toate. Pragurile se
stabilesc la configurare din distributia reala a ultimilor doi ani si se revizuiesc anual.

### A1.1.3 Importanta clientului - 20 de puncte

| Clasificare | Puncte |
|---|---|
| A | 20 |
| B | 12 |
| C | 5 |
| Client nou, neclasificat inca | 12 (se trateaza ca B pana la clasificare) |

A1.1.3.1 Clasificarea este stabilita si revizuita de Sales / KAM, nu de R&D. R&D o
consuma, nu o negociaza. Revizuirea este anuala; data ultimei clasificari este vizibila,
iar o clasificare mai veche de 18 luni se semnaleaza.

### A1.1.4 Termen impus extern - 20 de puncte

Punctajul depinde de tipul termenului si de cat de aproape este:

| Situatie | Puncte |
|---|---|
| Listare la retail cu data ferma, in mai putin de 60 de zile | 20 |
| Listare la retail cu data ferma, in 60 - 120 de zile | 15 |
| Sezon (Craciun, Paste, vara) cu data de livrare ferma | 15 |
| Licitatie sau caiet de sarcini cu termen de depunere | 15 |
| Lansare anuntata de client, fara data ferma | 8 |
| Cerinta de reglementare cu termen legal | 20 |
| Fara termen impus | 0 |

A1.1.4.1 Termenul impus se documenteaza: cine l-a impus si prin ce document. Un termen
impus declarat verbal de KAM, fara dovada, primeste jumatate din punctaj. Motiv: fara
aceasta regula, toate proiectele devin "listare urgenta" in prima luna de folosire.

### A1.1.5 Efort de dezvoltare - 10 puncte, invers proportional

| Efort estimat | Descriere | Puncte |
|---|---|---|
| Foarte mic | Schimbare de ambalaj sau eticheta, reteta identica | 10 |
| Mic | Reformulare partiala, linie deja setata, MP existente | 8 |
| Mediu | Produs nou pe tehnologie cunoscuta, linie setata | 5 |
| Mare | Tehnologie noua sau linie care necesita setare | 2 |
| Foarte mare | Produs care cere echipament, capabilitate sau validare noua | 0 |

Efortul se estimeaza de tehnolog sau de Managerul R&D la triaj, pe aceasta scala de
cinci trepte, nu in ore. Estimarea in ore la triaj este o iluzie de precizie.

### A1.1.6 Risc de materie prima noua - minus 10 puncte

| Situatie | Puncte |
|---|---|
| Fara materii prime noi | 0 |
| O materie prima noua, din portofoliul unui furnizor aprobat | -3 |
| O materie prima noua, furnizor nou sau achizitie noua | -6 |
| Doua sau mai multe materii prime noi | -8 |
| Materie prima de import sau caz special | -10 |

Argument: materia prima noua este cea mai frecventa cauza de intarziere si de blocaj
extern. Penalizarea nu spune ca proiectul e mai putin important, spune ca este mai putin
probabil sa se termine repede, deci nu trebuie sa blocheze coada.

### A1.1.7 Reutilizare - 10 puncte

| Situatie | Puncte |
|---|---|
| Reteta existenta, doar gramaj sau ambalaj diferit | 10 |
| Reteta derivata dintr-un produs existent, linie deja setata | 7 |
| Linie deja setata pentru acest tip de produs | 4 |
| Nimic reutilizabil | 0 |

### A1.1.8 Formula finala

```
scor_baza = puncte_volum + puncte_client + puncte_termen + puncte_efort
            + puncte_risc_mp + puncte_reutilizare

scor_cu_imbatranire = scor_baza + bonus_imbatranire        (vezi A1.1.9)

scor_final = MIN(100, MAX(0, scor_cu_imbatranire))

banda = P1 daca scor_final >= 80
        P2 daca scor_final intre 60 si 79
        P3 daca scor_final intre 35 si 59
        P4 daca scor_final sub 35
```

Daca `rd_scorsuprascris` este completat, el inlocuieste `scor_final` la calculul benzii,
dar scorul calculat ramane vizibil alaturi, pentru comparatie.

### A1.1.9 Mecanismul de imbatranire in coada

PROPUNERE: bonus de imbatranire care creste cu timpul de asteptare, ca proiectele mici sa
nu ramana blocate la infinit in spatele celor mari.

```
zile_coada = zile lucratoare de la data acceptarii, cat timp proiectul
             nu a intrat in status In dezvoltare

bonus_imbatranire = MIN(20, INTREG(zile_coada / 10) * 2)
```

Adica 2 puncte la fiecare 10 zile lucratoare de asteptare, plafonat la 20 de puncte, deci
la 100 de zile lucratoare.

Argument in trei randuri: fara imbatranire, un proiect P4 pentru un client C cu volum mic
nu ajunge niciodata sa fie lucrat, iar KAM-ul respectiv inceteaza sa mai foloseasca
sistemul. Cu plafon la 20 de puncte, un proiect nu poate urca din P4 in P1 doar prin
asteptare, dar poate urca din P3 in P2, ceea ce este suficient ca sa intre in coada reala.
Ceasul de imbatranire se opreste cand proiectul intra in lucru, si se opreste si pe durata
blocajelor externe, ca sa nu premieze proiectele blocate din vina furnizorului.

### A1.1.10 Bugetul de urgenta pe KAM

PROPUNERE, conform cerintei: fiecare KAM poate avea simultan un numar limitat de proiecte
in banda maxima.

| Element | Valoare |
|---|---|
| Buget implicit pe KAM | 2 proiecte simultan in banda P1 |
| Buget pentru Comercial Manager (arbitru) | 1 proiect suplimentar, pentru arbitraj |
| Ce se numara | Proiecte in statusuri active (4-9) cu banda P1, indiferent daca banda vine din scor sau din suprascriere |

Mecanismul, la incercarea de a promova un al treilea proiect in P1:

| Pas | Ce se intampla |
|---|---|
| 1 | Sistemul refuza promovarea automata si afiseaza cele doua proiecte P1 existente ale KAM-ului |
| 2 | KAM-ul (sau Comercial Managerul) trebuie sa aleaga explicit unul dintre ele pentru retrogradare in P2 |
| 3 | Retrogradarea cere motiv obligatoriu si se inregistreaza in audit |
| 4 | Daca refuza, proiectul nou ramane in P2, cu scorul calculat vizibil |
| 5 | Managerul R&D primeste notificare la fiecare schimb de acest tip |

A1.1.10.1 Argument: fara buget de urgenta, scorul se erodeaza in trei luni - toti KAM-ii
suprascriu totul in banda maxima si sistemul redevine "cine striga mai tare". Cu buget,
urgenta devine o resursa rara pe care fiecare KAM o gestioneaza singur, iar arbitrajul
intre KAM-i ramane, conform cerintei, la Managerul R&D.

A1.1.10.2 Bugetul nu se aplica proiectelor cu termen impus extern documentat de tip
reglementare. Acelea intra in P1 fara sa consume buget.

### A1.1.11 Coada pe linie

A1.1.11.1 Cele 9 linii nu concureaza intre ele. Coada se vede in doua feluri:

| Vedere | Ce arata | Cine o foloseste |
|---|---|---|
| Coada globala | Toate proiectele active, ordonate dupa scor | Comercial, Head of R&D |
| Coada pe linie | Proiectele care vizeaza fiecare linie, ordonate dupa scor, cu primul slot liber estimat | Manager R&D, Planificare |

A1.1.11.2 Un proiect P1 pe linia L03 nu are prioritate fata de un proiect P2 pe linia L07:
sunt resurse diferite. Prioritatea conteaza numai in interiorul aceleiasi linii si in
alocarea timpului de tehnolog.

A1.1.11.3 Supraincarcarea unei linii (peste `rd_pragsupraincarcare`) se semnaleaza vizual
si intra ca factor in calculul termenului propus (A1.2), nu in scorul de prioritate.

### A1.1.12 Suprascrierea

| Element | Regula |
|---|---|
| Cine poate | Numai Comercial Manager (ROL-06), prin securitate pe coloana |
| Ce cere | Scorul nou (0-100) si motivul, ambele obligatorii |
| Ce se pastreaza | Scorul calculat ramane vizibil alaturi; suprascrierea nu il sterge |
| Audit | Coloanele de suprascriere sunt auditate; data si autorul se scriu automat |
| Expirare | PROPUNERE: suprascrierea expira dupa 90 de zile si scorul revine la cel calculat, cu notificare cu 7 zile inainte |
| Raportare | Raport lunar cu toate suprascrierile, motivele si autorii |

A1.1.12.1 Argument pentru expirare: o suprascriere facuta pentru o situatie reala din
martie nu mai are sens in septembrie, dar nimeni nu se intoarce sa o retraga. Expirarea
automata pastreaza sistemul curat fara sedinte de curatare.

## A1.2 Calculul termenului propus

### A1.2.1 Formula

```
durata_baza = durata standard din sablonul de etape, pentru tipul de proiect
              (implicit 14 zile lucratoare)

durata_ajustata = durata_baza
                  * factor_incarcare_tehnolog
                  * factor_coada_linie
                  * factor_sezonalitate
                  + adaos_materii_prime_noi
                  + zile_indisponibilitate_tehnolog

termen_propus = data_acceptarii + durata_ajustata zile lucratoare
```

### A1.2.2 Factorul de incarcare a tehnologului

| Proiecte active ale tehnologului | Factor |
|---|---|
| 1 - 2 | 0.9 |
| 3 - 4 | 1.0 |
| 5 - 6 | 1.2 |
| 7 - 8 | 1.5 |
| 9 - 10 | 1.9 |
| peste 10 | 2.4, cu avertizare de supraincarcare la alocare |

Argument: un tehnolog cu 8 proiecte active nu lucreaza de 8 ori mai incet la fiecare, dar
nici nu lucreaza la fel de repede ca unul cu 2. Factorii de mai sus sunt punctul de
pornire; se recalibreaza dupa 6-12 luni din duratele reale, conform Sectiunii 14.

### A1.2.3 Factorul de coada pe linie

| Proiecte active care vizeaza linia | Factor |
|---|---|
| 0 - 2 | 1.0 |
| 3 - 5 | 1.1 |
| 6 - 8 | 1.25 |
| peste 8 | 1.4 |

Se aplica numai daca proiectul are linie stabilita la acceptare. Daca nu are, se foloseste
media liniilor compatibile cu tipul de produs.

### A1.2.4 Factorul de sezonalitate

| Perioada de acceptare | Factor | Motiv |
|---|---|---|
| Ianuarie - martie | 1.0 | Perioada normala |
| Aprilie - mai | 1.1 | Pregatirea sezonului de vara |
| Iunie - august | 1.2 | Concedii, capacitate redusa |
| Septembrie - octombrie | 1.3 | Varful de dezvoltare pentru Craciun; linii ocupate |
| Noiembrie - decembrie | 1.25 | Productie de varf, acces greu la linii |

A1.2.4.1 Factorii de sezonalitate sunt PROPUNERE si trebuie confirmati cu date reale din
ultimii doi ani, la configurare. Sunt intre primele care se recalibreaza dupa un an de
masuratori.

### A1.2.5 Adaosul pentru materii prime noi

| Situatie | Zile adaugate |
|---|---|
| Fara materii prime noi | 0 |
| MP noua, pe stoc la furnizor | +5 zile lucratoare |
| MP noua, in portofoliul furnizorului | +5 zile lucratoare |
| MP noua, achizitie noua | +20 de zile lucratoare |
| MP de import sau caz special | +30 de zile lucratoare sau ETA declarat, care e mai mare |
| Mai multe MP noi | Se ia cea mai mare valoare, nu suma |

A1.2.5.1 Se ia maximul, nu suma, pentru ca aprovizionarea materiilor prime se face in
paralel. Daca ETA-ul confirmat exista deja, el inlocuieste estimarea.

### A1.2.6 Cele trei termene

| Termen | Cine il stabileste | Cand se schimba | Ce masoara |
|---|---|---|---|
| Propus | Sistemul, prin FLX-03 | La orice recalculare (schimbare de tehnolog, linie, ETA) | Ce poate livra R&D in conditiile date |
| Negociat | Managerul R&D impreuna cu KAM | Numai manual, cu urma in audit | Angajamentul catre client |
| Realizat | Sistemul, la trecerea in `Finalizat` | O singura data | Realitatea |

A1.2.6.1 Diferenta `negociat - propus` masoara cat de des se promite mai mult decat se
poate. Diferenta `realizat - negociat` masoara respectarea angajamentului. Ambele se
raporteaza, separat, pe KAM si pe tehnolog. Sunt cele doua cifre care schimba discutia
anuala dintre R&D si comercial dintr-una despre impresii intr-una despre date.

### A1.2.7 Slotul de testare

A1.2.7.1 Slotul de testare pe linie este o **estimare negociabila, nu o constrangere
blocanta**. Sistemul propune primul slot disponibil pe linia vizata, pe baza cozii, dar nu
rezerva nimic in aplicatia de planificare a productiei si nu impiedica nimic.

A1.2.7.2 Arbitrajul intre doi KAM care vor acelasi slot il face Managerul R&D. Sistemul ii
arata: cele doua proiecte cu scorurile lor detaliate, bugetul de urgenta consumat de
fiecare KAM, si impactul asupra termenului fiecarui proiect daca este mutat. Decizia si
motivul se inregistreaza pe proiectul care pierde slotul.

A1.2.7.3 NOTA: legatura cu aplicatia interna de planificare (9 linii, 3 schimburi, sarje,
paleti, Gantt) ramane manuala in Valurile 0-3. Slotul propus de R&D se comunica
planificarii, care il confirma sau il muta. O integrare reala ar cere un API stabil pe
partea de planificare si este candidat pentru un val ulterior, nu pentru acest blueprint.
