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
G = "aluminum-lock-gallery-"
CLIENT = {"aluminum-shingle-home-deep-snow": G + "1.jpg", "copper-aluminum-shingle-arched-roof": G + "10-scaled.jpg",
          "green-aluminum-shingle-commercial-mountains": G + "11.jpg", "copper-aluminum-shingle-roof-snow": G + "12-scaled.jpg",
          "gray-aluminum-shingle-bungalow": G + "13.jpg", "copper-aluminum-shingle-new-construction": G + "14.jpg",
          "gray-green-aluminum-shingle-home": G + "15.jpg", "green-aluminum-shingle-mountain-home": G + "16-scaled.jpg",
          "brick-red-aluminum-shingle-stone-cottage": G + "17.jpg", "brown-aluminum-shingle-home": G + "18-scaled.jpg",
          "copper-aluminum-shingle-a-frame": G + "19.jpg", "brown-stone-aluminum-shingle-home": G + "2.jpg",
          "gray-aluminum-shingle-two-story-home": G + "3-scaled.jpg", "gray-aluminum-shingle-home-aerial": G + "4.jpg",
          "red-aluminum-shingle-white-home": G + "5.jpg", "brown-aluminum-shingle-brick-home": G + "6.jpg",
          "red-aluminum-shingle-stucco-home": G + "7.jpg", "matte-black-aluminum-shingle-home": G + "8-scaled.jpg",
          "copper-aluminum-shingle-log-home": G + "9.jpg", "copper-aluminum-shingle-cabin": "Aluminum-Lock-Copper-Cabin.jpg.jpeg",
          "green-aluminum-shingle-log-home": "Aluminum-Lock-Green-Cabin.jpg-rhzcet8emrao9i0qckbe3leqw21ibgoxfmis19ckl4.jpeg",
          "blue-aluminum-roof-high-school": "Aluminum-Lock-High-School.jpg", "aluminum-shingle-color-chart": "Aluminum-Lock-Roofing-Colors.jpg.jpeg"}
for name, f in CLIENT.items():
    save(os.path.join(DL, f), name)
from PIL import Image as _I
lg = _I.open(os.path.join(DL, "12Aluminum-Lock-Logo-no-background.png")).convert("RGBA")
lg.thumbnail((520, 520)); lg.save(os.path.join(OUT, "aluminum-lock-roofing-logo-light.png"), optimize=True)
lg.save(os.path.join(OUT, "aluminum-lock-roofing-logo-light.webp"), "WEBP", quality=92); meta["aluminum-lock-roofing-logo-light"] = list(lg.size) + [0]
lg2 = _I.open(os.path.join(DL, "Aluminum-Lock-Logo-no-background-2.png")).convert("RGB"); lg2.thumbnail((600, 600))
lg2.save(os.path.join(OUT, "aluminum-lock-roofing-logo.png"), optimize=True); meta["aluminum-lock-roofing-logo"] = list(lg2.size) + [0]
fav = _I.open(os.path.join(DL, "Aluminum-Lock-Roofing-Monogram-logo-1.png")).convert("RGBA"); fav.thumbnail((64, 64)); fav.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
json.dump(imap, open(os.path.join(HERE, "imgmap.json"), "w"), indent=0)
big = {k: v for k, v in meta.items() if v[2] >= 150}
print(len(meta), "images;", len(imap), "from page content; over 150KB:", big)
