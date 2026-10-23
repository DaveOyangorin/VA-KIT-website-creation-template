"""whitepineplumbingut.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the 4 sitemap URLs plus a browser render for images (Web.com builder; URLs end in a slash, canonicals
without). Same URLs and canonicals; the empty "Blog Page" (/blank/) becomes the blog index; one new post.
From the site: White Pine Plumbing; "Plumbing services you can rely on! From drain cleaning, to water heater installs, White Pine Plumbing
delivers expert care for every client"; services: drain cleaning, general plumbing, water softeners, water heaters, plumbing repairs, leak
locating & repair; "Why choose us" and "Our promise" copy; five-step process (contact, assessment, planning, implementation, follow-up);
tagline "Rooted in Quality, Flowing in Trust"; team: Jake Winward (owner, expert plumber, over a decade of hands-on experience), Rett Speidel
(co-owner, expert plumber), Brady Winward (plumber), Sebastian Rivera (plumber), Brooke Stratton (office administrator, customer care);
"Plumber education" section showing Mountainland Technical College and Salt Lake Tech / SLCC logos; Instagram and YouTube.
NAP: Google listing 489 South Jordan Pkwy Ste 239, South Jordan, UT 84095, +1435-357-5862 (used, copied exactly). The phone is a 435 area
code; copied exactly (report note). The site shows no address.
Left out until confirmed: the 5-star / 160-review rating. Education logos: mentioned in text, flagged.
Photos: their team photo, five headshots and two job photos (clawfoot tub install, drain repair). The forest and texture images are stock and
not used; the banner is a credited Wikimedia Commons photo of a sunset over South Jordan."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "whitepineplumbingut.com"
U = "https://whitepineplumbingut.com/"
TRAIL = True
NAME = "White Pine Plumbing"
TODAY = "2026-10-22"
HOME_OG = "wp-team"
THEME_COLOR = "#16352a"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "wp-logo"
CTA_PATH = "getaquote/"
CTA_LABEL = "Get a quote"
CTA_TITLE = "Rooted in quality, <em>flowing in trust.</em>"
CTA_TEXT = "Call or text 435-357-5862, or send the quote form. Fast communication, honest pricing and expert solutions in South Jordan and the southwest valley."
SIDE_TITLE = "Fast communication. Honest pricing."
PHONES = [("Call or text", "435-357-5862", "+14353575862")]
EMAIL = ""
HOURS = ""
ADDRESS = [("South Jordan", "489 South Jordan Pkwy Ste 239<br>South Jordan, UT 84095")]
AREAS = ["South Jordan", "the Salt Lake Valley"]
SOCIAL = [("Instagram", "https://www.instagram.com/white_pine_plumbing/"), ("YouTube", "https://youtube.com/@whitepineplumbing")]
BLURB = "White Pine Plumbing: drain cleaning, general plumbing, water softeners, water heaters, repairs and leak locating in South Jordan. Rooted in Quality, Flowing in Trust."
SVC_LABEL = "Services"
SVC = [("#services", "Drain cleaning", None), ("#services", "Water heaters", None), ("#services", "Water softeners", None), ("#services", "Leak locating &amp; repair", None), ("#services", "Plumbing repairs", None)]
NAV = [("Our process", "#process"), ("Team", "team/"), ("Blog", "blank/"), ("Get a quote", "getaquote/")]


def biz(full=True):
    n = {"@type": "Plumber", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+14353575862",
         "logo": U + "assets/img/wp-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "489 South Jordan Pkwy Ste 239", "addressLocality": "South Jordan", "addressRegion": "UT", "postalCode": "84095", "addressCountry": "US"}}
    if full:
        n.update({"description": "South Jordan plumber: drain cleaning, general plumbing, water softeners, water heaters, plumbing repairs and leak locating & repair.",
                  "slogan": "Rooted in Quality, Flowing in Trust", "sameAs": [u for l, u in SOCIAL],
                  "founder": [{"@type": "Person", "name": "Jake Winward"}, {"@type": "Person", "name": "Rett Speidel"}],
                  "areaServed": {"@type": "City", "name": "South Jordan, UT"}})
    return [n]
