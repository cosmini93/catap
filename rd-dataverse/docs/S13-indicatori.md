# Sectiunea 13 - Indicatori si raportare

## 13.1 Cei trei indicatori

| Indicator | Ce masoara | Tinta |
|---|---|---|
| T-Total | Respectarea timpului | 95% |
| Q-Corect | Corectitudinea a ceea ce se livreaza | 98% |
| Q-Complet | Completitudinea a ceea ce se livreaza | 98% |

13.1.1 Tintele se seteaza in `rd_indicator` si sunt parametrizabile. Valorile de mai sus
sunt punctul de pornire recomandat: T-Total mai jos decat cele de calitate, pentru ca
timpul depinde partial de factori externi, in timp ce corectitudinea si completitudinea
depind aproape integral de R&D.

## 13.2 T-Total

### 13.2.1 Definitia

T-Total masoara procentul de activitati finalizate in termenul stabilit, dupa scaderea
timpului in care ceasul a fost oprit de blocaje externe.

```
Pentru fiecare activitate masurabila (livrabil sau etapa):

durata_bruta  = data_realizarii - data_inceperii              [zile lucratoare]
zile_blocate  = suma zilelor de blocaj activ cu rd_oprsteceas = Da,
                suprapuse peste intervalul activitatii
durata_neta   = durata_bruta - zile_blocate

termen_efectiv = termen_planificat + zile_blocate

la_termen = data_realizarii <= termen_efectiv

T-Total (%) = numar activitati la_termen / numar activitati finalizate * 100
```

13.2.2 Suprapunerea blocajelor se calculeaza pe intervale, nu prin insumare simpla. Doua
blocaje care se suprapun partial in timp contribuie cu reuniunea intervalelor lor, nu cu
suma zilelor. Aceasta este singura parte a calculului care se implementeaza gresit tipic
si care produce, dupa un an, indicatori peste 100%.

### 13.2.3 Oprirea ceasului

| Situatie | Ceas R&D | Termen catre client |
|---|---|---|
| Blocaj cu sursa Furnizor, Client, Calitate, Planificare, Productie, Achizitii, Extern reglementar | Oprit | Curge |
| Blocaj cu sursa Intern R&D | Curge | Curge |
| Status `In asteptare materie prima` | Oprit, daca exista blocaj activ deschis | Curge |
| Status `Suspendat` | Oprit | Se renegociaza; se raporteaza separat |
| Concediul tehnologului | Curge | Curge |

13.2.3.1 Concediul nu opreste ceasul. Este o problema de alocare a Managerului R&D, nu o
cauza externa. Daca ar opri ceasul, indicatorul ar deveni nefalsificabil.

13.2.3.2 Termenul catre client continua sa curga in orice situatie si se raporteaza
separat, ca `abatere fata de termenul negociat`. Aceasta este dubla masurare ceruta
explicit: R&D nu este penalizat pentru asteptarea unei mostre de la furnizor, dar compania
stie ca a livrat cu 12 zile intarziere catre client si de ce.

### 13.2.4 Nivelurile de masurare

| Nivel | Unitatea numarata | Cine il vede |
|---|---|---|
| Activitate | Fiecare livrabil si etapa finalizata | Manager R&D |
| Rol | Toate activitatile cu `rd_rolresponsabil` = rolul respectiv | Head of R&D |
| Persoana | Toate activitatile cu responsabilul = persoana | Persoana, Manager R&D, Head of R&D |
| Departament | Toate activitatile R&D | Head of R&D, conducere |

13.2.4.1 T-Total pe rol este cel mai util indicator dintre cele patru: arata daca
intarzierile vin din R&D, din Achizitii, din Calitate sau din Productie. Astazi aceasta
intrebare nu are raspuns cu cifre.

13.2.4.2 T-Total pe persoana se raporteaza persoanei si Managerului R&D, nu se afiseaza
public. Motiv: un indicator individual afisat public produce, in trei luni, declararea
selectiva a datelor de realizare, nu imbunatatirea performantei.

## 13.3 Q-Corect

### 13.3.1 Definitia

Q-Corect masoara procentul de livrabile acceptate din prima, fara respingere si fara
corectie ceruta de aprobator.

```
respins = livrabilul a trecut prin status Respins cel putin o data
          SAU documentul asociat a primit versiune noua dupa respingere

Q-Corect (%) = livrabile aprobate fara respingere / livrabile aprobate total * 100
```

13.3.2 Se numara numai livrabilele care au aprobator. Un livrabil fara aprobare nu poate
fi masurat pe corectitudine.

13.3.3 Componente suplimentare, care intra in Q-Corect cu pondere:

| Componenta | Pondere | Sursa |
|---|---|---|
| Livrabile aprobate din prima | 60% | Din statusul livrabilelor |
| Trialuri cu rezultat Reusit din prima incercare | 15% | Din TBL-15 |
| Masuratori conforme fata de toleranta declarata | 10% | Din TBL-16b |
| Verificari HACCP conforme la productia 0 | 10% | Din TBL-34 |
| Antecalcule aprobate fara revizuire | 5% | Din TBL-22 |

13.3.4 Argument pentru ponderare: un Q-Corect construit doar pe aprobari masoara cat de
indulgent este aprobatorul. Adaugand trialurile reusite din prima si conformitatea
masuratorilor, indicatorul masoara si calitatea tehnica, nu doar cea documentara.

## 13.4 Q-Complet

### 13.4.1 Definitia

Q-Complet masoara procentul de livrabile obligatorii si aplicabile care sunt realizate la
momentul inchiderii proiectului sau la data de raportare.

```
Q-Complet la inchidere (%) =
    livrabile obligatorii aplicabile realizate / livrabile obligatorii aplicabile * 100

Q-Complet in curs (%) =
    livrabile scadente si realizate / livrabile scadente * 100
```

13.4.2 Livrabilele marcate `Nu se aplica` de Managerul R&D nu intra la numitor, dar se
raporteaza separat: numarul de derogari pe proiect si pe an. Un numar mare de derogari
inseamna ca sablonul de livrabile nu corespunde realitatii si trebuie corectat, nu ca
oamenii sunt neglijenti.

13.4.3 Q-Complet la nivel de departament, calculat lunar pe proiectele finalizate in luna
respectiva, este indicatorul care raspunde direct la problema centralizatorului actual:
astazi nimeni nu poate spune cate dosare sunt complete fara sa le deschida unul cate unul.

## 13.5 Cum se calculeaza si cand

| Indicator | Frecventa | Flux | Ce se scrie |
|---|---|---|---|
| Campuri de proiect (zile in coada, T-Total net, abatere de termen) | Zilnic | FLX-16 | Coloane pe `rd_proiect` |
| T-Total, Q-Corect, Q-Complet pe activitate, rol, persoana | Lunar, in prima zi lucratoare | FLX-16 | Inregistrari in `rd_masurareindicator` |
| Sinteza trimestriala si anuala | Trimestrial, anual | FLX-16 | Idem, cu perioada corespunzatoare |

13.5.1 Masuratorile lunare se congeleaza: odata scrisa, o inregistrare de masurare nu se
recalculeaza. Motiv: altfel, o inregistrare corectata retroactiv in martie schimba
indicatorul din ianuarie, iar raportarea isi pierde credibilitatea.

## 13.6 Rapoartele

### 13.6.1 Lista rapoartelor

| Cod | Raport | Continut | Cine il vede | Frecventa |
|---|---|---|---|---|
| RAP-01 | Durata medie reala pe etapa | Mediana si media duratei nete pe fiecare etapa, comparata cu durata standard, pe ultimele 12 luni | Head of R&D, Manager R&D | Lunar |
| RAP-02 | Livrabilele care intarzie cel mai des | Top 10 livrabile dupa procentul de intarziere si dupa media zilelor de intarziere, cu rolul responsabil | Head of R&D, Manager R&D, sefii rolurilor implicate | Lunar |
| RAP-03 | Incarcarea pe tehnolog | Proiecte active, distributia pe benzi, gradul de incarcare, evolutie pe 12 luni | Manager R&D, Head of R&D | Saptamanal |
| RAP-04 | Coada pe linie | Proiecte pe fiecare linie, primul slot estimat, gradul de supraincarcare | Manager R&D, Planificare | Saptamanal |
| RAP-05 | Rata de acceptare a solicitarilor pe KAM | Solicitari trimise, acceptate, respinse, amanate, cu motivele; rata de acceptare | Head of R&D, Comercial Manager, fiecare KAM pentru el | Lunar |
| RAP-06 | Proiecte abandonate cu motive | Lista, cu motivul, faza in care s-au oprit si costul estimat al efortului pierdut | Head of R&D, conducere | Trimestrial |
| RAP-07 | T-Total pe rol si pe persoana | Cu detaliul zilelor blocate si al sursei blocajelor | Head of R&D | Lunar |
| RAP-08 | Q-Corect si Q-Complet | Pe departament, rol si persoana | Head of R&D | Lunar |
| RAP-09 | Blocaje pe sursa | Zile de blocaj cumulate pe sursa (furnizor, client, Calitate, Planificare), cu top 10 cauze | Head of R&D, conducere | Trimestrial |
| RAP-10 | Termen propus fata de negociat fata de realizat | Pe KAM si pe tehnolog | Head of R&D, Comercial Manager | Trimestrial |
| RAP-11 | Produse lansate si indicele de sanatate | Din revizuirea post-implementare | Head of R&D, conducere, comercial | Trimestrial |
| RAP-12 | Materii prime si furnizori | Lead time real fata de asumat, rata de respingere pe furnizor, numarul de modificari de ETA | Achizitii, Head of R&D | Lunar |
| RAP-13 | Portofoliu pe alergeni | Ce produse contin fiecare alergen | Calitate, R&D | La cerere |
| RAP-14 | Suprascrieri de prioritate | Cine, ce, de ce, cand | Head of R&D, conducere | Lunar |
| RAP-15 | Ce am invatat (anual) | Abateri de cost si de randament pe categorie si pe linie; corectii propuse pentru antecalcul | Head of R&D, conducere | Anual |

### 13.6.2 Unde traiesc rapoartele

| Tip de raport | Implementare | Motiv |
|---|---|---|
| RAP-03, RAP-04, si listele operationale | Vizualizari si tablouri de bord native Dataverse | Sunt liste filtrabile, nu au nevoie de Power BI; sunt disponibile in Val 1, fara licente suplimentare |
| RAP-01, RAP-02, RAP-05 ... RAP-15 | Power BI, cu conexiune la Dataverse | Cer agregari pe perioade, comparatii istorice si grafice |
| RAP-13 | Vizualizare Dataverse cu filtru pe Choice multi-select | Se cere ad-hoc, la audit sau la cerinta de client |

13.6.2.1 Raportarea este read-only, conform deciziei de arhitectura. Nicio actiune nu se
declanseaza dintr-un raport.

13.6.2.2 NOTA: raportarea in Power BI cere licente Pro pentru cei care publica si
consuma continut in spatii de lucru, sau capacitate dedicata. Pentru cei ~200 de cititori
din companie, ecranul public de status (ECR-04) este in aplicatia model-driven, nu in
Power BI, tocmai ca sa nu genereze cerinta de licentiere pentru toata firma.

## 13.7 Ce se face cu indicatorii

13.7.1 Indicatorii nu sunt scop in sine. Regula de folosire, scrisa in procedura:

| Indicator sub tinta | Prima intrebare | Actiune tipica |
|---|---|---|
| T-Total pe departament | Care rol si care etapa trag in jos? | Corectia duratelor standard (Sectiunea 14) sau realocarea |
| T-Total pe rol extern R&D | Care sursa de blocaj domina? | Discutie cu departamentul respectiv, cu RAP-09 pe masa |
| Q-Corect | Ce livrabile se resping cel mai des si de ce? | Sablon de document mai clar, sau instruire, sau aprobator prea vag |
| Q-Complet | Ce livrabile lipsesc sistematic la inchidere? | Sablonul cere ceva ce nu se face niciodata: se elimina sau se face obligatoriu real |

13.7.2 Un indicator care sta trei luni sub tinta fara actiune declarata este un indicator
care trebuie eliminat sau retintit. Se revizuiesc anual, impreuna cu ponderile de
prioritizare si cu duratele standard.
