#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genereaza cele 11 sabloane Word (.docx) din Sectiunea 5.5, cu content controls.

Fiecare sablon contine controale de continut (SDT) etichetate cu numele campului din
Dataverse, pe care actiunea "Populate a Microsoft Word template" din Power Automate le
completeaza (FLX-12).

Iesire: build/deploy/sabloane-word/*.docx
"""
import zipfile, json
from pathlib import Path

OUT = Path(__file__).parent / "sabloane-word"

# cod, titlu, sectiuni: (titlu sectiune, [(eticheta camp, tag, tip)])
# tip: t = text simplu, r = rand repetitiv (tabel)
SABLOANE = [
 ("SCP", "Solicitare cerinta produs", "DOC-01", [
  ("1. Identificare", [("Numar SCP","rd_numarscp"),("Data","rd_createdon"),
    ("KAM","rd_kam"),("Client","rd_client"),("Clasificare client","rd_clasificare"),
    ("Canal","rd_canal")]),
  ("2. Produsul cerut", [("Denumire de lucru","rd_produsdorit"),("Descriere","rd_descriere"),
    ("Gramaj (g)","rd_gramaj"),("Dimensiuni","rd_dimensiuni"),
    ("Bucati pe ambalaj","rd_bucatiambalaj"),("Tip ambalare","rd_tipambalare")]),
  ("3. Piata", [("Volum estimat anual (kg)","rd_volumanual"),("Pret tinta","rd_prettinta")]),
  ("4. Termen", [("Termen dorit","rd_termendorit"),("Termen impus extern","rd_termenimpus"),
    ("Tip termen impus","rd_tiptermenimpus")]),
  ("5. Motivul cererii", [("Motiv","rd_motivcerere")]),
  ("6. Referinta de comparatie", [("Tip referinta","rd_tipreferinta"),
    ("Detalii","rd_detaliireferinta")]),
  ("7. Cerinte de eticheta", [("Cerinte","rd_cerinteeticheta")]),
  ("8. Cerinte de ambalaj", [("Cerinte","rd_cerinteambalaj")]),
  ("9. Triaj", [("Rezultat","rd_rezultattriaj"),("Motiv","rd_motivtriaj"),
    ("Comentariu","rd_comentariutriaj"),("Data","rd_datatriaj"),
    ("Cod proiect generat","rd_codproiect")]),
 ]),
 ("PLAN", "Plan de dezvoltare produs", "DOC-02", [
  ("1. Identificare", [("Cod proiect","rd_codproiect"),("Produs","rd_numeprodus"),
    ("Client","rd_client"),("Tehnolog","rd_tehnolog"),("Versiune","rd_versiune")]),
  ("2. Obiectiv", [("Descrierea produsului tinta","rd_obiectiv")]),
  ("3. Criterii de acceptanta", [("Gramaj si toleranta","rd_criteriigramaj"),
    ("Scor senzorial minim","rd_scorminim"),("Cost tinta","rd_costtinta")]),
  ("4. Abordare tehnologica", [("Tip de aluat si proces","rd_abordare"),
    ("Linie vizata","rd_linie")]),
  ("5. Materii prime", [("REPETITIV_MP","rd_materiiprime")]),
  ("6. Plan de testare", [("Numar de trialuri estimate","rd_numartrialuri"),
    ("Ce se variaza","rd_plantestare")]),
  ("7. Etape si termene", [("REPETITIV_ETAPE","rd_etape")]),
  ("8. Livrabile", [("REPETITIV_LIVRABILE","rd_livrabile")]),
  ("9. Riscuri de proiect", [("REPETITIV_RISCURI","rd_riscuri")]),
  ("10. Aprobare", [("Tehnolog","rd_tehnolog"),("Manager R&D","rd_manager"),
    ("Data","rd_dataaprobare")]),
 ]),
 ("FTEST", "Fisa de testare", "DOC-03", [
  ("1. Identificare", [("Numar fisa","rd_numarfisa"),("Proiect","rd_codproiect"),
    ("Versiune reteta","rd_versiunereteta"),("Data planificata","rd_dataplanificata")]),
  ("2. Obiectivul testarii", [("Obiectiv","rd_obiectiv")]),
  ("3. Reteta", [("REPETITIV_RETETA","rd_liniireteta")]),
  ("4. Parametri de proces tinta", [("Parametri","rd_parametritinta")]),
  ("5. Plan de esantionare", [("Plan","rd_planesantionare")]),
  ("6. Tolerante declarate", [("Tolerante","rd_tolerante")]),
  ("7. Criterii senzoriale", [("Grila aplicabila","rd_grila"),
    ("Scor minim acceptabil","rd_scorminim")]),
  ("8. Aprobare", [("Tehnolog","rd_autor"),("Manager R&D","rd_aprobator")]),
 ]),
 ("RTEST", "Raport de testare", "DOC-04", [
  ("1. Identificare", [("Proiect","rd_codproiect"),("Trial","rd_numartrial"),
    ("Data","rd_start"),("Linie","rd_linie"),("Schimb","rd_schimb"),
    ("Operator","rd_operator")]),
  ("2. Reteta executata", [("REPETITIV_RETETA","rd_liniireteta")]),
  ("3. Parametri realizati fata de tinta", [("REPETITIV_PARAMETRI","rd_parametri")]),
  ("4. Randament", [("Aluat introdus (kg)","rd_cantitatealuat"),
    ("Bucati obtinute","rd_bucatiobtinute"),("Randament (%)","rd_randament")]),
  ("5. Masuratori", [("REPETITIV_STATISTICA","rd_statistica")]),
  ("6. Neconformitati", [("REPETITIV_NECONFORME","rd_neconforme")]),
  ("7. Evaluare senzoriala", [("Scor ponderat","rd_scortotal"),
    ("Verdict","rd_verdict"),("Diferenta fata de referinta","rd_diferenta")]),
  ("8. Defecte constatate", [("REPETITIV_DEFECTE","rd_defecte")]),
  ("9. Concluzie", [("Rezultat","rd_rezultat"),("Observatii","rd_observatii")]),
  ("10. Aprobare", [("Tehnolog","rd_autor"),("Manager R&D","rd_aprobator")]),
 ]),
 ("FSENZ", "Fisa de evaluare senzoriala", "DOC-05", [
  ("1. Identificare", [("Numar evaluare","rd_numarevaluare"),("Proiect","rd_codproiect"),
    ("Trial","rd_trial"),("Data","rd_data"),("Tip evaluare","rd_tipevaluare")]),
  ("2. Conditii de degustare", [("Conditii","rd_conditii")]),
  ("3. Panel", [("Numar evaluatori","rd_numarevaluatori")]),
  ("4. Scoruri pe criterii", [("REPETITIV_SCORURI","rd_scoruri")]),
  ("5. Sinteza", [("Scor ponderat produs","rd_scortotal"),
    ("Scor referinta","rd_scorreferinta"),("Diferenta","rd_diferenta"),
    ("Dezacord maxim","rd_dezacord")]),
  ("6. Defecte bifate", [("REPETITIV_DEFECTE","rd_defecte")]),
  ("7. Verdict", [("Verdict","rd_verdict"),("Actiuni cerute","rd_actiuni")]),
 ]),
 ("ANTECALC", "Antecalcul", "DOC-06", [
  ("1. Identificare", [("Proiect","rd_codproiect"),("Produs","rd_numeprodus"),
    ("Versiune antecalcul","rd_versiune"),("Data","rd_datacalcul"),("Linie","rd_linie")]),
  ("2. Ipoteze", [("Pierdere tehnologica (%)","rd_pierdere"),
    ("Viteza de linie","rd_vitezanominala")]),
  ("3. Materii prime", [("REPETITIV_LINII","rd_liniiantecalcul")]),
  ("4. Cost MP", [("Cost MP / kg","rd_costmp"),("Cost MP ajustat / kg","rd_costmpajustat")]),
  ("5. Ambalaj", [("Cost ambalaj / buc","rd_costambalaj")]),
  ("6. Manopera", [("Cost manopera / kg","rd_costmanopera")]),
  ("7. Energie si congelare", [("Cost energie / kg","rd_costenergie"),
    ("Cost congelare / kg","rd_costcongelare")]),
  ("8. Regie", [("Regie / kg","rd_regie")]),
  ("9. Cost total", [("Cost total / kg","rd_costtotal"),
    ("Cost total / buc","rd_costbuc")]),
  ("10. Pret si marja", [("Pret tinta","rd_prettinta"),("Marja bruta (%)","rd_marja")]),
  ("11. Sensibilitate", [("REPETITIV_SENSIBILITATE","rd_sensibilitate")]),
  ("12. Aprobare", [("Tehnolog","rd_autor"),("Manager R&D","rd_aprobator")]),
 ]),
 ("SDP", "Specificatie de produs", "DOC-07", [
  ("1. Identificare", [("Cod SAP","rd_codsapfinit"),("Denumire","rd_numeprodus"),
    ("Versiune","rd_versiune"),("Data","rd_dataaprobare"),("Linie","rd_linie")]),
  ("2. Descrierea produsului", [("Denumire legala","rd_denumirelegala"),
    ("Gramaj","rd_gramaj"),("Dimensiuni","rd_dimensiuni")]),
  ("3. Reteta de productie", [("REPETITIV_RETETA","rd_liniireteta")]),
  ("4. Proces pas cu pas", [("Parametri de proces","rd_parametri")]),
  ("5. Puncte critice", [("Puncte critice HACCP","rd_haccp")]),
  ("6. Controale in proces", [("Controale","rd_controale")]),
  ("7. Ambalare", [("Ambalare si etichetare","rd_ambalare")]),
  ("8. Paletizare", [("Paletizare","rd_paletizare")]),
  ("9. Depozitare si transport", [("Conditii de depozitare","rd_depozitare"),
    ("Termen de valabilitate (luni)","rd_valabilitate")]),
  ("10. Utilizare la client", [("Decongelare, dospire, coacere","rd_utilizare")]),
  ("11. Alergeni", [("Alergeni continuti","rd_alergeni"),("Urme","rd_alergeniurme")]),
  ("12. Valori nutritionale", [("REPETITIV_NUTRITIONAL","rd_nutritional")]),
  ("13. Aprobare", [("Aprobator R&D","rd_aprobatorrd"),
    ("Aprobator Calitate","rd_aprobatorcalitate")]),
 ]),
 ("CONDIPN", "Conditii IPN", "DOC-08a", [
  ("1. Identificare", [("Numar IPN","rd_numaripn"),("Proiect","rd_codproiect"),
    ("Linie","rd_linie"),("Data planificata productie 0","rd_dataprod0")]),
  ("2. Checklist de conditii", [("REPETITIV_CONDITII","rd_conditii")]),
  ("3. Status", [("Status implementare","rd_statusipn")]),
 ]),
 ("PLANIPN", "Plan IPN", "DOC-08b", [
  ("1. Identificare", [("Proiect","rd_codproiect"),("Produs","rd_numeprodus"),
    ("Linie","rd_linie"),("Data","rd_dataprod0"),("Schimb","rd_schimb"),
    ("Cantitate planificata","rd_cantitateplanificata")]),
  ("2. Echipa", [("Tehnolog","rd_tehnolog"),("Sef de tura","rd_seftura"),
    ("Calitate","rd_calitate"),("Cine decide oprirea","rd_decidentoprire")]),
  ("3. Program orar", [("Program","rd_programorar")]),
  ("4. Parametri de urmarit", [("REPETITIV_PARAMETRI","rd_parametri")]),
  ("5. Plan de esantionare", [("Plan","rd_planesantionare")]),
  ("6. Criterii de oprire", [("Criterii","rd_criteriioprire")]),
  ("7. Destinatia produsului", [("Destinatie","rd_destinatie")]),
  ("8. Riscuri anticipate", [("REPETITIV_RISCURI","rd_riscuri")]),
  ("9. Aprobare", [("R&D","rd_aprobatorrd"),("Calitate","rd_aprobatorcalitate"),
    ("Productie","rd_aprobatorproductie")]),
 ]),
 ("RPROD0", "Raport de productie 0", "DOC-09", [
  ("1. Identificare", [("Numar","rd_numarp0"),("Proiect","rd_codproiect"),
    ("Data","rd_data"),("Linie","rd_linie"),("Schimb","rd_schimb")]),
  ("2. Cantitati si randament", [("Cantitate planificata (kg)","rd_cantitateplanificata"),
    ("Aluat introdus (kg)","rd_aluatintrodus"),("Bucati bune","rd_bucatibune"),
    ("Cantitate realizata (kg)","rd_cantitaterealizata"),
    ("Randament aluat (%)","rd_randamentaluat")]),
  ("3. Rebut pe cauze", [("REPETITIV_REBUT","rd_rebut"),
    ("Rebut total (%)","rd_rebutprocent"),("Cauza dominanta","rd_cauzadominanta")]),
  ("4. Viteza si timpi", [("Viteza nominala","rd_vitezanominala"),
    ("Viteza reala","rd_vitezareala"),("Eficienta (%)","rd_eficientaviteza"),
    ("Timp setup (min)","rd_timpsetup")]),
  ("5. Parametri reali fata de specificati", [("REPETITIV_PARAMETRI","rd_parametri")]),
  ("6. Greutate la ambalare", [("Greutate medie (g)","rd_greutatemedie"),
    ("Abatere de la gramaj (%)","rd_abateregramaj"),
    ("Supraumplere (%)","rd_supraumplere")]),
  ("7. Conformitate HACCP", [("REPETITIV_HACCP","rd_haccp")]),
  ("8. Probleme aparute", [("REPETITIV_PROBLEME","rd_probleme")]),
  ("9. Decizie finala", [("Decizie","rd_decizie"),
    ("Conditii de validare","rd_conditiivalidare"),
    ("Responsabil","rd_responsabildecizie"),("Data","rd_datadecizie")]),
 ]),
 ("TDV", "Dosar TDV validat", "DOC-10", [
  ("1. Pagina de garda", [("Cod proiect","rd_codproiect"),("Produs","rd_numeprodus"),
    ("Client","rd_client"),("Cod SAP","rd_codsapfinit"),
    ("Data validarii","rd_datavalidare")]),
  ("2. Cerinta initiala", [("SCP","rd_numarscp"),("Referinta","rd_referinta")]),
  ("3. Traseul proiectului", [("REPETITIV_ETAPE","rd_etape"),
    ("REPETITIV_BLOCAJE","rd_blocaje")]),
  ("4. Reteta validata", [("Versiune","rd_versiunereteta"),
    ("REPETITIV_RETETA","rd_liniireteta")]),
  ("5. Rezultate de testare", [("REPETITIV_TRIALURI","rd_trialuri")]),
  ("6. Evaluare senzoriala", [("Verdict final","rd_verdict"),
    ("Comparatie cu referinta","rd_diferenta")]),
  ("7. Antecalcul aprobat", [("Cost total / kg","rd_costtotal"),("Marja (%)","rd_marja")]),
  ("8. Specificatii", [("ST finala","rd_stfinala"),("SDP","rd_sdp")]),
  ("9. Alergeni si nutritionale", [("Alergeni","rd_alergeni"),
    ("REPETITIV_NUTRITIONAL","rd_nutritional")]),
  ("10. Eticheta aprobata", [("Versiune","rd_versiuneeticheta"),
    ("Data aprobarii","rd_dataaprobareeticheta")]),
  ("11. Implementare", [("Numar IPN","rd_numaripn"),("Plan HACCP","rd_haccp")]),
  ("12. Productie 0", [("Decizie","rd_deciziep0"),("Randament","rd_randamentp0")]),
  ("13. Lista livrabilelor", [("REPETITIV_LIVRABILE","rd_livrabile")]),
  ("14. Declaratie de validare", [("Text de validare","rd_declaratie"),
    ("Manager R&D","rd_aprobatorrd"),("Managementul Calitatii","rd_aprobatorcalitate")]),
 ]),
 ("RPI", "Raport de revizuire post-implementare", "DOC-11", [
  ("1. Identificare", [("Numar","rd_numarrpi"),("Proiect","rd_codproiect"),
    ("Etapa revizuire","rd_etaparevizuire"),("Data scadenta","rd_datascadenta"),
    ("Data efectuarii","rd_dataefectuare")]),
  ("2. Volume", [("Cantitate produsa (kg)","rd_cantitateprodusa"),
    ("Numar loturi","rd_numarloturi"),
    ("Volum realizat fata de estimat (%)","rd_realizarevolum")]),
  ("3. Calitate", [("Reclamatii","rd_reclamatii"),
    ("Neconformitati interne","rd_neconformitati"),
    ("Rata reclamatii (ppm)","rd_ratareclamatii")]),
  ("4. Randament si rebut", [("Randament in serie (%)","rd_randamentserie"),
    ("Randament la productia 0 (%)","rd_randamentprod0"),
    ("Diferenta (pp)","rd_diferentarandament"),("Rebut in serie (%)","rd_rebutserie")]),
  ("5. Cost", [("Cost real / kg","rd_costreal"),
    ("Cost din antecalcul / kg","rd_costantecalcul"),
    ("Abatere de cost (%)","rd_abaterecost")]),
  ("6. Feedback", [("De la client","rd_feedbackclient"),("De la KAM","rd_feedbackkam"),
    ("De la productie","rd_feedbackproductie")]),
  ("7. Indice de sanatate", [("Indice","rd_indicesanatate")]),
  ("8. Date indisponibile", [("Departamente care nu au furnizat","rd_dateindisponibile")]),
  ("9. Decizie", [("Decizie","rd_decizie"),("Actiuni","rd_actiuni"),
    ("Responsabil","rd_responsabil"),("Aprobator","rd_aprobator")]),
 ]),
]

NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")


def par(text, stil=None, bold=False, size=None):
    p = ['<w:p><w:pPr>']
    if stil: p.append(f'<w:pStyle w:val="{stil}"/>')
    p.append('</w:pPr><w:r><w:rPr>')
    if bold: p.append('<w:b/>')
    if size: p.append(f'<w:sz w:val="{size}"/>')
    p.append(f'</w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>')
    return "".join(p)


def sdt(eticheta, tag, placeholder=True):
    """Content control text, legat prin tag de numele campului Dataverse."""
    return (f'<w:sdt><w:sdtPr><w:alias w:val="{esc(eticheta)}"/>'
            f'<w:tag w:val="{esc(tag)}"/><w:id w:val="{abs(hash(tag)) % 90000000}"/>'
            f'<w:text/></w:sdtPr><w:sdtContent><w:r><w:t>'
            f'{"[" + esc(tag) + "]" if placeholder else ""}</w:t></w:r>'
            f'</w:sdtContent></w:sdt>')


def rand_tabel(eticheta, tag):
    return ('<w:tr>'
            f'<w:tc><w:tcPr><w:tcW w:w="3400" w:type="dxa"/></w:tcPr>'
            f'<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>{esc(eticheta)}</w:t></w:r></w:p></w:tc>'
            f'<w:tc><w:tcPr><w:tcW w:w="5600" w:type="dxa"/></w:tcPr>'
            f'<w:p>{sdt(eticheta, tag)}</w:p></w:tc>'
            '</w:tr>')


def tabel(randuri):
    return ('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/>'
            '<w:tblW w:w="9000" w:type="dxa"/>'
            '<w:tblBorders>'
            '<w:top w:val="single" w:sz="4" w:color="D0D0D0"/>'
            '<w:left w:val="single" w:sz="4" w:color="D0D0D0"/>'
            '<w:bottom w:val="single" w:sz="4" w:color="D0D0D0"/>'
            '<w:right w:val="single" w:sz="4" w:color="D0D0D0"/>'
            '<w:insideH w:val="single" w:sz="4" w:color="D0D0D0"/>'
            '<w:insideV w:val="single" w:sz="4" w:color="D0D0D0"/>'
            '</w:tblBorders></w:tblPr>'
            + "".join(randuri) + '</w:tbl>')


def document(cod, titlu, doccod, sectiuni):
    b = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
         f'<w:document {NS}><w:body>']
    b.append(par(titlu, bold=True, size="36"))
    b.append(par(f"{doccod} - sablon generat din blueprint, Sectiunea 5.5. "
                 f"Campurile marcate [rd_...] se completeaza automat de FLX-12.", size="18"))
    b.append(par(""))
    for titlu_sec, campuri in sectiuni:
        b.append(par(titlu_sec, bold=True, size="26"))
        randuri = []
        repetitive = []
        for eticheta, tag in campuri:
            if eticheta.startswith("REPETITIV_"):
                repetitive.append((eticheta.replace("REPETITIV_", ""), tag))
            else:
                randuri.append(rand_tabel(eticheta, tag))
        if randuri:
            b.append(tabel(randuri))
        for nume_rep, tag in repetitive:
            b.append(par(f"Tabel repetitiv: {nume_rep}", size="18"))
            b.append(f'<w:sdt><w:sdtPr><w:alias w:val="{nume_rep}"/>'
                     f'<w:tag w:val="{tag}"/><w:id w:val="{abs(hash(tag)) % 90000000}"/>'
                     f'<w:repeatingSection/></w:sdtPr><w:sdtContent>'
                     + tabel([rand_tabel("Element", tag + "_element")]) +
                     '</w:sdtContent></w:sdt>')
        b.append(par(""))
    b.append('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
             '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134"/>'
             '</w:sectPr></w:body></w:document>')
    return "".join(b)


CT = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''

RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''


def main():
    OUT.mkdir(exist_ok=True)
    index = []
    for cod, titlu, doccod, sectiuni in SABLOANE:
        cale = OUT / f"{cod}.docx"
        with zipfile.ZipFile(cale, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("[Content_Types].xml", CT)
            z.writestr("_rels/.rels", RELS)
            z.writestr("word/document.xml", document(cod, titlu, doccod, sectiuni))
        campuri = sum(len(c) for _, c in sectiuni)
        index.append({"cod": cod, "titlu": titlu, "document": doccod,
                      "sectiuni": len(sectiuni), "campuri": campuri,
                      "fisier": f"{cod}.docx"})
    (OUT / "_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1))
    print("SABLOANE WORD GENERATE")
    for i in index:
        print(f"  {i['cod']:10} {i['titlu'][:42]:44} {i['sectiuni']:2} sectiuni, "
              f"{i['campuri']:2} campuri")
    print(f"\n  Total: {len(index)} sabloane, "
          f"{sum(i['campuri'] for i in index)} content controls")
    print(f"  Iesire: {OUT}")


if __name__ == "__main__":
    main()
