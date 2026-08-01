# Asediu la Apus

Joc de asediu în browser — catapultă și balistă contra cetăților, cu fizică reală
(Matter.js), 26 de niveluri în 4 capitole și editor de cetăți.

## Cum îl rulezi

Deschide `index.html` în browser. Nu are nevoie de server sau de instalare —
motorul fizic (`matter.min.js`) e inclus în repo, deci merge și offline.

## Ce conține

- **26 de asedii** în 4 capitole, fiecare cu atmosfera lui: Câmpia de Apus,
  Nordul Înghețat, Deșertul de Aramă, Furtuna de Miez de Noapte.
- **Două mașini de asediu** — catapultă (arc înalt, trece peste ziduri) și
  balistă (traiectorie întinsă, precisă).
- **8 tipuri de muniție** — bolovan, ghiulea, butoi exploziv, tripletă,
  plus patru tipuri de săgeți pentru balistă.
- **Materiale cu comportament propriu** — piatră, lemn, gheață, fier și butoaie
  cu praf de pușcă; zidurile se fisurează, se sparg în fragmente și lasă cratere.
- **Editor** — construiește-ți propria cetate și asediaz-o.

## Grafică

Randare pe canvas cu pipeline propriu: cer în straturi cu parallax, raze
volumetrice, nori și vreme per capitol (jar, ninsoare, praf, ploaie cu fulgere),
umbre proiectate pe teren, particule pe bază de sprite-uri, bloom aditiv,
gradare de culoare și grain.

Materialele sunt generate procedural (zgomot cu relief calculat din propriul
câmp de înălțime), iar fiecare bloc primește grosime — o față laterală
orientată după poziția camerei — plus lumină direcțională recalculată din
unghiul lui real, așa că umbrirea se rotește odată cu zidul care se prăbușește.
Suprafața fiecărui bloc e desenată o singură dată într-un cache; per cadru
rămâne doar lumina.

Mișcările sunt legate de fizică: roțile se rotesc exact cât se deplasează
carul la recul, sacul catapultei rămâne în urmă și biciuiește la lansare,
tamburul se învârte cât e întins brațul, iar soldații pășesc după distanța
parcursă efectiv — se opresc când sunt opriți. Pelerinele, penajele și
stindardele se înclină după vântul din nivel.

Butonul **FX** comută între `ULTRA`, `BOGAT` și `RAPID`. Calitatea coboară
automat dacă rata de cadre scade, până când o fixezi manual din buton.
