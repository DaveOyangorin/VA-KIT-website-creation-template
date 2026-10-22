"""Downloads every image the pages use, converts to WebP (<150 KB) into site/assets/img.

  python -I imgprep.py <pylib> <extract.json> <img_out> <cache_dir> <logo_svg>

Badges, award graphics and icons are skipped. Writes imgmeta.json (name -> [w, h, kb]) and imgmap.json
(remote url -> name) next to this file.
"""
import sys, os, json, re, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, sys.argv[1])
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ex = json.load(open(sys.argv[2], encoding="utf-8"))
OUT, CACHE, LOGO = sys.argv[3], sys.argv[4], sys.argv[5]
os.makedirs(OUT, exist_ok=True); os.makedirs(CACHE, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
SKIP = re.compile(r"google-raster|faces-of-ar|bbb|gold\.png|badge|logo|icon|favicon|owens-corning-preferred|rsra|award|star", re.I)
meta, imap = {}, {}


def slug(url):
    b = os.path.splitext(os.path.basename(url.split("?")[0]))[0].lower()
    b = re.sub(r"-\d+x\d+$", "", b); b = re.sub(r"-(scaled|e\d+)$", "", b); b = re.sub(r"[^a-z0-9]+", "-", b).strip("-")
    return b[:70] or "image"


def fetch(u):
    local = os.path.join(CACHE, slug(u) + os.path.splitext(u.split("?")[0])[1].lower())
    if os.path.exists(local) and os.path.getsize(local) > 0: return u, local
    for _ in range(3):
        try:
            open(local, "wb").write(urllib.request.urlopen(urllib.request.Request(urllib.parse.quote(u, safe=":/?&=%"), headers=UA), timeout=60).read()); time.sleep(.3)
            return u, local
        except Exception as e:
            err = e; time.sleep(3)
    print("FAIL", u, err); return u, None


def save(src_path, name, maxw=1600):
    im = Image.open(src_path)
    if im.mode in ("P", "LA", "RGBA"):
        im = im.convert("RGBA"); bg = Image.new("RGB", im.size, (255, 255, 255)); bg.paste(im, mask=im.split()[3]); im = bg
    else:
        im = im.convert("RGB")
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    if im.height > 1800: im = im.resize((round(im.width * 1800 / im.height), 1800), Image.LANCZOS)
    q, p = 80, os.path.join(OUT, name + ".webp")
    while True:
        im.save(p, "WEBP", quality=q, method=6)
        if os.path.getsize(p) < 150_000 or q <= 45: break
        q -= 7
    while os.path.getsize(p) >= 150_000 and im.width > 700:
        im = im.resize((int(im.width * .85), int(im.height * .85)), Image.LANCZOS); im.save(p, "WEBP", quality=60, method=6)
    meta[name] = [im.width, im.height, os.path.getsize(p) // 1024]


urls = []
for r in ex:
    urls += r["images"]
    if r.get("og_image") and "/wp-content/" in r["og_image"]: urls.append(r["og_image"])
urls = [u for u in dict.fromkeys(urls) if not SKIP.search(u) and re.search(r"\.(jpe?g|png|webp)$", u.split("?")[0], re.I)]
with ThreadPoolExecutor(4) as pool:
    got = list(pool.map(fetch, urls))
used = {}
for u, local in got:
    if not local: continue
    name = slug(u)
    if name in used and used[name] != u: name = name + "-2"
    used[name] = u
    try:
        im = Image.open(local)
        if min(im.size) < 160: continue  # tiny graphics
        save(local, name); imap[u] = name
    except Exception as e:
        print("BAD", u, e)

# logo: the client's white SVG, rendered to PNG/WebP for the maroon header
from playwright.sync_api import sync_playwright
svg = open(LOGO, encoding="utf-8").read()
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge"); pg = b.new_page(viewport={"width": 400, "height": 562})
    pg.set_content(f'<html><body style="margin:0;background:transparent">{svg.replace("<svg ", "<svg width=\"400\" height=\"562\" ", 1)}</body></html>')
    pg.screenshot(path=os.path.join(OUT, "ez-roofing-logo.png"), omit_background=True, clip={"x": 0, "y": 0, "width": 400, "height": 562}); b.close()
lg = Image.open(os.path.join(OUT, "ez-roofing-logo.png")).convert("RGBA"); lg = lg.crop(lg.getbbox()); lg.thumbnail((240, 340))
lg.save(os.path.join(OUT, "ez-roofing-logo.png"), optimize=True); lg.save(os.path.join(OUT, "ez-roofing-logo.webp"), "WEBP", quality=92)
meta["ez-roofing-logo"] = list(lg.size) + [0]
fav = Image.new("RGBA", (64, 64), (104, 18, 20, 255)); t = lg.copy(); t.thumbnail((44, 56)); fav.paste(t, ((64 - t.width) // 2, (64 - t.height) // 2), t)
fav.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
json.dump(imap, open(os.path.join(HERE, "imgmap.json"), "w"), indent=0)
print(len(meta), "images;", len(imap), "mapped; over 150KB:", {k: v for k, v in meta.items() if v[2] >= 150})
