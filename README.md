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
- **Campanie cu aur** — fiecare asediu îți lasă pradă, iar în *Arsenal* o dai pe
  îmbunătățiri: putere de lansare, lovituri în plus, muniție, proiectile mai grele,
  ochire pe vânt și foc grecesc. Progresul se salvează pe dispozitiv.
- **Foc care se propagă** — cu foc grecesc, butoaiele aprind lemnul; focul trece
  din grindă în grindă, topește gheața și mistuie cetatea mult după impact.

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

## Varianta 3D (`catapult3d.html`)

Un al doilea joc, pe altă tehnologie: WebGL (three.js) cu fizică 3D (cannon-es),
cameră din spatele praștiei și forturi care se dezmembrează bloc cu bloc.

Mecanica e pe tensiune: ții apăsat ca să întinzi praștia, tragi cu degetul ca să
ochești, eliberezi la momentul potrivit. Bara urcă până sus și apoi coboară
înapoi, deci momentul eliberării contează.

Terenul e o plasă deformabilă cu relief propriu și sol real în fizică: bolovanii
sapă gropi cu buză ridicată și pământ răscolit acolo unde cad, iar praful se
ridică la impact.

La ochire vezi arcul prezis punct cu punct plus inelul de aterizare pe sol, deci
știi unde cade înainte să eliberezi. Bara de tensiune e segmentată, cu zonă de
maxim marcată și procent afișat.

Piatra se sparge: la o lovitură destul de tare blocul se sfărâmă în moloz care
zboară mai departe și dărâmă ce prinde.

Șase tipuri de fort (turn de strajă, poarta gemenilor, donjon, zid lung, cetate
cu turnuri, citadelă) peste trei ținuturi (dune, creastă înghețată, câmpie de
miez de noapte), care cresc în mărime și garnizoană pe măsură ce avansezi.
Aur și scor salvate pe dispozitiv.

Se construiește cu:

```sh
npm pack three@0.169.0 cannon-es@0.20.0     # sursele bibliotecilor
sh src3d/build.sh <esbuild> <three.module.min.js> <cannon-es.js> catapult3d.html
```

Rezultatul e un singur fișier HTML, fără dependențe externe.
