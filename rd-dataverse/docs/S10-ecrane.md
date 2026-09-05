# Sectiunea 10 - Ecranele aplicatiilor

Doua aplicatii: `R&D Birou` (model-driven) si `R&D Linie` (canvas, mobil). Regula de
departajare: daca activitatea se face stand jos, cu tastatura, este model-driven; daca se
face in picioare, cu manusi, este canvas.

## 10.1 Aplicatia model-driven `R&D Birou`

### 10.1.1 Harta de site

| Grup | Element | Tabela / tip | Cine il foloseste |
|---|---|---|---|
| **Lucrul meu** | Proiectele mele | rd_proiect, vizualizare filtrata | Tehnolog |
| | Livrabilele mele scadente | rd_livrabil | Toti |
| | Solicitarile mele | rd_solicitare | KAM |
| | Aprobarile mele | Vizualizare de sarcini | Manager R&D, Calitate |
| **Solicitari** | Solicitari in triaj | rd_solicitare | Manager R&D |
| | Toate solicitarile | rd_solicitare | KAM, Manager R&D |
| | Solicitari amanate | rd_solicitare | Manager R&D |
| **Proiecte** | Proiecte active | rd_proiect | Toti |
| | Coada pe prioritate | rd_proiect, grupat pe banda | Manager R&D, comercial |
| | Coada pe linie | rd_proiect, grupat pe linie | Manager R&D, Planificare |
| | Proiecte blocate | rd_proiect | Manager R&D |
| | Proiecte in intarziere | rd_proiect | Manager R&D, Head of R&D |
| | Arhiva (respinse, abandonate) | rd_proiect | Toti |
| **Executie** | Fise de testare | rd_fisatestare | Tehnolog |
| | Trialuri | rd_trial | Tehnolog |
| | Evaluari senzoriale | rd_evaluaresenzoriala | Tehnolog |
| | Retete si versiuni | rd_reteta | Tehnolog |
| | Antecalcule | rd_antecalcul | Tehnolog, Manager R&D |
| **Materii prime** | MP de proiect in asteptare | rd_mpproiect | Achizitii, Tehnolog |
| | Catalog de materii prime | rd_materieprima | Toti |
| | Furnizori | rd_furnizor | Achizitii, Calitate |
| | Iteratii de furnizor | rd_iteratiefurnizor | Achizitii |
| | MP cu specificatie expirata | rd_materieprima | Calitate |
| **Mostre** | Cereri de mostra | rd_ceremostra | Suport R&D |
| | Livrari in curs | rd_miscaremostra | Suport R&D |
| **Implementare** | IPN in pregatire | rd_implementare | Tehnolog, Productie |
| | Productii 0 | rd_productie0 | Tehnolog, Productie |
| | Revizuiri scadente | rd_revizuire | Manager R&D |
| **Specificatii** | Specificatii tehnice | rd_specificatie | Calitate |
| | SDP | rd_sdp | Calitate, Productie |
| | Etichete | rd_eticheta | Suport R&D, Calitate |
| **Tablouri de bord** | Tablou operational R&D | Dashboard | Manager R&D |
| | Incarcare tehnologi | Dashboard | Manager R&D |
| | Status public | Dashboard | Toata compania |
| | Indicatori | Dashboard | Head of R&D |
| **Configurare** | Sabloane de livrabile | rd_sablonlivrabil | Head of R&D |
| | Sabloane de etape | rd_sablonetapa | Head of R&D |
| | Linii de productie | rd_linie | Head of R&D |
| | Clienti | rd_client | Head of R&D, comercial |
| | Profiluri de tehnolog | rd_profiltehnolog | Head of R&D |
| | Criterii senzoriale | rd_criteriusenzorial | Head of R&D |
| | Motive si nomenclatoare | rd_motiv, rd_tipdocument | Head of R&D |
| | Parametri de prioritizare | Setari de mediu | Head of R&D |

### 10.1.2 ECR-01 Formularul de proiect

Formularul principal, cu antet permanent vizibil si file. Antetul (maximum 5 campuri,
limita platformei): cod proiect, status, tehnolog, termen negociat, banda de prioritate.

| Fila | Continut | Note |
|---|---|---|
| Sinteza | Client, produs, tip, linie, gramaj, volum, referinta, cele trei termene, urmatorul livrabil si cine il datoreaza, procentul de livrabile realizate, zilele blocate | Ecranul pe care il vede toata lumea |
| Livrabile | Subgrila cu livrabilele aplicabile, grupate pe faza, cu status colorat, termen si responsabil | Editare rapida in grila |
| Etape | Subgrila cu etapele, planificat fata de real, cu bara vizuala | - |
| Materii prime | Subgrila MP de proiect, cu status de ciclu, ETA si semnal de intarziere | Achizitii lucreaza aici |
| Testare | Fise de testare, trialuri, sinteza statistica a ultimului trial | - |
| Senzorial | Evaluari, scor ponderat, verdict, comparatie cu referinta | - |
| Reteta si cost | Versiunea curenta de reteta, antecalculul aprobat, marja | - |
| Specificatii | ST-uri, SDP, etichete, cu status si versiune | Calitate lucreaza aici |
| Implementare | IPN, conditii, productie 0, decizie | - |
| Documente | Controlul de documente SharePoint, cu arborele de foldere | Integrare nativa |
| Blocaje | Subgrila de blocaje, cu impactul cumulat | - |
| Istoric | Audit history si cronologia proiectului | Pentru audit |

10.1.2.1 Butoane pe bara de comenzi: `Accepta proiectul` (genereaza cod, folder,
livrabile, etape, termen propus), `Creeaza proiect-copil`, `Adauga blocaj`,
`Genereaza dosar TDV`, `Genereaza document` (alege sablonul), `Recalculeaza termenul`,
`Reatribuie tehnologul`.

### 10.1.3 ECR-02 Ecranul de triaj

Vizualizare de solicitari in status `Trimisa`, cu formular lateral care arata tot SCP-ul
pe un ecran, fara derulare. Trei butoane mari: Accepta, Respinge, Amana. Fiecare deschide
un dialog care cere motivul (obligatoriu la respingere si amanare) si, la acceptare,
propune tehnologul si termenul calculate de sistem, cu posibilitatea de a le schimba.

10.1.3.1 In dialogul de acceptare se afiseaza, langa fiecare tehnolog propus: numarul de
proiecte active, cate sunt P1, gradul de incarcare cu semnal color, si specializarea.
Aceasta este cerinta din 4.2: la alocare, managerul vede incarcarea.

### 10.1.4 ECR-03 Tabloul de bord operational R&D

| Componenta | Continut |
|---|---|
| Proiecte pe status | Grafic de bare, click pentru drill-down |
| Coada pe banda de prioritate | P1-P4, cu numarul si volumul cumulat |
| Incarcarea pe tehnolog | Bare orizontale cu prag, colorate verde / galben / rosu |
| Coada pe linie | Cele 9 linii, cu numarul de proiecte si primul slot liber estimat |
| Livrabile scadente in 7 zile | Lista, cu responsabil |
| Livrabile depasite | Lista, sortata dupa zile de intarziere |
| Proiecte blocate | Cu sursa blocajului si zilele cumulate |
| Materii prime cu ETA depasit | Lista, cu furnizorul |

### 10.1.5 ECR-04 Ecranul public de status

Cerinta: vizibil intregii companii, read-only, lizibil de oricine, fara instruire.

10.1.5.1 Un singur ecran, cu o singura lista si patru filtre mari (client, linie,
tehnolog, status). Coloanele: cod proiect, produs, client, status cu pastila colorata,
termen catre client, responsabil, urmatorul pas. Fara jargon: statusurile se afiseaza cu
denumirile din 2.2.1, care sunt deja in limbaj natural.

10.1.5.2 Sus, patru numere mari: proiecte active, proiecte finalizate luna aceasta,
proiecte in intarziere, proiecte blocate. Fara grafice complicate.

10.1.5.3 Regula de proiectare: cineva din productie sau din financiar trebuie sa poata
raspunde la intrebarea "unde este produsul X pentru clientul Y" in mai putin de 15
secunde, fara sa fi vazut vreodata aplicatia. Se testeaza cu doi oameni din afara R&D
inainte de publicare (criteriu de acceptanta CA-42).

10.1.5.4 NOTA: ecranul public este o aplicatie model-driven separata, cu un singur tabel
si un rol de securitate de citire. Nu se da acces la aplicatia principala cu drepturi
reduse - riscul de a expune accidental costuri si marje este prea mare.

### 10.1.6 ECR-05 Ecranul de prioritizare

Lista proiectelor cu scorul detaliat pe componente (volum, client, termen, efort, risc
MP, reutilizare), banda rezultata, si butonul `Suprascrie scorul` disponibil doar rolului
de manager operational / vanzari. Suprascrierea deschide un dialog care cere scorul nou
si motivul, si afiseaza bugetul de urgenta consumat de KAM-ul respectiv.

### 10.1.7 Alte ecrane model-driven

| Cod | Ecran | Continut |
|---|---|---|
| ECR-06 | Formular de solicitare (SCP) | Cele 10 sectiuni din 5.5.1, in trei file |
| ECR-07 | Formular de materie prima de proiect | Ciclul MP cu bara de progres pe cele 11 statusuri, campurile de Achizitii separate vizual |
| ECR-08 | Formular de antecalcul | Liniile de cost in grila editabila, cu totalul si marja recalculate live |
| ECR-09 | Formular de versiune de reteta | Liniile de reteta cu totalul de 100 kg validat, plus fila de alergeni si nutritionale |
| ECR-10 | Formular de revizuire post-implementare | Campurile automate precompletate, cele manuale grupate pe furnizorul de date |

## 10.2 Aplicatia canvas `R&D Linie`

### 10.2.1 Principii de proiectare pentru hala

| Principiu | Aplicare concreta |
|---|---|
| Tinta de atins cu manusi | Butoane de minimum 64 x 64 px, spatiere de minimum 12 px |
| Contrast ridicat | Text de minimum 18 px, contrast peste 7:1, fara gri pe gri |
| Minim de tastare | Numere din tastatura numerica mare; alegeri din butoane, nu din liste derulante |
| Conexiune slaba | Colectie locala, salvare in coada, sincronizare cand revine semnalul |
| O mana libera | Toate actiunile principale in treimea de jos a ecranului |
| Fara derulare la introducere | Un ecran = o intrebare sau un set scurt |
| Confirmare vizibila | Dupa salvare, confirmare mare, verde, 2 secunde |

10.2.1.1 Modul offline: aplicatia foloseste `SaveData` / `LoadData` pentru colectiile de
masuratori si pentru contextul proiectului. La pornire incarca proiectele active ale
utilizatorului si nomenclatoarele necesare. Fiecare salvare merge intr-o coada locala; un
indicator permanent arata cate inregistrari asteapta sincronizarea.

10.2.1.2 NOTA de platforma: Power Apps canvas nu poate crea offline inregistrari care au
nevoie de un ID generat de server (Autonumber). Din acest motiv, trialul si evaluarea se
creeaza online, in birou sau la intrarea in hala, iar in offline se adauga doar copii
(masuratori, scoruri, inregistrari de productie 0) la inregistrari care exista deja.
Aceasta constrangere trebuie respectata in proiectarea ecranelor, altfel sincronizarea
esueaza tacit.

### 10.2.2 ECR-11 Masuratori la linie

| Ecran | Continut | Actiuni |
|---|---|---|
| 11.1 Selectie | Lista proiectelor active ale utilizatorului, cu cod si produs, cautare rapida | Alege proiectul |
| 11.2 Selectie trial | Trialurile deschise; buton mare `Trial nou` | Alege sau creeaza |
| 11.3 Alege ce masor | Sase butoane mari: Greutate, Dimensiuni, Aspect, Alveolare, Miros, Gust | - |
| 11.4 Introducere numerica | Numarul bucatii afisat mare; tastatura numerica; tinta si toleranta afisate deasupra; culoare verde / rosu instantaneu; contor "bucata 3 din 10" | Salveaza si urmatoarea; Poza; Inapoi |
| 11.5 Introducere calitativa | Trei butoane: Conform, Minor neconform, Neconform; camp de observatie optional | Salveaza; Poza |
| 11.6 Sinteza | Media, abaterea standard, min, max, conformitatea, cu semnal color; lista valorilor, cu cele semnalate ca posibil aberante marcate | Exclude o valoare (cere motiv); Finalizeaza |

10.2.2.1 Ecranul 11.4 este cel mai folosit din toata solutia. Fluxul optim: se citeste
valoarea de pe cantar, se tasteaza, se apasa un singur buton, se trece automat la bucata
urmatoare. Trei atingeri pe bucata, nu mai mult.

### 10.2.3 ECR-12 Evaluare senzoriala

| Ecran | Continut |
|---|---|
| 12.1 Selectie | Proiect si trial; daca exista referinta, se anunta ca evaluarea este comparativa |
| 12.2 Instructiuni | Conditiile de degustare, codificarea probelor |
| 12.3 Criteriu | Un criteriu pe ecran: denumirea mare, ancorele pentru 1, 3 si 5 afisate ca text scurt, cinci butoane mari de scor; camp de comentariu care apare automat la scor 1 sau 2 |
| 12.4 Comparativ | Acelasi criteriu, aplicat referintei, imediat dupa; cele doua scoruri raman vizibile |
| 12.5 Defecte | Lista de defecte bifabile, grupate, cu severitate si procent |
| 12.6 Sinteza | Scor ponderat, comparatia cu referinta, verdictul propus de sistem, camp de actiuni |

10.2.3.1 Ancorele descriptive se afiseaza pe ecran, la fiecare criteriu. Este singura
modalitate prin care grila din 6.5 functioneaza in practica: un evaluator nu retine 17
seturi de ancore, dar le citeste in doua secunde daca sunt in fata lui.

### 10.2.4 ECR-13 Receptie de mostra

| Ecran | Continut |
|---|---|
| 13.1 Scanare sau selectie | Cerere de mostra din lista celor asteptate; scanare de cod de bare de pe AWB daca exista |
| 13.2 Verificare | Cantitate primita, temperatura la receptie (obligatorie pentru congelat), stare a ambalajului |
| 13.3 Conformitate | Conform / Neconform, cu motiv si poza obligatorie la neconform |
| 13.4 Confirmare | Salvare, cu actualizarea automata a statusului MP si notificarea tehnologului |

### 10.2.5 ECR-14 Checklist de productie 0

| Ecran | Continut |
|---|---|
| 14.1 Selectie | Productia 0 planificata pentru azi, pe linia utilizatorului |
| 14.2 Conditii IPN | Cele 13 conditii din 5.5.8, ca lista bifabila; nu se poate porni pana nu sunt toate bifate sau derogate cu motiv |
| 14.3 Cantitati | Aluat introdus pe sarje, bucati obtinute; tastatura numerica |
| 14.4 Parametri | Pe faze: valoarea specificata afisata, camp pentru valoarea reala, semnal automat de abatere |
| 14.5 Rebut | Cantitate si cauza din cele 14 predefinite, ca butoane; se pot adauga mai multe inregistrari |
| 14.6 Gramaj la ambalare | Ca ECR-11, cu esantion de 20 |
| 14.7 HACCP | Punctele critice, cu valoarea limita afisata, valoarea masurata si conform da / nu |
| 14.8 Probleme | Descriere, poza, actiune imediata, responsabil |
| 14.9 Sinteza si decizie | Randament, rebut pe cauze, abateri, conformitate HACCP; propunerea de decizie a sistemului; decizia se ia numai online, de Managerul R&D |

10.2.5.1 Ecranele 14.3 - 14.8 functioneaza offline. Ecranul 14.9 cere conexiune, pentru
ca decizia declanseaza fluxuri si nu poate ramane in coada locala.

### 10.2.6 ECR-15 Consultare rapida

Un ecran de cautare pentru cine este in hala si vrea doar sa vada: cauta dupa cod de
proiect, produs sau client, si afiseaza statusul, tehnologul, urmatorul pas si termenul.
Este versiunea mobila a ecranului public.

## 10.3 Ce nu se pune in canvas

10.3.1 Nu se pun in aplicatia mobila: triajul, alocarea, antecalculul, editarea retetei,
aprobarile de specificatii, configurarea. Acestea cer context si atentie, iar un ecran de
telefon garanteaza greseli.

10.3.2 NOTA: exista presiunea previzibila de a face "totul in canvas, ca e mai frumos".
Se rezista. Aplicatia model-driven da gratuit ceea ce in canvas ar cere saptamani de
lucru si intretinere permanenta: vizualizari filtrabile, cautare avansata, export in
Excel, audit, securitate pe coloana, formulare responsive. Canvas se foloseste exact
acolo unde model-driven nu poate: hala, manusi, poze, offline.
