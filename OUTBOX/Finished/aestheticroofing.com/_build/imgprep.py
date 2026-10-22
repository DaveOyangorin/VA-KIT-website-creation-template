"""Downloads every image the pages use, converts to WebP (<150 KB) into site/assets/img.

  python -I imgprep.py <pylib> <extract.json> <img_out> <cache_dir> <unsplash_dir> <client_dl_dir>

Writes imgmeta.json (name -> [w, h, kb]) and imgmap.json (remote url -> name) next to this file.
"""
import sys, os, json, re, time, urllib.request
sys.path.insert(0, sys.argv[1])
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ex = json.load(open(sys.argv[2], encoding="utf-8"))
OUT, CACHE, US, DL = sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
os.makedirs(OUT, exist_ok=True); os.makedirs(CACHE, exist_ok=True)
meta, imap = {}, {}


def save(src_path, name, maxw=1600, bgc=(255, 255, 255)):
    im = Image.open(src_path)
    if im.mode in ("P", "LA", "RGBA"):
        im = im.convert("RGBA"); bg = Image.new("RGB", im.size, bgc); bg.paste(im, mask=im.split()[3]); im = bg
    else:
        im = im.convert("RGB")
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    q, p = 80, os.path.join(OUT, name + ".webp")
    while True:
        im.save(p, "WEBP", quality=q, method=6)
        if os.path.getsize(p) < 150_000 or q <= 45: break
        q -= 7
    while os.path.getsize(p) >= 150_000 and im.width > 700:
        im = im.resize((int(im.width * .85), int(im.height * .85)), Image.LANCZOS); im.save(p, "WEBP", quality=60, method=6)
    meta[name] = [im.width, im.height, os.path.getsize(p) // 1024]


def slug(url):
    b = os.path.splitext(os.path.basename(url.split("?")[0]))[0].lower()
    b = re.sub(r"-\d+x\d+$", "", b); b = re.sub(r"[^a-z0-9]+", "-", b).strip("-")
    return b[:70] or "image"


# 1) images found in page content and og:image of blog posts
urls = []
for r in ex:
    urls += r["images"]
    if r.get("og_image") and "/wp-content/" in r["og_image"] and not re.search(r"logo|favicon", r["og_image"], re.I):
        urls.append(r["og_image"])
for u in dict.fromkeys(urls):
    name = slug(u)
    local = os.path.join(CACHE, name + os.path.splitext(u)[1].lower())
    pre = os.path.join(DL, os.path.basename(u.split("?")[0]))
    if os.path.exists(pre) and os.path.getsize(pre) > 0:
        local = pre  # already downloaded
    if not os.path.exists(local):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            open(local, "wb").write(urllib.request.urlopen(req, timeout=30).read()); time.sleep(1.5)
        except Exception as e:
            print("FAIL", u, e); continue
    try:
        save(local, name); imap[u] = name
    except Exception as e:
        print("BAD", u, e)

# 2) the client's own home-page photos (already downloaded) and chosen Unsplash photos
C = DL  # all client photos were downloaded into one folder
CLIENT = {"aerial-new-roof-neighborhood": "6a2976fd47498bd2a51b5b77_Main-P1.avif", "aerial-roofs-street": "6a2977041b174d5f6f00f59f_4-P1.avif",
          "top-down-new-roof": "DJI_20260529035444_0188_D.jpg", "aerial-gray-roof-solar": "DJI_20260603012518_0275_D.webp",
          "aerial-new-shingle-roof": "DJI_20260626014642_0355_D.webp", "aerial-home-mountains": "DJI_20260717041329_0438_D.webp",
          "aesthetic-team": "69f9d2136eb69cfc87e6c556_about-hero.avif", "aerial-new-roof-yard": "69fc98231c4827218eaa93e9_process-04.avif",
          "crew-on-roof-utah-county": "Utah-County_Aesthetic-Roofing.jpg", "aerial-roof-crew-install": "roofrepair-img.jpg",
          "material-asphalt-shingles": "DJI_20260526235009_0161_D.webp", "roof-material-samples": "roof-types-img-temp.webp",
          "storm-damaged-shingles": "Storm-damage-roof-img.jpg", "shingle-inspection-marks": "roofinspection-img.jpg",
          "gaf-master-elite": "Master_Elite.webp", "bbb-logo": "BBB_PrimaryLogo_Blue_RGB.svg.webp", "service-area-map": "SA-Map.webp"}
for name, f in CLIENT.items():
    save(os.path.join(DL, f), name, bgc=(241, 242, 239) if name == "service-area-map" else (255, 255, 255))
UNSPLASH = {"material-metal": "1779941373840-a93f6e0d5db0.jpg", "material-flat": "1640476750068-72c645e653cd.jpg"}
for name, f in UNSPLASH.items():
    save(os.path.join(US, f), name)
from PIL import Image as _I
for name, f in (("aesthetic-roofing-logo-white", "aesthetic-roofing-wht-logo.webp"), ("aesthetic-roofing-logo-dark", "aesthetic-logo-blk.png")):
    lg = _I.open(os.path.join(DL, f)).convert("RGBA")
    if lg.width > 600: lg = lg.resize((600, round(lg.height * 600 / lg.width)), _I.LANCZOS)
    lg.save(os.path.join(OUT, name + ".png"), optimize=True); lg.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=92)
    meta[name] = list(lg.size) + [0]
fav = _I.open(os.path.join(DL, "Aesthetic-A-yellow.webp")).convert("RGBA"); fav.thumbnail((64, 64)); fav.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
json.dump(imap, open(os.path.join(HERE, "imgmap.json"), "w"), indent=0)
big = {k: v for k, v in meta.items() if v[2] >= 150}
print(len(meta), "images;", len(imap), "from page content; over 150KB:", big)
