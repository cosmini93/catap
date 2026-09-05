# Sectiunea 3 - Diagrama relatiilor

## 3.1 Conventii

3.1.1 Relatie **parentala**: copilul nu are sens fara parinte. Comportament la stergere
`Cascade All` sau `Parental`; drepturile de securitate se mostenesc de la parinte, deci
cine vede proiectul vede si copiii.

3.1.2 Relatie **referentiala**: cele doua inregistrari exista independent. Comportament
`Restrict Delete` pentru nomenclatoare (nu se sterge o linie de productie folosita in
proiecte) sau `Remove Link` acolo unde legatura este informativa.

3.1.3 NOTA de platforma: relatia parentala transmite si atribuirea (Assign) si partajarea
(Share). Din acest motiv, `rd_proiect` -> `rd_livrabil` este parentala (livrabilul urmeaza
proiectul cand acesta se reatribuie altui tehnolog), dar `rd_proiect` ->
`rd_proiectparinte` este referentiala (proiectul-copil are propriul responsabil si nu
trebuie sa isi schimbe proprietarul odata cu parintele).

3.1.4 Cascade Delete se foloseste doar unde stergerea are sens de business. In rest,
stergerea este interzisa prin rol de securitate: inregistrarile se dezactiveaza, nu se
sterg. Pentru un mediu certificat IFS, stergerea fizica a unei inregistrari de proiect
este un risc de audit, nu o facilitate.

## 3.2 Arborele principal

```
rd_solicitare (SCP)
  |
  +-- 1:N referential --> rd_proiect                      [Remove Link]
                            |
  rd_proiect (RADACINA)     |
  |                         |
  +-- 1:N PARENTAL --> rd_livrabil                        [Cascade All]
  +-- 1:N PARENTAL --> rd_etapa                           [Cascade All]
  +-- 1:N PARENTAL --> rd_mpproiect                       [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_iteratiefurnizor   [Cascade All]
  +-- 1:N PARENTAL --> rd_blocaj                          [Cascade All]
  +-- 1:N PARENTAL --> rd_ceremostra                      [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_miscaremostra      [Cascade All]
  +-- 1:N PARENTAL --> rd_fisatestare                     [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_trial             [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_masuratoare      [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_statisticatrial  [Cascade All]
  +-- 1:N PARENTAL --> rd_evaluaresenzoriala              [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_scorsenzorial      [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_defectconstatat    [Cascade All]
  +-- 1:N PARENTAL --> rd_referinta                       [Cascade All]
  +-- 1:N PARENTAL --> rd_reteta                          [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_versiunereteta     [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_liniereteta      [Cascade All]
  +-- 1:N PARENTAL --> rd_antecalcul                      [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_linieantecalcul    [Cascade All]
  +-- 1:N PARENTAL --> rd_specificatie                    [Cascade All]
  +-- 1:N PARENTAL --> rd_sdp                             [Cascade All]
  +-- 1:N PARENTAL --> rd_eticheta                        [Cascade All]
  +-- 1:N PARENTAL --> rd_implementare                    [Cascade All]
  |                      +-- 1:N PARENTAL --> rd_productie0         [Cascade All]
  |                                             +-- 1:N PARENTAL --> rd_inregistrareprod0 [Cascade All]
  +-- 1:N PARENTAL --> rd_revizuire                       [Cascade All]
  +-- 1:N REFERENTIAL (auto) --> rd_proiect (copil .1)    [Remove Link]
```

## 3.3 Relatiile catre nomenclatoare (toate referentiale)

| Cod | Parinte | Copil | Coloana lookup | Comportament la stergere | Tip |
|---|---|---|---|---|---|
| REL-01 | rd_client | rd_solicitare | rd_client | Restrict | Referential |
| REL-02 | rd_client | rd_proiect | rd_client | Restrict | Referential |
| REL-03 | rd_client | rd_referinta | rd_client | Remove Link | Referential |
| REL-04 | rd_linie | rd_proiect | rd_linie | Restrict | Referential |
| REL-05 | rd_linie | rd_trial | rd_linie | Restrict | Referential |
| REL-06 | rd_linie | rd_fisatestare | rd_linie | Remove Link | Referential |
| REL-07 | rd_linie | rd_antecalcul | rd_linie | Restrict | Referential |
| REL-08 | rd_linie | rd_implementare | rd_linie | Restrict | Referential |
| REL-09 | rd_linie | rd_productie0 | rd_linie | Restrict | Referential |
| REL-10 | rd_materieprima | rd_mpproiect | rd_materieprima | Restrict | Referential |
| REL-11 | rd_materieprima | rd_liniereteta | rd_materieprima | Restrict | Referential |
| REL-12 | rd_materieprima | rd_linieantecalcul | rd_materieprima | Restrict | Referential |
| REL-13 | rd_materieprima | rd_specificatie | rd_materieprima | Remove Link | Referential |
| REL-14 | rd_furnizor | rd_materieprima | rd_furnizor | Remove Link | Referential |
| REL-15 | rd_furnizor | rd_mpproiect | rd_furnizor | Remove Link | Referential |
| REL-16 | rd_furnizor | rd_iteratiefurnizor | rd_furnizor | Restrict | Referential |
| REL-17 | rd_motiv | rd_solicitare | rd_motivtriaj | Restrict | Referential |
| REL-18 | rd_motiv | rd_proiect | rd_motivstatus | Restrict | Referential |
| REL-19 | rd_motiv | rd_iteratiefurnizor | rd_motivrespingere | Restrict | Referential |
| REL-20 | rd_criteriusenzorial | rd_scorsenzorial | rd_criteriu | Restrict | Referential |
| REL-21 | rd_defect | rd_defectconstatat | rd_defect | Restrict | Referential |
| REL-22 | rd_sablonlivrabil | rd_livrabil | rd_sablon | Remove Link | Referential |
| REL-23 | rd_sablonetapa | rd_etapa | rd_sablon | Remove Link | Referential |
| REL-24 | rd_sablonetapa | rd_sablonlivrabil | rd_etapa | Remove Link | Referential |
| REL-25 | rd_indicator | rd_masurareindicator | rd_indicator | Cascade All | Parental |

## 3.4 Relatiile transversale (referentiale, in interiorul proiectului)

Aceste relatii leaga copii ai aceluiasi proiect intre ei. Toate sunt referentiale cu
`Remove Link`, ca stergerea unui trial sa nu distruga evaluarea senzoriala facuta pe el.

| Cod | De la | La | Coloana | Motiv |
|---|---|---|---|---|
| REL-30 | rd_fisatestare | rd_versiunereteta | rd_versiunereteta | Ce reteta se testeaza |
| REL-31 | rd_evaluaresenzoriala | rd_trial | rd_trial | Ce s-a degustat |
| REL-32 | rd_evaluaresenzoriala | rd_referinta | rd_referinta | Comparatia |
| REL-33 | rd_antecalcul | rd_versiunereteta | rd_versiunereteta | Pe ce reteta s-a calculat |
| REL-34 | rd_linieantecalcul | rd_mpproiect | rd_mpproiect | MP fara cod SAP inca |
| REL-35 | rd_liniereteta | rd_mpproiect | rd_mpproiect | Idem |
| REL-36 | rd_sdp | rd_versiunereteta | rd_versiunereteta | Ce reteta se implementeaza |
| REL-37 | rd_blocaj | rd_etapa | rd_etapa | Pe ce etapa se opreste ceasul |
| REL-38 | rd_ceremostra | rd_mpproiect | rd_mpproiect | Mostra pentru ce MP |
| REL-39 | rd_productie0 | rd_implementare | rd_implementare | Pe ce IPN |
| REL-40 | rd_specificatie | rd_specificatie | rd_inlocuieste | Lantul de versiuni |
| REL-41 | rd_reteta | rd_versiunereteta | rd_versiunecurenta | Care versiune este in vigoare |
| REL-42 | rd_proiect | rd_referinta | rd_referinta | Referinta activa a proiectului |
| REL-43 | rd_trial | rd_proiect | rd_proiect | Denormalizare pentru raportare |

3.4.1 REL-41 si REL-42 sunt referinte "inapoi", de la parinte la un copil anume. Sunt
necesare pentru ca formularul de proiect trebuie sa arate versiunea curenta si referinta
activa fara sa parcurga o subgrila. Se scriu de flux, nu manual.

3.4.2 REL-43 duplica informatia disponibila prin fisa de testare. Este acceptata
constient: raportarea pe trialuri la nivel de departament ar cere altfel un join pe doua
niveluri, ceea ce in vizualizarile native Dataverse nu se poate.

## 3.5 Relatiile catre systemuser

Toate lookup-urile catre `systemuser` sunt referentiale cu `Remove Link`. Nu se sterge
niciodata un utilizator din Dataverse; se dezactiveaza. Coloanele afectate:
`rd_kam`, `rd_tehnolog`, `rd_manager`, `rd_responsabil`, `rd_aprobator`, `rd_autor`,
`rd_evaluator`, `rd_masuratde`, `rd_solicitant`, `rd_persoana`, `rd_preluatde`,
`rd_aprobatorcalitate`.

3.5.1 Proprietarul inregistrarii (`ownerid`) este intotdeauna tehnologul alocat pentru
proiect si copiii lui, ca sa functioneze securitatea la nivel de User / Business Unit
descrisa in Sectiunea 11. Reatribuirea proiectului reatribuie toti copiii, prin
comportamentul parental Cascade All pe Assign.

## 3.6 Relatia cu SharePoint

3.6.1 Legatura documentelor se face prin integrarea nativa Dataverse - SharePoint, care
creeaza automat, pentru tabela `rd_proiect`, o relatie catre entitatea de sistem
`SharePointDocumentLocation`. Nu se construieste o tabela proprie de documente.

3.6.2 Locatia se personalizeaza in FLX-02 astfel incat folderul sa nu fie generat de
platforma in formatul implicit `{nume}_{guid}`, ci in formatul cerut la 5.1:
`/PRODUSE IN DEZVOLTARE/{an}/{cod}_{nume produs}/`.

3.6.3 NOTA: integrarea nativa creeaza implicit un singur folder per inregistrare, fara
subfoldere. Arborele pe faze din 5.1 se creeaza cu FLX-02 (actiune SharePoint "Creeaza
folder"), iar `SharePointDocumentLocation` se seteaza catre folderul radacina al
proiectului. Subfolderele sunt vizibile in controlul de documente din formular.

## 3.7 Diagrama compacta a fluxului de date

```
SCP --triaj--> PROIECT --sablon--> LIVRABILE + ETAPE
                 |
                 +--> MP PROIECT --> ITERATII FURNIZOR --> (ETA) --> recalcul termen
                 |
                 +--> RETETA --> VERSIUNE --> LINII --> ALERGENI + NUTRITIONALE
                 |                    |
                 |                    +--> ANTECALCUL --> MARJA
                 |                    |
                 |                    +--> FISA TESTARE --> TRIAL --> MASURATORI --> STATISTICA
                 |                                            |
                 |                                            +--> EVALUARE SENZORIALA --> VERDICT
                 |
                 +--> SPECIFICATIE (ST) --> SDP --> ETICHETA
                 |                            |
                 |                            +--> IMPLEMENTARE (IPN) --> PRODUCTIE 0
                 |                                                            |
                 |                                                            +--> REVIZUIRE 30/60/90
                 |
                 +--> BLOCAJE --> oprirea ceasului --> T-TOTAL
```
