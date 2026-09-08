# -*- coding: utf-8 -*-
"""Genereaza data/tabele.json din notatia compacta:
   "Nume coloana|nume_logic|Tip|O/-|valori|regula|observatii"
"""
import json, collections

def cols(block):
    out = []
    for line in block.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        p = (line.split("|") + [""] * 7)[:7]
        out.append(collections.OrderedDict([
            ("nume", p[0].strip()),
            ("nume_logic", p[1].strip()),
            ("tip", p[2].strip()),
            ("obligatoriu", p[3].strip() == "O"),
            ("valori", p[4].strip() or None),
            ("regula", p[5].strip() or None),
            ("observatii", p[6].strip() or None),
        ]))
    return out

T = []
def t(cod, nume, logic, primara, categorie, val, coloane, nota=None):
    e = collections.OrderedDict([
        ("cod", cod), ("nume", nume), ("nume_logic", logic),
        ("coloana_primara", primara), ("categorie", categorie), ("val", val),
    ])
    if nota:
        e["nota"] = nota
    e["coloane"] = cols(coloane)
    T.append(e)

t("TBL-01", "Solicitare (SCP)", "rd_solicitare", "rd_numarscp", "Tranzactionala", 1, """
Numar SCP|rd_numarscp|Autonumber|O|SCP-{AA}-{SEQ:0000}|Se genereaza la salvare|Coloana primara
Client|rd_client|Lookup (rd_client)|O|||Nu se accepta client liber
Lant sau canal|rd_canal|Choice|O|Choice CANAL||
KAM solicitant|rd_kam|Lookup (systemuser)|O||Implicit utilizatorul curent|Se pastreaza si daca omul pleaca
Sursa solicitarii|rd_sursa|Choice|O|Aplicatie / Mail preluat de suport R&D / Sedinta comerciala|Implicit Aplicatie|Varianta de rezerva se marcheaza explicit
Preluat de|rd_preluatde|Lookup (systemuser)|-||Obligatoriu daca sursa = Mail preluat|Business rule
Produs dorit|rd_produsdorit|Text (200)|O|||Denumire de lucru
Descriere cerinta|rd_descriere|Text Area (4000)|O|||Text liber de la client
Gramaj (g)|rd_gramaj|Decimal (2)|O|1 - 20000||Pe bucata
Numar bucati pe ambalaj|rd_bucatiambalaj|Whole Number|-|1 - 500||
Dimensiuni cerute|rd_dimensiuni|Text (100)|-|LxlxH mm||
Tip ambalare|rd_tipambalare|Choice|O|Choice AMBALARE||
Volum estimat anual (kg)|rd_volumanual|Decimal (2)|O|0 - 10000000|Intra in scorul de prioritate|Banda, nu liniar
Termen dorit de client|rd_termendorit|Date Only|O|>= azi||Nu este angajament
Termen impus extern|rd_termenimpus|Yes/No|O|Implicit Nu|Da doar cu tip si data|Listare, sezon
Tip termen impus|rd_tiptermenimpus|Choice|-|Listare retail / Sezon / Licitatie / Lansare client / Altul|Obligatoriu daca rd_termenimpus = Da|
Motivul cererii|rd_motivcerere|Choice|O|Choice MOTIVCERERE||
Referinta de comparatie|rd_tipreferinta|Choice|O|Choice TIPREFERINTA|Obligatoriu la deschidere|Vezi 6.4
Detalii referinta|rd_detaliireferinta|Text (300)|-||Obligatoriu daca referinta != Inexistenta|
Cerinte de eticheta|rd_cerinteeticheta|Text Area (2000)|-|||Limba, logo, declaratii
Cerinte de ambalaj|rd_cerinteambalaj|Text Area (2000)|-|||Material, print, dimensiune bax
Rezultat triaj|rd_rezultattriaj|Choice|-|Acceptata / Respinsa / Amanata|Numai rol Manager R&D|Vezi 2.1.1
Motiv triaj|rd_motivtriaj|Lookup (rd_motiv)|-||Obligatoriu daca rezultat != Acceptata|
Comentariu triaj|rd_comentariutriaj|Text Area (2000)|-||Obligatoriu daca rezultat = Respinsa|
Data triaj|rd_datatriaj|Date and Time|-||Automat la salvarea rezultatului|User Local
Amanata pana la|rd_amanatapanala|Date Only|-|> azi|Obligatoriu daca rezultat = Amanata|Reintra automat in coada (FLX-14)
Proiect generat|rd_proiect|Lookup (rd_proiect)|-||Completat de FLX-01|Referential
Status solicitare|rd_statussolicitare|Choice|O|Ciorna / Trimisa / In triaj / Acceptata / Respinsa / Amanata|Implicit Ciorna|Choice local
""")

t("TBL-02", "Proiect CDI", "rd_proiect", "rd_codproiect", "Radacina", 1, """
Cod proiect|rd_codproiect|Autonumber|O|{AA}{SEQ:000}, exemplu 26025|Generat la acceptare, succesiv pe an|Coloana primara, imutabila
Nume produs|rd_numeprodus|Text (200)|O|||Intra in numele folderului
Denumire completa|rd_denumire|Calculated (Text)|O|{cod}_{nume produs}|Calculata|Folosita in denumirea fisierelor
Solicitare sursa|rd_solicitare|Lookup (rd_solicitare)|-|||Referential
Proiect parinte|rd_proiectparinte|Lookup (rd_proiect)|-||Doar pentru versiuni cu sufix .1|Auto-referential, vezi 2.2.2
Sufix versiune|rd_sufixversiune|Text (10)|-|.1, .2, ...|Obligatoriu daca exista parinte|
Tip proiect|rd_tipproiect|Choice|O|Choice TIPPROIECT||
Client|rd_client|Lookup (rd_client)|O||Se preia din solicitare|
KAM|rd_kam|Lookup (systemuser)|O||Se preia din solicitare|
Tehnolog alocat|rd_tehnolog|Lookup (systemuser)|-||Obligatoriu la Acceptat - planificat|Vezi 2.22
Manager R&D|rd_manager|Lookup (systemuser)|O||Implicit managerul de departament|
Linie de productie vizata|rd_linie|Lookup (rd_linie)|-||Obligatoriu la In dezvoltare|Una din cele 9
Amplasament|rd_amplasament|Choice|O|Choice AMPLASAMENT|Se preia din linie|
Status|rd_status|Choice|O|Choice STATUSPROIECT|Tranzitii controlate de business rule|Vezi 2.2.1
Motiv status|rd_motivstatus|Lookup (rd_motiv)|-||Obligatoriu pentru Respins, Suspendat, Abandonat, Blocat|
Gramaj (g)|rd_gramaj|Decimal (2)|O|1 - 20000|Diferenta de gramaj = proiect nou|Vezi 2.2.3
Dimensiuni|rd_dimensiuni|Text (100)|-||Diferenta de dimensiune = proiect nou|
Tip ambalare|rd_tipambalare|Choice|O|Choice AMBALARE||
Volum estimat anual (kg)|rd_volumanual|Decimal (2)|O|0 - 10000000|Intra in scor|
Ambalaj nou|rd_ambalajnou|Yes/No|O|Implicit Nu|Conditia C4 de aplicabilitate|
Are materie prima noua|rd_aremp|Yes/No|O|Implicit Nu|Scris de flux din liniile de MP|Conditioneaza livrabilele C1
Numar MP noi|rd_numarmpnoi|Rollup (Count)|-|0 - n|Numara rd_mpproiect cu rd_estenoua = Da|Rollup
Termen propus|rd_termenpropus|Date Only|-||Generat de FLX-03|Nu se editeaza manual
Termen negociat|rd_termennegociat|Date Only|-||Rezultatul discutiei cu KAM|Termenul catre client
Termen realizat|rd_termenrealizat|Date Only|-||Se scrie la trecerea in Finalizat|
Abatere fata de termen (zile)|rd_abateretermen|Whole Number|-|-999 - 999|realizat - negociat|Scris de flux
Data acceptare|rd_dataacceptare|Date Only|-||Se scrie la generarea codului|Start ceas
Durata standard (zile)|rd_duratastandard|Whole Number|O|1 - 365, implicit 14|Din sablonul de etape|Vezi Sectiunea 14
Zile blocate cumulat|rd_zileblocate|Rollup (Sum)|-|0 - 999|Suma impactului din blocaje inchise|Vezi 2.8
T-Total zile nete|rd_ttotalnet|Whole Number|-||(realizat - acceptare) - zile blocate|Scris de FLX-16
Scor prioritate|rd_scorprioritate|Whole Number|-|0 - 100|Recalculat saptamanal de FLX-10|Nu se editeaza manual
Banda prioritate|rd_banda|Choice|-|Choice BANDA|Derivata din scor|Vezi 2.2.4
Scor suprascris|rd_scorsuprascris|Whole Number|-|0 - 100|Doar rol Comercial Manager|Audit obligatoriu
Motiv suprascriere|rd_motivsuprascriere|Text Area (1000)|-||Obligatoriu daca exista scor suprascris|Business rule
Data suprascrierii|rd_datasuprascriere|Date and Time|-||Automat|
Zile in coada|rd_zilecoada|Whole Number|-|0 - 999|azi - data acceptare, cat timp nu e In dezvoltare|Alimenteaza imbatranirea
Referinta de comparatie|rd_referinta|Lookup (rd_referinta)|-||Obligatorie la deschidere|Vezi 2.12
Cod material SAP produs finit|rd_codsapfinit|Text (20)|-||Se introduce dupa creare in SAP|Niciodata scriere in SAP
Data cod SAP|rd_datacodsap|Date Only|-|||
Slot testare propus|rd_slottestare|Date Only|-||Estimare negociabila, nu blocanta|Vezi A1.2.7
Schimb propus|rd_schimb|Choice|-|Choice SCHIMB||
Folder SharePoint|rd_folderurl|Text (500)|-|URL|Scris de FLX-02|
Procent livrabile realizate|rd_procentlivrabile|Decimal (2)|-|0 - 100|Realizate / obligatorii aplicabile|Scris de FLX-05
Toate livrabilele obligatorii OK|rd_livrabileok|Yes/No|-||Conditie pentru trecerea in Finalizat|Business rule
Urmatorul livrabil|rd_urmatorullivrabil|Text (150)|-||Scris de FLX-05|Cerinta 2.2.1.1
Urmatorul responsabil|rd_urmatorulresponsabil|Lookup (systemuser)|-||Scris de FLX-05|Cerinta 2.2.1.1
Data ultimei activitati|rd_ultimaactivitate|Date and Time|-||Scris la orice modificare de copil|Detecteaza proiecte uitate
Importat la migrare|rd_importat|Yes/No|O|Implicit Nu|Exclude proiectul din indicatori|Vezi 15.3.3.2
""")

t("TBL-03", "Livrabil de proiect", "rd_livrabil", "rd_name", "Copil", 1, """
Denumire livrabil|rd_name|Text (150)|O||Se preia din sablon|Coloana primara
Cod livrabil|rd_codlivrabil|Text (10)|O|LIV-01 ... LIV-43|Din sablon|Pentru raportare stabila
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Sablon sursa|rd_sablon|Lookup (rd_sablonlivrabil)|-|||Trasabilitate
Faza|rd_faza|Choice|O|Choice FAZA|Din sablon|
Ordine in faza|rd_ordine|Whole Number|O|1 - 99|Din sablon|Sortare
Responsabil rol|rd_rolresponsabil|Choice|O|Choice ROL|Din sablon|Cine datoreaza livrabilul
Responsabil persoana|rd_responsabil|Lookup (systemuser)|-||Rezolvat din rol la generare|Poate fi reatribuit
Obligatoriu|rd_obligatoriu|Yes/No|O||Din sablon|Vezi 4.3
Conditie de aplicabilitate|rd_conditie|Choice|O|C0 ... C7|Din sablon|Vezi 4.2
Aplicabil|rd_aplicabil|Yes/No|O|Implicit Da|Evaluat de FLX-05|Cele neaplicabile raman vizibile
Termen|rd_termen|Date Only|-||Calculat din etapa si offset|Editabil de manager
Data realizarii|rd_datarealizare|Date Only|-||Se scrie la trecerea in Realizat|
Status livrabil|rd_statuslivrabil|Choice|O|Choice STATUSLIVRABIL|Implicit Neinceput|
Document atasat|rd_document|Text (500)|-|URL SharePoint|Completat la incarcarea fisierului|Vezi 2.3.1
Necesita document|rd_necesitadocument|Yes/No|O||Nu trece in Realizat fara document|Business rule
Aprobator|rd_aprobator|Lookup (systemuser)|-||Din sablon (rol)|
Data aprobarii|rd_dataaprobare|Date Only|-|||
Zile intarziere|rd_zileintarziere|Whole Number|-|0 - 999|max(0, azi - termen) daca nu e realizat|Scris de FLX-08
Observatii|rd_observatii|Text Area (2000)|-|||
""")

t("TBL-04", "Sablon de livrabil", "rd_sablonlivrabil", "rd_name", "Configurare", 0, """
Denumire|rd_name|Text (150)|O|||Coloana primara
Cod livrabil|rd_codlivrabil|Text (10)|O|LIV-nn|Unic|
Tip proiect aplicabil|rd_tipproiect|Choice (multi)|O|Choice TIPPROIECT|Filtreaza sablonul|Multi-select
Faza|rd_faza|Choice|O|Choice FAZA||
Ordine|rd_ordine|Whole Number|O|1 - 99||
Etapa asociata|rd_etapa|Lookup (rd_sablonetapa)|-||Din ea se ia termenul|
Offset termen (zile)|rd_offsettermen|Whole Number|O|0 - 365|Zile de la data de acceptare|
Offset fata de implementare|rd_offsetimplementare|Whole Number|-|0 - 365|Pentru LIV-41 ... LIV-43|Vezi 4.6.3
Rol responsabil|rd_rolresponsabil|Choice|O|Choice ROL||
Rol aprobator|rd_rolaprobator|Choice|-|Choice ROL||
Obligatoriu|rd_obligatoriu|Yes/No|O||Vezi 4.3|
Necesita document|rd_necesitadocument|Yes/No|O|||
Conditie de aplicabilitate|rd_conditie|Choice|O|C0 ... C7||
Sablon Word|rd_sablonword|Text (300)|-|Cod tip document|Pentru generarea documentului|Vezi FLX-12
Activ|rd_activ|Yes/No|O|Implicit Da|Sablonul dezactivat nu mai genereaza|Istoricul ramane
""")

t("TBL-05", "Etapa de proiect", "rd_etapa", "rd_name", "Copil", 1, """
Denumire|rd_name|Text (100)|O||Din sablon|Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Sablon|rd_sablon|Lookup (rd_sablonetapa)|-|||
Ordine|rd_ordine|Whole Number|O|1 - 20||
Data start planificata|rd_startplanificat|Date Only|O||Din offset|
Data final planificata|rd_finalplanificat|Date Only|O||Start + durata|
Data start reala|rd_startreal|Date Only|-||La prima activitate reala pe etapa|Vezi 14.3.3
Data final reala|rd_finalreal|Date Only|-||La inchiderea etapei|
Durata reala bruta (zile)|rd_duratabruta|Whole Number|-||final real - start real|Scris de flux
Zile blocate pe etapa|rd_zileblocate|Rollup (Sum)|-|0 - 999|Din blocajele legate de etapa|
Durata reala neta (zile)|rd_duratanet|Whole Number|-||bruta - blocate|Baza pentru T-Total
Abatere fata de standard|rd_abatere|Whole Number|-|-99 - 999|neta - durata standard|Alimenteaza Sectiunea 14
Status etapa|rd_statusetapa|Choice|O|Choice STATUSETAPA||
Motiv sarire|rd_motivsarire|Text (300)|-||Obligatoriu daca status = Sarita|
""")

t("TBL-06", "Sablon de etapa", "rd_sablonetapa", "rd_name", "Configurare", 0, """
Denumire etapa|rd_name|Text (100)|O|||Coloana primara
Cod etapa|rd_codetapa|Text (10)|O|ETP-nn|Unic|
Ordine|rd_ordine|Whole Number|O|1 - 20||
Tip proiect|rd_tipproiect|Choice (multi)|O|Choice TIPPROIECT||
Durata standard (zile lucratoare)|rd_duratastandard|Whole Number|O|1 - 90|Vezi Sectiunea 14|Setata o data la configurare
Durata propusa de sistem|rd_duratapropusa|Decimal (1)|-||Mediana duratelor reale|Scrisa de FLX-17, nu se aplica automat
Rol responsabil|rd_rolresponsabil|Choice|O|Choice ROL||
Opreste ceasul la blocaj|rd_oprsteceasul|Yes/No|O|Implicit Da||
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-07", "Materie prima de proiect", "rd_mpproiect", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (200)|O|||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Materie prima catalog|rd_materieprima|Lookup (rd_materieprima)|-||Gol daca este MP complet noua|
Este noua|rd_estenoua|Yes/No|O|Implicit Nu|Da declanseaza livrabilele C1|Scrie rd_aremp pe proiect
Categorie|rd_categorie|Choice|O|Choice CATEGORIEMP||
Cantitate in reteta (kg/100kg)|rd_cantitate|Decimal (4)|-|0 - 100||Pentru faza de plan
Furnizor propus|rd_furnizor|Lookup (rd_furnizor)|-|||
Status ciclu MP|rd_statusmp|Choice|O|Choice STATUSMP|Vezi 4.4|
Initiator cerere mostra|rd_initiator|Choice|-|R&D / Achizitii||Ambele pot initia
Tip lead time|rd_tipleadtime|Choice|-|Pe stoc / In portofoliu furnizor / Achizitie noua / Import sau caz special|Determina lead time implicit|Vezi 2.6.2
Lead time asumat (zile)|rd_leadtime|Whole Number|-|0 - 365|Implicit din tip, editabil de Achizitii|
ETA confirmat|rd_eta|Date Only|-||Se introduce doar de Achizitii|Modificarea declanseaza FLX-07
ETA initial|rd_etainitial|Date Only|-||Primul ETA confirmat, nu se mai schimba|Masoara alunecarea
Numar modificari ETA|rd_modificarieta|Whole Number|-|0 - 99|Incrementat de flux|Indicator de furnizor
Data receptiei|rd_datareceptie|Date Only|-|||
Cod SAP MP|rd_codsapmp|Text (20)|-||Creat de Achizitii in SAP|Niciodata scriere in SAP
Numar iteratii|rd_numariteratii|Rollup (Count)|-|0 - 99|Din rd_iteratiefurnizor|
Critica pentru proiect|rd_critica|Yes/No|O|Implicit Da|Daca Da, intarzierea opreste proiectul|
Observatii|rd_observatii|Text Area (2000)|-|||
""")

t("TBL-08", "Iteratie de furnizor", "rd_iteratiefurnizor", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (150)|O|{MP}_{Furnizor}_it{n}|Generata|Coloana primara
Materie prima de proiect|rd_mpproiect|Lookup (rd_mpproiect)|O||Parental|
Numar iteratie|rd_numar|Whole Number|O|1 - 99|Succesiv pe MP|
Furnizor|rd_furnizor|Lookup (rd_furnizor)|O|||
Denumire comerciala oferta|rd_denumireoferta|Text (200)|-|||Varianta furnizorului
Data cererii de mostra|rd_datacerere|Date Only|-|||
Data primirii mostrei|rd_dataprimire|Date Only|-|||
Rezultat|rd_rezultat|Choice|O|Choice REZULTATITERATIE||
Motiv respingere|rd_motivrespingere|Lookup (rd_motiv)|-||Obligatoriu daca rezultat contine Respinsa|
Detalii respingere|rd_detalii|Text Area (2000)|-|||
Pret oferit|rd_pret|Currency (4)|-|||Securitate pe coloana
Data deciziei|rd_datadecizie|Date Only|-|||
""")

t("TBL-09", "Materie prima (catalog)", "rd_materieprima", "rd_name", "Nomenclator", 1, """
Denumire|rd_name|Text (200)|O|||Coloana primara
Cod SAP|rd_codsap|Text (20)|-||Unic daca exista|Import din SAP, read-only
Categorie|rd_categorie|Choice|O|Choice CATEGORIEMP||
Furnizor principal|rd_furnizor|Lookup (rd_furnizor)|-|||
Unitate de masura|rd_um|Choice|O|Choice UM||
Pret curent|rd_pret|Currency (4)|-||Actualizat manual sau prin import|Alimenteaza antecalculul
Data pretului|rd_datapret|Date Only|-|||Semnaleaza preturi vechi
Alergeni continuti|rd_alergeni|Choice (multi)|O|Choice ALERGEN (14 valori)||Vezi Sectiunea 9
Alergeni pe urme|rd_alergeniurme|Choice (multi)|-|Choice ALERGEN|Din declaratia furnizorului|Vezi 9.4
Energie (kcal/100g)|rd_energie|Decimal (2)|-|0 - 900|Din ST furnizor|
Grasimi (g/100g)|rd_grasimi|Decimal (2)|-|0 - 100||
din care acizi grasi saturati|rd_saturate|Decimal (2)|-|0 - 100|<= rd_grasimi|
Glucide (g/100g)|rd_glucide|Decimal (2)|-|0 - 100||
din care zaharuri|rd_zaharuri|Decimal (2)|-|0 - 100|<= rd_glucide|
Fibre (g/100g)|rd_fibre|Decimal (2)|-|0 - 100||
Proteine (g/100g)|rd_proteine|Decimal (2)|-|0 - 100||
Sare (g/100g)|rd_sare|Decimal (4)|-|0 - 100||
Umiditate (%)|rd_umiditate|Decimal (2)|-|0 - 100|Necesara pentru randament|
Suma macronutrienti|rd_summacro|Calculated (Decimal)|-|0 - 105|grasimi + glucide + fibre + proteine + sare + umiditate|Validare de plauzibilitate 95-105
Ingrediente compuse|rd_ingredientecompuse|Text Area (2000)|-||Obligatoriu daca MP este un compus|Vezi 9.1.4
Denumire legala pe eticheta|rd_denumirelegala|Text (200)|-|||Pentru lista de ingrediente
Data ultimei ST furnizor|rd_datast|Date Only|-||ST mai veche de 24 de luni se semnaleaza|Cerinta IFS
Status|rd_statusmp|Choice|O|Activa / In evaluare / Blocata / Iesita din uz||
Bio / ecologic|rd_bio|Yes/No|-|||
Origine|rd_origine|Text (100)|-||Pentru declaratii de origine|
""")

t("TBL-10", "Furnizor", "rd_furnizor", "rd_name", "Nomenclator", 2, """
Denumire|rd_name|Text (200)|O|||Coloana primara
Cod SAP furnizor|rd_codsap|Text (20)|-|||Import
Tip|rd_tipfurnizor|Choice|O|Producator / Distribuitor / Broker / Intern||
Aprobat Calitate|rd_aprobat|Yes/No|O|Implicit Nu|Nu se comanda de la furnizor neaprobat|Cerinta IFS
Data aprobarii|rd_dataaprobare|Date Only|-|||
Certificari|rd_certificari|Choice (multi)|-|IFS / BRC / FSSC 22000 / ISO 22000 / Bio / Halal / Kosher||
Expirare certificare|rd_expirarecertificare|Date Only|-||Alerta cu 60 de zile inainte|FLX-21
Persoana de contact|rd_contact|Text (150)|-|||
Email contact|rd_email|Text (150)|-|Format email||
Lead time mediu real (zile)|rd_leadtimemediu|Decimal (1)|-||Calculat din iteratii incheiate|Indicator de furnizor
Rata de respingere (%)|rd_ratarespingere|Decimal (2)|-|0 - 100|Iteratii respinse / total|Scris de flux
""")

t("TBL-11", "Blocaj", "rd_blocaj", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (150)|O|||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Etapa afectata|rd_etapa|Lookup (rd_etapa)|-||Referential|Pentru durata neta pe etapa
Cine blocheaza|rd_sursablocaj|Choice|O|Choice SURSABLOCAJ||
Categorie blocaj|rd_categorie|Choice|O|Asteptare mostra / Asteptare decizie / Asteptare aprobare / Indisponibilitate linie / Indisponibilitate MP / Lipsa specificatie / Lipsa ambalaj / Altul||
Data start|rd_datastart|Date Only|O|<= azi||
Data sfarsit|rd_datasfarsit|Date Only|-|>= data start|Gol = blocaj activ|
Impact in zile|rd_impactzile|Whole Number|-|0 - 999|Zile lucratoare intre start si sfarsit|Scris de FLX-09
Opreste ceasul R&D|rd_oprsteceas|Yes/No|O|Implicit Da pentru surse externe|Intern R&D = Nu|Vezi 2.8.1
Termen client afectat|rd_afecteazaclient|Yes/No|O|Implicit Da|Termenul catre client curge oricum|Vezi 13.2.3
Descriere|rd_descriere|Text Area (2000)|O|||
Actiune de deblocare|rd_actiune|Text Area (2000)|-|||
Responsabil deblocare|rd_responsabil|Lookup (systemuser)|-|||
Activ|rd_activ|Calculated (Yes/No)|-||Da daca rd_datasfarsit este gol|
""")

t("TBL-12", "Cerere de mostra", "rd_ceremostra", "rd_name", "Copil", 2, """
Numar cerere|rd_name|Autonumber|O|CM-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Tip mostra|rd_tipmostra|Choice|O|Choice TIPMOSTRA||
Materie prima de proiect|rd_mpproiect|Lookup (rd_mpproiect)|-||Obligatoriu daca tip = Materie prima|
Solicitant|rd_solicitant|Lookup (systemuser)|O|||
Rol solicitant|rd_rolsolicitant|Choice|O|R&D / Achizitii|Ambele pot initia|
Destinatar|rd_destinatar|Choice|O|Intern laborator / Client / Furnizor / Panel senzorial||
Cantitate ceruta|rd_cantitate|Decimal (2)|O|> 0||
Unitate de masura|rd_um|Choice|O|Choice UM||
Data ceruta|rd_dataceruta|Date Only|O|>= azi||
Status cerere|rd_statuscerere|Choice|O|Ciorna / Trimisa / Confirmata / In transport / Livrata / Anulata||
Data livrarii|rd_datalivrare|Date Only|-|||
Adresa de livrare|rd_adresa|Text Area (500)|-||Obligatorie daca destinatar = Client|
Curier si AWB|rd_awb|Text (100)|-|||
Observatii|rd_observatii|Text Area (2000)|-|||
""")

t("TBL-13", "Miscare de mostra", "rd_miscaremostra", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (150)|O||Generata|Coloana primara
Cerere de mostra|rd_ceremostra|Lookup (rd_ceremostra)|O||Parental|
Tip miscare|rd_tipmiscare|Choice|O|Pregatita / Predata la transport / Expediata / Receptionata / Returnata / Distrusa||
Data si ora|rd_datamiscare|Date and Time|O||Implicit acum|User Local
Persoana|rd_persoana|Lookup (systemuser)|O||Implicit utilizator curent|
Cantitate|rd_cantitate|Decimal (2)|-|> 0||
Temperatura la receptie (C)|rd_temperatura|Decimal (1)|-|-40 - 40|Obligatorie la receptie de congelat|Cerinta HACCP
Conform|rd_conform|Yes/No|-||Obligatoriu la receptie|
Motiv neconformitate|rd_motiv|Text (300)|-||Obligatoriu daca conform = Nu|
Poza|rd_poza|Image|-||Din canvas mobil|Vezi ECR-13
""")

t("TBL-14", "Fisa de testare", "rd_fisatestare", "rd_name", "Copil", 1, """
Numar fisa|rd_name|Autonumber|O|FT-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Obiectivul testarii|rd_obiectiv|Text Area (2000)|O|||
Versiune reteta testata|rd_versiunereteta|Lookup (rd_versiunereteta)|O|||
Linie|rd_linie|Lookup (rd_linie)|-|||
Data planificata|rd_dataplanificata|Date Only|O|||
Parametri de proces tinta|rd_parametritinta|Text Area (4000)|-|||Preluati in trial
Tolerante declarate|rd_tolerante|Text Area (2000)|O||Baza pentru conformitatea masuratorilor|Vezi 6.3
Status fisa|rd_statusfisa|Choice|O|Ciorna / Aprobata / In executie / Finalizata / Anulata||
Aprobator|rd_aprobator|Lookup (systemuser)|-|||
Concluzie|rd_concluzie|Text Area (4000)|-||Obligatorie la Finalizata|
""")

t("TBL-15", "Trial", "rd_trial", "rd_name", "Copil", 1, """
Numar trial|rd_name|Autonumber|O|TR-{AA}-{SEQ:0000}||Coloana primara
Fisa de testare|rd_fisatestare|Lookup (rd_fisatestare)|O||Parental|
Proiect|rd_proiect|Lookup (rd_proiect)|O||Denormalizat pentru raportare|Scris de flux, REL-43
Numar incercare|rd_numarincercare|Whole Number|O|1 - 99|Succesiv pe fisa|
Data si ora start|rd_start|Date and Time|O|||User Local
Data si ora final|rd_final|Date and Time|-|||
Linie|rd_linie|Lookup (rd_linie)|O|||
Schimb|rd_schimb|Choice|O|Choice SCHIMB||
Operator|rd_operator|Text (150)|-||Nu toti operatorii au cont|Text, nu lookup
Cantitate aluat (kg)|rd_cantitatealuat|Decimal (2)|-|> 0||
Bucati obtinute|rd_bucatiobtinute|Whole Number|-|>= 0||
Randament (%)|rd_randament|Decimal (2)|-|0 - 120|(bucati x gramaj) / (aluat x 1000) x 100|Vezi 7.2
Temperatura aluat (C)|rd_tempaluat|Decimal (1)|-|0 - 40||Parametru critic la laminare
Timp framantare (min)|rd_timpframantare|Decimal (1)|-|0 - 120||
Timp fermentare (min)|rd_timpfermentare|Decimal (1)|-|0 - 600||
Grosime laminare (mm)|rd_grosimelaminare|Decimal (2)|-|0 - 100||Fritsch / Rademaker
Timp dospire (min)|rd_timpdospire|Decimal (1)|-|0 - 600||
Temperatura dospire (C)|rd_tempdospire|Decimal (1)|-|0 - 60||
Temperatura coacere (C)|rd_tempcoacere|Decimal (1)|-|0 - 350||WP tunel
Timp coacere (min)|rd_timpcoacere|Decimal (1)|-|0 - 120||
Temperatura congelare (C)|rd_tempcongelare|Decimal (1)|-|-45 - 0||JBT shockfreezer
Timp congelare (min)|rd_timpcongelare|Decimal (1)|-|0 - 300||
Temperatura in centru la iesire (C)|rd_tempcentru|Decimal (1)|-|-40 - 20|Punct critic HACCP|Vezi 7.5.2
Rezultat trial|rd_rezultat|Choice|O|Choice REZULTATTRIAL||
Observatii|rd_observatii|Text Area (4000)|-||Obligatorii daca rezultat = Nereusit|
Numar masuratori|rd_numarmasuratori|Rollup (Count)|-|||
""")

t("TBL-16", "Masuratoare", "rd_masuratoare", "rd_name", "Copil", 1, """
Denumire|rd_name|Text (150)|O||Generata|Coloana primara
Trial|rd_trial|Lookup (rd_trial)|O||Parental|
Tip masuratoare|rd_tipmasuratoare|Choice|O|Choice TIPMASURATOARE||
Numar bucata|rd_numarbucata|Whole Number|O|1 - 50|Succesiv in cadrul tipului|
Valoare numerica|rd_valoare|Decimal (3)|-||Obligatorie pentru tipuri numerice|
Valoare calitativa|rd_valoarecalitativa|Choice|-|Conform / Minor neconform / Neconform|Obligatorie pentru aspect, miros, gust, alveolare|
Unitate de masura|rd_um|Choice|O|g / mm / ml / C / % / scor|Implicit din tip|
Valoare tinta|rd_tinta|Decimal (3)|-||Din fisa de testare|
Toleranta minus|rd_tolminus|Decimal (3)|-||Din fisa de testare|
Toleranta plus|rd_tolplus|Decimal (3)|-||Din fisa de testare|
Conform|rd_conform|Calculated (Yes/No)|-||valoare intre tinta-tolminus si tinta+tolplus|Vezi 6.3
Data si ora|rd_datamasurare|Date and Time|O|Implicit acum||User Local
Masurat de|rd_masuratde|Lookup (systemuser)|O|Implicit utilizator curent||
Poza|rd_poza|Image|-||Din canvas mobil|Comprimata la 1024px
Exclus din statistica|rd_exclus|Yes/No|O|Implicit Nu|Doar cu motiv|Vezi 6.2.4
Motiv excludere|rd_motivexcludere|Text (300)|-||Obligatoriu daca exclus = Da|Din lista 6.2.4.3
Observatii|rd_observatii|Text (500)|-|||
""")

t("TBL-16b", "Statistica de trial", "rd_statisticatrial", "rd_name", "Derivata", 1, """
Denumire|rd_name|Text (150)|O|{Trial}_{Tip}||Coloana primara
Trial|rd_trial|Lookup (rd_trial)|O||Parental|
Tip masuratoare|rd_tipmasuratoare|Choice|O|Choice TIPMASURATOARE|Unic pe trial|
Numar valori|rd_n|Whole Number|O|1 - 50|Fara cele excluse|
Media|rd_medie|Decimal (3)|O|||
Abatere standard|rd_abaterestandard|Decimal (4)|-|>= 0|Esantion, n-1|Vezi 6.1.5
Coeficient de variatie (%)|rd_cv|Decimal (2)|-|0 - 100|abatere / medie x 100|Vezi 6.2.3
Minim|rd_minim|Decimal (3)|O|||
Maxim|rd_maxim|Decimal (3)|O|||
Numar neconforme|rd_neconforme|Whole Number|O|0 - 50||
Conformitate lot (%)|rd_conformitate|Decimal (2)|O|0 - 100|conforme / n x 100|
Verdict|rd_verdict|Choice|O|Conform / Conform cu observatii / Neconform / Esantion insuficient|Vezi 6.3.2|
""", nota="PROPUNERE: tabela separata pentru ca Rollup Dataverse nu calculeaza abatere standard (2.10.4). Scrisa de FLX-11.")

t("TBL-17", "Evaluare senzoriala", "rd_evaluaresenzoriala", "rd_name", "Copil", 2, """
Numar evaluare|rd_name|Autonumber|O|ES-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Trial evaluat|rd_trial|Lookup (rd_trial)|-||Referential|
Tip evaluare|rd_tipevaluare|Choice|O|Interna R&D / Panel extins / Cu clientul / Comparativa cu referinta / Shelf life||
Data|rd_data|Date Only|O|||
Numar evaluatori|rd_numarevaluatori|Rollup (Count)|-|1 - 20|Distinct pe rd_scorsenzorial|Vezi 6.5.3
Referinta comparata|rd_referinta|Lookup (rd_referinta)|-||Obligatorie daca tip = Comparativa|
Scor total ponderat|rd_scortotal|Decimal (2)|-|1 - 5|Media ponderata a scorurilor|Scris de FLX-11
Scor referinta|rd_scorreferinta|Decimal (2)|-|1 - 5|Idem, pe referinta|
Diferenta fata de referinta|rd_diferenta|Decimal (2)|-|-4 - 4|scor total - scor referinta|Vezi 6.5.5.1
Dezacord maxim|rd_dezacord|Decimal (2)|-|0 - 4|Amplitudinea maxima pe un criteriu|Vezi 6.5.4
Verdict|rd_verdict|Choice|O|Choice VERDICT|Vezi 6.5.5|
Actiuni cerute|rd_actiuni|Text Area (4000)|-||Obligatorii daca verdict != Acceptat|
Conditii de degustare|rd_conditii|Text Area (1000)|-||Temperatura, timp de la coacere|Cerinta de repetabilitate
""")

t("TBL-18", "Criteriu senzorial", "rd_criteriusenzorial", "rd_name", "Nomenclator", 2, """
Denumire criteriu|rd_name|Text (100)|O|||Coloana primara
Cod|rd_cod|Text (10)|O|CR-nn|Unic|
Grupa|rd_grupa|Choice|O|Aspect exterior / Structura interna / Textura / Aroma si gust / Comportament la utilizare||
Pondere (%)|rd_pondere|Decimal (2)|O|0 - 100|Suma pe categoria de produs = 100|Vezi 6.5.1
Categorie produs|rd_categorieprodus|Choice|O|Foietaj / Aluat dospit / Patiserie cu umplutura / Paine / Produs gata copt / Produs bake-off|Grile diferite pe categorie|
Ancora scor 1|rd_ancora1|Text (300)|O||Descriere, nu cifra|Vezi 6.5.2
Ancora scor 3|rd_ancora3|Text (300)|O|||
Ancora scor 5|rd_ancora5|Text (300)|O|||
Eliminatoriu sub|rd_eliminatoriusub|Whole Number|-|1 - 5|Scor sub prag = respins automat|Vezi 6.5.5
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-19", "Scor senzorial", "rd_scorsenzorial", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (150)|O||Generata|Coloana primara
Evaluare|rd_evaluare|Lookup (rd_evaluaresenzoriala)|O||Parental|
Criteriu|rd_criteriu|Lookup (rd_criteriusenzorial)|O|||
Evaluator|rd_evaluator|Lookup (systemuser)|O||Unic impreuna cu criteriu si tinta|
Tinta scorului|rd_tintascor|Choice|O|Produs dezvoltat / Referinta|Permite comparatia pe acelasi ecran|
Scor|rd_scor|Whole Number|O|1 - 5||
Comentariu|rd_comentariu|Text (500)|-||Obligatoriu daca scor <= 2|Business rule
""")

t("TBL-20a", "Defect (nomenclator)", "rd_defect", "rd_name", "Nomenclator", 2, """
Denumire|rd_name|Text (150)|O|||Coloana primara
Cod|rd_cod|Text (10)|O|DF-nn|Unic|
Grupa|rd_grupa|Choice|O|Aluat / Laminare / Dospire / Coacere / Congelare / Ambalare / Materie prima||
Descriere|rd_descriere|Text Area (1000)|-|||
Severitate implicita|rd_severitate|Choice|O|Minor / Major / Critic||
Cauza probabila|rd_cauza|Text Area (1000)|-|||
Punct critic HACCP|rd_ccp|Yes/No|-|||
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-20b", "Defect constatat", "rd_defectconstatat", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (150)|O||Generata|Coloana primara
Evaluare|rd_evaluare|Lookup (rd_evaluaresenzoriala)|O||Parental|
Defect|rd_defect|Lookup (rd_defect)|O|||
Severitate|rd_severitate|Choice|O|Minor / Major / Critic|Implicit din nomenclator|Critic = verdict Respins
Numar bucati afectate|rd_bucatiafectate|Whole Number|-|0 - 999||
Procent afectat|rd_procentafectat|Decimal (2)|-|0 - 100||
Poza|rd_poza|Image|-|||
Observatii|rd_observatii|Text Area (1000)|-|||
""")

t("TBL-21", "Referinta de comparatie", "rd_referinta", "rd_name", "Copil", 1, """
Denumire|rd_name|Text (200)|O|||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Tip referinta|rd_tipreferinta|Choice|O|Choice TIPREFERINTA||
Client asociat|rd_client|Lookup (rd_client)|-|||
Producator|rd_producator|Text (150)|-||Pentru produs concurenta|
Cod produs actual|rd_codprodusactual|Text (20)|-||Cod SAP daca este produs propriu|
Gramaj (g)|rd_gramaj|Decimal (2)|-|||
Gramaj masurat real (g)|rd_gramajmasurat|Decimal (2)|-||Minimum 5 bucati la produs concurenta|Vezi 6.4.4
Pret raft|rd_pretraft|Currency (2)|-||Pentru pozitionare|
Data achizitiei referintei|rd_dataachizitie|Date Only|-|||
Lista de ingrediente|rd_ingrediente|Text Area (4000)|-||De pe eticheta|
Valori nutritionale declarate|rd_nutritionale|Text Area (2000)|-|||
Poza|rd_poza|Image|-|||
Documente|rd_documenteurl|Text (500)|-||Folder in 00_Solicitare|
""")

t("TBL-22", "Antecalcul", "rd_antecalcul", "rd_name", "Copil", 2, """
Numar antecalcul|rd_name|Autonumber|O|AC-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Versiune reteta|rd_versiunereteta|Lookup (rd_versiunereteta)|O|||
Versiune antecalcul|rd_versiune|Whole Number|O|1 - 99|Succesiv pe proiect|
Data calculului|rd_datacalcul|Date Only|O|||
Linie de productie|rd_linie|Lookup (rd_linie)|O||Determina tariful si viteza|
Gramaj (g)|rd_gramaj|Decimal (2)|O||Din proiect|
Cost materii prime / kg|rd_costmp|Currency (4)|-||Suma liniilor de antecalcul|Rollup
Pierdere tehnologica (%)|rd_pierdere|Decimal (2)|O|0 - 30, implicit 3|Din date de linie|
Cost MP ajustat / kg|rd_costmpajustat|Decimal (4)|-||cost MP / (1 - pierdere/100)|
Cost ambalaj / buc|rd_costambalaj|Currency (4)|-|||
Cost manopera / kg|rd_costmanopera|Currency (4)|-||Tarif linie x timp / cantitate|
Cost energie si utilitati / kg|rd_costenergie|Currency (4)|-||Din tariful liniei|
Cost congelare / kg|rd_costcongelare|Currency (4)|-||Separat, pentru comparabilitate|PROPUNERE
Regie / kg|rd_regie|Currency (4)|-||Procent din costul direct|
Cost total / kg|rd_costtotal|Currency (4)|-||Suma componentelor|Securitate pe coloana
Cost total / buc|rd_costbuc|Currency (4)|-||cost/kg x gramaj / 1000 + ambalaj|
Pret tinta client|rd_prettinta|Currency (4)|-||Din solicitare sau negociere|Securitate pe coloana
Marja bruta (%)|rd_marja|Decimal (2)|-|-100 - 100|(pret - cost) / pret x 100|Securitate pe coloana
Status|rd_statusantecalcul|Choice|O|Ciorna / Trimis spre aprobare / Aprobat / Respins / Inlocuit||
Aprobator|rd_aprobator|Lookup (systemuser)|-||Doua trepte daca marja sub prag|FLX-18
Data aprobarii|rd_dataaprobare|Date Only|-|||
Cost real la revizuire|rd_costreal|Currency (4)|-||Din Sectiunea 8|Compara antecalcul cu realitate
""")

t("TBL-23", "Linie de antecalcul", "rd_linieantecalcul", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (200)|O||Generata|Coloana primara
Antecalcul|rd_antecalcul|Lookup (rd_antecalcul)|O||Parental|
Materie prima|rd_materieprima|Lookup (rd_materieprima)|-|||
Materie prima de proiect|rd_mpproiect|Lookup (rd_mpproiect)|-||Pentru MP fara cod|REL-34
Cantitate (kg/100kg)|rd_cantitate|Decimal (4)|O|0 - 100||
Pret unitar|rd_pret|Currency (4)|O|||Securitate pe coloana
Cost linie|rd_costlinie|Calculated (Currency)|-||cantitate x pret / 100|
Sursa pretului|rd_sursapret|Choice|O|Catalog / Oferta furnizor / Estimare||
Data pretului|rd_datapret|Date Only|-|||
Observatii|rd_observatii|Text (500)|-|||
""")

t("TBL-24", "Reteta (antet)", "rd_reteta", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (200)|O|||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Cod reteta|rd_codreteta|Text (20)|-|||
Categorie produs|rd_categorieprodus|Choice|O|Foietaj / Aluat dospit / Patiserie cu umplutura / Paine / Produs gata copt / Produs bake-off|Determina grila senzoriala|
Versiune curenta|rd_versiunecurenta|Lookup (rd_versiunereteta)|-||Referential, scris de flux|REL-41
Status|rd_statusreteta|Choice|O|In dezvoltare / Validata / Inlocuita / Retrasa||
Observatii|rd_observatii|Text Area (2000)|-|||
""")

t("TBL-25", "Versiune de reteta", "rd_versiunereteta", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (150)|O|{Reteta} v{n}|Generata|Coloana primara
Reteta|rd_reteta|Lookup (rd_reteta)|O||Parental|
Numar versiune|rd_numarversiune|Whole Number|O|1 - 99|Succesiv|
Data versiunii|rd_dataversiune|Date Only|O|||
Autor|rd_autor|Lookup (systemuser)|O|||
Motivul modificarii|rd_motivmodificare|Text Area (1000)|O||Obligatoriu de la versiunea 2|Cerinta IFS
Total cantitate (kg/100kg)|rd_total|Rollup (Sum)|-||Suma liniilor, trebuie sa fie 100|Validare
Blocata|rd_blocata|Yes/No|O|Implicit Nu|Versiunea validata nu se mai editeaza|Vezi 2.14.4
Status|rd_statusversiune|Choice|O|Ciorna / In testare / Validata / Inlocuita||
Factor randament|rd_factorrandament|Decimal (4)|-|0 - 2|masa produs finit / masa aluat|Vezi 9.2.1.2
Sursa factor randament|rd_sursafactor|Choice|-|Productie 0 / Trial validat / Estimare pe categorie|Estimarea nu poate sustine o eticheta aprobata|
Energie (kcal/100g)|rd_energie|Decimal (2)|-||Calculat, Sectiunea 9|Scris de FLX-13
Grasimi|rd_grasimi|Decimal (2)|-||Calculat|
Saturate|rd_saturate|Decimal (2)|-||Calculat|
Glucide|rd_glucide|Decimal (2)|-||Calculat|
Zaharuri|rd_zaharuri|Decimal (2)|-||Calculat|
Fibre|rd_fibre|Decimal (2)|-||Calculat|
Proteine|rd_proteine|Decimal (2)|-||Calculat|
Sare|rd_sare|Decimal (4)|-||Calculat|
Alergeni continuti|rd_alergeni|Choice (multi)|-|Choice ALERGEN|Reuniunea alergenilor din linii|Scris de FLX-13
Alergeni pe urme|rd_alergeniurme|Choice (multi)|-|Choice ALERGEN|Vezi 9.4|
Data ultimului calcul|rd_datacalcul|Date and Time|-|||Semnaleaza calcule invechite
""")

t("TBL-26", "Linie de reteta", "rd_liniereteta", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (200)|O||Generata|Coloana primara
Versiune reteta|rd_versiunereteta|Lookup (rd_versiunereteta)|O||Parental|
Materie prima|rd_materieprima|Lookup (rd_materieprima)|-||Datele nutritionale complete sunt obligatorii|Vezi 15.2.2
Materie prima de proiect|rd_mpproiect|Lookup (rd_mpproiect)|-||Pentru MP inca fara cod|REL-35
Faza de retetare|rd_fazaretetare|Choice|O|Aluat de baza / Grasime de laminare / Umplutura / Decor / Glazura / Presarare||
Cantitate (kg/100kg)|rd_cantitate|Decimal (4)|O|0 - 100||
Ordine|rd_ordine|Whole Number|O|1 - 99||Ordinea de adaugare
Procent din total|rd_procent|Calculated (Decimal)|-|0 - 100||Pentru lista de ingrediente
Pierdere la proces (%)|rd_pierdere|Decimal (2)|-|0 - 100||
Observatii|rd_observatii|Text (500)|-|||
""")

t("TBL-27", "Alergen", "rd_alergen", "rd_name", "Nomenclator", 3, """
Denumire|rd_name|Text (100)|O|Cei 14 din Anexa II Reg. 1169/2011||Coloana primara
Cod|rd_cod|Text (5)|O|GLU, CRU, OUA, PES, ARA, SOI, LAP, FRC, TEL, MUS, SUS, SO2, LUP, MOL|Unic|
Denumire legala pe eticheta|rd_denumirelegala|Text (150)|O|||
Grupa|rd_grupa|Choice|O|Cereale cu gluten / Fructe cu coaja / Altele||
Necesita evidentiere pe eticheta|rd_evidentiere|Yes/No|O|Implicit Da||
Prag de declarare|rd_prag|Text (100)|-||Fara prag pentru alergenii continuti|Vezi 9.2.2.1
Observatii|rd_observatii|Text Area (1000)|-|||
""", nota="Valorile nutritionale sunt modelate ca set de coloane pe rd_versiunereteta, nu ca tabela separata (2.15).")

t("TBL-29", "Specificatie tehnica", "rd_specificatie", "rd_name", "Copil", 2, """
Numar specificatie|rd_name|Autonumber|O|ST-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|-||Gol pentru ST de MP din catalog|Referential
Tip specificatie|rd_tipspecificatie|Choice|O|Choice TIPST||
Materie prima|rd_materieprima|Lookup (rd_materieprima)|-||Obligatorie daca tip = ST interna MP|
Versiune|rd_versiune|Text (10)|O|v01, v02||
Status|rd_statusst|Choice|O|Ciorna / In aprobare / Aprobata / Inlocuita / Retrasa||
Autor|rd_autor|Lookup (systemuser)|O|||
Aprobator Calitate|rd_aprobatorcalitate|Lookup (systemuser)|-||Obligatoriu pentru Aprobata|
Data aprobarii|rd_dataaprobare|Date Only|-|||
Valabila de la|rd_valabiladela|Date Only|-|||
Document|rd_documenturl|Text (500)|-||Fisier in 05_Specificatii|Formatul intern al ST nu face obiectul blueprintului
Inlocuieste|rd_inlocuieste|Lookup (rd_specificatie)|-||Auto-referential|Lant de versiuni, REL-40
""")

t("TBL-30", "SDP (Specificatie de produs)", "rd_sdp", "rd_name", "Copil", 2, """
Numar SDP|rd_name|Autonumber|O|SDP-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Versiune reteta|rd_versiunereteta|Lookup (rd_versiunereteta)|O|||REL-36
Versiune|rd_versiune|Text (10)|O|v01, v02||
Status|rd_statussdp|Choice|O|Ciorna / In aprobare / Aprobata / Inlocuita||
Linie|rd_linie|Lookup (rd_linie)|O|||
Parametri de proces|rd_parametri|Text Area (8000)|-||Preluati din trialul validat si din productia 0|Vezi 7.10.3
Puncte critice HACCP|rd_haccp|Text Area (4000)|-||Completat de Calitate|
Controale in proces|rd_controale|Text Area (4000)|-|||
Ambalare si etichetare|rd_ambalare|Text Area (4000)|-|||
Paletizare|rd_paletizare|Text Area (2000)|-|||
Conditii de depozitare|rd_depozitare|Text (300)|-|||
Termen de valabilitate (luni)|rd_valabilitate|Whole Number|-|1 - 36||
Utilizare la client|rd_utilizare|Text Area (2000)|-||Decongelare, dospire, coacere|
Aprobator R&D|rd_aprobatorrd|Lookup (systemuser)|-|||
Aprobator Calitate|rd_aprobatorcalitate|Lookup (systemuser)|-|||
Data aprobarii|rd_dataaprobare|Date Only|-|||
Document|rd_documenturl|Text (500)|-|||
""")

t("TBL-31", "Eticheta", "rd_eticheta", "rd_name", "Copil", 3, """
Denumire|rd_name|Text (200)|O|||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Tip eticheta|rd_tipeticheta|Choice|O|Choice TIPETICHETA||
Format fisier imprimanta|rd_formatimprimanta|Choice|-|Colos / Zebra ZPL / Altul|Obligatoriu daca tip = Fisier imprimanta|
Versiune|rd_versiune|Text (10)|O|v01||
Status|rd_statuseticheta|Choice|O|De realizat / In lucru / Trimisa spre aprobare / Aprobata / Implementata / Inlocuita|Acopera LIV-28 si LIV-30|
Limba|rd_limba|Choice (multi)|O|RO / EN / HU / BG / DE / FR / IT||
Denumire legala produs|rd_denumirelegala|Text (300)|O||Preluata din SDP|
Lista de ingrediente|rd_ingrediente|Text Area (8000)|-||Generata din reteta, ordine descrescatoare|Vezi 9.3
Declaratie alergeni|rd_declaratiealergeni|Text Area (2000)|-||Generata, alergenii evidentiati|Vezi 9.3
Declaratie urme|rd_declaratieurme|Text (500)|-||Numai dupa evaluare de risc|Vezi 9.4.3
Tabel nutritional|rd_tabelnutritional|Text Area (2000)|-||Generat din versiunea de reteta|
Gramaj declarat|rd_gramajdeclarat|Text (50)|O|||
Termen de valabilitate|rd_valabilitate|Text (100)|O|||
Conditii de pastrare|rd_pastrare|Text (300)|O|||
Cod EAN|rd_ean|Text (20)|-|13 cifre|Validare de lungime|
Aprobator Calitate|rd_aprobator|Lookup (systemuser)|-||Obligatoriu pentru Aprobata|Raspunderea juridica ramane umana
Data aprobarii|rd_dataaprobare|Date Only|-|||
Fisier|rd_fisierurl|Text (500)|-||In 06_Eticheta|
""")

t("TBL-32", "Implementare (IPN)", "rd_implementare", "rd_name", "Copil", 2, """
Numar IPN|rd_name|Autonumber|O|IPN-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental, 1:1 in practica|
Linie|rd_linie|Lookup (rd_linie)|O|||
Data planificata productie 0|rd_dataprod0|Date Only|O|||
Conditii IPN completate|rd_conditiiok|Yes/No|O|Implicit Nu|Checklist de 13 conditii|Vezi 5.5.8
Plan IPN aprobat|rd_planok|Yes/No|O|Implicit Nu||
IL productie emisa|rd_ilok|Yes/No|O|Implicit Nu||
Numar IL|rd_numaril|Text (30)|-|||
Plan HACCP actualizat|rd_haccpok|Yes/No|O|Implicit Nu|Aprobare Calitate obligatorie|Cerinta IFS
Data actualizarii HACCP|rd_datahaccp|Date Only|-|||
Puncte critice noi identificate|rd_ccpnoi|Text Area (4000)|-|||
Necesita validare shelf life|rd_shelflife|Yes/No|O|Implicit Da pentru produs nou||
Termen de valabilitate propus (luni)|rd_valabilitate|Whole Number|-|1 - 36||
Instruire operatori efectuata|rd_instruireok|Yes/No|O|Implicit Nu|Data si lista de participanti in document|Cerinta IFS
Ambalaj disponibil|rd_ambalajok|Yes/No|O|Implicit Nu|Blocheaza productia 0|
Status implementare|rd_statusipn|Choice|O|In pregatire / Gata de productie 0 / In derulare / Finalizata / Amanata|Gata doar cu toate bifele Da|Business rule
Data implementarii|rd_dataimplementare|Date Only|-||Porneste ceasul revizuirii|Vezi Sectiunea 8
""")

t("TBL-33", "Productie 0", "rd_productie0", "rd_name", "Copil", 2, """
Numar|rd_name|Autonumber|O|P0-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Implementare|rd_implementare|Lookup (rd_implementare)|O||REL-39|
Data|rd_data|Date Only|O|||
Linie|rd_linie|Lookup (rd_linie)|O|||
Schimb|rd_schimb|Choice|O|Choice SCHIMB||
Cantitate planificata (kg)|rd_cantitateplanificata|Decimal (2)|O||Din planul IPN|
Cantitate de aluat introdusa (kg)|rd_aluatintrodus|Decimal (2)|-|> 0|Cantarire la malaxor, pe sarje|
Numar sarje|rd_numarsarje|Whole Number|-|1 - 99||
Bucati bune obtinute|rd_bucatibune|Whole Number|-|>= 0|Numarate la ambalare|
Cantitate realizata (kg)|rd_cantitaterealizata|Decimal (2)|-||bucati bune x gramaj / 1000|
Randament aluat (%)|rd_randamentaluat|Decimal (2)|-|0 - 120|realizata / aluat introdus x 100|Vezi 7.2.9
Randament fata de trial (%)|rd_randamentvstrial|Decimal (2)|-|||
Realizat fata de planificat (%)|rd_realizatvsplan|Decimal (2)|-|||
Rebut (kg)|rd_rebutkg|Decimal (2)|-|>= 0||
Rebut (%)|rd_rebutprocent|Decimal (2)|-|0 - 100|Din cantitatea introdusa|Prag 5% laminate, 3% depuse
Cauza dominanta de rebut|rd_cauzadominanta|Text (150)|-||Cauza cu ponderea cea mai mare|Scris de flux
Viteza nominala (buc/h)|rd_vitezanominala|Decimal (2)|-||Din nomenclatorul de linie|
Viteza reala (buc/h)|rd_vitezareala|Decimal (2)|-||Bucati / timp efectiv|
Eficienta viteza (%)|rd_eficientaviteza|Decimal (2)|-|0 - 150|reala / nominala x 100|Vezi 7.4.8
Timp setup (min)|rd_timpsetup|Whole Number|-|0 - 999|De la eliberarea liniei la prima bucata buna|
Timp schimb sortiment (min)|rd_timpschimb|Whole Number|-|0 - 999|Comparat cu cele 120 de minute implicite|
Timp total de ocupare (min)|rd_timpocupare|Whole Number|-|0 - 9999||
Greutate medie la ambalare (g)|rd_greutatemedie|Decimal (2)|-||Minimum 20 de bucati, 4 prelevari|
Abatere de la gramaj (%)|rd_abateregramaj|Decimal (2)|-|-50 - 50||
Supraumplere medie (%)|rd_supraumplere|Decimal (2)|-|-50 - 50|Cost ascuns|Vezi 7.6.7
Conformitate HACCP|rd_conformitatehaccp|Yes/No|-||O neconformitate blocheaza Validat|Vezi 7.7.3
Numar abateri de proces|rd_numarabateri|Rollup (Count)|-|||
Decizie finala|rd_decizie|Choice|-|Validat / Validat conditionat / Se repeta|Vezi 7.9|
Conditii de validare|rd_conditiivalidare|Text Area (4000)|-||Obligatorii daca decizie = Validat conditionat|
Responsabil decizie|rd_responsabildecizie|Lookup (systemuser)|-|||
Data deciziei|rd_datadecizie|Date Only|-|||
""")

t("TBL-34", "Inregistrare de productie 0", "rd_inregistrareprod0", "rd_name", "Copil", 2, """
Denumire|rd_name|Text (150)|O|||Coloana primara
Productie 0|rd_productie0|Lookup (rd_productie0)|O||Parental|
Tip inregistrare|rd_tipinregistrare|Choice|O|Parametru de proces / Rebut pe cauza / Problema / Masuratoare de ambalare / Verificare HACCP||
Faza|rd_faza|Choice|-|Framantare / Fermentare / Laminare / Formare / Dospire / Coacere / Congelare / Ambalare||
Valoare specificata|rd_valoarespecificata|Decimal (3)|-||Din SDP|
Valoare reala|rd_valoarereala|Decimal (3)|-|||
Unitate|rd_um|Choice|-|Choice UM sau C / min / mm / %||
Abatere|rd_abatere|Calculated (Decimal)|-||reala - specificata|
In toleranta|rd_intoleranta|Yes/No|-|||Marcata automat
Cauza rebut|rd_cauzarebut|Choice|-|RB-01 ... RB-14|Obligatorie daca tip = Rebut pe cauza|Vezi 7.3.1
Cantitate (kg)|rd_cantitate|Decimal (2)|-|>= 0||
Procent|rd_procent|Decimal (2)|-|0 - 100||
Valoare limita HACCP|rd_limitahaccp|Text (100)|-||Pentru tip = Verificare HACCP|
Conform|rd_conform|Yes/No|-|||
Descriere problema|rd_descriere|Text Area (2000)|-||Obligatorie daca tip = Problema|
Actiune corectiva|rd_actiune|Text Area (2000)|-||Obligatorie la neconformitate|
Responsabil|rd_responsabil|Lookup (systemuser)|-|||
Termen|rd_termen|Date Only|-|||
Status actiune|rd_statusactiune|Choice|-|Deschisa / In lucru / Inchisa|Actiunile deschise blocheaza Validat|
Poza|rd_poza|Image|-||Din canvas mobil|
""")

t("TBL-35", "Revizuire post-implementare", "rd_revizuire", "rd_name", "Copil", 3, """
Numar|rd_name|Autonumber|O|RPI-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|
Etapa revizuire|rd_etaparevizuire|Choice|O|30 de zile / 60 de zile / 90 de zile||
Data scadenta|rd_datascadenta|Date Only|O||dataimplementare + 30/60/90|
Data efectuarii|rd_dataefectuare|Date Only|-|||
Status|rd_statusrevizuire|Choice|O|Programata / In lucru / Finalizata / Sarita|Sarita dupa 30 de zile de la scadenta|Vezi 8.6.3
Cantitate produsa cumulat (kg)|rd_cantitateprodusa|Decimal (2)|-||Furnizata de Productie|
Numar loturi|rd_numarloturi|Whole Number|-|||
Numar reclamatii|rd_reclamatii|Whole Number|-|>= 0|Furnizate de Calitate|
Numar neconformitati interne|rd_neconformitati|Whole Number|-|>= 0||
Rata reclamatii (ppm)|rd_ratareclamatii|Decimal (2)|-||cantitate reclamata / produsa x 1000000|
Randament in serie (%)|rd_randamentserie|Decimal (2)|-|0 - 120||
Randament la productia 0 (%)|rd_randamentprod0|Decimal (2)|-||Automat din TBL-33|
Diferenta de randament (pp)|rd_diferentarandament|Calculated (Decimal)|-|||
Rebut in serie (%)|rd_rebutserie|Decimal (2)|-|0 - 100||
Rebut la productia 0 (%)|rd_rebutprod0|Decimal (2)|-||Automat|
Cost real / kg|rd_costreal|Currency (4)|-||Furnizat de Controlling|Securitate pe coloana
Cost din antecalcul / kg|rd_costantecalcul|Currency (4)|-||Automat din TBL-22|Securitate pe coloana
Abatere de cost (%)|rd_abaterecost|Calculated (Decimal)|-|||
Volum realizat fata de estimat (%)|rd_realizarevolum|Decimal (2)|-||Anualizat, cu exceptia produselor sezoniere|Vezi 8.3.1
Numar modificari dupa lansare|rd_modificari|Whole Number|-||Automat, din versiuni|
Feedback client|rd_feedbackclient|Text Area (4000)|-||Furnizat de KAM|
Feedback KAM|rd_feedbackkam|Text Area (4000)|-|||
Feedback productie|rd_feedbackproductie|Text Area (4000)|-|||
Indice de sanatate|rd_indicesanatate|Whole Number|-|0 - 100|Cost 30 + volum 25 + calitate 25 + producibilitate 20|PROPUNERE, vezi 8.4
Date indisponibile|rd_dateindisponibile|Text (500)|-||Departamentele care nu au furnizat datele|Vezi 8.7.1
Decizie|rd_decizie|Choice|-|Mentinere / Optimizare / Retragere|Optimizare creeaza automat proiect nou|Vezi 8.5.1
Actiuni|rd_actiuni|Text Area (4000)|-|||
Responsabil|rd_responsabil|Lookup (systemuser)|-|||
Aprobator|rd_aprobator|Lookup (systemuser)|-||Head of R&D la 90 de zile|
""")

t("TBL-36", "Linie de productie", "rd_linie", "rd_name", "Nomenclator", 0, """
Denumire linie|rd_name|Text (100)|O|||Coloana primara
Cod linie|rd_codlinie|Text (10)|O|L01 - L09|Unic|
Amplasament|rd_amplasament|Choice|O|Choice AMPLASAMENT||
Tip linie|rd_tiplinie|Choice|O|Laminare / Aluat dospit / Paine / Patiserie cu umplutura / Mixta||
Echipament principal|rd_echipament|Text (200)|-|Fritsch / Rademaker / VMI / WP Bakery / JBT||
Capabilitati|rd_capabilitati|Choice (multi)|O|Laminare / Impletire / Injectare umplutura / Depunere / Presarare / Glazurare / Coacere tunel / Congelare rapida / Ambalare flow-pack / Ambalare tava|Filtreaza liniile compatibile|Vezi 2.21.1
Alergeni prelucrati pe linie|rd_alergeniilinie|Choice (multi)|-|Choice ALERGEN|Pentru matricea de secventiere|Vezi 9.4.4
Gramaj minim (g)|rd_gramajmin|Decimal (2)|-||Validare la alocarea liniei|
Gramaj maxim (g)|rd_gramajmax|Decimal (2)|-|||
Latime banda (mm)|rd_latimebanda|Whole Number|-||Constrangere de dimensiune|
Viteza nominala (buc/h)|rd_vitezanominala|Decimal (2)|-||Referinta pentru productia 0|
Timp schimb sortiment (min)|rd_timpschimb|Whole Number|O|Implicit 120|Din aplicatia de planificare|
Tarif orar|rd_tariforar|Currency (2)|-||Pentru antecalcul|Securitate pe coloana
Pierdere tehnologica implicita (%)|rd_pierdereimplicita|Decimal (2)|-|0 - 30, implicit 3||
Numar proiecte active|rd_proiecteactive|Whole Number|-|0 - 99|Scris de FLX-06|Coada pe linie
Prag de supraincarcare|rd_pragsupraincarcare|Whole Number|O|Implicit 6|Peste prag, semnalizare vizuala|Vezi 2.21.2
Activa|rd_activa|Yes/No|O|||
""")

t("TBL-37", "Profil de tehnolog", "rd_profiltehnolog", "rd_name", "Nomenclator", 0, """
Denumire|rd_name|Text (150)|O|Numele persoanei||Coloana primara
Utilizator|rd_utilizator|Lookup (systemuser)|O||Unic|Sursa de adevar ramane Entra ID
Rol principal|rd_rolprincipal|Choice|O|Choice ROL||
Amplasament|rd_amplasament|Choice|O|Choice AMPLASAMENT||
Specializare|rd_specializare|Choice (multi)|-|Foietaj / Aluat dospit / Paine / Patiserie / Umpluturi / Ambalaje / Solutii tehnice|Filtreaza propunerea de alocare|
Linii pe care lucreaza|rd_linii|Text (100)|-|Coduri separate prin virgula||NOTA: N:N ar fi mai curat, dar se citeste mai greu
Capacitate maxima proiecte|rd_capacitatemax|Whole Number|O|1 - 10, implicit 6|Vezi A1.2.2|Securitate pe coloana
Proiecte active|rd_proiecteactive|Whole Number|-|0 - 99|Scris de FLX-06|
Proiecte active P1|rd_activep1|Whole Number|-|0 - 99|Scris de FLX-06|
Grad de incarcare (%)|rd_incarcare|Decimal (2)|-|0 - 300|active / capacitate max x 100|Securitate pe coloana
Semnal incarcare|rd_semnal|Choice|-|Verde / Galben / Rosu|Vezi 2.22.1|Afisat in dashboard
Disponibil|rd_disponibil|Yes/No|O|Implicit Da|Concediu, delegatie|
Indisponibil pana la|rd_indisponibilpanala|Date Only|-|||Intra in calculul termenului propus
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-38", "Client", "rd_client", "rd_name", "Nomenclator", 0, """
Denumire client|rd_name|Text (200)|O|||Coloana primara
Cod SAP client|rd_codsap|Text (20)|-|||Import
Clasificare|rd_clasificare|Choice|O|A / B / C|Stabilita si revizuita de Sales / KAM|20 de puncte in scor
Data ultimei clasificari|rd_dataclasificare|Date Only|-||Revizuire anuala|Peste 18 luni se semnaleaza
Canal|rd_canal|Choice|O|Choice CANAL||
Tara|rd_tara|Text (100)|O|Implicit Romania||Determina cerintele de eticheta (conditia C6)
KAM responsabil|rd_kam|Lookup (systemuser)|O|||
Cerinte specifice de eticheta|rd_cerinteeticheta|Text Area (4000)|-|||Se preiau automat in proiect
Cerinte de audit sau certificare|rd_cerinteaudit|Text Area (2000)|-|||
Numar proiecte active|rd_proiecteactive|Whole Number|-||Scris de FLX-06|Conditia C3
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-39", "Indicator", "rd_indicator", "rd_name", "Configurare", 3, """
Denumire|rd_name|Text (100)|O|||Coloana primara
Cod|rd_cod|Text (20)|O|T-TOTAL / Q-CORECT / Q-COMPLET|Unic|
Tip|rd_tip|Choice|O|Timp / Calitate / Volum||
Nivel de masurare|rd_nivel|Choice (multi)|O|Activitate / Rol / Persoana / Departament||
Formula de calcul|rd_formula|Text Area (2000)|O||Descriptiva|Vezi 13.2 - 13.4
Tinta (%)|rd_tinta|Decimal (2)|O|95 - 98||Parametrizabila
Prag de alerta (%)|rd_pragalerta|Decimal (2)|-|0 - 100||
Unitate|rd_um|Choice|O|Procent / Zile / Numar||
Frecventa|rd_frecventa|Choice|O|Saptamanal / Lunar / Trimestrial / Anual||
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-40", "Masurare de indicator", "rd_masurareindicator", "rd_name", "Derivata", 3, """
Denumire|rd_name|Text (150)|O||Generata|Coloana primara
Indicator|rd_indicator|Lookup (rd_indicator)|O||Parental|
Perioada|rd_perioada|Choice|O|Luna / Trimestru / An||
Data de inceput|rd_datainceput|Date Only|O|||
Data de sfarsit|rd_datasfarsit|Date Only|O|||
Nivel|rd_nivel|Choice|O|Activitate / Rol / Persoana / Departament||
Persoana|rd_persoana|Lookup (systemuser)|-|||Nu se afiseaza public
Rol|rd_rol|Choice|-|Choice ROL||
Linie|rd_linie|Lookup (rd_linie)|-|||
Valoare realizata|rd_valoare|Decimal (2)|O|||
Tinta|rd_tinta|Decimal (2)|O||Copiata la momentul calculului|
Atins|rd_atins|Calculated (Yes/No)|-||valoare >= tinta|
Numar cazuri|rd_numarcazuri|Whole Number|-|||Numitorul
Numar conforme|rd_numarconforme|Whole Number|-|||Numaratorul
Observatii|rd_observatii|Text Area (2000)|-|||
""", nota="Masuratorile se congeleaza: odata scrise, nu se recalculeaza retroactiv (13.5.1).")

t("TBL-41", "Motiv", "rd_motiv", "rd_name", "Nomenclator", 0, """
Denumire|rd_name|Text (200)|O|||Coloana primara
Cod|rd_cod|Text (10)|O||Unic|
Tip motiv|rd_tipmotiv|Choice|O|Respingere solicitare / Amanare / Respingere materie prima / Suspendare proiect / Abandon proiect / Suprascriere prioritate / Blocaj / Respingere livrabil||
Descriere|rd_descriere|Text Area (1000)|-|||
Necesita comentariu|rd_necesitacomentariu|Yes/No|O|||
Activ|rd_activ|Yes/No|O|||
""", nota="O singura tabela de motive in loc de sase: se raporteaza impreuna la analiza anuala (2.25.1).")

t("TBL-42", "Tip document", "rd_tipdocument", "rd_name", "Nomenclator", 0, """
Denumire|rd_name|Text (100)|O|||Coloana primara
Cod|rd_cod|Text (10)|O||Unic|Folosit in numele fisierului
Faza|rd_faza|Choice|O|Choice FAZA||Determina folderul tinta
Extensie asteptata|rd_extensie|Text (20)|-|pdf / docx / xlsx / jpg / zpl||
Necesita aprobare|rd_necesitaaprobare|Yes/No|O|||
Rol aprobator|rd_rolaprobator|Choice|-|Choice ROL||
Retentie (ani)|rd_retentie|Whole Number|-|1 - 99|Gol = Permanent|Vezi 5.2.3
Sablon Word|rd_sablonword|Text (300)|-||Pentru FLX-12|
Activ|rd_activ|Yes/No|O|||
""")


# ============================================================================
# SINTEZA ENTERPRISE - tabelele noi din Sectiunile 23, 24, 25 (vezi S22.7.2)
# ============================================================================

t("TBL-43", "Sablon de gate", "rd_sablongate", "rd_name", "Configurare", 1, """
Denumire|rd_name|Text (100)|O|||Coloana primara
Cod gate|rd_codgate|Text (10)|O|G0 ... G8|Unic|Alternate key
Ordine|rd_ordine|Whole Number|O|0 - 20||
Etapa asociata|rd_sablonetapa|Lookup (rd_sablonetapa)|O||Gate-ul se evalueaza la iesirea din etapa|
Tip proiect|rd_tipproiect|Choice (multi)|O|Choice TIPPROIECT|Nu toate gate-urile se aplica la toate tipurile|
Rol decident|rd_roldecident|Choice|O|Choice ROL||
Rol coaprobator|rd_rolcoaprobator|Choice|-|Choice ROL|Unele gate-uri cer doua semnaturi|G2, G4, G5, G6, G7
Blocheaza avansarea|rd_blocheaza|Yes/No|O|Implicit Da|Nu = gate informativ|
Permite GO cu conditii|rd_permiteconditii|Yes/No|O|Implicit Da|G5 si G6 = Nu|
Prag RPN blocant|rd_pragrpn|Whole Number|-|1 - 125, implicit 48|Riscul peste acest RPN blocheaza GO|Vezi 23.2.5
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-44", "Criteriu de gate", "rd_criteriugate", "rd_name", "Configurare", 1, """
Denumire criteriu|rd_name|Text (200)|O|||Coloana primara
Cod|rd_cod|Text (15)|O|G0-01, G0-02 ...|Unic|
Sablon gate|rd_sablongate|Lookup (rd_sablongate)|O||Parental|Cascade All
Ordine|rd_ordine|Whole Number|O|1 - 30||
Tip verificare|rd_tipverificare|Choice|O|Automata / Manuala / Mixta||Vezi 23.1.10
Sursa verificarii automate|rd_sursaauto|Text (200)|-||Obligatorie daca tip = Automata|Livrabil, camp sau agregare
Livrabil legat|rd_codlivrabil|Text (10)|-|LIV-nn|Criteriul verifica un livrabil anume|
Obligatoriu pentru GO|rd_obligatoriu|Yes/No|O|Implicit Da|Nu = criteriu de atentionare|
Sever|rd_sever|Yes/No|O|Implicit Nu|Da = nu admite GO cu conditii|
Rol responsabil|rd_rolresponsabil|Choice|O|Choice ROL||
Activ|rd_activ|Yes/No|O|||
""")

t("TBL-45", "Gate de proiect", "rd_gate", "rd_name", "Copil", 1, """
Denumire|rd_name|Text (150)|O|{cod proiect}_{cod gate}|Generata|Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Sablon gate|rd_sablongate|Lookup (rd_sablongate)|O|||
Etapa|rd_etapa|Lookup (rd_etapa)|-||Referential|
Data planificata|rd_dataplanificata|Date Only|O||Din data de final a etapei|
Data evaluarii|rd_dataevaluare|Date and Time|-||Automata la salvarea deciziei|
Status gate|rd_statusgate|Choice|O|Neevaluat / In pregatire / Gata de evaluare / Evaluat / Sarit|Gata cand toate criteriile automate sunt indeplinite|Scris de FLX-23
Decizie|rd_decizie|Choice|-|GO / GO cu conditii / HOLD / REWORK / STOP|Vezi 23.1.4|Choice global DECIZIEGATE
Decident|rd_decident|Lookup (systemuser)|-||Trebuie sa aiba rolul din sablon|Business rule
Coaprobator|rd_coaprobator|Lookup (systemuser)|-||Obligatoriu daca sablonul cere|
Criterii indeplinite|rd_criteriiok|Whole Number|-|0 - 30|Rollup pe verificari|
Criterii totale aplicabile|rd_criteriitotal|Whole Number|-|0 - 30||
Procent pregatire|rd_procentpregatire|Decimal (2)|-|0 - 100|indeplinite / total x 100|Afisat ca bara
Motivul deciziei|rd_motivdecizie|Text Area (2000)|-||Obligatoriu pentru tot ce nu e GO|Business rule
Numar actiuni deschise|rd_actiunideschise|Rollup (Count)|-||Din rd_actiune legate de gate|GO cu conditii cere minimum 1
Derogare acordata|rd_derogare|Yes/No|O|Implicit Nu|Permite GO peste un risc blocant|Vezi 23.1.5
Motivul derogarii|rd_motivderogare|Text Area (2000)|-||Obligatoriu daca derogare = Da|Auditat
Aprobator derogare|rd_aprobatorderogare|Lookup (systemuser)|-||Obligatoriu daca derogare = Da|Head of R&D
Numar reveniri|rd_numarreveniri|Whole Number|-|0 - 20|Incrementat la fiecare REWORK|Indicator de calitate
Zile in gate|rd_zileingate|Whole Number|-|0 - 999|Data evaluarii - data planificata|Masoara birocratia
Data ultimei alerte|rd_dataultimaalerta|Date and Time|-||Deduplicare alerte|Vezi 23.7.2.1
Amanat pana la|rd_amanatpanala|Date Only|-||Snooze cu motiv|
Motiv amanare|rd_motivamanare|Text (300)|-||Obligatoriu daca exista amanare|
""")

t("TBL-46", "Verificare de gate", "rd_verificaregate", "rd_name", "Copil", 1, """
Denumire|rd_name|Text (200)|O||Din criteriu|Coloana primara
Gate|rd_gate|Lookup (rd_gate)|O||Parental|Cascade All
Criteriu|rd_criteriu|Lookup (rd_criteriugate)|O|||
Rezultat|rd_rezultat|Choice|O|Neverificat / Indeplinit / Neindeplinit / Nu se aplica|Implicit Neverificat|
Verificat automat|rd_automat|Yes/No|O||Din tipul criteriului|
Data verificarii|rd_dataverificare|Date and Time|-|||
Verificat de|rd_verificatde|Lookup (systemuser)|-||Gol pentru verificarile automate|
Observatii|rd_observatii|Text Area (1000)|-||Obligatorii daca rezultat = Neindeplinit|
Actiune generata|rd_actiune|Lookup (rd_actiune)|-||Referential|Vezi 23.4
""")

t("TBL-47", "Risc de proiect", "rd_risc", "rd_name", "Copil", 2, """
Numar risc|rd_name|Autonumber|O|RSK-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Etapa detectarii|rd_etapa|Lookup (rd_etapa)|-||Referential|Cand a fost vazut
Titlu|rd_titlu|Text (200)|O|||
Descriere|rd_descriere|Text Area (2000)|O|||
Categorie|rd_categorie|Choice|O|Choice CATEGORIERISC||16 valori, vezi 23.2.3
Probabilitate|rd_probabilitate|Whole Number|O|1 - 5|Vezi 23.2.4|
Impact|rd_impact|Whole Number|O|1 - 5|Vezi 23.2.4|
Detectabilitate|rd_detectabilitate|Whole Number|O|1 - 5|1 = se vede imediat, 5 = se afla tarziu|
RPN|rd_rpn|Calculated (Whole Number)|-|1 - 125|probabilitate x impact x detectabilitate|Vezi 23.2.5
Nivel de risc|rd_nivel|Choice|-|Scazut / Mediu / Ridicat / Critic|Derivat din RPN|Scris de flux
Impact estimat in zile|rd_impactzile|Whole Number|-|0 - 365||Pentru termenul forecast
Expunere financiara|rd_expunere|Currency (2)|-||Optionala, vezi 23.2.7|Securitate pe coloana
Afecteaza siguranta alimentelor|rd_afecteazafoodsafety|Yes/No|O|Implicit Nu|Da = nivel Critic automat|Blocheaza gate
Afecteaza clientul|rd_afecteazaclient|Yes/No|O|Implicit Nu||
Afecteaza conformitatea|rd_afecteazaconformitate|Yes/No|O|Implicit Nu|IFS, ISO, legal|
Semnal de declansare|rd_trigger|Text (500)|-||Ce ar arata ca riscul se produce|Face riscul urmaribil
Plan de mitigare|rd_mitigare|Text Area (2000)|-||Obligatoriu pentru Ridicat si Critic|Business rule
Plan de contingenta|rd_contingenta|Text Area (2000)|-||Ce facem daca se produce totusi|
Proprietar|rd_proprietar|Lookup (systemuser)|O||O persoana, nu un departament|
Termen de mitigare|rd_termen|Date Only|-||Obligatoriu pentru Ridicat si Critic|
Probabilitate reziduala|rd_probabilitatereziduala|Whole Number|-|1 - 5|Dupa mitigare|
Impact rezidual|rd_impactrezidual|Whole Number|-|1 - 5|Dupa mitigare|
RPN rezidual|rd_rpnrezidual|Whole Number|-|1 - 125||Ce ramane asumat
Status|rd_statusrisc|Choice|O|Identificat / In evaluare / In mitigare / Mitigat / Acceptat / Produs / Inchis|Produs = se creeaza problema|Vezi 23.2.6
Tendinta|rd_tendinta|Choice|-|In crestere / Stabil / In scadere|Comparat cu ultima revizuire|
Problema generata|rd_problema|Lookup (rd_problema)|-||Cand riscul se produce|Trasabilitate
Data ultimei revizuiri|rd_dataultimarevizuire|Date Only|-||Ridicat si Critic se revizuiesc lunar|FLX-24
Data ultimei alerte|rd_dataultimaalerta|Date and Time|-||Deduplicare alerte|
""")

t("TBL-48", "Problema de proiect", "rd_problema", "rd_name", "Copil", 2, """
Numar problema|rd_name|Autonumber|O|ISS-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Etapa|rd_etapa|Lookup (rd_etapa)|-||Referential|
Titlu|rd_titlu|Text (200)|O|||
Descriere|rd_descriere|Text Area (2000)|O|||
Sursa|rd_sursa|Choice|O|Trial / Materie prima / Furnizor / Productie 0 / Client / Calitate / Reclamatie / Audit / Risc materializat / Alta||
Categorie|rd_categorie|Choice|O|Choice CATEGORIERISC|Aceleasi categorii ca la risc|Permite analiza comuna
Severitate|rd_severitate|Choice|O|Minora / Majora / Critica / Blocanta|Critica si Blocanta blocheaza gate|
Impact asupra termenului (zile)|rd_impacttermen|Whole Number|-|0 - 365||
Impact asupra costului|rd_impactcost|Currency (2)|-||Optional|Securitate pe coloana
Impact asupra calitatii|rd_impactcalitate|Yes/No|O|Implicit Nu||
Impact asupra clientului|rd_impactclient|Yes/No|O|Implicit Nu||
Siguranta alimentelor|rd_foodsafety|Yes/No|O|Implicit Nu|Da = severitate Critica automat|Declanseaza neconformitate
Cauza radacina|rd_cauzaradacina|Lookup (rd_motiv)|-||Obligatorie la inchidere pentru Critica si Blocanta|Nomenclator, vezi 25.6.2
Detalii cauza|rd_detaliicauza|Text Area (2000)|-|||
Metoda de analiza|rd_metodaanaliza|Choice|-|5 De ce / Ishikawa / Experienta / Altele||
Actiune corectiva|rd_actiunecorectiva|Text Area (2000)|-||Ce rezolva problema acum|
Actiune preventiva|rd_actiunepreventiva|Text Area (2000)|-||Ce impiedica repetarea|
Proprietar|rd_proprietar|Lookup (systemuser)|O|||
Termen|rd_termen|Date Only|-||Obligatoriu pentru Critica si Blocanta|
Status|rd_statusproblema|Choice|O|Deschisa / In analiza / In rezolvare / Rezolvata / Verificata / Inchisa / Reaparuta||
Data deschiderii|rd_datadeschidere|Date Only|O|Implicit azi||
Data inchiderii|rd_datainchidere|Date Only|-|||
Zile deschisa|rd_ziledeschisa|Whole Number|-|0 - 999||Scris de flux
Risc sursa|rd_risc|Lookup (rd_risc)|-||Daca provine dintr-un risc materializat|
Trial legat|rd_trial|Lookup (rd_trial)|-||Referential|
Materie prima legata|rd_mpproiect|Lookup (rd_mpproiect)|-||Referential|
Productie 0 legata|rd_productie0|Lookup (rd_productie0)|-||Referential|
Lectie generata|rd_lectie|Lookup (rd_lectie)|-||Vezi 25.2|
Repetare|rd_esterepetare|Yes/No|O|Implicit Nu|Aceeasi cauza in ultimele 12 luni|Scris de FLX-26
""")

t("TBL-49", "Actiune", "rd_actiune", "rd_name", "Copil", 1, """
Numar actiune|rd_name|Autonumber|O|ACT-{AA}-{SEQ:00000}||Coloana primara
Titlu|rd_titlu|Text (200)|O|||
Descriere|rd_descriere|Text Area (2000)|-|||
Proiect|rd_proiect|Lookup (rd_proiect)|-||Referential; poate exista si actiune fara proiect|Remove Link
Sursa|rd_sursaactiune|Choice|O|Choice SURSAACTIUNE||12 valori, vezi 23.4.2
Risc|rd_risc|Lookup (rd_risc)|-||Completat de flux|
Problema|rd_problema|Lookup (rd_problema)|-||Completat de flux|
Gate|rd_gate|Lookup (rd_gate)|-||Pentru GO cu conditii|
Productie 0|rd_productie0|Lookup (rd_productie0)|-|||
Prioritate|rd_prioritate|Choice|O|Scazuta / Normala / Ridicata / Urgenta|Implicit Normala|
Proprietar|rd_proprietar|Lookup (systemuser)|O||O persoana|
Termen|rd_termen|Date Only|O|||
Status|rd_statusactiune|Choice|O|Deschisa / In lucru / In verificare / Inchisa / Anulata||
Data inchiderii|rd_datainchidere|Date Only|-|||
Zile intarziere|rd_zileintarziere|Whole Number|-|0 - 999|max(0, azi - termen) daca nu e inchisa|Scris de FLX-08
Dovada|rd_dovada|Text Area (1000)|-||Obligatorie la inchidere pentru Gate, CAPA, Neconformitate|Business rule
Verificator|rd_verificator|Lookup (systemuser)|-||Cine confirma ca s-a facut|
Data verificarii|rd_dataverificare|Date Only|-|||
Eficacitate|rd_eficacitate|Choice|-|Eficace / Partial eficace / Neeficace / Prea devreme pentru evaluare|Se evalueaza la 30 de zile de la inchidere|Cerinta IFS pentru CAPA
Blocheaza gate|rd_blocheazagate|Yes/No|O|Implicit Nu|Da = gate-ul nu trece pana la inchidere|
Escaladata|rd_escaladata|Yes/No|O|Implicit Nu|Scris de FLX-27|
Nivel escaladare|rd_nivelescaladare|Whole Number|-|0 - 4|Vezi 23.7.3|
Data ultimei alerte|rd_dataultimaalerta|Date and Time|-||Deduplicare alerte|
Amanat pana la|rd_amanatpanala|Date Only|-||Snooze cu motiv|
Motiv amanare|rd_motivamanare|Text (300)|-||Obligatoriu daca exista amanare|
""")

t("TBL-50", "Decizie de proiect", "rd_decizie", "rd_name", "Copil", 2, """
Numar decizie|rd_name|Autonumber|O|DEC-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Etapa|rd_etapa|Lookup (rd_etapa)|-||Referential|
Titlu|rd_titlu|Text (200)|O|||
Contextul deciziei|rd_context|Text Area (2000)|O||Ce problema se rezolva|
Alternative considerate|rd_alternative|Text Area (2000)|-||Ce s-a mai luat in calcul|Partea cea mai valoroasa la recitire
Decizia luata|rd_deciziatext|Text Area (2000)|O|||
Motivul|rd_motiv|Text Area (2000)|O|||
Categorie|rd_categorie|Choice|O|Tehnica / Reteta / Furnizor / Cost / Comerciala / Calitate / Planificare / Scop||
Decident|rd_decident|Lookup (systemuser)|O|||
Data deciziei|rd_datadecizie|Date Only|O|||
Consultati|rd_consultati|Text (300)|-||Cine a participat|
Reversibila|rd_reversibila|Yes/No|O|Implicit Da|Nu = consecinte greu de anulat|Merita mai multa atentie
Ipoteze asumate|rd_ipoteze|Text Area (2000)|-||Ce presupunem ca este adevarat|Vezi 23.5.3
Data de reevaluare|rd_datareevaluare|Date Only|-||Cand se verifica ipotezele|Genereaza actiune
Rezultat la reevaluare|rd_rezultat|Choice|-|Confirmata / Partial confirmata / Infirmata / Nereevaluata||Alimenteaza lectiile
Impact asupra costului|rd_impactcost|Currency (2)|-||Optional|Securitate pe coloana
""")

t("TBL-51", "Stabilizare", "rd_stabilizare", "rd_name", "Copil", 3, """
Numar|rd_name|Autonumber|O|STB-{AA}-{SEQ:0000}||Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Productie 0 sursa|rd_productie0|Lookup (rd_productie0)|O||Referential|
Linie|rd_linie|Lookup (rd_linie)|O|||
Data inceperii|rd_datainceput|Date Only|O||Prima productie de serie|
Numar loturi necesare|rd_loturinecesare|Whole Number|O|1 - 10, implicit 3|Configurabil pe categorie|Variabila de mediu
Loturi produse|rd_loturiproduse|Rollup (Count)|-|0 - 99|Din rd_lotstabilizare|
Loturi conforme consecutive|rd_loturiconforme|Whole Number|-|0 - 99|Se reseteaza la primul neconform|Scris de FLX-31
Schimburi acoperite|rd_schimburi|Whole Number|-|1 - 3|Distinct pe loturi conforme|Vezi 24.1.3
Randament mediu in serie (%)|rd_randamentmediu|Decimal (2)|-|0 - 120|Media loturilor conforme|
Randament la productia 0 (%)|rd_randamentprod0|Decimal (2)|-||Preluat automat|Baza de comparatie
Diferenta de randament (pp)|rd_diferentarandament|Calculated (Decimal)|-||serie - productie 0|Vezi 24.1.7
Rebut mediu in serie (%)|rd_rebutmediu|Decimal (2)|-|0 - 100||
Giveaway mediu (%)|rd_giveawaymediu|Decimal (2)|-|-50 - 50|Supraumplerea in serie|Vezi 7.6.7
Viteza medie realizata (%)|rd_vitezamedie|Decimal (2)|-|0 - 150|Fata de viteza nominala|
Reclamatii interne|rd_reclamatiiinterne|Whole Number|-|0 - 99||
Variabilitate acceptabila|rd_variabilitateok|Yes/No|-||CV al gramajului sub prag pe toate loturile|Vezi 6.2.3
Actiuni deschise|rd_actiunideschise|Rollup (Count)|-||Din rd_actiune|Blocheaza inchiderea
Status|rd_statusstabilizare|Choice|O|In curs / Reusita / Neconcludenta / Esuata||Choice global STATUSSTAB
Data finalizarii|rd_datafinalizare|Date Only|-||La al treilea lot conform consecutiv|Declanseaza G7
Decizie|rd_deciziestabilizare|Choice|-|Release / Release cu monitorizare / Se prelungeste / Se reia productia 0||
Motivul deciziei|rd_motivdecizie|Text Area (2000)|-||Obligatoriu pentru tot ce nu e Release|
Responsabil|rd_responsabil|Lookup (systemuser)|O|||
""")

t("TBL-52", "Lot de stabilizare", "rd_lotstabilizare", "rd_name", "Copil", 3, """
Denumire|rd_name|Text (150)|O|Numarul lotului de productie||Coloana primara
Stabilizare|rd_stabilizare|Lookup (rd_stabilizare)|O||Parental|Cascade All
Numar de ordine|rd_numarordine|Whole Number|O|1 - 99|Succesiv|
Data productiei|rd_dataproductie|Date Only|O|||
Schimb|rd_schimb|Choice|O|Choice SCHIMB||
Cantitate produsa (kg)|rd_cantitate|Decimal (2)|O|> 0||
Randament (%)|rd_randament|Decimal (2)|-|0 - 120||
Rebut (%)|rd_rebut|Decimal (2)|-|0 - 100||
Greutate medie (g)|rd_greutatemedie|Decimal (2)|-||Minimum 20 de bucati|
CV gramaj (%)|rd_cvgramaj|Decimal (2)|-|0 - 100||Vezi 6.2.3
Giveaway (%)|rd_giveaway|Decimal (2)|-|-50 - 50||
Viteza realizata (%)|rd_viteza|Decimal (2)|-|0 - 150||
Conformitate HACCP|rd_haccpok|Yes/No|O||O neconformitate = lot neconform|
Reclamatii sau neconformitati|rd_neconformitati|Whole Number|-|0 - 99||
Lot conform|rd_conform|Yes/No|O||Vezi 24.1.2|Scris de FLX-31
Motivul neconformitatii|rd_motivneconform|Text Area (1000)|-||Obligatoriu daca lot conform = Nu|
Problema generata|rd_problema|Lookup (rd_problema)|-||Un lot neconform creeaza automat o problema|FLX-31
""")

t("TBL-53", "Capabilitate de proces", "rd_capabilitateproces", "rd_name", "Derivata", 3, """
Denumire|rd_name|Text (200)|O|{produs}_{parametru}|Generata|Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Stabilizare|rd_stabilizare|Lookup (rd_stabilizare)|-||Referential|
Linie|rd_linie|Lookup (rd_linie)|O||Capabilitatea este a perechii produs-linie|
Parametru|rd_parametru|Choice|O|Choice TIPMASURATOARE|Tipuri numerice|
Perioada de la|rd_perioadadela|Date Only|O|||
Perioada pana la|rd_perioadapanala|Date Only|O|||
Numar de valori|rd_n|Whole Number|O|1 - 9999|Sub 30 = Date insuficiente|Vezi 24.2.5
Numar de loturi|rd_numarloturi|Whole Number|O|1 - 99|Minimum 3|
Media|rd_medie|Decimal (4)|O|||
Abaterea standard|rd_sigma|Decimal (5)|O|> 0|Esantion, n-1|
Tinta|rd_tinta|Decimal (4)|O||Din specificatie|
Limita inferioara|rd_lis|Decimal (4)|O||tinta - toleranta minus|
Limita superioara|rd_lss|Decimal (4)|O||tinta + toleranta plus|
Cp|rd_cp|Decimal (3)|-|0 - 10|Vezi 24.2.2|
Cpk|rd_cpk|Decimal (3)|-|-5 - 10|Poate fi negativ daca media e in afara limitelor|
Deplasare fata de tinta (%)|rd_deplasare|Decimal (2)|-|-100 - 100|(medie - tinta) / tinta x 100|Arata daca e reglaj sau imprastiere
Verdict|rd_verdict|Choice|O|Date insuficiente / Incapabil / Marginal / Capabil / Foarte capabil|Vezi 24.2.3|
Recomandare|rd_recomandare|Text Area (1000)|-||Generata din combinatia Cp / Cpk|Vezi 24.2.4
Data calculului|rd_datacalcul|Date and Time|O|||Scris de FLX-32
""")

t("TBL-54", "Lectie invatata", "rd_lectie", "rd_name", "Cunoastere", 3, """
Numar lectie|rd_name|Autonumber|O|LSN-{AA}-{SEQ:0000}||Coloana primara
Titlu|rd_titlu|Text (200)|O||Formulat ca afirmatie, nu ca subiect|Vezi 25.2.4
Situatia|rd_situatie|Text Area (2000)|O||Ce s-a intamplat concret|
Cauza radacina|rd_cauzaradacina|Text Area (2000)|O||De ce s-a intamplat|
Lectia|rd_lectietext|Text Area (2000)|O||Ce stim acum si nu stiam inainte|
Recomandarea|rd_recomandare|Text Area (2000)|O||Ce sa faca altcineva data viitoare|Partea reutilizabila
Actiune preventiva|rd_actiunepreventiva|Text Area (2000)|-||Ce schimbare de proces ar impiedica repetarea|
Categorie|rd_categorie|Choice|O|Choice CATEGORIELECTIE||12 valori
Severitatea situatiei|rd_severitate|Choice|O|Minora / Majora / Critica||
Nivel de reutilizare|rd_nivelreutilizare|Choice|O|Proiect / Categorie de produs / Linie / Furnizor / Client / Intreaga companie|Determina cui i se recomanda|Vezi 25.4
Categorie de produs|rd_categorieprodus|Choice|-|Foietaj / Aluat dospit / Patiserie cu umplutura / Paine / Toate|Pentru potrivire|
Linie|rd_linie|Lookup (rd_linie)|-||Referential|
Materie prima|rd_materieprima|Lookup (rd_materieprima)|-||Referential|
Furnizor|rd_furnizor|Lookup (rd_furnizor)|-||Referential|
Client|rd_client|Lookup (rd_client)|-||Referential|
Etichete|rd_etichete|Text (300)|-|Cuvinte separate prin ;|Pentru cautare libera|
Cost potential evitat|rd_costevitat|Currency (2)|-||Estimare, optionala|Securitate pe coloana
Zile potential evitate|rd_zileevitate|Whole Number|-|0 - 365|Estimare|
Proiect sursa|rd_proiect|Lookup (rd_proiect)|-||De unde provine|Referential
Problema sursa|rd_problema|Lookup (rd_problema)|-||Referential|
Productie 0 sursa|rd_productie0|Lookup (rd_productie0)|-||Referential|
Generata automat|rd_generataauto|Yes/No|O|Implicit Nu|Draft creat de FLX-33|Vezi 25.2.2
Status|rd_statuslectie|Choice|O|Draft / In verificare / Aprobata / Respinsa / Arhivata|Numai cele Aprobate se recomanda|
Autor|rd_autor|Lookup (systemuser)|O|||
Aprobator|rd_aprobator|Lookup (systemuser)|-||Manager R&D|
Data aprobarii|rd_dataaprobare|Date Only|-|||
Numar reutilizari|rd_numarreutilizari|Rollup (Count)|-|0 - 999|Din rd_utilizarelectie|Vezi 25.3
Data ultimei reutilizari|rd_dataultimareutilizare|Date Only|-|||Lectiile nefolosite se revizuiesc
""")

t("TBL-55", "Utilizare de lectie", "rd_utilizarelectie", "rd_name", "Cunoastere", 3, """
Denumire|rd_name|Text (200)|O|Generata||Coloana primara
Lectie|rd_lectie|Lookup (rd_lectie)|O||Parental|Cascade All
Proiect|rd_proiect|Lookup (rd_proiect)|O||Unde s-a folosit|Referential
Etapa|rd_etapa|Lookup (rd_etapa)|-||Referential|
Persoana|rd_persoana|Lookup (systemuser)|O||Cine a folosit-o|
Data|rd_data|Date Only|O|Implicit azi||
Cum a fost folosita|rd_mod|Text Area (1000)|-|||
Rezultat|rd_rezultat|Choice|O|A ajutat / Partial / Nu a ajutat / Prea devreme||
Cost evitat estimat|rd_costevitat|Currency (2)|-||Optional|Securitate pe coloana
Zile evitate estimate|rd_zileevitate|Whole Number|-|0 - 365|Optional|
Risc evitat|rd_riscevitat|Text (300)|-|||
""")

t("TBL-56", "Recomandare de lectie", "rd_recomandarelectie", "rd_name", "Cunoastere", 3, """
Denumire|rd_name|Text (200)|O|Generata||Coloana primara
Lectie|rd_lectie|Lookup (rd_lectie)|O||Referential|
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Momentul recomandarii|rd_moment|Choice|O|Acceptare / Alocare linie / Materie prima / Fisa de testare / IPN / Problema|Vezi 25.4.2|
Scor de potrivire|rd_scorpotrivire|Whole Number|O|0 - 100|Vezi 25.4.4|
Motivul potrivirii|rd_motivpotrivire|Text (300)|O||Aceeasi linie si categorie de produs|Face recomandarea credibila
Data recomandarii|rd_datarecomandare|Date and Time|O|||
Status|rd_statusrecomandare|Choice|O|Afisata / Acceptata / Aplicata / Respinsa / Ignorata||
Motivul respingerii|rd_motivrespingere|Text (300)|-||Optional, dar util pentru calibrare|
Utilizare generata|rd_utilizare|Lookup (rd_utilizarelectie)|-||La status Aplicata|
""")

t("TBL-57", "Istoric de lead time", "rd_leadtimeistoric", "rd_name", "Derivata", 2, """
Denumire|rd_name|Text (200)|O||Generata|Coloana primara
Furnizor|rd_furnizor|Lookup (rd_furnizor)|O||Referential|
Materie prima|rd_materieprima|Lookup (rd_materieprima)|-||Referential|
Materie prima de proiect|rd_mpproiect|Lookup (rd_mpproiect)|-||Referential|
Data comenzii|rd_datacomanda|Date Only|O|||
ETA initial|rd_etainitial|Date Only|-||Primul ETA confirmat|
ETA final|rd_etafinal|Date Only|-||Ultimul ETA confirmat|
Data livrarii reale|rd_datalivrare|Date Only|-|||
Lead time realizat (zile)|rd_leadtimerealizat|Whole Number|-|0 - 999|livrare - comanda|
Abatere fata de ETA initial|rd_abatereeta|Whole Number|-|-999 - 999|livrare - ETA initial|Masoara increderea in ETA
Numar modificari ETA|rd_modificarieta|Whole Number|-|0 - 99||
Livrat complet|rd_livratcomplet|Yes/No|-||Pentru OTIF|
Conform la receptie|rd_conform|Yes/No|-|||
Tip achizitie|rd_tipachizitie|Choice|-|Pe stoc / In portofoliu furnizor / Achizitie noua / Import|Pentru calcul pe categorie|
""")

t("TBL-58", "Snapshot de sanatate", "rd_snapshotsanatate", "rd_name", "Derivata", 3, """
Denumire|rd_name|Text (150)|O|{cod proiect}_{AAAALLZZ}|Generata|Coloana primara
Proiect|rd_proiect|Lookup (rd_proiect)|O||Parental|Cascade All
Data snapshot|rd_data|Date Only|O||Saptamanal, luni|Unic impreuna cu proiectul
Status la data|rd_status|Choice|O|Choice STATUSPROIECT|Copiat, nu referit|Ca sa ramana istoric corect
Etapa la data|rd_etapatext|Text (100)|-||Copiata ca text|Idem
Scor sanatate|rd_scorsanatate|Whole Number|O|0 - 100|Vezi 24.3.2|
Nivel|rd_nivel|Choice|O|Verde / Galben / Portocaliu / Rosu / Blocat||
Componenta riscuri|rd_compriscuri|Whole Number|-|0 - 20||
Componenta livrabile|rd_complivrabile|Whole Number|-|0 - 20||
Componenta termen|rd_comptermen|Whole Number|-|0 - 15||
Componenta aprovizionare|rd_compaprovizionare|Whole Number|-|0 - 15||
Componenta productie|rd_compproductie|Whole Number|-|0 - 10||
Componenta calitate|rd_compcalitate|Whole Number|-|0 - 10||
Componenta capacitate|rd_compcapacitate|Whole Number|-|0 - 10||
Variatie fata de saptamana trecuta|rd_variatie|Whole Number|-|-100 - 100||Semnalul cel mai util
Zile de la ultima activitate|rd_zileinactiv|Whole Number|-|0 - 999|Din rd_ultimaactivitate|Detecteaza proiecte uitate
Riscuri deschise|rd_riscurideschise|Whole Number|-|0 - 99||
Probleme deschise|rd_problemedeschise|Whole Number|-|0 - 99||
Actiuni restante|rd_actiunirestante|Whole Number|-|0 - 99||
Livrabile depasite|rd_livrabiledepasite|Whole Number|-|0 - 99||
""")

t("TBL-59", "Log de eroare", "rd_logeroare", "rd_name", "Tehnic", 1, """
Denumire|rd_name|Text (200)|O|{flux}_{data}|Generata|Coloana primara
Flux|rd_flux|Text (100)|O|FLX-nn si denumirea||
Correlation ID|rd_correlationid|Text (100)|O||Identificator unic de executie|Vezi 22.6
Data si ora|rd_data|Date and Time|O|Implicit acum||
Tabela afectata|rd_tabela|Text (100)|-|||
Inregistrare afectata|rd_inregistrare|Text (200)|-|GUID sau cod de business||
Mesaj de eroare|rd_mesaj|Text Area (4000)|O|||
Pas al fluxului|rd_pas|Text (200)|-||Unde anume a esuat|
Numar de reincercari|rd_reincercari|Whole Number|-|0 - 10||
Status|rd_statuslog|Choice|O|Nou / In analiza / Rezolvat / Ignorat||
Actiune corectiva|rd_actiune|Text Area (1000)|-|||
""")


doc = collections.OrderedDict([
    ("_descriere", "Modelul de date Dataverse complet. Referinta: Sectiunea 2. Tipurile sunt numite exact ca in Dataverse."),
    ("_reguli", collections.OrderedDict([
        ("prefix_editor", "rd"),
        ("solution", "RDSuitaDigitala"),
        ("nume_logice", "fara diacritice, fara spatii"),
        ("statusuri", "toate Choice, niciodata text liber (2.0.4)"),
        ("date", "Date Only Time Zone Independent, cu exceptia masuratorilor si a miscarilor de mostra, care sunt User Local (2.0.6)"),
        ("audit", "activat pe toate tabelele de proces si pe coloanele de status, termen, decizie si aprobare (5.6.1)"),
        ("stergere", "interzisa prin rol de securitate pe tabelele de proces; inregistrarile se dezactiveaza (11.7.1)"),
        ("calcule_multinivel", "Calculated si Rollup nu acopera calculele pe mai multe niveluri; acestea se fac cu flux si se scriu in coloane simple (2.0.9)"),
    ])),
    ("tipuri_dataverse_folosite", ["Text", "Text Area", "Whole Number", "Decimal", "Currency", "Choice",
                                  "Choice (multi)", "Yes/No", "Date Only", "Date and Time", "Lookup",
                                  "File", "Image", "Autonumber", "Calculated", "Rollup"]),
    ("tabele", T),
])

with open("data/tabele.json", "w") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)

nc = sum(len(x["coloane"]) for x in T)
print("Tabele:", len(T), "| Coloane:", nc)
print("Pe categorie:", dict(collections.Counter(x["categorie"] for x in T)))
print("Pe val:", dict(sorted(collections.Counter(x["val"] for x in T).items())))
