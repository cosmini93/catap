# catap

**Asediu la Apus** — un joc de catapultă/asediu, într-un singur fișier `index.html`, fără biblioteci externe, fără CDN-uri.

## Cum îl joci pe telefon

Fișierul `index.html` folosește JavaScript, așa că **nu poate fi deschis direct** din previzualizatorul de fișiere al telefonului (de ex. app-ul Files de pe iPhone) — trebuie servit printr-un server web.

Cel mai simplu mod, prin GitHub Pages:

1. Pe GitHub, în acest repo, mergi la **Settings → Pages**.
2. La **Build and deployment → Source**, alege **Deploy from a branch**.
3. Alege branch-ul cu jocul (`claude/github-mobile-game-access-2u18hl`, sau `main` după ce va fi unit) și folderul `/ (root)`.
4. Salvează. După un minut, GitHub va afișa adresa (ceva de forma `https://<user>.github.io/catap/`).
5. Deschide acea adresă în Safari (iPhone) sau Chrome (Android) — jocul rulează direct în browser, fără instalare.

Pasul acesta de activare a Pages se face o singură dată, manual din Settings, din motive de permisiuni (Claude nu poate schimba setările repo-ului automat).