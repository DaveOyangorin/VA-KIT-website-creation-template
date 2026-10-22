"""utahroofingpros.com: facts and settings (18 Oct 2026).
Name, phone, email and address copied from the client's contact page. Founded 2017 by John and Phil Panos, family-owned, based
in Cottonwood Heights (about page). Google profile: 4.9 stars from 104 reviews (5 Oct 2026, report); not shown as a number until
the client confirms. Tracking kept: Google Tag Manager GTM-N8SH5R5N and GA4 G-R2BHVYTVSQ (head snippets copied as on the live site)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "utahroofingpros.com"
U = "https://utahroofingpros.com/"
TRAIL = True
NAME = "Utah Roofing Pros"
TODAY = "2026-10-18"
HOME_OG = "new-roof-mountain-view"
THEME_COLOR = "#102944"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Public+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap"
S = {"phone": "(801) 688-3853", "tel": "+18016883853", "email": "john@utahroofingpros.com",
     "street": "2825 E Cottonwood Pkwy #500", "city": "Cottonwood Heights", "st": "UT", "zip": "84121"}
FOUNDED = "2017"
TRACK_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-N8SH5R5N');</script>
<!-- End Google Tag Manager -->
<!-- Google Analytics 4 - Utah Roofing Pros Main Website -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-R2BHVYTVSQ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-R2BHVYTVSQ');
</script>
<!-- End Google Analytics 4 -->"""

# Service areas exactly as the client groups them on /service-areas/ (Kaysville is listed there but has no page; left out).
# Coordinates are approximate city centres, used only to plot the service-area map.
REGIONS = [
    ("Salt Lake Valley", [("cottonwood-heights", "Cottonwood Heights", 40.620, -111.810), ("draper", "Draper", 40.524, -111.864), ("herriman", "Herriman", 40.514, -112.033),
                          ("holladay", "Holladay", 40.669, -111.825), ("kearns", "Kearns", 40.660, -111.996), ("magna", "Magna", 40.709, -112.101), ("midvale", "Midvale", 40.611, -111.900),
                          ("millcreek", "Millcreek", 40.687, -111.875), ("murray", "Murray", 40.667, -111.888), ("riverton", "Riverton", 40.522, -111.939),
                          ("salt-lake-city", "Salt Lake City", 40.761, -111.891), ("sandy", "Sandy", 40.572, -111.860), ("south-jordan", "South Jordan", 40.562, -111.930),
                          ("south-salt-lake", "South Salt Lake", 40.718, -111.888), ("taylorsville", "Taylorsville", 40.668, -111.939), ("west-jordan", "West Jordan", 40.610, -111.939),
                          ("west-valley-city", "West Valley City", 40.692, -112.001)]),
    ("Northern Wasatch Front", [("bountiful", "Bountiful", 40.889, -111.881), ("centerville", "Centerville", 40.918, -111.872), ("clearfield", "Clearfield", 41.111, -112.026),
                                ("clinton", "Clinton", 41.139, -112.051), ("farmington", "Farmington", 40.980, -111.887), ("layton", "Layton", 41.060, -111.971),
                                ("north-ogden", "North Ogden", 41.307, -111.960), ("north-salt-lake", "North Salt Lake", 40.849, -111.907), ("ogden", "Ogden", 41.223, -111.974),
                                ("pleasant-view", "Pleasant View", 41.318, -111.992), ("roy", "Roy", 41.162, -112.026), ("south-ogden", "South Ogden", 41.192, -111.971),
                                ("syracuse", "Syracuse", 41.089, -112.065), ("west-bountiful", "West Bountiful", 40.894, -111.902), ("west-haven", "West Haven", 41.203, -112.051),
                                ("west-point", "West Point", 41.118, -112.084), ("woods-cross", "Woods Cross", 40.872, -111.892)]),
    ("Utah County", [("alpine", "Alpine", 40.453, -111.778), ("american-fork", "American Fork", 40.377, -111.796), ("cedar-hills", "Cedar Hills", 40.414, -111.759),
                     ("eagle-mountain", "Eagle Mountain", 40.314, -112.007), ("highland", "Highland", 40.425, -111.795), ("lehi", "Lehi", 40.392, -111.851),
                     ("lindon", "Lindon", 40.343, -111.721), ("mapleton", "Mapleton", 40.130, -111.578), ("orem", "Orem", 40.297, -111.695),
                     ("pleasant-grove", "Pleasant Grove", 40.364, -111.739), ("provo", "Provo", 40.234, -111.659), ("saratoga-springs", "Saratoga Springs", 40.349, -111.904),
                     ("spanish-fork", "Spanish Fork", 40.115, -111.655), ("springville", "Springville", 40.165, -111.611), ("vineyard", "Vineyard", 40.297, -111.746)]),
    ("Wasatch Back", [("heber-city", "Heber City", 40.507, -111.413), ("park-city", "Park City", 40.646, -111.498)]),
    ("Tooele Area", [("tooele", "Tooele", 40.531, -112.298)]),
]


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/utah-roofing-pros-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "geo": {"@type": "GeoCoordinates", "latitude": 40.62, "longitude": -111.81}}
    if full:
        n.update({"description": "Utah Roofing Pros is a family-owned roofing company in Cottonwood Heights, Utah, founded in 2017 by John and Phil Panos: residential and commercial roofing, roof repair and replacement, storm damage and insurance claim help.",
                  "foundingDate": FOUNDED, "founder": [{"@type": "Person", "name": "John Panos"}, {"@type": "Person", "name": "Phil Panos"}],
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for r, cs in REGIONS for k, c, *_ in cs]})
    return [n]
