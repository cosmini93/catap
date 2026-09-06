# Sectiunea 18 - Riscuri

Probabilitate si impact pe scala Mica / Medie / Mare. Riscurile sunt ordonate dupa
produsul celor doua, descrescator.

## 18.1 Registrul de riscuri

| Cod | Risc | Prob. | Impact | Masura |
|---|---|---|---|---|
| RSC-01 | **Mediul Developer**: solutia se construieste intr-un mediu personal, legat de licenta si de contul unei persoane. Mediul Developer poate fi dezactivat automat dupa o perioada de inactivitate, iar la plecarea persoanei dispare impreuna cu contul | Mare | Mare | Export saptamanal, managed si unmanaged, pe OneDrive **si** intr-o biblioteca SharePoint a companiei, nu doar pe OneDrive personal. Trecerea in mediu de productie real cel tarziu dupa Val 2, nu dupa Val 3. Cerere formala catre IT pentru mediu de productie inca din Val 0, chiar daca se foloseste mai tarziu |
| RSC-02 | **Dependenta de o singura persoana**: intreaga solutie este construita, cunoscuta si intretinuta de Head of R&D. Fara el, nimeni nu stie de ce o regula este cum este si cum se face o modificare | Mare | Mare | Blueprintul acesta, tinut la zi, este masura principala. In plus: registrul de versiuni; conturi de serviciu pentru fluxuri (17.1.3.1); un al doilea utilizator cu rol RD Administrator, instruit pe nomenclatoare si sabloane; documentarea in timpul constructiei, nu dupa |
| RSC-03 | **Rezistenta la schimbare a utilizatorilor**: tehnologii revin la Excel, mai ales sub presiune de timp; se creeaza evidenta paralela | Mare | Mare | Taietura neta la punerea in functiune (15.5.4); prezenta zilnica in primele 10 zile; ecrane cu numar minim de campuri; livrarea in Val 1 a ceea ce doare cel mai tare azi (livrabile si termene), nu a ceea ce este mai spectaculos; masurarea explicita a criteriului "centralizatorul Excel nu se mai actualizeaza" |
| RSC-04 | **Adoptarea SCP-ului de catre KAM**: KAM-ii continua sa trimita cereri pe mail, iar suportul R&D le introduce; SCP-ul in aplicatie ramane o formalitate | Mare | Medie | Varianta de rezerva ramane, dar se marcheaza explicit ca `Mail preluat de suport R&D` si se raporteaza lunar pe KAM (RAP-05); formularul SCP se proiecteaza sa se completeze in sub 10 minute (test 33 din 17.3.4); triajul se face numai pe SCP-uri din sistem, deci un mail nu produce niciodata un cod de proiect |
| RSC-05 | **Datele de materie prima incomplete**: catalogul nu are date nutritionale si de alergeni, deci Sectiunea 9 nu functioneaza si etichetele nu se pot genera | Mare | Medie | Completare la utilizare (15.2.2): o materie prima fara date complete nu poate intra intr-o linie de reteta; migrare in doua transe, incepand cu cele 150-250 de coduri care acopera 90% din utilizare; raport permanent de materii prime incomplete |
| RSC-06 | **Scorul de prioritate se erodeaza**: toti KAM-ii suprascriu totul in banda maxima si sistemul redevine "cine striga mai tare" | Medie | Mare | Buget de urgenta pe KAM (A1.1.10); expirarea automata a suprascrierilor la 90 de zile; raport lunar cu toate suprascrierile si autorii (RAP-14); dreptul de suprascriere limitat la un singur rol |
| RSC-07 | **Efortul de constructie depaseste disponibilitatea reala**: 78-98 de zile-om la 1-2 zile pe saptamana inseamna peste un an, nu 6 luni; proiectul se opreste la jumatate | Mare | Medie | Confirmarea explicita a disponibilitatii inainte de start (16.6.1); Val 1 cu domeniu strict limitat si termen ferm; tot ce nu incape se amana, nimic din Val 1 nu se amana; livrare in valuri care aduc valoare separat, astfel incat o oprire dupa Val 2 sa lase totusi o solutie utila |
| RSC-08 | **Costul licentelor pentru cititorii din companie**: accesul de citire pentru ~200 de persoane poate fi refuzat pe motive de cost, iar cerinta de vizibilitate pentru toata compania cade | Medie | Medie | Ecranul public construit ca aplicatie separata, tocmai pentru licentierea per aplicatie (17.1.2.1); varianta de rezerva C (export zilnic intr-o lista SharePoint) pregatita din proiectare; decizie ceruta de la IT inainte de Val 2 |
| RSC-09 | **Capacitatea Dataverse depasita**, mai ales pe Log: auditul creste imprevizibil si costa scump pe gigabyte | Medie | Medie | Audit activat selectiv, pe tabele si coloane, nu pe tot; auditul de citire numai unde e nevoie; FLX-20 arhiveaza in SharePoint, permitand retentie scurta in Dataverse; monitorizare lunara a capacitatii in primul an |
| RSC-10 | **Departamentele externe nu intra in sistem**: Achizitiile nu introduc ETA-uri, Calitatea nu aproba in aplicatie, Productia nu completeaza productia 0; sistemul ramane o unealta doar de R&D | Medie | Mare | Argument de vanzare pregatit separat pentru fiecare departament (16.3.1); ecrane dedicate, cu campurile lor separate vizual; masurarea explicita a adoptiei pe departament in criteriile Valului 2; escaladare catre conducere daca la 90 de zile ETA-urile nu se introduc |
| RSC-11 | **Aplicatia canvas nu functioneaza in hala**: semnal slab, telefoane vechi, manusi, ecrane greu de citit | Medie | Medie | Proiectare explicita pentru hala (10.2.1); mod offline cu coada de sincronizare; testare de acceptanta cu utilizatori reali, in hala, nu la birou (testele 31, 32, 34); pastrarea posibilitatii de a genera formularul pe hartie ca varianta de avarie |
| RSC-12 | **Datele migrate gresit erodeaza increderea**: proiectele in curs apar cu date incorecte in prima saptamana, iar concluzia devine "sistemul nou are date gresite" | Medie | Mare | Confirmarea individuala a fiecarui tehnolog pentru proiectele lui (15.5.1, pasul 8); excluderea proiectelor importate din indicatori (15.3.3.2); raport de verificare dupa migrare, semnat (15.7) |
| RSC-13 | **Modificarile in productie fara test**: "e o schimbare mica" duce la fluxuri oprite si formulare rupte | Medie | Medie | Procedura de promovare in 11 pasi, fara exceptii (17.2.2); mediu de test permanent; registrul de versiuni; nicio componenta creata in afara solutiei |
| RSC-14 | **Sablonul de livrabile nu corespunde realitatii**: prea multe derogari `Nu se aplica`, oamenii bifeaza formal ca sa treaca mai departe | Medie | Medie | Numarul de derogari se raporteaza explicit (13.4.2); revizuirea sablonului dupa primele 50 de proiecte; regula ca un livrabil derogat sistematic se elimina sau se face obligatoriu real |
| RSC-15 | **Automatizarea trecerilor de status ascunde realitatea**: proiectele avanseaza pe hartie fara sa avanseze in fapt | Mica | Mare | Statusul nu se automatizeaza, cu exceptia blocajelor (12.4.3); startul real al etapelor se inregistreaza din activitate reala, nu din bife (14.3.3) |
| RSC-16 | **Scurgere de informatie sensibila prin fluxuri**: securitatea pe coloana nu se aplica in Power Automate, iar o notificare include costul sau marja | Mica | Mare | Regula explicita: fluxurile nu includ in corpul mesajelor coloane protejate (11.5.2); verificare dedicata la testare (testul 26 din 17.3.2) |
| RSC-17 | **Generarea documentelor Word esueaza la structuri complexe**: dosarul TDV nu se poate genera dintr-un singur sablon | Mica | Medie | Generare in doua etape, cu anexe unite in PDF (12.3.12.1); dosarul TDV este in Val 3, deci exista timp pentru o alternativa; conector din AppSource ca varianta, verificat fata de politica DLP |
| RSC-18 | **Autonumber cu goluri sau resetare uitata**: codurile de proiect sar numere sau continua seria din anul precedent | Mica | Mica | Resetarea semintei la 1 ianuarie, trecuta in procedura anuala (12.3.1.1); verificarea duplicatelor dupa import; golurile in serie se accepta explicit, nu se corecteaza |
| RSC-19 | **Pierderea jurnalului de audit prin retentia mediului**, tacit, dupa perioada configurata | Mica | Mare | FLX-20, arhivare lunara in SharePoint cu retentie de 10 ani (5.6.3.3); verificarea explicita a setarii de retentie la trecerea in productie |
| RSC-20 | **Reteta validata se modifica tacit** la schimbarea datelor unei materii prime, iar eticheta livrata nu mai corespunde | Mica | Mare | Regula din 9.5.2: retetele validate nu se recalculeaza automat, se genereaza alerta de impact; versiunile validate se blocheaza (2.14.4) |

## 18.2 Riscurile care merita cea mai multa atentie

18.2.1 RSC-01, RSC-02 si RSC-03 sunt in acelasi timp cele mai probabile si cele mai grave.
Toate trei au aceeasi natura: solutia depinde de o singura persoana si de un mediu
personal, iar utilizatorii au o alternativa care functioneaza (Excelul).

18.2.2 Masura cu cel mai bun raport efort-beneficiu pentru toate trei este aceeasi:
livrarea rapida a Valului 1, cu domeniu strict limitat, urmata de trecerea intr-un mediu
de productie real. O solutie folosita zilnic de zece oameni intr-un mediu al companiei nu
mai poate fi abandonata; una construita perfect intr-un mediu personal, timp de un an,
poate disparea intr-o zi.

18.2.3 NOTA: riscul cel mai putin discutat in astfel de proiecte este cel de succes
partial - solutia functioneaza pentru R&D, dar celelalte departamente nu intra in ea
(RSC-10). Rezultatul este ca R&D face acum si munca de urmarire pe care o faceau altii,
prin telefon. Adoptia pe departament trebuie masurata explicit si escaladata, nu sperata.
