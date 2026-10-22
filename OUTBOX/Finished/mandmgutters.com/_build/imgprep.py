"""M&M Gutters images (17 Oct 2026). Only the client's own job photos are used, chosen by eye from contact sheets
(index numbers in the scratch sheet index). Not used: Unsplash and Pixabay stock, Shutterstock files, Bannerbear
auto-generated banners, icons, partner logos and badges, and a 3D render.
  python -I imgprep.py <pylib> <dl_dir> <sheet_index.txt> <out_img_dir>"""
import sys, os, re, json
sys.path.insert(0, sys.argv[1])
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
DL, IDX, OUT = sys.argv[2], sys.argv[3], sys.argv[4]
HERE = os.path.dirname(os.path.abspath(__file__))
REAL = set(range(0, 33)) | {36, 46} | set(range(48, 59)) | {67, 68, 69} | set(range(97, 108)) | {117, 118} | set(range(122, 141)) | \
       {143, 144, 145} | set(range(147, 159)) | {162, 163, 165, 166, 167, 168, 182, 189, 194, 198, 209}
BIG = {"mg-6540": 2400, "20140530-144851": 2000, "heat-cable1": 1920, "heat-cable5": 1920, "heat-cable7": 1920, "down-net-http20240904-65-v2w3su-1": 2000}
# These came from the old page builder with decorative frames (black borders, orange or blue corner blocks, white
# card backgrounds) baked into the file. The frame is trimmed off so only the photo is shown.
FRAMED = {"benefits-of-a-heated-roof-system", "common-types-of-roofing-problems", "cutting-edge-technology-that-keeps-you-prepared",
          "enjoy-a-safer-and-worry-free-home", "fast-reliable-roofing-you-can-rely-on", "heat-cables-and-the-most-efficient-option-for-utah-homes",
          "heat-cables", "heat-panels", "house", "house-2", "ice-melting", "image-1-117", "image-1", "image-10-with-orange-box", "image-11-with-blue-square",
          "image-2", "image-3-with-blue-square", "image-4-with-orange-square-1", "image-5", "image-6-with-blue-square", "image-9", "image2",
          "parts-of-a-gutter-system", "pillars", "rest-easy-knowing-your-family-and-home-are-safe", "roofing-contractor-services-offered-by-mm",
          "roofing-contractor", "siding-cost-in-salt-lake-city", "siding-repair-services", "trust-our-qualified-contractors-for-your-heating-cables",
          "trust-our-qualified-contractors-for-your-roofing-needs", "utahs-preferred-ice-melt-systems", "why-mm-1", "why-mm", "window", "a-bad-roof-is-unsafe-and-uncomfortable"}


def trim_frame(im, cap=0.16):
    """Walk in from each edge while the line is flat colour (a frame), then step 1% further in to clear soft edges."""
    g = im.convert("L"); w, h = g.size; px = g.load()
    def flat(line):
        d = sum(abs(line[i] - line[i - 1]) for i in range(1, len(line))) / max(1, len(line) - 1)
        return d < 2.2
    def row(y): return [px[x, y] for x in range(0, w, 2)]
    def col(x): return [px[x, y] for y in range(0, h, 2)]
    t = 0
    while t < h * cap and flat(row(t)): t += 1
    b = h - 1
    while h - 1 - b < h * cap and flat(row(b)): b -= 1
    l = 0
    while l < w * cap and flat(col(l)): l += 1
    r = w - 1
    while w - 1 - r < w * cap and flat(col(r)): r -= 1
    # a second pass catches an inner border (e.g. a black frame inside an orange block)
    box = (l, t, r + 1, b + 1)
    if box == (0, 0, w, h): return im
    pad_x, pad_y = int(w * .012), int(h * .012)
    return im.crop((box[0] + pad_x, box[1] + pad_y, box[2] - pad_x, box[3] - pad_y))


rows = [l.split("\t") for l in open(IDX, encoding="utf-8").read().splitlines()]
meta, imap = {}, {}
for i, f, sz in rows:
    if int(i) not in REAL: continue
    base = re.sub(r"^\d{4}_\d{2}_", "", f)
    stem = re.sub(r"(-scaled|_resized|-min)?\.(jpe?g|png|webp)$", "", base, flags=re.I)
    name = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")[:60]
    if name in meta: name += "-" + i
    im = Image.open(os.path.join(DL, f))
    im.draft("RGB", (2000, 2000)); im = im.convert("RGB")
    if name in FRAMED:
        for _ in range(2): im = trim_frame(im)
    cap = BIG.get(name, 1400)   # full-bleed photos get a larger file
    if im.width > cap: im = im.resize((cap, round(im.height * cap / im.width)), Image.LANCZOS)
    q = 80
    while True:
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q, method=6)
        kb = os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024
        if kb <= (330 if name in BIG else 170) or q <= 55: break
        q -= 8
    meta[name] = [im.width, im.height, kb]
    imap[base.lower()] = name     # original upload file name (lower-case) -> local name
logo = Image.open(os.path.join(DL, [f for _, f, _ in rows if "LOGO-FILE" in f][0])).convert("RGB")
logo.thumbnail((520, 520)); logo.save(os.path.join(OUT, "mm-gutters-exteriors-logo.png"), optimize=True); logo.save(os.path.join(OUT, "mm-gutters-exteriors-logo.webp"), "WEBP", quality=88)
meta["mm-gutters-exteriors-logo"] = [logo.width, logo.height, 0]
fav = logo.copy(); fav.thumbnail((96, 96)); fav.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
json.dump(imap, open(os.path.join(HERE, "imgmap.json"), "w"), indent=0)
print(len(meta), "images,", sum(v[2] for v in meta.values()), "KB; max", max(v[2] for v in meta.values()))
