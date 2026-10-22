"""rwkconstruction.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (21 Oct 2026) of the home page and every linked page: /about/, /services/, /galleries/ (+ /galleries/basements/,
/galleries/theater-rooms/, /galleries/928/), /process/, /testimonials/, /contact/, /blog/, /news/, /privacy-policy/ and the six posts at the
root (/the-art-of-basement-remodeling/ etc.). Same URLs (trailing slash) and canonicals.
From the site: phone 801-820-4049, rwkconstructionco@gmail.com, office 14672 Heritage Crest Way, Bluffdale, UT 84065 (contact page, copied
exactly), office hours Monday-Friday 9am-4pm; "Since 2001", "over 20 years of experience", Utah-born; serves Salt Lake, Utah, Davis and Tooele
Counties (about page); services: basement finishing, home renovations, home theaters, custom homes; process: Consultation, Design,
Communication (online Homeowner Portal), Construction, Finishing Up (warranty process), Post-Completion; motto "Build the Right Way";
project rules from the contact page: basements must be at least 500 sq ft, walkouts only together with finishing the whole basement,
no houses older than 1975. Testimonials: the 22 named reviews on /testimonials/ (some also on the home page), shown as written.
Left out until confirmed: "the best basement finishes ... in Utah", "Five-Star Reviews" as a rating, "Award wining contractor" (no award
named), "Most Skilled Project Managers". The 2020 restaurant gift-card promotion post is kept at its URL but marked closed (it says so).
Photos: their own project photos (the Adele Lamb Photography architecture shoots of the Alta condo and Saratoga Springs home, the
S Amanda Lane custom home, a basement family room and a theater room). Most gallery images on the live site return 404 (the files are
gone), so the galleries here are rebuilt from the photos that still load."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "rwkconstruction.com"
U = "https://rwkconstruction.com/"
TRAIL = True
NAME = "RWK Construction Co."
TODAY = "2026-10-21"
HOME_OG = "rw-family"
THEME_COLOR = "#16161a"
FONTS = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "rw-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Let&rsquo;s build it <em>the right way.</em>"
CTA_TEXT = "Call 801-820-4049 or send the form. Our estimator meets you at your home, talks through your ideas, and puts together a customized plan and a free estimate."
SIDE_TITLE = "Free consultation and estimate, at your home."
PHONES = [("Call", "801-820-4049", "+18018204049")]
EMAIL = "rwkconstructionco@gmail.com"
HOURS = "Office: Mon&ndash;Fri 9 am&ndash;4 pm"
ADDRESS = [("Office", "14672 Heritage Crest Way<br>Bluffdale, UT 84065")]
AREAS = ["Salt Lake County", "Utah County", "Davis County", "Tooele County"]
SOCIAL = []
BLURB = "Utah-born and building since 2001: basement finishing, home renovations, home theaters and custom homes. Build the Right Way."
SVC_LABEL = "Services"
SVC = [("services/", "Basement finishing", None), ("services/#renovations", "Home renovations", None), ("services/#theaters", "Home theaters", None),
       ("galleries/928/", "Custom homes", None), ("galleries/", "Photo galleries", None), ("process/", "Our process", None)]
NAV = [("Process", "process/"), ("Galleries", "galleries/"), ("Reviews", "testimonials/"), ("About", "about/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "GeneralContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18018204049", "email": EMAIL,
         "logo": U + "assets/img/rw-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "slogan": "Build the Right Way",
         "address": {"@type": "PostalAddress", "streetAddress": "14672 Heritage Crest Way", "addressLocality": "Bluffdale", "addressRegion": "UT", "postalCode": "84065", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "16:00"}]}
    if full:
        n.update({"description": "RWK Construction Co. finishes basements, remodels homes and builds home theaters and custom homes across Salt Lake, Utah, Davis and Tooele Counties. Building in Utah since 2001.",
                  "foundingDate": "2001",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + ", UT"} for c in AREAS]})
    return [n]
