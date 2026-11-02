import base64, pathlib, sys
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); img = pathlib.Path(sys.argv[3])
def d(p, mime): return f"data:{mime};base64," + base64.b64encode((img / p).read_bytes()).decode()
h = src.read_text(encoding="utf-8")
h = h.replace("__MARK__", d("ep-mark.png", "image/png")).replace("__PORTRAIT__", d("miquelle-portrait-800.webp", "image/webp")).replace("__BOOK__", "https://earthenphoenix.com/appointment-8682")
out.parent.mkdir(parents=True, exist_ok=True); out.write_text(h, encoding="utf-8"); print(out, len(h))
