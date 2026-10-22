"""dryhouse.com: facts and settings (19 Oct 2026).
Business: Rocky Mountain Waterproofing (legal name Modern Damp Proofing, Inc., DBA Rocky Mountain Waterproofing; name registered
1996; in business since 1960). The domain does not match the name, but the live site, logo, phone and address are all theirs.
Name, address, phones, fax and hours copied from the client's own site (home page location block and header):
8401 S 4300 W, West Jordan, UT 84088 · Office 801-282-2100 · Toll free (877) 282-2100 · Fax 801-282-2111 ·
Open Mon-Fri 7:00 AM - 4:00 PM (Mountain). Google profile: 4.8 stars from 50 reviews (report), not shown until confirmed.
Tracking kept as on the live site: gtag.js with UA-138052846-1 (a Universal Analytics ID; Google stopped processing UA data in
2023, so it no longer records anything: flagged in the notes)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "dryhouse.com"
U = "https://dryhouse.com/"
TRAIL = False
NAME = "Rocky Mountain Waterproofing"
LEGAL = "Modern Damp Proofing, Inc."
TODAY = "2026-10-19"
HOME_OG = "foundation-waterproofed"
THEME_COLOR = "#1d1d1f"
FONTS = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Instrument+Sans:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
S = {"phone": "801-282-2100", "tel": "+18012822100", "toll": "(877) 282-2100", "tel_toll": "+18772822100", "fax": "801-282-2111",
     "street": "8401 S 4300 W", "city": "West Jordan", "st": "UT", "zip": "84088", "hours": "Mon&ndash;Fri 7:00 AM &ndash; 4:00 PM (Mountain)",
     "fb": "https://www.facebook.com/Rocky-Mountain-Waterproofing-154057997954809/", "tw": "https://twitter.com/rmtwproof",
     "yt": "https://www.youtube.com/channel/UCewoZJJXB6Ed9HS-Ni4IjXw", "li": "https://www.linkedin.com/company/rocky-mountain-waterproofing/",
     "ig": "https://www.instagram.com/rockymountainwaterproofing/", "houzz": "https://www.houzz.com/pro/rockymountainwaterproofing/rocky-mountain-waterproofing",
     "glassdoor": "https://www.glassdoor.com/Overview/Working-at-Rocky-Mountain-Waterproofing-EI_IE3048505.11,39.htm",
     "chamber": "http://business.westjordanchamber.com/list/member/rocky-mountain-waterproofing-88184"}
TRACK_HEAD = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-138052846-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-138052846-1');
</script>"""
# Cities near the office, all from the client's own service-area list (the full list of 300+ Utah towns is on the home page).
CITIES = ["West Jordan", "South Jordan", "Riverton", "Herriman", "Sandy", "Draper", "Taylorsville", "West Valley City", "Murray", "Salt Lake City", "Lehi", "Bluffdale"]


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "GeneralContractor"], "@id": U + "#business", "name": NAME, "legalName": LEGAL, "url": U,
         "telephone": S["tel"], "faxNumber": "+18012822111", "foundingDate": "1960",
         "logo": U + "assets/img/rmwp-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:00", "closes": "16:00"}],
         "sameAs": [S["fb"], S["tw"], S["yt"], S["li"], S["ig"], S["houzz"]]}
    if full:
        n.update({"description": "Rocky Mountain Waterproofing is a family-owned foundation waterproofing contractor in West Jordan, Utah, in business since 1960: below-grade waterproofing and damp proofing, foundation drains and insulation, horizontal and under-slab waterproofing, and foundation leak repair.",
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in CITIES]})
    return [n]
