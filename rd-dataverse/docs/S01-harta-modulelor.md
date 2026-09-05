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
| M05 | Livrabile de proiect | Generarea din sablon a celor ~34 de livrabile, termen, responsabil, status | Tehnolog | Model-driven | 1 | Val 1 |
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
care nu pot fi exprimate altfel (scor de prioritate, statistica de masuratori, alergeni).
