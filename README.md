# Daily Lyrics

Roz ek naya Kabir doha — synced word-by-word lyrics, alag animation, code se bana flower background.
GitHub Actions roz subah 6 baje (IST) site rebuild + deploy karta hai.

## Setup (ek baar)
1. GitHub pe naya repo `daily-lyrics` banao, ye saari files push karo (branch `main`).
2. Repo → Settings → Pages → Source: **GitHub Actions**.
3. Actions tab → "Daily lyrics publish" → Run workflow (pehli baar). Uske baad roz khud chalega.

## Naye dohe jodna
`songs.json` me entry add karo: `title, poet, flower, anim, palette[4], lines[]`.
- flower: lotus, rose, marigold, jasmine, sunflower, cherry, hibiscus
- anim: blur, glow, rise, type, zoom, wave

Sirf public-domain ya apne likhe lyrics rakho (filmi gaane copyrighted hain).

## Audio
Page par "Apni audio lagao" se apni (royalty-free / khud ki) audio chala sakte ho.

## Local test
`python3 scripts/publish_daily.py && python3 -m http.server -d site`
