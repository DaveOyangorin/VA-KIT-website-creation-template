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
CLIENT = {"roof-work-in-utah-winter": "roof-work-in-Utah-winter.jpg", "utah-roofing-service-areas": "utah-roofing-service-areas.jpg",
          "hero-house": "hero-house.jpg", "metal-roof-chimney-dusk": "iStock-2158006561.jpg", "shingle-damage-closeup": "iStock-2259570783-1.jpg",
          "commercial-roofing-salt-lake-city": "commercial-roofing-salt-lake-city.jpg", "completed-roofing-project-final-inspection": "completed-roofing-project-final-inspection.jpg",
          "multifamily-roof-replacement": "multifamily-roof-replacement.jpg", "residential-roofing-utah-home": "residential-roofing-utah-home.jpg",
          "roof-condition-options-review": "roof-condition-options-review.jpg", "roof-evaluation-appointment": "roof-evaluation-appointment.jpg",
          "roofing-project-utah-blue-home": "roofing-project-utah-blue-home.jpg", "roofing-project-utah-main": "roofing-project-utah-main.jpg",
          "roofing-project-utah-residential": "roofing-project-utah-residential.jpg", "storm-damage-roofing": "storm-damage-roofing.jpg",
          "roofing-services-menu-img": "roofing-services-menu-img.jpg", "utah-service-area-map": "utah-service-area-map.png",
          "repair-first-promise": "repair-first-promise.png", "badge-bbb": "bbb-accredited-roofing-company.png",
          "badge-certainteed-gold-star": "certainteed-gold-star-contractor.png", "badge-certainteed-shinglemaster": "certainteed-select-shinglemaster-certification.png",
          "badge-gephardt": "gephardt-approved-roofing-company.png"}
for name, f in CLIENT.items():
    save(os.path.join(DL, f), name, bgc=(19, 40, 77) if name == "utah-service-area-map" else (255, 255, 255))
UNSPLASH = {"icicles-snow-overhang-roof": "1770128076146-1eae85354f2f.jpg", "icicles-log-cabin-eave": "1642344497711-8fc0a4ce22ed.jpg",
            "snowy-house-evergreens": "1553550319-d8d5393e1c80.jpg", "snow-on-roof-edge-leaves": "1763046041616-062540e57c20.jpg"}
for name, f in UNSPLASH.items():
    save(os.path.join(US, f), name)

# logo (keep PNG with transparency) + favicon
logo = Image.open(os.path.join(DL, "Amcoroof_logo_230.png")).convert("RGBA")
logo.save(os.path.join(OUT, "american-roofing-logo.png"), optimize=True)
logo.save(os.path.join(OUT, "american-roofing-logo.webp"), "WEBP", quality=92)
meta["american-roofing-logo"] = list(logo.size) + [0]
fav = os.path.join(DL, "..", "favicon.png")
if os.path.exists(fav): Image.open(fav).convert("RGBA").resize((64, 64)).save(os.path.join(OUT, "favicon.png"))

json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
json.dump(imap, open(os.path.join(HERE, "imgmap.json"), "w"), indent=0)
big = {k: v for k, v in meta.items() if v[2] >= 150}
print(len(meta), "images;", len(imap), "from page content; over 150KB:", big)
