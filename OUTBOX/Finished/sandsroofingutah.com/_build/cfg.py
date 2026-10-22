"""sandsroofingutah.com: facts and settings (18 Oct 2026).
Name, phones, email, address and hours copied from the client's contact page. The site writes the office as "2331 South Redwood
Road, Salt Lake City, Utah 84119"; the Google profile writes "2331 S Redwood Rd, West Valley City, UT 84119" (flagged). Google:
4.6 stars from 149 reviews (report), not shown as a number until confirmed. Tracking kept exactly as on the live site: Google Ads
AW-16973777089 (with its conversion snippet), the Amazon pixel and Google Tag Manager GTM-MF6VFD8T."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "sandsroofingutah.com"
U = "https://sandsroofingutah.com/"
TRAIL = True
NAME = "S&S Roofing, Inc."
SHORT = "S&S Roofing"
TODAY = "2026-10-18"
HOME_OG = "drone-home-new-roof"
THEME_COLOR = "#141414"
FONTS = "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Instrument+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
S = {"phone": "+1 (801) 272-7000", "tel": "+18012727000", "phone2": "+1 (435) 658-4344", "tel2": "+14356584344", "email": "admin@sandsroofingutah.com",
     "street": "2331 South Redwood Road", "city": "Salt Lake City", "st": "Utah", "zip": "84119",
     "hours": [("Mon &ndash; Fri", "8:00am &ndash; 5:00pm"), ("Sat/Sun", "CLOSED")]}
TRACK_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16973777089"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-16973777089');
</script>

<!-- Event snippet for Lead form submissions conversion page -->
<script>
  gtag('event', 'conversion', {'send_to': 'AW-16973777089/MaWwCPLp8d0aEMGR3Z0_'});
</script>

<script>

    !function(w,d,s,t,a){if(w.amzn)return;w.amzn=a=function(){w.amzn.q.push([arguments,(new Date).getTime()])};a.q=[];a.version="0.0";s=d.createElement("script");s.src="https://c.amazon-adsystem.com/aat/amzn.js";s.id="amzn-pixel";s.async=true;t=d.getElementsByTagName("script")[0];t.parentNode.insertBefore(s,t)}(window,document);

    amzn("setRegion", "NA");

    amzn("addTag", "bd8ac336-b37a-4d3d-a6ea-dddae3980a1c");

    amzn("trackEvent", "PageView");

</script>
<!-- Google Tag Manager -->
<script data-cfasync="false" data-pagespeed-no-defer>
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MF6VFD8T');
</script>"""
# Service areas exactly as listed on /service-areas/.
AREAS = ["American Fork", "Bluffdale", "Bountiful", "Centerville", "Clinton", "Clearfield", "Cottonwood Heights", "Deer Valley", "Draper", "Emigration Canyon", "Farmington",
         "Heber City", "Herriman", "Holladay", "Kaysville", "Kearns", "Layton", "Lehi", "Lindon", "Magna", "Midvale", "Midway", "Millcreek", "Morgan", "Murray",
         "North Salt Lake", "Ogden", "Orem", "Park City", "Pleasant Grove", "Provo", "Riverdale", "Riverton", "Roy", "Salt Lake City", "Sandy", "South Jordan",
         "South Ogden", "South Salt Lake", "Stansbury Park", "Summit Park", "Syracuse", "Taylorsville", "Tooele", "West Haven", "West Jordan", "West Valley City", "Woods Cross"]
# Where people heard about them: the client's own form options, in order. Each has its own landing page.
CHANNELS = [("Hometown Values", "hometown-values/"), ("TV Segment", "tv-segment/"), ("TV Commercial", "tv-commercial/"), ("Millcreek City Lifestyle Magazine", "millcreek-city-lifestyle-magazine/"),
            ("TheHomeMag", "thehomemag/"), ("Savvy Magazine", "savvy-magazine/"), ("Park City Showcase of Home Magazine", "park-city-showcase-of-home-magazine/"),
            ("Neighbors of Utah Magazine", "neighbors-of-utah-magazine/"), ("Villager Magazine", "villager-magazine/"), ("Vehicle Scan", "vehicle-scan/"), ("Valpak", "valpak/"),
            ("Value Pages", "value-pages/"), ("Yellow Pages", "yellow-pages/"), ("Banner Advertisement", "banner-advertisement/"), ("ABC4", "abc4/"), ("RSVP", "rsvp/")]


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/ss-roofing-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": "UT", "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "S&S Roofing, Inc. is a roofing contractor in the Salt Lake Valley and Park City for residential, commercial and multi-family roofs: repairs, re-roofing, replacement, flat roofs, skylights, heat cable and snow removal.",
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in AREAS]})
    return [n]
