# Sectiunea 4 - Livrabilele de proiect

## 4.1 Principiul

4.1.1 Cele ~30 de coloane din centralizatorul F-PS-LID-10.01 nu devin coloane. Devin
inregistrari in `rd_livrabil` (TBL-03), generate automat din `rd_sablonlivrabil`
(TBL-04) la acceptarea proiectului, prin FLX-05.

4.1.2 Motivul, in trei randuri: o coloana-bifa spune doar "exista sau nu", in timp ce o
inregistrare de livrabil spune cine il datoreaza, pana cand, in ce stadiu, cu ce document
si de ce nu se aplica. Numai a doua forma permite alertele, indicatorul Q-Complet si
raportul "livrabilele care intarzie cel mai des".

4.1.3 Fiecare livrabil are: denumire, cod stabil, faza, responsabil (rol si persoana),
termen, data realizarii, status, document atasat, obligatoriu sau optional, conditie de
aplicabilitate.

## 4.2 Conditiile de aplicabilitate

| Cod conditie | Se evalueaza pe | Livrabilul apare cand |
|---|---|---|
| C0 Intotdeauna | - | Mereu |
| C1 Doar MP noua | rd_proiect.rd_aremp | Proiectul are cel putin o materie prima noua |
| C2 Doar eticheta noua | rd_proiect.rd_tipproiect + cerinte client | Produsul primeste eticheta proprie (nu marca proprie a clientului cu eticheta lui) |
| C3 Doar client nou | rd_client.rd_proiecteactive = 0 la deschidere | Primul proiect cu acest client |
| C4 Doar ambalaj nou | Camp pe proiect `rd_ambalajnou` | Se schimba materialul sau formatul de ambalaj |
| C5 Doar linie nesetata | rd_linie.rd_capabilitati vs. cerinta produsului | Produsul cere o capabilitate pe care linia nu o are inca setata |
| C6 Doar export | rd_client.rd_tara != Romania | Cerinte suplimentare de eticheta si documentatie |
| C7 Doar produs nou | rd_tipproiect = Produs nou | Nu se aplica la reformulari sau abateri |

4.2.1 Conditiile se reevalueaza si dupa generare. Daca la doua saptamani de la acceptare
tehnologul marcheaza o materie prima ca noua, FLX-05 adauga livrabilele C1 lipsa, cu
termen recalculat, si notifica responsabilul. Livrabilele nu se sterg niciodata la
reevaluare: daca o conditie devine falsa, livrabilul trece in status `Nu se aplica`, cu
urma in audit.

## 4.3 Ce inseamna "obligatoriu"

4.3.1 Un livrabil marcat obligatoriu si aplicabil trebuie sa fie in status `Realizat`
pentru ca proiectul sa poata trece in `Finalizat`. Business rule pe `rd_proiect`
blocheaza tranzitia si afiseaza lista celor lipsa.

4.3.2 Minimul cerut explicit de blueprint - antecalcul, ST draft, ST finala, plan IPN,
dosarul de mostra, TDV validat - este acoperit de LIV-11, LIV-16, LIV-21, LIV-26,
LIV-09 si LIV-34.

4.3.3 Un livrabil obligatoriu poate fi marcat `Nu se aplica` numai de Managerul R&D, cu
motiv din nomenclator si comentariu. Aceasta este singura poarta de iesire si este
auditata.

## 4.4 Sablonul complet de livrabile

Legenda: Ob. = obligatoriu; Doc = necesita document atasat; Cond. = conditie de
aplicabilitate; Offset = zile de la data acceptarii, pe durata standard de 14 zile
lucratoare (vezi Sectiunea 14).

### Faza 00 - Solicitare

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent in centralizator |
|---|---|---|---|---|---|---|---|---|
| LIV-01 | SCP completat si trimis | KAM | Manager R&D | Da | Da | C0 | 0 | (nou, azi este mail) |
| LIV-02 | Eticheta produs client (EPC) primita | KAM | - | Nu | Da | C2 | 2 | (nou) |
| LIV-03 | Referinta de comparatie inregistrata | KAM | Tehnolog | Da | Nu | C0 | 1 | (nou) |
| LIV-04 | Cerinte de eticheta si ambalaj de la client | KAM | - | Nu | Da | C0 | 2 | (nou) |
| LIV-05 | Decizie de triaj cu motiv | Manager R&D | - | Da | Nu | C0 | 1 | (nou) |

### Faza 01 - Plan

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-06 | Plan de dezvoltare produs | Tehnolog | Manager R&D | Da | Da | C0 | 2 | PLAN DEZVOLTARE PRODUS |
| LIV-07 | Cerere achizitii mostra MP noua | Tehnolog | Achizitii | Da | Da | C1 | 3 | CERERE ACHIZITII MOSTRA MP NOUA |
| LIV-08 | Lista materiilor prime cu marcarea celor noi | Tehnolog | - | Da | Nu | C0 | 3 | (implicit azi) |
| LIV-09 | Slot de testare propus si negociat | Manager R&D | Planificare | Nu | Nu | C0 | 3 | (nou) |

### Faza 02 - Testare

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-10 | Fisa de test | Tehnolog | Manager R&D | Da | Da | C0 | 5 | FISA DE TEST |
| LIV-11 | Testare realizata (cel putin un trial reusit) | Tehnolog | - | Da | Nu | C0 | 8 | TESTARE REALIZATA |
| LIV-12 | Raport de testare cu masuratori si statistica | Tehnolog | Manager R&D | Da | Da | C0 | 9 | (partial: formularele Excel de masuratori) |
| LIV-13 | Evaluare produs (fisa de evaluare senzoriala) | Tehnolog | Manager R&D | Da | Da | C0 | 9 | EVALUARE PRODUS |
| LIV-14 | Test comparativ fata de referinta | Tehnolog | - | Nu | Nu | C0 | 9 | (nou) |

### Faza 03 - Mostre

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-15 | Mostre de produs pregatite si livrate | Suport R&D | - | Da | Nu | C0 | 10 | MOSTRE |
| LIV-16 | Dosar de mostra (fisa, poze, dovada livrarii) | Suport R&D | Tehnolog | Da | Da | C0 | 10 | (nou, cerut explicit ca obligatoriu) |
| LIV-17 | Feedback client la mostra | KAM | - | Da | Da | C0 | 12 | (nou) |

### Faza 04 - Antecalcul

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-18 | Antecalcul | Tehnolog | Manager R&D | Da | Da | C0 | 7 | ANTECALCUL |
| LIV-19 | Confirmare de pret de la client | KAM | - | Nu | Da | C0 | 12 | (nou) |

### Faza 05 - Specificatii

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-20 | Conditii ST | Tehnolog | Calitate | Da | Da | C0 | 6 | CONDITII ST |
| LIV-21 | ST draft | Tehnolog | Calitate | Da | Da | C0 | 10 | ST DRAFT |
| LIV-22 | ST interna pentru MP noua | Calitate | Calitate | Da | Da | C1 | 8 | ST INTERN MP NOUA |
| LIV-23 | Material SAP creat pentru MP noua | Achizitii | - | Da | Nu | C1 | 9 | MATERIAL SAP |
| LIV-24 | ST finala | Tehnolog | Calitate | Da | Da | C0 | 13 | ST FINAL |
| LIV-25 | SDP - specificatie de produs | Tehnolog | Calitate | Da | Da | C0 | 14 | SDP |
| LIV-26 | Material SAP creat pentru produsul finit | Tehnolog | Manager R&D | Da | Nu | C0 | 13 | MATERIAL SAP |
| LIV-27 | Alergeni si valori nutritionale calculate | Tehnolog | Calitate | Da | Nu | C0 | 12 | (nou) |

### Faza 06 - Eticheta

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-28 | Eticheta realizata (punga si bax) | Suport R&D | Calitate | Da | Da | C2 | 14 | ETICHETA REALIZATA |
| LIV-29 | Fisier de imprimanta Colos / Zebra | Suport R&D | - | Nu | Da | C2 | 15 | (implicit azi) |
| LIV-30 | Eticheta implementata pe linie | Productie | Tehnolog | Da | Nu | C2 | 18 | ETICHETA IMPLEMENTATA |

### Faza 07 - Implementare

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-31 | Conditii IPN | Tehnolog | Manager R&D | Da | Da | C0 | 15 | CONDITII IPN |
| LIV-32 | Plan IPN | Tehnolog | Manager R&D | Da | Da | C0 | 15 | PLAN IPN |
| LIV-33 | IL productie creata | Tehnolog | Productie | Da | Da | C0 | 16 | CREAZA IL PROD |
| LIV-34 | Plan HACCP actualizat si aprobat | Calitate | Calitate | Da | Da | C0 | 16 | PLAN HACCP |
| LIV-35 | Instruire operatori efectuata | Productie | Tehnolog | Da | Da | C0 | 17 | (nou, cerinta IFS) |
| LIV-36 | Productie 0 realizata si inregistrata | Tehnolog | Manager R&D | Da | Da | C0 | 18 | PROD 0 |
| LIV-37 | Raport de productie 0 cu decizie | Tehnolog | Manager R&D si Calitate | Da | Da | C0 | 19 | (nou, vezi Sectiunea 7) |

### Faza 08 - Dosar validat

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-38 | Dosar validat complet | Suport R&D | Manager R&D | Da | Da | C0 | 20 | DOSAR VALIDAT |
| LIV-39 | TDV validat, semnat R&D si Calitate | Manager R&D | Calitate | Da | Da | C0 | 20 | TDV VALIDAT |
| LIV-40 | Predare catre productie si comercial | Manager R&D | - | Da | Nu | C0 | 20 | (nou) |

### Faza 09 - Post-implementare (nu blocheaza inchiderea)

| Cod | Livrabil | Rol responsabil | Rol aprobator | Ob. | Doc | Cond. | Offset | Corespondent |
|---|---|---|---|---|---|---|---|---|
| LIV-41 | Revizuire la 30 de zile | Manager R&D | - | Nu | Da | C0 | +30 | (nou, Sectiunea 8) |
| LIV-42 | Revizuire la 60 de zile | Manager R&D | - | Nu | Da | C0 | +60 | (nou) |
| LIV-43 | Revizuire la 90 de zile cu decizie finala | Manager R&D | Head of R&D | Da | Da | C0 | +90 | (nou) |

## 4.5 Acoperirea coloanelor din centralizatorul actual

| Coloana actuala | Livrabil nou | Observatie |
|---|---|---|
| PLAN DEZVOLTARE PRODUS | LIV-06 | Devine document generat din date, vezi 5.5.2 |
| CERERE ACHIZITII MOSTRA MP NOUA | LIV-07 | Conditionat C1 |
| FISA DE TEST | LIV-10 | Devine inregistrare TBL-14, nu fisier |
| ANTECALCUL | LIV-18 | Devine TBL-22 cu linii |
| TESTARE REALIZATA | LIV-11 | Se bifeaza automat la primul trial cu rezultat Reusit |
| EVALUARE PRODUS | LIV-13 | Devine TBL-17 cu grila din 6.5 |
| DOSAR VALIDAT | LIV-38 | - |
| ST DRAFT | LIV-21 | - |
| MOSTRE | LIV-15 | Plus dosarul de mostra LIV-16 |
| CONDITII ST | LIV-20 | - |
| ETICHETA REALIZATA | LIV-28 | Conditionat C2 |
| ST INTERN MP NOUA | LIV-22 | Conditionat C1 |
| MATERIAL SAP | LIV-23 si LIV-26 | Se separa MP de produs finit; azi sunt confundate |
| ST FINAL | LIV-24 | - |
| CONDITII IPN | LIV-31 | - |
| PLAN IPN | LIV-32 | - |
| ETICHETA IMPLEMENTATA | LIV-30 | Conditionat C2 |
| CREAZA IL PROD | LIV-33 | - |
| PLAN HACCP | LIV-34 | - |
| PROD 0 | LIV-36 | Plus raportul LIV-37 |
| SDP | LIV-25 | - |
| TDV VALIDAT | LIV-39 | - |

4.5.1 Sase coloane devin doua livrabile fiecare, pentru ca astazi acopera doua obligatii
diferite sub o singura bifa (MATERIAL SAP, MOSTRE, PROD 0). Aceasta este principala
sursa de "bifat, dar incomplet" din evidenta actuala.

4.5.2 Livrabile complet noi, adaugate ca expert: LIV-01 - LIV-05 (faza de solicitare, azi
inexistenta ca evidenta), LIV-12, LIV-14, LIV-17, LIV-19, LIV-27, LIV-35, LIV-37, LIV-40,
LIV-41 - LIV-43. Motiv: fara ele nu se poate calcula Q-Complet si nu se poate demonstra
la audit lantul cerinta - testare - validare.

## 4.6 Generarea si termenele

4.6.1 FLX-05 genereaza livrabilele la trecerea proiectului in `Acceptat - planificat`,
filtrand sablonul dupa `rd_tipproiect` si evaluand conditiile din 4.2.

4.6.2 Termenul fiecarui livrabil = data acceptarii + offset in zile lucratoare, ajustat
proportional daca durata standard a proiectului difera de 14 zile:
`termen = data_acceptare + ROUND(offset * durata_proiect / 14)` zile lucratoare.

4.6.3 Livrabilele post-implementare (LIV-41 - LIV-43) se genereaza separat, de FLX-15, la
completarea `rd_implementare.rd_dataimplementare`, cu offset fata de acea data.

4.6.4 Reatribuirea proiectului catre alt tehnolog reatribuie toate livrabilele cu rol
responsabil `Tehnolog` care nu sunt inca in status `Realizat`. Cele realizate isi pastreaza
responsabilul istoric, ca sa nu se rescrie trecutul.

## 4.7 Sabloane pe tip de proiect

| Tip proiect | Livrabile excluse din sablon | Motiv |
|---|---|---|
| Produs nou | - | Sablonul complet |
| Reformulare | LIV-03, LIV-26 | Referinta este produsul actual; codul SAP exista deja |
| Abatere (.1) | LIV-06, LIV-18, LIV-26, LIV-38 | Mosteneste de la parinte, se refac doar testarea si specificatia |
| Transfer pe alta linie | LIV-18, LIV-20, LIV-21, LIV-24, LIV-28 | Reteta si eticheta raman; se reface doar implementarea |
| Optimizare cost | LIV-02, LIV-03, LIV-28, LIV-30 | Eticheta nu se schimba daca lista de ingrediente ramane identica |
| Ambalaj nou | LIV-08, LIV-10 - LIV-14, LIV-27 | Produsul nu se schimba; se reface eticheta si IPN-ul |

4.7.1 NOTA: exceptia de la 4.7 este alergenul. Orice optimizare de cost care schimba o
materie prima reactiveaza LIV-27 si LIV-28, chiar daca sablonul le excludea, pentru ca
declaratia de pe eticheta trebuie sa ramana corecta. Regula se implementeaza in FLX-13, nu
in sablon.
