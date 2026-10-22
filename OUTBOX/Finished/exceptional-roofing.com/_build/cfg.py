"""exceptional-roofing.com: facts and settings (19 Oct 2026).
Exceptional Roofing, Salt Lake Valley. No address on the Google profile or the site (service-area business): no address shown.
Phones from the contact page: Estimator 801 680 6499 (also the Google number, +1801-680-6499), Production 801 809 8535.
Email ExceptionalroofingUT@gmail.com. "Best hours to reach us": Mon-Fri 06:30 am - 07:00 pm, Sat 09:00 am - 05:00 pm, Sun closed.
Financing through Acorn Finance (their own pre-qualify link). Google: 4.8 stars from 16 reviews (report), not shown until confirmed.
Tracking: none found on the live pages (WordPress 7.1.3)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "exceptional-roofing.com"
U = "https://exceptional-roofing.com/"
TRAIL = True
NAME = "Exceptional Roofing"
TODAY = "2026-10-19"
HOME_OG = "copper-roof-crew"
THEME_COLOR = "#1f2427"
FONTS = "https://fonts.googleapis.com/css2?family=Antonio:wght@500;600;700&family=Schibsted+Grotesk:wght@400;500;600;700;800&family=Azeret+Mono:wght@500;600&display=swap"
TRACK_HEAD = ""
LOGO = "er-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Tell us about the roof."
CTA_TEXT = "Free quotes on any project. Leave your info, email or call; most quotes are given the same day or week."
SIDE_TITLE = "Free quotes on any roof, any material."
PHONES = [("Estimator", "801-680-6499", "+18016806499"), ("Production", "801-809-8535", "+18018098535")]
EMAIL = "ExceptionalroofingUT@gmail.com"
HOURS = "Mon&ndash;Fri 6:30 AM&ndash;7:00 PM &middot; Sat 9 AM&ndash;5 PM"
ADDRESS = []
AREAS = ["Salt Lake City", "Sandy", "Draper", "Murray", "Holladay", "Cottonwood Heights", "South Jordan", "West Jordan", "Riverton", "Park City", "Heber", "Kamas", "Oakley", "Alpine", "Alta", "Santaquin"]
SOCIAL = []
BLURB = "Roofing is our passion: asphalt, metal, copper, wood shake and flat roofs for homes and businesses across the Salt Lake Valley and the Wasatch Back."
SVC = [("roof-repair/", "Roof repair", None), ("roof-replacement/", "Roof replacement", None), ("asphalt-roofing/", "Asphalt shingles", None), ("metal-roofing/", "Metal roofing", None),
       ("flat-roofing/", "Flat roofing", None), ("tpo-roofing/", "TPO roofing", None), ("commercial-roofing/", "Commercial roofing", None), ("storm-damage-insurance-claims/", "Storm damage &amp; insurance", None),
       ("roof-inspections/", "Roof inspections", None), ("emergency-roofing/", "Emergency roofing", None), ("preventative-maintenance/", "Preventative maintenance", None),
       ("apartment-hoa-roofing/", "Apartment &amp; HOA", None), ("retail-office-roofing/", "Retail &amp; office", None)]
NAV = [("Gallery", "gallery/"), ("Service Areas", "service-areas/"), ("Financing", "financing/"), ("About", "about/"), ("Blog", "blog/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18016806499", "email": EMAIL,
         "logo": U + "assets/img/er-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "slogan": "Roofing is our passion",
         "address": {"@type": "PostalAddress", "addressLocality": "Salt Lake City", "addressRegion": "UT", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "06:30", "closes": "19:00"},
                                       {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "Exceptional Roofing is a Salt Lake Valley roofing contractor for asphalt shingle, standing seam metal, copper, wood shake, flat and TPO roofs: repair, replacement, inspections and storm damage for homes and businesses.",
                  "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
