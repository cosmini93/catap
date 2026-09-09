# Volumul 1 - Arhitectura, modelul de date si documentatia

Parte din blueprintul Suitei Digitale R&D, export din 09.09.2026.
Contine sectiunile: S00-sumar-executiv, S01-harta-modulelor, S02-model-date, S03-relatii, S04-livrabile, S05-documentatie.

Contextul complet al proiectului este in preambulul din `BLUEPRINT-COMPLET.md`.



<!-- ==================== S00-sumar-executiv.md ==================== -->

---

# Sectiunea 0 - Sumar executiv

0.1 Se inlocuieste centralizatorul Excel F-PS-LID-10.01 si evidenta pe foldere cu o
baza de date Dataverse in care proiectul CDI este radacina, iar cele ~30 de bife de azi
devin inregistrari de livrabil generate automat din sablon la acceptarea proiectului.

0.2 Datele stau in Dataverse, fisierele raman in SharePoint intr-un arbore pe faze
generat automat, legat de proiect prin integrarea nativa de documente.

0.3 Doua interfete: o aplicatie model-driven pentru birou (triaj, alocare, coada,
aprobari, rapoarte) si o aplicatie canvas pentru hala si laborator (masuratori la linie,
evaluare senzoriala, receptie mostra, checklist productie 0).

0.4 Prioritizarea devine un scor automat pe 100 de puncte, recalculat saptamanal, cu
buget de urgenta pe KAM si imbatranire in coada, suprascriabil doar cu motiv si urma
in audit.

0.5 Termenul are trei valori distincte - propus de sistem, negociat cu KAM, realizat -
iar blocajele externe opresc ceasul indicatorului R&D fara sa opreasca termenul catre
client.

0.6 Doua procese care azi nu exista se nasc din blueprint: inregistrarea structurata a
productiei 0 si revizuirea post-implementare declansata automat la 30, 60 si 90 de zile.

0.7 Alergenii si valorile nutritionale se calculeaza din reteta, cu recalculare automata
la orice schimbare de materie prima sau de versiune de reteta.

0.8 Trasabilitatea IFS / ISO / HACCP se obtine din audit nativ Dataverse plus versionare
SharePoint, astfel incat dosarul de produs sa fie reconstituibil la orice data din trecut.

0.9 Constructia se face intr-un mediu Developer, intr-o Solution unica exportata
periodic pe OneDrive, in patru valuri: Val 0 fundatie, Val 1 MVP la 30 de zile, Val 2 la
90 de zile, Val 3 la 6 luni.

0.10 Rezultatul masurabil la 6 luni: T-Total, Q-Corect si Q-Complet calculate automat pe
activitate, rol si persoana, cu tinte de 95-98%, si o coada de proiecte vizibila intregii
companii fara instruire.


<!-- ==================== S01-harta-modulelor.md ==================== -->

---

# Sectiunea 1 - Harta modulelor

## 1.1 Tabelul modulelor

Prioritate: 1 = fara el nu functioneaza nimic; 2 = necesar pentru operare completa;
3 = valoare adaugata dupa stabilizare.

| Cod | Modul | Proces acoperit | Rol principal | Tip aplicatie | Prioritate | Val |
|---|---|---|---|---|---|---|
| M01 | Fundatie si nomenclatoare | Mediu, Solution, prefix editor, linii, clienti, tipuri de documente, roluri | Head of R&D (constructor) | Model-driven (configurare) | 1 | Val 0 |
| M02 | Solicitare (SCP) | Deschiderea cererii de catre KAM, varianta de rezerva pe mail | KAM | Model-driven + formular canvas simplificat | 1 | Val 1 |
| M03 | Triaj si generare proiect | Acceptat / respins / amanat cu motiv, generare cod {AA}{NNN}, creare folder | Manager R&D | Model-driven | 1 | Val 1 |
| M04 | Proiect CDI si versiuni | Radacina proiectului, proiecte-copil cu sufix .1, mostenire referinte | Manager R&D, tehnolog | Model-driven | 1 | Val 1 |
| M05 | Livrabile de proiect | Generarea din sablon a celor 43 de livrabile, termen, responsabil, status | Tehnolog | Model-driven | 1 | Val 1 |
| M06 | Etape si durate | Sablon de etape, durata standard 2 saptamani, data estimata de finalizare | Manager R&D | Model-driven | 2 | Val 1 |
| M07 | Alocare si incarcare | Alocarea tehnologului, incarcarea pe tehnolog si pe linie, praguri vizuale | Manager R&D | Model-driven (dashboard) | 1 | Val 1 |
| M08 | Prioritizare | Scor 100 de puncte, benzi P1-P4, buget de urgenta, imbatranire, suprascriere | Manager operational / vanzari | Model-driven + flux programat | 2 | Val 2 |
| M09 | Materii prime si aprovizionare | Lista MP pe proiect, ciclul MP noua, iteratii de furnizor, lead time, ETA | Achizitii | Model-driven | 2 | Val 2 |
| M10 | Mostre | Cerere de mostra, miscari, receptie, evidenta livrarilor la client | Suport R&D | Canvas (receptie) + model-driven | 2 | Val 2 |
| M11 | Blocaje si oprirea ceasului | Cine blocheaza, din ce data, impact in zile, efect asupra T-Total | Manager R&D | Model-driven | 2 | Val 2 |
| M12 | Testare si masuratori | Fisa de testare, trial, masuratori la linie, statistica, conformitate | Tehnolog | Canvas mobil | 1 | Val 1 |
| M13 | Evaluare senzoriala | Grila ponderata 1-5, defecte, verdict, comparatie cu referinta | Tehnolog, panel | Canvas mobil | 2 | Val 2 |
| M14 | Reteta si antecalcul | Versiuni de reteta, linii de reteta, antecalcul si linii de antecalcul | Tehnolog | Model-driven | 2 | Val 2 |
| M15 | Alergeni si nutritionale | Calcul din reteta, urme si contaminare incrucisata, recalculare automata | Tehnolog, Calitate | Model-driven (rollup + flux) | 3 | Val 3 |
| M16 | Specificatii si SDP | ST draft / final / intern MP, SDP ca suport pentru IL | Tehnolog, Calitate | Model-driven | 2 | Val 2 |
| M17 | Etichete | Eticheta punga, bax, EPC, fisier de imprimanta Colos / Zebra | Suport R&D | Model-driven | 3 | Val 3 |
| M18 | Implementare (IPN) | Conditii IPN, plan IPN, IL productie, plan HACCP | Tehnolog, Calitate, Productie | Model-driven | 2 | Val 2 |
| M19 | Productie 0 | Checklist la linie, randament, rebut, parametri reali, decizie finala | Tehnolog, Productie | Canvas mobil | 2 | Val 2 |
| M20 | Revizuire post-implementare | Declansare automata la 30 / 60 / 90 de zile, decizie de mentinere | Manager R&D, KAM | Model-driven + flux programat | 3 | Val 3 |
| M21 | Documente si sabloane | Arbore de foldere, denumire, metadate, versionare, generare din Word | Suport R&D | SharePoint + Power Automate | 1 | Val 1 |
| M22 | Indicatori si raportare | T-Total, Q-Corect, Q-Complet, rapoarte operationale si anuale | Head of R&D | Power BI + vizualizari native | 3 | Val 3 |
| M23 | Ecran public de status | Status vizibil intregii companii, read-only, fara instruire | Toata compania | Model-driven dashboard partajat | 2 | Val 2 |
| M24 | Securitate si roluri | Matrice Rol x Tabela, roluri externe R&D, rol de cititor global | Head of R&D | Configurare | 1 | Val 0 |
| M25 | Migrare | Import din centralizator si din foldere, curatare, proiecte in curs | Head of R&D | Dataflow / import Excel | 2 | Val 1 |
| M26 | Gate-uri | Stage-gate cu criterii, decizii GO / conditii / HOLD / REWORK / STOP | Manager R&D | Model-driven | 1 | Val 1 |
| M27 | Actiuni centralizate | O singura coada de actiuni, din toate sursele | Toti | Model-driven | 1 | Val 1 |
| M28 | Riscuri si probleme | Registru de riscuri cu RPN, registru de probleme cu cauza radacina | Manager R&D, tehnolog | Model-driven | 2 | Val 2 |
| M29 | Jurnal de decizii | Context, alternative, motiv, ipoteze, reevaluare | Manager R&D | Model-driven | 3 | Val 2 |
| M30 | Stabilizare | Trei loturi consecutive conforme inainte de release | Tehnolog, Productie | Model-driven + canvas | 2 | Val 3 |
| M31 | Capabilitate de proces | Cp si Cpk pe gramaj si parametri critici | Tehnolog, Calitate | Model-driven | 3 | Val 3 |
| M32 | Lectii invatate | Generare de drafturi, aprobare, recomandare, urmarirea reutilizarii | Toti | Model-driven | 3 | Val 3 |
| M33 | Sanatatea proiectului | Snapshot saptamanal, tendinta, alerta de degradare | Manager R&D | Dashboard | 3 | Val 3 |
| M34 | Validare si feedback de client | Validari, feedback pe mostra si lansare | KAM | Model-driven | 3 | Val 4 |
| M35 | Reclamatii | Legate de produs, lot si proiect | Calitate | Model-driven | 3 | Val 4 |
| M36 | Neconformitati si CAPA | Cu evaluarea eficacitatii la 30 de zile | Calitate | Model-driven | 3 | Val 4 |
| M37 | Performanta furnizorilor | Scorecard, incidente, OTIF, acuratetea ETA | Achizitii | Model-driven | 3 | Val 4 |
| M38 | Business case si buget | Buget pe proiect, urmarirea consumului | Head of R&D | Model-driven | 3 | Val 5 |
| M39 | Cost real de productie | Cost real, giveaway, comparatie cu antecalculul | Head of R&D | Power BI | 3 | Val 5 |
| M40 | Realizarea beneficiilor | La 3, 6, 12 si 24 de luni | Head of R&D | Model-driven | 3 | Val 5 |
| M41 | Registru de documente tehnice | Ciclu de viata si harta de dependente | Suport R&D | Model-driven | 3 | Val 5 |

## 1.2 Dependente intre module

| Modul | Depinde de | Motiv |
|---|---|---|
| M03 | M01, M02 | Codul de proiect are nevoie de an si de nomenclatorul de tipuri |
| M05 | M04, M06 | Livrabilul se ataseaza proiectului si isi ia termenul din etapa |
| M07 | M04, M06 | Incarcarea se calculeaza din proiectele active si din etape |
| M08 | M04, M07, M09 | Scorul foloseste volum, client, efort si riscul de MP noua |
| M11 | M04, M06 | Blocajul opreste ceasul pe etapa curenta |
| M12 | M04, M14 | Trialul se face pe o versiune de reteta |
| M15 | M14, M09 | Alergenii se calculeaza din linii de reteta si date de MP |
| M18 | M16 | Planul IPN presupune ST finala aprobata |
| M19 | M18 | Productia 0 se face pe conditiile IPN aprobate |
| M20 | M19 | Revizuirea compara seria cu productia 0 |
| M22 | M06, M11 | T-Total are nevoie de etape si de blocaje pentru oprirea ceasului |
| M26 | M04, M05, M06 | Gate-ul verifica livrabilele si se aseaza la iesirea dintr-o etapa |
| M28 | M04, M27 | Riscul si problema genereaza actiuni in tabela centrala |
| M30 | M19 | Stabilizarea porneste de la productia 0 validata |
| M31 | M30, M12 | Capabilitatea are nevoie de minimum 30 de masuratori pe 3 loturi |
| M32 | M28, M19 | Drafturile de lectii se genereaza din probleme si din productia 0 |
| M33 | M28, M05, M09 | Scorul de sanatate agrega riscuri, livrabile si aprovizionare |

## 1.3 Ce nu face aceasta solutie

1.3.1 Nu inlocuieste SAP si nu scrie in SAP. Codurile de material se creeaza in SAP de
catre rolurile actuale si se inregistreaza in Dataverse ca text, cu data si autorul
inregistrarii.

1.3.2 Nu inlocuieste aplicatia interna de planificare a productiei. Coada pe linie din
R&D este o estimare negociabila; planificarea reala ramane in aplicatia existenta.
Legatura se face prin codul liniei si prin slotul de testare propus.

1.3.3 Nu defineste formatul intern al ST. Blueprintul defineste doar inregistrarea,
statusul, versiunea si legatura documentului ST cu proiectul.

1.3.4 Nu contine cod si nu contine formule Power Fx, cu exceptia regulilor de calcul
care nu pot fi exprimate altfel (scor de prioritate, statistica de masuratori, alergeni,
RPN, Cp si Cpk, scor de sanatate).

1.3.5 Nu construieste modulele din Anexa A2 pana cand criteriile lor de activare nu sunt
indeplinite. Modulele M26-M41 provin din sinteza cu blueprintul Enterprise (Sectiunea 22);
tot ce nu apare in tabelul de mai sus a fost amanat sau respins explicit, cu motiv.


<!-- ==================== S02-model-date.md ==================== -->

---

# Sectiunea 2 - Modelul de date Dataverse

## 2.0 Reguli generale de modelare

2.0.1 Prefix de editor: `rd`. Toate tabelele si coloanele au nume logic `rd_...`, fara
diacritice, fara spatii, cu cuvinte lipite sau separate prin `_` doar acolo unde
lizibilitatea o cere. Prefixul nu se schimba niciodata dupa primul export de solutie.

2.0.2 Solution unica: `RDSuitaDigitala`, editor `RD Digital (rd)`. Tot ce se construieste
intra in ea, de la primul tabel. Export saptamanal, managed si unmanaged, pe OneDrive,
in `/RD_Solutions/{AAAALLZZ}_RDSuitaDigitala_v{n}.zip`.

2.0.3 Coloana primara: fiecare tabela are o coloana primara de tip Text cu rol de
identificator lizibil. Unde exista numar de document, coloana primara este Autonumber.
Unde nu, coloana primara se completeaza automat prin flux sau regula de business, ca sa
nu ramana niciodata "Nou".

2.0.4 Toate statusurile sunt Choice, niciodata text liber. Toate seturile de optiuni
folosite in mai multe tabele sunt Choice globale (Global Option Set), definite o singura
data.

2.0.5 Se folosesc doua campuri de stare native: `statecode` (Active / Inactive) si
`statuscode`. Statusul de business al proiectului este o coloana Choice proprie
`rd_status`, nu `statuscode`, pentru ca ciclul de business nu se suprapune peste ciclul
tehnic al inregistrarii.

2.0.6 Datele fara ora se modeleaza `Date Only`, cu comportament `User Local` doar acolo
unde ora conteaza (masuratori, trial, miscari de mostra); in rest `Date Only` cu
comportament `Time Zone Independent`, ca sa nu apara decalaje de o zi intre amplasamente.

2.0.7 Auditul se activeaza la nivel de mediu si, explicit, pe toate tabelele din 2.1-2.9
si pe coloanele de status, termen, cantitate, decizie si aprobare.

2.0.8 Rollup-urile Dataverse se recalculeaza la interval de o ora. Unde valoarea trebuie
sa fie exacta in momentul citirii (scor de prioritate, conformitate), se foloseste o
coloana obisnuita scrisa de flux, nu Rollup.

2.0.9 NOTA de platforma: Calculated si Rollup nu pot referi decat relatii 1:N directe si
nu accepta filtre pe campuri de tip lookup din alta tabela. Toate calculele pe mai multe
niveluri (alergeni din reteta, scor de prioritate, T-Total cu oprirea ceasului) se fac cu
flux Power Automate programat sau declansat, si se scriu in coloane simple.

2.0.10 Zecimale: pretul si costul in `Currency` cu 4 zecimale (materiile prime au costuri
sub 1 leu pe kilogram in unele cazuri); cantitatile in `Decimal` cu 4 zecimale; procentele
in `Decimal` cu 2 zecimale, interval 0-100.

## 2.1 TBL-01 Solicitare (SCP)

Nume: `rd_solicitare`. Rol: cererea deschisa de KAM, inainte de a exista proiect.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar SCP | rd_numarscp | Autonumber | Da | SCP-{AA}-{SEQ:0000} | Se genereaza la salvare | Coloana primara |
| Client | rd_client | Lookup (rd_client) | Da | - | Clientul din nomenclator | Nu se accepta client liber |
| Lant sau canal | rd_canal | Choice | Da | Retail modern / Retail traditional / HoReCa / Industrial / Export / Marca proprie | - | Choice global CANAL |
| KAM solicitant | rd_kam | Lookup (systemuser) | Da | - | Implicit utilizatorul curent | Se pastreaza si daca omul pleaca |
| Sursa solicitarii | rd_sursa | Choice | Da | Aplicatie / Mail preluat de suport R&D / Sedinta comerciala | Implicit Aplicatie | Varianta de rezerva se marcheaza explicit |
| Preluat de | rd_preluatde | Lookup (systemuser) | Nu | - | Obligatoriu daca sursa = Mail preluat | Business rule |
| Produs dorit | rd_produsdorit | Text (200) | Da | - | - | Denumire de lucru |
| Descriere cerinta | rd_descriere | Text Area (4000) | Da | - | - | Text liber de la client |
| Gramaj (g) | rd_gramaj | Decimal (2) | Da | 1 - 20000 | - | Pe bucata |
| Numar bucati pe ambalaj | rd_bucatiambalaj | Whole Number | Nu | 1 - 500 | - | - |
| Dimensiuni cerute | rd_dimensiuni | Text (100) | Nu | LxlxH mm | - | Text structurat, validat vizual |
| Tip ambalare | rd_tipambalare | Choice | Da | Punga / Tava / Bax direct / Vrac / Flow-pack / Termoformat | - | Choice global AMBALARE |
| Volum estimat anual (kg) | rd_volumanual | Decimal (2) | Da | 0 - 10000000 | Intra in scorul de prioritate | Banda, nu liniar |
| Termen dorit de client | rd_termendorit | Date Only | Da | >= azi | - | Nu este angajament |
| Termen impus extern | rd_termenimpus | Yes/No | Da | Implicit Nu | Da doar cu tip si data | Listare, sezon |
| Tip termen impus | rd_tiptermenimpus | Choice | Nu | Listare retail / Sezon / Licitatie / Lansare client / Altul | Obligatoriu daca rd_termenimpus = Da | - |
| Motivul cererii | rd_motivcerere | Choice | Da | Client nou / Extindere portofoliu / Inlocuire produs / Cerere de pret / Reformulare / Reactie la concurenta / Reglementare | - | Choice global MOTIVCERERE |
| Referinta de comparatie | rd_tipreferinta | Choice | Da | Produs concurenta / Produs actual / Mostra client / Specificatie client / Inexistenta | Obligatoriu la deschidere | Vezi 6.4 |
| Detalii referinta | rd_detaliireferinta | Text (300) | Nu | - | Obligatoriu daca referinta != Inexistenta | - |
| Cerinte de eticheta | rd_cerinteeticheta | Text Area (2000) | Nu | - | - | Limba, logo, declaratii |
| Cerinte de ambalaj | rd_cerinteambalaj | Text Area (2000) | Nu | - | - | Material, print, dimensiune bax |
| Rezultat triaj | rd_rezultattriaj | Choice | Nu | Acceptata / Respinsa / Amanata | Se completeaza doar de Manager R&D | Vezi 2.1.1 |
| Motiv triaj | rd_motivtriaj | Lookup (rd_motiv) | Nu | - | Obligatoriu daca rezultat != Acceptata | Nomenclator de motive |
| Comentariu triaj | rd_comentariutriaj | Text Area (2000) | Nu | - | Obligatoriu daca rezultat = Respinsa | - |
| Data triaj | rd_datatriaj | Date and Time | Nu | - | Se scrie automat la salvarea rezultatului | User Local |
| Amanata pana la | rd_amanatapanala | Date Only | Nu | > azi | Obligatoriu daca rezultat = Amanata | Reintra automat in coada |
| Proiect generat | rd_proiect | Lookup (rd_proiect) | Nu | - | Se completeaza de flux la acceptare | Referential |
| Status solicitare | rd_statussolicitare | Choice | Da | Ciorna / Trimisa / In triaj / Acceptata / Respinsa / Amanata | Implicit Ciorna | Choice local |

2.1.1 Regula de triaj: `rd_rezultattriaj` nu poate fi modificat decat de rolul Manager
R&D (ROL-02). O solicitare respinsa nu se sterge niciodata; ramane consultabila ca
istoric, conform 15.5.

2.1.2 O solicitare amanata reintra in lista de triaj automat la data din
`rd_amanatapanala`, prin fluxul FLX-14.

## 2.2 TBL-02 Proiect CDI

Nume: `rd_proiect`. Rol: radacina intregii solutii. Aproape toate celelalte tabele sunt
copii ai acestei tabele.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Cod proiect | rd_codproiect | Autonumber | Da | {AA}{SEQ:000}, exemplu 26025 | Se genereaza la acceptare, succesiv pe an | Coloana primara, imutabila |
| Nume produs | rd_numeprodus | Text (200) | Da | - | - | Intra in numele folderului |
| Denumire completa | rd_denumire | Calculated (Text) | Da | {rd_codproiect}_{rd_numeprodus} | Calculata | Folosita in denumirea fisierelor |
| Solicitare sursa | rd_solicitare | Lookup (rd_solicitare) | Nu | - | - | Referential |
| Proiect parinte | rd_proiectparinte | Lookup (rd_proiect) | Nu | - | Doar pentru versiuni cu sufix .1 | Auto-referential, vezi 2.2.2 |
| Sufix versiune | rd_sufixversiune | Text (10) | Nu | .1, .2, ... | Obligatoriu daca exista parinte | - |
| Tip proiect | rd_tipproiect | Choice | Da | Produs nou / Reformulare / Abatere / Transfer pe alta linie / Optimizare cost / Ambalaj nou | - | Choice global TIPPROIECT |
| Client | rd_client | Lookup (rd_client) | Da | - | Se preia din solicitare | - |
| KAM | rd_kam | Lookup (systemuser) | Da | - | Se preia din solicitare | - |
| Tehnolog alocat | rd_tehnolog | Lookup (systemuser) | Nu | - | Obligatoriu la trecerea in Acceptat - planificat | Vezi 2.20 |
| Manager R&D | rd_manager | Lookup (systemuser) | Da | - | Implicit managerul de departament | - |
| Linie de productie vizata | rd_linie | Lookup (rd_linie) | Nu | - | Obligatoriu la trecerea in In dezvoltare | Una din cele 9 |
| Amplasament | rd_amplasament | Choice | Da | Amplasament 1 / Amplasament 2 | Se preia din linie | Choice global AMPLASAMENT |
| Status | rd_status | Choice | Da | Vezi 4.6 / lista din 2.2.1 | Tranzitii controlate de business rule | Choice global STATUSPROIECT |
| Motiv status | rd_motivstatus | Lookup (rd_motiv) | Nu | - | Obligatoriu pentru Respins, Suspendat, Abandonat, Blocat | - |
| Gramaj (g) | rd_gramaj | Decimal (2) | Da | 1 - 20000 | Diferenta de gramaj = proiect nou | Vezi 2.2.3 |
| Dimensiuni | rd_dimensiuni | Text (100) | Nu | - | Diferenta de dimensiune = proiect nou | - |
| Tip ambalare | rd_tipambalare | Choice | Da | Choice AMBALARE | - | - |
| Volum estimat anual (kg) | rd_volumanual | Decimal (2) | Da | 0 - 10000000 | Intra in scor | - |
| Are materie prima noua | rd_aremp | Yes/No | Da | Implicit Nu | Se scrie de flux din liniile de MP | Conditioneaza livrabile |
| Numar MP noi | rd_numarmpnoi | Rollup (Count) | Nu | 0 - n | Numara rd_mpproiect cu rd_esteno = Da | Rollup |
| Termen propus | rd_termenpropus | Date Only | Nu | - | Generat de sistem la acceptare, FLX-03 | Nu se editeaza manual |
| Termen negociat | rd_termennegociat | Date Only | Nu | - | Rezultatul discutiei cu KAM | Termenul catre client |
| Termen realizat | rd_termenrealizat | Date Only | Nu | - | Se scrie la trecerea in Finalizat | - |
| Abatere fata de termen (zile) | rd_abateretermen | Whole Number | Nu | -999 - 999 | rd_termenrealizat - rd_termennegociat | Scris de flux |
| Data acceptare | rd_dataacceptare | Date Only | Nu | - | Se scrie la generarea codului | Start ceas |
| Durata standard (zile) | rd_duratastandard | Whole Number | Da | 1 - 365, implicit 14 | Din sablonul de etape | Vezi Sectiunea 14 |
| Zile blocate cumulat | rd_zileblocate | Rollup (Sum) | Nu | 0 - 999 | Suma impactului din rd_blocaj inchise | Vezi 2.11 |
| T-Total zile nete | rd_ttotalnet | Whole Number | Nu | - | (realizat - acceptare) - zile blocate | Scris de FLX-16 |
| Scor prioritate | rd_scorprioritate | Whole Number | Nu | 0 - 100 | Recalculat saptamanal, FLX-10 | Nu se editeaza manual |
| Banda prioritate | rd_banda | Choice | Nu | P1 / P2 / P3 / P4 | Derivata din scor, vezi 2.2.4 | Choice global BANDA |
| Scor suprascris | rd_scorsuprascris | Whole Number | Nu | 0 - 100 | Doar rol Manager operational vanzari | Audit obligatoriu |
| Motiv suprascriere | rd_motivsuprascriere | Text Area (1000) | Nu | - | Obligatoriu daca exista scor suprascris | Business rule |
| Data suprascrierii | rd_datasuprascriere | Date and Time | Nu | - | Automat | - |
| Zile in coada | rd_zilecoada | Whole Number | Nu | 0 - 999 | azi - data acceptare, cat timp nu e In dezvoltare | Alimenteaza imbatranirea |
| Referinta de comparatie | rd_referinta | Lookup (rd_referinta) | Nu | - | Obligatorie la deschidere | Vezi 2.13 |
| Cod material SAP produs finit | rd_codsapfinit | Text (20) | Nu | - | Se introduce dupa creare in SAP | Niciodata scriere in SAP |
| Data cod SAP | rd_datacodsap | Date Only | Nu | - | - | - |
| Slot testare propus | rd_slottestare | Date Only | Nu | - | Estimare negociabila, nu blocanta | Vezi 4.2 |
| Schimb propus | rd_schimb | Choice | Nu | 07-15 / 15-23 / 23-07 | - | Choice global SCHIMB |
| Folder SharePoint | rd_folderurl | Text (500) | Nu | URL | Scris de FLX-02 | - |
| Procent livrabile realizate | rd_procentlivrabile | Decimal (2) | Nu | 0 - 100 | Livrabile realizate / obligatorii aplicabile | Scris de FLX-05 |
| Toate livrabilele obligatorii OK | rd_livrabileok | Yes/No | Nu | - | Conditie pentru trecerea in Finalizat | Business rule |
| Data ultimei activitati | rd_ultimaactivitate | Date and Time | Nu | - | Scris la orice modificare de copil | Detecteaza proiecte uitate |

### 2.2.1 Statusurile proiectului

Lista finala, pornind de la propunerea din 4.6, cu doua completari argumentate:

| Nr | Status | Cine il seteaza | Conditie de intrare | Ceas T-Total |
|---|---|---|---|---|
| 1 | Solicitat | Sistem, la trimiterea SCP | SCP trimis | Nu porneste |
| 2 | In evaluare | Manager R&D | Triaj inceput | Nu porneste |
| 3 | Acceptat - planificat | Sistem la acceptare | Cod generat, tehnolog si termen propus | Porneste |
| 4 | In dezvoltare | Tehnolog | Linie stabilita, plan de dezvoltare aprobat | Curge |
| 5 | In asteptare materie prima | Sistem sau tehnolog | Exista MP noua fara receptie | Oprit |
| 6 | In testare | Tehnolog | Exista cel putin un trial deschis | Curge |
| 7 | Blocat | Manager R&D | Exista blocaj activ extern | Oprit |
| 8 | In implementare | Tehnolog | ST finala aprobata | Curge |
| 9 | Productie 0 | Tehnolog | Plan IPN aprobat | Curge |
| 10 | In revizuire | Sistem | La 30 de zile de la implementare | Nu conteaza |
| 11 | Finalizat | Manager R&D | Toate livrabilele obligatorii realizate | Se opreste definitiv |
| 12 | Respins | Manager R&D | Din triaj, cu motiv | Nu porneste |
| 13 | Suspendat | Manager R&D | Decizie interna, cu motiv si data de reluare | Oprit |
| 14 | Abandonat | Manager R&D | Cu motiv obligatoriu | Se opreste definitiv |

PROPUNERE: s-au adaugat statusurile "In revizuire" (10) si s-a separat "Suspendat" de
"Blocat". Motiv: revizuirea post-implementare din Sectiunea 8 are responsabil si termen
propriu si nu poate trai sub "Finalizat"; iar "Blocat" este cauzat extern si opreste
ceasul, in timp ce "Suspendat" este o decizie interna si trebuie sa se vada separat la
analiza anuala.

2.2.1.1 Fiecare status afiseaza intotdeauna, in formular si in vizualizare: data
planificata (`rd_termennegociat`), responsabilul (`rd_tehnolog`), urmatorul livrabil
scadent si cine il datoreaza. Ultimele doua se obtin din TBL-03 prin coloanele
`rd_urmatorullivrabil` si `rd_urmatorulresponsabil`, scrise de FLX-05.

### 2.2.2 Proiecte-copil

Relatia `rd_proiectparinte` este referentiala, nu parentala. Motiv: un proiect-copil are
ciclu de viata propriu si nu trebuie sters odata cu parintele. La crearea copilului,
FLX-04 copiaza: client, KAM, referinta de comparatie, linia, reteta curenta ca versiune
noua si legatura catre folderul parintelui. Documentele parintelui raman accesibile prin
lookup, nu se dubleaza fizic.

### 2.2.3 Regula "proiect nou, nu varianta"

Orice diferenta de gramaj, dimensiune sau reteta inseamna proiect nou. Se implementeaza
ca business rule pe formular: la modificarea `rd_gramaj`, `rd_dimensiuni` sau la crearea
unei versiuni de reteta cu alt set de ingrediente pe un proiect aflat in status >= 8, se
blocheaza salvarea si se propune butonul "Creeaza proiect-copil". Sufixul `.1` se
foloseste doar pentru abateri sau versiuni ale aceluiasi proiect.

### 2.2.4 Benzile de prioritate

| Banda | Scor | Semnificatie operationala |
|---|---|---|
| P1 | 80 - 100 | Se lucreaza acum, are slot rezervat |
| P2 | 60 - 79 | Se lucreaza in urmatoarele 2 saptamani |
| P3 | 35 - 59 | In coada, fara slot rezervat |
| P4 | 0 - 34 | Se lucreaza cand exista capacitate libera |

## 2.3 TBL-03 Livrabil de proiect

Nume: `rd_livrabil`. Rol: inlocuieste cele ~30 de coloane-bifa din centralizatorul actual.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire livrabil | rd_name | Text (150) | Da | - | Se preia din sablon | Coloana primara |
| Cod livrabil | rd_codlivrabil | Text (10) | Da | LIV-01 ... LIV-34 | Din sablon | Pentru raportare stabila |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascada la stergere |
| Sablon sursa | rd_sablon | Lookup (rd_sablonlivrabil) | Nu | - | - | Trasabilitate |
| Faza | rd_faza | Choice | Da | 00 Solicitare ... 08 Dosar validat | Din sablon | Choice global FAZA |
| Ordine in faza | rd_ordine | Whole Number | Da | 1 - 99 | Din sablon | Sortare |
| Responsabil rol | rd_rolresponsabil | Choice | Da | Choice global ROL | Din sablon | Cine datoreaza livrabilul |
| Responsabil persoana | rd_responsabil | Lookup (systemuser) | Nu | - | Se rezolva din rol la generare | Poate fi reatribuit |
| Obligatoriu | rd_obligatoriu | Yes/No | Da | - | Din sablon | Vezi 4.3 |
| Conditie de aplicabilitate | rd_conditie | Choice | Da | Intotdeauna / Doar MP noua / Doar eticheta noua / Doar client nou / Doar ambalaj nou / Doar linie nesetata / Doar export | Din sablon | Vezi 4.2 |
| Aplicabil | rd_aplicabil | Yes/No | Da | Implicit Da | Evaluat de FLX-05 la generare si la schimbarea conditiei | Livrabilele neaplicabile raman vizibile, gri |
| Termen | rd_termen | Date Only | Nu | - | Calculat din etapa si offset din sablon | Editabil de manager |
| Data realizarii | rd_datarealizare | Date Only | Nu | - | Se scrie la trecerea in Realizat | - |
| Status livrabil | rd_statuslivrabil | Choice | Da | Neinceput / In lucru / Trimis spre aprobare / Realizat / Respins / Nu se aplica | Implicit Neinceput | Choice global STATUSLIVRABIL |
| Document atasat | rd_document | Text (500) | Nu | URL SharePoint | Se completeaza la incarcarea fisierului | Vezi 2.3.1 |
| Necesita document | rd_necesitadocument | Yes/No | Da | Din sablon | Nu poate trece in Realizat fara document | Business rule |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | Din sablon (rol) | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Zile intarziere | rd_zileintarziere | Whole Number | Nu | 0 - 999 | max(0, azi - termen) daca nu e realizat | Scris de FLX-08 |
| Observatii | rd_observatii | Text Area (2000) | Nu | - | - | - |

2.3.1 Documentul nu se stocheaza in Dataverse. Coloana `rd_document` retine URL-ul
fisierului din biblioteca SharePoint a proiectului. Motiv: fisierele trebuie sa ramana in
SharePoint pentru versionare, co-editare si retentie, iar stocarea in Dataverse consuma
capacitate File scumpa si dubleaza sursa de adevar.

2.3.2 NOTA: livrabilele care "nu se aplica" nu se sterg si nu se ascund. Raman in lista
cu status `Nu se aplica`, pentru ca la audit trebuie demonstrat ca decizia de
neaplicabilitate a fost luata constient, nu ca livrabilul a fost omis.

## 2.4 TBL-04 Sablon de livrabil

Nume: `rd_sablonlivrabil`. Rol: sursa din care se genereaza TBL-03 la acceptarea
proiectului. Continutul complet este in Sectiunea 4 si in `data/sablon-livrabile.json`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | - | - | Coloana primara |
| Cod livrabil | rd_codlivrabil | Text (10) | Da | LIV-nn | Unic | - |
| Tip proiect aplicabil | rd_tipproiect | Choice (multi) | Da | Choice TIPPROIECT | Sablonul se filtreaza pe tipul proiectului | Multi-select |
| Faza | rd_faza | Choice | Da | Choice FAZA | - | - |
| Ordine | rd_ordine | Whole Number | Da | 1 - 99 | - | - |
| Etapa asociata | rd_etapa | Lookup (rd_sabloneteapa) | Nu | - | Din ea se ia termenul | - |
| Offset termen (zile) | rd_offsettermen | Whole Number | Da | 0 - 365 | Zile de la data de acceptare | - |
| Rol responsabil | rd_rolresponsabil | Choice | Da | Choice ROL | - | - |
| Rol aprobator | rd_rolaprobator | Choice | Nu | Choice ROL | - | - |
| Obligatoriu | rd_obligatoriu | Yes/No | Da | - | Vezi 4.3 | - |
| Necesita document | rd_necesitadocument | Yes/No | Da | - | - | - |
| Conditie de aplicabilitate | rd_conditie | Choice | Da | Ca in TBL-03 | - | - |
| Sablon Word | rd_sablonword | Text (300) | Nu | Nume fisier | Pentru generarea documentului | Vezi FLX-12 |
| Activ | rd_activ | Yes/No | Da | Implicit Da | Sablonul dezactivat nu mai genereaza | Istoricul ramane |

## 2.5 TBL-05 Etapa de proiect si TBL-06 Sablon de etapa

Nume: `rd_etapa`, `rd_sablonetapa`. Rol: masurarea duratelor reale pe etapa si baza
pentru T-Total.

### 2.5.1 rd_sablonetapa

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire etapa | rd_name | Text (100) | Da | - | - | Coloana primara |
| Cod etapa | rd_codetapa | Text (10) | Da | ETP-nn | Unic | - |
| Ordine | rd_ordine | Whole Number | Da | 1 - 20 | - | - |
| Tip proiect | rd_tipproiect | Choice (multi) | Da | Choice TIPPROIECT | - | - |
| Durata standard (zile lucratoare) | rd_duratastandard | Whole Number | Da | 1 - 90 | Vezi Sectiunea 14 | Setata o data la configurare |
| Durata propusa de sistem | rd_duratapropusa | Decimal (1) | Nu | - | Mediana duratelor reale, dupa 6-12 luni | Scrisa de FLX-17, nu se aplica automat |
| Rol responsabil | rd_rolresponsabil | Choice | Da | Choice ROL | - | - |
| Opreste ceasul la blocaj | rd_oprsteceasul | Yes/No | Da | Implicit Da | - | - |
| Activ | rd_activ | Yes/No | Da | - | - | - |

### 2.5.2 rd_etapa

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (100) | Da | - | Din sablon | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Sablon | rd_sablon | Lookup (rd_sablonetapa) | Nu | - | - | - |
| Ordine | rd_ordine | Whole Number | Da | 1 - 20 | - | - |
| Data start planificata | rd_startplanificat | Date Only | Da | - | Din offset | - |
| Data final planificata | rd_finalplanificat | Date Only | Da | - | Start + durata | - |
| Data start reala | rd_startreal | Date Only | Nu | - | La prima activitate pe etapa | - |
| Data final reala | rd_finalreal | Date Only | Nu | - | La inchiderea etapei | - |
| Durata reala bruta (zile) | rd_duratabruta | Whole Number | Nu | - | final real - start real | Scris de flux |
| Zile blocate pe etapa | rd_zileblocate | Rollup (Sum) | Nu | 0 - 999 | Din blocaje legate de etapa | - |
| Durata reala neta (zile) | rd_duratanet | Whole Number | Nu | - | bruta - blocate | Baza pentru T-Total |
| Abatere fata de standard | rd_abatere | Whole Number | Nu | -99 - 999 | neta - durata standard | Alimenteaza Sectiunea 14 |
| Status etapa | rd_statusetapa | Choice | Da | Neinceputa / In lucru / Blocata / Finalizata / Sarita | - | Choice global STATUSETAPA |
| Motiv sarire | rd_motivsarire | Text (300) | Nu | - | Obligatoriu daca status = Sarita | - |

## 2.6 TBL-07 Materie prima de proiect si TBL-08 Iteratie de furnizor

### 2.6.1 rd_mpproiect (Materie prima de proiect)

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Materie prima catalog | rd_materieprima | Lookup (rd_materieprima) | Nu | - | Gol daca este MP complet noua | - |
| Este noua | rd_estenoua | Yes/No | Da | Implicit Nu | Da declanseaza livrabilele conditionate | Scrie rd_aremp pe proiect |
| Categorie | rd_categorie | Choice | Da | Faina / Grasimi / Zaharuri / Lactate / Oua / Drojdie si afanatori / Amelioratori / Umpluturi / Fructe / Ciocolata / Arome / Aditivi / Ambalaje / Altele | - | Choice global CATEGORIEMP |
| Cantitate in reteta (kg/100kg) | rd_cantitate | Decimal (4) | Nu | 0 - 100 | - | Redundant cu linia de reteta, tinut pentru faza de plan |
| Furnizor propus | rd_furnizor | Lookup (rd_furnizor) | Nu | - | - | - |
| Status ciclu MP | rd_statusmp | Choice | Da | Identificata / Mostra ceruta / Mostra primita / In testare / Conditii ST emise / ST interna MP / Aprobata Calitate / Respinsa / Cod SAP creat / Comanda plasata / Receptionata | Vezi 4.4 | Choice global STATUSMP |
| Initiator cerere mostra | rd_initiator | Choice | Nu | R&D / Achizitii | - | Ambele pot initia |
| Tip lead time | rd_tipleadtime | Choice | Nu | Pe stoc / In portofoliu furnizor / Achizitie noua / Import sau caz special | Determina lead time implicit | Vezi 2.6.2 |
| Lead time asumat (zile) | rd_leadtime | Whole Number | Nu | 0 - 365 | Implicit din tip, editabil de Achizitii | - |
| ETA confirmat | rd_eta | Date Only | Nu | - | Se introduce doar de Achizitii | Modificarea declanseaza FLX-07 |
| ETA initial | rd_etainitial | Date Only | Nu | - | Primul ETA confirmat, nu se mai schimba | Masoara alunecarea |
| Numar modificari ETA | rd_modificarieta | Whole Number | Nu | 0 - 99 | Incrementat de flux | Indicator de furnizor |
| Data receptiei | rd_datareceptie | Date Only | Nu | - | - | - |
| Cod SAP MP | rd_codsapmp | Text (20) | Nu | - | Creat de Achizitii in SAP | Niciodata scriere in SAP |
| Numar iteratii | rd_numariteratii | Rollup (Count) | Nu | 0 - 99 | Din rd_iteratiefurnizor | - |
| Critica pentru proiect | rd_critica | Yes/No | Da | Implicit Da | Daca Da, intarzierea ei opreste proiectul | - |
| Observatii | rd_observatii | Text Area (2000) | Nu | - | - | - |

2.6.2 Lead time implicit pe tip, editabil de Achizitii: Pe stoc = 7 zile; In portofoliu
furnizor = 7 zile; Achizitie noua = 30 de zile; Import sau caz special = fara implicit,
data se declara explicit si campul `rd_eta` devine obligatoriu.

### 2.6.3 rd_iteratiefurnizor

Rol: pastreaza fiecare bucla de respingere / reluare, cu motiv. Fara aceasta tabela,
istoricul incercarilor cu furnizori se pierde.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {MP}_{Furnizor}_it{n} | Generata | Coloana primara |
| Materie prima de proiect | rd_mpproiect | Lookup (rd_mpproiect) | Da | - | Parental | - |
| Numar iteratie | rd_numar | Whole Number | Da | 1 - 99 | Succesiv pe MP | - |
| Furnizor | rd_furnizor | Lookup (rd_furnizor) | Da | - | - | - |
| Denumire comerciala oferta | rd_denumireoferta | Text (200) | Nu | - | - | Varianta furnizorului |
| Data cererii de mostra | rd_datacerere | Date Only | Nu | - | - | - |
| Data primirii mostrei | rd_dataprimire | Date Only | Nu | - | - | - |
| Rezultat | rd_rezultat | Choice | Da | In curs / Acceptata tehnic / Respinsa tehnic / Respinsa de Calitate / Respinsa pe cost / Retrasa de furnizor | - | Choice global REZULTATITERATIE |
| Motiv respingere | rd_motivrespingere | Lookup (rd_motiv) | Nu | - | Obligatoriu daca rezultat contine Respinsa | - |
| Detalii respingere | rd_detalii | Text Area (2000) | Nu | - | - | - |
| Pret oferit | rd_pret | Currency (4) | Nu | - | - | - |
| Data deciziei | rd_datadecizie | Date Only | Nu | - | - | - |

## 2.7 TBL-09 Materie prima (catalog) si TBL-10 Furnizor

### 2.7.1 rd_materieprima

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Cod SAP | rd_codsap | Text (20) | Nu | - | Unic daca exista | Import din SAP, read-only |
| Categorie | rd_categorie | Choice | Da | Choice CATEGORIEMP | - | - |
| Furnizor principal | rd_furnizor | Lookup (rd_furnizor) | Nu | - | - | - |
| Unitate de masura | rd_um | Choice | Da | kg / g / l / ml / buc | - | Choice global UM |
| Pret curent | rd_pret | Currency (4) | Nu | - | Actualizat manual sau prin import | Alimenteaza antecalculul |
| Data pretului | rd_datapret | Date Only | Nu | - | - | Semnaleaza preturi vechi |
| Alergeni continuti | rd_alergeni | Choice (multi) | Da | Cei 14 alergeni din Anexa II Reg. 1169/2011 | - | Vezi Sectiunea 9 |
| Alergeni pe urme | rd_alergeniurme | Choice (multi) | Nu | Idem | Din declaratia furnizorului | Vezi 9.4 |
| Energie (kcal/100g) | rd_energie | Decimal (2) | Nu | 0 - 900 | Din ST furnizor | - |
| Grasimi (g/100g) | rd_grasimi | Decimal (2) | Nu | 0 - 100 | - | - |
| din care acizi grasi saturati | rd_saturate | Decimal (2) | Nu | 0 - 100 | <= rd_grasimi | - |
| Glucide (g/100g) | rd_glucide | Decimal (2) | Nu | 0 - 100 | - | - |
| din care zaharuri | rd_zaharuri | Decimal (2) | Nu | 0 - 100 | <= rd_glucide | - |
| Fibre (g/100g) | rd_fibre | Decimal (2) | Nu | 0 - 100 | - | - |
| Proteine (g/100g) | rd_proteine | Decimal (2) | Nu | 0 - 100 | - | - |
| Sare (g/100g) | rd_sare | Decimal (4) | Nu | 0 - 100 | - | - |
| Umiditate (%) | rd_umiditate | Decimal (2) | Nu | 0 - 100 | Necesara pentru randament | - |
| Suma macronutrienti | rd_summacro | Calculated (Decimal) | Nu | 0 - 105 | grasimi + glucide + fibre + proteine + sare + umiditate | Validare de plauzibilitate |
| Data ultimei ST furnizor | rd_datast | Date Only | Nu | - | ST mai veche de 24 de luni se semnaleaza | Cerinta IFS |
| Status | rd_statusmp | Choice | Da | Activa / In evaluare / Blocata / Iesita din uz | - | - |
| Bio / ecologic | rd_bio | Yes/No | Nu | - | - | - |
| Origine | rd_origine | Text (100) | Nu | - | Pentru declaratii de origine | - |

### 2.7.2 rd_furnizor

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Cod SAP furnizor | rd_codsap | Text (20) | Nu | - | - | Import |
| Tip | rd_tipfurnizor | Choice | Da | Producator / Distribuitor / Broker / Intern | - | - |
| Aprobat Calitate | rd_aprobat | Yes/No | Da | Implicit Nu | Nu se comanda de la furnizor neaprobat | Cerinta IFS |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Certificari | rd_certificari | Choice (multi) | Nu | IFS / BRC / FSSC 22000 / ISO 22000 / Bio / Halal / Kosher | - | - |
| Expirare certificare | rd_expirarecertificare | Date Only | Nu | - | Alerta cu 60 de zile inainte | - |
| Persoana de contact | rd_contact | Text (150) | Nu | - | - | - |
| Email contact | rd_email | Text (150) | Nu | Format email | - | - |
| Lead time mediu real (zile) | rd_leadtimemediu | Decimal (1) | Nu | - | Calculat din iteratii incheiate | Indicator de furnizor |
| Rata de respingere (%) | rd_ratarespingere | Decimal (2) | Nu | 0 - 100 | Iteratii respinse / total | Scris de flux |

## 2.8 TBL-11 Blocaj

Nume: `rd_blocaj`. Rol: sursa principala de explicatie a intarzierilor la analiza anuala.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | - | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Etapa afectata | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | Pentru durata neta pe etapa |
| Cine blocheaza | rd_sursablocaj | Choice | Da | Furnizor / Client / Calitate / Planificare / Productie / Achizitii / Intern R&D / Extern reglementar | - | Choice global SURSABLOCAJ |
| Categorie blocaj | rd_categorie | Choice | Da | Asteptare mostra / Asteptare decizie / Asteptare aprobare / Indisponibilitate linie / Indisponibilitate MP / Lipsa specificatie / Lipsa ambalaj / Altul | - | - |
| Data start | rd_datastart | Date Only | Da | <= azi | - | - |
| Data sfarsit | rd_datasfarsit | Date Only | Nu | >= data start | Gol = blocaj activ | - |
| Impact in zile | rd_impactzile | Whole Number | Nu | 0 - 999 | Zile lucratoare intre start si sfarsit | Scris de FLX-09 |
| Opreste ceasul R&D | rd_oprsteceas | Yes/No | Da | Implicit Da pentru surse externe | Intern R&D = Nu | Vezi 2.8.1 |
| Termen client afectat | rd_afecteazaclient | Yes/No | Da | Implicit Da | Termenul catre client curge oricum | Vezi 4.5 |
| Descriere | rd_descriere | Text Area (2000) | Da | - | - | - |
| Actiune de deblocare | rd_actiune | Text Area (2000) | Nu | - | - | - |
| Responsabil deblocare | rd_responsabil | Lookup (systemuser) | Nu | - | - | - |
| Activ | rd_activ | Calculated (Yes/No) | Nu | - | Da daca rd_datasfarsit este gol | - |

2.8.1 Regula de oprire a ceasului: cat timp exista cel putin un blocaj activ cu
`rd_oprsteceas = Da`, ceasul indicatorului T-Total al R&D se opreste. Termenul catre
client (`rd_termennegociat`) continua sa curga si se raporteaza separat. Blocajele cu
sursa "Intern R&D" nu opresc ceasul niciodata - altfel indicatorul devine
nefalsificabil.

## 2.9 TBL-12 Cerere de mostra si TBL-13 Miscare de mostra

### 2.9.1 rd_ceremostra

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar cerere | rd_name | Autonumber | Da | CM-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Tip mostra | rd_tipmostra | Choice | Da | Materie prima / Produs finit intern / Produs concurenta / Mostra client / Ambalaj | - | Choice global TIPMOSTRA |
| Materie prima de proiect | rd_mpproiect | Lookup (rd_mpproiect) | Nu | - | Obligatoriu daca tip = Materie prima | - |
| Solicitant | rd_solicitant | Lookup (systemuser) | Da | - | - | - |
| Rol solicitant | rd_rolsolicitant | Choice | Da | R&D / Achizitii | Ambele pot initia | - |
| Destinatar | rd_destinatar | Choice | Da | Intern laborator / Client / Furnizor / Panel senzorial | - | - |
| Cantitate ceruta | rd_cantitate | Decimal (2) | Da | > 0 | - | - |
| Unitate de masura | rd_um | Choice | Da | Choice UM | - | - |
| Data ceruta | rd_dataceruta | Date Only | Da | >= azi | - | - |
| Status cerere | rd_statuscerere | Choice | Da | Ciorna / Trimisa / Confirmata / In transport / Livrata / Anulata | - | - |
| Data livrarii | rd_datalivrare | Date Only | Nu | - | - | - |
| Adresa de livrare | rd_adresa | Text Area (500) | Nu | - | Obligatorie daca destinatar = Client | - |
| Curier si AWB | rd_awb | Text (100) | Nu | - | - | - |
| Observatii | rd_observatii | Text Area (2000) | Nu | - | - | - |

### 2.9.2 rd_miscaremostra

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Generata | - | Coloana primara |
| Cerere de mostra | rd_ceremostra | Lookup (rd_ceremostra) | Da | - | Parental | - |
| Tip miscare | rd_tipmiscare | Choice | Da | Pregatita / Predata la transport / Expediata / Receptionata / Returnata / Distrusa | - | - |
| Data si ora | rd_datamiscare | Date and Time | Da | - | Implicit acum | User Local |
| Persoana | rd_persoana | Lookup (systemuser) | Da | - | Implicit utilizator curent | - |
| Cantitate | rd_cantitate | Decimal (2) | Nu | > 0 | - | - |
| Temperatura la receptie (C) | rd_temperatura | Decimal (1) | Nu | -40 - 40 | Obligatorie la receptie de congelat | Cerinta HACCP |
| Conform | rd_conform | Yes/No | Nu | - | Obligatoriu la receptie | - |
| Motiv neconformitate | rd_motiv | Text (300) | Nu | - | Obligatoriu daca conform = Nu | - |
| Poza | rd_poza | Image | Nu | - | Din canvas mobil | Vezi ECR-13 |

## 2.10 TBL-14 Fisa de testare, TBL-15 Trial, TBL-16 Masuratoare

### 2.10.1 rd_fisatestare

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar fisa | rd_name | Autonumber | Da | FT-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Obiectivul testarii | rd_obiectiv | Text Area (2000) | Da | - | - | - |
| Versiune reteta testata | rd_versiunereteta | Lookup (rd_versiunereteta) | Da | - | - | - |
| Linie | rd_linie | Lookup (rd_linie) | Nu | - | - | - |
| Data planificata | rd_dataplanificata | Date Only | Da | - | - | - |
| Parametri de proces tinta | rd_parametritinta | Text Area (4000) | Nu | - | - | Preluati in trial |
| Tolerante declarate | rd_tolerante | Text Area (2000) | Da | - | Baza pentru conformitatea masuratorilor | Vezi 6.3 |
| Status fisa | rd_statusfisa | Choice | Da | Ciorna / Aprobata / In executie / Finalizata / Anulata | - | - |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | - | - |
| Concluzie | rd_concluzie | Text Area (4000) | Nu | - | Obligatorie la Finalizata | - |

### 2.10.2 rd_trial

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar trial | rd_name | Autonumber | Da | TR-{AA}-{SEQ:0000} | - | Coloana primara |
| Fisa de testare | rd_fisatestare | Lookup (rd_fisatestare) | Da | - | Parental | - |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Denormalizat pentru raportare | Scris de flux |
| Numar incercare | rd_numarincercare | Whole Number | Da | 1 - 99 | Succesiv pe fisa | - |
| Data si ora start | rd_start | Date and Time | Da | - | - | User Local |
| Data si ora final | rd_final | Date and Time | Nu | - | - | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | - | - |
| Schimb | rd_schimb | Choice | Da | Choice SCHIMB | - | - |
| Operator | rd_operator | Text (150) | Nu | - | Nu toti operatorii au cont | Text, nu lookup |
| Cantitate aluat (kg) | rd_cantitatealuat | Decimal (2) | Nu | > 0 | - | - |
| Bucati obtinute | rd_bucatiobtinute | Whole Number | Nu | >= 0 | - | - |
| Randament (%) | rd_randament | Decimal (2) | Nu | 0 - 120 | (bucati x gramaj) / (aluat x 1000) x 100 | Vezi 7.2 |
| Temperatura aluat (C) | rd_tempaluat | Decimal (1) | Nu | 0 - 40 | - | Parametru critic la laminare |
| Timp framantare (min) | rd_timpframantare | Decimal (1) | Nu | 0 - 120 | - | - |
| Timp fermentare (min) | rd_timpfermentare | Decimal (1) | Nu | 0 - 600 | - | - |
| Grosime laminare (mm) | rd_grosimelaminare | Decimal (2) | Nu | 0 - 100 | - | Fritsch / Rademaker |
| Timp dospire (min) | rd_timpdospire | Decimal (1) | Nu | 0 - 600 | - | - |
| Temperatura dospire (C) | rd_tempdospire | Decimal (1) | Nu | 0 - 60 | - | - |
| Temperatura coacere (C) | rd_tempcoacere | Decimal (1) | Nu | 0 - 350 | - | WP tunel |
| Timp coacere (min) | rd_timpcoacere | Decimal (1) | Nu | 0 - 120 | - | - |
| Temperatura congelare (C) | rd_tempcongelare | Decimal (1) | Nu | -45 - 0 | - | JBT shockfreezer |
| Timp congelare (min) | rd_timpcongelare | Decimal (1) | Nu | 0 - 300 | - | - |
| Temperatura in centru la iesire (C) | rd_tempcentru | Decimal (1) | Nu | -40 - 20 | Punct critic HACCP | Vezi 7.5 |
| Rezultat trial | rd_rezultat | Choice | Da | In curs / Reusit / Reusit cu observatii / Nereusit | - | Choice global REZULTATTRIAL |
| Observatii | rd_observatii | Text Area (4000) | Nu | - | Obligatorii daca rezultat = Nereusit | - |
| Numar masuratori | rd_numarmasuratori | Rollup (Count) | Nu | - | - | - |

### 2.10.3 rd_masuratoare

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Generata | - | Coloana primara |
| Trial | rd_trial | Lookup (rd_trial) | Da | - | Parental | - |
| Tip masuratoare | rd_tipmasuratoare | Choice | Da | Greutate / Lungime / Latime / Inaltime / Diametru / Grosime / Volum / Aspect / Alveolare / Miros / Gust / Culoare / Umiditate / Aw / pH / Temperatura | - | Choice global TIPMASURATOARE |
| Numar bucata | rd_numarbucata | Whole Number | Da | 1 - 50 | Succesiv in cadrul tipului | - |
| Valoare numerica | rd_valoare | Decimal (3) | Nu | - | Obligatorie pentru tipuri numerice | - |
| Valoare calitativa | rd_valoarecalitativa | Choice | Nu | Conform / Minor neconform / Neconform | Obligatorie pentru aspect, miros, gust, alveolare | - |
| Unitate de masura | rd_um | Choice | Da | g / mm / ml / C / % / scor | Implicit din tip | - |
| Valoare tinta | rd_tinta | Decimal (3) | Nu | - | Din fisa de testare | - |
| Toleranta minus | rd_tolminus | Decimal (3) | Nu | - | Din fisa de testare | - |
| Toleranta plus | rd_tolplus | Decimal (3) | Nu | - | Din fisa de testare | - |
| Conform | rd_conform | Calculated (Yes/No) | Nu | - | valoare intre tinta-tolminus si tinta+tolplus | Vezi 6.3 |
| Data si ora | rd_datamasurare | Date and Time | Da | Implicit acum | - | User Local |
| Masurat de | rd_masuratde | Lookup (systemuser) | Da | Implicit utilizator curent | - | - |
| Poza | rd_poza | Image | Nu | - | Din canvas mobil | Comprimata la 1024px |
| Exclus din statistica | rd_exclus | Yes/No | Da | Implicit Nu | Doar cu motiv, vezi 6.2.4 | - |
| Motiv excludere | rd_motivexcludere | Text (300) | Nu | - | Obligatoriu daca exclus = Da | - |
| Observatii | rd_observatii | Text (500) | Nu | - | - | - |

### 2.10.4 rd_statisticatrial (sinteza pe tip de masuratoare)

PROPUNERE: tabela separata de sinteza, scrisa de FLX-11 dupa fiecare salvare de
masuratoare. Motiv: Rollup-ul Dataverse calculeaza numai Sum, Count, Min, Max - nu
calculeaza abatere standard, deci sinteza ceruta in 6.1 nu poate trai in coloane de
proiect.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {Trial}_{Tip} | - | Coloana primara |
| Trial | rd_trial | Lookup (rd_trial) | Da | - | Parental | - |
| Tip masuratoare | rd_tipmasuratoare | Choice | Da | Choice TIPMASURATOARE | Unic pe trial | - |
| Numar valori | rd_n | Whole Number | Da | 1 - 50 | Fara cele excluse | - |
| Media | rd_medie | Decimal (3) | Da | - | - | - |
| Abatere standard | rd_abaterestandard | Decimal (4) | Nu | >= 0 | Esantion, n-1 | - |
| Coeficient de variatie (%) | rd_cv | Decimal (2) | Nu | 0 - 100 | abatere / medie x 100 | Vezi 6.2.3 |
| Minim | rd_minim | Decimal (3) | Da | - | - | - |
| Maxim | rd_maxim | Decimal (3) | Da | - | - | - |
| Numar neconforme | rd_neconforme | Whole Number | Da | 0 - 50 | - | - |
| Conformitate lot (%) | rd_conformitate | Decimal (2) | Da | 0 - 100 | conforme / n x 100 | - |
| Verdict | rd_verdict | Choice | Da | Conform / Conform cu observatii / Neconform / Esantion insuficient | Vezi 6.2 | - |

## 2.11 TBL-17 Evaluare senzoriala, TBL-18 Criteriu, TBL-19 Scor, TBL-20 Defect

### 2.11.1 rd_evaluaresenzoriala

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar evaluare | rd_name | Autonumber | Da | ES-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Trial evaluat | rd_trial | Lookup (rd_trial) | Nu | - | Referential | - |
| Tip evaluare | rd_tipevaluare | Choice | Da | Interna R&D / Panel extins / Cu clientul / Comparativa cu referinta / Shelf life | - | - |
| Data | rd_data | Date Only | Da | - | - | - |
| Numar evaluatori | rd_numarevaluatori | Rollup (Count) | Nu | 1 - 20 | Distinct pe rd_scor | Vezi 6.5.3 |
| Referinta comparata | rd_referinta | Lookup (rd_referinta) | Nu | - | Obligatorie daca tip = Comparativa | - |
| Scor total ponderat | rd_scortotal | Decimal (2) | Nu | 1 - 5 | Media ponderata a scorurilor | Scris de FLX-11 |
| Scor referinta | rd_scorreferinta | Decimal (2) | Nu | 1 - 5 | Idem, pe referinta | - |
| Diferenta fata de referinta | rd_diferenta | Decimal (2) | Nu | -4 - 4 | scor total - scor referinta | - |
| Dezacord maxim | rd_dezacord | Decimal (2) | Nu | 0 - 4 | Amplitudinea maxima pe un criteriu | Vezi 6.5.4 |
| Verdict | rd_verdict | Choice | Da | Acceptat / Acceptat cu observatii / Respins | Vezi 6.5.5 | Choice global VERDICT |
| Actiuni cerute | rd_actiuni | Text Area (4000) | Nu | - | Obligatorii daca verdict != Acceptat | - |
| Conditii de degustare | rd_conditii | Text Area (1000) | Nu | - | Temperatura, timp de la coacere | Cerinta de repetabilitate |

### 2.11.2 rd_criteriusenzorial (nomenclator)

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire criteriu | rd_name | Text (100) | Da | - | - | Coloana primara |
| Cod | rd_cod | Text (10) | Da | CR-nn | Unic | - |
| Grupa | rd_grupa | Choice | Da | Aspect exterior / Structura interna / Textura / Aroma si gust / Comportament la utilizare | - | - |
| Pondere (%) | rd_pondere | Decimal (2) | Da | 0 - 100 | Suma pe categoria de produs = 100 | Vezi 6.5.1 |
| Categorie produs | rd_categorieprodus | Choice | Da | Foietaj / Aluat dospit / Patiserie cu umplutura / Paine / Produs gata copt / Produs bake-off | Grile diferite pe categorie | - |
| Ancora scor 1 | rd_ancora1 | Text (300) | Da | - | Descriere, nu cifra | Vezi 6.5.2 |
| Ancora scor 3 | rd_ancora3 | Text (300) | Da | - | - | - |
| Ancora scor 5 | rd_ancora5 | Text (300) | Da | - | - | - |
| Eliminatoriu sub | rd_eliminatoriusub | Whole Number | Nu | 1 - 5 | Scor sub prag = respins automat | Vezi 6.5.5 |
| Activ | rd_activ | Yes/No | Da | - | - | - |

### 2.11.3 rd_scorsenzorial

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Generata | - | Coloana primara |
| Evaluare | rd_evaluare | Lookup (rd_evaluaresenzoriala) | Da | - | Parental | - |
| Criteriu | rd_criteriu | Lookup (rd_criteriusenzorial) | Da | - | - | - |
| Evaluator | rd_evaluator | Lookup (systemuser) | Da | - | Unic impreuna cu criteriu si tinta | - |
| Tinta scorului | rd_tintascor | Choice | Da | Produs dezvoltat / Referinta | Permite comparatia pe acelasi ecran | - |
| Scor | rd_scor | Whole Number | Da | 1 - 5 | - | - |
| Comentariu | rd_comentariu | Text (500) | Nu | - | Obligatoriu daca scor <= 2 | Business rule |

### 2.11.4 rd_defect (nomenclator) si rd_defectconstatat

`rd_defect`: Denumire (Text, primara), Cod (Text, DF-nn), Grupa (Choice: Aluat /
Laminare / Dospire / Coacere / Congelare / Ambalare / Materie prima), Descriere (Text
Area), Severitate implicita (Choice: Minor / Major / Critic), Cauza probabila (Text
Area), Activ (Yes/No).

`rd_defectconstatat`: Evaluare (Lookup, parental), Defect (Lookup), Severitate (Choice),
Numar bucati afectate (Whole Number), Procent afectat (Decimal 2), Poza (Image),
Observatii (Text Area).

## 2.12 TBL-21 Referinta de comparatie

Nume: `rd_referinta`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascada la stergere |
| Tip referinta | rd_tipreferinta | Choice | Da | Produs concurenta / Produs actual / Mostra client / Specificatie client / Inexistenta | - | Choice global TIPREFERINTA |
| Client asociat | rd_client | Lookup (rd_client) | Nu | - | - | - |
| Producator | rd_producator | Text (150) | Nu | - | Pentru produs concurenta | - |
| Cod produs actual | rd_codprodusactual | Text (20) | Nu | - | Cod SAP daca este produs propriu | - |
| Gramaj (g) | rd_gramaj | Decimal (2) | Nu | - | Gramajul nominal, de pe eticheta | - |
| Gramaj masurat real (g) | rd_gramajmasurat | Decimal (2) | Nu | - | Minimum 5 bucati la produs concurenta | Vezi 6.4.4 |
| Pret raft | rd_pretraft | Currency (2) | Nu | - | Pentru pozitionare | - |
| Data achizitiei referintei | rd_dataachizitie | Date Only | Nu | - | - | - |
| Lista de ingrediente | rd_ingrediente | Text Area (4000) | Nu | - | De pe eticheta | - |
| Valori nutritionale declarate | rd_nutritionale | Text Area (2000) | Nu | - | - | - |
| Poza | rd_poza | Image | Nu | - | - | - |
| Documente | rd_documenteurl | Text (500) | Nu | - | Folder in 00_Solicitare | - |

## 2.13 TBL-22 Antecalcul si TBL-23 Linie de antecalcul

### 2.13.1 rd_antecalcul

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar antecalcul | rd_name | Autonumber | Da | AC-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Versiune reteta | rd_versiunereteta | Lookup (rd_versiunereteta) | Da | - | - | - |
| Versiune antecalcul | rd_versiune | Whole Number | Da | 1 - 99 | Succesiv pe proiect | - |
| Data calculului | rd_datacalcul | Date Only | Da | - | - | - |
| Linie de productie | rd_linie | Lookup (rd_linie) | Da | - | Determina tariful si viteza | - |
| Gramaj (g) | rd_gramaj | Decimal (2) | Da | - | Din proiect | - |
| Cost materii prime / kg | rd_costmp | Currency (4) | Nu | - | Suma liniilor de antecalcul | Rollup |
| Pierdere tehnologica (%) | rd_pierdere | Decimal (2) | Da | 0 - 30, implicit 3 | Din date de linie | - |
| Cost MP ajustat / kg | rd_costmpajustat | Decimal (4) | Nu | - | cost MP / (1 - pierdere/100) | - |
| Cost ambalaj / buc | rd_costambalaj | Currency (4) | Nu | - | - | - |
| Cost manopera / kg | rd_costmanopera | Currency (4) | Nu | - | Tarif linie x timp / cantitate | - |
| Cost energie si utilitati / kg | rd_costenergie | Currency (4) | Nu | - | Din tariful liniei | Congelarea este semnificativa |
| Cost congelare / kg | rd_costcongelare | Currency (4) | Nu | - | Separat, pentru comparabilitate | PROPUNERE |
| Regie / kg | rd_regie | Currency (4) | Nu | - | Procent din costul direct | - |
| Cost total / kg | rd_costtotal | Currency (4) | Nu | - | Suma componentelor | - |
| Cost total / buc | rd_costbuc | Currency (4) | Nu | - | cost/kg x gramaj / 1000 + ambalaj | - |
| Pret tinta client | rd_prettinta | Currency (4) | Nu | - | Din solicitare sau negociere | - |
| Marja bruta (%) | rd_marja | Decimal (2) | Nu | -100 - 100 | (pret - cost) / pret x 100 | - |
| Status | rd_statusantecalcul | Choice | Da | Ciorna / Trimis spre aprobare / Aprobat / Respins / Inlocuit | - | - |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | - | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Cost real la revizuire | rd_costreal | Currency (4) | Nu | - | Din Sectiunea 8 | Compara antecalcul cu realitate |

### 2.13.2 rd_linieantecalcul

Coloane: Antecalcul (Lookup, parental), Materie prima (Lookup rd_materieprima), Materie
prima de proiect (Lookup, pentru MP fara cod), Cantitate kg/100kg (Decimal 4), Pret
unitar (Currency 4), Cost linie (Calculated Currency = cantitate x pret / 100), Sursa
pretului (Choice: Catalog / Oferta furnizor / Estimare), Data pretului (Date Only),
Observatii (Text 500).

## 2.14 TBL-24 Reteta, TBL-25 Versiune de reteta, TBL-26 Linie de reteta

### 2.14.1 rd_reteta (antet)

Coloane: Denumire (Text 200, primara), Proiect (Lookup, parental), Cod reteta (Text 20),
Categorie produs (Choice), Versiune curenta (Lookup rd_versiunereteta, referential),
Status (Choice: In dezvoltare / Validata / Inlocuita / Retrasa), Observatii (Text Area).

### 2.14.2 rd_versiunereteta

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | {Reteta} v{n} | Generata | Coloana primara |
| Reteta | rd_reteta | Lookup (rd_reteta) | Da | - | Parental | - |
| Numar versiune | rd_numarversiune | Whole Number | Da | 1 - 99 | Succesiv | - |
| Data versiunii | rd_dataversiune | Date Only | Da | - | - | - |
| Autor | rd_autor | Lookup (systemuser) | Da | - | - | - |
| Motivul modificarii | rd_motivmodificare | Text Area (1000) | Da | - | Obligatoriu de la versiunea 2 | Cerinta IFS |
| Total cantitate (kg/100kg) | rd_total | Rollup (Sum) | Nu | - | Suma liniilor, trebuie sa fie 100 | Validare |
| Blocata | rd_blocata | Yes/No | Da | Implicit Nu | Versiunea validata nu se mai editeaza | Vezi 2.14.4 |
| Status | rd_statusversiune | Choice | Da | Ciorna / In testare / Validata / Inlocuita | - | - |
| Energie (kcal/100g) | rd_energie | Decimal (2) | Nu | - | Calculat, vezi Sectiunea 9 | Scris de FLX-13 |
| Grasimi | rd_grasimi | Decimal (2) | Nu | - | Idem | - |
| Saturate | rd_saturate | Decimal (2) | Nu | - | Idem | - |
| Glucide | rd_glucide | Decimal (2) | Nu | - | Idem | - |
| Zaharuri | rd_zaharuri | Decimal (2) | Nu | - | Idem | - |
| Fibre | rd_fibre | Decimal (2) | Nu | - | Idem | - |
| Proteine | rd_proteine | Decimal (2) | Nu | - | Idem | - |
| Sare | rd_sare | Decimal (4) | Nu | - | Idem | - |
| Alergeni continuti | rd_alergeni | Choice (multi) | Nu | - | Reuniunea alergenilor din linii | Scris de FLX-13 |
| Alergeni pe urme | rd_alergeniurme | Choice (multi) | Nu | - | Vezi 9.4 | - |
| Data ultimului calcul | rd_datacalcul | Date and Time | Nu | - | - | Semnaleaza calcule invechite |

### 2.14.3 rd_liniereteta

Coloane: Versiune reteta (Lookup, parental), Materie prima (Lookup rd_materieprima),
Materie prima de proiect (Lookup rd_mpproiect, pentru MP inca fara cod), Faza de retetare
(Choice: Aluat de baza / Grasime de laminare / Umplutura / Decor / Glazura / Presarare),
Cantitate kg/100kg (Decimal 4), Ordine (Whole Number), Procent din total (Calculated
Decimal), Pierdere la proces (%) (Decimal 2), Observatii (Text 500).

2.14.4 Regula de blocare: la trecerea versiunii in `Validata`, `rd_blocata` devine Da si
toate liniile devin read-only prin business rule si prin rol de securitate (drept Write
retras pe status validat). O modificare ulterioara obliga la versiune noua cu motiv.
Motiv: reconstituirea dosarului de produs la orice data din trecut, cerinta IFS.

## 2.15 TBL-27 Alergen si TBL-28 Valoare nutritionala

`rd_alergen` (nomenclator fix, 14 pozitii): Denumire (Text, primara), Cod (Text: GLU,
CRU, OUA, PES, ARA, SOI, LAP, FRC, TEL, MUS, SUS, SO2, LUP, MOL), Denumire legala pe
eticheta (Text 150), Grupa (Choice: Cereale cu gluten / Fructe cu coaja / Altele),
Necesita evidentiere pe eticheta (Yes/No, implicit Da), Prag de declarare (Text 100),
Observatii.

`rd_valoarenutritionala` este modelata ca set de coloane pe `rd_versiunereteta`
(2.14.2), nu ca tabela separata. Motiv: valorile sunt intotdeauna exact 8, fixe prin
Reg. 1169/2011, si o tabela separata ar adauga un join fara nicio flexibilitate reala.
NOTA: daca in viitor se cer si micronutrienti sau declaratii voluntare, se adauga tabela
`rd_nutrientsuplimentar` cu Lookup catre versiune.

## 2.16 TBL-29 Specificatie tehnica si TBL-30 SDP

### 2.16.1 rd_specificatie

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar specificatie | rd_name | Autonumber | Da | ST-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Nu | - | Gol pentru ST de MP din catalog | Referential |
| Tip specificatie | rd_tipspecificatie | Choice | Da | Conditii ST / ST draft / ST finala / ST interna MP noua | - | Choice global TIPST |
| Materie prima | rd_materieprima | Lookup (rd_materieprima) | Nu | - | Obligatorie daca tip = ST interna MP | - |
| Versiune | rd_versiune | Text (10) | Da | v01, v02 | - | - |
| Status | rd_statusst | Choice | Da | Ciorna / In aprobare / Aprobata / Inlocuita / Retrasa | - | - |
| Autor | rd_autor | Lookup (systemuser) | Da | - | - | - |
| Aprobator Calitate | rd_aprobatorcalitate | Lookup (systemuser) | Nu | - | Obligatoriu pentru Aprobata | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Valabila de la | rd_valabiladela | Date Only | Nu | - | - | - |
| Document | rd_documenturl | Text (500) | Nu | - | Fisier in 05_Specificatii | Formatul intern al ST nu face obiectul acestui blueprint |
| Inlocuieste | rd_inlocuieste | Lookup (rd_specificatie) | Nu | - | Auto-referential | Lant de versiuni |

### 2.16.2 rd_sdp (Specificatie de produs)

Coloane: Numar SDP (Autonumber SDP-{AA}-{SEQ:0000}, primara), Proiect (Lookup,
parental), Versiune reteta (Lookup), Versiune (Text 10), Status (Choice: Ciorna / In
aprobare / Aprobata / Inlocuita), Linie (Lookup), Parametri de proces (Text Area 8000,
preluati din trialul validat), Puncte critice HACCP (Text Area 4000), Ambalare si
etichetare (Text Area 4000), Conditii de depozitare (Text 300), Termen de valabilitate
(Whole Number, luni), Conditii de decongelare si coacere la client (Text Area 2000),
Aprobator R&D (Lookup), Aprobator Calitate (Lookup), Data aprobarii (Date Only), Document
(Text 500).

## 2.17 TBL-31 Eticheta

Nume: `rd_eticheta`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | - | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | - |
| Tip eticheta | rd_tipeticheta | Choice | Da | Punga / Bax / EPC eticheta produs client / Fisier imprimanta | - | Choice global TIPETICHETA |
| Format fisier imprimanta | rd_formatimprimanta | Choice | Nu | Colos / Zebra ZPL / Altul | Obligatoriu daca tip = Fisier imprimanta | - |
| Versiune | rd_versiune | Text (10) | Da | v01 | - | - |
| Status | rd_statuseticheta | Choice | Da | De realizat / In lucru / Trimisa spre aprobare / Aprobata / Implementata / Inlocuita | Vezi livrabilele ETICHETA REALIZATA si ETICHETA IMPLEMENTATA | - |
| Limba | rd_limba | Choice (multi) | Da | RO / EN / HU / BG / DE / FR / IT | - | - |
| Denumire legala produs | rd_denumirelegala | Text (300) | Da | - | Preluata din SDP | - |
| Lista de ingrediente | rd_ingrediente | Text Area (8000) | Nu | - | Generata din reteta, ordine descrescatoare | Vezi 9.5 |
| Declaratie alergeni | rd_declaratiealergeni | Text Area (2000) | Nu | - | Generata, alergenii evidentiati | Vezi 9.3 |
| Declaratie urme | rd_declaratieurme | Text (500) | Nu | - | Vezi 9.4 | - |
| Tabel nutritional | rd_tabelnutritional | Text Area (2000) | Nu | - | Generat din versiunea de reteta | - |
| Gramaj declarat | rd_gramajdeclarat | Text (50) | Da | - | - | - |
| Termen de valabilitate | rd_valabilitate | Text (100) | Da | - | - | - |
| Conditii de pastrare | rd_pastrare | Text (300) | Da | - | - | - |
| Cod EAN | rd_ean | Text (20) | Nu | 13 cifre | Validare de lungime | - |
| Aprobator Calitate | rd_aprobator | Lookup (systemuser) | Nu | - | Obligatoriu pentru Aprobata | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Fisier | rd_fisierurl | Text (500) | Nu | - | In 06_Eticheta | - |

## 2.18 TBL-32 Implementare (IPN)

Nume: `rd_implementare`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar IPN | rd_name | Autonumber | Da | IPN-{AA}-{SEQ:0000} | - | Coloana primara |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental, 1:1 in practica | - |
| Linie | rd_linie | Lookup (rd_linie) | Da | - | - | - |
| Data planificata productie 0 | rd_dataprod0 | Date Only | Da | - | - | - |
| Conditii IPN completate | rd_conditiiok | Yes/No | Da | Implicit Nu | Checklist de conditii, vezi 5.5.8 | - |
| Plan IPN aprobat | rd_planok | Yes/No | Da | Implicit Nu | - | - |
| IL productie emisa | rd_ilok | Yes/No | Da | Implicit Nu | - | - |
| Numar IL | rd_numaril | Text (30) | Nu | - | - | - |
| Plan HACCP actualizat | rd_haccpok | Yes/No | Da | Implicit Nu | Aprobare Calitate obligatorie | Cerinta IFS |
| Data actualizarii HACCP | rd_datahaccp | Date Only | Nu | - | - | - |
| Puncte critice noi identificate | rd_ccpnoi | Text Area (4000) | Nu | - | - | - |
| Necesita validare shelf life | rd_shelflife | Yes/No | Da | Implicit Da pentru produs nou | - | - |
| Termen de valabilitate propus (luni) | rd_valabilitate | Whole Number | Nu | 1 - 36 | - | - |
| Instruire operatori efectuata | rd_instruireok | Yes/No | Da | Implicit Nu | Data si lista de participanti in document | Cerinta IFS |
| Ambalaj disponibil | rd_ambalajok | Yes/No | Da | Implicit Nu | Blocheaza productia 0 | - |
| Status implementare | rd_statusipn | Choice | Da | In pregatire / Gata de productie 0 / In derulare / Finalizata / Amanata | Gata doar cu toate bifele Da | Business rule |
| Data implementarii | rd_dataimplementare | Date Only | Nu | - | Porneste ceasul revizuirii | Vezi Sectiunea 8 |

## 2.19 TBL-33 Productie 0 si TBL-34 Inregistrare de productie 0

Structura completa este in Sectiunea 7. Rezumat de coloane:

`rd_productie0`: Numar (Autonumber P0-{AA}-{SEQ:0000}, primara), Proiect (Lookup,
parental), Implementare (Lookup), Data (Date Only), Linie (Lookup), Schimb (Choice),
Cantitate planificata kg (Decimal 2), Cantitate realizata kg (Decimal 2), Randament aluat
% (Decimal 2), Rebut kg (Decimal 2), Rebut % (Decimal 2), Viteza nominala buc/h (Decimal
2), Viteza reala buc/h (Decimal 2), Eficienta viteza % (Decimal 2), Timp setup min (Whole
Number), Timp de schimb sortiment min (Whole Number), Greutate medie la ambalare g
(Decimal 2), Abatere de la gramaj % (Decimal 2), Conformitate HACCP (Yes/No), Numar
abateri de proces (Rollup Count), Decizie finala (Choice: Validat / Validat conditionat /
Se repeta), Conditii de validare (Text Area 4000), Responsabil decizie (Lookup), Data
deciziei (Date Only).

`rd_inregistrareprod0`: Productie 0 (Lookup, parental), Tip inregistrare (Choice:
Parametru de proces / Rebut pe cauza / Problema / Masuratoare de ambalare / Verificare
HACCP), Denumire (Text 150), Valoare specificata (Decimal 3), Valoare reala (Decimal 3),
Unitate (Choice), Abatere (Calculated Decimal), In toleranta (Yes/No), Cauza rebut
(Choice, vezi 7.3), Cantitate kg (Decimal 2), Procent (Decimal 2), Descriere problema
(Text Area), Actiune corectiva (Text Area), Responsabil (Lookup), Termen (Date Only),
Status actiune (Choice), Poza (Image).

## 2.20 TBL-35 Revizuire post-implementare

Nume: `rd_revizuire`. Structura completa in Sectiunea 8.

Coloane: Numar (Autonumber RPI-{AA}-{SEQ:0000}, primara), Proiect (Lookup, parental),
Etapa revizuire (Choice: 30 de zile / 60 de zile / 90 de zile), Data scadenta (Date
Only), Data efectuarii (Date Only), Status (Choice: Programata / In lucru / Finalizata /
Sarita), Numar reclamatii (Whole Number), Numar neconformitati interne (Whole Number),
Cantitate produsa cumulat kg (Decimal 2), Randament in serie % (Decimal 2), Randament la
productia 0 % (Decimal 2), Diferenta de randament (Calculated Decimal), Rebut in serie %
(Decimal 2), Cost real / kg (Currency 4), Cost din antecalcul / kg (Currency 4), Abatere
de cost % (Calculated Decimal), Feedback client (Text Area 4000), Feedback KAM (Text Area
4000), Volum realizat fata de estimat % (Decimal 2), Decizie (Choice: Mentinere /
Optimizare / Retragere), Actiuni (Text Area 4000), Responsabil (Lookup), Aprobator
(Lookup).

## 2.21 TBL-36 Linie de productie

Nume: `rd_linie`. Nomenclator cu cele 9 linii.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire linie | rd_name | Text (100) | Da | - | - | Coloana primara |
| Cod linie | rd_codlinie | Text (10) | Da | L01 - L09 | Unic | - |
| Amplasament | rd_amplasament | Choice | Da | Choice AMPLASAMENT | - | - |
| Tip linie | rd_tiplinie | Choice | Da | Laminare / Aluat dospit / Paine / Patiserie cu umplutura / Mixta | - | - |
| Echipament principal | rd_echipament | Text (200) | Nu | Fritsch / Rademaker / VMI / WP Bakery / JBT | - | - |
| Capabilitati | rd_capabilitati | Choice (multi) | Da | Laminare / Impletire / Injectare umplutura / Depunere / Presarare / Glazurare / Coacere tunel / Congelare rapida / Ambalare flow-pack / Ambalare tava | Filtreaza liniile compatibile cu produsul | Vezi 2.21.1 |
| Gramaj minim (g) | rd_gramajmin | Decimal (2) | Nu | - | Validare la alocarea liniei | - |
| Gramaj maxim (g) | rd_gramajmax | Decimal (2) | Nu | - | Idem | - |
| Latime banda (mm) | rd_latimebanda | Whole Number | Nu | - | Constrangere de dimensiune | - |
| Viteza nominala (buc/h) | rd_vitezanominala | Decimal (2) | Nu | - | Referinta pentru productia 0 | - |
| Timp schimb sortiment (min) | rd_timpschimb | Whole Number | Da | Implicit 120 | Din aplicatia de planificare | - |
| Tarif orar | rd_tariforar | Currency (2) | Nu | - | Pentru antecalcul | - |
| Numar proiecte active | rd_proiecteactive | Whole Number | Nu | 0 - 99 | Scris de FLX-06 | Coada pe linie |
| Prag de supraincarcare | rd_pragsupraincarcare | Whole Number | Da | Implicit 6 | Peste prag, semnalizare vizuala | Vezi 2.21.2 |
| Activa | rd_activa | Yes/No | Da | - | - | - |

2.21.1 Capabilitatile filtreaza liniile propuse la alocare. Un proiect de foietaj laminat
nu poate primi decat linii cu capabilitatea Laminare, iar gramajul trebuie sa intre in
intervalul liniei. Validarea este avertisment, nu blocaj: se poate forta cu motiv, pentru
ca dezvoltarea presupune uneori si incercari in afara plicului declarat.

2.21.2 Coada pe linie se vede si global, si pe fiecare linie. Cele 9 linii nu concureaza
intre ele: supraincarcarea liniei L03 nu retrogradeaza proiectele de pe L07.

## 2.22 TBL-37 Profil de tehnolog

Nume: `rd_profiltehnolog`. Extinde `systemuser` fara sa il inlocuiasca.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (150) | Da | Numele persoanei | - | Coloana primara |
| Utilizator | rd_utilizator | Lookup (systemuser) | Da | - | Unic | Sursa de adevar ramane Entra ID |
| Rol principal | rd_rolprincipal | Choice | Da | Choice ROL | - | - |
| Amplasament | rd_amplasament | Choice | Da | Choice AMPLASAMENT | - | - |
| Specializare | rd_specializare | Choice (multi) | Nu | Foietaj / Aluat dospit / Paine / Patiserie / Umpluturi / Ambalaje / Solutii tehnice | Filtreaza propunerea de alocare | - |
| Linii pe care lucreaza | rd_linii | Text (100) | Nu | Coduri de linie separate prin virgula | - | NOTA: N:N ar fi mai curat, dar se citeste mai greu in formular |
| Capacitate maxima proiecte | rd_capacitatemax | Whole Number | Da | 1 - 10, implicit 6 | Vezi 4.2 | - |
| Proiecte active | rd_proiecteactive | Whole Number | Nu | 0 - 99 | Scris de FLX-06 | - |
| Proiecte active P1 | rd_activep1 | Whole Number | Nu | 0 - 99 | Scris de FLX-06 | - |
| Grad de incarcare (%) | rd_incarcare | Decimal (2) | Nu | 0 - 300 | active / capacitate max x 100 | Vezi 2.22.1 |
| Semnal incarcare | rd_semnal | Choice | Nu | Verde / Galben / Rosu | Vezi 2.22.1 | Afisat in dashboard |
| Disponibil | rd_disponibil | Yes/No | Da | Implicit Da | Concediu, delegatie | - |
| Indisponibil pana la | rd_indisponibilpanala | Date Only | Nu | - | - | Intra in calculul termenului propus |
| Activ | rd_activ | Yes/No | Da | - | - | - |

2.22.1 Praguri de supraincarcare: Verde sub 80%; Galben 80-100%; Rosu peste 100%.
Suplimentar, un tehnolog cu mai mult de 2 proiecte in banda P1 se marcheaza Rosu
indiferent de gradul de incarcare, pentru ca P1 inseamna lucru simultan real, nu coada.

## 2.23 TBL-38 Client

Nume: `rd_client`.

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire client | rd_name | Text (200) | Da | - | - | Coloana primara |
| Cod SAP client | rd_codsap | Text (20) | Nu | - | - | Import |
| Clasificare | rd_clasificare | Choice | Da | A / B / C | Stabilita si revizuita de Sales / KAM | 20 de puncte in scor |
| Data ultimei clasificari | rd_dataclasificare | Date Only | Nu | - | Revizuire anuala | - |
| Canal | rd_canal | Choice | Da | Choice CANAL | - | - |
| Tara | rd_tara | Text (100) | Da | Implicit Romania | - | Determina cerintele de eticheta |
| KAM responsabil | rd_kam | Lookup (systemuser) | Da | - | - | - |
| Cerinte specifice de eticheta | rd_cerinteeticheta | Text Area (4000) | Nu | - | - | Se preiau automat in proiect |
| Cerinte de audit sau certificare | rd_cerinteaudit | Text Area (2000) | Nu | - | - | - |
| Numar proiecte active | rd_proiecteactive | Whole Number | Nu | - | Scris de FLX-06 | - |
| Activ | rd_activ | Yes/No | Da | - | - | - |

## 2.24 TBL-39 Indicator si TBL-40 Masurare de indicator

`rd_indicator` (definitie): Denumire (Text, primara), Cod (Text: T-TOTAL, Q-CORECT,
Q-COMPLET), Tip (Choice: Timp / Calitate / Volum), Nivel de masurare (Choice: Activitate
/ Rol / Persoana / Departament), Formula de calcul (Text Area 2000, descriptiva), Tinta
% (Decimal 2, intre 95 si 98), Prag de alerta % (Decimal 2), Unitate (Choice), Frecventa
(Choice: Saptamanal / Lunar / Trimestrial / Anual), Activ (Yes/No).

`rd_masurareindicator`: Indicator (Lookup, parental), Perioada (Choice: Luna / Trimestru
/ An), Data de inceput (Date Only), Data de sfarsit (Date Only), Nivel (Choice), Persoana
(Lookup systemuser), Rol (Choice), Linie (Lookup), Valoare realizata (Decimal 2), Tinta
(Decimal 2), Atins (Calculated Yes/No), Numar cazuri (Whole Number), Numar conforme
(Whole Number), Observatii (Text Area). Detaliile de calcul sunt in Sectiunea 13.

## 2.25 Nomenclatoare comune

### 2.25.1 rd_motiv (motive unificate)

Coloane: Denumire (Text 200, primara), Cod (Text 10), Tip motiv (Choice: Respingere
solicitare / Amanare / Respingere materie prima / Suspendare proiect / Abandon proiect /
Suprascriere prioritate / Blocaj / Respingere livrabil), Descriere (Text Area), Necesita
comentariu (Yes/No), Activ (Yes/No).

Motiv pentru o singura tabela de motive in loc de sase: motivele se raporteaza impreuna
la analiza anuala ("de ce nu s-au terminat proiectele"), iar o tabela unica cu tip
permite o singura vizualizare de analiza si o singura intretinere.

### 2.25.2 rd_tipdocument

Coloane: Denumire (Text 100, primara), Cod (Text 10, folosit in numele fisierului),
Faza (Choice FAZA), Extensie asteptata (Text 20), Necesita aprobare (Yes/No), Rol
aprobator (Choice ROL), Retentie (ani) (Whole Number), Sablon Word (Text 300), Activ
(Yes/No). Continutul complet in `data/nomenclatoare.json`.

### 2.25.3 Choice-uri globale

Lista completa, cu valori si etichete, in `data/choices.json`: AMPLASAMENT, CANAL,
AMBALARE, MOTIVCERERE, TIPPROIECT, STATUSPROIECT, STATUSLIVRABIL, STATUSETAPA,
STATUSMP, CATEGORIEMP, SURSABLOCAJ, TIPMOSTRA, TIPMASURATOARE, REZULTATTRIAL,
REZULTATITERATIE, VERDICT, TIPST, TIPETICHETA, TIPREFERINTA, FAZA, ROL, BANDA, SCHIMB,
UM, ALERGEN.

## 2.26 Rezumatul tabelelor

| Cod | Tabela | Nume logic | Tip | Val |
|---|---|---|---|---|
| TBL-01 | Solicitare (SCP) | rd_solicitare | Tranzactionala | 1 |
| TBL-02 | Proiect CDI | rd_proiect | Radacina | 1 |
| TBL-03 | Livrabil de proiect | rd_livrabil | Copil | 1 |
| TBL-04 | Sablon de livrabil | rd_sablonlivrabil | Configurare | 0 |
| TBL-05 | Etapa de proiect | rd_etapa | Copil | 1 |
| TBL-06 | Sablon de etapa | rd_sablonetapa | Configurare | 0 |
| TBL-07 | Materie prima de proiect | rd_mpproiect | Copil | 2 |
| TBL-08 | Iteratie de furnizor | rd_iteratiefurnizor | Copil | 2 |
| TBL-09 | Materie prima (catalog) | rd_materieprima | Nomenclator | 1 |
| TBL-10 | Furnizor | rd_furnizor | Nomenclator | 2 |
| TBL-11 | Blocaj | rd_blocaj | Copil | 2 |
| TBL-12 | Cerere de mostra | rd_ceremostra | Copil | 2 |
| TBL-13 | Miscare de mostra | rd_miscaremostra | Copil | 2 |
| TBL-14 | Fisa de testare | rd_fisatestare | Copil | 1 |
| TBL-15 | Trial | rd_trial | Copil | 1 |
| TBL-16 | Masuratoare | rd_masuratoare | Copil | 1 |
| TBL-16b | Statistica de trial | rd_statisticatrial | Derivata | 1 |
| TBL-17 | Evaluare senzoriala | rd_evaluaresenzoriala | Copil | 2 |
| TBL-18 | Criteriu senzorial | rd_criteriusenzorial | Nomenclator | 2 |
| TBL-19 | Scor senzorial | rd_scorsenzorial | Copil | 2 |
| TBL-20a | Defect (nomenclator) | rd_defect | Nomenclator | 2 |
| TBL-20b | Defect constatat | rd_defectconstatat | Copil | 2 |
| TBL-21 | Referinta de comparatie | rd_referinta | Copil | 1 |
| TBL-22 | Antecalcul | rd_antecalcul | Copil | 2 |
| TBL-23 | Linie de antecalcul | rd_linieantecalcul | Copil | 2 |
| TBL-24 | Reteta | rd_reteta | Copil | 2 |
| TBL-25 | Versiune de reteta | rd_versiunereteta | Copil | 2 |
| TBL-26 | Linie de reteta | rd_liniereteta | Copil | 2 |
| TBL-27 | Alergen | rd_alergen | Nomenclator | 3 |
| TBL-28 | (valorile nutritionale sunt coloane pe TBL-25, nu tabela separata - vezi 2.15) | - | - | - |
| TBL-29 | Specificatie tehnica | rd_specificatie | Copil | 2 |
| TBL-30 | SDP | rd_sdp | Copil | 2 |
| TBL-31 | Eticheta | rd_eticheta | Copil | 3 |
| TBL-32 | Implementare (IPN) | rd_implementare | Copil | 2 |
| TBL-33 | Productie 0 | rd_productie0 | Copil | 2 |
| TBL-34 | Inregistrare de productie 0 | rd_inregistrareprod0 | Copil | 2 |
| TBL-35 | Revizuire post-implementare | rd_revizuire | Copil | 3 |
| TBL-36 | Linie de productie | rd_linie | Nomenclator | 0 |
| TBL-37 | Profil de tehnolog | rd_profiltehnolog | Nomenclator | 0 |
| TBL-38 | Client | rd_client | Nomenclator | 0 |
| TBL-39 | Indicator | rd_indicator | Configurare | 3 |
| TBL-40 | Masurare de indicator | rd_masurareindicator | Derivata | 3 |
| TBL-41 | Motiv | rd_motiv | Nomenclator | 0 |
| TBL-42 | Tip document | rd_tipdocument | Nomenclator | 0 |


<!-- ==================== S03-relatii.md ==================== -->

---

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


<!-- ==================== S04-livrabile.md ==================== -->

---

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


<!-- ==================== S05-documentatie.md ==================== -->

---

# Sectiunea 5 - Structura documentatiei

Aceasta sectiune este centrala. Datele stau in Dataverse, fisierele in SharePoint.
Regula de departajare: daca informatia se cauta, se filtreaza, se aduna sau declanseaza
ceva, este data si sta in Dataverse. Daca informatia se citeste, se semneaza sau se
trimite in afara, este document si sta in SharePoint.

## 5.1 Arborele de foldere

### 5.1.1 Structura generata automat

Se creeaza de FLX-02, in momentul acceptarii proiectului, in biblioteca
`PRODUSE IN DEZVOLTARE`:

```
/PRODUSE IN DEZVOLTARE/{an}/{cod}_{nume produs}/
  00_Solicitare        SCP, EPC, cerinte client, referinta de comparatie
  01_Plan              plan dezvoltare, cerere achizitii mostra MP noua
  02_Testare           fisa de test, rapoarte de testare, poze
  03_Mostre            mostre MP si produs, evidenta livrarilor
  04_Antecalcul
  05_Specificatii      conditii ST, ST draft, ST intern MP, ST final, SDP
  06_Eticheta          eticheta punga, eticheta bax, fisier Colos / Zebra
  07_Implementare      conditii IPN, plan IPN, IL productie, plan HACCP, prod 0
  08_Dosar_validat     TDV validat, dosar final, cod material SAP
```

PROPUNERE: se adauga un al zecelea folder, `09_Revizuire`, pentru rapoartele de la 30,
60 si 90 de zile. Motiv: revizuirea post-implementare produce documente dupa inchiderea
dosarului validat, iar amestecarea lor in `08_Dosar_validat` ar strica principiul ca
dosarul validat este inghetat la data validarii.

### 5.1.2 De ce structura pe faze este superioara celei actuale

| Criteriu | Structura actuala (Antecalcul, Finalizare ST, Implementare, Mostra) | Structura pe faze |
|---|---|---|
| Acoperire | Patru foldere pentru un proces cu noua faze; solicitarea, testarea si eticheta nu au loc propriu si ajung in radacina | Fiecare faza are exact un loc |
| Cautare | "Unde e fisa de test?" nu are raspuns unic | Faza determina folderul, fara ambiguitate |
| Ordine | Numele nu spun ordinea; sortarea alfabetica pune Antecalcul primul, desi este al patrulea in proces | Prefixul numeric ordoneaza folderul in ordinea reala a procesului |
| Audit | Auditorul cere dovezi in ordinea procesului si trebuie ghidat manual | Auditorul parcurge 00 - 08 si vede singur ce lipseste |
| Automatizare | Fisierele din radacina nu se pot lega de un livrabil | Fiecare livrabil are folderul lui tinta, deci incarcarea se poate valida automat |

### 5.1.3 Migrarea folderelor existente

| Pas | Actiune | Cine | Observatie |
|---|---|---|---|
| 1 | Inventar: se listeaza cu un flux toate folderele de proiect si continutul lor, intr-un fisier Excel de lucru | Head of R&D | Fara mutari inca |
| 2 | Maparea folderelor vechi: Antecalcul -> 04, Finalizare ST -> 05, Implementare -> 07, Mostra -> 03 | Head of R&D | Regula fixa |
| 3 | Fisierele din radacina se clasifica dupa nume: cele cu "eticheta" -> 06, cele cu "SAP" sau "material" -> 08, restul -> 00 | Flux + verificare manuala | Vezi 5.1.4 |
| 4 | Se creeaza folderele lipsa (00, 01, 02, 06, 08, 09) in fiecare proiect | Flux | Goale, dar prezente |
| 5 | Se muta fisierele conform mapei, pastrand numele original | Flux | Redenumirea vine la pasul 7 |
| 6 | Se creeaza inregistrarea de proiect in Dataverse si se leaga de folder | Flux de migrare | Vezi Sectiunea 15 |
| 7 | Redenumirea la conventia din 5.2 se face doar pentru proiectele din ultimele 24 de luni | Suport R&D | Vezi 5.1.5 |

5.1.4 Fisierele care nu se pot clasifica automat raman intr-un folder `99_Neclasificat`
din proiect si apar intr-un raport de curatare. Nu se sterge nimic si nu se ghiceste.

5.1.5 NOTA: nu se redenumesc retroactiv toate fisierele istorice. Efortul este de ordinul
a mii de fisiere, castigul este estetic, iar riscul de a rupe legaturi existente este
real. Se redenumesc doar proiectele active si cele din ultimele 24 de luni, care intra
efectiv in audit.

### 5.1.6 Proiectele-copil (.1)

Proiectul-copil primeste folder propriu, `{cod parinte}.1_{nume}`, ca subfolder al
proiectului parinte. Documentele parintelui nu se copiaza; se refera prin legatura din
Dataverse. Motiv: dublarea fizica ar crea doua versiuni ale aceleiasi ST, iar la audit
nu s-ar mai putea spune care este in vigoare.

## 5.2 Conventia de denumire a fisierelor

### 5.2.1 Formatul

```
{cod proiect}_{tip document}_{vNN}_{AAAALLZZ}.{ext}
```

Reguli: fara diacritice; fara spatii (se foloseste `_`); codul de tip document din
nomenclatorul `rd_tipdocument` (5.2.3); versiunea pe doua cifre; data in formatul
AAAALLZZ, care sorteaza cronologic.

### 5.2.2 Exemple reale

| Fisier | Ce este |
|---|---|
| `26025_SCP_v01_20260114.pdf` | Solicitarea initiala pentru proiectul 26025 |
| `26025_PLAN_v01_20260116.docx` | Plan de dezvoltare, prima versiune |
| `26025_PLAN_v02_20260121.docx` | Planul revizuit dupa feedbackul clientului |
| `26025_FTEST_v01_20260119.pdf` | Fisa de test |
| `26025_RTEST_v01_20260122.pdf` | Raport de testare, generat din masuratori |
| `26025_ANTECALC_v03_20260123.xlsx` | A treia varianta de antecalcul |
| `26025_STDRAFT_v01_20260126.pdf` | ST draft |
| `26025_STFINAL_v01_20260202.pdf` | ST finala aprobata |
| `26025_SDP_v01_20260203.pdf` | Specificatia de produs |
| `26025_ETPUNGA_v02_20260204.pdf` | Eticheta de punga, versiunea 2 |
| `26025_PLANIPN_v01_20260206.pdf` | Plan IPN |
| `26025_RPROD0_v01_20260212.pdf` | Raport de productie 0 |
| `26025_TDV_v01_20260215.pdf` | TDV validat, semnat |
| `26025.1_RTEST_v01_20260304.pdf` | Raport de testare pe proiectul-copil |
| `26025_RPI30_v01_20260317.pdf` | Revizuire la 30 de zile |

### 5.2.3 Codurile de tip document

| Cod | Document | Folder | Retentie |
|---|---|---|---|
| SCP | Solicitare cerinta produs | 00 | 5 ani |
| EPC | Eticheta produs client | 00 | 5 ani |
| REF | Documentatie de referinta | 00 | 3 ani |
| PLAN | Plan de dezvoltare produs | 01 | 5 ani |
| CAMP | Cerere achizitii mostra MP | 01 | 3 ani |
| FTEST | Fisa de test | 02 | 5 ani |
| RTEST | Raport de testare | 02 | 5 ani |
| FSENZ | Fisa de evaluare senzoriala | 02 | 5 ani |
| POZA | Documentatie foto | 02 | 3 ani |
| DMOSTRA | Dosar de mostra | 03 | 3 ani |
| ANTECALC | Antecalcul | 04 | 5 ani |
| CONDST | Conditii ST | 05 | 10 ani |
| STDRAFT | ST draft | 05 | 10 ani |
| STFINAL | ST finala | 05 | 10 ani |
| STMP | ST interna materie prima | 05 | 10 ani |
| SDP | Specificatie de produs | 05 | 10 ani |
| ETPUNGA | Eticheta punga | 06 | 10 ani |
| ETBAX | Eticheta bax | 06 | 10 ani |
| ETPRINT | Fisier imprimanta Colos / Zebra | 06 | 5 ani |
| CONDIPN | Conditii IPN | 07 | 10 ani |
| PLANIPN | Plan IPN | 07 | 10 ani |
| IL | Instructiune de lucru | 07 | 10 ani |
| HACCP | Plan HACCP actualizat | 07 | Permanent |
| INSTR | Dovada de instruire | 07 | 5 ani |
| RPROD0 | Raport de productie 0 | 07 | 10 ani |
| TDV | TDV validat | 08 | Permanent |
| DOSAR | Dosar validat complet | 08 | Permanent |
| SAP | Dovada codului de material SAP | 08 | 10 ani |
| RPI30 / RPI60 / RPI90 | Rapoarte de revizuire | 09 | 5 ani |

5.2.4 Denumirea nu se scrie manual. FLX-12 genereaza documentele din sabloane Word cu
numele deja corect; pentru fisierele incarcate manual, aplicatia canvas si formularul
model-driven propun numele prin butonul "Incarca document la livrabil", care primeste
codul de proiect si tipul din contextul livrabilului.

## 5.3 Coloanele de metadate din biblioteca

Biblioteca `PRODUSE IN DEZVOLTARE` primeste urmatoarele coloane de site, cu tipurile
SharePoint corespunzatoare:

| Coloana | Tip SharePoint | Obligatorie | Sursa valorii | Observatii |
|---|---|---|---|---|
| Cod proiect | Text (single line) | Da | Scrisa de flux la incarcare | Indexata |
| Tip document | Choice | Da | Nomenclator 5.2.3 | Indexata |
| Versiune document | Text | Da | Din numele fisierului | Diferita de versiunea SharePoint |
| Status document | Choice: Ciorna / In aprobare / Aprobat / Inlocuit / Retras | Da | Actualizata de fluxul de aprobare | Vezi 5.4 |
| Autor | Person | Da | Utilizatorul care incarca | - |
| Aprobator | Person | Nu | Din livrabilul asociat | - |
| Data aprobarii | Date | Nu | La aprobare | - |
| Produs | Text | Da | Numele produsului din proiect | Pentru cautare libera |
| Linie | Choice | Nu | Codul liniei | - |
| Client | Text | Da | Din proiect | - |
| Faza | Choice: 00 - 09 | Da | Din folderul tinta | Indexata |
| Livrabil asociat | Text | Nu | Codul LIV-nn | Leaga fisierul de inregistrare |
| Confidential | Yes/No | Da | Implicit Nu | Vezi 11.6 |

5.3.1 Coloanele indexate (Cod proiect, Tip document, Faza) sunt obligatorii pentru ca
biblioteca va depasi pragul de 5000 de elemente in mai putin de doi ani la 130-180 de
proiecte pe an cu 20-30 de fisiere fiecare. Fara indexare, vizualizarile filtrate se
opresc cu eroare de prag.

5.3.2 NOTA: metadatele se scriu de flux, nu de utilizator. Un tehnolog cu manusi in hala
nu completeaza 13 coloane. Formularul de incarcare din aplicatie primeste doar fisierul
si tipul de document; restul se deduce din livrabilul si proiectul in context.

## 5.4 Politica de versionare

### 5.4.1 Setari de biblioteca

| Setare | Valoare | Motiv |
|---|---|---|
| Versionare | Majora si minora (publicare) | Ciornele nu trebuie sa fie vizibile companiei |
| Versiuni majore pastrate | 50 | Acopera intreaga viata a unui document de produs |
| Ciorne pastrate per versiune majora | 10 | Suficient pentru un ciclu de revizuire |
| Cine vede ciornele | Autorul si aprobatorii | Restul companiei vede doar versiunile publicate |
| Check-out obligatoriu | Da pentru folderele 05, 06, 07, 08 | Documentele care se aproba nu se editeaza in paralel |
| Cos de reciclare | 93 de zile, plus cos de nivel doi | Recuperare dupa stergere accidentala |

### 5.4.2 Semnificatia versiunilor

| Tip | Cand | Efect |
|---|---|---|
| Minora (0.1, 0.2, ...) | Orice salvare in lucru | Vizibila doar autorului si aprobatorilor |
| Majora (1.0, 2.0, ...) | La publicare, dupa aprobare | Vizibila tuturor; devine versiunea in vigoare |
| Majora noua peste una aprobata | Orice modificare de continut dupa aprobare | Obliga la motivul modificarii si la reaprobare |

### 5.4.3 Ce se blocheaza dupa aprobare

5.4.3.1 La aprobarea unui document (status `Aprobat`), fluxul FLX-19: seteaza versiunea
majora, aplica `Retentie / Nu se poate edita` prin eticheta de retentie Purview daca este
disponibila, altfel seteaza permisiune de citire pe fisier pentru toti in afara de
Calitate si Head of R&D, si scrie data aprobarii in Dataverse.

5.4.3.2 Documentele blocate: ST finala, SDP, eticheta aprobata, plan IPN, plan HACCP,
raport de productie 0, TDV validat. Acestea sunt dovezile de audit; o modificare ulterioara
fara versiune noua ar face dosarul nereconstituibil.

5.4.3.3 Documentele care raman editabile dupa aprobare: planul de dezvoltare (se
actualizeaza in timpul proiectului), dosarul de mostra, documentatia foto.

### 5.4.4 Retentia

Se aplica etichetele de retentie din 5.2.3, la nivel de tip de document. Documentele
`Permanent` (TDV, dosar validat, HACCP) nu se sterg niciodata automat. Restul intra in
revizuire de dispozitie la expirarea termenului, cu aprobarea Head of R&D.

### 5.4.5 Proiectele abandonate si respinse

| Situatie | Ce se intampla cu documentele |
|---|---|
| Solicitare respinsa la triaj | Nu se creeaza folder. SCP-ul ramane ca inregistrare in Dataverse, cu motivul |
| Proiect abandonat dupa acceptare | Folderul se pastreaza integral, se muta in `/PRODUSE IN DEZVOLTARE/{an}/_ABANDONATE/`, cu prefixul `X_` la numele folderului |
| Proiect suspendat | Folderul ramane pe loc. Suspendarea este temporara |
| Proiect respins de client dupa mostra | Se trateaza ca abandonat, cu motivul "Respins de client" |

5.4.5.1 Documentele proiectelor abandonate raman consultabile, read-only, cu retentie de
5 ani. Motiv: peste doi ani, cand acelasi client cere un produs similar, dosarul
abandonat este cea mai ieftina sursa de informatie din companie. Se marcheaza vizibil ca
abandonat, ca sa nu fie confundat cu un produs in productie.

## 5.5 Continutul-cadru al documentelor generate din date

Constructie pe referinta IFS Food v8 (capitolele 4.3 Specificatii, 4.4 Dezvoltare de
produs, 4.5 Achizitii, 5.6 Validare) si practica standard din bakery industrial, nu pe
formularele actuale ale companiei. Formatul intern al ST nu se trateaza aici.

Legenda coloanei "Sursa": [D] = preluat automat din Dataverse; [M] = completat manual;
[C] = calculat.

### 5.5.1 DOC-01 SCP - Solicitare cerinta produs

**Scop**: sa transforme o discutie comerciala intr-o cerinta tehnica evaluabila, astfel
incat triajul sa se poata face fara alte intrebari catre KAM.

**Completeaza**: KAM. **Aproba**: Manager R&D (prin decizia de triaj).

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Numar SCP, data, KAM, client, clasificare client, canal | [D] |
| 2. Produsul cerut | Denumire de lucru, descriere, categorie, gramaj, dimensiuni, bucati pe ambalaj, tip ambalare | [M] |
| 3. Piata | Volum estimat anual, sezonalitate, magazine sau puncte de livrare, pret tinta | [M] |
| 4. Termen | Termen dorit, termen impus extern si tipul lui, data listarii | [M] |
| 5. Motivul cererii | Motiv din nomenclator, context comercial | [M] |
| 6. Referinta de comparatie | Tip, denumire, producator, pret raft, poza, eticheta | [M] |
| 7. Cerinte de eticheta | Limbi, marca, declaratii obligatorii, cerinte de client | [M] + [D] din client |
| 8. Cerinte de ambalaj | Material, format, print, dimensiune bax, paletizare | [M] |
| 9. Restrictii | Alergeni interzisi, aditivi interzisi, cerinte bio / halal, origine | [M] |
| 10. Triaj | Rezultat, motiv, comentariu, data, cod de proiect generat | [D] |

### 5.5.2 DOC-02 Plan de dezvoltare produs

**Scop**: sa fixeze ce se dezvolta, cu ce resurse, in ce pasi si cu ce criterii de
succes, inainte de a consuma materie prima si timp de linie.

**Completeaza**: tehnolog. **Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Cod proiect, produs, client, tehnolog, data, versiune | [D] |
| 2. Obiectiv | Descrierea produsului tinta, in termeni masurabili | [M] |
| 3. Criterii de acceptanta | Gramaj si toleranta, dimensiuni si toleranta, aspect, textura, scor senzorial minim, cost tinta | [M] |
| 4. Abordare tehnologica | Tip de aluat, proces propus, linie vizata, capabilitati necesare | [M] |
| 5. Materii prime | Lista, existente si noi, furnizori propusi, lead time, riscuri | [D] din TBL-07 |
| 6. Plan de testare | Numar de trialuri estimate, ce se varieaza la fiecare, esantioane | [M] |
| 7. Etape si termene | Etapele din sablon, cu date planificate | [D] din TBL-05 |
| 8. Livrabile | Lista livrabilelor aplicabile, cu responsabil si termen | [D] din TBL-03 |
| 9. Riscuri de proiect | Risc, probabilitate, masura | [M] |
| 10. Resurse | Ore de linie estimate, cantitati de MP, cost estimat al dezvoltarii | [M] + [C] |
| 11. Aprobare | Tehnolog, Manager R&D, data | [D] |

### 5.5.3 DOC-03 Fisa de testare

**Scop**: sa defineasca inainte de trial ce se masoara si fata de ce tolerante, astfel
incat rezultatul sa fie interpretabil, nu discutabil.

**Completeaza**: tehnolog. **Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Numar fisa, proiect, produs, versiune de reteta testata, data planificata | [D] |
| 2. Obiectivul testarii | Ce ipoteza se verifica | [M] |
| 3. Reteta | Lista completa de ingrediente cu cantitati, din versiunea testata | [D] din TBL-26 |
| 4. Parametri de proces tinta | Framantare, fermentare, laminare, dospire, coacere, congelare, cu valori si tolerante | [M] |
| 5. Plan de esantionare | Ce se masoara, cate bucati pe tip, in ce moment | [M] + implicit din 6.2.1 |
| 6. Tolerante declarate | Pentru fiecare masuratoare: tinta, toleranta minus, toleranta plus | [M] |
| 7. Criterii senzoriale | Grila aplicabila, scor minim acceptabil, defecte eliminatorii | [D] din TBL-18 |
| 8. Resurse si siguranta | Cantitate de aluat, timp de linie, alergeni prezenti, masuri de separare | [M] |
| 9. Aprobare | Tehnolog, Manager R&D, data | [D] |

### 5.5.4 DOC-04 Raport de testare

**Scop**: sa arate ce a iesit, cu cifre, si sa sustina decizia de a continua sau de a
relua.

**Completeaza**: se genereaza integral din date; tehnologul adauga doar concluzia.
**Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Proiect, fisa de testare, trial, data, linie, schimb, operator | [D] |
| 2. Reteta executata | Ingrediente si cantitati reale | [D] |
| 3. Parametri realizati fata de tinta | Tabel cu specificat, real, abatere, in toleranta | [D] + [C] |
| 4. Randament | Aluat introdus, bucati obtinute, randament calculat, pierderi pe faze | [C] |
| 5. Masuratori | Pe tip: n, media, abaterea standard, CV, min, max, conformitate | [C] din TBL-16b |
| 6. Neconformitati | Masuratorile in afara tolerantei, cu bucata si valoarea | [D] |
| 7. Evaluare senzoriala | Scor ponderat, scor pe criterii, verdict, comparatie cu referinta | [D] din TBL-17 |
| 8. Defecte constatate | Defect, severitate, procent afectat, poza | [D] |
| 9. Documentatie foto | Pozele din masuratori si defecte | [D] |
| 10. Concluzie si decizie | Reusit / Reusit cu observatii / Nereusit, ce se schimba la trialul urmator | [M] |
| 11. Aprobare | Tehnolog, Manager R&D, data | [D] |

### 5.5.5 DOC-05 Fisa de evaluare senzoriala

**Scop**: sa produca un verdict repetabil si aparabil, nu o impresie.

**Completeaza**: evaluatorii, pe telefon. **Aproba**: Manager R&D.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Numar evaluare, proiect, trial, data, tip de evaluare | [D] |
| 2. Conditii de degustare | Temperatura de servire, timp de la coacere, ordinea probelor, codificare oarba | [M] |
| 3. Panel | Evaluatori, rol, experienta | [D] |
| 4. Grila | Criterii cu pondere, ancore descriptive pentru 1, 3 si 5 | [D] din TBL-18 |
| 5. Scoruri individuale | Scor pe evaluator si criteriu, cu comentariu la scor <= 2 | [M] |
| 6. Scoruri comparative | Aceleasi criterii, aplicate referintei | [M] |
| 7. Sinteza | Scor ponderat produs, scor ponderat referinta, diferenta, dezacord maxim | [C] |
| 8. Defecte bifate | Din lista, cu severitate si procent | [M] |
| 9. Verdict | Acceptat / Acceptat cu observatii / Respins, cu regula din 6.5.5 | [C] + [M] |
| 10. Actiuni cerute | Ce se modifica, cine, pana cand | [M] |

### 5.5.6 DOC-06 Antecalcul

**Scop**: sa arate daca produsul are marja la pretul discutat, inainte de a-l promite.

**Completeaza**: tehnolog. **Aproba**: Manager R&D (si Financiar, daca marja este sub
prag).

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Proiect, produs, versiune de antecalcul, versiune de reteta, data, linie | [D] |
| 2. Ipoteze | Lot de referinta, viteza de linie, pierdere tehnologica, randament asumat | [M] + [D] din linie |
| 3. Materii prime | Ingredient, cantitate kg/100kg, pret unitar, sursa pretului, data pretului, cost | [D] + [C] |
| 4. Cost MP | Total MP, ajustat cu pierderea tehnologica | [C] |
| 5. Ambalaj | Punga, bax, eticheta, palet, cost pe bucata | [M] + [C] |
| 6. Manopera | Timp de linie, tarif orar, numar de operatori, cost pe kg | [C] |
| 7. Energie si congelare | Cost de coacere, cost de congelare separat, utilitati | [C] |
| 8. Regie | Procent aplicat, baza de aplicare | [D] parametru |
| 9. Cost total | Pe kg si pe bucata | [C] |
| 10. Pret si marja | Pret tinta, marja bruta, comparatie cu pragul companiei | [C] |
| 11. Sensibilitate | Efectul unei variatii de +/- 10% la cele mai scumpe trei materii prime | [C] |
| 12. Aprobare | Tehnolog, Manager R&D, data | [D] |

PROPUNERE: sectiunea 11 (sensibilitate) nu exista azi. Motiv: la produse de panificatie
congelata, faina si grasimea de laminare fac tipic peste 60% din costul de materie prima,
iar volatilitatea lor decide singura daca marja promisa tine sase luni.

### 5.5.7 DOC-07 SDP - Specificatie de produs

**Scop**: sa fie sursa unica din care se scrie instructiunea de lucru si dupa care se
produce, in timpul si dupa implementare.

**Completeaza**: tehnolog. **Aproba**: Manager R&D si Calitate.

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Cod SAP, denumire, versiune, data, linie, aprobatori | [D] |
| 2. Descrierea produsului | Denumire legala, descriere, gramaj, dimensiuni, forma, aspect tinta | [D] |
| 3. Reteta de productie | Ingrediente, cantitati pe sarja de productie, ordinea de adaugare, faza | [D] din TBL-26 |
| 4. Proces pas cu pas | Pentru fiecare faza: parametru, valoare, toleranta, echipament, durata | [D] din trialul validat |
| 5. Puncte critice | CCP si oPRP din planul HACCP, valori limita, monitorizare, actiune la deviatie | [D] + [M] Calitate |
| 6. Controale in proces | Ce se verifica, la ce frecventa, cine, ce se inregistreaza | [M] |
| 7. Ambalare | Tip de ambalaj, numar de bucati, gramaj net, toleranta de cantarire, eticheta aplicata | [D] |
| 8. Paletizare | Bucati pe bax, baxuri pe strat, straturi pe palet, eticheta de palet | [M] |
| 9. Depozitare si transport | Temperatura, umiditate, termen de valabilitate, conditii de transport | [M] |
| 10. Utilizare la client | Decongelare, dospire, coacere, timp si temperatura, randament asteptat | [M] |
| 11. Alergeni | Alergeni continuti, urme, masuri de separare pe linie | [D] din Sectiunea 9 |
| 12. Valori nutritionale | Tabelul pe 100 g si pe portie | [D] |
| 13. Istoricul versiunilor | Versiune, data, modificare, autor, aprobator | [D] |

### 5.5.8 DOC-08 Conditii IPN si Plan IPN

**Scop**: sa garanteze ca nimic nu lipseste inainte de prima productie pe linie, si sa
spuna cine face ce in ziua respectiva.

**Completeaza**: tehnolog. **Aproba**: Manager R&D, Calitate, Productie.

Conditii IPN - checklist, fiecare pozitie cu bifa, responsabil si dovada:

| Nr | Conditie | Responsabil | Dovada |
|---|---|---|---|
| 1 | ST finala aprobata | Tehnolog | LIV-24 |
| 2 | SDP aprobata | Tehnolog | LIV-25 |
| 3 | Cod material SAP creat pentru produsul finit | Tehnolog | LIV-26 |
| 4 | Toate materiile prime receptionate si eliberate de Calitate | Achizitii | TBL-07 |
| 5 | Ambalajul disponibil in cantitate suficienta | Achizitii | LIV-29 |
| 6 | Eticheta aprobata si fisierul de imprimanta incarcat | Suport R&D | LIV-28, LIV-29 |
| 7 | Plan HACCP actualizat si aprobat | Calitate | LIV-34 |
| 8 | IL de productie emisa si afisata la linie | Tehnolog | LIV-33 |
| 9 | Operatorii instruiti, cu lista de prezenta | Productie | LIV-35 |
| 10 | Slotul de linie confirmat in planificare | Planificare | TBL-02 |
| 11 | Setarile de linie pregatite (scule, forme, matrite) | Productie | [M] |
| 12 | Plan de esantionare pentru productia 0 stabilit | Tehnolog | Sectiunea 7 |
| 13 | Decizia de destinatie a productiei 0 (vanzare, mostra, rebut) | Manager R&D | [M] |

Plan IPN:

| Sectiune | Campuri | Sursa |
|---|---|---|
| 1. Identificare | Proiect, produs, linie, data, schimb, cantitate planificata | [D] |
| 2. Echipa | Tehnolog, sef de tura, operator-cheie, Calitate, Mentenanta, cine decide oprirea | [M] |
| 3. Program orar | Ora de setup, ora de start, puncte de verificare, ora estimata de final | [M] |
| 4. Parametri de urmarit | Din SDP, cu valorile si tolerantele | [D] |
| 5. Plan de esantionare | Ce, cand, cate bucati, cine masoara | [M] |
| 6. Criterii de oprire | Ce abatere opreste productia si cine decide | [M] |
| 7. Destinatia produsului | Vanzabil / mostra / rebut, cu decizie asumata | [M] |
| 8. Riscuri anticipate | Ce poate merge prost, ce se pregateste dinainte | [M] |
| 9. Aprobare | Trei semnaturi: R&D, Calitate, Productie | [D] |

### 5.5.9 DOC-09 Raport de productie 0

**Scop**: sa transforme prima productie intr-o validare documentata, nu intr-o amintire.
Continutul complet este in Sectiunea 7; structura documentului urmeaza sectiunile 7.2 -
7.9, plus decizia finala si semnaturile.

### 5.5.10 DOC-10 Dosar TDV validat

**Scop**: sa fie dovada unica, la audit si la reclamatie, ca produsul a fost dezvoltat,
testat si validat corect.

**Completeaza**: suport R&D, prin generare automata. **Aproba**: Manager R&D si
Managementul Calitatii.

| Sectiune | Continut | Sursa |
|---|---|---|
| 1. Pagina de garda | Cod proiect, produs, client, cod SAP, data validarii, semnaturi | [D] |
| 2. Cerinta initiala | SCP, cu referinta de comparatie | [D] |
| 3. Traseul proiectului | Etape cu date planificate si reale, blocaje cu motiv | [D] |
| 4. Reteta validata | Versiunea validata, cu istoricul versiunilor | [D] |
| 5. Rezultate de testare | Sinteza trialurilor, statistica, conformitatea | [D] |
| 6. Evaluare senzoriala | Verdictul final si comparatia cu referinta | [D] |
| 7. Antecalcul aprobat | Costul si marja la data validarii | [D] |
| 8. Specificatii | ST finala, SDP, cu versiunile in vigoare | [D] |
| 9. Alergeni si nutritionale | Valorile calculate si baza de calcul | [D] |
| 10. Eticheta aprobata | Imaginea etichetei si data aprobarii | [D] |
| 11. Implementare | Conditii IPN, plan IPN, plan HACCP, IL | [D] |
| 12. Productie 0 | Raportul si decizia | [D] |
| 13. Lista livrabilelor | Toate livrabilele cu status, data si responsabil | [D] |
| 14. Declaratie de validare | Textul de validare, semnat R&D si Calitate | [M] |

5.5.10.1 Dosarul TDV se genereaza integral din date, ca PDF, cu link-uri catre fisierele
sursa. Nimeni nu il asambleaza manual. Aceasta este dovada practica ca "dosarul de produs
este reconstituibil oricand".

### 5.5.11 DOC-11 Raport de revizuire post-implementare

Structura urmeaza Sectiunea 8: identificare, perioada acoperita, reclamatii si
neconformitati, randament in serie fata de productia 0, rebut, feedback client si KAM,
cost real fata de antecalcul, volum realizat fata de estimat, decizie (mentinere,
optimizare, retragere), actiuni cu responsabil si termen, semnaturi.

## 5.6 Trasabilitatea

### 5.6.1 Ce se auditeaza in Dataverse

| Ce | Nivel | Motiv |
|---|---|---|
| Toate tabelele din 2.1 - 2.20 | Creare, modificare, stergere, atribuire | Cerinta IFS de trasabilitate |
| Coloanele de status | Modificare | Cine a mutat proiectul si cand |
| Coloanele de termen (propus, negociat, realizat) | Modificare | Sursa disputelor cu comercialul |
| Scorul si suprascrierea de prioritate | Modificare | Cerinta explicita: urma in audit |
| Aprobarile (aprobator, data aprobarii) | Modificare | Dovada de semnatura |
| Reteta si liniile de reteta | Toate | Reconstituirea produsului la orice data |
| Alergeni si valori nutritionale | Modificare | Raspundere legala |
| Accesul la citire | Doar pe tabelele marcate confidential | Auditul de citire este scump; se aplica selectiv |

### 5.6.2 Cine vede istoricul

| Rol | Ce istoric vede |
|---|---|
| Head of R&D, Manager R&D | Tot, pe toate tabelele |
| Calitate | Tot ce tine de specificatii, alergeni, HACCP, aprobari |
| Tehnolog | Istoricul proiectelor proprii |
| Auditor (rol dedicat, temporar) | Citire pe tot, inclusiv audit, fara drept de modificare |
| KAM, restul companiei | Nu vad istoricul de audit; vad doar starea curenta si datele |

5.6.2.1 PROPUNERE: rol de securitate `RD Auditor`, activat pe durata auditului si
dezactivat dupa. Motiv: auditorul extern are nevoie de acces de citire demonstrabil, dar
nu trebuie sa aiba cont permanent cu drepturi largi.

### 5.6.3 Cum se demonstreaza la audit

5.6.3.1 Intrebarea tipica de audit este "aratati-mi cum a fost dezvoltat produsul X si
cine a aprobat ce". Raspunsul se da in trei pasi, din aplicatie, in fata auditorului:

| Pas | Ecran | Ce arata |
|---|---|---|
| 1 | Formularul de proiect, fila Livrabile | Toate livrabilele, cu responsabil, termen, data realizarii, aprobator, link la document |
| 2 | Butonul "Genereaza dosar TDV" | PDF-ul complet, cu toate documentele in vigoare la data validarii |
| 3 | Fila Audit history, pe inregistrarea sau coloana ceruta | Cine a modificat, ce valoare a fost inainte, ce valoare dupa, la ce data si ora |

5.6.3.2 Pentru documente, versiunea in vigoare la o data din trecut se obtine din
istoricul de versiuni SharePoint al fisierului, care pastreaza autorul si data fiecarei
publicari.

5.6.3.3 NOTA de platforma: auditul Dataverse are retentie configurabila la nivel de
mediu, implicit limitata. Se seteaza explicit retentia de audit la valoarea maxima
disponibila in licenta si, pentru cerinta IFS de pastrare peste acea limita, se ruleaza
lunar FLX-20, care exporta jurnalul de audit al tabelelor critice intr-o biblioteca
SharePoint de arhiva, cu retentie proprie. Fara acest export, jurnalul de audit se pierde
tacit dupa perioada de retentie a mediului.
