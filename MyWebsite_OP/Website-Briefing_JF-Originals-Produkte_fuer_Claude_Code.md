# Website brief – J&F Originals product website (consumer products)

**For:** Claude Code · **Owner:** Jehan Khan Afridi · **Status:** 02.11.2026
**Goal:** A brand and product website (B2C) for the products J&F Originals sells online. It presents the products attractively, builds trust and sends visitors to where they can buy. **Version 1 is a product showcase with "Jetzt kaufen" buttons that link to the existing Amazon and Etsy listings. It has no shop of its own: no cart, no checkout, no payments.** Section 8 describes what a shop of its own would need later.

Build it as plain static files that can be opened locally in the browser. Hosting is decided later; don't build anything that depends on a particular host.

Do not invent facts, product properties, test results, reviews, customer numbers or prices. Where information is missing, insert a clearly marked placeholder (`[PLATZHALTER: …]`) and list it in the README.

---

## 1. Business facts

| Item | Value |
|---|---|
| Brand | **J&F Originals** |
| Owner | Jehan Khan Afridi (Einzelunternehmen) |
| Address | Raiffeisenstr. 14, 93173 Wenzenbach, Deutschland |
| Phone | +49 176 76858048 |
| Email | info@jandforiginals.de |
| USt-IdNr. | DE455771208 |
| Sales channels today | Amazon.de (main), Amazon.co.uk, Amazon.sa (occasional), Etsy |
| Languages | **German** (main market) and **English** (strong UK sales). Build with a language switch DE/EN. German is the default. |

**Never on the website:** sales figures, margins, purchase prices, suppliers' names, stock levels, tax matters, the B2B vending business (that has its own website).

---

## 2. Product range for version 1

### 2.1 Islamic Dua stickers (main product, already selling)

The bestseller: sets of **12 pre-printed daily duas (supplications)** on vinyl sticker paper, for walls, doors, mirrors, plastic and ceramic surfaces. Intended for home, school or as a gift, for children and adults.

| Variant | Languages on the sticker | Look | Amazon DE | Amazon UK |
|---|---|---|---|---|
| Arabisch + Deutsch, transparent | Arabic / German | clear background | [amazon.de/dp/B0F8VQGDZ8](https://www.amazon.de/dp/B0F8VQGDZ8) | – |
| Arabisch + Deutsch, weiß | Arabic / German | white | [amazon.de/dp/B0F91BPRGZ](https://www.amazon.de/dp/B0F91BPRGZ) | – |
| Arabic + English ("Daily Supplications") | Arabic / English | white | [amazon.de/dp/B0FDVJSX24](https://www.amazon.de/dp/B0FDVJSX24) | [amazon.co.uk/dp/B0FDVJSX24](https://www.amazon.co.uk/dp/B0FDVJSX24) |
| Arabic + English, white edition | Arabic / English | white | [amazon.de/dp/B0FDWNMXJL](https://www.amazon.de/dp/B0FDWNMXJL) | [amazon.co.uk/dp/B0FDWNMXJL](https://www.amazon.co.uk/dp/B0FDWNMXJL) |
| Arabic + English + German, clear | Arabic / English / German | clear background | [amazon.de/dp/B0GP6YP3DD](https://www.amazon.de/dp/B0GP6YP3DD) | [amazon.co.uk/dp/B0GP6YP3DD](https://www.amazon.co.uk/dp/B0GP6YP3DD) |
| Arabic + English, Black & White | Arabic / English | black & white | – | [amazon.co.uk/dp/B0GM8J5HFS](https://www.amazon.co.uk/dp/B0GM8J5HFS) |

- Facts for the copy: 12 duas per set; pre-printed; vinyl sticker paper; languages as in the table; suitable for walls, doors, mirrors, plastic, ceramic; for kids and adults; as a gift.
- Do not claim anything else (e.g. "waterproof", "removable without residue", sizes) unless the owner confirms it: `[PLATZHALTER: Größe der Aufkleber / Bogenmaß]`, `[PLATZHALTER: wasserfest? rückstandslos ablösbar?]`.
- Show **no prices** on the site in v1, since Amazon prices change. The button text says "Bei Amazon ansehen" / "View on Amazon".
- Tone: warm and respectful. This is religious content, so no jokes and no stock photos of people praying. Arabic text must be rendered right-to-left correctly (`dir="rtl"`, `lang="ar"`) wherever it appears.

### 2.2 Himalaya-Salzmühle (new: "Bald erhältlich" / "Coming soon", launch planned around January 2027)

| Fact | Value (from the supplier's order confirmation) |
|---|---|
| Product | Verstellbare Glasmühle mit Stahldeckel (long version), mit Etikett |
| Contents | Himalaya-Salz, grob – 200 g (7 oz) |
| Grain size | mainly 2–5 mm, dark pink |
| Origin of the salt | Pakistan |
| Packaging | each grinder bubble-wrapped in an individual printed box |
| Grinding mechanism | ceramic grinder (owner's information) |

- Section with a "Bald erhältlich – jetzt vormerken" (coming soon) message and a `mailto:` button "Benachrichtigen, wenn verfügbar" (notify me when available). Don't build a newsletter form; that would need double opt-in and a mailing service.
- **Strictly no health or nutrition claims** (EU Health Claims Regulation 1924/2006). Not allowed: "84 Mineralien", "entgiftend", "gesünder als Speisesalz", "basisch", "reguliert den Blutdruck" and similar. Allowed are descriptions of taste, look, grain and use: "für Fleisch, Fisch, Gemüse und Salate", "fein bis grob einstellbar", "schönes Rosa auf dem Tisch", "nachfüllbar"? → `[PLATZHALTER: Mühle nachfüllbar?]`.
- **Lab test:** a sample was analysed by Eurofins in June 2026 (microbiology and heavy metals). Mention it **only** if the owner confirms the result was fine and the test applies to the product being sold → `[PLATZHALTER: Laborprüfung erwähnen? ja/nein]`.
- Mandatory food information for the product page (for the later shop at the latest; good practice already in v1): Verkehrsbezeichnung ("Steinsalz aus Pakistan, grob" or as on the label), Nettofüllmenge 200 g, Ursprungsland Pakistan, Name und Anschrift des Lebensmittelunternehmers (J&F Originals, address above). Take the exact wording from the final label: `[PLATZHALTER: Etikettentext]`.

### 2.3 Birthday napkins (optional, remaining stock on Amazon)

Plain coloured paper napkins for birthdays and parties, 2-ply, 33 × 33 cm, packs of 20 (some colours 16). Colours on Amazon.de include Blau, Schwarz, Regenbogen, Rosa, Gelb, Weiß, Multi and castle motifs.
- ASINs (Amazon.de): Blau B0H2J1K6NH · Schwarz B0H2HWHGMT · Regenbogen B0H2FKR7NY · Rosa B0H2FQGMK5 · Weiß B0H2FV98T7 · Multi B0H2FSRNGJ
- **Only include this section if the owner says yes**: `[PLATZHALTER: Servietten anzeigen? ja/nein]`. Never show the Hello Kitty napkins or any other licensed characters or brands.

### 2.4 Not included
Candle tattoos (discontinued), digital downloads (negligible), snack boxes (still undecided). Leave them out unless the owner adds them.

---

## 3. Page structure

1. **Header:** logo/wordmark "J&F Originals", navigation (Dua-Aufkleber · Salzmühle · Über uns · Kontakt), DE/EN switch.
2. **Hero:** short brand statement, e.g. "Liebevoll gestaltete Produkte für Zuhause" / "Thoughtfully designed products for your home" (suggestion, owner can change), with a large image of the Dua stickers and a button "Dua-Aufkleber entdecken".
3. **Dua-Aufkleber:** intro text, variant cards (image, title, languages, look, "Bei Amazon ansehen" buttons for DE and/or UK as in the table), "So einfach geht's" (3 steps: aussuchen – aufkleben – jeden Tag erinnert werden), gallery of application photos.
4. **Himalaya-Salzmühle (coming soon):** image, product facts from 2.2, coming-soon badge, notify button.
5. **(Optional) Servietten**
6. **Über uns:** short, personal text about J&F Originals as a small family business from Wenzenbach near Regensburg → `[PLATZHALTER: Text "Über uns" vom Inhaber]`. No invented history.
7. **Wo kaufen?** Buttons for Amazon.de, Amazon.co.uk and Etsy (`[PLATZHALTER: Etsy-Shop-URL]`, `[PLATZHALTER: Amazon-Storefront-URL, falls vorhanden]`).
8. **Kontakt:** phone, email (mailto), no form in v1.
9. **Footer:** Impressum · Datenschutz · © 2026 J&F Originals.

---

## 4. Design

- **Same brand family as the J&F Originals B2B website**, but lighter and more product-focused (a consumer audience instead of property managers):
  - background `#F6F4F1`, accent rust `#A8500B`, brown `#79573D`, dark grey `#494F56`, light tint `#ECDFD4`;
  - fonts (self-hosted): script accent "Alex Brush" or "Mrs Saint Delafield", headlines "Bebas Neue", labels "Noto Sans", body "Lora";
  - for the Arabic sample text use "Amiri" or "Noto Naskh Arabic" (self-hosted).
- Product photos on calm backgrounds, generous whitespace, rounded rust "Bei Amazon ansehen" buttons, a small rust "Bald erhältlich" badge on the salt grinder.
- Mobile-first: most visitors will come from Instagram, Pinterest or Amazon on a phone.

---

## 5. Technical requirements

- Static site (HTML/CSS/vanilla JS, or Astro producing static output). Must open locally from `index.html` or via a simple local preview; no backend.
- DE/EN: either two folders (`/` and `/en/`) or one page with a JS language switch. Prefer real separate pages for SEO, with `hreflang` tags.
- Images: WebP in several sizes with `srcset`, lazy-loading, German/English alt texts.
- **No cookies, no tracking, no embeds (YouTube, Instagram, Google Maps), no external font or CDN requests.** Then no cookie banner is needed.
- Amazon/Etsy links: `target="_blank" rel="noopener"`. No Amazon logos, except the official "Available at Amazon" badge according to Amazon's brand guidelines.
- SEO:
  - titles and descriptions per page;
  - schema.org `Product` markup for each Dua variant, without price/offer and without ratings;
  - `Organization` markup;
  - `sitemap.xml` and `robots.txt`.
  - Keywords: "Dua Aufkleber", "islamische Wandaufkleber", "Dua Sticker Kinder", "Islamic dua stickers", "Himalaya Salz Mühle".
- Favicon: "J&F" monogram in rust (SVG).
- README: how to preview locally, list of all `[PLATZHALTER]`, list of images still missing.

---

## 6. Legal pages (Germany)

- **Impressum** (§ 5 DDG):
  - Jehan Khan Afridi, J&F Originals, Raiffeisenstr. 14, 93173 Wenzenbach
  - Telefon +49 176 76858048, E-Mail info@jandforiginals.de
  - USt-IdNr. DE455771208
- **Datenschutzerklärung:** placeholder structure for:
  - responsible person;
  - hosting (`[PLATZHALTER: Hoster]`);
  - server logs;
  - email contact;
  - self-hosted fonts;
  - no cookies or tracking;
  - outgoing links to Amazon/Etsy (their own privacy policies apply once the visitor is there);
  - data-subject rights;
  - supervisory authority (Bayerisches Landesamt für Datenschutzaufsicht).
  Mark it: `<!-- TODO: Text vom Inhaber final prüfen / mit Generator erstellen -->`.
- **Trademark:** use "J&F Originals" as plain text. Don't add ® unless the owner confirms the trademark is registered: `[PLATZHALTER: Marke eingetragen? Welcher Name?]`.
- No customer reviews or star ratings copied from Amazon (Amazon's terms prohibit it, and fake or uncredited reviews are unlawful). A neutral line is fine: "Bewertungen finden Sie direkt bei Amazon."

---

## 7. Images: to be supplied by the owner

None of the product photos exist in this folder yet. Ask the owner for:

1. **Dua stickers:** the main Amazon listing images (his own) for each variant, plus 2–4 photos of the stickers applied at home (on a door, mirror or wall).
2. **Salt grinder:** a photo of the actual grinder and printed box from the supplier's samples or the first delivery, plus the final label design (the Fiverr design from August 2026). Until then use a neutral placeholder graphic, not a stock photo of another brand's grinder.
3. **Napkins:** the Amazon images, only if section 2.3 is included.
4. **Logo:** if none exists, create a simple text wordmark "J&F Originals" (script + capitals as in the B2B site).

Use only images the owner owns or supplies. No stock photos with recognisable people, no images taken from other Amazon listings.

---

## 8. Later: own online shop (not part of v1, for information only)

If the owner later wants to sell directly on the website, this is needed in addition:
- shop system (e.g. Shopify or WooCommerce) with a payment provider;
- AGB, Widerrufsbelehrung plus a model withdrawal form, and a withdrawal button ("Vertrag widerrufen", mandatory from 19.06.2026);
- the "zahlungspflichtig bestellen" order button;
- prices with "inkl. MwSt., zzgl. Versandkosten" (PAngV) and a shipping cost page;
- packaging registration (LUCID number, VerpackG);
- full food information for the salt before purchase (Art. 14 LMIV);
- EU VAT: orders from other EU countries are reported through the OSS scheme the business already uses.

These pages should be written or checked with a legal-text service (e.g. IT-Recht Kanzlei, Händlerbund, e-recht24), not freely invented.

---

## 9. Open questions for the owner (ask before building)

1. Which products should appear in v1: Dua stickers + salt grinder only, or the napkins too?
2. Is there an Etsy shop URL and/or an Amazon brand storefront URL?
3. Which name was applied for at the DPMA (2025), and is it registered?
4. Sticker details: size of the stickers/sheet, waterproof?, removable without residue?
5. Salt grinder: may the Eurofins lab test be mentioned? Is the grinder refillable? Final label text?
6. A short "Über uns" text in the owner's own words.
7. Product photos (section 7).
