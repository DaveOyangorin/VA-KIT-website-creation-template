"""sterlingtreeco.godaddysites.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the one-page GoDaddy site (no canonical tag). Same URL; one new post added.
From the site: Sterling Tree Co.; "Tree Care in Salt Lake City, Utah"; "for the love of trees"; "We strive to provide the absolute best
quality tree care in Salt Lake City, second to none. Our company was built on a deep rooted interest in arboriculture as well as providing
a fun, personal customer service experience."; ISA certified arborists; services: tree trimming and removals, hedges and ornamental
pruning, land clearing, cabling / bracing, storm damage; "Our Team of Climbing Arborists"; "Call Today for a free estimate"; 315-863-6747;
1826 S 1100 E, Salt Lake City, UT 84105.
NAP: Google listing "Sterling Tree Company", 1826 S 1100 E, Salt Lake City, UT 84105, +1315-863-6747 (used, copied exactly; same as the site).
The phone is a 315 (New York) area code: copied exactly; ask if there is a local number (report note).
Left out until confirmed: the 5-star / 185-review rating.
Photos: their three own photos (a climber in a London plane above Salt Lake City, a climber high in a tree, an elm in snow). No logo exists;
the wordmark is set in the site's display font."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "sterlingtreeco.godaddysites.com"
U = "https://sterlingtreeco.godaddysites.com/"
TRAIL = False
NAME = "Sterling Tree Co."
TODAY = "2026-10-22"
HOME_OG = "st-hero"
THEME_COLOR = "#173026"
FONTS = "https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "st-logo"
CTA_PATH = "#estimate"
CTA_LABEL = "Free estimate"
CTA_TITLE = "For the love of <em>trees.</em>"
CTA_TEXT = "Call 315-863-6747 today for a free estimate from Sterling Tree Co.'s ISA certified arborists in Salt Lake City."
SIDE_TITLE = "ISA certified arborists. Free estimates."
PHONES = [("Call", "315-863-6747", "+13158636747")]
EMAIL = ""
HOURS = ""
ADDRESS = [("Salt Lake City", "1826 S 1100 E<br>Salt Lake City, UT 84105")]
AREAS = ["Salt Lake City", "the Salt Lake Valley"]
SOCIAL = []
BLURB = "Tree care in Salt Lake City by ISA certified, climbing arborists: trimming and removals, hedges and ornamental pruning, land clearing, cabling and bracing, storm damage."
SVC_LABEL = "Tree care"
SVC = [("#services", "Tree trimming &amp; removals", None), ("#services", "Hedges &amp; ornamental pruning", None), ("#services", "Land clearing", None), ("#services", "Cabling / bracing", None), ("#services", "Storm damage", None)]
NAV = [("Tree check", "#treecheck"), ("Services", "#services"), ("Blog", "why-topping-hurts-trees/")]


def biz(full=True):
    n = {"@type": "LocalBusiness", "@id": U + "#business", "name": "Sterling Tree Company", "alternateName": "Sterling Tree Co.", "url": U, "telephone": "+13158636747",
         "logo": U + "assets/img/st-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "1826 S 1100 E", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84105", "addressCountry": "US"}}
    if full:
        n.update({"description": "Tree care in Salt Lake City by ISA certified, climbing arborists: tree trimming and removals, hedges and ornamental pruning, land clearing, cabling and bracing, and storm damage.",
                  "areaServed": {"@type": "City", "name": "Salt Lake City, UT"}})
    return [n]
