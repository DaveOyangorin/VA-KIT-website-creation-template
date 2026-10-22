"""imgprep.py <pylib> <dl_dir> <out_img_dir> : converts the images listed in JOBS (imgjobs.json next to this file) to WebP
(<=150 KB where possible), writes imgmeta.json. Logos (name ending -logo / -logo-white) are kept as PNG; ink-* drawings keep their alpha.
imgjobs.json: [[local_name, source_file, max_width], ...]"""
import sys, os, json
sys.path.insert(0, sys.argv[1])
from PIL import Image, ImageOps
DL, OUT = sys.argv[2], sys.argv[3]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
jobs = json.load(open(os.path.join(HERE, "imgjobs.json"), encoding="utf-8"))
meta = json.load(open(os.path.join(HERE, "imgmeta.json"))) if os.path.exists(os.path.join(HERE, "imgmeta.json")) else {}
for name, src, cap in jobs:
    im = ImageOps.exif_transpose(Image.open(os.path.join(DL, src)))
    if name.endswith(("-logo", "-logo-white", "-logo-dark")):
        im = im.convert("RGBA"); im.thumbnail((cap, cap))
        im.save(os.path.join(OUT, name + ".png"), optimize=True); meta[name] = [im.width, im.height, os.path.getsize(os.path.join(OUT, name + ".png")) // 1024]; continue
    if name.startswith("ink-"):  # the brand's ink-wash drawings keep their transparent ground
        im = im.convert("RGBA"); im.thumbnail((cap, cap), Image.LANCZOS)
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=84, method=6)
        meta[name] = [im.width, im.height, os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024]; continue
    im = im.convert("RGB")
    if im.width > cap: im = im.resize((cap, round(im.height * cap / im.width)), Image.LANCZOS)
    q = 82
    while True:
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q, method=6)
        kb = os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024
        if kb <= 150 or q <= 56: break
        q -= 6
    meta[name] = [im.width, im.height, kb]
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
print({k: v for k, v in meta.items()})
