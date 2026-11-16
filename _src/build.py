"""Genera il sito statico in italiano, inglese e tedesco. Uso:  python _src/build.py
Legge _src/data.py (contenuti in italiano), _src/i18n.py (traduzioni EN/DE) e _src/images.json
(creato da fetch_assets.py) e scrive le pagine HTML, più sitemap.xml, robots.txt e asset.
Italiano agli stessi URL del vecchio sito; inglese sotto /en/, tedesco sotto /de/."""
import copy, datetime, hashlib, html, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
sys.path.insert(0, str(SRC))
import data  # noqa: E402
import i18n  # noqa: E402
from data import SITE, DISTANCES  # noqa: E402

IMGS = json.loads((SRC / "images.json").read_text(encoding="utf-8"))
PH, PANO = IMGS["photos"], IMGS["panos"]
U = SITE["url"]
TODAY = datetime.date.today().isoformat()
PAGES = []  # (key, lang, images) per la sitemap
e = html.escape

# Contenuti originali in italiano: per ogni lingua se ne fa una copia tradotta (vedi localize()).
IT_DATA = dict(STAYS=data.STAYS, VILLAGES=data.VILLAGES, EXPS=data.EXPS, FAQ=data.FAQ, FARIE=data.FARIE, SERVICES=data.SERVICES)
STAYS, VILLAGES, EXPS, FAQ, FARIE, SERVICES = IT_DATA["STAYS"], IT_DATA["VILLAGES"], IT_DATA["EXPS"], IT_DATA["FAQ"], IT_DATA["FARIE"], IT_DATA["SERVICES"]
STAY, VILL, VILL_BY_NAME = {}, {}, {}


# ---------------------------------------------------------------- lingue
LANGS = ("it", "en", "de")
LANG = "it"
CUR_KEY = "home"
LANG_NAME = {"it": "Italiano", "en": "English", "de": "Deutsch"}
OG_LOCALE = {"it": "it_IT", "en": "en_GB", "de": "de_DE"}
MISSING_TR = {}


def t(s):
    """Traduce una stringa dell'interfaccia (chiave: il testo italiano)."""
    if LANG == "it":
        return s
    tr = i18n.UI.get(s)
    if tr is None:
        MISSING_TR.setdefault(LANG, set()).add(s)
        return s
    return tr[LANGS.index(LANG) - 1]


def tf(s, **kw):
    return t(s).format(**kw)


def low(s):
    """Minuscolo per l'inizio di una frase, ma non in tedesco (i sostantivi restano maiuscoli)."""
    return s if LANG == "de" else s.lower()


# Percorsi di ogni pagina nelle tre lingue (it, en, de)
ROUTES = {
    "home": ("/", "/en/", "/de/"),
    "catalog": ("/it/alloggi/", "/en/accommodation/", "/de/unterkuenfte/"),
    "territorio": ("/it/territorio", "/en/territory", "/de/gebiet"),
    "contact": ("/it/contact", "/en/contact", "/de/kontakt"),
    "exp:trekking": ("/it/trekking", "/en/trekking", "/de/wandern"),
    "exp:cicloturismo": ("/it/cicloturismo", "/en/cycle-touring", "/de/radfahren"),
    "exp:arte-e-cultura": ("/it/arte-e-cultura", "/en/art-and-culture", "/de/kunst-und-kultur"),
    "exp:visita-la-carnia": ("/it/visita-la-carnia", "/en/visit-carnia", "/de/carnia-entdecken"),
    "benessere": ("/it/benessere", "/en/wellness", "/de/wellness"),
    "svc:bagno-di-bosco": ("/it/bagno-di-bosco", "/en/forest-bathing", "/de/waldbaden"),
    "svc:sauna": ("/it/sauna", "/en/sauna", "/de/sauna"),
    "svc-results": (data.WELORA["results"], "/en/book-wellness", "/de/wellness-buchen"),
    "farie": ("/la-farie", "/en/la-farie", "/de/la-farie"),
    "farie-results": (data.FARIE["welora"]["results"], "/en/la-farie-booking", "/de/la-farie-buchen"),
    "farie-cond": ("/la-farie-condizioni", "/en/la-farie-terms", "/de/la-farie-bedingungen"),
    "privacy": ("/privacy", "/en/privacy", "/de/datenschutz"),
    "cookies": ("/cookies", "/en/cookies", "/de/cookies"),
    "terms": ("/condizioni-servizi", "/en/service-terms", "/de/service-bedingungen"),
    "booking-terms": ("/condizioni-prenotazione", "/en/booking-terms", "/de/buchungsbedingungen"),
    "404": ("/404", "/404", "/404"),
}
STAY_BASE = {"it": "/it/alloggi/", "en": "/en/accommodation/", "de": "/de/unterkuenfte/"}
ONLY_IT = {"404"}  # pagine solo in italiano


def P(key, lang=None):
    lang = lang or LANG
    if key.startswith("stay:"):
        return STAY_BASE[lang] + key[5:]
    if key.startswith("vill:"):
        return f"/{lang}/{key[5:]}"
    return ROUTES[key][LANGS.index(lang)]


def localize(lang):
    """Rende globali i contenuti nella lingua richiesta, sovrascrivendo i campi tradotti in i18n.CONTENT."""
    global STAYS, VILLAGES, EXPS, FAQ, FARIE, SERVICES, STAY, VILL, VILL_BY_NAME, LANG
    LANG = lang
    stays, villages, exps = copy.deepcopy(IT_DATA["STAYS"]), copy.deepcopy(IT_DATA["VILLAGES"]), copy.deepcopy(IT_DATA["EXPS"])
    faq, farie, services = list(IT_DATA["FAQ"]), copy.deepcopy(IT_DATA["FARIE"]), copy.deepcopy(IT_DATA["SERVICES"])
    for s in stays:
        s["pets"] = "Animali ammessi" in s.get("am", [])
    if lang != "it":
        C = i18n.CONTENT[lang]
        for s in stays:
            s.update(C["stays"].get(s["id"], {}))
            s["label"] = t(s["label"])
            s["am"] = [t(a) for a in s.get("am", [])]
        for v in villages:
            o = C["villages"].get(v["id"], {})
            if "f" in o:
                v["f"] = dict(v["f"], **o.pop("f"))
            v.update(o)
        for k, x in exps.items():
            o = copy.deepcopy(C["exps"].get(k, {}))
            for field in ("routes", "items"):
                for i, r in enumerate(o.pop(field, [])):
                    x[field][i].update(r)
            x.update(o)
        faq = C["faq"]
        farie.update(C["farie"])
        for s in services:
            s.update(C["services"].get(s["id"], {}))
    STAYS, VILLAGES, EXPS, FAQ, FARIE, SERVICES = stays, villages, exps, faq, farie, services
    STAY = {s["id"]: s for s in STAYS}
    VILL = {v["id"]: v for v in VILLAGES}
    VILL_BY_NAME = {v["n"]: v for v in VILLAGES}


# ---------------------------------------------------------------- helpers
OLD_FILES = "https://albergodiffusosocchieve.it/sites/default/files/"
MISSING = set()


def remote(name):
    MISSING.add(name)
    return name if name.startswith("http") else OLD_FILES + name


def img_url(name, w=1600):
    m = PH.get(name)
    if not m:
        return remote(name)
    ws = [x for x in m["widths"] if x <= w] or m["widths"][:1]
    return f"/img/{m['slug']}-{ws[-1]}.webp"


def abs_img(name, w=1600):
    u = img_url(name, w)
    return u if u.startswith("http") else U + u


def og_img(name):
    o = PH.get(name, {}).get("og")
    return U + o if o else abs_img(name)


def pic(name, alt, sizes="100vw", cls="", eager=False, attrs=""):
    m = PH.get(name)
    if not m:
        load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
        return f'<img{f" class={chr(34)}{cls}{chr(34)}" if cls else ""} src="{remote(name)}" alt="{e(alt)}" {load} {attrs}>'
    ws = m["widths"]
    big = ws[-1]
    srcset = ", ".join(f"/img/{m['slug']}-{x}.webp {x}w" for x in ws)
    src = f"/img/{m['slug']}-{[x for x in ws if x <= 960][-1] if any(x <= 960 for x in ws) else ws[0]}.webp"
    h = round(m["h"] * big / m["w"])
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{src}" srcset="{srcset}" sizes="{sizes}" width="{big}" height="{h}" alt="{e(alt)}" {load} {attrs}>'


def I(name):
    return f'<svg aria-hidden="true"><use href="#i-{name}"/></svg>'


def stay_url(s): return P("stay:" + s["id"])
def vill_url(v): return P("vill:" + v["id"])
def exp_url(k): return P("exp:" + k)
def svc_url(s): return P("svc:" + s["id"])
def beds(n): return tf("Fino a {n} ospiti", n=n)
def stars(n): return tf("{n} stelle", n=n)
def size(n): return "s" if n <= 8 else "m" if n <= 16 else "l"
def top_stays(): return [s for s in STAYS if not s.get("parent")]
def stays_in(b): return [s for s in STAYS if s["b"] == b and not s.get("parent")]
def dist_items(): return "".join(f"<li><b>{e(t(n))}</b><span>{km} km · {tf('circa {t}', t=tm)}</span></li>" for n, km, tm in DISTANCES)


def clip(text, n=158):
    text = " ".join(text.split())
    if len(text) <= n: return text
    cut = text[:n].rsplit(" ", 1)[0].rstrip(",;:·-")
    return cut + "…"


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": U + p} for i, (n, p) in enumerate(items)]}


def address(street, locality=None):
    return {"@type": "PostalAddress", "streetAddress": street, "addressLocality": locality or "Socchieve",
            "postalCode": SITE["zip"], "addressRegion": SITE["region"], "addressCountry": "IT"}


LODGING_ID = U + "/#lodging"


def relativize(doc, depth):
    """Percorsi relativi: il sito funziona sia nella radice del dominio sia in una
    sottocartella (es. GitHub Pages /adsocchieve/)."""
    pre = "../" * depth
    doc = re.sub(r'((?:href|src|imagesrcset|srcset)=")/(?!/)', lambda m: m.group(1) + pre, doc)
    doc = re.sub(r'(,\s*)/(img/)', lambda m: m.group(1) + pre + m.group(2), doc)
    doc = doc.replace('"/img/', '"' + pre + 'img/')
    return doc.replace('href=""', 'href="./"')


BASE_404 = """<script>(function(){var p=location.pathname.split('/')[1];var b=(/github[.]io$/.test(location.hostname)&&p)?'/'+p+'/':'/';document.write('<base href="'+b+'">');})();</script>"""


# ---------------------------------------------------------------- layout
def asset_ver(p):
    return hashlib.md5(p.read_bytes()).hexdigest()[:8]


def nav():
    return [("alloggi", P("catalog"), t("Le case")), ("borghi", P("territorio") + "#borghi", t("I borghi")),
            ("esperienze", P("territorio") + "#esperienze", t("Esperienze")), ("benessere", P("benessere"), t("Benessere")),
            ("contatti", P("contact"), t("Contatti")), ("farie", P("farie"), "La Farie")]


ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="i-left" viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="i-right" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21Z" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="9.5" r="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M5 4h3l2 5-2.5 1.5a11 11 0 0 0 6 6L15 14l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
  <symbol id="i-mark" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M6 28 15 15l5 7 4-5 10 11" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M17 28v-5h6v5" fill="none" stroke="currentColor" stroke-width="1.4"/></symbol>
</svg>"""


def lightbox():
    return f"""<dialog class="lb" data-lb aria-label="{t('Galleria fotografica')}">
  <div class="lb-top"><span data-lb-count></span><button class="lb-close" data-lb-close aria-label="{t('Chiudi galleria')}">×</button></div>
  <div class="lb-stage">
    <button class="lb-nav lb-prev" data-lb-step="-1" aria-label="{t('Foto precedente')}"><svg><use href="#i-left"/></svg></button>
    <img data-lb-img alt="">
    <button class="lb-nav lb-next" data-lb-step="1" aria-label="{t('Foto successiva')}"><svg><use href="#i-right"/></svg></button>
  </div>
  <div class="lb-thumbs" data-lb-thumbs></div>
</dialog>"""


def lang_switch(cls="lang"):
    """Selettore di lingua: porta alla stessa pagina nelle altre lingue."""
    links = []
    for l in LANGS:
        href = P("home", l) if CUR_KEY in ONLY_IT else P(CUR_KEY, l)
        cur = ' aria-current="true"' if l == LANG else ""
        links.append(f'<a href="{href}" hreflang="{l}" lang="{l}" title="{LANG_NAME[l]}"{cur}>{l.upper()}</a>')
    return f'<nav class="{cls}" aria-label="{t("Lingua")}">{"".join(links)}</nav>'


def header(active, solid=False):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{x}</a>' for k, h, x in nav())
    return f"""<a class="skip" href="#main">{t('Vai al contenuto')}</a>
<header class="hdr" data-hdr{" data-solid" if solid else ""}>
  <div class="wrap bar">
    <a href="{P('home')}" class="logo" aria-label="{t('Albergo Diffuso Socchieve Col Gentile, home')}">
      <svg class="logo-mark" aria-hidden="true"><use href="#i-mark"/></svg>
      <span><b>Col Gentile</b><small>Albergo Diffuso Socchieve</small></span>
    </a>
    <nav class="menu" aria-label="{t('Principale')}">{links}</nav>
    <div class="hdr-cta">
      {lang_switch()}
      <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">{t('Prenota')} {I('arrow')}</a>
      <button class="burger" aria-label="{t('Apri menu')}" data-open><span></span></button>
    </div>
  </div>
</header>
<div class="drawer" data-drawer aria-hidden="true">
  <div class="drawer-top"><span class="logo"><svg class="logo-mark" aria-hidden="true"><use href="#i-mark"/></svg><span><b>Col Gentile</b></span></span><button class="close" data-close aria-label="{t('Chiudi menu')}">×</button></div>
  <nav aria-label="{t('Menu mobile')}"><a href="{P('home')}">Home</a>{"".join(f'<a href="{h}">{x}</a>' for k, h, x in nav())}</nav>
  <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">{t('Verifica disponibilità')} {I('arrow')}</a>
  {lang_switch("lang lang-drawer")}
</div>"""


def credits():
    return (f'<span class="credits">{t("Sito realizzato da")} <a href="https://jdevpro.it" target="_blank" rel="noopener">jdevpro.it</a> · '
            'Booking engine powered by <a href="https://welora.it" target="_blank" rel="noopener">Welora</a></span>')


def footer():
    case = "".join(f'<a href="{stay_url(s)}">{e(s["n"])}</a>' for s in top_stays())
    borghi = "".join(f'<a href="{vill_url(v)}">{e(v["n"])}</a>' for v in VILLAGES)
    exps = "".join(f'<a href="{exp_url(k)}">{e(x["n"])}</a>' for k, x in EXPS.items())
    return f"""<footer class="foot" id="contatti">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a href="{P('home')}" class="logo" style="color:var(--bone)"><svg class="logo-mark" aria-hidden="true"><use href="#i-mark"/></svg><span><b>Col Gentile</b><small>Albergo Diffuso Socchieve</small></span></a>
        <p class="big">{t('La porta delle Dolomiti Friulane.')}</p>
        <p>{SITE['street']}, {SITE['locality']}<br>{SITE['zip']} Socchieve (UD) · Friuli Venezia Giulia</p>
        <a href="mailto:{SITE['email']}">{SITE['email']}</a><a href="tel:{SITE['phone_href']}">{SITE['phone']}</a><a href="tel:{SITE['mobile_href']}">{SITE['mobile']}</a>
        <div class="partners">{pic("logoborghi%20autentici%20d%27Italia.jpg", "Borghi Autentici d'Italia", "120px")}</div>
      </div>
      <div><h4>{t('Le case')}</h4>{case}<a href="{P('catalog')}">{t('Tutte le case')} →</a></div>
      <div><h4>{t('I borghi')}</h4>{borghi}</div>
      <div><h4>{t('Esperienze')}</h4>{exps}<a href="{P('benessere')}">{t('Benessere: sauna e bagno di bosco')}</a><a href="{P('territorio')}">{t('Il territorio')}</a><a href="{P('contact')}">{t('Contatti e come arrivare')}</a><a href="{P('farie')}">La Farie</a></div>
    </div>
    <div class="foot-bottom"><span>© {datetime.date.today().year} {SITE['legal']} · {t('P.I.')} {SITE['vat']}</span><span class="foot-links"><a href="{P('booking-terms')}">{t('Condizioni di prenotazione')}</a><a href="{P('privacy')}">Privacy</a><a href="{P('cookies')}">{t('Cookie')}</a>{credits()}</span></div>
  </div>
</footer>"""


def contact_form(brand="col-gentile"):
    """Modulo AJAX: markup comune alle pagine; invio gestito da /contatti.php."""
    if brand == "la-farie":
        eyebrow, h2, intro = "La Farie · Lungis", t("Scrivi a <em>La Farie.</em>"), t("Il messaggio sarà identificato come richiesta per La Farie e non per gli appartamenti Col Gentile.")
    else:
        eyebrow, h2, intro = "Col Gentile · Albergo Diffuso", t("Richiedi informazioni <em>sul soggiorno.</em>"), t("Per informazioni su case, periodi e soggiorni a Socchieve, inviaci un messaggio. Per la disponibilità aggiornata utilizza sempre il motore di prenotazione.")
    return f"""
<section class="sec contact-section" id="scrivici" aria-labelledby="contact-title">
  <div class="wrap contact-grid">
    <div class="contact-intro">
      <span class="eyebrow">{eyebrow}</span>
      <h2 id="contact-title">{h2}</h2>
      <p>{intro}</p>
      <p class="contact-small">{t('I campi contrassegnati con * sono obbligatori. La richiesta non costituisce una prenotazione.')}</p>
    </div>
    <form class="contact-form" data-ajax-contact action="/contatti.php" method="post" accept-charset="UTF-8">
      <input type="hidden" name="brand" value="{brand}">
      <input type="hidden" name="lang" value="{LANG}">
      <div class="contact-honeypot" aria-hidden="true"><label>{t('Lascia vuoto questo campo')}<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="contact-fields">
        <label>{t('Nome e cognome')} *<input type="text" name="nome" autocomplete="name" minlength="2" maxlength="100" required placeholder="{t('Il tuo nome')}"></label>
        <label>Email *<input type="email" name="email" autocomplete="email" maxlength="254" required placeholder="{t('nome@esempio.it')}"></label>
        <label>{t('Telefono (facoltativo)')}<input type="tel" name="telefono" autocomplete="tel" maxlength="40" placeholder="+39 ..."></label>
        <label class="contact-wide">{t('Messaggio')} *<textarea name="messaggio" rows="5" minlength="10" maxlength="5000" required placeholder="{t('Raccontaci la tua richiesta...')}"></textarea></label>
      </div>
      <label class="contact-consent"><input type="checkbox" name="privacy" value="1" required> {tf("Ho letto l'<a href=\"{href}\" target=\"_blank\" rel=\"noopener noreferrer\">informativa sulla privacy</a> e acconsento al trattamento dei dati per rispondere alla mia richiesta.", href=P('privacy'))} *</label>
      <div class="contact-form-actions"><button type="submit" class="btn btn-primary" data-form-submit>{t('Invia il messaggio')}</button><span class="contact-small">{t("Risposta visibile qui dopo l'invio")}</span></div>
      <p class="contact-result" data-form-status role="status" aria-live="polite" aria-atomic="true" tabindex="-1" hidden></p>
    </form>
  </div>
</section>
"""


def mbar_html(href, label, external=False):
    tgt = ' target="_blank" rel="noopener"' if external else ""
    return f'<div class="mbar"><a class="btn btn-primary" href="{href}"{tgt}>{label}</a><a class="mbar-tel" href="tel:{SITE["phone_href"]}" aria-label="{t("Chiama")}">{I("phone")}</a></div>'


def page(key, title, desc, body, *, active="", image=None, ld=(), solid=False, noindex=False, images=(), preload=None, og_type="website", wrapper=None):
    global CUR_KEY
    CUR_KEY = key
    path = P(key)
    canonical = U + path
    og = og_img(image) if image else og_img("Slide1Socchieve.jpg")
    head_ld = "\n".join(jsonld(x) for x in ld)
    pre = f'<link rel="preload" as="image" href="{preload[0]}" imagesrcset="{preload[1]}" imagesizes="100vw" fetchpriority="high">' if preload else ""
    if key in ("home", "contact", "farie"):
        body += contact_form("la-farie" if key == "farie" else "col-gentile")
    content = wrapper(body) if wrapper else f"{header(active, solid)}\n<main id=\"main\">\n{body}\n</main>\n{footer()}"
    if wrapper and key == "farie":
        mbar = mbar_html("#prenota", t("Prenota La Farie")) if FARIE["welora"]["live"] else mbar_html("#scrivici", t("Chiedi disponibilità"))
    elif key in ("svc:sauna", "svc:bagno-di-bosco", "benessere") and data.WELORA["live"]:
        mbar = mbar_html("#prenota", t("Prenota online"))
    elif key in ("404", "farie-results", "svc-results") or wrapper:
        mbar = ""
    else:
        mbar = mbar_html(SITE["booking"], t("Verifica disponibilità"), external=True)
    alternates = ""
    if key not in ONLY_IT and not noindex:
        alternates = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{U + P(key, l)}">' for l in LANGS) + f'\n<link rel="alternate" hreflang="x-default" href="{U + P(key, "it")}">'
    og_alt = "".join(f'<meta property="og:locale:alternate" content="{OG_LOCALE[l]}">' for l in LANGS if l != LANG and key not in ONLY_IT)
    doc = f"""<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
{alternates}
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow,max-image-preview:large'}">
<meta name="theme-color" content="#16241e">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:locale" content="{OG_LOCALE[LANG]}">{og_alt}
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="IT-UD"><meta name="geo.placename" content="Socchieve">
<meta name="geo.position" content="{SITE['geo'][0]};{SITE['geo'][1]}"><meta name="ICBM" content="{SITE['geo'][0]}, {SITE['geo'][1]}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/fraunces-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-tight-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
{pre}
<link rel="stylesheet" href="/assets/site.css?v={CSS_V}">
{head_ld}
</head>
<body>
{ICONS}
{content}
{mbar}
{lightbox()}
<script src="/assets/site.js?v={JS_V}" defer></script>
</body>
</html>
"""
    doc = doc.replace("\n\n<meta name=\"robots\"", "\n<meta name=\"robots\"")
    if path == "/":
        out = ROOT / "index.html"
    elif path.endswith("/"):
        out = ROOT / path.strip("/") / "index.html"
    else:
        out = ROOT / (path.strip("/") + ".html")
    if key == "404":
        doc = doc.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + BASE_404, 1)
    doc = relativize(doc, len(out.relative_to(ROOT).parts) - 1)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8", newline="\n")
    if not noindex:
        PAGES.append((key, LANG, list(images)))


# ---------------------------------------------------------------- blocchi riusabili
def card(s, feature=False):
    badge = '<span class="badge360">360°</span>' if s.get("pano") else ""
    sizes = "(max-width:640px) 84vw, (max-width:1080px) 50vw, 33vw" if not feature else "(max-width:640px) 84vw, 60vw"
    return f"""<a class="card{' feature' if feature else ''}" data-b="{s['b']}" data-s="{size(s['beds'])}" href="{stay_url(s)}">
      <div class="card-img">{pic(s['card'], tf("{n}, {label} a {b}, Carnia", n=s['n'], label=low(s['label']), b=s['b']), sizes)}<span class="tag">{beds(s['beds'])}</span>{badge}</div>
      <div class="card-body">
        <div><h3>{e(s['n'])}</h3><div class="where">{I('pin')}{s['b']} · {s['label']}</div>{f"<p>{e(s['short'])}</p>" if feature else ""}</div>
        <span class="arrow" aria-hidden="true">{I('arrow')}</span>
      </div>
    </a>"""


def filters_block():
    borghi = sorted({s["b"] for s in STAYS}, key=lambda b: [v["n"] for v in VILLAGES].index(b))
    chips = "".join(f'<button class="chip" data-f="borgo" data-v="{b}" aria-pressed="false">{b}</button>' for b in borghi)
    return f"""<div class="filters rv" role="group" aria-label="{t('Filtra le residenze')}">
          <button class="chip" data-f="borgo" data-v="all" aria-pressed="true">{t('Tutti i borghi')}</button>{chips}
          <span class="sep"></span>
          <button class="chip" data-f="size" data-v="all" aria-pressed="true">{t('Ogni capienza')}</button>
          <button class="chip" data-f="size" data-v="s" aria-pressed="false">{t('2–8 posti')}</button>
          <button class="chip" data-f="size" data-v="m" aria-pressed="false">{t('9–16 posti')}</button>
          <button class="chip" data-f="size" data-v="l" aria-pressed="false">{t('Oltre 16')}</button>
          <span class="count" aria-live="polite" data-count></span>
        </div>
        <p class="count-m" data-count-m aria-hidden="true"></p>
        <div class="grid" data-grid>{"".join(card(s, s.get('feature', False)) for s in STAYS)}</div>
        <p class="swipe-hint" aria-hidden="true">{t('Scorri per vedere tutte le case')} {I('right')}</p>
        <div class="empty" data-empty>{t("Nessuna casa con questi filtri. Prova un altro borgo o un'altra capienza.")}</div>"""


def book_strip():
    return f"""<div class="book-strip rv">
          <div><strong>{t('Date, prezzi e disponibilità in tempo reale')}</strong><p>{t('Prenoti direttamente sul sistema ufficiale Col Gentile, senza intermediari.')}</p></div>
          <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">{t('Verifica disponibilità')} {I('arrow')}</a>
        </div>"""


def aside(title, extra=""):
    return f"""<aside class="aside rv">
      <h2 style="font-size:30px;line-height:1.1;margin:0">{e(title)}</h2>
      <p>{t('Date, prezzi e disponibilità in tempo reale sul sistema ufficiale di prenotazione Col Gentile.')}</p>
      <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">{t('Verifica disponibilità')} {I('arrow')}</a>
      <a class="btn btn-ghost" href="mailto:{SITE['email']}?subject={e(t('Richiesta informazioni: ') + title)}">{t('Scrivici')}</a>
      <a class="btn btn-ghost" href="tel:{SITE['phone_href']}">{SITE['phone']}</a>
      {extra}
    </aside>"""


def gallery(names, label, max_shown=7):
    urls = [img_url(n, 1600) for n in names]
    items = []
    for i, n in enumerate(names[:max_shown]):
        more = f'<span class="more">+{len(names) - max_shown + 1}</span>' if i == max_shown - 1 and len(names) > max_shown else ""
        sz = "(max-width:640px) 100vw, 40vw" if i == 0 else "(max-width:640px) 50vw, 20vw"
        items.append(f'<button data-open-lb="{i}" aria-label="{tf("Apri foto {i} di {n}", i=i + 1, n=len(names))}">{pic(n, tf("{label}, foto {i}", label=label, i=i + 1), sz)}{more}</button>')
    return f"""<div class="gal" data-gallery='{json.dumps(urls)}'>{"".join(items)}</div>"""


def tour(s):
    panos = [PANO[p] for p in s.get("pano", []) if p in PANO]
    if not panos: return ""
    thumbs = "".join(f'<button aria-pressed="{str(i == 0).lower()}" aria-label="{tf("Ambiente {i}", i=i + 1)}"><img loading="lazy" src="{p["thumb"]}" alt=""></button>' for i, p in enumerate(panos))
    return f"""<div class="rv" id="tour-360"><span class="eyebrow">{t('Tour virtuale')}</span><h2>{t('Entra in casa, a 360°')}</h2>
      <div class="tour" data-tour='{json.dumps([p["src"] for p in panos])}'>
        <div class="tour-stage"><img src="{panos[0]['thumb']}" alt="{e(tf('Anteprima del tour virtuale di {n}', n=s['n']))}" loading="lazy">
          <button class="tour-start" aria-label="{t('Avvia il tour virtuale a 360 gradi')}"><div><b><i>360°</i> {t('Avvia il tour')}</b><span>{tf('{n} ambienti da esplorare · trascina per guardarti intorno', n=len(panos))}</span></div></button>
        </div>
        {f'<div class="tour-thumbs">{thumbs}</div>' if len(panos) > 1 else ""}
      </div></div>"""


def mini_stay(s):
    return f'<a class="mini" href="{stay_url(s)}">{pic(s["card"], s["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{e(s["n"])}</b><span>{s["b"]} · {beds(s["beds"])}</span></div></a>'


def mini_vill(v):
    return f'<a class="mini" href="{vill_url(v)}">{pic(v["card"], tf("Il borgo di {n}", n=v["n"]), "(max-width:640px) 70vw, 25vw")}<div><b>{e(v["n"])}</b><span>{v["f"]["q"] + " " + t("m s.l.m.") if v["f"] else t("Frazione di Socchieve")}</span></div></a>'


def hero(img, alt, crumbs, h1, sub="", pills=()):
    nv = "".join(f'<a href="{p}">{e(n)}</a><span>/</span>' for n, p in crumbs[:-1]) + f"<b>{e(crumbs[-1][0])}</b>"
    pl = "".join(f'<span class="pill">{x}</span>' for x in pills)
    return f"""<section class="ph">
  {pic(img, alt, "100vw", eager=True)}
  <div class="wrap">
    <nav class="crumbs" aria-label="{t('Percorso')}">{nv}</nav>
    <h1>{h1}</h1>
    {f'<p class="lead">{sub}</p>' if sub else ""}
    {f'<div class="ph-meta">{pl}</div>' if pl else ""}
  </div>
</section>"""


def preload_for(name):
    m = PH.get(name)
    if not m: return None
    return (img_url(name, 960), ", ".join(f"/img/{m['slug']}-{x}.webp {x}w" for x in m["widths"]))


def home_crumb(): return ("Home", P("home"))


# ---------------------------------------------------------------- pagine
def build_stay(s):
    v = VILL_BY_NAME[s["b"]]
    parent = STAY.get(s.get("parent"))
    siblings = [STAY[u] for u in parent["units"] if u != s["id"]] if parent else []
    related = (siblings or [x for x in STAYS if x["id"] != s["id"] and x["b"] == s["b"]])
    related = (related + [x for x in top_stays() if x["id"] != s["id"] and x not in related])[:4]
    cins = [s["cin"]] if s.get("cin") else [STAY[u]["cin"] for u in s.get("units", []) if STAY[u].get("cin")]
    crumbs = [home_crumb(), (t("Le case"), P("catalog"))] + ([(parent["n"], stay_url(parent))] if parent else []) + [(s["n"], stay_url(s))]
    pills = [f"{I('pin')}{s['b']}, Socchieve", beds(s["beds"])] + ([stars(s['stars'])] if s.get("stars") else []) + ([t("Tour 360°")] if s.get("pano") else [])
    units = ""
    if s.get("units"):
        units = f'<div class="rv"><span class="eyebrow">{t("Gli appartamenti")}</span><h2>{t("Prenota tutta la casa o un solo appartamento")}</h2><div class="units">' + "".join(
            f'<a class="unit" href="{stay_url(STAY[u])}">{pic(STAY[u]["g"][0], STAY[u]["n"], "96px")}<div><b>{e(STAY[u]["n"])}</b><span>{beds(STAY[u]["beds"])}{" · " + stars(STAY[u]["stars"]) if STAY[u].get("stars") else ""}</span></div></a>'
            for u in s["units"]) + "</div></div>"
    plan = ""
    if s.get("plan"):
        plan = f"""<div class="rv"><span class="eyebrow">{t('Planimetria')}</span><div class="plan" style="margin-top:20px" data-gallery='{json.dumps([img_url(s["plan"])])}'>{pic(s["plan"], tf("Planimetria di {n}", n=s["n"]), "(max-width:980px) 100vw, 60vw", attrs='data-open-lb="0"')}</div></div>"""
    am = f'<div class="rv"><span class="eyebrow">{t("Servizi")}</span><ul class="amen" style="margin-top:20px">{"".join(f"<li>{a}</li>" for a in s["am"])}</ul></div>' if s.get("am") else ""
    bedrooms = s.get("bedrooms")
    if s.get("units"): rooms_v, rooms_l = len(s["units"]), t("Appartamenti")
    elif bedrooms == 0: rooms_v, rooms_l = 1, t("Ambiente unico")
    elif bedrooms: rooms_v, rooms_l = bedrooms, t("Camere") if bedrooms > 1 else t("Camera")
    else: rooms_v, rooms_l = "—", t("Camere")
    body = f"""{hero(s['g'][0], tf("{n} a {b}, Carnia", n=s['n'], b=s['b']), crumbs, e(s['n']), pills=pills)}
<section class="d-body">
  <div class="wrap d-grid">
    <div class="d-main">
      <div class="rv">
        <span class="eyebrow">{tf('{label} a {b} · Carnia', label=s['label'], b=s['b'])}</span>
        <h2>{e(s['short'])}</h2>
        {"".join(f'<p{" class=\"prose-first\"" if i == 0 else ""}>{e(p)}</p>' for i, p in enumerate(s['text']))}
      </div>
      <div class="facts rv">
        <div><b>{s['beds']}</b><span>{t('Posti letto')}</span></div>
        <div><b>{f"{s['stars']}★" if s.get('stars') else s['label']}</b><span>{t("Classificazione") if s.get('stars') else t("Tipologia")}</span></div>
        <div><b>{rooms_v}</b><span>{rooms_l}</span></div>
        <div><b>{v['f']['q'] if v['f'] else '—'}</b><span>{t('m s.l.m.')}</span></div>
      </div>
      {am}
      <div class="rv"><span class="eyebrow">{t('Foto')}</span><h2>{tf('{c} foto di {n}', c=len(s['g']), n=e(s['n']))}</h2>{gallery(s['g'], s['n'])}</div>
      {tour(s)}
      {units}
      {plan}
      <div class="rv">
        <span class="eyebrow">{t('Il borgo')}</span>
        <h2>{tf('{b}, frazione di Socchieve', b=s['b'])}</h2>
        <p>{e(clip(v['t'], 300))}</p>
        <p style="margin-top:20px"><a class="link" href="{vill_url(v)}">{tf('Scopri {b}: sentieri, locali e cosa fare', b=s['b'])} {I('arrow')}</a></p>
      </div>
      {f'<p class="cin rv">{t("Codice identificativo nazionale (CIN)")}: {" · ".join(cins)}</p>' if cins else ""}
    </div>
    {aside(s['n'], f"<dl><dt>{t('Indirizzo')}</dt><dd>{e(s['addr'])}</dd><dt>{t('Comune')}</dt><dd>Socchieve (UD)</dd><dt>{t('Ospiti')}</dt><dd>{tf('fino a {n}', n=s['beds'])}</dd><dt>{t('Categoria')}</dt><dd>{s['label']}{' ' + str(s['stars']) + '★' if s.get('stars') else ''}</dd></dl>")}
  </div>
</section>
<section class="related"><div class="wrap"><span class="eyebrow">{t("Nella stessa casa") if siblings else t("Potrebbero piacerti")}</span><h2>{t("Altre case dell'albergo diffuso")}</h2><div class="mini-rail">{"".join(mini_stay(x) for x in related)}</div></div></section>"""

    ld_stay = {
        "@context": "https://schema.org", "@type": s["kind"], "@id": U + stay_url(s) + "#accommodation",
        "name": s["n"], "description": " ".join(s["text"])[:600], "url": U + stay_url(s),
        "image": [abs_img(g) for g in s["g"][:8]],
        "address": address(s["addr"].split(",")[0], f"{s['b']}, Socchieve"),
        "geo": {"@type": "GeoCoordinates", "latitude": v["geo"][0], "longitude": v["geo"][1]},
        "occupancy": {"@type": "QuantitativeValue", "maxValue": s["beds"], "unitCode": "C62"},
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in s.get("am", [])],
        "containedInPlace": {"@id": LODGING_ID},
    }
    if bedrooms is not None: ld_stay["numberOfBedrooms"] = bedrooms
    if s.get("pets"): ld_stay["petsAllowed"] = True
    if s.get("cin"): ld_stay["identifier"] = {"@type": "PropertyValue", "propertyID": "CIN", "value": s["cin"]}
    if s.get("units"): ld_stay["containsPlace"] = [{"@id": U + stay_url(STAY[u]) + "#accommodation"} for u in s["units"]]
    title = tf("{n} a {b} · {label} fino a {beds} ospiti in Carnia", n=s['n'], b=s['b'], label=s['label'], beds=s['beds'])
    star_txt = tf("{n} stelle, ", n=s['stars']) if s.get('stars') else ''
    tour_txt = t(", tour virtuale 360°") if s.get('pano') else ''
    desc = clip(tf("{short} {stars}{b} (Socchieve, Carnia). {c} foto{tour} e prenotazione diretta.", short=s['short'], stars=star_txt, b=s['b'], c=len(s['g']), tour=tour_txt), 160)
    page("stay:" + s["id"], title, desc, body, active="alloggi", image=s["g"][0], og_type="place", preload=preload_for(s["g"][0]),
         ld=[ld_stay, crumbs_ld(crumbs)], images=[abs_img(g) for g in s["g"]])


def build_village(v):
    here = stays_in(v["n"])
    near = stays_in(v["near"]) if v.get("near") else []
    crumbs = [home_crumb(), (t("Il territorio"), P("territorio")), (v["n"], vill_url(v))]
    trek = {r["n"].split(" ·")[0]: r for r in EXPS["trekking"]["routes"]}
    def sent(n):
        return f'<a href="{exp_url("trekking")}">{e(n)}{I("arrow")}</a>' if n.split(" ·")[0] in trek else e(n)
    lists = "".join(f'<div><h3 style="font:600 12px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--moss);margin-bottom:14px">{h}</h3><ul>{"".join(f"<li>{f(i)}</li>" for i in items)}</ul></div>'
                    for h, items, f in ((t("Sentieri dal paese"), v["sentieri"], sent), (t("Dove mangiare e bere"), v["locali"], e), (t("Servizi in paese"), v.get("servizi", []), e)) if items)
    stays_block = ""
    if here or near:
        lst = here or near
        stays_block = f'<div class="rv"><span class="eyebrow">{tf("Dove dormire a {n}", n=v["n"]) if here else tf("Le case più vicine, a {n}", n=v["near"])}</span><h2>{t("Le case dell'albergo diffuso")}</h2><div class="units">' + "".join(
            f'<a class="unit" href="{stay_url(x)}">{pic(x["card"], x["n"], "96px")}<div><b>{e(x["n"])}</b><span>{beds(x["beds"])} · {x["label"]}</span></div></a>' for x in lst) + "</div></div>"
    facts = ""
    if v["f"]:
        f = v["f"]
        lo_style = "" if any(c.isdigit() for c in f["lo"]) else ' style="font-size:22px;line-height:1.4"'
        facts = f'<div class="facts rv"><div><b>{f["ab"]}</b><span>{t("Abitanti")}</span></div><div><b>{f["q"]}</b><span>{t("m s.l.m.")}</span></div><div><b>{f["se"]}</b><span>{t("Sentieri")}</span></div><div><b{lo_style}>{f["lo"]}</b><span>{t("Locali")}</span></div></div>'
    pills = [f"{v['f']['q']} {t('m s.l.m.')}", tf("{n} abitanti", n=v['f']['ab'])] if v["f"] else [t("Frazione di Socchieve")]
    body = f"""{hero(v['hero'][0], tf("Panorama di {n}, Socchieve, Carnia", n=v['n']), crumbs, e(v['n']), sub=(t("Capoluogo del comune, in Carnia") if v["id"] == "socchieve" else t("Frazione di Socchieve, in Carnia")), pills=pills)}
<section class="d-body">
  <div class="wrap d-grid">
    <div class="d-main">
      <div class="rv"><span class="eyebrow">{t('Il borgo')}</span><h2>{tf('Cosa vedere e cosa fare a {n}', n=v['n'])}</h2><p class="prose-first">{e(v['t'])}</p></div>
      {facts}
      {f'<div class="rv"><span class="eyebrow">{t("Panorami")}</span><h2>{tf("{n} in foto", n=v["n"])}</h2>{gallery(v["hero"], v["n"])}</div>' if len(v['hero']) > 1 else ""}
      <div class="list2 rv">{lists}</div>
      {stays_block}
    </div>
    {aside(tf("Dormire a {n}", n=v['n']) if here else t("Soggiorna a Socchieve"))}
  </div>
</section>
<section class="related"><div class="wrap"><span class="eyebrow">{t('Socchieve e i suoi paesi')}</span><h2>{t('Gli altri borghi')}</h2><div class="mini-rail">{"".join(mini_vill(x) for x in VILLAGES if x['id'] != v['id'])}</div></div></section>"""
    ld = {"@context": "https://schema.org", "@type": "TouristDestination", "@id": U + vill_url(v) + "#place", "name": f"{v['n']} (Socchieve)",
          "description": v["t"], "url": U + vill_url(v), "image": [abs_img(h) for h in v["hero"] if h in PH],
          "geo": {"@type": "GeoCoordinates", "latitude": v["geo"][0], "longitude": v["geo"][1]},
          "containedInPlace": {"@type": "AdministrativeArea", "name": "Socchieve, Carnia, Friuli Venezia Giulia"}}
    if here: ld["containsPlace"] = [{"@id": U + stay_url(x) + "#accommodation"} for x in here]
    title = tf("{n}, Socchieve: cosa vedere, sentieri e dove dormire", n=v['n'])
    alt_txt = tf(", a {q} m", q=v['f']['q']) if v['f'] else ''
    desc = clip(tf("{n}, frazione di Socchieve in Carnia{alt}: {t}", n=v['n'], alt=alt_txt, t=v['t']), 160)
    page("vill:" + v["id"], title, desc, body, active="borghi", image=v["hero"][0], preload=preload_for(v["hero"][0]),
         ld=[ld, crumbs_ld(crumbs)], images=[abs_img(h) for h in v["hero"] if h in PH])


def build_exp(k, x):
    crumbs = [home_crumb(), (t("Il territorio"), P("territorio")), (x["n"], exp_url(k))]
    routes = ""
    if x.get("routes"):
        routes = f'<div class="rv"><span class="eyebrow">{t("Gli itinerari")}</span><div style="margin-top:20px">' + "".join(f"""
        <article class="route" id="{k}-{i + 1}"><span class="n">{i + 1:02d}</span><div>
          <h3>{e(r['n'])}</h3><p>{e(r['t'])}</p>
          {f'<div class="stats-inline">{"".join(f"<span>{s}</span>" for s in r["stats"])}</div>' if r.get('stats') else ""}
          <p style="margin-top:14px;font-size:14px">{t('Borghi')}: {", ".join(f'<a class="link" style="border:0;padding:0" href="{vill_url(VILL[b])}">{VILL[b]["n"]}</a>' for b in r.get('via', []))}</p>
          {f'<figure data-gallery=\'{json.dumps([img_url(r["map"])])}\'>{pic(r["map"], tf("Mappa del percorso {n}", n=r["n"]), "(max-width:980px) 100vw, 60vw", attrs="data-open-lb=\"0\"")}</figure>' if r.get('map') else ""}
        </div></article>""" for i, r in enumerate(x["routes"])) + "</div></div>"
    items = ""
    if x.get("items"):
        items = "<div>" + "".join(f"""
        <article class="feature-row rv" data-gallery='{json.dumps([img_url(it["img"])])}'>{pic(it['img'], it['n'], "(max-width:640px) 100vw, 40vw", attrs='data-open-lb="0"')}<div><span class="eyebrow">{x['n']}</span><h3>{e(it['n'])}</h3>{"".join(f"<p>{e(p)}</p>" for p in it['t'])}</div></article>""" for it in x["items"]) + "</div>"
    more = ""
    if x.get("more"):
        more = f'<div class="rv"><span class="eyebrow">{t("Altri itinerari in zona")}</span><div class="list2" style="margin-top:20px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr))">' + "".join(
            f'<div><h3 style="font:600 12px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--moss);margin-bottom:14px">{h}</h3><ul>{"".join(f"<li>{i}</li>" for i in l)}</ul></div>' for h, l in x["more"]) + "</div></div>"
    others = [(kk, xx) for kk, xx in EXPS.items() if kk != k]
    body = f"""{hero(x['hero'], tf("{n} a Socchieve, Carnia", n=x['n']), crumbs, e(x['n']), sub=e(x['lead']))}
<section class="d-body">
  <div class="wrap d-grid">
    <div class="d-main">
      <div class="rv">{"".join(f'<p{" class=\"prose-first\"" if i == 0 else ""}>{e(p)}</p>' for i, p in enumerate(x['intro']))}</div>
      {routes}{items}{more}
      {f'<p class="cin rv">{e(x["note"])}</p>' if x.get('note') else ""}
    </div>
    {aside(t("Parti da Socchieve"))}
  </div>
</section>
<section class="related"><div class="wrap"><span class="eyebrow">{t('Cosa fare a Socchieve')}</span><h2>{t('Altre esperienze')}</h2><div class="mini-rail">{"".join(f'<a class="mini" href="{exp_url(kk)}">{pic(xx["hero"], xx["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{xx["n"]}</b><span>{e(xx["lead"].split(":")[0].split(",")[0])}</span></div></a>' for kk, xx in others)}<a class="mini" href="{P('benessere')}">{pic("PanoramaNonta1.jpg", t("Benessere a Socchieve"), "(max-width:640px) 70vw, 25vw")}<div><b>{t('Benessere')}</b><span>{t('Sauna e bagno di bosco')}</span></div></a></div></div></section>"""
    if x.get("routes"):
        ld = {"@context": "https://schema.org", "@type": "TouristTrip", "name": tf("{n} a Socchieve", n=x['n']), "description": x["desc"], "url": U + exp_url(k),
              "touristType": [t("Escursionisti") if k == "trekking" else t("Ciclisti")],
              "itinerary": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "TouristAttraction", "name": r["n"], "description": r["t"], "url": f"{U}{exp_url(k)}#{k}-{i + 1}"}} for i, r in enumerate(x["routes"])]},
              "provider": {"@id": LODGING_ID}}
    else:
        ld = {"@context": "https://schema.org", "@type": "ItemList", "name": x["n"], "url": U + exp_url(k), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "TouristAttraction", "name": it["n"], "description": " ".join(it["t"]), "image": abs_img(it["img"])}} for i, it in enumerate(x["items"])]}
    imgs = [abs_img(x["hero"])] + [abs_img(r["map"]) for r in x.get("routes", []) if r.get("map") in PH] + [abs_img(i["img"]) for i in x.get("items", []) if i["img"] in PH]
    page("exp:" + k, x["title"], x["desc"], body, active="esperienze", image=x["hero"], preload=preload_for(x["hero"]), ld=[ld, crumbs_ld(crumbs)], images=imgs)


def lodging_ld():
    return {"@context": "https://schema.org", "@type": "LodgingBusiness", "@id": LODGING_ID,
            "name": "Albergo Diffuso Socchieve “Col Gentile”", "alternateName": ["Albergo Diffuso Socchieve", "Col Gentile"],
            "description": t("Albergo diffuso con case e appartamenti vacanza nei borghi di Socchieve, in Carnia (Friuli Venezia Giulia), alla porta delle Dolomiti Friulane."),
            "url": U + P("home"), "logo": U + "/apple-touch-icon.png", "image": [og_img("Slide1Socchieve.jpg"), abs_img("Casa-Vanda-esterno.jpg")],
            "telephone": SITE["phone"], "email": SITE["email"], "vatID": "IT" + SITE["vat"],
            "address": address(SITE["street"], SITE["locality"]),
            "geo": {"@type": "GeoCoordinates", "latitude": SITE["geo"][0], "longitude": SITE["geo"][1]},
            "hasMap": f"https://www.google.com/maps/search/?api=1&query={SITE['geo'][0]},{SITE['geo'][1]}",
            "areaServed": "Carnia", "knowsLanguage": ["it", "en", "fr"], "petsAllowed": True,
            "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": t(n), "value": True} for n in ("Wi-Fi", "Parcheggio", "Giardino", "Animali ammessi")],
            "containsPlace": [{"@id": U + stay_url(s) + "#accommodation"} for s in STAYS],
            "potentialAction": {"@type": "ReserveAction", "target": SITE["booking"]},
            "memberOf": {"@type": "Organization", "name": "Borghi Autentici d'Italia"}}


def build_home():
    villages = "".join(f"""<a class="village" href="{vill_url(v)}">{pic(v['card'], tf('Il borgo di {n}', n=v['n']), '(max-width:640px) 72vw, 340px')}<small>{v['f']['q'] + ' ' + t('m s.l.m.') if v['f'] else 'Socchieve'}</small><strong>{v['n']}{I('arrow')}</strong></a>""" for v in VILLAGES)
    marquee = "".join(f"<span>{v['n']}</span>" for v in VILLAGES) * 2
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    n_stays = len(STAYS)
    body = f"""<section class="hero">
      <div class="hero-media">{pic("Slide1Socchieve.jpg", t("Strada tra i prati verso le montagne della Carnia, a Socchieve"), "100vw", eager=True)}</div>
      <div class="wrap hero-in">
        <h1><span class="eyebrow light" style="display:flex;margin-bottom:22px">{t('Albergo diffuso a Socchieve · Carnia')}</span>{t('Vivi la Carnia <em>da paesano.</em>')}</h1>
        <div class="hero-row">
          <p>{t("Case e appartamenti vacanza nei borghi di Socchieve, con i servizi di un albergo. A 18 km da Sauris e mezz'ora dalle Dolomiti Friulane.")}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="{P('catalog')}">{t('Scopri le case')} {I('arrow')}</a>
            <a class="btn btn-ghost" href="{P('benessere')}">{t('Sauna e bagno di bosco')}</a>
          </div>
        </div>
        <div class="hero-meta"><span><b>{n_stays}</b> {t('alloggi')}</span><span><b>8</b> {t('borghi')}</span><span>{t('Dolomiti Friulane · <b>Patrimonio UNESCO</b>')}</span></div>
      </div>
      <span class="scroll-cue" aria-hidden="true">{t('Scorri')}</span>
    </section>
    <div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

    <section class="sec" id="albergo-diffuso">
      <div class="wrap intro-grid">
        <div>
          <span class="eyebrow rv">{t("Cos'è un albergo diffuso")}</span>
          <h2 class="statement rv d1">{t('Non un hotel con tante stanze. <em>Un paese intero</em> che ti apre le sue case.')}</h2>
          <p class="intro-copy rv d2">{t("L'albergo diffuso offre i servizi di una struttura alberghiera dentro un territorio abitato. A Socchieve dormi in una casa vera del borgo, prendi il caffè con chi ci vive ed esci a piedi sui sentieri della Carnia. Turista e paesano, nello stesso viaggio.")}</p>
          <div class="stats rv d3"><div><b>{n_stays}</b><span>{t('case e appartamenti')}</span></div><div><b>8</b><span>{t('borghi del comune')}</span></div><div><b>2–21</b><span>{t('posti letto per casa')}</span></div></div>
        </div>
        <div class="intro-media rv d2">
          {pic("Slide2Socchieve.jpg", t("Albero e panchina in un prato di montagna a Socchieve"), "(max-width:820px) 80vw, 40vw", cls="a")}
          {pic("Casa-Vanda-esterno.jpg", t("Casa Vanda a Viaso, villa settecentesca con ballatoi in legno"), "(max-width:820px) 40vw, 20vw", cls="b")}
          <div class="badge" aria-hidden="true"><svg viewBox="0 0 100 100"><defs><path id="circ" d="M50 50m-38 0a38 38 0 1 1 76 0a38 38 0 1 1-76 0"/></defs><text font-size="8.6" fill="#fff" font-family="Inter Tight, sans-serif" font-weight="600"><textPath href="#circ" textLength="236" lengthAdjust="spacing">{t('OSPITI DELLA NATURA · OSPITI DELLA NATURA · ')}</textPath></text></svg><i>Carnia</i></div>
        </div>
      </div>
    </section>

    <section class="sec stays" id="alloggi">
      <div class="wrap">
        <div class="sec-head">
          <div><span class="eyebrow rv">{t('Dove dormire in Carnia')}</span><h2 class="rv d1">{t('Scegli la tua <em>casa nel borgo.</em>')}</h2></div>
          <p class="rv d2">{t('Dal monolocale per due alla villa per gruppi fino a 21 persone. Filtra per borgo o per numero di posti letto.')}</p>
        </div>
        {filters_block()}
        {book_strip()}
      </div>
    </section>

    <section class="sec villages on-dark" id="borghi">
      <div class="wrap sec-head">
        <div><span class="eyebrow rv">{t('Socchieve e i suoi paesi')}</span><h2 class="rv d1">{t("Otto borghi, <em>un'unica valle.</em>")}</h2></div>
        <div class="rail-ctrl"><button data-rail="-1" aria-label="{t('Borghi precedenti')}"><svg><use href="#i-left"/></svg></button><button data-rail="1" aria-label="{t('Borghi successivi')}"><svg><use href="#i-right"/></svg></button></div>
      </div>
      <div class="rail" data-railbox>{villages}</div>
    </section>

    <section class="sec" id="esperienze">
      <div class="wrap">
        <div class="sec-head">
          <div><span class="eyebrow rv">{t('Cosa fare a Socchieve')}</span><h2 class="rv d1">{t('Prenditi <em>il tempo.</em>')}</h2></div>
          <p class="rv d2">{t('Passeggiate ed escursioni, bici, arte romanica e i grandi classici della Carnia. Si parte direttamente dalle nostre case.')}</p>
        </div>
        <div class="bento">
          <a class="tile big rv" href="{exp_url('trekking')}">{pic("Slide1Socchieve.jpg", t("Sentiero tra prati e boschi in Carnia"), "(max-width:640px) 100vw, 50vw")}<span class="num">01</span><h3>{EXPS['trekking']['n']}</h3><p>{t('Quattro anelli che partono dai borghi e la traversata del Col Gentile sul sentiero CAI 235.')}</p><span class="link">{t('Scopri i percorsi')} {I('arrow')}</span></a>
          <a class="tile green rv d1" href="{exp_url('cicloturismo')}"><span class="num">02</span><h3>{EXPS['cicloturismo']['n']}</h3><p>{t("La pista MTB di Mediis e l'anello del Passo Rest, con lo Zoncolan a 24 km.")}</p><span class="link">{t('Approfondisci')} {I('arrow')}</span></a>
          <a class="tile rv d2" href="{exp_url('arte-e-cultura')}">{pic("Slide3Socchieve.jpg", t("Antica meridiana dipinta su un muro in pietra a Socchieve"), "(max-width:640px) 100vw, 25vw")}<span class="num">03</span><h3>{EXPS['arte-e-cultura']['n']}</h3><span class="link">{t('Approfondisci')} {I('arrow')}</span></a>
          <a class="tile wide plain rv d1" href="{exp_url('visita-la-carnia')}"><span class="num">04</span><h3>{EXPS['visita-la-carnia']['n']}</h3><p>{t("Sauris e il suo prosciutto, la Forra del Lumiei, Forni di Sopra e la Val Pesarina: tutto a meno di un'ora.")}</p><span class="link">{t('Approfondisci')} {I('arrow')}</span></a>
        </div>
      </div>
    </section>

    <section class="sec" id="benessere" style="background:var(--bone)">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow rv">{t('Benessere in Carnia')}</span><h2 class="rv d1">{t('Sauna e <em>bagno di bosco</em> a Socchieve.')}</h2></div>
        <p class="rv d2">{t("Dopo una giornata sui sentieri o in bici, la sauna scioglie i muscoli; nei boschi intorno ai borghi lo Shinrin-yoku con Petra ti insegna a rallentare. Si prenotano online con conferma immediata: serve una carta di credito a garanzia.")}</p></div>
        <div class="bento">{"".join(svc_card(s) for s in SERVICES)}</div>
        <div class="svc-seo rv">
          <div><h3>{t('Sauna in Carnia')}</h3><p>{tf("Sauna a ore per tutto il gruppo, {p} € l'ora a prezzo unico, da un'ora in su: il modo migliore per chiudere un'escursione, un'uscita in mountain bike o una giornata sulle piste di Forni di Sopra.", p=SERVICES[1]["price"])} <a class="link" href="{svc_url(SERVICES[1])}">{t('Prezzi e orari')} {I("arrow")}</a></p></div>
          <div><h3>{t('Bagno di bosco (Shinrin-yoku)')}</h3><p>{tf("Forest bathing guidato da Petra nei boschi di Socchieve: circa due ore di immersione lenta e sensoriale nella natura, gruppi fino a 6 persone, {p} € a persona, ritrovo alla reception di Mediis.", p=SERVICES[0]["price"])} <a class="link" href="{svc_url(SERVICES[0])}">{t('Come funziona')} {I("arrow")}</a></p></div>
        </div>
        {welora("search", None, t("Prenota il tuo momento di benessere"))}
      </div>
    </section>

    <section class="sec loc" id="dove">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow rv">{t("Dov'è Socchieve")}</span><h2 class="rv d1">{t('Al centro della Carnia, <em>vicino a tutto.</em>')}</h2></div>
        <p class="rv d2">{t('Tra le Dolomiti Friulane e le Pesarine, lungo la SS52 che unisce Tolmezzo a Forni di Sopra. Distanze in auto dalla reception di Mediis.')}</p></div>
        <ul class="dist rv">{dist_items()}</ul>
        <p style="margin-top:28px" class="rv"><a class="link" href="{P('contact')}">{t('Come arrivare e contatti')} {I('arrow')}</a></p>
      </div>
    </section>

    <section class="farie-teaser">
      {pic("LungisCartolina.jpg", tf("Il borgo di {n}", n="Lungis"), "100vw")}
      <div class="wrap">
        <span class="eyebrow light rv">{t("Bed &amp; Breakfast a Lungis · gestito dall'Albergo Diffuso")}</span>
        <h2 class="rv d1">La Farie.</h2>
        <p class="rv d2">{t("Un bed &amp; breakfast in una casa carnica ristrutturata nel borgo di Lungis, ora gestito direttamente dall'Albergo Diffuso Socchieve.")}</p>
        <a class="btn btn-light rv d3" href="{P('farie')}">{t('Scopri La Farie')} {I('arrow')}</a>
      </div>
    </section>

    <section class="sec" id="domande">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow rv">{t('Domande frequenti')}</span><h2 class="rv d1">{t('Prima di <em>partire.</em>')}</h2></div></div>
        <div class="faq rv">{faq}</div>
      </div>
    </section>

    <section class="cta">
      <div class="wrap">
        <span class="eyebrow rv">{t('Una vacanza diversa')}</span>
        <h2 class="rv d1">{t('La montagna, <em>tra le persone.</em>')}</h2>
        <p class="rv d2">{t('Lasciati affascinare dal vivere in montagna tra la gente e la natura della Carnia.')}</p>
        <div class="row rv d3">
          <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">{t('Prenota il soggiorno')} {I('arrow')}</a>
          <a class="btn btn-dark" href="#scrivici">{t('Scrivici')}</a>
        </div>
      </div>
    </section>"""
    website = {"@context": "https://schema.org", "@type": "WebSite", "@id": U + "/#website", "name": SITE["name"], "url": U + P("home"), "inLanguage": {"it": "it-IT", "en": "en", "de": "de"}[LANG], "publisher": {"@id": LODGING_ID}}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    page("home", t("Albergo Diffuso Socchieve · Case vacanza in Carnia e Dolomiti"),
         tf("Case e appartamenti vacanza nei borghi di Socchieve, in Carnia: {n} alloggi da 2 a 21 posti, a 18 km da Sauris e 30 minuti dalle Dolomiti Friulane. Prenotazione diretta.", n=n_stays),
         body, image="Slide1Socchieve.jpg", preload=preload_for("Slide1Socchieve.jpg"), ld=[lodging_ld(), website, faq_ld] + [service_ld(x) for x in SERVICES],
         images=[og_img("Slide1Socchieve.jpg")] + [abs_img(s["card"]) for s in STAYS])


def build_catalog():
    crumbs = [home_crumb(), (t("Le case"), P("catalog"))]
    body = f"""{hero("Casa-Vanda-esterno.jpg", t("Case vacanza dell'albergo diffuso di Socchieve"), crumbs, t("Case vacanza <em>in Carnia</em>"), sub=tf("{n} case e appartamenti nei borghi di Socchieve, dal monolocale per due alla villa per gruppi. Prenotazione diretta, senza intermediari.", n=len(STAYS)))}
<section class="sec stays">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow rv">{t('Tutti gli alloggi')}</span><h2 class="rv d1">{t('Trova la casa <em>giusta per te.</em>')}</h2></div>
    <p class="rv d2">{t('Appartamenti per coppie e famiglie, case intere per gruppi: tutte arredate, con cucina, e a pochi passi dai sentieri.')}</p></div>
    {filters_block()}
    {book_strip()}
  </div>
</section>"""
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": t("Case vacanza dell'Albergo Diffuso Socchieve"), "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": U + stay_url(s), "name": s["n"]} for i, s in enumerate(STAYS)]}
    page("catalog", tf("Case vacanza e appartamenti in Carnia · {n} alloggi a Socchieve", n=len(STAYS)),
         tf("{n} case vacanza e appartamenti nei borghi di Socchieve, in Carnia: da 2 a 21 posti letto, 3 e 4 stelle, alcuni con tour 360° e animali ammessi. Prenota direttamente.", n=len(STAYS)),
         body, active="alloggi", image="Casa-Vanda-esterno.jpg", preload=preload_for("Casa-Vanda-esterno.jpg"), ld=[items, crumbs_ld(crumbs)],
         images=[abs_img(s["card"]) for s in STAYS])


def build_territorio():
    crumbs = [home_crumb(), (t("Il territorio"), P("territorio"))]
    vgrid = "".join(mini_vill(v) for v in VILLAGES)
    egrid = "".join(f'<a class="mini" href="{exp_url(k)}">{pic(x["hero"], x["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{x["n"]}</b><span>{e(clip(x["lead"], 70))}</span></div></a>' for k, x in EXPS.items())
    body = f"""{hero("Panoramica-feltrone-montagne.jpg", t("Montagne della Carnia sopra Feltrone"), crumbs, t("Socchieve <em>e la Carnia</em>"), sub=t("Otto borghi tra le Dolomiti Friulane e le Pesarine, sentieri fuori dalla porta e i grandi classici della Carnia a meno di un'ora."))}
<section class="sec" id="borghi"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">{t('Socchieve e i suoi paesi')}</span><h2 class="rv d1">{t("Otto borghi, <em>un'unica valle.</em>")}</h2></div><p class="rv d2">{t('Ogni frazione ha il suo carattere, i suoi sentieri e le sue osterie. Scopri dove dormire e cosa fare in ciascuna.')}</p></div>
  <div class="mini-rail" style="grid-template-columns:repeat(4,1fr)">{vgrid}</div>
</div></section>
<section class="sec" id="esperienze" style="background:var(--bone)"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">{t('Cosa fare a Socchieve')}</span><h2 class="rv d1">{t('Prenditi <em>il tempo.</em>')}</h2></div></div>
  <div class="mini-rail">{egrid}</div>
</div></section>
<section class="sec" id="distanze"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">{t('Distanze')}</span><h2 class="rv d1">{t('Il campo base <em>per la Carnia.</em>')}</h2></div></div>
  <ul class="dist rv">{dist_items()}</ul>
</div></section>"""
    page("territorio", t("Socchieve e i suoi borghi: cosa fare in Carnia"),
         t("Gli otto borghi di Socchieve, i sentieri, la mountain bike, l'arte romanica e le mete della Carnia vicine: Sauris, Forni di Sopra, Ampezzo e la Val Pesarina."),
         body, active="borghi", image="Panoramica-feltrone-montagne.jpg", preload=preload_for("Panoramica-feltrone-montagne.jpg"), ld=[crumbs_ld(crumbs)])


def build_contact():
    crumbs = [home_crumb(), (t("Contatti"), P("contact"))]
    lat, lon = SITE["geo"]
    body = f"""{hero("Mediispanoramica.jpg", t("Panorama di Mediis, sede della reception"), crumbs, t("Contatti <em>e come arrivare</em>"), sub=t("La reception è a Mediis, in Via Roma 20. Scrivici o chiamaci per qualsiasi informazione sul soggiorno."))}
<section class="d-body"><div class="wrap">
  <div class="contact-cards rv">
    <a href="tel:{SITE['phone_href']}"><span>{t('Telefono')}</span><b>{SITE['phone']}</b></a>
    <a href="tel:{SITE['mobile_href']}"><span>{t('Cellulare')}</span><b>{SITE['mobile']}</b></a>
    <a href="mailto:{SITE['email']}"><span>Email</span><b>{SITE['email']}</b></a>
  </div>
  <div class="loc-grid" style="margin-top:clamp(48px,6vw,80px)">
    <div>
      <span class="eyebrow rv">{t('Come arrivare')}</span>
      <h2 class="rv d1" style="font-size:clamp(34px,4vw,56px);line-height:1;margin:18px 0 22px">{t('Tra le Dolomiti Friulane <em>e le Pesarine.</em>')}</h2>
      <p class="rv">{t("Socchieve è nell'Alto Friuli, in Carnia, lungo la valle che unisce Villa Santina a Forni di Sotto.")}</p>
      <div class="routes rv">
        <div><b>{t('Autostrada A23')}</b><span>{t('Uscita Carnia, poi SS52 verso Tolmezzo e Forni di Sopra (27 km dal casello)')}</span></div>
        <div><b>{t('Dal Cadore')}</b><span>{t('SS52 da Forni di Sopra (26 km)')}</span></div>
        <div><b>{t('Da Pordenone')}</b><span>{t('SS552 del Monte Rest da Tramonti di Sopra')}</span></div>
        <div><b>{t("Dalla Val d'Arzino")}</b><span>{t('Strada comunale di Preone')}</span></div>
        <div><b>{t('In aereo')}</b><span>{t('Aeroporto di Trieste (103 km), Venezia Marco Polo (circa 2 h 30)')}</span></div>
        <div><b>{t('In treno')}</b><span>{t('Stazione Carnia, poi autobus SAF (fermata a Mediis, Bar alla Posta)')}</span></div>
      </div>
      <a class="btn btn-dark rv" href="https://www.google.com/maps/dir/?api=1&destination={lat},{lon}" target="_blank" rel="noopener">{t('Indicazioni stradali')} {I('arrow')}</a>
    </div>
    <div class="mapcard rv d2">
      <iframe title="{t('Mappa della reception a Mediis, Socchieve')}" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox={lon - 0.06}%2C{lat - 0.03}%2C{lon + 0.06}%2C{lat + 0.03}&amp;layer=mapnik&amp;marker={lat}%2C{lon}"></iframe>
      <div class="pin"><div><b>Reception · Mediis</b><span>{SITE['street']}, {SITE['zip']} Socchieve (UD)</span></div><a class="arrow" href="tel:{SITE['phone_href']}" aria-label="{t('Chiama la reception')}"><svg><use href="#i-arrow"/></svg></a></div>
    </div>
  </div>
  <div class="rv" style="margin-top:clamp(48px,6vw,80px)"><span class="eyebrow">{t('Distanze dalla reception')}</span><ul class="dist" style="margin-top:20px">{dist_items()}</ul></div>
</div></section>"""
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": t("Contatti"), "url": U + P("contact"), "about": {"@id": LODGING_ID}}
    page("contact", t("Contatti e come arrivare · Albergo Diffuso Socchieve"),
         t("Reception a Mediis (Socchieve, UD), tel. +39 0433 819934, info@albergodiffusosocchieve.it. Come arrivare in Carnia da A23, Cadore, Pordenone e aeroporto di Trieste."),
         body, active="contatti", image="Mediispanoramica.jpg", preload=preload_for("Mediispanoramica.jpg"), ld=[ld, lodging_ld(), crumbs_ld(crumbs)])


def welora_stays(view, title=None):
    """Widget soggiorni Welora di La Farie (stessi colori del sito, senza intestazione)."""
    F, W = FARIE, data.WELORA
    if not F["welora"]["live"]:
        return ""
    head = f'<h2 class="book-title">{title}</h2>' if title else ""
    return (f'<div class="book rv" id="prenota">{head}<div data-welora-booking data-slug="{F["welora"]["slug"]}" data-mode="stays" data-view="{view}" data-branding="none"></div>'
            f'<p class="book-note">{t("Prenotazione diretta · conferma via email")} · {e(F["cancel"])}</p></div>'
            f'<script src="{W["base"]}/assets/js/booking-widget.js?v={W["script_v"]}" defer></script>')


def build_farie():
    F = FARIE
    live = F["welora"]["live"]
    book_btn = (f'<a class="btn btn-primary" href="#prenota">{t("Prenota")} {I("arrow")}</a>') if live else (f'<a class="btn btn-primary" href="#scrivici">{t("Chiedi disponibilità")} {I("arrow")}</a>')
    fnav = f'<a href="#farie-casa">{t("La casa")}</a><a href="#farie-camere">{t("Camere")}</a><a href="#farie-foto">{t("Foto")}</a><a href="#farie-servizi">{t("Servizi")}</a><a href="#farie-info">{t("Info utili")}</a><a href="{P("home")}">← Col Gentile</a>'
    def wrap(body):
        return f"""<a class="skip" href="#main">{t('Vai al contenuto')}</a>
<div id="farie">
<header class="hdr" data-hdr>
  <div class="wrap bar">
    <a href="{P('farie')}" class="logo" aria-label="{t('La Farie, bed and breakfast a Lungis')}"><span><b>La Farie</b><small>{t('Bed &amp; Breakfast · Lungis, Carnia')}</small></span></a>
    <nav class="menu" aria-label="La Farie">{fnav}</nav>
    <div class="hdr-cta">{lang_switch()}{book_btn}<button class="burger" aria-label="{t('Apri menu')}" data-open><span></span></button></div>
  </div>
</header>
<div class="drawer" data-drawer aria-hidden="true" style="background:#2b1c14">
  <div class="drawer-top"><span class="logo"><span><b style="font-style:italic">La Farie</b></span></span><button class="close" data-close aria-label="{t('Chiudi menu')}">×</button></div>
  <nav>{fnav}</nav>
  {book_btn}
  {lang_switch("lang lang-drawer")}
</div>
<main id="main">{body}</main>
<footer class="foot"><div class="wrap"><div class="foot-bottom" style="margin-top:0;border:0;padding-top:0"><span>La Farie · Bed &amp; Breakfast · {F['addr']}, Lungis · 33020 Socchieve (UD)</span><span class="foot-links"><a href="{P('home')}">Albergo Diffuso Socchieve</a><a href="{P('booking-terms')}">{t('Condizioni di prenotazione')}</a><a href="{P('privacy')}">Privacy</a>{credits()}</span></div></div></footer>
</div>"""
    rules = "".join(f"<div><b>{k}</b><span>{v}</span></div>" for k, v in F["rules"])
    near = "".join(f"<li><b>{n}</b><span>{d}</span></li>" for n, d in F["near"])
    body = f"""<section class="hero" id="la-farie">
      <div class="hero-media">{pic(F['g'][0], t("La Farie, bed and breakfast in una casa carnica a Lungis"), "100vw", eager=True)}</div>
      <div class="wrap hero-in">
        <h1><span class="eyebrow light" style="display:flex;margin-bottom:22px">{t('Bed &amp; Breakfast a Lungis · Carnia')}</span>{t('La Farie. <em>Sentirsi a casa.</em>')}</h1>
        <div class="hero-row">
          <p>{t("Una casa tipica carnica ristrutturata nel borgo di Lungis, con camere con terrazza o balcone, giardino e la quiete delle montagne. Gestita dall'Albergo Diffuso Socchieve.")}</p>
          <div class="hero-actions">{'' if live else book_btn}<a class="btn btn-ghost" href="#farie-camere">{t('Le camere')}</a><a class="btn btn-ghost" href="#farie-foto">{t('Foto')}</a></div>
        </div>
        <div class="hero-meta"><span>Lungis · <b>554 m</b></span><span>Wi-Fi · <b>{t('Parcheggio gratuito')}</b></span><span>{t('Gestione <b>Albergo Diffuso Socchieve</b>')}</span></div>
      </div>
    </section>
    {f'<section class="book-sec"><div class="wrap">{welora_stays("search")}</div></section>' if live else ""}
    <section class="sec" id="farie-casa"><div class="wrap fa-split">
      {pic(F['g'][1], "La Farie, Lungis", "(max-width:820px) 100vw, 50vw", cls="rv")}
      <div><span class="eyebrow rv">{t('La casa')}</span><h2 class="rv d1">{t('Una casa carnica, <em>la quiete di Lungis.</em>')}</h2>
        {"".join(f'<p class="rv d2" style="margin-top:16px">{e(p)}</p>' for p in F['intro'])}
      </div></div></section>
    <section class="sec" id="farie-foto" style="padding-top:0"><div class="wrap">
      <span class="eyebrow rv">{t('Foto')}</span><h2 class="rv d1" style="font-size:clamp(36px,4.6vw,64px);line-height:1;margin:16px 0 28px">{tf('{c} foto di <em>La Farie</em>', c=len(F['g']))}</h2>
      <div class="rv">{gallery(F['g'], t("La Farie, bed and breakfast a Lungis"), max_shown=9)}</div>
    </div></section>
    <section class="sec" id="farie-camere" style="padding-top:0"><div class="wrap">
      <span class="eyebrow rv">{t('Le camere')}</span><h2 class="rv d1" style="font-size:clamp(36px,4.6vw,64px);line-height:1;margin:16px 0 28px">{t('Cinque camere, <em>un appartamento.</em>')}</h2>
      <div class="rooms rv">{"".join(f'<div class="room"><b>{e(n)}</b><span>{e(d)}</span><small>{tf("fino a {m} ospite", m=m) if m == 1 else tf("fino a {m} ospiti", m=m)}</small></div>' for n, d, m in F["rooms"])}</div>
      <p class="rv" style="margin-top:18px;color:var(--fa-muted)">{tf('Tariffe: {plans}.', plans=low(t(" o ").join(F["plans"])))} {e(F["cancel"])}</p>
    </div></section>
    <section class="sec" id="farie-servizi" style="padding-top:0"><div class="wrap">
      <span class="eyebrow rv">{t('Servizi')}</span><h2 class="rv d1" style="font-size:clamp(36px,4.6vw,64px);line-height:1;margin:16px 0 28px">{t('Tutto quello <em>che serve.</em>')}</h2>
      <ul class="amen rv">{"".join(f"<li>{a}</li>" for a in F['am'])}</ul>
    </div></section>
    <section class="sec" id="farie-info"><div class="wrap fa-split" style="align-items:start">
      <div><span class="eyebrow rv">{t('Info utili')}</span><h2 class="rv d1">{t('Prima di <em>arrivare.</em>')}</h2>
        <div class="routes rv" style="margin-top:24px">{rules}</div></div>
      <div><span class="eyebrow rv">{t('Dove siamo')}</span><h2 class="rv d1">{t('A Lungis, nella <em>Carnia più vera.</em>')}</h2>
        <p class="rv d2">{tf("{addr}, frazione di Lungis, comune di Socchieve (UD), a 554 metri di quota. A due passi l'agriturismo In Già, il bar alimentari Al Cervo e i sentieri dell'Anello delle Frazioni.", addr=F['addr'])}</p>
        <ul class="dist rv" style="margin-top:24px;grid-template-columns:repeat(2,1fr)">{near}</ul>
        <p class="rv" style="margin-top:24px"><a class="link" href="{P('vill:lungis')}">{t('Scopri il borgo di Lungis')} {I('arrow')}</a></p></div>
    </div></section>
    <section class="cta"><div class="wrap">
      <span class="eyebrow rv">La Farie · Lungis</span>
      <h2 class="rv d1">{t('Il tuo B&amp;B <em>in Carnia.</em>')}</h2>
      <p class="rv d2">{t('Scegli le date e prenota direttamente: conferma immediata via email. Hai domande? Scrivici.')}</p>
      <div class="row rv d3">{book_btn}<a class="btn btn-dark" href="#scrivici">{t('Scrivici')}</a><a class="btn btn-dark" href="{P('home')}">{t('Scopri anche Col Gentile')}</a></div>
    </div></section>"""
    ld = {"@context": "https://schema.org", "@type": "BedAndBreakfast", "@id": U + "/la-farie#bnb", "name": "La Farie",
          "description": " ".join(F["intro"]), "url": U + P("farie"), "image": [abs_img(g) for g in F["g"][:8] if g in PH],
          "address": address(F["addr"], "Lungis, Socchieve"),
          "geo": {"@type": "GeoCoordinates", "latitude": F["geo"][0], "longitude": F["geo"][1]},
          "checkinTime": "15:00", "checkoutTime": "10:00", "petsAllowed": True, "smokingAllowed": False,
          "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in F["am"]],
          "sameAs": [F["booking"]], "email": SITE["email"], "telephone": SITE["phone"], "parentOrganization": {"@id": LODGING_ID}}
    crumbs = [home_crumb(), ("La Farie", P("farie"))]
    page("farie", t("La Farie · Bed & Breakfast a Lungis, Socchieve (Carnia)"),
         t("B&B in una casa carnica ristrutturata a Lungis, Socchieve (Carnia), gestito dall'Albergo Diffuso Socchieve: camere con terrazza, giardino, Wi-Fi e parcheggio gratuito."),
         body, image=F["g"][0], preload=preload_for(F["g"][0]), wrapper=wrap, ld=[ld, crumbs_ld(crumbs)],
         images=[abs_img(g) for g in F["g"] if g in PH])


def welora(view, sid=None, title=None, note=True):
    """Widget servizi Welora: senza intestazione (logo e nome sono già nella pagina),
    con il servizio della pagina preselezionato e i colori del sito (variabili --welora-*)."""
    W = data.WELORA
    if not W["live"]:
        return ""
    svc = f' data-service="{sid}"' if sid else ""
    head = f'<h2 class="book-title">{title}</h2>' if title else ""
    foot = (f'<p class="book-note">{t("Conferma immediata via email · carta di credito richiesta a garanzia · preferisci parlarci?")} '
            f'<a href="tel:{SITE["phone_href"]}">{SITE["phone"]}</a> · <a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p>') if note else ""
    return (f'<div class="book rv" id="prenota">{head}<div data-welora-booking data-slug="{W["slug"]}" data-mode="services" data-view="{view}" data-branding="none"{svc}></div>{foot}</div>'
            f'<script src="{W["base"]}/assets/js/booking-widget.js?v={W["script_v"]}" defer></script>')


def svc_aside(s=None):
    name = s["n"] if s else t("Benessere")
    subj = e(t("Prenotazione ") + name)
    live = data.WELORA["live"]
    online = f'<a class="btn btn-primary" href="{P("svc-results")}">{t("Prenota online")} {I("arrow")}</a>' if live else ""
    price = f'<p style="margin-top:16px;color:var(--bone);font:400 30px/1 var(--serif)">{s["price"]} € <span style="font:500 14px var(--sans);color:var(--sage)">{s["unit"]}</span></p>' if s else ""
    intro = t("Scegli giorno, orario e numero di persone: la conferma arriva via email.") if live else t("Scrivici o chiamaci con giorno, orario e numero di persone: ti confermiamo la disponibilità.")
    mail_cls = "btn-ghost" if online else "btn-primary"
    return f"""<aside class="aside rv">
      <h2 style="font-size:30px;line-height:1.1;margin:0">{e(name)}</h2>
      {price}
      <p>{intro}</p>
      {online}
      <a class="btn {mail_cls}" href="mailto:{SITE['email']}?subject={subj}">{t('Prenota via email')} {I('arrow')}</a>
      <a class="btn btn-ghost" href="tel:{SITE['phone_href']}">{SITE['phone']}</a>
      <p style="margin-top:16px;font-size:13px">{t('Per prenotare online serve una carta di credito a garanzia.')}</p>
    </aside>"""


def svc_card(s):
    img = pic(s["hero"], s["n"], "(max-width:640px) 100vw, 50vw") if s["hero"] else ""
    cls = "tile big" if s["hero"] else "tile green"
    unit = s["unit"].split(",")[0]
    return (f'<a class="{cls} rv" href="{svc_url(s)}" style="grid-column:span 2">{img}<span class="num">{s["price"]} € · {unit}</span>'
            f'<h3>{e(s["n"])}</h3><p>{e(s["lead"])}</p><span class="link">{t("Scopri e prenota")} {I("arrow")}</span></a>')


def service_ld(s):
    url = U + svc_url(s)
    ld = {"@context": "https://schema.org", "@type": "Service", "@id": U + f"/it/{s['id']}#service", "name": s["n"], "serviceType": t("Benessere"),
          "description": " ".join(s["text"]), "url": url, "provider": {"@id": LODGING_ID}, "areaServed": "Carnia",
          "offers": {"@type": "Offer", "price": f"{s['price']:.2f}", "priceCurrency": "EUR", "description": s["unit"], "url": url}}
    if s["hero"]:
        ld["image"] = abs_img(s["hero"])
    return ld


def build_services():
    S = SERVICES
    live = data.WELORA["live"]
    for s in S:
        crumbs = [home_crumb(), (t("Benessere"), P("benessere")), (s["n"], svc_url(s))]
        facts = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in s["facts"])
        bring = ""
        if s.get("bring"):
            rows = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in s["bring"])
            note = f'<p class="cin" style="margin-top:18px">{e(s["note"])}</p>' if s.get("note") else ""
            bring = f'<div class="rv"><span class="eyebrow">{t("Cosa portare")}</span><h2>{t("Come prepararsi")}</h2><div class="routes">{rows}</div>{note}</div>'
        meet = ""
        if s.get("meeting"):
            meet = f'<div class="rv"><span class="eyebrow">{t("Ritrovo")}</span><h2>{t("Dove ci si incontra")}</h2><p>{e(s["meeting"])}. <a class="link" href="{P("contact")}">{t("Come arrivare")} {I("arrow")}</a></p></div>'
        price_pill = f"{s['price']} € {s['unit'].split(',')[0]}"
        book_pill = f'<a href="#prenota" style="color:inherit">{t("Prenota online")} →</a>'
        if s["hero"]:
            hero_html = hero(s["hero"], tf("{n} a Socchieve, Carnia", n=s["n"]), crumbs, e(s["n"]), sub=e(s["lead"]), pills=[price_pill] + ([book_pill] if live else []))
        else:
            hero_html = (f'<section class="ph ph-plain"><div class="wrap"><nav class="crumbs" aria-label="{t("Percorso")}"><a href="{P("home")}">Home</a><span>/</span>'
                         f'<a href="{P("benessere")}">{t("Benessere")}</a><span>/</span><b>{e(s["n"])}</b></nav><h1>{e(s["n"])}</h1><p class="lead">{e(s["lead"])}</p><div class="ph-meta"><span class="pill">{price_pill}</span>{f"<span class={chr(34)}pill{chr(34)}>{book_pill}</span>" if live else ""}</div></div></section>')
        paras = "".join(f'<p class="prose-first">{e(p)}</p>' if i == 0 else f"<p>{e(p)}</p>" for i, p in enumerate(s["text"]))
        minis = ""
        for x in S:
            if x["id"] == s["id"]:
                continue
            ph = pic(x["hero"], x["n"], "(max-width:640px) 70vw, 25vw") if x["hero"] else f'<div class="mini-ph">{e(x["n"])}</div>'
            minis += f'<a class="mini" href="{svc_url(x)}">{ph}<div><b>{x["n"]}</b><span>{x["price"]} € {x["unit"].split(",")[0]}</span></div></a>'
        for k in ("trekking", "cicloturismo", "visita-la-carnia"):
            x = EXPS[k]
            minis += f'<a class="mini" href="{exp_url(k)}">{pic(x["hero"], x["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{x["n"]}</b><span>{e(clip(x["lead"], 60))}</span></div></a>'
        h2 = {"bagno-di-bosco": t("Cos'è il bagno di bosco"), "sauna": t("Come funziona la sauna")}.get(s["id"], t("Come funziona"))
        intro = f'<div class="rv"><span class="eyebrow">{t("Benessere a Socchieve · Carnia")}</span><h2>{h2}</h2>{paras}</div><div class="facts rv">{facts}</div>'
        if live:
            book = welora("search", s["welora_id"], tf("Prenota {n}", n=low(s['n'])))
            main = f'<section class="d-body"><div class="wrap svc-wrap"><div class="d-main">{intro}{book}{meet}{bring}</div></div></section>'
        else:
            main = f'<section class="d-body"><div class="wrap d-grid"><div class="d-main">{intro}{meet}{bring}</div>{svc_aside(s)}</div></section>'
        body = f"""{hero_html}
{main}
<section class="related"><div class="wrap"><span class="eyebrow">{t('Benessere e natura')}</span><h2>{t('Da abbinare')}</h2><div class="mini-rail">{minis}</div></div></section>"""
        page("svc:" + s["id"], s["title"], s["desc"], body, active="benessere", image=s["hero"] or "PanoramaNonta1.jpg",
             preload=preload_for(s["hero"]) if s["hero"] else None, ld=[service_ld(s), crumbs_ld(crumbs)],
             images=[abs_img(s["hero"])] if s["hero"] else [])

    crumbs = [home_crumb(), (t("Benessere"), P("benessere"))]
    cards = "".join(svc_card(s) for s in S)
    body = f"""{hero("PanoramaNonta1.jpg", t("Prati al tramonto a Nonta, Socchieve"), crumbs, t("Benessere <em>in Carnia</em>"), sub=t("Sauna e bagno di bosco all'Albergo Diffuso di Socchieve: il modo giusto per chiudere una giornata in montagna."))}
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">{t('I servizi')}</span><h2 class="rv d1">{t('Rallenta, <em>respira.</em>')}</h2></div><p class="rv d2">{t('Prezzi chiari e conferma immediata. Per prenotare online serve una carta di credito a garanzia. Scrivici per sapere se si possono prenotare anche senza soggiornare da noi.')}</p></div>
  <div class="bento">{cards}</div>
  {welora("search", None, t("Prenota sauna o bagno di bosco"))}
</div></section>"""
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": t("Benessere all'Albergo Diffuso Socchieve"), "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": U + svc_url(s), "name": s["n"]} for i, s in enumerate(S)]}
    page("benessere", t("Benessere in Carnia: sauna e bagno di bosco a Socchieve"),
         t("Sauna (50 € l'ora per il gruppo) e bagno di bosco Shinrin-yoku con guida (15 € a persona) all'Albergo Diffuso di Socchieve, in Carnia. Prenota direttamente."),
         body, active="benessere", image="PanoramaNonta1.jpg", preload=preload_for("PanoramaNonta1.jpg"),
         ld=[items, crumbs_ld(crumbs)] + [service_ld(s) for s in S], images=[abs_img("PanoramaNonta1.jpg")])

    W = data.WELORA
    crumbs = [home_crumb(), (t("Benessere"), P("benessere")), (t("Prenota servizi"), P("svc-results"))]
    if W["live"]:
        inner = welora("results")
    else:
        inner = (f'<p style="max-width:620px;color:var(--muted);font-size:17px">{t("La prenotazione online sarà disponibile a breve. Nel frattempo scrivici a")} '
                 f'<a class="link" href="mailto:{SITE["email"]}?subject=Prenotazione%20servizi">{SITE["email"]}</a> {t("o chiama il")} '
                 f'<a class="link" href="tel:{SITE["phone_href"]}">{SITE["phone"]}</a>.</p>')
    body = f"""<section class="d-body" style="padding-top:140px"><div class="wrap">
  <nav class="crumbs" aria-label="{t('Percorso')}" style="color:var(--muted)"><a href="{P('home')}">Home</a><span>/</span><a href="{P('benessere')}">{t('Benessere')}</a><span>/</span><b>{t('Prenota servizi')}</b></nav>
  <h1 style="font-size:clamp(40px,6vw,80px);line-height:1;margin:10px 0 28px">{t('Prenota <em>sauna e bagno di bosco</em>')}</h1>
  {inner}
</div></section>"""
    page("svc-results", t("Prenota sauna e bagno di bosco · Albergo Diffuso Socchieve"),
         t("Prenota online sauna e bagno di bosco all'Albergo Diffuso di Socchieve, in Carnia."), body, active="benessere", solid=True,
         noindex=not W["live"], ld=[crumbs_ld(crumbs)])


def build_farie_extra():
    inner = welora_stays("results") or (f'<p style="max-width:620px;color:var(--muted);font-size:17px">{t("La prenotazione online sarà disponibile a breve.")} '
                                         f'{t("Scrivici a")} <a class="link" href="mailto:{SITE["email"]}?subject=La%20Farie">{SITE["email"]}</a> {t("o chiama il")} <a class="link" href="tel:{SITE["phone_href"]}">{SITE["phone"]}</a>.</p>')
    res = f"""<section class="d-body" style="padding-top:140px"><div class="wrap">
  <nav class="crumbs" aria-label="{t('Percorso')}" style="color:var(--muted)"><a href="{P('home')}">Home</a><span>/</span><a href="{P('farie')}">La Farie</a><span>/</span><b>{t('Prenota')}</b></nav>
  <h1 style="font-size:clamp(40px,6vw,80px);line-height:1;margin:10px 0 28px">{t('Prenota <em>La Farie</em>')}</h1>
  {inner}
</div></section>"""
    page("farie-results", t("Prenota La Farie · Bed & Breakfast a Lungis"), t("Disponibilità e prenotazione diretta delle camere di La Farie, B&B a Lungis (Socchieve)."), res,
         solid=True, noindex=True)
    F = FARIE
    plans = t(" e ").join(f"“{x}”" for x in F["plans"])
    rules = " · ".join(f"{k}: {v}" for k, v in F["rules"])
    cond = f"""<section class="d-body" style="padding-top:140px"><div class="wrap prose">
  <span class="eyebrow">La Farie · Lungis</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">{t('Condizioni di soggiorno')}</h1>
  <p>{tf("Valgono per le prenotazioni delle camere di La Farie, {addr}, Lungis, Socchieve (UD), gestita da {legal}, {street}, {locality}, P.I. {vat}.", addr=F['addr'], legal=SITE['legal'], street=SITE['street'], locality=SITE['locality'], vat=SITE['vat'])}</p>
  <h2>{t('Tariffe')}</h2><p>{tf("Sono disponibili le tariffe {plans}. Il prezzo è quello indicato al momento della prenotazione per le date, la camera e il numero di ospiti scelti.", plans=plans)}</p>
  <h2>{t('Cancellazione')}</h2><p>{e(F["cancel"])} {t('Dopo questo termine contatta la struttura.')}</p>
  <h2>{t('Arrivo e partenza')}</h2><p>{rules}.</p>
  <h2>{t('Contatti')}</h2><p><a href="mailto:{SITE['email']}">{SITE['email']}</a> · <a href="tel:{SITE['phone_href']}">{SITE['phone']}</a></p>
  <h2>{t('Dati personali')}</h2><p>{tf("I dati della prenotazione sono trattati come descritto nell'<a href=\"{href}\">informativa privacy</a>.", href=P('privacy'))}</p>
</div></section>"""
    page("farie-cond", t("Condizioni di soggiorno · La Farie, Lungis"), t("Condizioni di prenotazione e cancellazione delle camere di La Farie, B&B a Lungis gestito dall'Albergo Diffuso Socchieve."), cond, solid=True)


def build_legal():
    """Testi legali (versione 1.0). L'italiano è il testo di riferimento; le traduzioni EN e DE sono in
    i18n.LEGAL e rimandano all'originale."""
    pages = {}
    privacy = """<section class="d-body" style="padding-top:140px"><div class="wrap prose">
<span class="eyebrow">Informativa</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">Privacy</h1>
<p><strong>Versione 1.0 · 16 novembre 2026</strong></p>
<p>La presente informativa riguarda il sito dell’Albergo Diffuso Socchieve “Col Gentile”, i moduli di contatto e le richieste collegate ai soggiorni e ai servizi. È resa ai sensi del Regolamento (UE) 2016/679 (GDPR).</p>
<h2>1. Titolare del trattamento</h2>
<p><strong>Zanier Lucio</strong> · Albergo Diffuso Socchieve “Col Gentile” · Via Roma 20, Mediis, 33020 Socchieve (UD) · P. IVA 02790180307. Email: <a href="mailto:info@albergodiffusosocchieve.it">info@albergodiffusosocchieve.it</a> · Telefono: <a href="tel:+390433819934">+39 0433 819934</a>.</p>
<h2>2. Dati trattati</h2>
<p>Nei moduli contatti possono essere richiesti nome e cognome, indirizzo email, telefono (facoltativo), messaggio e informazioni sulla struttura o il servizio a cui si riferisce la richiesta. Per prenotazioni e soggiorni possono essere trattati dati identificativi e di contatto, date, numero di ospiti, preferenze, informazioni necessarie alla prenotazione e agli adempimenti previsti dalla legge. I server possono registrare dati tecnici di accesso, tra cui indirizzo IP, data, ora e risorse richieste.</p>
<h2>3. Finalità e basi giuridiche</h2>
<p>I dati sono utilizzati per rispondere alle richieste e predisporre preventivi (misure precontrattuali), gestire prenotazioni, soggiorni e servizi acquistati (esecuzione del contratto), adempiere agli obblighi fiscali, amministrativi e di pubblica sicurezza (obbligo legale) e proteggere la sicurezza del sito e prevenire abusi o spam (legittimo interesse). Non sono previsti trattamenti promozionali mediante i moduli descritti, salvo specifica informazione separata.</p>
<h2>4. Prenotazioni, pagamenti e carta a garanzia</h2>
<p>Le prenotazioni degli alloggi Col Gentile sono collegate a <strong>Slope</strong>; quelle di La Farie, sauna e bagno di bosco a <strong>Welora</strong>. Quando si utilizza un sistema esterno di prenotazione o pagamento, i dati inseriti nel relativo ambiente sono trattati anche dai fornitori coinvolti secondo i rispettivi ruoli e informative. Il modulo contatti del sito non richiede il numero della carta di credito. Le condizioni della carta a garanzia e degli eventuali addebiti sono indicate nella procedura di prenotazione e nelle <a href="/condizioni-prenotazione">condizioni di prenotazione</a>.</p>
<h2>5. Destinatari e strumenti esterni</h2>
<p>I dati possono essere comunicati, nei limiti necessari, a fornitori di hosting e posta elettronica, servizi di prenotazione e pagamento, collaboratori autorizzati, consulenti e autorità nei casi previsti dalla legge. Il sito può collegare mappe OpenStreetMap, tour 360° con librerie esterne e altri contenuti o servizi di terzi. Quando tali risorse vengono caricate, i relativi fornitori possono ricevere dati tecnici di connessione.</p>
<h2>6. Conservazione e sicurezza</h2>
<p>Le richieste sono conservate per il tempo necessario a rispondere e a gestire gli eventuali rapporti successivi; i dati di prenotazione e quelli amministrativi per i periodi imposti dalle norme applicabili. Si adottano misure tecniche e organizzative adeguate a proteggere i dati personali.</p>
<h2>7. Trasferimenti internazionali</h2>
<p>L’uso di servizi esterni può comportare trasferimenti di dati al di fuori dello Spazio Economico Europeo. Quando presenti, tali trasferimenti devono avvenire secondo le garanzie previste dal GDPR.</p>
<h2>8. Diritti dell’interessato</h2>
<p>Puoi chiedere accesso, rettifica, cancellazione, limitazione, portabilità o opposizione nei casi previsti dalla normativa e revocare eventuali consensi senza pregiudicare la liceità dei trattamenti precedenti. Per esercitare i diritti scrivi a <a href="mailto:info@albergodiffusosocchieve.it">info@albergodiffusosocchieve.it</a>. Puoi proporre reclamo al Garante per la protezione dei dati personali.</p>
<h2>9. Cookie e aggiornamenti</h2>
<p>Per informazioni sui cookie e sui servizi integrati consulta la <a href="/cookies">Cookie Policy</a>. Questa informativa può essere aggiornata; la versione vigente è pubblicata su questa pagina.</p>
</div></section>"""
    pages["privacy"] = ("Privacy · Albergo Diffuso Socchieve", "Informativa privacy GDPR per ospiti, contatti, prenotazioni e servizi dell'Albergo Diffuso Socchieve.", privacy)
    cookies = """<section class="d-body" style="padding-top:140px"><div class="wrap prose">
<span class="eyebrow">Informativa</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">Cookie</h1>
<p><strong>Versione 1.0 · 16 novembre 2026</strong></p>
<p>Il sito utilizza le risorse tecniche necessarie a visualizzare le pagine e a gestire le richieste. Non sono dichiarati sistemi di analisi o profilazione gestiti direttamente dal sito; tuttavia i servizi esterni integrati possono utilizzare cookie e tecnologie analoghe.</p>
<h2>Servizi esterni</h2>
<p>I sistemi di prenotazione <strong>Slope</strong> e <strong>Welora</strong> possono utilizzare propri cookie e strumenti tecnici nei rispettivi ambienti o widget. Altri componenti esterni, come la mappa OpenStreetMap e il tour virtuale, possono ricevere dati tecnici quando vengono caricati. Consulta le informative rese disponibili dai rispettivi fornitori per conoscere categorie, finalità, durata dei cookie e modalità di gestione delle preferenze.</p>
<h2>Preferenze e contatti</h2>
<p>Puoi gestire o eliminare i cookie attraverso le impostazioni del browser e, quando disponibili, attraverso i controlli presenti nei servizi esterni. Per richieste relative ai dati personali consulta l’<a href="/privacy">informativa privacy</a> o scrivi a <a href="mailto:info@albergodiffusosocchieve.it">info@albergodiffusosocchieve.it</a>.</p>
</div></section>"""
    pages["cookies"] = ("Cookie · Albergo Diffuso Socchieve", "Informativa sui cookie del sito e sui servizi esterni di prenotazione.", cookies)
    terms = """<section class="d-body" style="padding-top:140px"><div class="wrap prose">
<span class="eyebrow">Benessere</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">Condizioni di prenotazione dei servizi</h1>
<p><strong>Versione 1.0 · 16 novembre 2026</strong></p>
<p>Queste condizioni si riferiscono alle prenotazioni di sauna e bagno di bosco proposte dall’Albergo Diffuso Socchieve “Col Gentile”, Via Roma 20, Mediis, 33020 Socchieve (UD), P. IVA 02790180307. Sono parte delle <a href="/condizioni-prenotazione">condizioni generali di prenotazione</a>.</p>
<h2>Prezzi e durata</h2>
<p>La sauna è proposta a <strong>50 € l’ora per l’intero gruppo</strong>, con durata minima di un’ora. Il bagno di bosco è proposto a <strong>15 € a persona</strong>, con durata indicativa di circa due ore. Prezzi, date e disponibilità effettivi sono mostrati prima della conferma; si applica il prezzo accettato nella prenotazione.</p>
<h2>Carta a garanzia</h2>
<p>La prenotazione online può richiedere una carta a garanzia tramite Welora. Gli eventuali addebiti e le condizioni economiche applicabili devono essere mostrati prima della conferma. Non viene qui stabilito un importo aggiuntivo di penale per cancellazione tardiva o mancata presentazione in assenza di una specifica condizione comunicata e accettata nella prenotazione.</p>
<h2>Modifiche, cancellazioni e mancata presentazione</h2>
<p>Per modificare o annullare una prenotazione contatta tempestivamente la struttura all’indirizzo <a href="mailto:info@albergodiffusosocchieve.it">info@albergodiffusosocchieve.it</a> o al numero <a href="tel:+390433819934">+39 0433 819934</a>. In caso di mancata presentazione valgono soltanto le condizioni di penale rese note prima della conferma e accettate per quello specifico servizio; nessuna percentuale standard è indicata nel regolamento pubblico consultato.</p>
<h2>Svolgimento dei servizi</h2>
<p>Il bagno di bosco si svolge all’aperto su sentieri e terreno boschivo: sono necessari abbigliamento e calzature adatti. Per entrambi i servizi valgono la capienza, l’orario e le indicazioni comunicate nella conferma. Per la privacy consulta l’<a href="/privacy">informativa privacy</a>.</p>
</div></section>"""
    pages["terms"] = ("Condizioni di prenotazione dei servizi · Albergo Diffuso Socchieve",
                      "Condizioni per prenotazioni sauna e bagno di bosco: prezzo, carta a garanzia, cancellazioni e mancata presentazione.", terms)
    booking_terms = """<section class="d-body" style="padding-top:140px"><div class="wrap prose">
<span class="eyebrow">Informazioni contrattuali</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">Condizioni di prenotazione</h1>
<p><strong>Versione 1.0 · 16 novembre 2026</strong></p>
<p>Le presenti condizioni riguardano i soggiorni presso l’Albergo Diffuso Socchieve “Col Gentile”, il bed &amp; breakfast La Farie e i servizi sauna e bagno di bosco. Gestore: <strong>Zanier Lucio</strong>, Albergo Diffuso Socchieve “Col Gentile”, Via Roma 20, Mediis, 33020 Socchieve (UD), P. IVA 02790180307 · <a href="mailto:info@albergodiffusosocchieve.it">info@albergodiffusosocchieve.it</a>.</p>
<h2>1. Prezzi, disponibilità e conferma</h2>
<p>Disponibilità, prezzo totale, eventuali supplementi, caparra, condizioni della tariffa e modalità di pagamento sono mostrati prima della conferma della prenotazione o comunicati nel preventivo accettato. La prenotazione è confermata alle condizioni riportate nella conferma inviata al cliente. Condizioni specifiche di una tariffa, espressamente comunicate e accettate prima della conferma, prevalgono sulle indicazioni generali di questa pagina.</p>
<h2>2. Soggiorni negli alloggi Col Gentile</h2>
<p>Secondo il regolamento del sito ufficiale dell’Albergo Diffuso Socchieve, il prezzo comprende l’uso dell’alloggio e la biancheria da bagno e da camera. Gli alloggi sono disponibili dalle 12:00 e devono essere liberati entro le 10:00 del giorno di partenza, salvo accordi o indicazioni specifiche della conferma. Il saldo è previsto preferibilmente all’arrivo; gli eventuali extra sono conteggiati alla partenza.</p>
<h3>Supplementi e riduzioni per gli alloggi Col Gentile</h3>
<p>Il regolamento ufficiale pubblica i seguenti supplementi: animali, ove ammessi, 5 € una tantum; culla per neonati, 5 € una tantum; pulizia extra, 10 € per appartamenti piccoli o 15 € per appartamenti grandi; biancheria da letto aggiuntiva, 4 €; spugna aggiuntiva, 1 € al pezzo. Per soggiorni inferiori a tre notti indica una maggiorazione del 30% e per uso singolo degli appartamenti un aumento del 50% sulla tariffa. Le riduzioni indicate sono: gratuità fino a 3 anni, 50% dai 4 ai 6 anni e 30% dai 7 ai 10 anni. Importi e condizioni effettivi della prenotazione sono quelli confermati nel preventivo o nel riepilogo tariffario prima dell’acquisto.</p>
<h2>3. Caparra, cancellazione e partenza anticipata negli alloggi Col Gentile</h2>
<p>Il regolamento pubblicato prevede che, in caso di disdetta, la <strong>caparra eventualmente versata non venga rimborsata</strong>; previo accordo con la direzione può essere consentito recuperarla in un’altra data a condizioni equivalenti. Per la partenza anticipata è previsto l’addebito del costo del solo alloggio per il periodo non usufruito, salvo diverso accordo. Se la tariffa prenotata presenta una diversa politica di cancellazione, vale quella comunicata e accettata durante la prenotazione.</p>
<h2>4. La Farie</h2>
<p>Per il bed &amp; breakfast La Farie la condizione indicata nella pagina di prenotazione è: <strong>cancellazione gratuita tramite il portale fino a 7 giorni prima dell’arrivo, entro le ore 18:00</strong>. Per cancellazioni successive, mancata presentazione, eventuali caparre o addebiti si applicano esclusivamente gli importi e le condizioni espressamente mostrati e accettati durante la prenotazione; la presente pagina non introduce una percentuale di penale ulteriore.</p>
<h2>5. Mancata presentazione (no-show) e carta a garanzia</h2>
<p>Se il cliente non si presenta nella data e nell’orario concordati e non ha cancellato nei termini, si applicano le condizioni economiche della specifica prenotazione. Per Col Gentile resta applicabile la regola sulla caparra eventualmente versata, salvo diversa tariffa concordata. <strong>Non è pubblicata una penale percentuale standard aggiuntiva per il no-show</strong>: ulteriori addebiti su carta a garanzia possono essere effettuati soltanto se l’importo o il criterio di calcolo della penale sono stati comunicati prima della conferma e accettati dal cliente. La carta a garanzia viene richiesta e gestita nell’ambiente del sistema di prenotazione, quando previsto.</p>
<h2>6. Sauna e bagno di bosco</h2>
<p>La sauna è proposta a <strong>50 € l’ora per il gruppo</strong>; il bagno di bosco a <strong>15 € a persona</strong>. Le prenotazioni online possono richiedere una carta a garanzia tramite Welora. Modifiche, cancellazioni e no-show sono disciplinati dalle condizioni specifiche indicate e accettate in fase di prenotazione. In assenza di una penale esplicitamente comunicata prima della conferma, questa pagina non ne introduce una. Consulta anche le <a href="/condizioni-servizi">condizioni dettagliate dei servizi</a>.</p>
<h2>7. Regole del soggiorno</h2>
<p>Ogni ospite, inclusi i minori, deve presentare un documento di identità idoneo per gli adempimenti di legge. Non possono pernottare persone non registrate. Negli alloggi non è consentito fumare. Si richiede il rispetto della quiete nelle fasce orarie 23:00–08:00 e 14:00–16:00. Il regolamento vieta di portare la biancheria della struttura all’esterno degli appartamenti e di utilizzare apparecchi per cucinare o riscaldare cibi nelle camere non adibite a cucina. Biancheria mancante, danni o smarrimenti di chiavi possono comportare un addebito valutato in base al danno effettivo e secondo la normativa applicabile.</p>
<h2>8. Assistenza e privacy</h2>
<p>Per cancellazioni, modifiche o chiarimenti contatta <a href="mailto:info@albergodiffusosocchieve.it">info@albergodiffusosocchieve.it</a> oppure <a href="tel:+390433819934">+39 0433 819934</a>. I dati personali sono trattati secondo l’<a href="/privacy">informativa privacy</a>.</p>
</div></section>"""
    pages["booking-terms"] = ("Condizioni di prenotazione · Albergo Diffuso Socchieve",
                              "Condizioni di prenotazione per soggiorni Col Gentile, La Farie, sauna e bagno di bosco: caparra, cancellazioni, no-show e carta a garanzia.", booking_terms)
    for key, (title, desc, body) in pages.items():
        if LANG != "it":
            title, desc, body = i18n.LEGAL[LANG][key]
            body = body.format(privacy=P("privacy"), cookies=P("cookies"), booking=P("booking-terms"), terms=P("terms"), original=P(key, "it"))
        page(key, title, desc, body, solid=True)


def build_404():
    """Pagina 404 unica (il server non sa la lingua): testo in italiano con richiami a EN e DE."""
    err = f"""<section class="err"><div><span class="eyebrow">Errore 404</span><h1>Pagina <em>non trovata.</em></h1><p style="margin:20px auto 30px;max-width:460px;color:var(--muted)">Forse la pagina è stata spostata con il nuovo sito. Ecco da dove ripartire:</p>
  <div class="row" style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap"><a class="btn btn-dark" href="/it/alloggi/">Le case</a><a class="btn btn-primary" href="/">Home</a></div>
  <p style="margin-top:28px;color:var(--muted);font-size:15px"><span lang="en">Page not found:</span> <a class="link" href="/en/" lang="en">English home</a> · <span lang="de">Seite nicht gefunden:</span> <a class="link" href="/de/" lang="de">Startseite auf Deutsch</a></p></div></section>"""
    page("404", "Pagina non trovata · Albergo Diffuso Socchieve", "La pagina richiesta non esiste.", err, solid=True, noindex=True)
    # vecchia home /it -> /
    (ROOT / "it").mkdir(exist_ok=True)
    (ROOT / "it" / "index.html").write_text(f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Albergo Diffuso Socchieve</title><link rel="canonical" href="{U}/"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url=../"></head><body><a href="../">Vai alla home</a></body></html>\n', encoding="utf-8")


# ---------------------------------------------------------------- file di servizio
def build_meta():
    urls = []
    for key, lang, imgs in PAGES:
        path = P(key, lang)
        prio = "1.0" if key == "home" else "0.9" if key.startswith("stay:") or key == "catalog" else "0.7"
        im = "".join(f"<image:image><image:loc>{x}</image:loc></image:image>" for x in dict.fromkeys(imgs) if x)
        alt = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{U}{P(key, l)}"/>' for l in LANGS) if key not in ONLY_IT else ""
        urls.append(f"<url><loc>{U}{path}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority>{alt}{im}</url>")
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {U}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(json.dumps({"name": SITE["name"], "short_name": "Col Gentile", "start_url": "./", "display": "standalone", "background_color": "#fbf8f2", "theme_color": "#16241e",
        "icons": [{"src": "apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False), encoding="utf-8")
    # redirect 301 (Netlify / Cloudflare Pages): vecchie pagine inglesi e francesi verso le nuove pagine
    # in inglese (il francese non c'è: l'inglese è la lingua più vicina per chi arriva da lì)
    old = {"": "home", "/accomodation": "catalog", "/logement": "catalog", "/territory": "territorio", "/territoire": "territorio",
           "/visit-carnia": "exp:visita-la-carnia", "/visiter-la-carnia": "exp:visita-la-carnia", "/cycle-touring": "exp:cicloturismo", "/cyclisme": "exp:cicloturismo",
           "/trekking": "exp:trekking", "/art-and-culture": "exp:arte-e-cultura", "/art-et-culture": "exp:arte-e-cultura", "/contact": "contact",
           "/alloggi/casa-vanda-0": "stay:casa-vanda"}
    lines = ["/it  /  301"]
    for lang in ("en", "fr"):
        for a, key in old.items():
            src, dst = f"/{lang}{a}", P(key, "en")
            if src.rstrip("/") != dst.rstrip("/"):
                lines.append(f"{src}  {dst}  301")
        for s in IT_DATA["STAYS"]:
            lines.append(f"/{lang}/alloggi/{s['id']}  {P('stay:' + s['id'], 'en')}  301")
        if lang == "fr":
            lines.append("/fr/*  /en/  301")
    (ROOT / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_icons():
    from PIL import Image, ImageDraw
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#16241e"/><path d="M12 44 25 25l7 10 6-7 14 16" fill="none" stroke="#e2c39d" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M28 44v-7h8v7" fill="none" stroke="#e2c39d" stroke-width="3.2" stroke-linejoin="round"/></svg>'
    (ROOT / "favicon.svg").write_text(svg, encoding="utf-8")
    for sz, name in ((180, "apple-touch-icon.png"), (512, "icon-512.png"), (32, "favicon-32.png")):
        k = sz / 64
        im = Image.new("RGB", (sz, sz), "#16241e")
        d = ImageDraw.Draw(im)
        w = max(2, round(3.2 * k))
        d.line([(12 * k, 44 * k), (25 * k, 25 * k), (32 * k, 35 * k), (38 * k, 28 * k), (52 * k, 44 * k)], fill="#e2c39d", width=w, joint="curve")
        d.line([(28 * k, 44 * k), (28 * k, 37 * k), (36 * k, 37 * k), (36 * k, 44 * k)], fill="#e2c39d", width=w)
        im.save(ROOT / name)


def main():
    global CSS_V, JS_V
    (ROOT / "assets").mkdir(exist_ok=True)
    css = (SRC / "fonts.css").read_text(encoding="utf-8").replace("url(/assets/fonts/", "url(fonts/") + "\n" + (SRC / "site.css").read_text(encoding="utf-8")
    (ROOT / "assets" / "site.css").write_text(css, encoding="utf-8")
    shutil.copy(SRC / "site.js", ROOT / "assets" / "site.js")
    CSS_V, JS_V = asset_ver(ROOT / "assets" / "site.css"), asset_ver(ROOT / "assets" / "site.js")
    for lang in LANGS:
        localize(lang)
        build_home(); build_catalog()
        for s in STAYS: build_stay(s)
        for v in VILLAGES: build_village(v)
        for k, x in EXPS.items(): build_exp(k, x)
        build_territorio(); build_contact(); build_farie(); build_farie_extra(); build_services(); build_legal()
    localize("it")
    build_404()
    build_meta(); build_icons()
    print(f"OK: {len(PAGES)} pagine indicizzabili in {len(LANGS)} lingue, sitemap.xml, robots.txt, _redirects")
    if MISSING:
        print(f"  ! {len(MISSING)} immagini ancora remote: rilancia fetch_assets.py e poi build.py")
    for lang, miss in MISSING_TR.items():
        print(f"  ! {len(miss)} testi senza traduzione in {lang}:")
        for m in sorted(miss):
            print("     -", m[:110])


if __name__ == "__main__":
    main()
