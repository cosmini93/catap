# Sectiunea 17 - Trecerea in productie

## 17.1 Ce se cere concret de la IT

Lista de mai jos se transmite ca atare, ca cerere formala. Este scrisa astfel incat sa
poata fi evaluata de un IT care nu cunoaste Power Platform.

### 17.1.1 Medii

| Cerinta | Detaliu | Motiv |
|---|---|---|
| Mediu de productie Dataverse | Tip `Production`, cu baza de date Dataverse, in regiunea tenantului (Europa) | Aici traieste solutia finala |
| Mediu de test Dataverse | Tip `Sandbox`, cu baza de date, copie a productiei | Testarea importurilor inainte de productie |
| Mediul Developer existent | Ramane, ca mediu de constructie | Constructia continua dupa punerea in functiune |
| Grup de securitate pe mediu | Un grup Entra ID care controleaza cine are acces la mediul de productie | Fara el, toti utilizatorii tenantului apar in mediu |

17.1.1.1 Capacitate necesara, estimata pentru 3 ani de functionare:

| Resursa | Estimare | Baza de calcul |
|---|---|---|
| Dataverse Database | 3-5 GB | ~500 de proiecte pe an x ~2000 de inregistrari copil x ~2 KB, plus audit |
| Dataverse File | sub 1 GB | Numai imaginile din masuratori si evaluari; documentele stau in SharePoint |
| Dataverse Log (audit) | 2-4 GB | Auditul pe tabelele critice; vezi FLX-20 pentru arhivare |
| SharePoint | 50-150 GB | ~30 de fisiere pe proiect, medie 3 MB, plus versiuni |

17.1.1.2 NOTA: capacitatea de Log Dataverse este cea care creste cel mai imprevizibil si
este cea mai scumpa pe gigabyte. Se monitorizeaza lunar in primul an. FLX-20 (arhivarea in
SharePoint) exista tocmai pentru a permite scaderea retentiei de audit in Dataverse fara
pierderea informatiei.

### 17.1.2 Licente

| Rol | Licenta necesara | Numar estimat |
|---|---|---|
| Constructor (Head of R&D) | Power Apps Premium (per user) sau licenta care include Dataverse si conectori premium | 1 |
| Utilizatori care creeaza si modifica date (R&D, Achizitii, Calitate, Planificare, Productie, KAM) | Power Apps Premium (per user) | 25-35 |
| Cititori (restul companiei, ecranul public) | Vezi 17.1.2.1 | ~200 |
| Power Automate | Inclus in Power Apps Premium pentru fluxurile din contextul aplicatiei | - |
| Power BI | Power BI Pro pentru cei care publica si consuma rapoarte | 5-8 |

17.1.2.1 Accesul de citire pentru toata compania este punctul de decizie cel mai
costisitor. Trei variante, in ordinea recomandarii:

| Varianta | Cum | Cost | Observatii |
|---|---|---|---|
| A. Licenta per utilizator pentru toti | Power Apps Premium pentru ~200 de persoane | Cel mai mare | Nejustificabil pentru citire |
| B. Plan per aplicatie (per app) pentru ecranul public | O licenta ieftina, limitata la o singura aplicatie | Mediu | Recomandat; ecranul public este o aplicatie separata tocmai pentru asta |
| C. Publicarea statusului intr-o pagina SharePoint | Un flux exporta zilnic o lista de status intr-o lista SharePoint, vizibila tuturor | Zero suplimentar | Nu este in timp real; pierde filtrele; acceptabil daca varianta B este refuzata |

17.1.2.2 Se cere IT-ului o decizie explicita intre B si C **inainte de Val 2**, pentru ca
ECR-04 se construieste diferit in cele doua cazuri. Aceasta este si intrebarea deschisa
IQ-03 din Sectiunea 20.

### 17.1.3 Alte cerinte

| Cerinta | Detaliu |
|---|---|
| Site SharePoint dedicat | Site de tip Team, cu biblioteca `PRODUSE IN DEZVOLTARE` si biblioteca `Sabloane` |
| Politica DLP | Politica dedicata mediilor R&D, care permite Microsoft 365, Dataverse, Approvals si Teams, si blocheaza restul |
| Conturi de serviciu | Un cont de serviciu pentru conexiunile fluxurilor, cu licenta proprie, ca fluxurile sa nu depinda de contul unei persoane |
| Grupuri Entra ID | Sase grupuri, corespunzatoare echipelor din 11.1.2, intretinute de IT sau de HR |
| Backup si restaurare | Confirmarea politicii native de backup Dataverse (7 zile pentru Production) si a procedurii de restaurare |
| Mediu de test reimprospatat | Posibilitatea de a copia productia in sandbox, la cerere |

17.1.3.1 Contul de serviciu este cerinta cea mai des omisa si cea mai costisitoare cand
lipseste: daca fluxurile ruleaza pe contul personal al constructorului, plecarea sau
schimbarea parolei acelei persoane opreste intreaga automatizare. Se cere de la inceput.

## 17.2 Exportul si importul solutiei

### 17.2.1 Regulile de baza

| Regula | Motiv |
|---|---|
| Se lucreaza intr-o singura Solution, `RDSuitaDigitala` | O a doua solutie creeaza dependente greu de urmarit |
| Se exporta si `managed`, si `unmanaged` | Unmanaged pentru arhiva si pentru un eventual mediu de constructie nou; managed pentru test si productie |
| In test si productie se importa **numai managed** | Importul unmanaged in productie face imposibila dezinstalarea si stergerea componentelor |
| Versionarea solutiei | `major.minor.build.revision`, incrementat la fiecare export catre test |
| Referinte de conexiune si variabile de mediu | Obligatorii pentru toate fluxurile si conexiunile |
| Datele de nomenclator | Nu se exporta cu solutia; se muta separat, cu Configuration Migration Tool sau prin import Excel |

17.2.1.1 NOTA de platforma: componentele nesolutionate (vizualizari personale, aplicatii
canvas create in afara solutiei, fluxuri create direct in mediu) nu pleaca la export si
sunt cea mai frecventa cauza de "merge la mine, nu merge in productie". Regula: nimic nu
se creeaza in afara solutiei, de la prima zi.

### 17.2.2 Procedura de promovare

| Pas | Actiune | Mediu |
|---|---|---|
| 1 | Se incrementeaza versiunea solutiei | Developer |
| 2 | Export managed si unmanaged; se salveaza pe OneDrive cu conventia din 2.0.2 | Developer |
| 3 | Import managed in mediul de test | Test |
| 4 | Se configureaza referintele de conexiune si variabilele de mediu pentru test | Test |
| 5 | Se ruleaza lista de verificare din 17.3 | Test |
| 6 | Se muta datele de nomenclator, daca s-au schimbat | Test |
| 7 | La rezultat curat: import managed in productie | Productie |
| 8 | Se configureaza referintele de conexiune si variabilele de mediu pentru productie | Productie |
| 9 | Se activeaza fluxurile, in ordinea din 12.2 | Productie |
| 10 | Se verifica pe un proiect real, de la SCP la generarea folderului | Productie |
| 11 | Se noteaza in registrul de versiuni ce s-a livrat si cand | - |

17.2.2.1 Pasul 3 nu se sare niciodata, nici pentru "o modificare mica". Cele mai multe
incidente de productie in Power Platform vin din modificari considerate prea mici pentru a
merita un test.

### 17.2.3 Registrul de versiuni

Se tine un fisier simplu, in biblioteca `Sabloane`, cu: versiunea, data, ce contine, cine
a facut importul, si daca a fost nevoie de actiuni manuale dupa import. Este documentul pe
care il citeste prima data cineva care preia solutia.

## 17.3 Ce se testeaza inainte de punerea in functiune

### 17.3.1 Testare functionala

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 1 | KAM completeaza si trimite un SCP | Solicitarea apare in lista de triaj a Managerului R&D |
| 2 | Manager R&D accepta solicitarea | Se genereaza cod, proiect, folder cu 10 subfoldere, livrabile, etape si termen propus |
| 3 | Manager R&D respinge o solicitare fara motiv | Sistemul nu permite salvarea |
| 4 | Se aloca un tehnolog | Se vede incarcarea lui inainte de alocare; livrabilele lui se reatribuie |
| 5 | Se marcheaza o materie prima ca noua, dupa acceptare | Apar livrabilele conditionate C1, cu termene |
| 6 | Achizitiile schimba un ETA | Termenul propus se recalculeaza; KAM si tehnolog sunt notificati |
| 7 | Se introduc 10 masuratori de greutate pe telefon, offline | Se sincronizeaza la revenirea conexiunii; statistica se calculeaza corect |
| 8 | Se exclude o masuratoare fara motiv | Sistemul nu permite |
| 9 | Se face o evaluare senzoriala cu 3 evaluatori si dezacord de 3 puncte | Criteriul se marcheaza; verdictul nu poate fi `Acceptat` |
| 10 | Se deschide si se inchide un blocaj de 5 zile cu sursa Furnizor | Proiectul trece in `Blocat` si revine; zilele blocate se cumuleaza; T-Total se ajusteaza |
| 11 | Se deschide un blocaj cu sursa Intern R&D | Ceasul nu se opreste |
| 12 | Se incarca un document cu nume conform si unul neconform | Primul primeste metadate automat; al doilea se marcheaza `Neclasificat` si autorul e notificat |
| 13 | Se aproba o ST finala | Documentul se blocheaza; versiunea majora se publica; data aprobarii ajunge in Dataverse |
| 14 | Se incearca inchiderea unui proiect cu livrabile obligatorii nerealizate | Sistemul refuza si listeaza ce lipseste |
| 15 | Se genereaza dosarul TDV | PDF complet, cu toate sectiunile din 5.5.10 |
| 16 | Se schimba datele de alergeni ale unei materii prime folosite intr-o reteta validata | Nu se modifica nimic automat; se genereaza alerta de impact |
| 17 | Se creeaza un proiect-copil | Mosteneste referintele, reteta si legatura cu documentele parintelui |
| 18 | Se completeaza o productie 0 cu o neconformitate HACCP | Decizia `Validat` nu este disponibila |
| 19 | Se ruleaza recalcularea saptamanala a scorului | Benzile se actualizeaza; proiectele cu scor suprascris raman neatinse |
| 20 | Un KAM incearca sa promoveze un al treilea proiect in P1 | Sistemul cere retrogradarea altuia |

### 17.3.2 Testare de securitate

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 21 | Un utilizator cu rol Cititor deschide un proiect | Vede numai cele 9 coloane publice din 11.5.1 |
| 22 | Un KAM incearca sa deschida un antecalcul | Nu are acces |
| 23 | Un tehnolog incearca sa suprascrie un scor de prioritate | Campul nu este editabil |
| 24 | Un utilizator din Productie incearca sa stearga un trial | Nu are drept de stergere |
| 25 | Un utilizator din afara companiei este adaugat la mediu | Grupul de securitate pe mediu il blocheaza |
| 26 | Se verifica ce coloane apar in notificarile trimise de fluxuri | Nicio coloana protejata prin securitate pe coloana |
| 27 | Se incearca exportul in Excel de catre un rol restrans | Exportul respecta securitatea pe coloana |

### 17.3.3 Testare de performanta si volum

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 28 | Se incarca 500 de proiecte si 5000 de livrabile in mediul de test | Vizualizarile se deschid in sub 3 secunde |
| 29 | Biblioteca SharePoint depaseste 5000 de elemente | Vizualizarile filtrate functioneaza (coloane indexate) |
| 30 | Se ruleaza FLX-06 si FLX-10 pe volumul complet | Se termina fara limitare de API |
| 31 | Aplicatia canvas se deschide pe telefonul cel mai vechi din dotare | Sub 10 secunde pana la primul ecran utilizabil |
| 32 | Aplicatia canvas functioneaza in zona cu semnal slab din hala | Introducerea si salvarea locala functioneaza offline |

### 17.3.4 Testare de acceptanta cu utilizatorii

| Nr | Scenariu | Criteriu de trecere |
|---|---|---|
| 33 | Un KAM completeaza un SCP fara instruire, doar cu ecranul in fata | Reuseste in sub 10 minute |
| 34 | Un tehnolog introduce un set complet de masuratori cu manusi | Reuseste fara ajutor |
| 35 | Doua persoane din afara R&D gasesc statusul unui produs pe ecranul public | Sub 15 secunde fiecare |
| 36 | Un sef de tura completeaza checklistul de productie 0 | Reuseste fara ajutor |

17.3.4.1 Testele 33-36 sunt cele care decid daca solutia se foloseste sau nu. Se fac cu
oameni reali, nu cu constructorul care simuleaza. Un test picat aici inseamna reproiectarea
ecranului, nu instruire suplimentara.

## 17.4 Punerea in functiune

| Pas | Cand | Actiune |
|---|---|---|
| 1 | -2 saptamani | Inventarul proiectelor in curs (15.5) |
| 2 | -1 saptamana | Instruire: 2 ore pentru R&D, 1 ora pentru KAM, 30 de minute pentru celelalte roluri |
| 3 | -3 zile | Migrarea nomenclatoarelor si a proiectelor istorice in productie |
| 4 | -1 zi | Migrarea proiectelor in curs, cu confirmarea tehnologilor |
| 5 | Ziua 0 | Taietura neta: proiectele noi se deschid numai in sistem (15.5.4) |
| 6 | Zilele 1-10 | Prezenta zilnica a constructorului langa utilizatori, 30 de minute pe zi |
| 7 | Ziua 30 | Evaluarea criteriilor din 16.2 |

17.4.1 Se alege ca zi 0 o luni din prima jumatate a lunii, in afara varfului de
septembrie-decembrie. Punerea in functiune in sezonul de varf este cea mai sigura cale
catre respingerea solutiei.

## 17.5 Documentarea pentru preluare

Constrangerea din brief: solutia trebuie sa poata fi preluata de altcineva. Concret, se
pastreaza in biblioteca `Sabloane`, actualizate la fiecare val:

| Document | Continut |
|---|---|
| Acest blueprint | Sursa de adevar pentru arhitectura si decizii |
| Registrul de versiuni | Ce s-a livrat, cand, cu ce actiuni manuale |
| Lista fluxurilor | Cod, scop, declansator, conexiuni folosite, variabile de mediu |
| Lista variabilelor de mediu | Nume, tip, valoare in fiecare mediu, ce controleaza |
| Procedura de export si import | Pasii din 17.2.2, cu capturi de ecran |
| Procedura anuala | Resetarea semintei de Autonumber, revizuirea clasificarilor de client, revizuirea ponderilor si a duratelor |
| Lista de verificare de testare | Cele 36 de scenarii din 17.3 |
| Contactele | Cine raspunde pentru fiecare zona de business |

17.5.1 NOTA: documentatia se scrie in timpul constructiei, nu la sfarsit. Un blueprint
actualizat si un registru de versiuni tinut la zi sunt singura diferenta intre o solutie
preluabila si una care moare odata cu plecarea constructorului. Aceasta este si RSC-02 din
Sectiunea 18, riscul cel mai probabil al intregului proiect.
