# Provizionarea modelului de date

Creeaza in Dataverse, prin Web API, cele 31 de seturi de optiuni globale, 60 de tabele,
738 de coloane si 151 de relatii definite in `data/`.

Inlocuieste aproximativ 45 de zile de click-uri in interfata Power Apps cu o rulare de
sub o ora.

## Ce acopera

| Element | Numar | Cum |
|---|---|---|
| Seturi de optiuni globale | 31 | Generat integral |
| Tabele | 60 | Generat integral, cu coloana primara si audit activat |
| Coloane | 738 | Generat integral |
| Coloane de tip Lookup | 163 | Create prin relatii, nu separat |
| Relatii | 151 | Generat integral, cu comportamentul la stergere din `relatii.json` |
| **Coloane Calculated si Rollup** | **24** | **Manual, in interfata** - vezi mai jos |

Total: 985 din 985 de coloane ale modelului sunt acoperite, dintre care 961 automat.

## Ce ramane manual si de ce

Cele 24 de coloane Calculated si Rollup nu se pot crea complet prin API: definitia formulei
este o structura interna pe care API-ul de metadate nu o accepta fiabil. Lista lor completa
este in `payloaduri/coloane-manuale.json`, cu tabela, numele si regula de calcul din
blueprint.

Se creeaza in interfata, in aproximativ 2 ore, dupa ce restul modelului exista - ceea ce
este si ordinea corecta, pentru ca formulele refera coloane care trebuie sa existe deja.

## Cerinte

1. Un mediu Dataverse (Developer sau Sandbox).
2. O inregistrare de aplicatie in Entra ID (app registration) cu drept de a scrie metadate,
   adaugata ca utilizator de aplicatie in mediu, cu rolul System Customizer sau System
   Administrator.
3. Solutia `RDSuitaDigitala` creata in prealabil, cu editorul `RD Digital` si prefixul `rd`
   (pasul 3 din `build/V0-ghid-constructie.md`). Scriptul adauga componentele in ea prin
   antetul `MSCRM.SolutionUniqueName`.

## Utilizare

```bash
# 1. Verifica ce se va crea, fara sa atinga serverul
python3 build/deploy/provisioning.py --dry-run

# 2. Salveaza payloadurile ca JSON, pentru inspectie sau pentru alt instrument
python3 build/deploy/provisioning.py --dry-run --scrie-payload

# 3. Configureaza autentificarea
export DV_URL=https://organizatie.crm4.dynamics.com
export DV_TENANT_ID=...
export DV_CLIENT_ID=...
export DV_CLIENT_SECRET=...

# 4. Ruleaza pe etape, in aceasta ordine
python3 build/deploy/provisioning.py --etapa optionsets
python3 build/deploy/provisioning.py --etapa entities
python3 build/deploy/provisioning.py --etapa attributes
python3 build/deploy/provisioning.py --etapa relationships
```

Ordinea este obligatorie: coloanele de tip Choice refera seturi globale care trebuie sa
existe, iar relatiile refera tabele care trebuie sa existe.

## Idempotenta si reluare

Scriptul retine ce a creat in `build/deploy/stare.json`. O rulare intrerupta - din cauza
limitei de API, a expirarii tokenului sau a unei erori - se reia cu aceeasi comanda si
continua de unde a ramas.

Pentru a reporni de la zero intr-un mediu curat, se sterge `stare.json`.

## Ce se intampla la erori

Scriptul nu se opreste la prima eroare. Afiseaza tabela si coloana afectata, plus raspunsul
serverului, si continua. La final raporteaza cate elemente s-au creat, cate existau deja si
cate au esuat.

Erorile raman de rezolvat una cate una, dar sunt tipic de trei feluri:

| Tip de eroare | Cauza obisnuita | Rezolvare |
|---|---|---|
| Nume prea lung sau invalid | Un nume logic care depaseste limita cu prefixul aplicat | Se scurteaza in `build/genereaza-model.py` si se regenereaza |
| Interval invalid | O valoare de tip Decimal cu precizie mai mare decat permite tipul | Se corecteaza in model |
| Dependenta lipsa | O relatie catre o tabela care nu s-a creat inca | Se reia etapa anterioara |

## Avertisment onest

**Payloadurile sunt validate structural, nu impotriva unui tenant real.** Nu am putut testa
scriptul contra unui mediu Dataverse. Verificarile facute sunt: unicitatea numelor,
lungimile maxime, coerenta intervalelor, existenta seturilor de optiuni referite si a
tabelelor tinta ale relatiilor.

Dataverse va respinge, cu mare probabilitate, cateva elemente pentru motive care nu se pot
anticipa din afara: rezervari de nume, particularitati de versiune, restrictii de mediu.
Estimarea realista este de **2 pana la 4 cicluri de rulare si corectie**, adica 2-3 zile,
nu o rulare perfecta din prima.

Aceasta este totusi de aproximativ 15 ori mai putin decat crearea manuala a acelorasi
componente in interfata.

## Dupa provizionare

1. Cele 24 de coloane Calculated si Rollup, din `payloaduri/coloane-manuale.json`.
2. Cheile alternative pe codurile de business (22.6): `rd_codproiect` pe proiect,
   `rd_codsap` pe materie prima si client, `rd_codlivrabil` plus proiect pe livrabil.
3. Importul datelor de nomenclator, cu fisierele din `build/import/`.
4. Exportul solutiei, conform pasului 9 din ghidul Valului 0.
