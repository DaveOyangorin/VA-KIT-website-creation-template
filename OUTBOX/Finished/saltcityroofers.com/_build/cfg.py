"""saltcityroofers.com: facts and settings (18 Oct 2026).
Phone and email copied from the client's own site (header and contact page). No Google profile was found (report), so no address,
hours or rating are shown. People and history from the about page: Brock A. Horton (CEO and project manager), Asenath Horton
(owner); "a Salt City Builders, Inc. Company"; "in business since 2007". Travel area from the Q&A page: about 45 minutes, the
Wasatch Front from Provo and Lehi to Park City and Ogden. GA4 tag G-9CE799NZYH kept."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "saltcityroofers.com"
U = "https://www.saltcityroofers.com/"
TRAIL = True
NAME = "Salt City Roofers"
LEGAL = "Salt City Builders, Inc."
TODAY = "2026-10-18"
HOME_OG = "avenues-finished-b"
THEME_COLOR = "#15212c"
FONTS = "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
S = {"phone": "801-835-1868", "tel": "+18018351868", "email": "SaltCityRoofers@gmail.com", "fb": "https://www.facebook.com/saltcityroofers/"}
TRACK_HEAD = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-9CE799NZYH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-9CE799NZYH');
</script>"""
AREAS = ["Salt Lake City", "the Avenues", "Federal Heights", "Cottonwood Heights", "Draper", "North Salt Lake", "Lehi", "Provo", "Park City", "Ogden"]


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "parentOrganization": {"@type": "Organization", "name": LEGAL},
         "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/salt-city-roofers-logo.png", "sameAs": [S["fb"]], "image": U + "assets/img/" + HOME_OG + ".webp"}
    if full:
        n.update({"description": "Salt City Roofers is a roofing and exterior remodeling contractor in Salt Lake City: asphalt shingle, synthetic slate and metal roofs, tear-offs, roof conversions, gutters and chimney caps.",
                  "foundingDate": "2007", "employee": [{"@type": "Person", "name": "Brock A. Horton", "jobTitle": "CEO"}, {"@type": "Person", "name": "Asenath Horton", "jobTitle": "Owner"}],
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in ["Salt Lake City", "Cottonwood Heights", "Draper", "North Salt Lake", "Lehi", "Provo", "Park City", "Ogden"]]})
    return [n]
