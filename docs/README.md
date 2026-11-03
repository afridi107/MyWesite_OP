# J&F Originals – website (multi-page)

One website for both lines of business:

- **Services:** vending and lounge concepts for commercial premises. German only.
- **Shop:** products for your home, sold on Amazon. German and English.
- **Handgemacht:** crochet products, sold on Etsy. German and English.

Plain static HTML, CSS and a little JavaScript. No server, cookies or tracking, and no external requests (the fonts are self-hosted).

## Open locally

Double-click `docs/index.html`. Every page and link works straight from the file system.

## Editing and building

The content lives in `src/`, and `build.py` creates the finished pages in `docs/`.

- `src/de/…` holds the German pages and `src/en/…` the English ones. The folder structure becomes the URL structure.
- Each page starts with a JSON header: title, description, active menu item, matching page in the other language.
- Files starting with `_` are shared blocks, included with `{{include:_name.html}}` (e.g. the Services call-to-action and the legal texts).
- **The menu, the footer and the language switch are defined once, in `build.py`** (`NAV`).

After any change:

```bash
python3 build.py
```

This regenerates all pages, `sitemap.xml` and `robots.txt`. Images, CSS and JS live in `docs/assets/` and are not touched by the build.

## Pages

| Menu | German | English |
|---|---|---|
| Home | `index.html` | `en/index.html` |
| Services ▾ | `services/index.html`, `massagesessel`, `kaffeeautomaten`, `snackautomaten`, `kinderfahrgeschaefte`, `so-funktionierts` | — (the menu item links to the German pages, marked "(DE)") |
| Shop ▾ | `shop/index.html`, `dua-aufkleber`, `salzmuehle`, `servietten` | `en/shop/index.html`, `dua-stickers`, `salt-grinder`, `napkins` |
| Handgemacht | `handgemacht.html` | `en/handmade.html` |
| Über uns | `ueber-uns.html` | `en/about.html` |
| Kontakt | `kontakt.html` (enquiry form for businesses + product questions) | `en/contact.html` |
| Footer | `impressum.html`, `datenschutz.html` | `en/imprint.html`, `en/privacy.html` |

The menu has dropdowns on desktop (from 1200 px). Below that it's the ☰ menu, with sub-items opened by the arrow buttons.

## Domain

All canonical, hreflang, sitemap and schema.org URLs use `https://jandforiginals.de/`. Merging the two sites resolved the earlier domain conflict. To change the domain, edit `DOMAIN` in `build.py` and rebuild.

## Open items

1. **Datenschutz/Privacy:** hosting provider, its address and the data processing agreement; server log retention period; date ("Stand"). These are marked `[PLATZHALTER]`. Have the Impressum and Datenschutz checked by a legal-text service before going live.
2. **B2B images:** the original B2B README noted that the Canva/stock images (foyer, Konzept, product and coffee images) need a licence check. The foyer image also shows a visible "Nespresso" logo and an invented "Coffee & Massage Partners" sign. Check this before going live, or replace the image with your own photo.
3. **B2B wording:** I softened the claims when moving the text over. "100 % risikofrei" became "ohne eigene Investition", "das gesamte Risiko" became "Anschaffung, Aufbau und Betrieb", and "passiver Umsatz" became "Standplatzmiete oder Umsatzbeteiligung". "Financial Model" is now called "Konditionen".
4. **"Über uns" text:** a draft from known facts, marked with a TODO. Please review it.
5. **Hero photo:** the frame says "Wenn das Dua der Essen vergessen wird", which is ungrammatical. A corrected version is welcome.
6. **German print design vs. photo:** the German print-design PDF (curl ornaments) and the German stickers in the door photo (leaf ornaments) differ.
7. **The old B2B repository** (`afridi107/MyWebsite`) is not changed by this. It can be archived once this site is live.

## Images

- **Products:** `docs/assets/img/products/` (WebP in several sizes).
- **Services:** `docs/assets/img/services/` (AVIF/WebP with a JPG fallback, taken from the B2B site).
- **Originals:** the original photo uploads stay in the repo root folders (`Blau/`, `Etsy/`, …) and aren't used directly.
