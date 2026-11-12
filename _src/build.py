"""Genera il sito statico. Uso:  python _src/build.py
Legge _src/data.py e _src/images.json (creato da fetch_assets.py) e scrive le pagine HTML
agli stessi URL del vecchio sito, più sitemap.xml, robots.txt e asset."""
import datetime, hashlib, html, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
sys.path.insert(0, str(SRC))
import data  # noqa: E402
from data import SITE, STAYS, VILLAGES, EXPS, FAQ, DISTANCES  # noqa: E402

IMGS = json.loads((SRC / "images.json").read_text(encoding="utf-8"))
PH, PANO = IMGS["photos"], IMGS["panos"]
U = SITE["url"]
TODAY = datetime.date.today().isoformat()
STAY = {s["id"]: s for s in STAYS}
VILL = {v["id"]: v for v in VILLAGES}
VILL_BY_NAME = {v["n"]: v for v in VILLAGES}
PAGES = []  # (path, file, images) per la sitemap
e = html.escape


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


def stay_url(s): return f"/it/alloggi/{s['id']}"
def vill_url(v): return f"/it/{v['id']}"
def exp_url(k): return f"/it/{k}"
def beds(n): return f"Fino a {n} ospiti"
def size(n): return "s" if n <= 8 else "m" if n <= 16 else "l"
def top_stays(): return [s for s in STAYS if not s.get("parent")]
def stays_in(b): return [s for s in STAYS if s["b"] == b and not s.get("parent")]


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


NAV = [("alloggi", "/it/alloggi/", "Le case"), ("borghi", "/it/territorio#borghi", "I borghi"),
       ("esperienze", "/it/territorio#esperienze", "Esperienze"), ("benessere", "/it/benessere", "Benessere"), ("contatti", "/it/contact", "Contatti"),
       ("farie", "/la-farie", "La Farie")]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="i-left" viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="i-right" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21Z" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="9.5" r="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/></symbol>
  <symbol id="i-mark" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M6 28 15 15l5 7 4-5 10 11" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M17 28v-5h6v5" fill="none" stroke="currentColor" stroke-width="1.4"/></symbol>
</svg>"""

LIGHTBOX = """<dialog class="lb" data-lb aria-label="Galleria fotografica">
  <div class="lb-top"><span data-lb-count></span><button class="lb-close" data-lb-close aria-label="Chiudi galleria">×</button></div>
  <div class="lb-stage">
    <button class="lb-nav lb-prev" data-lb-step="-1" aria-label="Foto precedente"><svg><use href="#i-left"/></svg></button>
    <img data-lb-img alt="">
    <button class="lb-nav lb-next" data-lb-step="1" aria-label="Foto successiva"><svg><use href="#i-right"/></svg></button>
  </div>
  <div class="lb-thumbs" data-lb-thumbs></div>
</dialog>"""


def header(active, solid=False):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{t}</a>' for k, h, t in NAV)
    return f"""<a class="skip" href="#main">Vai al contenuto</a>
<header class="hdr" data-hdr{" data-solid" if solid else ""}>
  <div class="wrap bar">
    <a href="/" class="logo" aria-label="Albergo Diffuso Socchieve Col Gentile, home">
      <svg class="logo-mark" aria-hidden="true"><use href="#i-mark"/></svg>
      <span><b>Col Gentile</b><small>Albergo Diffuso Socchieve</small></span>
    </a>
    <nav class="menu" aria-label="Principale">{links}</nav>
    <div class="hdr-cta">
      <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">Prenota {I('arrow')}</a>
      <button class="burger" aria-label="Apri menu" data-open><span></span></button>
    </div>
  </div>
</header>
<div class="drawer" data-drawer aria-hidden="true">
  <div class="drawer-top"><span class="logo"><svg class="logo-mark" aria-hidden="true"><use href="#i-mark"/></svg><span><b>Col Gentile</b></span></span><button class="close" data-close aria-label="Chiudi menu">×</button></div>
  <nav aria-label="Menu mobile"><a href="/">Home</a>{"".join(f'<a href="{h}">{t}</a>' for k, h, t in NAV)}</nav>
  <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">Verifica disponibilità {I('arrow')}</a>
</div>"""


def footer():
    case = "".join(f'<a href="{stay_url(s)}">{e(s["n"])}</a>' for s in top_stays())
    borghi = "".join(f'<a href="{vill_url(v)}">{e(v["n"])}</a>' for v in VILLAGES)
    exps = "".join(f'<a href="{exp_url(k)}">{e(x["n"])}</a>' for k, x in EXPS.items())
    return f"""<footer class="foot" id="contatti">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a href="/" class="logo" style="color:var(--bone)"><svg class="logo-mark" aria-hidden="true"><use href="#i-mark"/></svg><span><b>Col Gentile</b><small>Albergo Diffuso Socchieve</small></span></a>
        <p class="big">La porta delle Dolomiti Friulane.</p>
        <p>{SITE['street']}, {SITE['locality']}<br>{SITE['zip']} Socchieve (UD) · Friuli Venezia Giulia</p>
        <a href="mailto:{SITE['email']}">{SITE['email']}</a><a href="tel:{SITE['phone_href']}">{SITE['phone']}</a><a href="tel:{SITE['mobile_href']}">{SITE['mobile']}</a>
        <div class="partners">{pic("logoborghi%20autentici%20d%27Italia.jpg", "Borghi Autentici d'Italia", "120px")}</div>
      </div>
      <div><h4>Le case</h4>{case}<a href="/it/alloggi/">Tutte le case →</a></div>
      <div><h4>I borghi</h4>{borghi}</div>
      <div><h4>Esperienze</h4>{exps}<a href="/it/benessere">Benessere: sauna e bagno di bosco</a><a href="/it/territorio">Il territorio</a><a href="/it/contact">Contatti e come arrivare</a><a href="/la-farie">La Farie</a></div>
    </div>
    <div class="foot-bottom"><span>© {datetime.date.today().year} {SITE['legal']} · P.I. {SITE['vat']}</span><span><a href="/privacy">Privacy</a><a href="/cookies">Cookie</a></span></div>
  </div>
</footer>"""



def contact_form(brand="col-gentile"):
    """Modulo AJAX: markup comune alle pagine; invio gestito da /contatti.php."""
    if brand == "la-farie":
        return "\n<section class=\"sec contact-section\" id=\"scrivici\" aria-labelledby=\"contact-title\">\n  <div class=\"wrap contact-grid\">\n    <div class=\"contact-intro\">\n      <span class=\"eyebrow\">La Farie · Lungis</span>\n      <h2 id=\"contact-title\">Scrivi a <em>La Farie.</em></h2>\n      <p>Il messaggio sarà identificato come richiesta per La Farie e non per gli appartamenti Col Gentile.</p>\n      <p class=\"contact-small\">I campi contrassegnati con * sono obbligatori. La richiesta non costituisce una prenotazione.</p>\n    </div>\n    <form class=\"contact-form\" data-ajax-contact action=\"/contatti.php\" method=\"post\" accept-charset=\"UTF-8\">\n      <input type=\"hidden\" name=\"brand\" value=\"la-farie\">\n      <div class=\"contact-honeypot\" aria-hidden=\"true\"><label>Lascia vuoto questo campo<input type=\"text\" name=\"website\" tabindex=\"-1\" autocomplete=\"off\"></label></div>\n      <div class=\"contact-fields\">\n        <label>Nome e cognome *<input type=\"text\" name=\"nome\" autocomplete=\"name\" minlength=\"2\" maxlength=\"100\" required placeholder=\"Il tuo nome\"></label>\n        <label>Email *<input type=\"email\" name=\"email\" autocomplete=\"email\" maxlength=\"254\" required placeholder=\"nome@esempio.it\"></label>\n        <label>Telefono (facoltativo)<input type=\"tel\" name=\"telefono\" autocomplete=\"tel\" maxlength=\"40\" placeholder=\"+39 ...\"></label>\n        <label class=\"contact-wide\">Messaggio *<textarea name=\"messaggio\" rows=\"5\" minlength=\"10\" maxlength=\"5000\" required placeholder=\"Raccontaci la tua richiesta...\"></textarea></label>\n      </div>\n      <label class=\"contact-consent\"><input type=\"checkbox\" name=\"privacy\" value=\"1\" required> Ho letto l'<a href=\"/privacy\" target=\"_blank\" rel=\"noopener noreferrer\">informativa sulla privacy</a> e acconsento al trattamento dei dati per rispondere alla mia richiesta. *</label>\n      <div class=\"contact-form-actions\"><button type=\"submit\" class=\"btn btn-primary\" data-form-submit>Invia il messaggio</button><span class=\"contact-small\">Risposta visibile qui dopo l'invio</span></div>\n      <p class=\"contact-result\" data-form-status role=\"status\" aria-live=\"polite\" aria-atomic=\"true\" tabindex=\"-1\" hidden></p>\n    </form>\n  </div>\n</section>\n"
    return "\n<section class=\"sec contact-section\" id=\"scrivici\" aria-labelledby=\"contact-title\">\n  <div class=\"wrap contact-grid\">\n    <div class=\"contact-intro\">\n      <span class=\"eyebrow\">Col Gentile · Albergo Diffuso</span>\n      <h2 id=\"contact-title\">Richiedi informazioni <em>sul soggiorno.</em></h2>\n      <p>Per informazioni su case, periodi e soggiorni a Socchieve, inviaci un messaggio. Per la disponibilità aggiornata utilizza sempre il motore di prenotazione.</p>\n      <p class=\"contact-small\">I campi contrassegnati con * sono obbligatori. La richiesta non costituisce una prenotazione.</p>\n    </div>\n    <form class=\"contact-form\" data-ajax-contact action=\"/contatti.php\" method=\"post\" accept-charset=\"UTF-8\">\n      <input type=\"hidden\" name=\"brand\" value=\"col-gentile\">\n      <div class=\"contact-honeypot\" aria-hidden=\"true\"><label>Lascia vuoto questo campo<input type=\"text\" name=\"website\" tabindex=\"-1\" autocomplete=\"off\"></label></div>\n      <div class=\"contact-fields\">\n        <label>Nome e cognome *<input type=\"text\" name=\"nome\" autocomplete=\"name\" minlength=\"2\" maxlength=\"100\" required placeholder=\"Il tuo nome\"></label>\n        <label>Email *<input type=\"email\" name=\"email\" autocomplete=\"email\" maxlength=\"254\" required placeholder=\"nome@esempio.it\"></label>\n        <label>Telefono (facoltativo)<input type=\"tel\" name=\"telefono\" autocomplete=\"tel\" maxlength=\"40\" placeholder=\"+39 ...\"></label>\n        <label class=\"contact-wide\">Messaggio *<textarea name=\"messaggio\" rows=\"5\" minlength=\"10\" maxlength=\"5000\" required placeholder=\"Raccontaci la tua richiesta...\"></textarea></label>\n      </div>\n      <label class=\"contact-consent\"><input type=\"checkbox\" name=\"privacy\" value=\"1\" required> Ho letto l'<a href=\"/privacy\" target=\"_blank\" rel=\"noopener noreferrer\">informativa sulla privacy</a> e acconsento al trattamento dei dati per rispondere alla mia richiesta. *</label>\n      <div class=\"contact-form-actions\"><button type=\"submit\" class=\"btn btn-primary\" data-form-submit>Invia il messaggio</button><span class=\"contact-small\">Risposta visibile qui dopo l'invio</span></div>\n      <p class=\"contact-result\" data-form-status role=\"status\" aria-live=\"polite\" aria-atomic=\"true\" tabindex=\"-1\" hidden></p>\n    </form>\n  </div>\n</section>\n"


def page(path, title, desc, body, *, active="", image=None, ld=(), solid=False, noindex=False, images=(), preload=None, og_type="website", wrapper=None):
    canonical = U + path
    og = og_img(image) if image else og_img("Slide1Socchieve.jpg")
    head_ld = "\n".join(jsonld(x) for x in ld)
    pre = f'<link rel="preload" as="image" href="{preload[0]}" imagesrcset="{preload[1]}" imagesizes="100vw" fetchpriority="high">' if preload else ""
    if path in ("/", "/it/contact", "/la-farie"):
        body += contact_form("la-farie" if path == "/la-farie" else "col-gentile")
    content = wrapper(body) if wrapper else f"{header(active, solid)}\n<main id=\"main\">\n{body}\n</main>\n{footer()}"
    doc = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow,max-image-preview:large'}">
<meta name="theme-color" content="#16241e">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:locale" content="it_IT">
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
{LIGHTBOX}
<script src="/assets/site.js?v={JS_V}" defer></script>
</body>
</html>
"""
    if path == "/":
        out = ROOT / "index.html"
    elif path.endswith("/"):
        out = ROOT / path.strip("/") / "index.html"
    else:
        out = ROOT / (path.strip("/") + ".html")
    if path == "/404":
        doc = doc.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + BASE_404, 1)
    doc = relativize(doc, len(out.relative_to(ROOT).parts) - 1)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8", newline="\n")
    if not noindex:
        PAGES.append((path, list(images)))


# ---------------------------------------------------------------- blocchi riusabili
def card(s, feature=False):
    badge = '<span class="badge360">360°</span>' if s.get("pano") else ""
    sizes = "(max-width:640px) 84vw, (max-width:1080px) 50vw, 33vw" if not feature else "(max-width:640px) 84vw, 60vw"
    return f"""<a class="card{' feature' if feature else ''}" data-b="{s['b']}" data-s="{size(s['beds'])}" href="{stay_url(s)}">
      <div class="card-img">{pic(s['card'], f"{s['n']}, {s['label'].lower()} a {s['b']}, Carnia", sizes)}<span class="tag">{beds(s['beds'])}</span>{badge}</div>
      <div class="card-body">
        <div><h3>{e(s['n'])}</h3><div class="where">{I('pin')}{s['b']} · {s['label']}</div>{f"<p>{e(s['short'])}</p>" if feature else ""}</div>
        <span class="arrow" aria-hidden="true">{I('arrow')}</span>
      </div>
    </a>"""


def filters_block():
    borghi = sorted({s["b"] for s in STAYS}, key=lambda b: [v["n"] for v in VILLAGES].index(b))
    chips = "".join(f'<button class="chip" data-f="borgo" data-v="{b}" aria-pressed="false">{b}</button>' for b in borghi)
    return f"""<div class="filters rv" role="group" aria-label="Filtra le residenze">
          <button class="chip" data-f="borgo" data-v="all" aria-pressed="true">Tutti i borghi</button>{chips}
          <span class="sep"></span>
          <button class="chip" data-f="size" data-v="all" aria-pressed="true">Ogni capienza</button>
          <button class="chip" data-f="size" data-v="s" aria-pressed="false">2–8 posti</button>
          <button class="chip" data-f="size" data-v="m" aria-pressed="false">9–16 posti</button>
          <button class="chip" data-f="size" data-v="l" aria-pressed="false">Oltre 16</button>
          <span class="count" aria-live="polite" data-count></span>
        </div>
        <p class="count-m" data-count-m aria-hidden="true"></p>
        <div class="grid" data-grid>{"".join(card(s, s.get('feature', False)) for s in STAYS)}</div>
        <p class="swipe-hint" aria-hidden="true">Scorri per vedere tutte le case {I('right')}</p>
        <div class="empty" data-empty>Nessuna casa con questi filtri. Prova un altro borgo o un'altra capienza.</div>"""


def book_strip():
    return f"""<div class="book-strip rv">
          <div><strong>Date, prezzi e disponibilità in tempo reale</strong><p>Prenoti direttamente sul sistema ufficiale Col Gentile, senza intermediari.</p></div>
          <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">Verifica disponibilità {I('arrow')}</a>
        </div>"""


def aside(title, extra=""):
    return f"""<aside class="aside rv">
      <h2 style="font-size:30px;line-height:1.1;margin:0">{e(title)}</h2>
      <p>Date, prezzi e disponibilità in tempo reale sul sistema ufficiale di prenotazione Col Gentile.</p>
      <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">Verifica disponibilità {I('arrow')}</a>
      <a class="btn btn-ghost" href="mailto:{SITE['email']}?subject={e('Richiesta informazioni: ' + title)}">Scrivici</a>
      <a class="btn btn-ghost" href="tel:{SITE['phone_href']}">{SITE['phone']}</a>
      {extra}
    </aside>"""


def gallery(names, label, max_shown=7):
    urls = [img_url(n, 1600) for n in names]
    items = []
    for i, n in enumerate(names[:max_shown]):
        more = f'<span class="more">+{len(names) - max_shown + 1}</span>' if i == max_shown - 1 and len(names) > max_shown else ""
        sz = "(max-width:640px) 100vw, 40vw" if i == 0 else "(max-width:640px) 50vw, 20vw"
        items.append(f'<button data-open-lb="{i}" aria-label="Apri foto {i + 1} di {len(names)}">{pic(n, f"{label}, foto {i + 1}", sz)}{more}</button>')
    return f"""<div class="gal" data-gallery='{json.dumps(urls)}'>{"".join(items)}</div>"""


def tour(s):
    panos = [PANO[p] for p in s.get("pano", []) if p in PANO]
    if not panos: return ""
    thumbs = "".join(f'<button aria-pressed="{str(i == 0).lower()}" aria-label="Ambiente {i + 1}"><img loading="lazy" src="{p["thumb"]}" alt=""></button>' for i, p in enumerate(panos))
    return f"""<div class="rv" id="tour-360"><span class="eyebrow">Tour virtuale</span><h2>Entra in casa, a 360°</h2>
      <div class="tour" data-tour='{json.dumps([p["src"] for p in panos])}'>
        <div class="tour-stage"><img src="{panos[0]['thumb']}" alt="Anteprima del tour virtuale di {e(s['n'])}" loading="lazy">
          <button class="tour-start" aria-label="Avvia il tour virtuale a 360 gradi"><div><b><i>360°</i> Avvia il tour</b><span>{len(panos)} ambienti da esplorare · trascina per guardarti intorno</span></div></button>
        </div>
        {f'<div class="tour-thumbs">{thumbs}</div>' if len(panos) > 1 else ""}
      </div></div>"""


def mini_stay(s):
    return f'<a class="mini" href="{stay_url(s)}">{pic(s["card"], s["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{e(s["n"])}</b><span>{s["b"]} · {beds(s["beds"])}</span></div></a>'


def mini_vill(v):
    return f'<a class="mini" href="{vill_url(v)}">{pic(v["card"], "Il borgo di " + v["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{e(v["n"])}</b><span>{v["f"]["q"] + " m s.l.m." if v["f"] else "Frazione di Socchieve"}</span></div></a>'


def hero(img, alt, crumbs, h1, sub="", pills=()):
    nav = "".join(f'<a href="{p}">{e(n)}</a><span>/</span>' for n, p in crumbs[:-1]) + f"<b>{e(crumbs[-1][0])}</b>"
    pl = "".join(f'<span class="pill">{x}</span>' for x in pills)
    return f"""<section class="ph">
  {pic(img, alt, "100vw", eager=True)}
  <div class="wrap">
    <nav class="crumbs" aria-label="Percorso">{nav}</nav>
    <h1>{h1}</h1>
    {f'<p class="lead">{sub}</p>' if sub else ""}
    {f'<div class="ph-meta">{pl}</div>' if pl else ""}
  </div>
</section>"""


def preload_for(name):
    m = PH.get(name)
    if not m: return None
    return (img_url(name, 960), ", ".join(f"/img/{m['slug']}-{x}.webp {x}w" for x in m["widths"]))


# ---------------------------------------------------------------- pagine
def build_stay(s):
    v = VILL_BY_NAME[s["b"]]
    parent = STAY.get(s.get("parent"))
    siblings = [STAY[u] for u in parent["units"] if u != s["id"]] if parent else []
    related = (siblings or [x for x in STAYS if x["id"] != s["id"] and x["b"] == s["b"]])
    related = (related + [x for x in top_stays() if x["id"] != s["id"] and x not in related])[:4]
    cins = [s["cin"]] if s.get("cin") else [STAY[u]["cin"] for u in s.get("units", []) if STAY[u].get("cin")]
    crumbs = [("Home", "/"), ("Le case", "/it/alloggi/")] + ([(parent["n"], stay_url(parent))] if parent else []) + [(s["n"], stay_url(s))]
    pills = [f"{I('pin')}{s['b']}, Socchieve", beds(s["beds"]), f"{s['stars']} stelle"] + (["Tour 360°"] if s.get("pano") else [])
    units = ""
    if s.get("units"):
        units = '<div class="rv"><span class="eyebrow">Gli appartamenti</span><h2>Prenota tutta la casa o un solo appartamento</h2><div class="units">' + "".join(
            f'<a class="unit" href="{stay_url(STAY[u])}">{pic(STAY[u]["g"][0], STAY[u]["n"], "96px")}<div><b>{e(STAY[u]["n"])}</b><span>{beds(STAY[u]["beds"])} · {STAY[u]["stars"]} stelle</span></div></a>'
            for u in s["units"]) + "</div></div>"
    plan = ""
    if s.get("plan"):
        plan = f"""<div class="rv"><span class="eyebrow">Planimetria</span><div class="plan" style="margin-top:20px" data-gallery='{json.dumps([img_url(s["plan"])])}'>{pic(s["plan"], "Planimetria di " + s["n"], "(max-width:980px) 100vw, 60vw", attrs='data-open-lb="0"')}</div></div>"""
    am = f'<div class="rv"><span class="eyebrow">Servizi</span><ul class="amen" style="margin-top:20px">{"".join(f"<li>{a}</li>" for a in s["am"])}</ul></div>' if s.get("am") else ""
    bedrooms = s.get("bedrooms")
    if s.get("units"): rooms_v, rooms_l = len(s["units"]), "Appartamenti"
    elif bedrooms == 0: rooms_v, rooms_l = 1, "Ambiente unico"
    elif bedrooms: rooms_v, rooms_l = bedrooms, "Camere" if bedrooms > 1 else "Camera"
    else: rooms_v, rooms_l = "—", "Camere"
    body = f"""{hero(s['g'][0], f"{s['n']} a {s['b']}, Carnia", crumbs, e(s['n']), pills=pills)}
<section class="d-body">
  <div class="wrap d-grid">
    <div class="d-main">
      <div class="rv">
        <span class="eyebrow">{s['label']} a {s['b']} · Carnia</span>
        <h2>{e(s['short'])}</h2>
        {"".join(f'<p{" class=\"prose-first\"" if i == 0 else ""}>{e(p)}</p>' for i, p in enumerate(s['text']))}
      </div>
      <div class="facts rv">
        <div><b>{s['beds']}</b><span>Posti letto</span></div>
        <div><b>{s['stars']}★</b><span>Classificazione</span></div>
        <div><b>{rooms_v}</b><span>{rooms_l}</span></div>
        <div><b>{v['f']['q'] if v['f'] else '—'}</b><span>m s.l.m.</span></div>
      </div>
      {am}
      <div class="rv"><span class="eyebrow">Foto</span><h2>{len(s['g'])} foto di {e(s['n'])}</h2>{gallery(s['g'], s['n'])}</div>
      {tour(s)}
      {units}
      {plan}
      <div class="rv">
        <span class="eyebrow">Il borgo</span>
        <h2>{s['b']}, frazione di Socchieve</h2>
        <p>{e(clip(v['t'], 300))}</p>
        <p style="margin-top:20px"><a class="link" href="{vill_url(v)}">Scopri {s['b']}: sentieri, locali e cosa fare {I('arrow')}</a></p>
      </div>
      {f'<p class="cin rv">Codice identificativo nazionale (CIN): {" · ".join(cins)}</p>' if cins else ""}
    </div>
    {aside(s['n'], f"<dl><dt>Indirizzo</dt><dd>{e(s['addr'])}</dd><dt>Comune</dt><dd>Socchieve (UD)</dd><dt>Ospiti</dt><dd>fino a {s['beds']}</dd><dt>Categoria</dt><dd>{s['label']} {s['stars']}★</dd></dl>")}
  </div>
</section>
<section class="related"><div class="wrap"><span class="eyebrow">{"Nella stessa casa" if siblings else "Potrebbero piacerti"}</span><h2>Altre case dell'albergo diffuso</h2><div class="mini-rail">{"".join(mini_stay(x) for x in related)}</div></div></section>"""

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
    if "Animali ammessi" in s.get("am", []): ld_stay["petsAllowed"] = True
    if s.get("cin"): ld_stay["identifier"] = {"@type": "PropertyValue", "propertyID": "CIN", "value": s["cin"]}
    if s.get("units"): ld_stay["containsPlace"] = [{"@id": U + stay_url(STAY[u]) + "#accommodation"} for u in s["units"]]
    title = f"{s['n']} a {s['b']} · {s['label']} fino a {s['beds']} ospiti in Carnia"
    desc = clip(f"{s['short']} {s['stars']} stelle, {s['b']} (Socchieve, Carnia). {len(s['g'])} foto{', tour virtuale 360°' if s.get('pano') else ''} e prenotazione diretta.", 160)
    page(stay_url(s), title, desc, body, active="alloggi", image=s["g"][0], og_type="place", preload=preload_for(s["g"][0]),
         ld=[ld_stay, crumbs_ld(crumbs)], images=[abs_img(g) for g in s["g"]])


def build_village(v):
    here = stays_in(v["n"])
    near = stays_in(v["near"]) if v.get("near") else []
    crumbs = [("Home", "/"), ("Il territorio", "/it/territorio"), (v["n"], vill_url(v))]
    trek = {r["n"].split(" ·")[0]: r for r in EXPS["trekking"]["routes"]}
    def sent(n):
        return f'<a href="/it/trekking">{e(n)}{I("arrow")}</a>' if n.split(" ·")[0] in trek else e(n)
    lists = "".join(f'<div><h3 style="font:600 12px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--moss);margin-bottom:14px">{t}</h3><ul>{"".join(f"<li>{f(i)}</li>" for i in items)}</ul></div>'
                    for t, items, f in (("Sentieri dal paese", v["sentieri"], sent), ("Dove mangiare e bere", v["locali"], e), ("Servizi in paese", v.get("servizi", []), e)) if items)
    stays_block = ""
    if here or near:
        lst = here or near
        stays_block = f'<div class="rv"><span class="eyebrow">{"Dove dormire a " + v["n"] if here else "Le case più vicine, a " + v["near"]}</span><h2>Le case dell\'albergo diffuso</h2><div class="units">' + "".join(
            f'<a class="unit" href="{stay_url(x)}">{pic(x["card"], x["n"], "96px")}<div><b>{e(x["n"])}</b><span>{beds(x["beds"])} · {x["label"]}</span></div></a>' for x in lst) + "</div></div>"
    facts = ""
    if v["f"]:
        f = v["f"]
        lo_style = "" if any(c.isdigit() for c in f["lo"]) else ' style="font-size:22px;line-height:1.4"'
        facts = f'<div class="facts rv"><div><b>{f["ab"]}</b><span>Abitanti</span></div><div><b>{f["q"]}</b><span>m s.l.m.</span></div><div><b>{f["se"]}</b><span>Sentieri</span></div><div><b{lo_style}>{f["lo"]}</b><span>Locali</span></div></div>'
    pills = [f"{v['f']['q']} m s.l.m.", f"{v['f']['ab']} abitanti"] if v["f"] else ["Frazione di Socchieve"]
    body = f"""{hero(v['hero'][0], f"Panorama di {v['n']}, Socchieve, Carnia", crumbs, e(v['n']), sub="Frazione di Socchieve, in Carnia", pills=pills)}
<section class="d-body">
  <div class="wrap d-grid">
    <div class="d-main">
      <div class="rv"><span class="eyebrow">Il borgo</span><h2>Cosa vedere e cosa fare a {v['n']}</h2><p class="prose-first">{e(v['t'])}</p></div>
      {facts}
      {f'<div class="rv"><span class="eyebrow">Panorami</span><h2>{v["n"]} in foto</h2>{gallery(v["hero"], v["n"])}</div>' if len(v['hero']) > 1 else ""}
      <div class="list2 rv">{lists}</div>
      {stays_block}
    </div>
    {aside("Dormire a " + v['n'] if here else "Soggiorna a Socchieve")}
  </div>
</section>
<section class="related"><div class="wrap"><span class="eyebrow">Socchieve e i suoi paesi</span><h2>Gli altri borghi</h2><div class="mini-rail">{"".join(mini_vill(x) for x in VILLAGES if x['id'] != v['id'])}</div></div></section>"""
    ld = {"@context": "https://schema.org", "@type": "TouristDestination", "@id": U + vill_url(v) + "#place", "name": f"{v['n']} (Socchieve)",
          "description": v["t"], "url": U + vill_url(v), "image": [abs_img(h) for h in v["hero"] if h in PH],
          "geo": {"@type": "GeoCoordinates", "latitude": v["geo"][0], "longitude": v["geo"][1]},
          "containedInPlace": {"@type": "AdministrativeArea", "name": "Socchieve, Carnia, Friuli Venezia Giulia"}}
    if here: ld["containsPlace"] = [{"@id": U + stay_url(x) + "#accommodation"} for x in here]
    title = f"{v['n']}, Socchieve: cosa vedere, sentieri e dove dormire"
    desc = clip(f"{v['n']}, frazione di Socchieve in Carnia{', a ' + v['f']['q'] + ' m' if v['f'] else ''}: {v['t']}", 160)
    page(vill_url(v), title, desc, body, active="borghi", image=v["hero"][0], preload=preload_for(v["hero"][0]),
         ld=[ld, crumbs_ld(crumbs)], images=[abs_img(h) for h in v["hero"] if h in PH])


def build_exp(k, x):
    crumbs = [("Home", "/"), ("Il territorio", "/it/territorio"), (x["n"], exp_url(k))]
    routes = ""
    if x.get("routes"):
        routes = '<div class="rv"><span class="eyebrow">Gli itinerari</span><div style="margin-top:20px">' + "".join(f"""
        <article class="route" id="{k}-{i + 1}"><span class="n">{i + 1:02d}</span><div>
          <h3>{e(r['n'])}</h3><p>{e(r['t'])}</p>
          {f'<div class="stats-inline">{"".join(f"<span>{s}</span>" for s in r["stats"])}</div>' if r.get('stats') else ""}
          <p style="margin-top:14px;font-size:14px">Borghi: {", ".join(f'<a class="link" style="border:0;padding:0" href="{vill_url(VILL[b])}">{VILL[b]["n"]}</a>' for b in r.get('via', []))}</p>
          {f'<figure data-gallery=\'{json.dumps([img_url(r["map"])])}\'>{pic(r["map"], "Mappa del percorso " + r["n"], "(max-width:980px) 100vw, 60vw", attrs="data-open-lb=\"0\"")}</figure>' if r.get('map') else ""}
        </div></article>""" for i, r in enumerate(x["routes"])) + "</div></div>"
    items = ""
    if x.get("items"):
        items = "<div>" + "".join(f"""
        <article class="feature-row rv" data-gallery='{json.dumps([img_url(it["img"])])}'>{pic(it['img'], it['n'], "(max-width:640px) 100vw, 40vw", attrs='data-open-lb="0"')}<div><span class="eyebrow">{x['n']}</span><h3>{e(it['n'])}</h3>{"".join(f"<p>{e(p)}</p>" for p in it['t'])}</div></article>""" for it in x["items"]) + "</div>"
    more = ""
    if x.get("more"):
        more = '<div class="rv"><span class="eyebrow">Altri itinerari in zona</span><div class="list2" style="margin-top:20px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr))">' + "".join(
            f'<div><h3 style="font:600 12px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--moss);margin-bottom:14px">{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in l)}</ul></div>' for t, l in x["more"]) + "</div></div>"
    others = [(kk, xx) for kk, xx in EXPS.items() if kk != k]
    body = f"""{hero(x['hero'], x['n'] + " a Socchieve, Carnia", crumbs, e(x['n']), sub=e(x['lead']))}
<section class="d-body">
  <div class="wrap d-grid">
    <div class="d-main">
      <div class="rv">{"".join(f'<p{" class=\"prose-first\"" if i == 0 else ""}>{e(p)}</p>' for i, p in enumerate(x['intro']))}</div>
      {routes}{items}{more}
      {f'<p class="cin rv">{e(x["note"])}</p>' if x.get('note') else ""}
    </div>
    {aside("Parti da Socchieve")}
  </div>
</section>
<section class="related"><div class="wrap"><span class="eyebrow">Cosa fare a Socchieve</span><h2>Altre esperienze</h2><div class="mini-rail">{"".join(f'<a class="mini" href="{exp_url(kk)}">{pic(xx["hero"], xx["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{xx["n"]}</b><span>{e(xx["lead"].split(":")[0].split(",")[0])}</span></div></a>' for kk, xx in others)}<a class="mini" href="/it/benessere">{pic("PanoramaNonta1.jpg", "Benessere a Socchieve", "(max-width:640px) 70vw, 25vw")}<div><b>Benessere</b><span>Sauna e bagno di bosco</span></div></a></div></div></section>"""
    if x.get("routes"):
        ld = {"@context": "https://schema.org", "@type": "TouristTrip", "name": f"{x['n']} a Socchieve", "description": x["desc"], "url": U + exp_url(k),
              "touristType": ["Escursionisti" if k == "trekking" else "Ciclisti"],
              "itinerary": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "TouristAttraction", "name": r["n"], "description": r["t"], "url": f"{U}{exp_url(k)}#{k}-{i + 1}"}} for i, r in enumerate(x["routes"])]},
              "provider": {"@id": LODGING_ID}}
    else:
        ld = {"@context": "https://schema.org", "@type": "ItemList", "name": x["n"], "url": U + exp_url(k), "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "TouristAttraction", "name": it["n"], "description": " ".join(it["t"]), "image": abs_img(it["img"])}} for i, it in enumerate(x["items"])]}
    imgs = [abs_img(x["hero"])] + [abs_img(r["map"]) for r in x.get("routes", []) if r.get("map") in PH] + [abs_img(i["img"]) for i in x.get("items", []) if i["img"] in PH]
    page(exp_url(k), x["title"], x["desc"], body, active="esperienze", image=x["hero"], preload=preload_for(x["hero"]), ld=[ld, crumbs_ld(crumbs)], images=imgs)


def lodging_ld():
    return {"@context": "https://schema.org", "@type": "LodgingBusiness", "@id": LODGING_ID,
            "name": "Albergo Diffuso Socchieve “Col Gentile”", "alternateName": ["Albergo Diffuso Socchieve", "Col Gentile"],
            "description": "Albergo diffuso con case e appartamenti vacanza nei borghi di Socchieve, in Carnia (Friuli Venezia Giulia), alla porta delle Dolomiti Friulane.",
            "url": U + "/", "logo": U + "/apple-touch-icon.png", "image": [og_img("Slide1Socchieve.jpg"), abs_img("Casa-Vanda-esterno.jpg")],
            "telephone": SITE["phone"], "email": SITE["email"], "vatID": "IT" + SITE["vat"],
            "address": address(SITE["street"], SITE["locality"]),
            "geo": {"@type": "GeoCoordinates", "latitude": SITE["geo"][0], "longitude": SITE["geo"][1]},
            "hasMap": f"https://www.google.com/maps/search/?api=1&query={SITE['geo'][0]},{SITE['geo'][1]}",
            "areaServed": "Carnia", "knowsLanguage": ["it", "en", "fr"], "petsAllowed": True,
            "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in ("Wi-Fi", "Parcheggio", "Giardino", "Animali ammessi")],
            "containsPlace": [{"@id": U + stay_url(s) + "#accommodation"} for s in STAYS],
            "potentialAction": {"@type": "ReserveAction", "target": SITE["booking"]},
            "memberOf": {"@type": "Organization", "name": "Borghi Autentici d'Italia"}}


def build_home():
    villages = "".join(f"""<a class="village" href="{vill_url(v)}">{pic(v['card'], 'Il borgo di ' + v['n'], '(max-width:640px) 72vw, 340px')}<small>{v['f']['q'] + ' m s.l.m.' if v['f'] else 'Socchieve'}</small><strong>{v['n']}{I('arrow')}</strong></a>""" for v in VILLAGES)
    marquee = "".join(f"<span>{v['n']}</span>" for v in VILLAGES) * 2
    dist = "".join(f"<li><b>{e(n)}</b><span>{km} km · circa {t}</span></li>" for n, km, t in DISTANCES)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    n_stays = len(STAYS)
    body = f"""<section class="hero">
      <div class="hero-media">{pic("Slide1Socchieve.jpg", "Strada tra i prati verso le montagne della Carnia, a Socchieve", "100vw", eager=True)}</div>
      <div class="wrap hero-in">
        <h1><span class="eyebrow light" style="display:flex;margin-bottom:22px">Albergo diffuso a Socchieve · Carnia</span>Vivi la Carnia <em>da paesano.</em></h1>
        <div class="hero-row">
          <p>Case e appartamenti vacanza nei borghi di Socchieve, con i servizi di un albergo. A 18 km da Sauris e mezz'ora dalle Dolomiti Friulane.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">Verifica disponibilità {I('arrow')}</a>
            <a class="btn btn-ghost" href="/it/alloggi/">Scopri le case</a>
          </div>
        </div>
        <div class="hero-meta"><span><b>{n_stays}</b> alloggi</span><span><b>8</b> borghi</span><span>Dolomiti Friulane · <b>Patrimonio UNESCO</b></span></div>
      </div>
      <span class="scroll-cue" aria-hidden="true">Scorri</span>
    </section>
    <div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

    <section class="sec" id="albergo-diffuso">
      <div class="wrap intro-grid">
        <div>
          <span class="eyebrow rv">Cos'è un albergo diffuso</span>
          <h2 class="statement rv d1">Non un hotel con tante stanze. <em>Un paese intero</em> che ti apre le sue case.</h2>
          <p class="intro-copy rv d2">L'albergo diffuso offre i servizi di una struttura alberghiera dentro un territorio abitato. A Socchieve dormi in una casa vera del borgo, prendi il caffè con chi ci vive ed esci a piedi sui sentieri della Carnia. Turista e paesano, nello stesso viaggio.</p>
          <div class="stats rv d3"><div><b>{n_stays}</b><span>case e appartamenti</span></div><div><b>8</b><span>borghi del comune</span></div><div><b>2–21</b><span>posti letto per casa</span></div></div>
        </div>
        <div class="intro-media rv d2">
          {pic("Slide2Socchieve.jpg", "Albero e panchina in un prato di montagna a Socchieve", "(max-width:820px) 80vw, 40vw", cls="a")}
          {pic("Casa-Vanda-esterno.jpg", "Casa Vanda a Viaso, villa settecentesca con ballatoi in legno", "(max-width:820px) 40vw, 20vw", cls="b")}
          <div class="badge" aria-hidden="true"><svg viewBox="0 0 100 100"><defs><path id="circ" d="M50 50m-38 0a38 38 0 1 1 76 0a38 38 0 1 1-76 0"/></defs><text font-size="8.6" fill="#fff" font-family="Inter Tight, sans-serif" font-weight="600"><textPath href="#circ" textLength="236" lengthAdjust="spacing">OSPITI DELLA NATURA · OSPITI DELLA NATURA · </textPath></text></svg><i>Carnia</i></div>
        </div>
      </div>
    </section>

    <section class="sec stays" id="alloggi">
      <div class="wrap">
        <div class="sec-head">
          <div><span class="eyebrow rv">Dove dormire in Carnia</span><h2 class="rv d1">Scegli la tua <em>casa nel borgo.</em></h2></div>
          <p class="rv d2">Dal monolocale per due alla villa per gruppi fino a 21 persone. Filtra per borgo o per numero di posti letto.</p>
        </div>
        {filters_block()}
        {book_strip()}
      </div>
    </section>

    <section class="sec villages on-dark" id="borghi">
      <div class="wrap sec-head">
        <div><span class="eyebrow rv">Socchieve e i suoi paesi</span><h2 class="rv d1">Otto borghi, <em>un'unica valle.</em></h2></div>
        <div class="rail-ctrl"><button data-rail="-1" aria-label="Borghi precedenti"><svg><use href="#i-left"/></svg></button><button data-rail="1" aria-label="Borghi successivi"><svg><use href="#i-right"/></svg></button></div>
      </div>
      <div class="rail" data-railbox>{villages}</div>
    </section>

    <section class="sec" id="esperienze">
      <div class="wrap">
        <div class="sec-head">
          <div><span class="eyebrow rv">Cosa fare a Socchieve</span><h2 class="rv d1">Prenditi <em>il tempo.</em></h2></div>
          <p class="rv d2">Passeggiate ed escursioni, bici, arte romanica e i grandi classici della Carnia. Si parte direttamente dalle nostre case.</p>
        </div>
        <div class="bento">
          <a class="tile big rv" href="/it/trekking">{pic("Slide1Socchieve.jpg", "Sentiero tra prati e boschi in Carnia", "(max-width:640px) 100vw, 50vw")}<span class="num">01</span><h3>Trekking</h3><p>Quattro anelli che partono dai borghi e la traversata del Col Gentile sul sentiero CAI 235.</p><span class="link">Scopri i percorsi {I('arrow')}</span></a>
          <a class="tile green rv d1" href="/it/cicloturismo"><span class="num">02</span><h3>Cicloturismo</h3><p>La pista MTB di Mediis e l'anello del Passo Rest, con lo Zoncolan a 24 km.</p><span class="link">Approfondisci {I('arrow')}</span></a>
          <a class="tile rv d2" href="/it/arte-e-cultura">{pic("Slide3Socchieve.jpg", "Antica meridiana dipinta su un muro in pietra a Socchieve", "(max-width:640px) 100vw, 25vw")}<span class="num">03</span><h3>Arte e cultura</h3><span class="link">Approfondisci {I('arrow')}</span></a>
          <a class="tile wide plain rv d1" href="/it/visita-la-carnia"><span class="num">04</span><h3>Visita la Carnia</h3><p>Sauris e il suo prosciutto, la Forra del Lumiei, Forni di Sopra e la Val Pesarina: tutto a meno di un'ora.</p><span class="link">Approfondisci {I('arrow')}</span></a>
        </div>
      </div>
    </section>

    <section class="sec" id="benessere" style="background:var(--bone)">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow rv">Benessere</span><h2 class="rv d1">Sauna e <em>bagno di bosco.</em></h2></div>
        <p class="rv d2">Il calore della sauna dopo i sentieri e lo Shinrin-yoku con Petra nei boschi di Socchieve.</p></div>
        <div class="bento">{"".join(svc_card(s) for s in data.SERVICES)}</div>
      </div>
    </section>

    <section class="sec loc" id="dove">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow rv">Dov'è Socchieve</span><h2 class="rv d1">Al centro della Carnia, <em>vicino a tutto.</em></h2></div>
        <p class="rv d2">Tra le Dolomiti Friulane e le Pesarine, lungo la SS52 che unisce Tolmezzo a Forni di Sopra. Distanze in auto dalla reception di Mediis.</p></div>
        <ul class="dist rv">{dist}</ul>
        <p style="margin-top:28px" class="rv"><a class="link" href="/it/contact">Come arrivare e contatti {I('arrow')}</a></p>
      </div>
    </section>

    <section class="farie-teaser">
      {pic("LungisCartolina.jpg", "Il borgo di Lungis", "100vw")}
      <div class="wrap">
        <span class="eyebrow light rv">Bed &amp; Breakfast a Lungis · {data.FARIE['rating']}/10 su Booking.com</span>
        <h2 class="rv d1">La Farie.</h2>
        <p class="rv d2">Una casa carnica ristrutturata, la colazione che gli ospiti non dimenticano e l'accoglienza di {data.FARIE['hosts']}: {data.FARIE['reviews']} recensioni, voto {data.FARIE['rating']}.</p>
        <a class="btn btn-light rv d3" href="/la-farie">Scopri La Farie {I('arrow')}</a>
      </div>
    </section>

    <section class="sec" id="domande">
      <div class="wrap">
        <div class="sec-head"><div><span class="eyebrow rv">Domande frequenti</span><h2 class="rv d1">Prima di <em>partire.</em></h2></div></div>
        <div class="faq rv">{faq}</div>
      </div>
    </section>

    <section class="cta">
      <div class="wrap">
        <span class="eyebrow rv">Una vacanza diversa</span>
        <h2 class="rv d1">La montagna, <em>tra le persone.</em></h2>
        <p class="rv d2">Lasciati affascinare dal vivere in montagna tra la gente e la natura della Carnia.</p>
        <div class="row rv d3">
          <a class="btn btn-primary" href="{SITE['booking']}" target="_blank" rel="noopener">Prenota il soggiorno {I('arrow')}</a>
          <a class="btn btn-dark" href="#scrivici">Scrivici</a>
        </div>
      </div>
    </section>"""
    website = {"@context": "https://schema.org", "@type": "WebSite", "@id": U + "/#website", "name": SITE["name"], "url": U + "/", "inLanguage": "it-IT", "publisher": {"@id": LODGING_ID}}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    page("/", "Albergo Diffuso Socchieve · Case vacanza in Carnia e Dolomiti",
         f"Case e appartamenti vacanza nei borghi di Socchieve, in Carnia: {n_stays} alloggi da 2 a 21 posti, a 18 km da Sauris e 30 minuti dalle Dolomiti Friulane. Prenotazione diretta.",
         body, image="Slide1Socchieve.jpg", preload=preload_for("Slide1Socchieve.jpg"), ld=[lodging_ld(), website, faq_ld],
         images=[og_img("Slide1Socchieve.jpg")] + [abs_img(s["card"]) for s in STAYS])


def build_catalog():
    crumbs = [("Home", "/"), ("Le case", "/it/alloggi/")]
    body = f"""{hero("Casa-Vanda-esterno.jpg", "Case vacanza dell'albergo diffuso di Socchieve", crumbs, "Case vacanza <em>in Carnia</em>", sub=f"{len(STAYS)} case e appartamenti nei borghi di Socchieve, dal monolocale per due alla villa per gruppi. Prenotazione diretta, senza intermediari.")}
<section class="sec stays">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow rv">Tutti gli alloggi</span><h2 class="rv d1">Trova la casa <em>giusta per te.</em></h2></div>
    <p class="rv d2">Appartamenti per coppie e famiglie, case intere per gruppi: tutte arredate, con cucina, e a pochi passi dai sentieri.</p></div>
    {filters_block()}
    {book_strip()}
  </div>
</section>"""
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Case vacanza dell'Albergo Diffuso Socchieve", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": U + stay_url(s), "name": s["n"]} for i, s in enumerate(STAYS)]}
    page("/it/alloggi/", f"Case vacanza e appartamenti in Carnia · {len(STAYS)} alloggi a Socchieve",
         f"{len(STAYS)} case vacanza e appartamenti nei borghi di Socchieve, in Carnia: da 2 a 21 posti letto, 3 e 4 stelle, alcuni con tour 360° e animali ammessi. Prenota direttamente.",
         body, active="alloggi", image="Casa-Vanda-esterno.jpg", preload=preload_for("Casa-Vanda-esterno.jpg"), ld=[items, crumbs_ld(crumbs)],
         images=[abs_img(s["card"]) for s in STAYS])


def build_territorio():
    crumbs = [("Home", "/"), ("Il territorio", "/it/territorio")]
    vgrid = "".join(mini_vill(v) for v in VILLAGES)
    egrid = "".join(f'<a class="mini" href="{exp_url(k)}">{pic(x["hero"], x["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{x["n"]}</b><span>{e(clip(x["lead"], 70))}</span></div></a>' for k, x in EXPS.items())
    body = f"""{hero("Panoramica-feltrone-montagne.jpg", "Montagne della Carnia sopra Feltrone", crumbs, "Socchieve <em>e la Carnia</em>", sub="Otto borghi tra le Dolomiti Friulane e le Pesarine, sentieri fuori dalla porta e i grandi classici della Carnia a meno di un'ora.")}
<section class="sec" id="borghi"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">Socchieve e i suoi paesi</span><h2 class="rv d1">Otto borghi, <em>un'unica valle.</em></h2></div><p class="rv d2">Ogni frazione ha il suo carattere, i suoi sentieri e le sue osterie. Scopri dove dormire e cosa fare in ciascuna.</p></div>
  <div class="mini-rail" style="grid-template-columns:repeat(4,1fr)">{vgrid}</div>
</div></section>
<section class="sec" id="esperienze" style="background:var(--bone)"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">Cosa fare a Socchieve</span><h2 class="rv d1">Prenditi <em>il tempo.</em></h2></div></div>
  <div class="mini-rail">{egrid}</div>
</div></section>
<section class="sec" id="distanze"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">Distanze</span><h2 class="rv d1">Il campo base <em>per la Carnia.</em></h2></div></div>
  <ul class="dist rv">{"".join(f"<li><b>{e(n)}</b><span>{km} km · circa {t}</span></li>" for n, km, t in DISTANCES)}</ul>
</div></section>"""
    page("/it/territorio", "Socchieve e i suoi borghi: cosa fare in Carnia",
         "Gli otto borghi di Socchieve, i sentieri, la mountain bike, l'arte romanica e le mete della Carnia vicine: Sauris, Forni di Sopra, Ampezzo e la Val Pesarina.",
         body, active="borghi", image="Panoramica-feltrone-montagne.jpg", preload=preload_for("Panoramica-feltrone-montagne.jpg"), ld=[crumbs_ld(crumbs)])


def build_contact():
    crumbs = [("Home", "/"), ("Contatti", "/it/contact")]
    lat, lon = SITE["geo"]
    body = f"""{hero("Mediispanoramica.jpg", "Panorama di Mediis, sede della reception", crumbs, "Contatti <em>e come arrivare</em>", sub="La reception è a Mediis, in Via Roma 20. Scrivici o chiamaci per qualsiasi informazione sul soggiorno.")}
<section class="d-body"><div class="wrap">
  <div class="contact-cards rv">
    <a href="tel:{SITE['phone_href']}"><span>Telefono</span><b>{SITE['phone']}</b></a>
    <a href="tel:{SITE['mobile_href']}"><span>Cellulare</span><b>{SITE['mobile']}</b></a>
    <a href="mailto:{SITE['email']}"><span>Email</span><b>{SITE['email']}</b></a>
  </div>
  <div class="loc-grid" style="margin-top:clamp(48px,6vw,80px)">
    <div>
      <span class="eyebrow rv">Come arrivare</span>
      <h2 class="rv d1" style="font-size:clamp(34px,4vw,56px);line-height:1;margin:18px 0 22px">Tra le Dolomiti Friulane <em>e le Pesarine.</em></h2>
      <p class="rv">Socchieve è nell'Alto Friuli, in Carnia, lungo la valle che unisce Villa Santina a Forni di Sotto.</p>
      <div class="routes rv">
        <div><b>Autostrada A23</b><span>Uscita Carnia, poi SS52 verso Tolmezzo e Forni di Sopra (27 km dal casello)</span></div>
        <div><b>Dal Cadore</b><span>SS52 da Forni di Sopra (26 km)</span></div>
        <div><b>Da Pordenone</b><span>SS552 del Monte Rest da Tramonti di Sopra</span></div>
        <div><b>Dalla Val d'Arzino</b><span>Strada comunale di Preone</span></div>
        <div><b>In aereo</b><span>Aeroporto di Trieste (103 km), Venezia Marco Polo (circa 2 h 30)</span></div>
        <div><b>In treno</b><span>Stazione Carnia, poi autobus SAF (fermata a Mediis, Bar alla Posta)</span></div>
      </div>
      <a class="btn btn-dark rv" href="https://www.google.com/maps/dir/?api=1&destination={lat},{lon}" target="_blank" rel="noopener">Indicazioni stradali {I('arrow')}</a>
    </div>
    <div class="mapcard rv d2">
      <iframe title="Mappa della reception a Mediis, Socchieve" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox={lon - 0.06}%2C{lat - 0.03}%2C{lon + 0.06}%2C{lat + 0.03}&amp;layer=mapnik&amp;marker={lat}%2C{lon}"></iframe>
      <div class="pin"><div><b>Reception · Mediis</b><span>{SITE['street']}, {SITE['zip']} Socchieve (UD)</span></div><a class="arrow" href="tel:{SITE['phone_href']}" aria-label="Chiama la reception"><svg><use href="#i-arrow"/></svg></a></div>
    </div>
  </div>
  <div class="rv" style="margin-top:clamp(48px,6vw,80px)"><span class="eyebrow">Distanze dalla reception</span><ul class="dist" style="margin-top:20px">{"".join(f"<li><b>{e(n)}</b><span>{km} km · circa {t}</span></li>" for n, km, t in DISTANCES)}</ul></div>
</div></section>"""
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contatti", "url": U + "/it/contact", "about": {"@id": LODGING_ID}}
    page("/it/contact", "Contatti e come arrivare · Albergo Diffuso Socchieve",
         "Reception a Mediis (Socchieve, UD), tel. +39 0433 819934, info@albergodiffusosocchieve.it. Come arrivare in Carnia da A23, Cadore, Pordenone e aeroporto di Trieste.",
         body, active="contatti", image="Mediispanoramica.jpg", preload=preload_for("Mediispanoramica.jpg"), ld=[ld, lodging_ld(), crumbs_ld(crumbs)])


def build_farie():
    F = data.FARIE
    mail = f"mailto:{SITE['email']}?subject={e('Richiesta disponibilità La Farie')}"
    def wrap(body):
        return f"""<a class="skip" href="#main">Vai al contenuto</a>
<div id="farie">
<header class="hdr" data-hdr>
  <div class="wrap bar">
    <a href="/la-farie" class="logo" aria-label="La Farie, bed and breakfast a Lungis"><span><b>La Farie</b><small>Bed &amp; Breakfast · Lungis, Carnia</small></span></a>
    <nav class="menu" aria-label="La Farie"><a href="#farie-casa">La casa</a><a href="#farie-foto">Foto</a><a href="#farie-ospiti">Gli ospiti</a><a href="#farie-info">Info utili</a><a href="/">← Col Gentile</a></nav>
    <div class="hdr-cta"><a class="btn btn-primary" href="#scrivici">Chiedi disponibilità {I('arrow')}</a><button class="burger" aria-label="Apri menu" data-open><span></span></button></div>
  </div>
</header>
<div class="drawer" data-drawer aria-hidden="true" style="background:#2b1c14">
  <div class="drawer-top"><span class="logo"><span><b style="font-style:italic">La Farie</b></span></span><button class="close" data-close aria-label="Chiudi menu">×</button></div>
  <nav><a href="#farie-casa">La casa</a><a href="#farie-foto">Foto</a><a href="#farie-ospiti">Gli ospiti</a><a href="#farie-info">Info utili</a><a href="/">← Col Gentile</a></nav>
  <a class="btn btn-primary" href="#scrivici">Chiedi disponibilità {I('arrow')}</a>
</div>
<main id="main">{body}</main>
<footer class="foot"><div class="wrap"><div class="foot-bottom" style="margin-top:0;border:0;padding-top:0"><span>La Farie · Bed &amp; Breakfast · {F['addr']}, Lungis · 33020 Socchieve (UD)</span><span><a href="/">Albergo Diffuso Socchieve</a><a href="/privacy">Privacy</a></span></div></div></footer>
</div>"""
    scores = "".join(f'<div><b>{v}</b><span>{k}</span></div>' for k, v in F["scores"][:4])
    rules = "".join(f"<div><b>{k}</b><span>{v}</span></div>" for k, v in F["rules"])
    near = "".join(f"<li><b>{n}</b><span>{d}</span></li>" for n, d in F["near"])
    body = f"""<section class="hero" id="la-farie">
      <div class="hero-media">{pic(F['g'][0], "La Farie, bed and breakfast in una casa carnica a Lungis", "100vw", eager=True)}</div>
      <div class="wrap hero-in">
        <h1><span class="eyebrow light" style="display:flex;margin-bottom:22px">Bed &amp; Breakfast a Lungis · Carnia</span>La Farie. <em>Sentirsi a casa.</em></h1>
        <div class="hero-row">
          <p>Una casa tipica carnica ristrutturata, la colazione che tutti ricordano e due padroni di casa che ti fanno sentire in famiglia.</p>
          <div class="hero-actions"><a class="btn btn-primary" href="#scrivici">Chiedi disponibilità {I('arrow')}</a><a class="btn btn-ghost" href="#farie-foto">Guarda le foto</a></div>
        </div>
        <div class="hero-meta"><span><b>{F['rating']}</b>/10 su Booking.com</span><span><b>{F['reviews']}</b> recensioni</span><span>Colazione · Wi-Fi · <b>Parcheggio gratuito</b></span></div>
      </div>
    </section>
    <section class="sec" id="farie-casa"><div class="wrap fa-split">
      {pic(F['g'][1], "La Farie, Lungis", "(max-width:820px) 100vw, 50vw", cls="rv")}
      <div><span class="eyebrow rv">La casa</span><h2 class="rv d1">Una casa carnica, <em>la quiete di Lungis.</em></h2>
        {"".join(f'<p class="rv d2" style="margin-top:16px">{e(p)}</p>' for p in F['intro'])}
      </div></div></section>
    <section class="sec" id="farie-foto" style="padding-top:0"><div class="wrap">
      <span class="eyebrow rv">Foto</span><h2 class="rv d1" style="font-size:clamp(36px,4.6vw,64px);line-height:1;margin:16px 0 28px">{len(F['g'])} foto de <em>La Farie</em></h2>
      <div class="rv">{gallery(F['g'], "La Farie, bed and breakfast a Lungis", max_shown=9)}</div>
    </div></section>
    <section class="sec" id="farie-servizi" style="padding-top:0"><div class="wrap">
      <span class="eyebrow rv">Servizi</span><h2 class="rv d1" style="font-size:clamp(36px,4.6vw,64px);line-height:1;margin:16px 0 28px">Tutto quello <em>che serve.</em></h2>
      <ul class="amen rv">{"".join(f"<li>{a}</li>" for a in F['am'])}</ul>
    </div></section>
    <section class="fa-cta" id="farie-ospiti"><div class="wrap">
      <span class="eyebrow light rv">Cosa dicono gli ospiti</span>
      <h2 class="rv d1"><em>{F['rating']}</em> su {F['reviews']} recensioni.</h2>
      <p class="rv d2" style="max-width:640px;margin:0 auto 34px;color:rgba(244,237,228,.8);font-size:18px">Su Booking.com gli ospiti premiano soprattutto l'accoglienza di {F['hosts']}, la colazione, la pulizia e la tranquillità della posizione, con la vista sulle montagne.</p>
      <div class="facts rv" style="max-width:760px;margin:0 auto 36px;background:transparent;border-color:rgba(244,237,228,.2)">{scores}</div>
      <a class="btn btn-light rv d3" href="{F['booking']}" target="_blank" rel="noopener">Leggi le recensioni su Booking.com {I('arrow')}</a>
    </div></section>
    <section class="sec" id="farie-info"><div class="wrap fa-split" style="align-items:start">
      <div><span class="eyebrow rv">Info utili</span><h2 class="rv d1">Prima di <em>arrivare.</em></h2>
        <div class="routes rv" style="margin-top:24px">{rules}</div></div>
      <div><span class="eyebrow rv">Dove siamo</span><h2 class="rv d1">A Lungis, nella <em>Carnia più vera.</em></h2>
        <p class="rv d2">{F['addr']}, frazione di Lungis, comune di Socchieve (UD), a 554 metri di quota. A due passi l'agriturismo In Già, il bar alimentari Al Cervo e i sentieri dell'Anello delle Frazioni.</p>
        <ul class="dist rv" style="margin-top:24px;grid-template-columns:repeat(2,1fr)">{near}</ul>
        <p class="rv" style="margin-top:24px"><a class="link" href="/it/lungis">Scopri il borgo di Lungis {I('arrow')}</a></p></div>
    </div></section>
    <section class="cta"><div class="wrap">
      <span class="eyebrow rv">La Farie · Lungis</span>
      <h2 class="rv d1">Il tuo B&amp;B <em>in Carnia.</em></h2>
      <p class="rv d2">Scrivici le date e il numero di ospiti: ti rispondiamo con disponibilità e prezzi.</p>
      <div class="row rv d3"><a class="btn btn-primary" href="#scrivici">Chiedi disponibilità {I('arrow')}</a><a class="btn btn-dark" href="/">Scopri anche Col Gentile</a></div>
    </div></section>"""
    ld = {"@context": "https://schema.org", "@type": "BedAndBreakfast", "@id": U + "/la-farie#bnb", "name": "La Farie",
          "description": " ".join(F["intro"]), "url": U + "/la-farie", "image": [abs_img(g) for g in F["g"][:8] if g in PH],
          "address": address(F["addr"], "Lungis, Socchieve"),
          "geo": {"@type": "GeoCoordinates", "latitude": F["geo"][0], "longitude": F["geo"][1]},
          "checkinTime": "15:00", "checkoutTime": "10:00", "petsAllowed": True, "smokingAllowed": False,
          "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in F["am"]],
          "sameAs": [F["booking"]], "email": SITE["email"], "parentOrganization": {"@id": LODGING_ID}}
    crumbs = [("Home", "/"), ("La Farie", "/la-farie")]
    page("/la-farie", "La Farie · Bed & Breakfast a Lungis, Socchieve (Carnia)",
         f"B&B in una casa carnica ristrutturata a Lungis, Socchieve: colazione, Wi-Fi, parcheggio gratuito, camere con terrazza. Voto {F['rating']}/10 su {F['reviews']} recensioni.",
         body, image=F["g"][0], preload=preload_for(F["g"][0]), wrapper=wrap, ld=[ld, crumbs_ld(crumbs)],
         images=[abs_img(g) for g in F["g"] if g in PH])


def welora(view):
    W = data.WELORA
    if not W["live"]:
        return ""
    return f'<div class="welora-box rv"><div data-welora-booking data-slug="{W["slug"]}" data-mode="services" data-view="{view}"></div></div><script src="{W["base"]}/assets/js/booking-widget.js?v={W["script_v"]}" defer></script>'


def svc_aside(s=None):
    name = s["n"] if s else "Benessere"
    subj = e("Prenotazione " + name)
    live = data.WELORA["live"]
    online = f'<a class="btn btn-primary" href="{data.WELORA["results"]}">Prenota online {I("arrow")}</a>' if live else ""
    price = f'<p style="margin-top:16px;color:var(--bone);font:400 30px/1 var(--serif)">{s["price"]} € <span style="font:500 14px var(--sans);color:var(--sage)">{s["unit"]}</span></p>' if s else ""
    intro = "Scegli giorno, orario e numero di persone: la conferma arriva via email." if live else "Scrivici o chiamaci con giorno, orario e numero di persone: ti confermiamo la disponibilità."
    mail_cls = "btn-ghost" if online else "btn-primary"
    return f"""<aside class="aside rv">
      <h2 style="font-size:30px;line-height:1.1;margin:0">{e(name)}</h2>
      {price}
      <p>{intro}</p>
      {online}
      <a class="btn {mail_cls}" href="mailto:{SITE['email']}?subject={subj}">Prenota via email {I('arrow')}</a>
      <a class="btn btn-ghost" href="tel:{SITE['phone_href']}">{SITE['phone']}</a>
      <p style="margin-top:16px;font-size:13px">Il pagamento si salda in struttura.</p>
    </aside>"""


def svc_card(s):
    img = pic(s["hero"], s["n"], "(max-width:640px) 100vw, 50vw") if s["hero"] else ""
    cls = "tile big" if s["hero"] else "tile green"
    unit = s["unit"].split(",")[0]
    return (f'<a class="{cls} rv" href="/it/{s["id"]}" style="grid-column:span 2">{img}<span class="num">{s["price"]} € · {unit}</span>'
            f'<h3>{e(s["n"])}</h3><p>{e(s["lead"])}</p><span class="link">Scopri e prenota {I("arrow")}</span></a>')


def service_ld(s):
    ld = {"@context": "https://schema.org", "@type": "Service", "@id": U + f"/it/{s['id']}#service", "name": s["n"], "serviceType": "Benessere",
          "description": " ".join(s["text"]), "url": U + f"/it/{s['id']}", "provider": {"@id": LODGING_ID}, "areaServed": "Carnia",
          "offers": {"@type": "Offer", "price": f"{s['price']:.2f}", "priceCurrency": "EUR", "description": s["unit"], "url": U + f"/it/{s['id']}"}}
    if s["hero"]:
        ld["image"] = abs_img(s["hero"])
    return ld


def build_services():
    S = data.SERVICES
    for s in S:
        crumbs = [("Home", "/"), ("Benessere", "/it/benessere"), (s["n"], f"/it/{s['id']}")]
        facts = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in s["facts"])
        bring = ""
        if s.get("bring"):
            rows = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in s["bring"])
            note = f'<p class="cin" style="margin-top:18px">{e(s["note"])}</p>' if s.get("note") else ""
            bring = f'<div class="rv"><span class="eyebrow">Cosa portare</span><h2>Come prepararsi</h2><div class="routes">{rows}</div>{note}</div>'
        meet = ""
        if s.get("meeting"):
            meet = f'<div class="rv"><span class="eyebrow">Ritrovo</span><h2>Dove ci si incontra</h2><p>{e(s["meeting"])}. <a class="link" href="/it/contact">Come arrivare {I("arrow")}</a></p></div>'
        if s["hero"]:
            hero_html = hero(s["hero"], s["n"] + " a Socchieve, Carnia", crumbs, e(s["n"]), sub=e(s["lead"]))
        else:
            hero_html = (f'<section class="ph ph-plain"><div class="wrap"><nav class="crumbs" aria-label="Percorso"><a href="/">Home</a><span>/</span>'
                         f'<a href="/it/benessere">Benessere</a><span>/</span><b>{e(s["n"])}</b></nav><h1>{e(s["n"])}</h1><p class="lead">{e(s["lead"])}</p></div></section>')
        paras = "".join(f'<p class="prose-first">{e(p)}</p>' if i == 0 else f"<p>{e(p)}</p>" for i, p in enumerate(s["text"]))
        minis = ""
        for x in S:
            if x["id"] == s["id"]:
                continue
            ph = pic(x["hero"], x["n"], "(max-width:640px) 70vw, 25vw") if x["hero"] else f'<div class="mini-ph">{e(x["n"])}</div>'
            minis += f'<a class="mini" href="/it/{x["id"]}">{ph}<div><b>{x["n"]}</b><span>{x["price"]} € {x["unit"].split(",")[0]}</span></div></a>'
        for k in ("trekking", "cicloturismo", "visita-la-carnia"):
            x = EXPS[k]
            minis += f'<a class="mini" href="{exp_url(k)}">{pic(x["hero"], x["n"], "(max-width:640px) 70vw, 25vw")}<div><b>{x["n"]}</b><span>{e(clip(x["lead"], 60))}</span></div></a>'
        body = f"""{hero_html}
<section class="d-body"><div class="wrap d-grid">
  <div class="d-main">
    <div class="rv"><span class="eyebrow">Benessere a Socchieve · Carnia</span><h2>{ {"bagno-di-bosco": "Cos'è il bagno di bosco", "sauna": "Come funziona la sauna"}.get(s["id"], "Come funziona") }</h2>{paras}</div>
    <div class="facts rv">{facts}</div>
    {welora("search")}
    {meet}
    {bring}
  </div>
  {svc_aside(s)}
</div></section>
<section class="related"><div class="wrap"><span class="eyebrow">Benessere e natura</span><h2>Da abbinare</h2><div class="mini-rail">{minis}</div></div></section>"""
        page(f"/it/{s['id']}", s["title"], s["desc"], body, active="benessere", image=s["hero"] or "PanoramaNonta1.jpg",
             preload=preload_for(s["hero"]) if s["hero"] else None, ld=[service_ld(s), crumbs_ld(crumbs)],
             images=[abs_img(s["hero"])] if s["hero"] else [])

    crumbs = [("Home", "/"), ("Benessere", "/it/benessere")]
    cards = "".join(svc_card(s) for s in S)
    body = f"""{hero("PanoramaNonta1.jpg", "Prati al tramonto a Nonta, Socchieve", crumbs, "Benessere <em>in Carnia</em>", sub="Sauna e bagno di bosco all'Albergo Diffuso di Socchieve: il modo giusto per chiudere una giornata in montagna.")}
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow rv">I servizi</span><h2 class="rv d1">Rallenta, <em>respira.</em></h2></div><p class="rv d2">Prezzi chiari, pagamento in struttura. Scrivici per sapere se si possono prenotare anche senza soggiornare da noi.</p></div>
  <div class="bento">{cards}</div>
  {welora("search")}
</div></section>"""
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Benessere all'Albergo Diffuso Socchieve", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": U + f"/it/{s['id']}", "name": s["n"]} for i, s in enumerate(S)]}
    page("/it/benessere", "Benessere in Carnia: sauna e bagno di bosco a Socchieve",
         "Sauna (50 € l'ora per il gruppo) e bagno di bosco Shinrin-yoku con guida (15 € a persona) all'Albergo Diffuso di Socchieve, in Carnia. Prenota direttamente.",
         body, active="benessere", image="PanoramaNonta1.jpg", preload=preload_for("PanoramaNonta1.jpg"),
         ld=[items, crumbs_ld(crumbs)] + [service_ld(s) for s in S], images=[abs_img("PanoramaNonta1.jpg")])

    W = data.WELORA
    crumbs = [("Home", "/"), ("Benessere", "/it/benessere"), ("Prenota servizi", W["results"])]
    if W["live"]:
        inner = welora("results")
    else:
        inner = (f'<p style="max-width:620px;color:var(--muted);font-size:17px">La prenotazione online sarà disponibile a breve. Nel frattempo scrivici a '
                 f'<a class="link" href="mailto:{SITE["email"]}?subject=Prenotazione%20servizi">{SITE["email"]}</a> o chiama il '
                 f'<a class="link" href="tel:{SITE["phone_href"]}">{SITE["phone"]}</a>.</p>')
    body = f"""<section class="d-body" style="padding-top:140px"><div class="wrap">
  <nav class="crumbs" aria-label="Percorso" style="color:var(--muted)"><a href="/">Home</a><span>/</span><a href="/it/benessere">Benessere</a><span>/</span><b>Prenota servizi</b></nav>
  <h1 style="font-size:clamp(40px,6vw,80px);line-height:1;margin:10px 0 28px">Prenota <em>sauna e bagno di bosco</em></h1>
  {inner}
</div></section>"""
    page(W["results"], "Prenota sauna e bagno di bosco · Albergo Diffuso Socchieve",
         "Prenota online sauna e bagno di bosco all'Albergo Diffuso di Socchieve, in Carnia.", body, active="benessere", solid=True,
         noindex=not W["live"], ld=[crumbs_ld(crumbs)])


def build_legal():
    privacy = f"""<section class="d-body" style="padding-top:140px"><div class="wrap prose">
  <span class="eyebrow">Informativa</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">Privacy</h1>
  <p>Titolare del trattamento: {SITE['legal']}, {SITE['street']}, {SITE['locality']}, {SITE['zip']} Socchieve (UD), P.I. {SITE['vat']}, email <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
  <h2>Dati raccolti da questo sito</h2>
  <p>Il sito non usa cookie di profilazione né strumenti di statistica e non contiene moduli di raccolta dati. I font e le immagini sono ospitati sul nostro server. Il server registra, come ogni sito web, dati tecnici di navigazione (indirizzo IP, data e ora, pagina richiesta) per motivi di sicurezza e funzionamento.</p>
  <h2>Contatti e prenotazioni</h2>
  <p>Se ci scrivi o ci telefoni, usiamo i tuoi dati solo per risponderti e gestire il soggiorno. Le prenotazioni online avvengono sul sistema Slope, che tratta i dati secondo la propria informativa; la mappa della pagina contatti è fornita da OpenStreetMap; il tour virtuale carica la libreria Pannellum da cdnjs (Cloudflare) solo quando lo avvii.</p>
  <h2>I tuoi diritti</h2>
  <p>Puoi chiedere in ogni momento accesso, rettifica, cancellazione o limitazione dei tuoi dati scrivendo a {SITE['email']}, e proporre reclamo al Garante per la protezione dei dati personali.</p>
</div></section>"""
    page("/privacy", "Privacy · Albergo Diffuso Socchieve", "Informativa privacy del sito dell'Albergo Diffuso Socchieve Col Gentile.", privacy, solid=True)
    cookies = f"""<section class="d-body" style="padding-top:140px"><div class="wrap prose">
  <span class="eyebrow">Informativa</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">Cookie</h1>
  <p>Questo sito non installa cookie di profilazione né cookie di terze parti per statistiche o pubblicità, per questo non mostra banner di consenso.</p>
  <p>Il sito di prenotazione Slope, raggiungibile dai pulsanti “Prenota”, e la mappa di OpenStreetMap nella pagina contatti hanno le proprie informative. Per domande scrivi a <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
</div></section>"""
    page("/cookies", "Cookie · Albergo Diffuso Socchieve", "Informativa cookie del sito dell'Albergo Diffuso Socchieve Col Gentile.", cookies, solid=True)
    terms = f"""<section class="d-body" style="padding-top:140px"><div class="wrap prose">
  <span class="eyebrow">Benessere</span><h1 style="font-size:clamp(40px,6vw,72px);margin:16px 0 24px">Condizioni di prenotazione dei servizi</h1>
  <p>Valgono per le prenotazioni di sauna e bagno di bosco fatte online, via email o per telefono presso {SITE['legal']}, {SITE['street']}, {SITE['locality']}, {SITE['zip']} Socchieve (UD), P.I. {SITE['vat']}.</p>
  <h2>Prezzi</h2>
  <p>I prezzi sono in euro. Il prezzo mostrato al momento della prenotazione è quello definitivo: per il bagno di bosco è a persona, per la sauna è all'ora per tutto il gruppo.</p>
  <h2>Pagamento</h2>
  <p>La prenotazione online non prevede pagamenti: il servizio si salda direttamente in struttura.</p>
  <h2>Conferma</h2>
  <p>Dopo la prenotazione ricevi un'email di conferma con data, orario e numero di partecipanti. Il numero di partecipanti non può superare la capienza indicata per il servizio.</p>
  <h2>Modifiche e cancellazioni</h2>
  <p>Per cambiare orario, numero di persone o per cancellare, scrivi a <a href="mailto:{SITE['email']}">{SITE['email']}</a> o chiama il <a href="tel:{SITE['phone_href']}">{SITE['phone']}</a> il prima possibile: modifiche e cancellazioni vanno concordate con la struttura.</p>
  <h2>Bagno di bosco</h2>
  <p>È un'attività all'aperto su sentieri e terreno boschivo: servono abbigliamento e calzature adatte, come indicato nella pagina del servizio.</p>
  <h2>Dati personali</h2>
  <p>I dati della prenotazione sono trattati come descritto nell'<a href="/privacy">informativa privacy</a>.</p>
</div></section>"""
    page("/condizioni-servizi", "Condizioni di prenotazione dei servizi · Albergo Diffuso Socchieve",
         "Condizioni per prenotare sauna e bagno di bosco all'Albergo Diffuso Socchieve: prezzi, pagamento in struttura, modifiche e cancellazioni.", terms, solid=True)
    err = f"""<section class="err"><div><span class="eyebrow">Errore 404</span><h1>Pagina <em>non trovata.</em></h1><p style="margin:20px auto 30px;max-width:460px;color:var(--muted)">Forse la pagina è stata spostata con il nuovo sito. Ecco da dove ripartire:</p>
  <div class="row" style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap"><a class="btn btn-dark" href="/it/alloggi/">Le case</a><a class="btn btn-primary" href="/">Home</a></div></div></section>"""
    page("/404", "Pagina non trovata · Albergo Diffuso Socchieve", "La pagina richiesta non esiste.", err, solid=True, noindex=True)
    # vecchia home /it -> /
    (ROOT / "it").mkdir(exist_ok=True)
    (ROOT / "it" / "index.html").write_text(f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Albergo Diffuso Socchieve</title><link rel="canonical" href="{U}/"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url=../"></head><body><a href="../">Vai alla home</a></body></html>\n', encoding="utf-8")


# ---------------------------------------------------------------- file di servizio
def build_meta():
    urls = []
    for path, imgs in PAGES:
        prio = "1.0" if path == "/" else "0.9" if path.startswith("/it/alloggi") else "0.7"
        im = "".join(f"<image:image><image:loc>{x}</image:loc></image:image>" for x in dict.fromkeys(imgs) if x)
        urls.append(f"<url><loc>{U}{path}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority>{im}</url>")
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {U}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(json.dumps({"name": SITE["name"], "short_name": "Col Gentile", "start_url": "./", "display": "standalone", "background_color": "#fbf8f2", "theme_color": "#16241e",
        "icons": [{"src": "apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False), encoding="utf-8")
    # redirect 301 dalle vecchie pagine EN/FR (Netlify / Cloudflare Pages) finché non esistono le traduzioni
    m = {"": "/", "/accomodation": "/it/alloggi/", "/logement": "/it/alloggi/", "/territory": "/it/territorio", "/territoire": "/it/territorio",
         "/visit-carnia": "/it/visita-la-carnia", "/visiter-la-carnia": "/it/visita-la-carnia", "/cycle-touring": "/it/cicloturismo", "/cyclisme": "/it/cicloturismo",
         "/trekking": "/it/trekking", "/art-and-culture": "/it/arte-e-cultura", "/art-et-culture": "/it/arte-e-cultura", "/contact": "/it/contact",
         "/alloggi/casa-vanda-0": "/it/alloggi/casa-vanda"}
    lines = ["/it  /  301"]
    for lang in ("en", "fr"):
        for a, b in m.items():
            lines.append(f"/{lang}{a}  {b}  301")
        for s in STAYS:
            lines.append(f"/{lang}/alloggi/{s['id']}  /it/alloggi/{s['id']}  301")
        lines.append(f"/{lang}/*  /  301")
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
    build_home(); build_catalog()
    for s in STAYS: build_stay(s)
    for v in VILLAGES: build_village(v)
    for k, x in EXPS.items(): build_exp(k, x)
    build_territorio(); build_contact(); build_farie(); build_services(); build_legal()
    build_meta(); build_icons()
    print(f"OK: {len(PAGES)} pagine indicizzabili, sitemap.xml, robots.txt, _redirects")
    if MISSING:
        print(f"  ! {len(MISSING)} immagini ancora remote: rilancia fetch_assets.py e poi build.py")


if __name__ == "__main__":
    main()
