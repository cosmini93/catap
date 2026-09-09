#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concateneaza documentatia intr-un singur .md portabil, plus o varianta pe volume.

Iesire: build/export/
  BLUEPRINT-COMPLET.md      tot, un singur fisier
  VOL1-arhitectura.md       S00-S05, modelul si documentatia
  VOL2-procese.md           S06-S15, procesele de business
  VOL3-implementare.md      S16-S21 + A1, roadmap si constructie
  VOL4-extensii.md          S22-S28 + A2, sinteza Enterprise si operarea
"""
import os
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent

PREAMBUL = """# Blueprint Suita Digitala R&D
## Dataverse / Power Apps / SharePoint / Power Automate

**Export complet al documentatiei. Generat {data}.**

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

"""

GRUPE = [
    ("VOL1-arhitectura", "Volumul 1 - Arhitectura, modelul de date si documentatia",
     ["S00", "S01", "S02", "S03", "S04", "S05"]),
    ("VOL2-procese", "Volumul 2 - Procesele de business",
     ["S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13", "S14", "S15"]),
    ("VOL3-implementare", "Volumul 3 - Roadmap, riscuri si constructie",
     ["S16", "S17", "S18", "S19", "S20", "S21", "A1"]),
    ("VOL4-extensii", "Volumul 4 - Sinteza Enterprise, extensii si operare",
     ["S22", "S23", "S24", "S25", "S26", "S27", "S28", "A2"]),
]


def fisiere_docs():
    d = BASE / "docs"
    return sorted(d.glob("*.md"), key=lambda p: (
        {"A": "Z"}.get(p.name[0], p.name[0]), p.name))


def citeste(p):
    return p.read_text(encoding="utf-8").rstrip()


def separator(titlu, fisier):
    return (f"\n\n<!-- ==================== {fisier} ==================== -->\n\n"
            f"---\n\n")


def main():
    docs = fisiere_docs()
    # ordonare: S00..S28, apoi A1, A2
    def cheie(p):
        n = p.stem
        if n.startswith("S"):
            return (0, int(n[1:3]))
        return (1, int(n[1:2]))
    docs = sorted(docs, key=cheie)

    extra = [
        (BASE / "README.md", "Index si sinteza"),
        (BASE / "build" / "V0-ghid-constructie.md", "Ghid de constructie, Valul 0"),
        (BASE / "build" / "deploy" / "README.md", "Provizionarea modelului"),
    ]

    data_azi = date.today().strftime("%d.%m.%Y")
    preambul = PREAMBUL.format(data=data_azi)

    # --- cuprins ---
    cuprins = ["## Cuprinsul exportului\n"]
    for p in docs:
        titlu = citeste(p).split("\n")[0].lstrip("# ").strip()
        cuprins.append(f"- **{p.stem}** &mdash; {titlu}")
    cuprins.append("")
    for p, et in extra:
        cuprins.append(f"- **{p.stem if p.stem != 'README' else 'README'}** &mdash; {et}")
    cuprins = "\n".join(cuprins)

    # --- fisierul complet ---
    parti = [preambul, cuprins]
    for p in docs:
        parti.append(separator(p.stem, p.name) + citeste(p))
    for p, et in extra:
        parti.append(separator(p.stem, str(p.relative_to(BASE))) + citeste(p))
    complet = "\n".join(parti) + "\n"
    (OUT / "BLUEPRINT-COMPLET.md").write_text(complet, encoding="utf-8")

    # --- volume ---
    rez = []
    for nume, titlu, prefixe in GRUPE:
        alese = [p for p in docs if p.stem[:3].rstrip("-") in prefixe
                 or p.stem[:2] in prefixe]
        alese = [p for p in docs if any(p.stem.startswith(x) for x in prefixe)]
        cap = (f"# {titlu}\n\n"
               f"Parte din blueprintul Suitei Digitale R&D, export din {data_azi}.\n"
               f"Contine sectiunile: {', '.join(p.stem for p in alese)}.\n\n"
               f"Contextul complet al proiectului este in preambulul din "
               f"`BLUEPRINT-COMPLET.md`.\n")
        corp = [cap] + [separator(p.stem, p.name) + citeste(p) for p in alese]
        txt = "\n".join(corp) + "\n"
        (OUT / f"{nume}.md").write_text(txt, encoding="utf-8")
        rez.append((f"{nume}.md", len(alese), len(txt)))

    # --- preambul separat, de pus inaintea oricarui volum ---
    (OUT / "CONTEXT.md").write_text(preambul + cuprins + "\n", encoding="utf-8")

    print("EXPORT GENERAT\n")
    c = len(complet)
    print(f"  {'BLUEPRINT-COMPLET.md':28} {len(docs)+len(extra):2} sectiuni  "
          f"{c:>8,} car.  ~{c/3.5:>7,.0f} tok")
    print(f"  {'CONTEXT.md':28} {'-':>2}           "
          f"{len(preambul+cuprins):>8,} car.  ~{len(preambul+cuprins)/3.5:>7,.0f} tok")
    print()
    for nume, n, dim in rez:
        print(f"  {nume:28} {n:2} sectiuni  {dim:>8,} car.  ~{dim/3.5:>7,.0f} tok")


if __name__ == "__main__":
    main()
