"""Converts the client's own photos to WebP (<150 KB) into site/assets/img.

  python -I imgprep.py <pylib> <client_dl_dir> <img_out>

Only photos from customroofs.biz are used. Left out on purpose: the stock photo of a roofer
(image1219.jpg), the stock "5 stars" photo, and the blue icon graphics.
Writes imgmeta.json (name -> [w, h, kb]) and imgmap.json (remote url -> name) next to this file.
"""
import sys, os, json, time, urllib.request
sys.path.insert(0, sys.argv[1])
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DL, OUT = sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
meta, imap = {}, {}
W = "https://customroofs.biz/wp-content/uploads/"

# local name: (file in DL, remote url)
CLIENT = {
    "copper-standing-seam-over-old-roof": ("Custom-Roofing-copper-over-old-scaled.jpg", W + "2025/10/Custom-Roofing-copper-over-old.jpg"),
    "copper-dome-roof-installer": ("Custom-Roofing-copper-roof-with-man-on-top.jpeg", W + "2024/05/Custom-Roofing-copper-roof-with-man-on-top.jpeg"),
    "red-black-metal-siding-barn": ("Custom-Roofing-red-and-black-siding-1.jpg", W + "2025/10/Custom-Roofing-red-and-black-siding-1.jpg"),
    "red-black-metal-siding-barn-sunset": ("Custom-Roofing-red-and-black-siding-2.jpg", W + "2025/10/Custom-Roofing-red-and-black-siding-2.jpg"),
    "roof-in-progress-mountain-view": ("Custom-Roofing-roof-in-progress.png", W + "2025/10/Custom-Roofing-roof-in-progress.png"),
    "copper-roofing-panels": ("IMG_2229-1-scaled.jpeg", W + "2022/11/IMG_2229-1.jpeg"),
    "copper-arched-roof-building": ("custom-roofing-A-Frame-Barn-shape.jpg", W + "2024/05/custom-roofing-A-Frame-Barn-shape.jpg"),
    "copper-chimney-cap": ("custom-roofing-copper-chimney-cap.jpg", W + "2024/09/custom-roofing-copper-chimney-cap.jpg"),
    "copper-curved-dormer": ("custom-roofing-copper-dormer.jpg", W + "2024/09/custom-roofing-copper-dormer.jpg"),
    "copper-roof-aerial": ("custom-roofing-copper-roof-birds-eye.jpg", W + "2024/09/custom-roofing-copper-roof-birds-eye.jpg"),
    "copper-siding-install": ("custom-roofing-copper-siding-on-red-brick-house.jpg", W + "2024/09/custom-roofing-copper-siding-on-red-brick-house.jpg"),
    "dark-roof-homes-aerial": ("custom-roofing-slate-roof.webp", W + "2024/05/custom-roofing-slate-roof.webp"),
    "cedar-shake-siding-gable": ("custom-roofing-wooden-siding.webp", W + "2024/05/custom-roofing-wooden-siding.webp"),
    "copper-roof-home": ("customs-05-e1715026133985.png", W + "2022/11/customs-05-e1715026133985.png"),
    "copper-flashing-on-truck": ("f45fe49f-.jpg", W + "2025/10/f45fe49f-.jpg"),
    "copper-siding-detail": ("IMG_2357-1.jpeg", W + "2022/11/IMG_2357-1.jpeg"),
    "copper-roof-ladder-trees": ("custom-roofing-copper-roof-with-ladder-and-trees-in-background.jpg", W + "2024/09/custom-roofing-copper-roof-with-ladder-and-trees-in-background.jpg"),
}


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


for name, (f, url) in CLIENT.items():
    local = os.path.join(DL, f)
    if not os.path.exists(local):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            open(local, "wb").write(urllib.request.urlopen(req, timeout=30).read()); time.sleep(1.5)
        except Exception as e:
            print("FAIL", url, e); continue
    save(local, name); imap[url] = name

# logo: silver lettering; knock out the white background so it sits on the dark header
lg = Image.open(os.path.join(DL, "logo-1.webp")).convert("RGBA")
px = lg.load()
for y in range(lg.height):
    for x in range(lg.width):
        r, g, b, a = px[x, y]
        m = min(r, g, b)
        if m > 235 and max(r, g, b) - m < 12: px[x, y] = (r, g, b, 0)
        elif m > 215 and max(r, g, b) - m < 12: px[x, y] = (r, g, b, int(a * (235 - m) / 20))
bb = lg.getbbox(); lg = lg.crop(bb); lg.thumbnail((520, 520))
lg.save(os.path.join(OUT, "custom-roofing-logo.png"), optimize=True)
lg.save(os.path.join(OUT, "custom-roofing-logo.webp"), "WEBP", quality=92, method=6)
meta["custom-roofing-logo"] = list(lg.size) + [os.path.getsize(os.path.join(OUT, "custom-roofing-logo.webp")) // 1024]
fav = lg.crop((0, 0, lg.height, lg.height)); fav.thumbnail((64, 64)); fav.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
json.dump(imap, open(os.path.join(HERE, "imgmap.json"), "w"), indent=0)
print(len(meta), "images;", {k: v for k, v in meta.items()})
