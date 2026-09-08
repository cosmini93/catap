# Sectiunea 20 - Intrebari deschise

Zece intrebari. Numai cele care blocheaza o decizie de constructie. Fiecare are impactul
declarat si o valoare implicita, folosita daca raspunsul intarzie, ca sa nu se opreasca
constructia.

---

**IQ-01. Cine detine mediul de productie si cand se obtine?**

*Ce blocheaza*: RSC-01, cel mai grav risc al proiectului. Constructia intr-un mediu
Developer personal este acceptabila pentru Val 0 si Val 1, dar nu pentru un sistem folosit
de 30 de oameni.

*Ce trebuie decis*: daca IT-ul aloca un mediu de productie Dataverse si pana cand; cine
este proprietarul lui administrativ; cine plateste capacitatea.

*Valoare implicita daca nu vine raspuns*: se continua in Developer pana la finalul Valului
1, cu export dublu (OneDrive si biblioteca SharePoint a companiei), si se escaladeaza
formal catre conducere inainte de Val 2.

---

**IQ-02. Cate licente Power Apps Premium se aproba si pentru cine?**

*Ce blocheaza*: domeniul Valului 2. Daca Achizitiile si Productia nu primesc licente,
modulele M09 si M19 nu au utilizatori si nu are sens sa fie construite in forma
proiectata.

*Ce trebuie decis*: numarul de licente pentru utilizatorii care creeaza si modifica date
(estimat 25-35).

*Valoare implicita*: se construieste pentru 30 de utilizatori. Daca se aproba mai putine,
prioritatea este: R&D complet, apoi Calitate, apoi Achizitii, apoi Productie.

*RASPUNS PARTIAL, Sectiunea 28*: costul este cunoscut - 30 de licente Power Apps Premium
inseamna aproximativ 7 200 USD pe an la pretul de lista. Se pot cumpara etapizat, 10-12
pentru Val 1 si restul la Val 2. Ce ramane deschis este aprobarea, nu cifra.

---

**IQ-03. Cum se rezolva accesul de citire pentru cei ~200 de angajati?**

*Ce blocheaza*: constructia ecranului public (ECR-04). Variantele B si C din 17.1.2.1 se
construiesc diferit si nu se pot schimba usor una in alta.

*Ce trebuie decis*: licenta per aplicatie pentru ecranul public, sau export zilnic intr-o
lista SharePoint.

*Valoare implicita*: se construieste varianta B (aplicatie separata, licenta per
aplicatie), pentru ca varianta C se poate deriva din ea in doua zile, dar nu si invers.

*RASPUNS REVIZUIT, Sectiunea 28.5.6*: aplicatia separata se construieste, ca in
recomandarea initiala, dar **lansarea se face prin varianta C**, cu lista SharePoint,
la cost zero. Motivul: accesul de citire pentru cei 200 costa aproximativ 12 000 USD pe
an, adica mai mult decat licentele intregului departament care lucreaza efectiv in sistem.
Se masoara intai cati oameni deschid ecranul, apoi se cumpara licentele, pe aplicatia
deja construita.

---

**IQ-04. Cine stabileste si revizuieste clasificarea A/B/C a clientilor, si cand?**

*Ce blocheaza*: 20 din cele 100 de puncte ale scorului de prioritate. Fara o clasificare
asumata si actualizata, scorul se contesta la fiecare proiect.

*Ce trebuie decis*: persoana responsabila (Comercial Manager sau Director de vanzari),
frecventa revizuirii, si daca clasificarea existenta in SAP sau in comercial poate fi
preluata ca punct de pornire.

*Valoare implicita*: se preia clasificarea existenta din comercial, se atribuie
responsabilitatea revizuirii Comercial Managerului, cu revizuire anuala in ianuarie.

---

**IQ-05. Cine furnizeaza costul real pe kilogram pentru revizuirea post-implementare, si
in ce format?**

*Ce blocheaza*: doua dintre cele patru componente ale indicelui de sanatate (8.4) si
raportul anual `Ce am invatat` (RAP-15). Fara cost real, revizuirea masoara doar calitatea
si volumul.

*Ce trebuie decis*: daca Controllingul poate furniza costul real pe produs, la 60 si 90 de
zile, si daca poate fi automatizat sau ramane manual.

*Valoare implicita*: se construieste ca introducere manuala, cu camp `Date indisponibile`
si raportare a departamentului care nu a furnizat datele.

---

**IQ-06. Aplicatia interna de planificare poate expune un API pentru sloturile de linie?**

*Ce blocheaza*: gradul de realism al slotului de testare propus si al cozii pe linie. Fara
integrare, coada pe linie din R&D este o estimare paralela cu planificarea reala, si cele
doua vor diverge.

*Ce trebuie decis*: daca aplicatia (variantele HTML si API Python) poate expune, chiar si
read-only, ocuparea liniilor pe schimburi.

*Valoare implicita*: fara integrare in Valurile 0-3. Coada pe linie se calculeaza doar din
proiectele R&D, iar slotul ramane o estimare negociabila comunicata manual planificarii
(A1.2.7.3).

---

**IQ-07. Cine raspunde pentru completarea datelor nutritionale si de alergeni ale celor
~1500 de materii prime?**

*Ce blocheaza*: intreaga Sectiune 9 si generarea etichetelor. Este cel mai mare efort de
introducere de date din tot proiectul si nu poate fi facut de constructor singur.

*Ce trebuie decis*: daca responsabilitatea este a Calitatii, a tehnologilor sau a
Achizitiilor, si daca se aloca timp dedicat pentru primele 150-250 de coduri.

*Valoare implicita*: completare la utilizare (15.2.2), cu prima transa in sarcina
Calitatii pentru materiile prime din proiectele active. Modulul M15 ramane in Val 3, cu
riscul de a aluneca.

---

**IQ-08. Sunt corecte pragurile propuse pentru randament si rebut la productia 0?**

*Ce blocheaza*: regula automata de decizie de la productia 0 (7.3.3, 7.9). Un prag gresit
face ca fie totul sa treaca, fie nimic.

*Ce trebuie decis*: confirmarea sau corectarea pragurilor: rebut sub 5% la laminate si sub
3% la depuse; randament peste 92% la laminate si peste 95% la depuse.

*Valoare implicita*: se folosesc valorile propuse, marcate ca PROPUNERE, si se
recalibreaza dupa primele 10 productii 0, cu datele reale.

---

**IQ-09. Cine sunt evaluatorii panelului senzorial si sunt disponibili?**

*Ce blocheaza*: grila din 6.5 cere 3 evaluatori pentru deciziile de continuare si 5 pentru
evaluarea finala. Daca nu exista oameni disponibili, grila ramane teoretica si evaluarea
se face tot de o singura persoana.

*Ce trebuie decis*: lista nominala a panelului, cu inlocuitori, si acordul sefilor lor
pentru timpul alocat.

*Valoare implicita*: se construieste pentru numarul de evaluatori din 6.5.3, dar sistemul
accepta si evaluari cu un singur evaluator, marcate explicit ca `Evaluare individuala` si
raportate ca atare.

---

**IQ-10. Care este disponibilitatea reala de timp a constructorului, in zile pe
saptamana?**

*Ce blocheaza*: intreg calendarul din Sectiunea 16. La 1.5 zile pe saptamana, cele 78-98
de zile-om inseamna peste un an, nu 6-7 luni (16.6.1).

*Ce trebuie decis*: un angajament explicit, asumat de conducere, pentru perioadele de
constructie concentrata din Valurile 0 si 1.

*Valoare implicita*: se planifica pe 1.5 zile pe saptamana si se comunica termenele
corespunzatoare, mai lungi. Este mai bine decat sa se promita 6 luni si sa se livreze in
14.

---

## Ce nu este intrebare deschisa

Urmatoarele nu apar mai sus pentru ca raspunsul este deja dat in blueprint si nu se
renegociaza: alegerea Dataverse; cele doua tipuri de aplicatii; pastrarea documentelor in
SharePoint; interdictia de scriere in SAP; formatul codului de proiect; regula ca orice
diferenta de gramaj, dimensiune sau reteta inseamna proiect nou; faptul ca cele 30 de bife
devin inregistrari de livrabil.
