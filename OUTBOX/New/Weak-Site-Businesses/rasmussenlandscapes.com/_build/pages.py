"""Pages for the rasmussenlandscapes.com redesign: "Your yard. Our work." (their own line).

A landscape company's best argument is its yards, and Rasmussen's own pages are full of seasonal know-how (turn-on in April and May,
the July heat tune-up, October shut-offs, spring and late-summer aeration, three hedge trims a year). So the site is an editorial garden
journal: their job photography large, Fraunces serif, a spruce-and-sod palette from their badge logo, and the signature "Yard year" dial:
turn the year and see what Rasmussen does in your yard that month, each item quoted from the page that describes it.
References (screenshotted 21 Oct 2026): Gardenista (editorial serif, garden photography), Chanticleer (full-bleed garden hero with
a quiet serif line), Longwood Gardens (seasonal programming as the organising idea). Terrain and Monrovia blocked the screenshot.
All 94 URLs and canonicals kept; email landing pages and the invoice page stay noindex and out of the sitemap."""
import html, json, os, re
from engine import img, canon, faq_html
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from fx import blocks
import home_ras
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
CLAIMS = re.compile(r"premier|premiere|best in the business|50 years|fifty years|#1|number one", re.I)
JUNK = re.compile(r"^(Button|Thanks!|Thank you for reaching out!|We will get back to you as soon as possible|Oops, there was an error.*|Get a Free Quote|Call Us!|Slide title|Write your caption here|"
                  r"Need a quote for a yard project\?.*|If you need a quote over the phone, or to speak with a customer service.*|First Name|Email|Phone number|City|What can we help with\?|Services Requested)$", re.I)
NOINDEX = ("email_", "website_estimate_request_submission", "invoice_link_page")
GROUPS = {
    "Design &amp; Build": ["DesignBuild", "dream", "plan", "execute", "demolition", "lawn", "sprinklers_installation", "rock_walls", "water_feature", "patios", "fencing", "sod", "trees_shrubs_flowers", "garden_boxes", "specialty_excavation"],
    "Maintenance": ["Services", "mow", "fertilize", "aerate6eed311a", "clean_up", "weeding", "hedging", "plant_reduction", "dead_heading_flowers", "fall_cleanup", "soils", "sprinkler_maintenance", "common_yard_issues", "cut", "fabric", "edging"],
    "Other services": ["other_services", "sprinklers", "snow_removal", "holiday_lighting", "sod_maintenence", "brush_cutting", "in_ground_trampolines", "manual_labor_projects", "demolition_structures", "power_washing", "fence_staining", "pond_cleaning"],
    "About": ["about_us", "Contact", "serivce_areas", "team", "values", "history", "project_page", "project_pagee7b6dd53", "philanthropy", "giving_back", "media", "blog", "testimonials", "portfolio", "Projects", "service"],
    "Values": ["change", "integrity", "positive", "choice", "productivity", "progression", "vision", "unity"]}
GROUP_HUB = {"Design &amp; Build": "DesignBuild/", "Maintenance": "Services/", "Other services": "other-services/", "About": "about-us/", "Values": "values/", "Service areas": "serivce-areas/"}
LABEL = {"DesignBuild": "Design &amp; Build", "lawn": "Soil Preparation", "sprinklers_installation": "Sprinkler Installation", "rock_walls": "Rock Walls", "water_feature": "Water &amp; Fire Features",
         "patios": "Patios &amp; Pathways", "sod": "Sod Installation", "trees_shrubs_flowers": "Trees, Shrubs &amp; Flowers", "Services": "Maintenance", "mow": "Mowing", "fertilize": "Fertilizing",
         "aerate6eed311a": "Aeration", "clean_up": "Leaves, Debris &amp; Organization", "weeding": "Plant Bed Weeding", "hedging": "Hedging &amp; Pruning", "plant_reduction": "Plant Reduction",
         "dead_heading_flowers": "Deadheading Flowers", "fall_cleanup": "Fall &amp; Spring Cleanup", "soils": "Soil Amendments", "sprinkler_maintenance": "Sprinkler Maintenance",
         "common_yard_issues": "Common Lawn Issues", "other_services": "Other Services", "sprinklers": "Sprinklers", "snow_removal": "Snow Removal", "holiday_lighting": "Holiday Lighting",
         "sod_maintenence": "Sod Patching", "brush_cutting": "Brush Cutting", "edging": "Edging", "specialty_excavation": "Specialty Excavation", "in_ground_trampolines": "In-Ground Trampolines",
         "manual_labor_projects": "Manual Labor Projects", "demolition_structures": "Demolition: Structures", "about_us": "About Us", "Contact": "Contact Us", "serivce_areas": "Service Areas",
         "team": "Team", "values": "Values", "history": "History", "project_page": "Community", "project_pagee7b6dd53": "Community Projects", "media": "Media", "blog": "Blog",
         "testimonials": "Testimonials", "portfolio": "Portfolio", "Projects": "Projects", "service": "Services", "power_washing": "Power Washing", "fence_staining": "Fence Staining",
         "pond_cleaning": "Pond Cleaning", "garden_boxes": "Garden Boxes", "giving_back": "Giving Back", "philanthropy": "Philanthropy", "cut": "Lawn Cutting", "fabric": "Weed Fabric",
         "dream": "Dream", "plan": "Plan", "execute": "Execute", "demolition": "Demolition", "fencing": "Fencing", "the_avenues": "The Avenues", "milcreek": "Millcreek"}
CITY_KEYS = ["salt_lake_city", "the_avenues", "milcreek", "holladay", "sandy", "draper", "west_jordan", "herriman", "bountiful", "layton", "syracuse", "ogden", "tooele", "park_city",
             "alpine", "highland", "orem", "provo"]
PHOTO = {"DesignBuild": "ras-rock-steps", "dream": "ras-garden-path", "plan": "ras-excavator-rocks", "execute": "ras-excavator", "demolition": "ras-excavator", "lawn": "ras-sod-roll",
         "sprinklers_installation": "ras-sprinkler-spray", "rock_walls": "ras-rock-steps", "water_feature": "ras-stone", "patios": "ras-patio", "fencing": "ras-fence", "sod": "ras-sod-roll",
         "trees_shrubs_flowers": "ras-flower-bed", "Services": "ras-bench-lawn", "sprinkler_maintenance": "ras-crew-sprinkler", "sprinklers": "ras-sprinkler-spray", "brush_cutting": "ras-brush-cutting",
         "specialty_excavation": "ras-excavator-rocks", "demolition_structures": "ras-excavator", "sod_maintenence": "ras-crew-sod", "weeding": "ras-flower-bed", "dead_heading_flowers": "ras-zinnia",
         "portfolio": "ras-patio", "Projects": "ras-fire-pit", "about_us": "ras-yard-trees", "history": "ras-bench-lawn", "team": "ras-crew-sod", "service": "ras-garden-path",
         "salt_lake_city": "ras-yard-trees", "the_avenues": "ras-garden-path", "garden_boxes": "ras-flower-bed", "mow": "ras-bench-lawn", "hedging": "ras-yard-trees", "pond_cleaning": "ras-stone"}
cta = K.cta


def header():
    return K.header()


def footer():
    return K.footer()


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com", 1)[1].strip("/")
    return (p + "/") if p else ""


def label_of(k):
    if k in LABEL: return LABEL[k]
    if k in CITY_KEYS: return html.escape(k.replace("_", " ").title())
    return html.escape(k.replace("_", " ").strip().title())


def group_of(k):
    if k in CITY_KEYS: return "Service areas"
    for g, ks in GROUPS.items():
        if k in ks: return g
    return None


def render(k):
    bl = [(t, x) for t, x in blocks(k) if not (t == "li" and len(re.sub(r"<[^>]+>", "", x)) < 40 and not re.search(r"[.!?]$", x))]
    out, ul, seen_h = [], [], set()
    def flush():
        if ul: out.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, x in bl:
        x = x.replace("&nbsp;", " ").strip()
        plain = html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        if not plain or JUNK.match(plain): continue
        if t == "li":
            if CLAIMS.search(plain): continue
            ul.append(x); continue
        flush()
        if t in ("h1", "h2", "h3", "h4"):
            h = re.sub(r"</?(strong|b)[^>]*>", "", x).strip(" *")
            if plain.lower() in seen_h or len(plain) < 2: continue
            seen_h.add(plain.lower())
            out.append(f"<h3>{h}</h3>" if t in ("h3", "h4") else f"<h2>{h}</h2>")
            continue
        if CLAIMS.search(plain):
            sents = [s for s in re.split(r"(?<=[.!?])\s+", plain) if not CLAIMS.search(s)]
            if not sents: continue
            x = html.escape(" ".join(sents))
        if len(plain) < 70 and not re.search(r"[.!?:]$", plain): out.append(f"<h3>{x}</h3>"); continue
        out.append(f"<p>{x}</p>")
    flush()
    s = "\n".join(out)
    s = re.sub(r"(?:<h[23]>[^<]*</h[23]>\s*)+$", "", s.strip())        # trailing CTA headings
    s = re.sub(r"<h([23])>([^<]*)</h\1>\s*(?=<h[23]>)", "", s)          # heading followed directly by heading
    return s


TEMPLATE = re.compile(r"Write a |short text area|Project Name|Short project description|555|Click to add|Tell potential customers|Every successful product|Intuition alone|You also need to do|"
                      r"Write about|let the images tell|Book Now|Button|Explore More|Inspired by what you see|It.s only the beginning|Describe its benefits|Make sure potential|product|"
                      r"your audience|this section|placeholder|lorem", re.I)


def fallback(k):
    """pages whose copy isn't in p/h tags: take the page text between the nav and the footer, minus template filler."""
    t = EXT[k]["text"]; nav = "Testimonials Get a Quote"; i = t.find(nav); j = t.find("Home Portfolio Services", i + 5)
    if i < 0: return ""
    body = re.sub(r"\s+", " ", t[i + len(nav):j if j > 0 else None]).strip()
    words = body.split(" ")
    if len(words) > 2 and words[0] == words[1]: body = " ".join(words[2:])            # "Change Change ..." page-title echo
    sents = [x.strip() for x in re.split(r"(?<=[.!?])\s+", body) if x.strip()]
    keep = [x for x in sents if not TEMPLATE.search(x) and not CLAIMS.search(x) and len(x) > 25]
    return "".join(f"<p>{html.escape(x)}</p>" for x in keep)


def first_sentence(k):
    for t, x in blocks(k):
        p = html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        if t == "p" and len(p) > 90 and not CLAIMS.search(p) and not JUNK.match(p): return p
    return ""


BLURB = {"Design &amp; Build": "We design, prepare and build yards: demolition, soil, sprinklers, rock walls, water features, patios, fencing, sod and plants.",
         "Maintenance": "Weekly mowing, fertilizing, aeration, weeding, hedging and pruning, cleanups and sprinkler maintenance across the Salt Lake Valley.",
         "Other services": "Snow removal, holiday lighting, sod patching, brush cutting, edging, specialty excavation and manual labor projects.",
         "About": "A landscaping company in South Salt Lake that designs, builds and maintains residential and commercial yards.",
         "Values": "One of the values the Rasmussen Landscapes team works by every day, with our employees and our customers.",
         "Service areas": "Mowing, cleanups, design and building for homes and businesses in this area."}


def meta_of(k, lab):
    m = first_sentence(k) or BLURB.get(group_of(k) or "About", "")
    base = f"{html.unescape(lab)} from Rasmussen Landscapes in South Salt Lake. "
    m = base + m
    if len(m) > 160: m = m[:157].rsplit(" ", 1)[0] + "..."
    if len(m) < 150: m = (m + " Call (801) 466-0303 for a quote.")[:160]
    return html.escape(m)


def title_of(k, lab):
    lab = html.unescape(lab)
    if k in CITY_KEYS:
        t = f"Landscaping & Yard Care in {lab}, UT | Rasmussen Landscapes"
        if len(t) > 60: t = f"Landscaping in {lab}, UT | Rasmussen Landscapes"
    else:
        t = f"{lab} | Rasmussen Landscapes, South Salt Lake"
        if len(t) > 60: t = f"{lab} | Rasmussen Landscapes"
        if len(t) < 50: t = f"{lab} in South Salt Lake & SLC | Rasmussen Landscapes"
        if len(t) > 60: t = f"{lab} | Rasmussen Landscapes"
        if len(t) < 50 and len(f"{lab} in Salt Lake City | Rasmussen Landscapes") <= 60: t = f"{lab} in Salt Lake City | Rasmussen Landscapes"
    return html.escape(t)


def related(k):
    g = group_of(k)
    if not g or g == "Service areas":
        ks = [c for c in CITY_KEYS if c != k][:10] if g else []
        title = "More service areas"
    else:
        ks = [x for x in GROUPS[g] if x != k and x in EXT][:10]; title = "More in " + g
    if not ks: return ""
    return f'<h2>{title}</h2><ul class="chips">' + "".join(f'<li><a href="@/{path_of(x)}">{label_of(x)}</a></li>' for x in ks) + "</ul>"


def inner_pages():
    out = []
    for k in EXT:
        if k == "home": continue
        lab = label_of(k); g = group_of(k); p = path_of(k)
        body = render(k)
        if len(re.sub(r"<[^>]+>", " ", body).split()) < 40:
            fb = fallback(k)
            if len(fb) > len(body): body = fb
        if k == "Contact":
            body = f'''<p class="answer">Call our customer service team for a quote over the phone or to answer any questions, or send a message and we&rsquo;ll call you to schedule a consultation with a landscape expert.</p>
<dl class="info"><div><dt>Call us</dt><dd><a href="tel:+18014660303">(801) 466-0303</a></dd></div><div><dt>Email us</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Visit us</dt><dd><address>3446 S W Temple St<br>South Salt Lake, UT 84115</address></dd></div></dl>'''
        if k in ("portfolio", "Projects"):
            pics = [("ras-rock-steps", "Natural rock steps"), ("ras-patio", "Covered patio"), ("ras-garden-path", "Garden path"), ("ras-flower-bed", "Perennial bed and flagstone"),
                    ("ras-fire-pit", "Stone fire pit"), ("ras-excavator-rocks", "Boulder placement"), ("ras-sod-roll", "Sod installation"), ("ras-fence", "Wood fence"),
                    ("ras-pavers", "Paver patio"), ("ras-stone", "Natural stone"), ("ras-yard-trees", "Mature yard"), ("ras-bench-lawn", "Lawn and garden bench")]
            body += '<div class="pgal">' + "".join(f'<figure>{img(n, c + ", a Rasmussen Landscapes project")}<figcaption>{c}</figcaption></figure>' for n, c in pics) + "</div>"
        if k == "blog":
            body += f'<div class="posts"><a class="post-card" href="@/{p_blog.SLUG}"><b>{p_blog.H1}</b><p>Why waiting until about Mother&rsquo;s Day helps roots, and how to use Utah&rsquo;s weekly watering guide.</p><em>Read it {ARROW}</em></a></div>'
        if k == "serivce_areas":
            body += '<h2>City pages</h2><ul class="chips">' + "".join(f'<li><a href="@/{path_of(c)}">{label_of(c)}</a></li>' for c in CITY_KEYS) + "</ul>"
        if k in ("DesignBuild", "Services", "other_services", "values", "about_us", "service"):
            hub = {"DesignBuild": "Design &amp; Build", "Services": "Maintenance", "other_services": "Other services", "values": "Values", "about_us": "About", "service": "Design &amp; Build"}[k]
            body += f"<h2>All {hub.lower()} pages</h2><ul class=\"chips\">" + "".join(f'<li><a href="@/{path_of(x)}">{label_of(x)}</a></li>' for x in GROUPS[hub] if x != k and x in EXT) + "</ul>"
        else:
            body += related(k)
        noindex = k.startswith(NOINDEX[0]) or k in NOINDEX[1:]
        h1 = f"Landscaping in {html.unescape(lab)}" if k in CITY_KEYS else html.unescape(lab)
        if k in CITY_KEYS: h1 += ", Utah"
        crumbs = [(g.replace("&amp;", "&amp;"), GROUP_HUB[g])] if g and GROUP_HUB.get(g) and GROUP_HUB[g] != p else []
        im = PHOTO.get(k)
        out.append(K.page(p, lab, html.escape(h1), "Quotes over the phone &middot; (801) 466-0303", g.replace("&amp;", "&amp;") if g else "Rasmussen Landscapes",
                          title_of(k, lab), meta_of(k, lab), body or "<p>Call (801) 466-0303 or send us a message and we&rsquo;ll get back to you as soon as possible.</p>",
                          image=im, alt=f"{html.unescape(lab)}: a Rasmussen Landscapes project" if im else "", art=None if im else '<div class="leafmark" aria-hidden="true"></div>',
                          crumbs=crumbs, canonical=EXT[k]["canon"] or canon(p), form_side=(k == "Contact"),
                          robots="noindex, follow" if noindex else None, sitemap=not noindex,
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"Landscaping in {html.unescape(lab)}, UT", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": html.unescape(lab) + ", UT"}}] if k in CITY_KEYS else
                                 ([{"@type": "Service", "@id": canon(p) + "#service", "name": html.unescape(lab), "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": "South Salt Lake, UT"}}] if g in ("Design &amp; Build", "Maintenance", "Other services") else [])))
    return out


def make_pages():
    out = [home_ras.home()] + inner_pages() + [p_blog.page(K)] + \
          [K.notfound((("Design &amp; Build", "DesignBuild/"), ("Maintenance", "Services/"), ("Contact", "Contact/")))]
    return [dict(x, body=Q(x["body"])) for x in out]
