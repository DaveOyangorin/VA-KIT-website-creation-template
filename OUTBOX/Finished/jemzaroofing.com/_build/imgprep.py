"""Converts Jemza's own photos (downloaded from jemzaroofing.com, 17 Oct 2026) to local WebP.
  python -I imgprep.py <pylib> <dl_dir> <out_img_dir>
Every photo is a real Jemza job photo (drone and crew shots). Low-res duplicates of the same shot are skipped."""
import sys, os, json
sys.path.insert(0, sys.argv[1])
from PIL import Image
DL, OUT = sys.argv[2], sys.argv[3]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
jobs = []
def add(prefix, folder, nums, maxw=1400):
    for i, n in enumerate(nums, 1):
        jobs.append((f"{prefix}-{i:02d}", f"img__gallery__{folder}{n}.jpg", maxw))
add("chimney-shroud", "ChimneyCap__full__", range(1, 18))
add("chimney", "chimney__full__", range(1, 11))               # 11-17 are 400px copies of 1-7
add("asphalt-shingle-roof", "asphalt-shingles__full__", range(1, 7))
add("roof-project", "full__", [1, 2, 3, 4, 5, 6, 7, 8, 9, 26, 27, 28, 29, 30, 31, 32, 33])
add("gutter-soffit-fascia", "gutter-soffit-fascia__full__", range(1, 11))
add("metal-roof", "metal-roofing__full__", [1, 2, 3, 5, 6, 7, 9, 10, 11])  # 4 and 8 repeat 1 and 2
add("new-roof", "new__full__", range(1, 6))
add("ballasted-paver-roof", "Pavers_and_ballasted__full__", range(1, 3))
add("snow-bars", "Snow_bars__full__", range(1, 3))
add("metal-wall-panels", "wall-panels__full__", range(1, 7))
jobs += [("metal-and-shingle-home-salt-lake", "img__video__slider.jpg", 1900), ("rooftop-chimney-shroud-deck", "img__gallery__serv2.jpg", 1600),
         ("metal-roof-stone-home", "img__gallery__serv4.jpg", 1600), ("roof-tear-off-crew", "img__gallery__serv1.jpg", 1600),
         ("snow-covered-new-roof", "img__video__1.jpg", 1200), ("shingle-roof-new-build", "img__video__2.jpg", 1200)]
# full-bleed photos (home hero, film strip, closing band) get a larger file
BIG = {"metal-roof-05", "new-roof-01", "new-roof-02", "metal-roof-07", "chimney-shroud-14", "roof-project-15", "metal-roof-01"}
meta = {}
for name, src, maxw in jobs:
    if name in BIG: maxw = 2000
    p = os.path.join(DL, src)
    if not os.path.exists(p): print("MISSING", src); continue
    im = Image.open(p); im = im.convert("RGB")
    try:
        from PIL import ImageOps; im = ImageOps.exif_transpose(im)
    except Exception: pass
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    q = 80
    while True:
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q, method=6)
        kb = os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024
        if kb <= (320 if name in BIG else 180) or q <= 55: break
        q -= 7
    meta[name] = [im.width, im.height, kb]
logo = Image.open(os.path.join(DL, "img__logo.png")).convert("RGBA")
logo.save(os.path.join(OUT, "jemza-roofing-logo.png"), optimize=True)
lw = logo.resize((408, 152)); lw.save(os.path.join(OUT, "jemza-roofing-logo.webp"), "WEBP", quality=90)
meta["jemza-roofing-logo"] = [408, 152, os.path.getsize(os.path.join(OUT, "jemza-roofing-logo.webp")) // 1024]
Image.open(os.path.join(DL, "img__favicon.png")).save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
print(len(meta), "images", sum(v[2] for v in meta.values()), "KB; max", max(v[2] for v in meta.values()))
