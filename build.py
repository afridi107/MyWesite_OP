#!/usr/bin/env python3
"""Build the J&F Originals website.

Page content lives in src/de/ and src/en/. Each page file starts with a JSON
header in an HTML comment, for example:

    <!--{"title": "...", "description": "...", "nav": "shop", "alt": "en/shop/index.html"}-->

This script wraps every page in the shared layout (head, header with menu,
footer), fixes relative paths and writes plain HTML files to docs/.
The result needs no server: open docs/index.html in a browser.

Run:  python3 build.py
"""
import json
import os
import re
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "docs")
DOMAIN = "https://jandforiginals.de/"
YEAR = "2026"

# ---------------------------------------------------------------- navigation
NAV = {
    "de": [
        {"key": "home", "label": "Home", "href": "index.html"},
        {"key": "services", "label": "Services", "href": "services/index.html", "children": [
            {"label": "Massagesessel", "href": "services/massagesessel.html"},
            {"label": "Kaffeeautomaten", "href": "services/kaffeeautomaten.html"},
            {"label": "Snackautomaten", "href": "services/snackautomaten.html"},
            {"label": "Kinderfahrgeschäfte", "href": "services/kinderfahrgeschaefte.html"},
            {"label": "So funktioniert’s", "href": "services/so-funktionierts.html"},
        ]},
        {"key": "shop", "label": "Shop", "href": "shop/index.html", "children": [
            {"label": "Dua-Aufkleber", "href": "shop/dua-aufkleber.html"},
            {"label": "Himalaya-Salzmühle <small>(bald)</small>", "href": "shop/salzmuehle.html"},
            {"label": "Party-Servietten", "href": "shop/servietten.html"},
        ]},
        {"key": "handmade", "label": "Handgemacht", "href": "handgemacht.html"},
        {"key": "about", "label": "Über uns", "href": "ueber-uns.html"},
        {"key": "contact", "label": "Kontakt", "href": "kontakt.html"},
    ],
    "en": [
        {"key": "home", "label": "Home", "href": "en/index.html"},
        {"key": "services", "label": "Services <small>(DE)</small>", "href": "services/index.html"},
        {"key": "shop", "label": "Shop", "href": "en/shop/index.html", "children": [
            {"label": "Dua stickers", "href": "en/shop/dua-stickers.html"},
            {"label": "Himalayan salt grinder <small>(soon)</small>", "href": "en/shop/salt-grinder.html"},
            {"label": "Party napkins", "href": "en/shop/napkins.html"},
        ]},
        {"key": "handmade", "label": "Handmade", "href": "en/handmade.html"},
        {"key": "about", "label": "About us", "href": "en/about.html"},
        {"key": "contact", "label": "Contact", "href": "en/contact.html"},
    ],
}

T = {
    "de": {"skip": "Zum Inhalt springen", "menu": "Menü öffnen", "home": "J&amp;F Originals – Startseite",
           "nav": "Hauptnavigation", "lang": "Sprache wählen", "sub": "Untermenü öffnen",
           "imprint": ("impressum.html", "Impressum"), "privacy": ("datenschutz.html", "Datenschutz"),
           "footer_sections": "Bereiche", "locale": "de_DE"},
    "en": {"skip": "Skip to content", "menu": "Open menu", "home": "J&amp;F Originals – home",
           "nav": "Main navigation", "lang": "Choose language", "sub": "Open submenu",
           "imprint": ("en/imprint.html", "Imprint"), "privacy": ("en/privacy.html", "Privacy"),
           "footer_sections": "Sections", "locale": "en_GB"},
}

ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'
ICON_CARET = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def rel(root, href):
    """Make a site-relative href ('shop/index.html') relative to the page."""
    if href.startswith(("http", "mailto:", "tel:", "#")):
        return href
    return root + href


def brand(root, lang, home_href):
    return (f'<a class="brand" href="{rel(root, home_href)}" aria-label="{T[lang]["home"]}">'
            '<span class="b-script">J<span class="amp">&amp;</span>F</span><span class="b-caps">Originals</span></a>')


def nav_html(lang, root, active, current_href):
    items = []
    for i, it in enumerate(NAV[lang]):
        cls = ' class="is-active"' if it["key"] == active else ""
        aria = ' aria-current="page"' if it["href"] == current_href else ""
        link = f'<a href="{rel(root, it["href"])}"{aria}>{it["label"]}</a>'
        if it.get("children"):
            sub_id = f"sub-{it['key']}"
            cur = ' aria-current="page"'
            subs = "".join(
                f'<li><a href="{rel(root, c["href"])}"{cur if c["href"] == current_href else ""}>{c["label"]}</a></li>'
                for c in it["children"])
            items.append(
                f'<li{cls} data-has-sub><div class="nav-item">{link}'
                f'<button class="sub-toggle" type="button" aria-expanded="false" aria-controls="{sub_id}" '
                f'aria-label="{T[lang]["sub"]}: {re.sub("<[^>]+>", "", it["label"])}">{ICON_CARET}</button></div>'
                f'<ul class="subnav" id="{sub_id}">{subs}</ul></li>')
        else:
            items.append(f"<li{cls}>{link}</li>")
    return "\n          ".join(items)


def lang_switch(lang, root, alt):
    de_href = rel(root, alt if lang == "en" else "")
    en_href = rel(root, alt if lang == "de" else "")
    if lang == "de":
        return (f'<span aria-current="true" lang="de">DE</span>'
                f'<a href="{en_href}" hreflang="en" lang="en" title="English version">EN</a>')
    return (f'<a href="{de_href}" hreflang="de" lang="de" title="Deutsche Version">DE</a>'
            f'<span aria-current="true" lang="en">EN</span>')


def footer_html(lang, root):
    t = T[lang]
    cols = "".join(f'<li><a href="{rel(root, it["href"])}">{it["label"]}</a></li>' for it in NAV[lang])
    other = ('<a href="{0}en/index.html" hreflang="en">English</a>' if lang == "de"
             else '<a href="{0}index.html" hreflang="de">Deutsch</a>').format(root)
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      {brand(root, lang, "index.html" if lang == "de" else "en/index.html")}
      <address>Raiffeisenstr. 14 · 93173 Wenzenbach<br><a href="tel:+4917676858048">+49 176 76858048</a> · <a href="mailto:info@jandforiginals.de">info@jandforiginals.de</a></address>
    </div>
    <nav aria-label="{t["footer_sections"]}"><ul class="footer-links">{cols}</ul></nav>
    <div class="footer-legal">
      <ul class="footer-links"><li><a href="{rel(root, t["imprint"][0])}">{t["imprint"][1]}</a></li><li><a href="{rel(root, t["privacy"][0])}">{t["privacy"][1]}</a></li><li>{other}</li></ul>
      <p>© {YEAR} J&amp;F Originals®</p>
    </div>
  </div>
</footer>'''


def layout(page, body):
    lang, root, path = page["lang"], page["root"], page["path"]
    t = T[lang]
    alt = page.get("alt")
    hreflang = ""
    canonical = DOMAIN + path.replace("index.html", "")
    if alt:
        de_path, en_path = (path, alt) if lang == "de" else (alt, path)
        hreflang = (f'<link rel="alternate" hreflang="de" href="{DOMAIN}{de_path.replace("index.html", "")}">\n'
                    f'<link rel="alternate" hreflang="en" href="{DOMAIN}{en_path.replace("index.html", "")}">\n'
                    f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{de_path.replace("index.html", "")}">\n')
    switch_target = alt or ("en/index.html" if lang == "de" else "index.html")
    robots = '<meta name="robots" content="noindex, follow">\n' if page.get("noindex") else ""
    jsonld = ""
    if page.get("jsonld"):
        jsonld = ('<script type="application/ld+json">\n'
                  + json.dumps(page["jsonld"], ensure_ascii=False, indent=2) + "\n</script>\n")
    home_href = "index.html" if lang == "de" else "en/index.html"
    title = page["title"]
    full_title = title if "J&amp;F Originals" in title else f"{title} | J&amp;F Originals"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{page["description"]}">
{robots}<link rel="canonical" href="{canonical}">
{hreflang}<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/css/style.css">
<meta property="og:type" content="website">
<meta property="og:site_name" content="J&amp;F Originals">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{page["description"]}">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:url" content="{canonical}">
{jsonld}</head>
<body class="{page.get("bodyclass", "")}">
<a class="skip-link" href="#main">{t["skip"]}</a>

<header class="site-header">
  <div class="container header-inner">
    {brand(root, lang, home_href)}
    <nav class="mainnav" id="mainnav" aria-label="{t["nav"]}">
      <ul class="mainnav-list">
          {nav_html(lang, root, page.get("nav"), path)}
      </ul>
    </nav>
    <div class="header-tools">
      <div class="lang-switch" aria-label="{t["lang"]}">{lang_switch(lang, root, switch_target)}</div>
      <button class="nav-toggle" type="button" aria-controls="mainnav" aria-expanded="false" aria-label="{t["menu"]}">{ICON_MENU}</button>
    </div>
  </div>
</header>

<main id="main">
{body}
</main>

{footer_html(lang, root)}

<script src="{root}assets/js/main.js"></script>
</body>
</html>
'''


# ---------------------------------------------------------------- pages
def read_page(src_file):
    raw = open(src_file, encoding="utf-8").read()
    m = re.match(r"\s*<!--(\{.*?\})-->\s*\n", raw, re.S)
    if not m:
        raise SystemExit(f"{src_file}: missing JSON header")
    meta = json.loads(m.group(1))
    body = raw[m.end():]
    folder = os.path.dirname(src_file)

    def include(mm):
        return open(os.path.join(folder, mm.group(1)), encoding="utf-8").read()
    for _ in range(3):  # nested includes
        body = re.sub(r"\{\{include:([^}]+)\}\}", include, body)
    return meta, body


def build():
    pages = []
    for lang in ("de", "en"):
        base = os.path.join(SRC, lang)
        for dirpath, _, files in os.walk(base):
            for f in sorted(files):
                if not f.endswith(".html") or f.startswith("_"):
                    continue
                src_file = os.path.join(dirpath, f)
                relpath = os.path.relpath(src_file, base).replace(os.sep, "/")
                path = relpath if lang == "de" else "en/" + relpath
                meta, body = read_page(src_file)
                depth = path.count("/")
                page = dict(meta, lang=lang, path=path, root="../" * depth)
                body = body.replace("{{root}}", page["root"])
                html = layout(page, body)
                out_file = os.path.join(OUT, path)
                os.makedirs(os.path.dirname(out_file), exist_ok=True)
                open(out_file, "w", encoding="utf-8").write(html)
                pages.append(page)

    # sitemap.xml (indexable pages only)
    urls = []
    for p in pages:
        if p.get("noindex"):
            continue
        loc = DOMAIN + p["path"].replace("index.html", "")
        alts = ""
        if p.get("alt"):
            de_path, en_path = (p["path"], p["alt"]) if p["lang"] == "de" else (p["alt"], p["path"])
            alts = (f'\n    <xhtml:link rel="alternate" hreflang="de" href="{DOMAIN}{de_path.replace("index.html", "")}"/>'
                    f'\n    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}{en_path.replace("index.html", "")}"/>')
        urls.append(f"  <url>\n    <loc>{loc}</loc>{alts}\n  </url>")
    open(os.path.join(OUT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n")
    open(os.path.join(OUT, "robots.txt"), "w").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}sitemap.xml\n")
    print(f"Built {len(pages)} pages into docs/")


if __name__ == "__main__":
    build()
