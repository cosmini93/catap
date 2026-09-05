# Sectiunea 9 - Alergeni si valori nutritionale

Principiul: se calculeaza din reteta, nu se copiaza din ST-urile furnizorilor. ST-ul
furnizorului este sursa de date pentru **materia prima**; declaratia produsului finit este
rezultatul calculului pe reteta.

## 9.1 Datele necesare la nivel de materie prima

9.1.1 Fara datele de mai jos, complete, materia prima nu poate intra intr-o reteta care
sustine o eticheta. Se valideaza la aprobarea materiei prime de catre Calitate.

| Nr | Data | Camp in TBL-09 | Sursa | Obligatoriu |
|---|---|---|---|---|
| 9.1.1.1 | Alergeni continuti | rd_alergeni | ST furnizor, declaratie de alergeni | Da |
| 9.1.1.2 | Alergeni prezenti ca urme | rd_alergeniurme | Declaratie de contaminare incrucisata a furnizorului | Da |
| 9.1.1.3 | Energie (kcal si kJ / 100 g) | rd_energie | ST furnizor | Da |
| 9.1.1.4 | Grasimi (g / 100 g) | rd_grasimi | ST furnizor | Da |
| 9.1.1.5 | Acizi grasi saturati | rd_saturate | ST furnizor | Da |
| 9.1.1.6 | Glucide | rd_glucide | ST furnizor | Da |
| 9.1.1.7 | Zaharuri | rd_zaharuri | ST furnizor | Da |
| 9.1.1.8 | Fibre | rd_fibre | ST furnizor | Nu (optional pe eticheta) |
| 9.1.1.9 | Proteine | rd_proteine | ST furnizor | Da |
| 9.1.1.10 | Sare | rd_sare | ST furnizor | Da |
| 9.1.1.11 | Umiditate | rd_umiditate | ST furnizor sau determinare interna | Da, pentru calculul pierderii la coacere |
| 9.1.1.12 | Denumirea legala pentru lista de ingrediente | rd_denumirelegala | Reglementare + ST | Da |
| 9.1.1.13 | Ingrediente compuse (daca MP este un compus) | rd_ingredientecompuse | ST furnizor | Da, daca este cazul |
| 9.1.1.14 | Data ST-ului furnizorului | rd_datast | - | Da |
| 9.1.1.15 | Origine | rd_origine | ST furnizor | Nu, doar unde se declara |

9.1.2 Validare de plauzibilitate la salvare: suma grasimi + glucide + fibre + proteine +
sare + umiditate trebuie sa fie intre 95 si 105 g / 100 g. In afara acestui interval,
sistemul avertizeaza - de obicei inseamna o eroare de transcriere din ST.

9.1.3 ST-ul furnizorului mai vechi de 24 de luni marcheaza materia prima cu semnal galben
si o raporteaza in lista `Materii prime cu specificatie expirata`. Este cerinta IFS de
actualizare a specificatiilor de intrare.

9.1.4 Ingredientele compuse (de exemplu un ameliorator care contine faina de malt, enzime
si acid ascorbic) se inregistreaza cu componentele lor, pentru ca lista de ingrediente de
pe eticheta trebuie sa le declare in paranteza, nu sub numele comercial.

## 9.2 Modul de calcul

### 9.2.1 Valori nutritionale

```
Pentru fiecare nutrient N si fiecare linie de reteta i:
  contributie_i(N) = cantitate_i (kg/100 kg) * valoare_i(N) / 100

Valoare in aluat (per 100 g de aluat):
  valoare_aluat(N) = SUMA(contributie_i(N))

Corectie de pierdere la coacere (concentrare prin evaporarea apei):
  factor_randament = masa_produs_finit / masa_aluat        [din trial sau productia 0]
  valoare_finit(N) = valoare_aluat(N) / factor_randament

Exceptie pentru apa si umiditate:
  umiditate_finit = (masa_apa_aluat - apa_evaporata) / masa_produs_finit * 100
```

9.2.1.1 Energia nu se preia ca suma directa, ci se recalculeaza din macronutrienti, cu
factorii legali de conversie: grasimi 9 kcal/g, glucide 4, proteine 4, fibre 2,
polioli 2.4, alcool 7, acizi organici 3. Motiv: sumarea energiilor declarate de furnizori
propaga rotunjirile lor si produce, tipic, o abatere de 3-5% fata de valoarea corecta.

9.2.1.2 Factorul de randament este cel mai delicat element al calculului. Se preia, in
ordinea de preferinta: din productia 0 daca exista; altfel din trialul validat; altfel
din valoarea implicita pe categorie de produs, din nomenclator, marcata explicit ca
estimare. Valorile nutritionale calculate cu factor estimat se marcheaza vizual si nu pot
sustine o eticheta aprobata.

9.2.1.3 Rotunjirea pe eticheta urmeaza regulile din ghidul de aplicare a Reg. 1169/2011:
energia la numar intreg; grasimi, saturate, glucide, zaharuri, fibre si proteine la o
zecimala sub 10 g si la numar intreg peste; sarea la doua zecimale sub 1 g. Rotunjirea se
aplica la afisare, nu la stocare - in baza de date raman valorile complete.

### 9.2.2 Alergeni

```
alergeni_produs = REUNIUNEA( alergeni_continuti(MP_i) ) pentru toate liniile de reteta

urme_produs = REUNIUNEA( urme_declarate(MP_i) )
              + alergeni introdusi de linia de productie (vezi 9.4)
              MINUS alergenii deja continuti (un alergen continut nu se declara si ca urma)
```

9.2.2.1 Calculul alergenilor este o reuniune, nu o suma: nu exista prag sub care un
alergen continut nu se declara. Un gram de faina de grau intr-o tona de produs face
produsul purtator de gluten.

9.2.2.2 Alergenii se propaga si prin ingredientele compuse. Daca un ameliorator contine
faina de malt de orz, alergenul `Cereale cu gluten` se propaga chiar daca eticheta
comerciala a amelioratorului nu il scoate in evidenta.

## 9.3 Declaratia pe eticheta

9.3.1 Lista de ingrediente se genereaza automat, in ordine descrescatoare a cantitatii in
aluat, cu denumirile legale, cu ingredientele compuse in paranteza si cu alergenii
evidentiati tipografic (majuscule sau bold, consecvent pe toata eticheta).

9.3.2 Ordinea se calculeaza pe cantitatile din reteta, la momentul framantarii, nu pe
cele din produsul finit. Apa adaugata se declara daca depaseste 5% din produsul finit.

9.3.3 Textul generat este propunere, nu eticheta finala. Aprobarea ramane la Calitate,
care verifica formularea legala. Sistemul genereaza continutul; responsabilitatea juridica
ramane umana.

9.3.4 NOTA: solutia nu inlocuieste o baza de date de specificatii de alergeni certificata
si nu emite declaratii legale. Genereaza propunerea din datele introduse; corectitudinea
datelor de intrare este responsabilitatea celui care le introduce, iar acest lucru se
declara explicit in procedura.

## 9.4 Contaminarea incrucisata si urmele

9.4.1 Urmele au trei surse, tratate distinct:

| Sursa | Cum se determina | Unde se stocheaza |
|---|---|---|
| Urme declarate de furnizor pentru materia prima | Din declaratia furnizorului | rd_materieprima.rd_alergeniurme |
| Urme din linia de productie (produse anterioare pe aceeasi linie) | Din analiza de linie a Calitatii | Camp `rd_alergeniilinie` pe TBL-36 |
| Urme din amplasament (praf de faina, manipulare comuna) | Din evaluarea de risc a amplasamentului | Parametru global pe amplasament |

9.4.2 Declaratia `Poate contine` se genereaza din reuniunea celor trei, minus alergenii
deja declarati ca fiind continuti. Este supusa aprobarii Calitatii si nu se genereaza
automat pe eticheta fara aceasta aprobare.

9.4.3 PROPUNERE: declaratia de urme se face numai dupa o evaluare de risc documentata, nu
preventiv. Motiv: declararea defensiva a tuturor celor 14 alergeni ca posibile urme
inchide accesul la clienti si contrazice practica IFS, care cere ca declaratia sa fie
justificata de un risc real, evaluat, si gestionata prin curatare si secventiere, nu prin
text pe ambalaj.

9.4.4 Matricea de secventiere pe linie: pentru fiecare linie se retine ce alergeni au fost
prelucrati si ce protocol de curatare exista intre sortimente. Cand un produs nou intra pe
o linie, sistemul semnaleaza ce alergeni ar putea aparea ca urme si cere decizia
Calitatii, in cadrul livrabilului LIV-34 (plan HACCP).

## 9.5 Recalcularea automata

9.5.1 FLX-13 recalculeaza alergenii si valorile nutritionale, in urmatoarele situatii:

| Declansator | Ce se recalculeaza | Ce se notifica |
|---|---|---|
| Se adauga, se modifica sau se sterge o linie de reteta | Versiunea de reteta afectata | Tehnologul |
| Se modifica datele nutritionale sau de alergeni ale unei materii prime din catalog | Toate versiunile de reteta nevalidate care o folosesc | Tehnologii proiectelor afectate |
| Idem, pe o materie prima folosita intr-o reteta **validata** | Nimic automat: se genereaza o alerta de impact | Calitate si Head of R&D, vezi 9.5.2 |
| Se schimba factorul de randament (productie 0 finalizata) | Versiunea de reteta a produsului | Tehnologul |
| Se schimba furnizorul unei materii prime | Se compara alergenii vechi cu cei noi | Calitate, daca difera |

9.5.2 Regula critica: o reteta validata nu se recalculeaza tacit. Daca datele unei
materii prime se schimba dupa validare, sistemul nu modifica valorile de pe eticheta
aprobata; genereaza o alerta de impact care listeaza toate produsele afectate si cere o
decizie explicita: reteta noua, eticheta noua, sau confirmarea ca schimbarea nu afecteaza
declaratia. Recalcularea automata a unei etichete deja tiparite ar face imposibila
reconstituirea a ceea ce era declarat pe produsul livrat la o data din trecut.

9.5.3 Alerta de impact este cel mai valoros mecanism din aceasta sectiune: la schimbarea
unui furnizor de ameliorator care introduce faina de malt de orz, sistemul spune imediat
care dintre cele 400 de produse din portofoliu isi schimba declaratia de alergeni. Astazi
raspunsul la aceasta intrebare cere zile de munca manuala.

9.5.4 Fiecare recalculare scrie `rd_datacalcul` pe versiunea de reteta. O versiune al carei
calcul este mai vechi decat ultima modificare a unei materii prime componente se
marcheaza `Calcul invechit` si nu poate sustine aprobarea unei etichete.

## 9.6 Ce se afiseaza in aplicatie

9.6.1 Pe formularul versiunii de reteta, o fila `Alergeni si nutritionale` cu: tabelul
nutritional calculat pe 100 g de produs finit; lista alergenilor continuti, cu materia
prima care ii aduce pe fiecare (trasabilitatea alergenului); lista urmelor, cu sursa;
factorul de randament folosit si de unde provine; data ultimului calcul.

9.6.2 Trasabilitatea alergenului - "de ce apare soia in acest produs" - se raspunde cu un
click, pana la linia de reteta si materia prima care il introduce. Este intrebarea cea mai
frecventa la audit si la reclamatie.

9.6.3 Un raport transversal `Portofoliu pe alergeni`, care raspunde la intrebarea inversa:
care produse contin un anumit alergen. Necesar la orice cerinta de client care exclude un
alergen, si la orice retragere de produs.
