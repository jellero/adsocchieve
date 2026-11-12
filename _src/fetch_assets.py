"""Scarica dal vecchio sito le immagini citate in data.py, le ottimizza (WebP in più
larghezze, panorami 360 in JPEG 4096x2048, immagini Open Graph 1200x630) e i font.
Uso:  python _src/fetch_assets.py      (serve Pillow; i file scaricati restano in _src/cache)"""
import json, re, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_src"))
import data  # noqa: E402

OLD = "https://albergodiffusosocchieve.it/sites/default/files/"
CACHE = ROOT / "_src" / "cache"
IMG = ROOT / "img"
UA = {"User-Agent": "Mozilla/5.0 (static-site-builder)"}
WIDTHS = [480, 960, 1600]
Image.MAX_IMAGE_PIXELS = None


def slug(name):
    if name.startswith("http"):
        m = re.search(r"/(\d+)\.jpg", name)
        return "farie-" + (m.group(1) if m else re.sub(r"\W+", "-", name)[-20:])
    base = urllib.parse.unquote(name).rsplit(".", 1)[0]
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")


def collect():
    photos, panos, og = set(), set(), set()
    photos |= {"Slide1Socchieve.jpg", "Slide2Socchieve.jpg", "Slide3Socchieve.jpg", "Casa-Vanda-esterno.jpg",
               "logoborghi%20autentici%20d%27Italia.jpg"}
    og |= {"Slide1Socchieve.jpg", "LungisCartolina.jpg", "PanoramaLungis3.jpg"}
    for s in data.STAYS:
        photos |= {s["card"], *s["g"]} | ({s["plan"]} if s.get("plan") else set())
        panos |= set(s.get("pano", []))
        og.add(s["g"][0])
    for v in data.VILLAGES:
        photos |= {v["card"], *v["hero"]}
        og.add(v["hero"][0])
    photos |= set(data.FARIE["g"]); og.add(data.FARIE["g"][0])
    for e in data.EXPS.values():
        photos.add(e["hero"]); og.add(e["hero"])
        photos |= {r["map"] for r in e.get("routes", []) if r.get("map")}
        photos |= {i["img"] for i in e.get("items", [])}
    return photos, panos, og


OLD_DOWN = False


def download(name):
    global OLD_DOWN
    dest = CACHE / slug(name)
    if dest.exists() and dest.stat().st_size > 0:
        return name, dest
    base = name.split("?")[0]
    urls = (name,) if name.startswith("http") else ()
    cands = (OLD + base, OLD + "styles/slide/public/" + base, OLD + "styles/portfolio/public/" + base)
    wb = "https://web.archive.org/web/2025id_/"
    archive = tuple(wb + c for c in cands) + tuple(wb + c.replace("://", "://www.") for c in cands)
    if not urls:
        urls = (archive if OLD_DOWN else cands + archive)
    import subprocess
    for url in urls:
        if "web.archive.org" in url:
            tmp = dest.with_suffix(".part")
            r = subprocess.run(["curl", "-s", "-L", "-f", "--ssl-no-revoke", "--retry", "2", "--max-time", "120", "-o", str(tmp), "-w", "%{content_type}", url], capture_output=True, text=True)
            if r.returncode == 0 and r.stdout.startswith("image") and tmp.exists() and tmp.stat().st_size > 1000:
                tmp.replace(dest)
                return name, dest
            tmp.unlink(missing_ok=True)
            continue
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
                if r.status == 200 and r.headers.get_content_type().startswith("image"):
                    dest.write_bytes(r.read())
                    return name, dest
        except Exception:
            continue
    return name, None


def process_photo(name, src, manifest):
    s = slug(name)
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    w, h = im.size
    variants = []
    for tw in WIDTHS:
        if tw > w and variants:
            break
        tw = min(tw, w)
        out = IMG / f"{s}-{tw}.webp"
        if not out.exists():
            im.resize((tw, round(h * tw / w)), Image.LANCZOS).save(out, "WEBP", quality=78, method=4)
        variants.append(tw)
        if tw == w:
            break
    manifest[name] = {"slug": s, "w": w, "h": h, "widths": variants}


def process_og(name, src, manifest):
    s = slug(name)
    out = IMG / "og" / f"{s}.jpg"
    if not out.exists():
        im = ImageOps.fit(ImageOps.exif_transpose(Image.open(src)).convert("RGB"), (1200, 630), Image.LANCZOS)
        im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    manifest[name]["og"] = f"/img/og/{s}.jpg"


def process_pano(name, src, manifest):
    s = slug(name)
    out, thumb = IMG / "360" / f"{s}.jpg", IMG / "360" / f"{s}-thumb.webp"
    im = None
    if not out.exists():
        im = Image.open(src).convert("RGB")
        im.resize((4096, 2048), Image.LANCZOS).save(out, "JPEG", quality=72, optimize=True, progressive=True)
    if not thumb.exists():
        im = im or Image.open(src).convert("RGB")
        w, h = im.size
        ImageOps.fit(im.crop((w // 4, h // 4, w * 3 // 4, h * 3 // 4)), (480, 300), Image.LANCZOS).save(thumb, "WEBP", quality=75)
    manifest[name] = {"slug": s, "src": f"/img/360/{s}.jpg", "thumb": f"/img/360/{s}-thumb.webp"}


def fonts():
    css_url = ("https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..500"
               "&family=Inter+Tight:wght@400;500;600;700&display=swap")
    ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
    css = urllib.request.urlopen(urllib.request.Request(css_url, headers=ua), timeout=60).read().decode()
    out_dir = ROOT / "assets" / "fonts"
    out_dir.mkdir(parents=True, exist_ok=True)
    blocks, keep = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S), []
    for subset, block in blocks:
        if subset not in ("latin", "latin-ext"):
            continue
        fam = re.search(r"font-family: '([^']+)'", block).group(1)
        style = re.search(r"font-style: (\w+)", block).group(1)
        url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
        fname = f"{slug(fam)}-{style}-{subset}.woff2"
        p = out_dir / fname
        if not p.exists():
            p.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers=ua), timeout=60).read())
        keep.append(block.replace(url, f"/assets/fonts/{fname}"))
    (ROOT / "_src" / "fonts.css").write_text("\n".join(keep), encoding="utf-8")
    print("fonts:", len(keep), "face")


def main():
    for d in (CACHE, IMG, IMG / "og", IMG / "360"):
        d.mkdir(parents=True, exist_ok=True)
    global OLD_DOWN
    photos, panos, og = collect()
    names = sorted(photos | panos)
    import subprocess
    try:
        ok = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "8", OLD], capture_output=True, text=True, timeout=12).stdout
    except Exception:
        ok = ""
    if not ok.startswith(("2", "3", "4")):
        OLD_DOWN = True
        print("vecchio sito non raggiungibile da questa rete: elaboro solo le foto già scaricate")
    with ThreadPoolExecutor(2) as ex:
        got = dict(ex.map(download, names))
    missing = [n for n, p in got.items() if p is None]
    if missing:
        print("NON TROVATE:", missing)
    mf = ROOT / "_src" / "images.json"
    manifest = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else {"photos": {}, "panos": {}}
    def work(n):
        p = got.get(n)
        if not p:
            return
        if n in panos:
            process_pano(n, p, manifest["panos"])
        else:
            process_photo(n, p, manifest["photos"])
            if n in og:
                process_og(n, p, manifest["photos"])
    with ThreadPoolExecutor(6) as ex:
        list(ex.map(work, names))
    (ROOT / "_src" / "images.json").write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
    print(f"foto: {len(manifest['photos'])}  panorami: {len(manifest['panos'])}  mancanti: {len(missing)}")
    fonts()


if __name__ == "__main__":
    main()
