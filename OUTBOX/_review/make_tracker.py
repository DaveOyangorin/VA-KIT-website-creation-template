import sys, re
sys.path.insert(0, sys.argv[1])
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

KIT = r"C:\Users\DaveDeibu\Desktop\VA-KIT\VA-KIT"
OUT = sys.argv[2]
md = open(KIT + r"\ARTIFACT-LINKS.md", encoding="utf-8").read()

SHARED = {"customroofs.biz", "mandmgutters.com", "roofwiseut.com", "jordanriverroofing.com", "aluminumlockroofing.com", "aestheticroofing.com", "amcoroof.com", "roofamc.com",
          "oakleyroofingslc.com", "jemzaroofing.com", "jandnroofing.com", "gprroofing.com", "pioneerroofingutah.com", "ezroofingnow.com", "skybridgeroofings.com",
          "roofrepairsaltlakecity.com", "utahoneroofing.com", "xperienceroofing.com", "utahroofingpros.com"}
# Mobile header fix (sticky header + mobile menu panel), applied to every redesign and republished 18 Oct 2026.
MOBILE_FIX = "Fixed and republished 18 Oct"
STATUS = {
    "actionyardcare.com": ("Premium", "Built premium from the start (21 Oct)"),
    "danielswildlife.com": ("Premium", "Built premium from the start (21 Oct)"),
    "greenjanitorialservice.com": ("Premium", "Built premium from the start (21 Oct)"),
    "emetplumbingservices.com": ("Premium", "Built premium from the start (21 Oct)"),
    "everworklandscape.com": ("Premium", "Built premium from the start (21 Oct)"),
    "iraut.com": ("Premium", "Built premium from the start (21 Oct)"),
    "applianceserviceut.com": ("Premium", "Built premium from the start (21 Oct)"),
    "triplejlandscaping.com": ("Premium", "Built premium from the start (21 Oct)"),
    "joestreecareutah.com": ("Premium", "Built premium from the start (21 Oct)"),
    "utahbluechipcarpetcleaning.com": ("Premium", "Built premium from the start (21 Oct)"),
    "trustyappliancerepairutah.com": ("Premium", "Built premium from the start (21 Oct)"),
    "vogldirect.com": ("Premium", "Built premium from the start (21 Oct)"),
    "ahc-utah.com": ("Premium", "Built premium from the start (21 Oct)"),
    "mountainwindowcleaning.com": ("Premium", "Built premium from the start (21 Oct)"),
    "rwkconstruction.com": ("Premium", "Built premium from the start (21 Oct)"),
    "5starkb.com": ("Premium", "Built premium from the start (21 Oct)"),
    "acs-hoa.com": ("Premium", "Built premium (21 Oct); v2 full-width photo banner added (21 Oct)"),
    "equitypmusa.com": ("Premium", "Built premium (21 Oct); v2 full-width photo banner added (21 Oct)"),
    "abode.cleaning": ("Premium", "Built premium from the start (21 Oct)"),
    "lockthesmithut.com": ("Premium", "Built premium (21 Oct); v2 full-width photo banner added (21 Oct)"),
    "saltcityroofers.com": ("Premium", "Premium redesign (v2) published 21 Oct"),
    "xperienceroofing.com": ("Premium", "Premium redesign (v2) published 21 Oct"),
    "sandsroofingutah.com": ("Premium", "Premium redesign (v2) published 20 Oct"),
    "rhinofoundationsystems.com": ("Premium", "Built premium from the start (20 Oct)"),
    "pestx.org": ("Premium", "Built premium (21 Oct); v2 full-width photo banner added (21 Oct)"),
    "therepairpros.com": ("Premium", "Built premium from the start (21 Oct)"),
    "ezelectric.com": ("Premium", "Built premium from the start (21 Oct)"),
    "rasmussenlandscapes.com": ("Premium", "Built premium from the start (21 Oct)"),
    "foundationrepairogden.com": ("Premium", "Premium redesign (v2) published 21 Oct"),
    "skybridgeroofings.com": ("Premium", "Built premium from the start (18 Oct)"),
    "oakleyroofingslc.com": ("Premium", "Built premium from the start (17 Oct)"),
    "mandmgutters.com": ("Premium", "Premium redesign (v2) published 17 Oct"),
    "roofwiseut.com": ("Premium", "Premium redesign (v2) published 17 Oct"),
    "jordanriverroofing.com": ("Premium", "Premium redesign (v2) published 17 Oct"),
    "jemzaroofing.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "jandnroofing.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "gprroofing.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "pioneerroofingutah.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "ezroofingnow.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "customroofs.biz": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "aluminumlockroofing.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "aestheticroofing.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "amcoroof.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
    "roofamc.com": ("Premium", "Premium redesign (v2) published 18 Oct"),
}

sections = re.split(r"\n### ", md.split("## Website redesigns (this kit)")[1].split("### Reports only")[0])
rows = []
for sec in sections:
    sec = sec.strip()
    if not re.match(r"[a-z0-9]", sec):  # domains may start with a digit (5starkb.com)
        continue
    head = sec.split("\n", 1)[0]
    m = re.match(r"(\S+): (.+?)(?: \((.+)\))?$", head)
    if not m: continue
    dom, biz, city = m.group(1), m.group(2), m.group(3) or ""
    get = lambda k: (re.search(r"- \*\*" + k + r":\*\* (.+)", sec) or [None, ""])[1]
    link = get("Preview link")
    made = re.match(r"(\d+ \w+ \d{4})", get("Made") or "")
    what = get("What it is")
    pages = re.search(r"([\d,]+) (?:real )?(?:pages|URLs)", what)
    blog = re.search(r'New blog post: "(.+?)"', what)
    warn = "; ".join(w.strip().rstrip(".") for w in re.findall(r"⚠([^⚠]+?)(?=⚠|New blog post|$)", what))
    wo = re.search(r"- \*\*Waiting on:\*\*(.*?)(?=\n### |\Z)", sec, re.S)
    waiting = ""
    if wo:
        t = wo.group(1).strip()
        items = [l.strip()[2:] for l in t.splitlines() if l.strip().startswith("- ")]
        waiting = "; ".join(items) if items else t
    mk = get("Made") or ""
    auto = ("Premium", "Built premium from the start (" + made.group(1) + ")") if made and "premium from the start" in mk else None
    st = STATUS.get(dom) or auto or ("Basic (v1)", "Premium rebuild still to do")
    fl = re.search(r"- \*\*Files:\*\* `(?:OUTBOX\\)?(.+?)\\?`", sec)
    folder = KIT + "\\OUTBOX\\" + (fl.group(1).rstrip("\\") if fl else dom)
    mob = get("Mobile header") or (MOBILE_FIX if link else "")
    rows.append([dom, biz, city, link, get("Sharing") or "Anyone with the link",
                 made.group(1) if made else "", st[0], st[1], pages.group(1) if pages else "", blog.group(1) if blog else "",
                 folder, mob, waiting, warn])

reports = re.findall(r"^\| ([a-z0-9.\-]+\.[a-z]+) \| (.+?) \| `(.+?)` \|$", md.split("### Reports only")[1].split("## Other previews")[0], re.M)
older = re.findall(r"^\| (.+?) \| (https://claude\.ai/artifact/\S+) \| (.+?) \|$", md.split("## Other previews")[1], re.M)

NAVY, COPPER, PAPER = "1F2A30", "B5652F", "F6F1EA"
thin = Side(style="thin", color="DDD5CA")
B = Border(bottom=thin)
H = Font(bold=True, color="FFFFFF", name="Calibri", size=11)
HF = PatternFill("solid", fgColor=NAVY)
LINK = Font(color="0B57D0", underline="single")
wrap = Alignment(wrap_text=True, vertical="top")
FILL = {"Premium": PatternFill("solid", fgColor="D9EFE4"), "Built, not published": PatternFill("solid", fgColor="FFF1C9"), "Basic (v1)": PatternFill("solid", fgColor="F8DCD6")}


def sheet(ws, headers, data, widths, link_cols=(), file_cols=()):
    ws.append(headers)
    for c in ws[1]:
        c.font, c.fill, c.alignment = H, HF, Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 30
    for r in data:
        ws.append(r)
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment, c.border = wrap, B
            if c.column in link_cols and c.value:
                c.hyperlink, c.font = c.value, LINK
            if c.column in file_cols and c.value:
                c.hyperlink, c.font = "file:///" + c.value.replace("\\", "/"), LINK
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = ws.dimensions


wb = Workbook()
s = wb.active; s.title = "Summary"
prem = sum(r[6] == "Premium" for r in rows); built = sum(r[6] == "Built, not published" for r in rows); basic = sum(r[6] == "Basic (v1)" for r in rows)
s["A1"] = "Client website tracker"; s["A1"].font = Font(bold=True, size=18, color=NAVY)
s["A2"] = "Updated 20 Oct 2026: 36 of 38 businesses have a premium preview; 2 are blocked (no source content). Drafts only, nothing is live. Send preview links to Angelo only."; s["A2"].font = Font(italic=True, color="666666")
summary = [("Website redesigns with a preview link", len(rows)), ("  Premium design, published", prem), ("  Premium design built, not yet published", built),
           ("  Basic design, premium rebuild still to do", basic), ("Reports only (no website built yet)", len(reports)), ("Older previews on this account", len(older))]
for i, (k, v) in enumerate(summary, 4):
    s.cell(i, 1, k); s.cell(i, 2, v).font = Font(bold=True, size=12, color=COPPER)
    s.cell(i, 1).border = s.cell(i, 2).border = B
s["A11"] = "Tabs"; s["A11"].font = Font(bold=True, color=NAVY)
for i, t in enumerate(["Redesigns: the sites with a preview link, their status, and what each one is waiting on",
                       "Reports only: the businesses with a website plan report but no build yet",
                       "Older previews: links made in earlier sessions (not in this kit's OUTBOX)"], 12):
    s.cell(i, 1, t)
s.column_dimensions["A"].width = 62; s.column_dimensions["B"].width = 10

ws = wb.create_sheet("Redesigns")
data = [[i + 1] + r for i, r in enumerate(rows)]
sheet(ws, ["#", "Website", "Business", "City", "Preview link", "Sharing", "First made", "Design", "Design status", "Pages", "New blog post", "Files folder", "Mobile header", "Waiting on", "Flags"],
      data, [5, 26, 30, 22, 46, 24, 13, 18, 34, 8, 42, 40, 24, 70, 50], link_cols=(5,), file_cols=(12,))
for row in ws.iter_rows(min_row=2):
    row[7].fill = FILL.get(row[7].value, PatternFill())
    row[7].font = Font(bold=True)

ws = wb.create_sheet("Reports only")
sheet(ws, ["#", "Website", "Business", "Report file"], [[i + 1, d, b, KIT + "\\" + p] for i, (d, b, p) in enumerate(reports)], [5, 32, 36, 90], file_cols=(4,))

ws = wb.create_sheet("Older previews")
sheet(ws, ["#", "Client / page", "Link", "Last updated"], [[i + 1, a, l, d] for i, (a, l, d) in enumerate(older)], [5, 50, 48, 16], link_cols=(3,))

wb.save(OUT)
print(len(rows), len(reports), len(older), prem, built, basic)
for r in rows: print(r[0], "|", r[3][-22:], "|", r[6], "|", r[8], "|", r[9][:40])
