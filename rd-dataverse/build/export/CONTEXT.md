# Blueprint Suita Digitala R&D
## Dataverse / Power Apps / SharePoint / Power Automate

**Export complet al documentatiei. Generat 09.09.2026.**

---

## Context pentru cine citeste acest document fara istoricul discutiei

### Ce este

Blueprint de arhitectura si constructie pentru digitalizarea procesului R&D intr-o
companie FMCG de panificatie si patiserie congelata: 2 amplasamente, 9 linii de productie,
aproximativ 400 de angajati, intre 130 si 180 de proiecte de dezvoltare de produs pe an.

Situatia de plecare: evidenta se tine intr-un formular Excel cu aproximativ 30 de coloane
care sunt bife de existenta a livrabilelor, plus foldere in SharePoint. Formatul este
mostenit si nu este considerat satisfacator.

### Cine il construieste

Head of R&D, inginer, **singur, fara echipa IT**, in paralel cu functia de baza. Aceasta
constrangere este cea mai importanta din tot documentul si explica majoritatea deciziilor
de secventiere: solutia trebuie sa fie utila si daca se opreste la jumatate.

### Deciziile de arhitectura care nu se renegociaza

1. Baza de date: **Dataverse**. Motiv: relatii parinte-copil reale, tipuri stricte, reguli
   in date, audit nativ, fara limita de delegare.
2. Constructia incepe intr-un mediu **Developer** personal, cu tot ce se construieste
   intr-o **Solution unica**, exportata periodic.
3. Interfata: o aplicatie **model-driven** pentru birou si una **canvas** pentru mobil,
   folosita la linie si in laborator.
4. Documentele raman in **SharePoint**, un folder per proiect, generat automat, legat de
   inregistrarea de proiect prin integrarea nativa de documente.
5. **Power Automate** pentru aprobari, alerte, generarea folderului si a documentelor.
6. Raportare: **Power BI** sau vizualizari native, read-only.
7. Integrarea cu **SAP**: import, export sau citire. **Niciodata scriere.**

### Ce contine documentul

| Zona | Sectiuni |
|---|---|
| Model de date si documentatie | S00-S05 |
| Procese de business | S06-S15 |
| Roadmap, riscuri, acceptanta | S16-S21, A1 |
| Sinteza cu un al doilea blueprint, extensii, operare | S22-S28, A2 |

Cifrele modelului: **60 de tabele, 985 de coloane, 151 de relatii, 31 de seturi de optiuni
globale, 43 de livrabile de proiect, 35 de fluxuri, 13 roluri de securitate.**

### Ce mai exista, in afara acestui document

Repository-ul contine si artefactele prelucrabile, care nu sunt incluse aici pentru ca
sunt redundante cu textul: modelul ca JSON (`data/`), fisierele CSV de import, scripturile
de provizionare care creeaza componentele in Dataverse prin Web API, cele 12 sabloane Word
si o macheta HTML a ecranelor.

### Conventii de referinta

`TBL-nn` tabela &middot; `REL-nn` relatie &middot; `LIV-nn` livrabil &middot; `ETP-nn`
etapa &middot; `FLX-nn` flux &middot; `ECR-nn` ecran &middot; `ROL-nn` rol &middot;
`RSC-nn` risc &middot; `CA-nn` criteriu de acceptanta &middot; `DOC-nn` document generat
&middot; `RAP-nn` raport &middot; `M-nn` modul &middot; `IQ-nn` intrebare deschisa

`PROPUNERE` marcheaza un element propus de arhitect, care nu venea din cerinta initiala.
`NOTA` marcheaza un conflict intre cerinta si buna practica de platforma.

### Limba

Romana **fara diacritice**, cerinta explicita a briefingului initial. Numerotarea este
consecventa in tot documentul si se foloseste pentru trimiteri interne.

### Ce merita stiut inainte de a optimiza acest document

1. **Efortul.** Estimarea curenta este de 78-94 zile-om, dupa ce generarea automata a
   redus partea de constructie de la 138 la circa 41. La o disponibilitate de 1.5 zile pe
   saptamana inseamna 12-14 luni. Aceasta ipoteza este cea mai fragila din tot documentul.
2. **Calea critica nu mai este constructia**, ci obtinerea datelor de la Sales, Productie
   si Calitate. Vezi S26.
3. **Zece intrebari deschise** raman fara raspuns, in S20. Fiecare are o valoare implicita
   ca sa nu blocheze constructia, dar IQ-01 si IQ-10 schimba calendarul.
4. **S22 este un document de decizie**, nu de arhitectura: explica ce s-a preluat dintr-un
   al doilea blueprint mai ambitios, ce s-a respins si de ce, si rezolva cinci
   contradictii intre cele doua.

---

## Cuprinsul exportului

- **S00-sumar-executiv** &mdash; Sectiunea 0 - Sumar executiv
- **S01-harta-modulelor** &mdash; Sectiunea 1 - Harta modulelor
- **S02-model-date** &mdash; Sectiunea 2 - Modelul de date Dataverse
- **S03-relatii** &mdash; Sectiunea 3 - Diagrama relatiilor
- **S04-livrabile** &mdash; Sectiunea 4 - Livrabilele de proiect
- **S05-documentatie** &mdash; Sectiunea 5 - Structura documentatiei
- **S06-masuratori-senzorial** &mdash; Sectiunea 6 - Masuratori si evaluare senzoriala
- **S07-productie-0** &mdash; Sectiunea 7 - Productie 0
- **S08-revizuire-post-implementare** &mdash; Sectiunea 8 - Revizuirea post-implementare
- **S09-alergeni-nutritionale** &mdash; Sectiunea 9 - Alergeni si valori nutritionale
- **S10-ecrane** &mdash; Sectiunea 10 - Ecranele aplicatiilor
- **S11-securitate-roluri** &mdash; Sectiunea 11 - Securitate si roluri
- **S12-automatizari** &mdash; Sectiunea 12 - Automatizari
- **S13-indicatori** &mdash; Sectiunea 13 - Indicatori si raportare
- **S14-durate-etape** &mdash; Sectiunea 14 - Duratele etapelor
- **S15-migrare** &mdash; Sectiunea 15 - Migrarea
- **S16-roadmap** &mdash; Sectiunea 16 - Roadmap pe valuri
- **S17-trecere-productie** &mdash; Sectiunea 17 - Trecerea in productie
- **S18-riscuri** &mdash; Sectiunea 18 - Riscuri
- **S19-criterii-acceptanta** &mdash; Sectiunea 19 - Criterii de acceptanta
- **S20-intrebari-deschise** &mdash; Sectiunea 20 - Intrebari deschise
- **S21-prompturi-continuare** &mdash; Sectiunea 21 - Prompturi de continuare
- **S22-sinteza-enterprise** &mdash; Sectiunea 22 - Sinteza celor doua blueprinturi
- **S23-guvernanta-proiect** &mdash; Sectiunea 23 - Guvernanta de proiect
- **S24-stabilizare-capabilitate** &mdash; Sectiunea 24 - Stabilizare, capabilitate de proces si sanatatea proiectului
- **S25-cunoastere** &mdash; Sectiunea 25 - Cunoastere organizationala
- **S26-constructie-asistata** &mdash; Sectiunea 26 - Constructia asistata: ce se genereaza si ce nu
- **S27-unde-traieste-ce** &mdash; Sectiunea 27 - Unde traieste ce
- **S28-acces-si-licentiere** &mdash; Sectiunea 28 - Acces si licentiere
- **A1-prioritizare-si-termene** &mdash; Anexa A1 - Prioritizarea si calculul termenelor
- **A2-backlog-enterprise** &mdash; Anexa A2 - Backlog enterprise, cu criterii de activare

- **README** &mdash; Index si sinteza
- **V0-ghid-constructie** &mdash; Ghid de constructie, Valul 0
- **README** &mdash; Provizionarea modelului
