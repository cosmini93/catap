# Sectiunea 25 - Cunoastere organizationala

Preluat integral din blueprintul Enterprise, capitolul 12. Este singurul domeniu in care
blueprintul de baza nu avea absolut nimic, si probabil cel cu cel mai bun raport
efort-beneficiu din toata sinteza.

## 25.1 Problema

25.1.1 La 130-180 de proiecte pe an, timp de zece ani, compania a rezolvat de mai multe ori
aceleasi probleme. Faina care se comporta altfel iarna, furnizorul de umplutura care
livreaza cu vascozitate variabila, linia care nu tine gramajul sub 45 g, clientul care
respinge orice produs cu ulei de palmier. Toate aceste lucruri sunt stiute. Niciunul nu
este scris.

25.1.2 Consecinta practica: un tehnolog nou repeta greselile facute acum trei ani, iar un
tehnolog care pleaca ia cu el cinci ani de context. Costul nu apare nicaieri in contabilitate,
dar este cel mai mare cost ascuns al departamentului.

25.1.3 Ce **nu** rezolva aceasta sectiune: nu transforma un sistem de evidenta intr-un
sistem de management al cunoasterii prin simpla existenta a unei tabele. Lectiile se scriu
numai daca sunt cerute la momentul potrivit si sunt reutilizate numai daca apar
neintrebate, la momentul potrivit. Ambele mecanisme sunt in 25.2 si 25.4.

## 25.2 Lectii invatate

### 25.2.1 TBL-54 `rd_lectie`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Numar lectie | rd_name | Autonumber | Da | LSN-{AA}-{SEQ:0000} | - | Coloana primara |
| Titlu | rd_titlu | Text (200) | Da | - | Formulat ca afirmatie, nu ca subiect | Vezi 25.2.4 |
| Situatia | rd_situatie | Text Area (2000) | Da | - | Ce s-a intamplat concret | - |
| Cauza radacina | rd_cauzaradacina | Text Area (2000) | Da | - | De ce s-a intamplat | - |
| Lectia | rd_lectie | Text Area (2000) | Da | - | Ce stim acum si nu stiam inainte | - |
| Recomandarea | rd_recomandare | Text Area (2000) | Da | - | Ce sa faca altcineva data viitoare | Partea reutilizabila |
| Actiune preventiva | rd_actiunepreventiva | Text Area (2000) | Nu | - | Ce schimbare de proces ar impiedica repetarea | Poate genera actiune |
| Categorie | rd_categorie | Choice | Da | Reteta / Materie prima / Furnizor / Proces / Echipament / Calitate / Client / Comercial / Cost / Planificare / Ambalaj / Reglementare | - | Choice global CATEGORIELECTIE |
| Severitatea situatiei | rd_severitate | Choice | Da | Minora / Majora / Critica | - | - |
| Nivel de reutilizare | rd_nivelreutilizare | Choice | Da | Proiect / Categorie de produs / Linie / Furnizor / Client / Intreaga companie | Determina cui i se recomanda | Vezi 25.4 |
| Categorie de produs | rd_categorieprodus | Choice | Nu | Foietaj / Aluat dospit / Patiserie cu umplutura / Paine / Toate | Pentru potrivire | - |
| Linie | rd_linie | Lookup (rd_linie) | Nu | - | Referential | - |
| Materie prima | rd_materieprima | Lookup (rd_materieprima) | Nu | - | Referential | - |
| Furnizor | rd_furnizor | Lookup (rd_furnizor) | Nu | - | Referential | - |
| Client | rd_client | Lookup (rd_client) | Nu | - | Referential | - |
| Etichete | rd_etichete | Text (300) | Nu | Cuvinte separate prin `;` | Pentru cautare libera | - |
| Cost potential evitat | rd_costevitat | Currency (2) | Nu | - | Estimare, optionala | Securitate pe coloana |
| Zile potential evitate | rd_zileevitate | Whole Number | Nu | 0 - 365 | Estimare | - |
| Proiect sursa | rd_proiect | Lookup (rd_proiect) | Nu | - | De unde provine | Referential |
| Problema sursa | rd_problema | Lookup (rd_problema) | Nu | - | Referential | - |
| Neconformitate sursa | rd_neconformitate | Lookup (rd_neconformitate) | Nu | - | Val 4 | - |
| Productie 0 sursa | rd_productie0 | Lookup (rd_productie0) | Nu | - | Referential | - |
| Generata automat | rd_generataauto | Yes/No | Da | Implicit Nu | Draft creat de FLX-33 | Vezi 25.2.2 |
| Status | rd_statuslectie | Choice | Da | Draft / In verificare / Aprobata / Respinsa / Arhivata | Numai cele Aprobate se recomanda | - |
| Autor | rd_autor | Lookup (systemuser) | Da | - | - | - |
| Aprobator | rd_aprobator | Lookup (systemuser) | Nu | - | Manager R&D | - |
| Data aprobarii | rd_dataaprobare | Date Only | Nu | - | - | - |
| Numar reutilizari | rd_numarreutilizari | Rollup (Count) | Nu | 0 - 999 | Din rd_utilizarelectie | Vezi 25.3 |
| Data ultimei reutilizari | rd_dataultimareutilizare | Date Only | Nu | - | - | Lectiile nefolosite se revizuiesc |

### 25.2.2 Generarea automata a drafturilor

Nimeni nu se aseaza sa scrie o lectie invatata din proprie initiativa. Sistemul creeaza
**drafturi**, la momentele in care exista material, si cere unei persoane sa le completeze.

| Declansator | Ce se precompleteaza |
|---|---|
| Productie 0 cu decizia `Se repeta` | Proiectul, linia, parametrii care au deviat, problemele deschise |
| Neconformitate critica inchisa | Cauza radacina, actiunea corectiva |
| Aceeasi cauza radacina de 3 ori in 12 luni | Cele trei probleme, cu proiectele lor |
| Abatere de cost peste prag la revizuire | Antecalculul, costul real, componenta care a deviat |
| Iteratie de furnizor respinsa a treia oara pe acelasi proiect | Furnizorul, motivele respingerii |
| Reclamatie critica de client | Reclamatia, produsul, lotul |
| Proiect abandonat dupa etapa de testare | Motivul, faza in care s-a oprit |
| Proiect inchis cu scor de succes sub 70 | Componentele scorului care au tras in jos |

25.2.3 Draftul are status `Draft`, autor = responsabilul proiectului si o actiune generata
automat cu termen de 10 zile lucratoare. **Nu se aproba singur.** O lectie generata automat
si neverificata este zgomot cu aspect de cunoastere.

25.2.4 Regula de formulare a titlului: lectia se scrie ca **afirmatie**, nu ca subiect.
"Faina cu W sub 280 nu tine laminarea la grosimi sub 2 mm" este o lectie. "Probleme cu
faina" este o eticheta de dosar. Regula se pune in ajutorul de camp, unde se citeste.

## 25.3 Urmarirea reutilizarii

### 25.3.1 TBL-55 `rd_utilizarelectie`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | Generata | - | Coloana primara |
| Lectie | rd_lectie | Lookup (rd_lectie) | Da | - | Parental | Cascade All |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Unde s-a folosit | Referential |
| Etapa | rd_etapa | Lookup (rd_etapa) | Nu | - | Referential | - |
| Persoana | rd_persoana | Lookup (systemuser) | Da | - | Cine a folosit-o | - |
| Data | rd_data | Date Only | Da | - | Implicit azi | - |
| Cum a fost folosita | rd_mod | Text Area (1000) | Nu | - | - | - |
| Rezultat | rd_rezultat | Choice | Da | A ajutat / Partial / Nu a ajutat / Prea devreme | - | - |
| Cost evitat estimat | rd_costevitat | Currency (2) | Nu | - | Optional | Securitate pe coloana |
| Zile evitate estimate | rd_zileevitate | Whole Number | Nu | 0 - 365 | Optional | - |
| Risc evitat | rd_riscevitat | Text (300) | Nu | - | - | - |

25.3.2 Inregistrarea se face cu un singur click, din recomandarea afisata pe proiect
(25.4). Daca ar cere completarea unui formular, nimeni nu ar face-o si intreaga sectiune ar
deveni decorativa.

25.3.3 Utilitatea reala a acestei tabele nu este raportarea, ci **selectia**: lectiile
folosite frecvent urca in recomandari, cele nefolosite dupa 18 luni intra in revizuire si
se arhiveaza. Fara acest mecanism, biblioteca de lectii creste la 400 de intrari si devine
nefolosibila, adica exact ca un folder de documente.

## 25.4 Recomandarea lectiilor

### 25.4.1 Principiul

O lectie cautata nu se gaseste. O lectie care apare singura, pe ecranul proiectului, in
momentul in care este relevanta, se citeste.

### 25.4.2 Cand se recomanda

| Moment | Ce se potriveste |
|---|---|
| La acceptarea proiectului | Categoria de produs, clientul, tipul de proiect |
| La alocarea liniei | Linia, plus categoria de produs |
| La adaugarea unei materii prime | Materia prima si furnizorul ei |
| La deschiderea unei fise de testare | Categoria de produs si linia |
| La pregatirea IPN | Linia, plus produsele similare implementate pe ea |
| La aparitia unei probleme | Categoria si cauza probabila |

### 25.4.3 TBL-56 `rd_recomandarelectie`

| Nume coloana | Nume logic | Tip Dataverse | Obligatoriu | Valori / interval | Regula de business | Observatii |
|---|---|---|---|---|---|---|
| Denumire | rd_name | Text (200) | Da | Generata | - | Coloana primara |
| Lectie | rd_lectie | Lookup (rd_lectie) | Da | - | Referential | - |
| Proiect | rd_proiect | Lookup (rd_proiect) | Da | - | Parental | Cascade All |
| Momentul recomandarii | rd_moment | Choice | Da | Acceptare / Alocare linie / Materie prima / Fisa de testare / IPN / Problema | Vezi 25.4.2 | - |
| Scor de potrivire | rd_scorpotrivire | Whole Number | Da | 0 - 100 | Vezi 25.4.4 | - |
| Motivul potrivirii | rd_motivpotrivire | Text (300) | Da | - | "Aceeasi linie si categorie de produs" | Face recomandarea credibila |
| Data recomandarii | rd_datarecomandare | Date and Time | Da | - | - | - |
| Status | rd_statusrecomandare | Choice | Da | Afisata / Acceptata / Aplicata / Respinsa / Ignorata | - | - |
| Motivul respingerii | rd_motivrespingere | Text (300) | Nu | - | Optional, dar util pentru calibrare | - |
| Utilizare generata | rd_utilizare | Lookup (rd_utilizarelectie) | Nu | - | La status Aplicata | - |

### 25.4.4 Scorul de potrivire

```
scor = 0
+ 30  daca categoria de produs coincide
+ 25  daca linia coincide
+ 20  daca materia prima coincide
+ 15  daca furnizorul coincide
+ 10  daca clientul coincide
+ 10  daca severitatea lectiei este Critica
+ min(10, numar_reutilizari x 2)   [lectiile care ajuta urca]
- 15  daca lectia este mai veche de 3 ani si nereutilizata

Se afiseaza maximum 3 recomandari, cu scor peste 40.
```

25.4.5 Plafonul de trei recomandari este deliberat. Zece recomandari relevante inseamna
zero recomandari citite. Pragul de 40 si plafonul de 3 sunt variabile de mediu si se
recalibreaza dupa primele sase luni, urmarind rata de acceptare din `rd_statusrecomandare`.

25.4.6 NOTA: potrivirea este pe reguli, nu pe model de limbaj. Este transparenta,
explicabila si functioneaza de la prima lectie. Un motor semantic peste lectii ar fi mai
bun la 300 de lectii, dar la 15 lectii, cate vor exista in primul an, ar fi doar mai greu
de explicat cand greseste. Trecerea la potrivire semantica este in Anexa A2, cu criteriu
de activare.

## 25.5 Impactul cunoasterii

25.5.1 Nu se creeaza tabela `KnowledgeImpact` din Enterprise. Datele necesare exista deja
in `rd_utilizarelectie`, iar impactul este o agregare, nu o entitate.

25.5.2 Raportul RAP-16 `Impactul cunoasterii`, adaugat la lista din 13.6.1:

| Indicator | Calcul |
|---|---|
| Lectii create in perioada | Count pe `rd_lectie` |
| Lectii aprobate | Count cu status Aprobata |
| Rata de aprobare a drafturilor automate | Aprobate / generate automat |
| Lectii reutilizate cel putin o data | Count distinct pe utilizari |
| Rata de reutilizare | Reutilizate / aprobate |
| Cost total evitat estimat | Suma pe utilizari |
| Zile totale evitate estimate | Suma pe utilizari |
| Top 10 lectii dupa reutilizare | Sortare |
| Lectii nereutilizate de peste 18 luni | Candidate la arhivare |
| Rata de acceptare a recomandarilor | Acceptate / afisate |

25.5.3 Cifrele de cost si zile evitate sunt estimari declarate de oameni, nu masuratori.
Se raporteaza ca atare, cu mentiunea "estimat", si nu se folosesc in justificari
financiare externe. Valoarea lor este comparativa in timp, nu absoluta.

## 25.6 Bibliotecile

25.6.1 Blueprintul Enterprise propune sase biblioteci separate: RootCause, Defect, Failure,
SuccessPattern, BestPractice, Playbook. Se pastreaza doua si se amana patru.

| Biblioteca | Decizie | Motiv |
|---|---|---|
| DefectLibrary | **Exista deja** | TBL-20a, cu 22 de defecte definite in `data/nomenclatoare.json` |
| RootCauseLibrary | **Se adauga**, ca nomenclator | Nomenclator de cauze radacina, folosit in TBL-48. Fara el, cauzele se scriu diferit de fiecare data si detectarea repetarii (25.2.2) nu functioneaza |
| FailureLibrary, SuccessPattern, BestPractice, Playbook | Amanate | Sunt vederi filtrate peste `rd_lectie`, nu entitati noi. Se construiesc ca vizualizari, cand exista suficiente lectii |

25.6.2 `rd_cauzaradacina` devine nomenclator (extindere a TBL-41 `rd_motiv`, cu tipul
`Cauza radacina`), nu tabela noua. Se populeaza initial cu cauzele din biblioteca de
defecte si creste prin utilizare, cu aprobarea Managerului R&D pentru intrari noi.

## 25.7 Fluxuri

| Cod | Flux | Declansator | Val |
|---|---|---|---|
| FLX-33 | Generarea drafturilor de lectii | Cele 8 declansatoare din 25.2.2 | 3 |
| FLX-34 | Potrivirea si afisarea recomandarilor | Cele 6 momente din 25.4.2 | 3 |
| FLX-35 | Revizuirea lectiilor nereutilizate | Programat, semestrial | 3 |

25.7.1 FLX-26 (detectarea cauzelor repetate, din 23.8) alimenteaza FLX-33. Cele doua se
construiesc impreuna.
