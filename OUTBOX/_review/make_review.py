"""Builds the review landing page that opens first in each client's preview artifact.

  python -I make_review.py <pylib> <screenshots_dir> [client_key]

For each client it writes <client>/preview/index.html (the review page) and <client>/preview/review/*.webp
(before/after screenshots). The new website itself lives at <client>/preview/home/index.html.
"""
import sys, os, re, html, json
sys.path.insert(0, sys.argv[1])
from PIL import Image

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # OUTBOX
SHOTS = sys.argv[2]

CLIENTS = [
    {
        "key": "New/Weak-Site-Businesses/husky-property-maintenance", "name": "Husky Property Maintenance", "city": "Midvale, UT", "title": "Husky Review",
        "report": "2026-10-21_husky-property-maintenance_report.html", "old": "old_hp", "new": "new_hp",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Husky Property Maintenance, 101 7200 S, Midvale, UT 84047, 801-742-5282, copied exactly", "Fixed"),
            ("Home target \"handyman midvale\"", "Title, H1 and first sentence use it; tap-to-call everywhere; HomeAndConstructionBusiness schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: Home safety checklist, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1022-word post: Smoke and carbon monoxide alarms: where they go and how to keep them working", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.6 / 196 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "smoke-and-co-alarm-basics/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/superior-locksmith", "name": "Superior Locksmith", "city": "West Jordan, UT", "title": "Superior Review",
        "report": "2026-10-21_superior-locksmith_report.html", "old": "old_sl", "new": "new_sl",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Superior Locksmith, 7679 S Redwood Rd, West Jordan, UT 84084, 801-565-0226, copied exactly", "Fixed"),
            ("Home target \"locksmith west jordan\"", "Title, H1 and first sentence use it; tap-to-call everywhere; Locksmith schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: Rekey, repair or replace?, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1005-word post: Lock grades explained: what BHMA ratings actually test", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.8 / 247 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "lock-grades-explained/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/eagle-locksmith-inc", "name": "Eagle Locksmith inc", "city": "Salt Lake City, UT", "title": "Eagle Review",
        "report": "2026-10-21_eagle-locksmith-inc_report.html", "old": "old_el", "new": "new_el",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Eagle Locksmith inc, no address on the listing (service-area business), 385-557-7669, copied exactly", "Fixed"),
            ("Home target \"locksmith salt lake city\"", "Title, H1 and first sentence use it; tap-to-call everywhere; Locksmith schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: The locksmith call checklist, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1053-word post: How to hire a locksmith without getting scammed", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Should an address be shown?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.2 / 756 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "how-to-hire-a-locksmith/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/gross-family-plumbing-llc", "name": "Gross Family Plumbing LLC", "city": "Salt Lake City, UT", "title": "Gross Family Review",
        "report": "2026-10-21_gross-family-plumbing-llc_report.html", "old": "old_gf", "new": "new_gf",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Gross Family Plumbing LLC, 1750 Research Way #3600, Salt Lake City, UT 84119, 385-331-1988, copied exactly", "Fixed"),
            ("Home target \"plumber salt lake city\"", "Title, H1 and first sentence use it; tap-to-call everywhere; Plumber schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: Toilet water calculator, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1045-word post: When to replace a toilet: what WaterSense says about old, thirsty models", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.8 / 163 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "when-to-replace-a-toilet/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/sean-s-plumbing", "name": "Sean's Plumbing", "city": "South Jordan, UT", "title": "Sean'S Review",
        "report": "2026-10-21_sean-s-plumbing_report.html", "old": "old_sn", "new": "new_sn",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Sean's Plumbing, 10330 S Redwood Rd #5230, South Jordan, UT 84095, 435-850-6314, copied exactly", "Fixed"),
            ("Home target \"plumber south jordan\"", "Title, H1 and first sentence use it; tap-to-call everywhere; Plumber schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: Water hardness converter, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1033-word post: Hard water explained: what the numbers mean for your home", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.9 / 254 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "hard-water-explained/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/stanley-sons-plumbing", "name": "Stanley & Sons Plumbing", "city": "Salt Lake City, UT", "title": "Stanley & Sons Review",
        "report": "2026-10-21_stanley-sons-plumbing_report.html", "old": "old_ss", "new": "new_ss",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Stanley & Sons Plumbing, 2346 E Fort Union Blvd #7100, Salt Lake City, UT 84121, 385-333-7488, copied exactly", "Fixed"),
            ("Home target \"plumber salt lake city\"", "Title, H1 and first sentence use it; tap-to-call everywhere; Plumber schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: Water heater thermometer, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1072-word post: What temperature should your water heater be? Why CPSC says 120°F", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.8 / 265 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "water-heater-temperature-120-degrees/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/stott-plumbing-excavating", "name": "Stott Plumbing & Excavating", "city": "Salt Lake City, UT", "title": "Stott Review",
        "report": "2026-10-21_stott-plumbing-excavating_report.html", "old": "old_sp", "new": "new_sp",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Stott Plumbing & Excavating, 165 Gregson Ave S, Salt Lake City, UT 84115, 801-467-2432, copied exactly", "Fixed"),
            ("Home target \"plumber salt lake city\"", "Title, H1 and first sentence use it; tap-to-call everywhere; Plumber schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: The 811 color code, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1053-word post: Blue Stakes 811 in Utah: what to know before you dig", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.8 / 1,172 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "blue-stakes-811-utah-before-you-dig/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/conrad-s-roofing-construction", "name": "Conrad's Roofing & Construction", "city": "Lehi, UT", "title": "Conrad'S Review",
        "report": "2026-10-21_conrad-s-roofing-construction_report.html", "old": "old_cr", "new": "new_cr",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: Conrad's Roofing & Construction, 1650 Digital Dr, Lehi, UT 84043, 435-375-3396, copied exactly", "Fixed"),
            ("Home target \"roofing company lehi\"", "Title, H1 and first sentence use it; tap-to-call everywhere; RoofingContractor schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: Snow load calculator, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1000-word post: How much snow can a roof hold? Weights, warning signs and safe removal", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.8 / 406 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "how-much-snow-can-a-roof-hold/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/rooftek", "name": "RoofTek", "city": "Millcreek, UT", "title": "Rooftek Review",
        "report": "2026-10-21_rooftek_report.html", "old": "old_rt", "new": "new_rt",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("1", "working signature tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("No website at all", "A first website built only from the Google listing: RoofTek, 4080 S W Temple St, Millcreek, UT 84107, 801-471-2054, copied exactly", "Fixed"),
            ("Home target \"roofing company millcreek\"", "Title, H1 and first sentence use it; tap-to-call everywhere; RoofingContractor schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: Roof pitch calculator, a working tool built on published sources, plus sourced tips", "Fixed"),
            ("No domain yet", "Canonicals, sitemap and robots use a reserved .example placeholder; set the real domain before launch", "Needs client"),
            ("No services, hours, photos, licenses or story", "Not invented. The pages stay lean until the client supplies them; banner is a credited open-license photo", "Needs client"),
            ("No blog", "A new 1042-word post: What is a FORTIFIED roof? A homeowner’s guide to the IBHS standard", "Fixed"),
        ],
        "questions": ["Which domain should the site use?", "Which services do you offer, and in which areas?", "What are your hours? Do you have a shop customers can visit?", "Licensed and insured? License number?", "Can you send photos of your team and work?", "Can we show 4.6 / 1,403 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "what-is-a-fortified-roof/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/jacksonplumbinghvac.com", "name": "Jackson Family Plumbing & HVAC", "city": "West Jordan, UT", "title": "Jackson Plumbing Review",
        "report": "2026-10-21_jacksonplumbinghvac.com_report.html", "old": "old_jk", "new": "new_jk",
        "stats": [("3", "pages (home + contact + 1 post)"), ("0", "invented facts"), ("630", "home page words (was 68)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Live page is a \"Colorado 24/7 Plumbing Call\" template: no phone, broken images, Colorado text", "Rebuilt from the Google listing only: name, West Jordan address and phone, copied exactly. Archive captures back to 2024 are the same template, so there was nothing else to recover", "Fixed"),
            ("Home target \"plumber west jordan\"; no tap-to-call; no page names West Jordan", "Title, H1 and first sentence name a plumber in West Jordan; tap-to-call everywhere; Plumber schema", "Fixed"),
            ("Nothing true to say beyond the listing", "Signature: EPA WaterSense two-hour water-meter leak test, as a working calculator; a frozen-pipe checklist from IBHS, USU Extension and the NWS", "Fixed"),
            ("Claims on the live page", "\"#1 Ranked\", \"Licensed, Bonded, Insured\" and the Milliken, CO service area left out until confirmed", "Needs client"),
            ("No services, hours, photos or story", "Not invented. Home is lean (630 words) until the client supplies services, hours and photos", "Needs client"),
            ("No blog", "A new 1,175-word post on keeping pipes from freezing (IBHS, USU Extension, NWS)", "Fixed"),
        ],
        "questions": ["Which services do you offer (drain cleaning, water heaters, sewer lines, HVAC repair...)?", "What are your hours, and do you take emergency calls?", "Do you still serve Milliken, Colorado as well as West Jordan?", "Are you licensed, bonded and insured? License number?", "Can you send photos of your team, trucks and work?", "Can we show 4.9 stars from 170 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Contact", "contact/index.html"), ("New blog post", "how-to-keep-pipes-from-freezing/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/dsihvac.com", "name": "Proformance Heating and Air", "city": "Draper, UT", "title": "Proformance HVAC Review",
        "report": "2026-10-21_dsihvac.com_report.html", "old": "old_pf", "new": "new_pf",
        "stats": [("7", "pages, same Wix URLs (+1 post)"), ("3", "services the dial points to"), ("790", "home page words (was 0)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Domain and old site say \"DSI HVAC\"; Google says Proformance", "Same phone number (385-226-7667) on both, which points to a rebrand. Google name used; DSI logo not used. Confirm before anything goes live", "Needs Angelo"),
            ("Site down; home page had 0 words, no H1, no meta, no tap-to-call", "Rebuilt from the Internet Archive (Nov 2025 and Jan 2026 captures): one H1, title, meta, tap-to-call, HVACBusiness schema with hours", "Fixed"),
            ("Home target \"hvac company draper\"; no page named Draper", "Title, H1 and first sentence name an HVAC company in Draper; service area listed", "Fixed"),
            ("Template Wix look", "\"Swing\": slate with furnace orange and coil blue; credited Draper banner; signature \"Maintain, repair or replace?\" dial built on their three services and ENERGY STAR guidance", "Fixed"),
            ("Wix stock photos", "Not used; their own install photos and the 2018 Trane award are", "Fixed"),
            ("Ten target services with no pages", "Only what the old site said they do is built (maintenance, repair, new installs, brands); ask which service pages to add", "Needs client"),
            ("No blog", "A new 1,269-word post on furnace filters and MERV ratings (EPA and ENERGY STAR sources)", "Fixed"),
        ],
        "questions": ["Is Proformance Heating and Air the same business as DSI HVAC (dsihvac.com)?", "Should the email stay david@dsihvac.com?", "Do you have a Proformance logo?", "Which services get their own page (AC repair, furnace repair, duct cleaning, heat pumps, mini-splits)?", "Can we show 5 stars from 191 Google reviews?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("About", "about-us/index.html"), ("Contact", "contact-us/index.html"), ("New blog post", "how-often-to-change-your-furnace-filter/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/marble-builders.com", "name": "Marble Builders", "city": "Riverton, UT", "title": "Marble Builders Review",
        "report": "2026-10-21_marble-builders.com_report.html", "old": "old_mb", "new": "new_mb",
        "stats": [("60", "pages, same WordPress URLs (+1 post)"), ("6", "steps in the rebuild timeline"), ("855", "home page words"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Live site down (account suspended, then a Cloudflare challenge)", "Rebuilt from the Internet Archive's most recent real captures of each page (March to September 2025)", "Fixed"),
            ("Home target \"general contractor riverton\"; home never names Riverton", "Title, H1 and first sentence name a general contractor in Riverton; tap-to-call; GeneralContractor schema with hours", "Fixed"),
            ("Template look", "\"Veined\": honed charcoal, CSS-drawn marble veining and brass; credited Lone Peak banner; signature two-lane \"After the damage\" timeline built from their own restoration posts", "Fixed"),
            ("Three different phone numbers", "Google's 801-828-5540 used everywhere; 385-644-6304 (home header) and 888-973-3212 (home meta) left out", "Needs client"),
            ("Service pages carry a copied \"Marble Homes\" FAQ", "Left out; replaced with real FAQs from their own pages and posts", "Fixed"),
            ("Project photos not archived; WordPress demo pages live", "No photos invented; demo and project template pages kept at their URLs, noindex, pointing home", "Needs client"),
            ("10 pages unrecoverable (Las Vegas page, mid-2025 posts)", "Kept at the same URLs as noindex placeholders until the text is supplied", "Needs client"),
            ("Blog", "A new 1,249-word post on lead paint and asbestos before remodeling an older home (five EPA sources)", "Fixed"),
        ],
        "questions": ["Which number should the site use: 801-828-5540, 385-644-6304 or 888-973-3212?", "Can you send project photos (Bountiful kitchen, Farmington bathroom, rebuilds)?", "Can you resend the text of the Las Vegas page and the mid-2025 blog posts?", "Can we show 4.6 stars from 198 Google reviews?", "Should the demo pages (salient-architect, sample-page, example project) be deleted?"],
        "pages": [("Home", "home/index.html"), ("Property repairs", "property-repairs-service-page/index.html"), ("Salt Lake City", "salt-lake-city-utah-home-remodeling/index.html"), ("Blog", "blog/index.html"), ("New blog post", "2026/10/lead-paint-asbestos-before-remodeling-older-home/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/prestigetreeandlandscape.com", "name": "Prestige Tree And Landscape", "city": "Murray, UT", "title": "Prestige Tree Review",
        "report": "2026-10-21_prestigetreeandlandscape.com_report.html", "old": "old_pt", "new": "new_pt",
        "stats": [("35", "pages, same .php URLs (+1 post)"), ("48", "growth rings, 1978 to 2026"), ("621", "home page words (was 13)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home page loads blank; no title; mobile speed 19/100", "A real, fast home page: plain HTML with one H1, title and meta; only a few compressed images", "Fixed"),
            ("Home target \"tree service murray\"; no page names Murray; no tap-to-call; no schema", "Title, H1 and first sentence name tree service in Murray; tap-to-call throughout; LocalBusiness schema with hours", "Fixed"),
            (".php URLs", "Same URLs kept: the live build writes real .php files (plain HTML), so no redirects are needed", "Fixed"),
            ("Template look", "\"Growth rings\": credited fall canyon banner; signature cut trunk with one ring per year since 1978, gold rings telling their milestones", "Fixed"),
            ("Stock photos", "Slider and service photos are stock and not used; the arborist's own climbing and crane photos are", "Fixed"),
            ("Claims and conflicts", "1996 vs 1997 certification; About page says Sandy; WSJ Businessman of the Year and Disney claims left out until confirmed", "Needs client"),
            ("Backup files live (header.php.bak etc.)", "Kept at their URLs, noindex, pointing home; they should be deleted from the server", "Needs client"),
            ("No blog", "A new 1251-word post on mulching around trees (ISA and USDA Forest Service sources)", "Fixed"),
        ],
        "questions": ["Were you certified in 1996 or 1997?", "Can we show the Wall Street Journal and Disney credentials? We left them out pending confirmation.", "Can we show 4.4 stars from 350 Google reviews?", "Is the office at 4780 S Commerce Dr, Murray open to visitors?"],
        "pages": [("Home", "home/index.html"), ("Tree pruning", "tree-pruning.php/index.html"), ("Credentials", "credentials-awards.php/index.html"), ("Contact", "contact-us.php/index.html"), ("New blog post", "how-to-mulch-around-trees.php/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/pineapplepropertygroup.com", "name": "Pineapple Property Group", "city": "Salt Lake City, UT", "title": "Pineapple Property Group Review",
        "report": "2026-10-21_pineapplepropertygroup.com_report.html", "old": "old_pp", "new": "new_pp",
        "stats": [("10", "pages, same URLs (+1 post)"), ("11", "inputs on the valuation tool"), ("842", "home page words"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Live site blocks our network", "Built from the Internet Archive's 2025-2026 captures of every page; no live screenshot of the current site", "Needs Angelo"),
            ("Home target \"property management salt lake city\"; 5 H1s; no page names Salt Lake City", "One H1 naming property management in Salt Lake City; title, meta and first sentence too", "Fixed"),
            ("No business schema; no sitemap; 10 of 10 images without alt text", "RealEstateAgent schema with hours and 40 service cities; sitemap and robots; every image has alt text", "Fixed"),
            ("Valuation tool shows lorem ipsum", "Rebuilt as a working owner statement: NOI, cap rate, cash flow, cash on cash, a 5% vs 10% fee comparison and the value of 90 fee-free days", "Fixed"),
            ("Template leftovers", "A hidden footer block with a Woods Cross address and another phone number (designer template) is ignored; flagged", "Needs client"),
            ("Performance claims", "99.2% occupancy, 18-hr repairs, 10% cash on cash, 32% NOI and the five property returns kept, labelled as figures Pineapple reports; confirm before going live", "Needs client"),
            ("Stock photos", "Not used; their team headshots plus credited Wikimedia Commons photos of Salt Lake City apartment buildings", "Fixed"),
            ("No blog", "A new 1145-word post on Fair Housing Act basics for landlords (statute and U.S. Justice Department sources)", "Fixed"),
        ],
        "questions": ["Are the KPI averages and the five property returns current, and can we publish them?", "Can we show 4.2 stars from 720 Google reviews?", "Do you have headshots for Affi Almas, Siddhi Rajan, Bernard Thomsen and Justin Curtis?", "The site's code has a hidden Woods Cross address and 801.294.6400: is that anything of yours?"],
        "pages": [("Home", "home/index.html"), ("Property management", "Property-Management/index.html"), ("Valuation tool", "Investment-Valuation-Tool/index.html"), ("Team", "The-Team/index.html"), ("New blog post", "fair-housing-basics-for-landlords/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/whitepineplumbingut.com", "name": "White Pine Plumbing", "city": "South Jordan, UT", "title": "White Pine Plumbing Review",
        "report": "2026-10-21_whitepineplumbingut.com_report.html", "old": "old_wp", "new": "new_wp",
        "stats": [("4", "pages, same URLs (+1 post)"), ("5", "valves on the process pipeline"), ("698", "home page words (was 397)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"plumber south jordan\"; 0 H1; no page names South Jordan", "One H1 naming a plumber in South Jordan; title, meta and first sentence too", "Fixed"),
            ("No tap-to-call; no business schema; 15 of 15 images without alt text", "Tap-to-call throughout; Plumber schema with NAP, founders and slogan; every image has alt text", "Fixed"),
            ("Phone is a 435 number", "Copied exactly as on Google; ask whether there is a local 801/385 number", "Needs client"),
            ("Template look", "\"Rooted & flowing\": credited sunset over South Jordan, their team front and center; signature pipeline where each valve opens one of their five process steps", "Fixed"),
            ("Stock images on the live site", "Not used; only their team photo, headshots and job photos (plus a credited Commons banner)", "Fixed"),
            ("Empty \"Blog Page\" at /blank/", "Same URL turned into the blog index with a new 1121-word post on hard water (USGS, EPA sources)", "Fixed"),
            ("10 of 10 report services have no page (drain cleaning 1,900)", "Their six services on the home page; separate pages need the client's input", "Needs client"),
        ],
        "questions": ["Do you have a local phone number, or keep 435-357-5862?", "Can we show 5 stars from 160 Google reviews?", "What should the 'plumber education' section say about Mountainland Tech and Salt Lake Tech / SLCC?", "Do you have more job photos for service pages?"],
        "pages": [("Home", "home/index.html"), ("Team", "team/index.html"), ("Get a quote", "getaquote/index.html"), ("New blog post", "hard-water-and-your-plumbing/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/hvaccowboy.com", "name": "Cowboy Heating & Air", "city": "Lehi, UT", "title": "Cowboy Heating & Air Review",
        "report": "2026-10-21_hvaccowboy.com_report.html", "old": "old_cb", "new": "new_cb",
        "stats": [("1", "page, same URL (+1 post)"), ("2", "modes: homeowner and business"), ("630", "words search engines can read (was 10)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home page is a JavaScript app: search engines see 10 words, 0 H1, no tap-to-call", "Plain HTML page with all their content readable, one H1 naming an HVAC company in Lehi, tap-to-call throughout, sitemap and robots", "Fixed"),
            ("Live schema says 3 reviews; Google shows 162", "Schema rebuilt without a rating; the 5.0 rating is left out until confirmed", "Needs client"),
            ("Award and dealer claims", "Best of BusinessRate 2025 (plaque photo on their site), Daikin Authorized and Bryant Dealer kept; confirm before going live", "Needs client"),
            ("Template look", "\"Home or business\": their branded car under a Utah Valley sunset; signature rope switch that re-saddles the page (headline, services, job photos and the quote form) for homeowners or businesses", "Fixed"),
            ("Photos", "All their own: residential AC and furnace work, rooftop units, control board, kitchen exhaust fan, award plaque", "Fixed"),
            ("10 of 10 report services have no page (AC repair 1,900, furnace repair 1,300)", "Four services on the home page; separate pages need the client's input", "Needs client"),
            ("No blog", "A new 1065-word post on carbon monoxide and your furnace (EPA and NFPA sources)", "Fixed"),
        ],
        "questions": ["Can we show the 5.0 rating from 162 Google reviews (and fix the live schema that says 3)?", "Are you a Daikin authorized and Bryant dealer, and can we show the BusinessRate 2025 award?", "Is 1227 W Bridlewood Lp, Lehi OK to show on the site?", "Which services should get their own pages first: AC repair or furnace repair?"],
        "pages": [("Home", "home/index.html"), ("New blog post", "carbon-monoxide-and-your-furnace/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/anyandallservices.com", "name": "Any & All Services", "city": "Salt Lake City, UT", "title": "Any & All Services Review",
        "report": "2026-10-21_anyandallservices.com_report.html", "old": "old_aa", "new": "new_aa",
        "stats": [("6", "pages, same URLs (+1 post)"), ("8", "breakers on the project panel"), ("508", "home page words (was 157)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Business model changed", "The live site now says it connects homeowners with trusted local electricians (\"we handle the shopping around\"). The draft says exactly that. Targeting \"electrician salt lake city\" for a referral service needs Angelo's call.", "Needs Angelo"),
            ("Home target \"electrician salt lake city\"; 2 H1s; no page names Salt Lake City; no tap-to-call", "One H1 naming an electrician in Salt Lake City, honestly framed; tap-to-call throughout; LocalBusiness schema without an address (service-area business)", "Fixed"),
            ("Years conflict", "Page says over 14 years; meta says over 13. Draft uses the page's 14; flagged", "Needs client"),
            ("No photos of their own", "Banner is a credited Wikimedia Commons photo of Salt Lake City at night; no stock image is presented as their work", "Fixed"),
            ("Template look", "\"Breaker panel\": black and red from their logo; signature breaker panel that turns the project parts you switch on into a description and drops it into their estimate form", "Fixed"),
            ("Legal pages are unedited Wix templates", "Kept at their URLs, noindex, with a notice pointing to their email; real policies needed from the client", "Needs client"),
            ("No blog", "A new 1145-word post on signs you need an electrician (NFPA and UL sources)", "Fixed"),
        ],
        "questions": ["Do you still do electrical work yourselves, or only connect homeowners with electricians?", "Over 13 years or over 14 years?", "Which project types and HVAC work should we list as services?", "Do you have real privacy, terms and refund policies to replace the Wix templates?"],
        "pages": [("Home", "home/index.html"), ("New blog post", "signs-you-need-an-electrician/index.html"), ("Book online", "book-online/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/sterlingtreeco.godaddysites.com", "name": "Sterling Tree Co.", "city": "Salt Lake City, UT", "title": "Sterling Tree Co. Review",
        "report": "2026-10-21_sterlingtreeco.godaddysites.com_report.html", "old": "old_st", "new": "new_st",
        "stats": [("1", "page, same URL (+1 post)"), ("11", "ISA checklist questions on the tree"), ("743", "home page words (was 137)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("One-page free GoDaddy site, no own domain", "Built as a full home page plus a blog post; ready to move to a real domain (canonicals set to the current address until then)", "Needs client"),
            ("Home target \"tree service salt lake city\"; no page names Salt Lake City; no meta description", "Title, H1, meta and first sentence name tree service in Salt Lake City", "Fixed"),
            ("No business schema; 3 of 3 images without alt text", "LocalBusiness schema with NAP; every image has descriptive alt text", "Fixed"),
            ("Phone is a 315 (New York) number", "Copied exactly as on Google and the site; ask whether there is a local number", "Needs client"),
            ("Template look", "\"Canopy\": full-width photo of their arborist in a London plane above Salt Lake City; signature tree check that draws ISA's tree risk checklist onto a tree and links ISA's management options to their services", "Fixed"),
            ("9 of 9 report services have no page (tree removal 480, pruning 720)", "All five of their services set out on the home page; separate pages need the client's input and photos", "Needs client"),
            ("No blog", "A new 1218-word post on why topping hurts trees (ISA sources)", "Fixed"),
        ],
        "questions": ["Do you have a local (801/385) phone number, or should we keep 315-863-6747?", "Would you like a real domain (e.g. sterlingtreeco.com)? The site is ready to move.", "Can we show 5 stars from 185 Google reviews?", "Can you send more job photos, and the names of your ISA certified arborists?"],
        "pages": [("Home", "home/index.html"), ("New blog post", "why-topping-hurts-trees/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/actionyardcare.com", "name": "Action Lawn & Yardcare", "city": "Murray, UT", "title": "Action Lawn & Yard Review",
        "report": "2026-10-21_actionyardcare.com_report.html", "old": "old_ay", "new": "new_ay",
        "stats": [("4", "pages, same URLs (+1 post)"), ("21", "services on the lineup card"), ("580", "home page words (was 83)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"landscaping murray\"; no page names Murray; 83-word home page; no meta description", "Title, H1, meta and first sentence name landscaping in Murray; home page built from their service list, plus a sourced USU yard calendar; metas on every page", "Fixed"),
            ("No tap-to-call; no business schema; no address on the site", "Tap-to-call throughout; LocalBusiness schema; Google NAP (6501 S Cottonwood St, Murray) in the footer and contact page; flagged", "Needs client"),
            ("Name differs", "Google says \"Action Lawn and Yard\"; the site says \"Action Lawn & Yardcare\" (logo: \"Action Lawn & Yard Care\"). Site name kept for display, Google name in schema", "Needs client"),
            ("Template look", "\"Lineup card\": varsity type from their logo, safety lime from their crew shirts, full-width crew photo; signature lineup card that turns their service list into a ready-to-send quote request", "Fixed"),
            ("Claims", "\"One of the highest rated landscaping companies in Utah\" and the 4.7 / 187 rating left out until confirmed", "Needs client"),
            ("10 of 10 report services have no page (sprinkler repair 1,000, lawn care 880)", "All services listed on one services page for now; separate pages are the next step once the client confirms", "Needs client"),
            ("No blog", "A new 1072-word post on how high to mow a Utah lawn (USU Extension sources)", "Fixed"),
        ],
        "questions": ["Which business name should the site use: Action Lawn and Yard (Google) or Action Lawn & Yardcare?", "Is 6501 S Cottonwood St, Murray OK to show on the site?", "Can we show 4.7 stars from 187 Google reviews?", "Do you have more job photos (finished landscapes, sprinklers, snow) for service pages?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("About", "about/index.html"), ("Contact", "contact-us/index.html"), ("New blog post", "how-high-to-mow-a-utah-lawn/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/danielswildlife.com", "name": "Daniel's Wildlife & Pest Control", "city": "Cottonwood Heights, UT", "title": "Daniel's Wildlife Review",
        "report": "2026-10-21_danielswildlife.com_report.html", "old": "old_dw", "new": "new_dw",
        "stats": [("18", "pages, same URLs (+1 post)"), ("14", "signs in the clue matcher"), ("862", "home page words (was 118)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"pest control cottonwood heights\"; 0 H1; no page names Cottonwood Heights; 118-word home page", "One H1 naming pest control and wildlife removal in Cottonwood Heights; title, meta and first sentence too; full home page from his own copy", "Fixed"),
            ("Location shown only as \"Northern Utah\"", "Google NAP used (6870 S Village Green Rd, Cottonwood Heights) in the footer, contact page and schema; flagged", "Needs client"),
            ("Template look", "\"Field notes\": full-width photo of a raccoon he trapped; signature clue matcher that ranks likely animals from the signs his own pages describe, with his job photos", "Fixed"),
            ("Photos", "His real job photos used throughout (traps, entry holes, droppings, cleanup, netting, solar, mounds); images that look generated or stock left out", "Fixed"),
            ("Wildlife-focused name (report note)", "Wildlife leads the design: raccoons, squirrels, bats and birds first; mosquito control not added (not on his site)", "Fixed"),
            ("5 stars from 198", "Not shown until confirmed", "Needs client"),
            ("No blog", "A new 1098-word post on cleaning up mouse droppings safely (CDC and National Park Service sources)", "Fixed"),
        ],
        "questions": ["Is 6870 S Village Green Rd, Cottonwood Heights (Google) OK to show, or should the site keep \"Northern Utah\" only?", "Can we show 5 stars from 198 Google reviews?", "Do you offer mosquito control? It has the most searches in the report.", "Is the dog in the polo shirt (Brownie) part of the brand? We left that photo out for now."],
        "pages": [("Home", "home/index.html"), ("Raccoons", "raccoons/index.html"), ("Birds", "birds/index.html"), ("About", "about/index.html"), ("New blog post", "how-to-clean-up-mouse-droppings/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/greenjanitorialservice.com", "name": "Green Janitorial Services", "city": "South Salt Lake, UT", "title": "Green Janitorial Review",
        "report": "2026-10-21_greenjanitorialservice.com_report.html", "old": "old_gj", "new": "new_gj",
        "stats": [("17", "pages, same URLs (+1 post)"), ("15", "space and clean combinations in the finder"), ("893", "home page words (was 376)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"janitorial services south salt lake\"; 2 H1s; no page names South Salt Lake", "One H1 naming janitorial services in South Salt Lake; title, meta and first sentence too", "Fixed"),
            ("No tap-to-call; no business schema; no sitemap", "Tap-to-call throughout; LocalBusiness schema with hours and areas; sitemap.xml and robots.txt", "Fixed"),
            ("Stock photos", "Not used. Their GJS vans are the banner; supporting photos are credited Wikimedia Commons pictures of South Salt Lake and Salt Lake City", "Fixed"),
            ("Template look", "\"Spotless & green\": vans banner under forest green with a leaf-green strip; signature service finder that matches space and type of clean to their services, in their words", "Fixed"),
            ("Ratings and badges", "5-star rating and BestProsInTown badge left out until confirmed; client quotes kept unnamed, as on the site", "Needs client"),
            ("7 of 7 report services have no page (carpet cleaning 1,600)", "Commercial, residential and specialized pages rebuilt; ask whether carpet cleaning is core before giving it its own page", "Needs client"),
            ("Blog posts missing from the sitemap", "Their 6 linked posts kept at the same URLs and added to the sitemap; a new 1194-word post on reading green cleaning labels (EPA, FTC sources)", "Fixed"),
        ],
        "questions": ["Can we show 5 stars from 201 Google reviews?", "Is carpet cleaning a core service you'd like its own page for?", "Do you have photos of your team or real jobs we could use?", "Should the duplicate home page (/home-4514) be removed?"],
        "pages": [("Home", "home/index.html"), ("Commercial", "commercial/index.html"), ("Residential", "residential/index.html"), ("Specialized", "specialized/index.html"), ("New blog post", "post/how-to-read-green-cleaning-labels/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/emetplumbingservices.com", "name": "Emet Plumbing Heating & Air", "city": "Taylorsville, UT", "title": "Emet Plumbing Review",
        "report": "2026-10-21_emetplumbingservices.com_report.html", "old": "old_em", "new": "new_em",
        "stats": [("14", "pages, same URLs (+1 post)"), ("5", "options totalled by the plan calculator"), ("548", "home page words (was 287)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"plumber taylorsville\"; 0 H1; no page names Taylorsville; 287-word home page", "One H1 naming a plumber in Taylorsville; title, meta and first sentence too; full home page from their own copy", "Fixed"),
            ("Address on site differs from Google", "Google NAP used (5941 S Redwood Rd, Taylorsville); the site lists 50 Broadway Ste. 300, Salt Lake City; flagged", "Needs client"),
            ("Fee conflict on their own site", "$59.99 diagnostic (about page) vs service call fee $59.00 (memberships page); both kept where they appear; flagged", "Needs client"),
            ("Unverified badges and stats", "A+ BBB, Google Guaranteed badges, HVAC page statistics (30%, 90%, 5-10 years) and anonymous quotes left out until confirmed", "Needs client"),
            ("Stock and AI images", "Only their own fleet, crew and install photos are used", "Fixed"),
            ("Template look", "\"Straight answers\": full-width photo of their fleet and crew with a $59.99 price tag; signature itemized plan calculator that totals a year with no plan and with each plan from their published rates", "Fixed"),
            ("10 of 10 report services have no page (drain cleaning 1,900)", "Services set out on the home page; separate pages wait for the client (plumbing or HVAC first?)", "Needs client"),
            ("Squarespace member template page live", "Kept at its URL, noindex; clients page noindex until real client names are confirmed", "Fixed"),
            ("Blog", "Their five posts kept at the same URLs; a new 1134-word post on furnace filters and MERV ratings (EPA, ENERGY STAR sources)", "Fixed"),
        ],
        "questions": ["Which address is current for customers: 5941 S Redwood Rd, Taylorsville (Google) or 50 Broadway Ste. 300, SLC (site)?", "Is the diagnostic $59.99 or the service call fee $59.00, or are they different charges?", "Can we show the A+ BBB rating and 4.4 stars from 201 Google reviews?", "Which side leads, plumbing or HVAC? Which service pages should we build first?"],
        "pages": [("Home", "home/index.html"), ("Memberships", "memberships/index.html"), ("HVAC", "hvac/index.html"), ("About", "about/index.html"), ("New blog post", "ourblog/furnace-filter-merv-ratings/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/everworklandscape.com", "name": "Everwork Property Maintenance & Landscaping", "city": "Sandy, UT", "title": "Everwork Review",
        "report": "2026-10-21_everworklandscape.com_report.html", "old": "old_ew", "new": "new_ew",
        "stats": [("41", "pages, same URLs (+1 post)"), ("12", "months on the season planner"), ("27", "city pages kept"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Live site changed after the audit", "The 21 Oct report saw 18 pages and no meta descriptions; the site has since been rebuilt (41 pages, alt text, schema). This draft works from the new live site.", "Needs Angelo"),
            ("Home target \"landscaping sandy\"; only 1 page names Sandy", "Home title, H1 and first sentence name landscaping in Sandy; Sandy in key service titles and metas", "Fixed"),
            ("Site claims \"5.0 / 5-star rated on Google\"", "Removed; the Google listing shows 4.9 from 210 reviews. Flagged.", "Needs client"),
            ("Template look", "\"Every season\": full-width photo of a lawn they maintain with an amber work-board strip; signature twelve-month season planner using their own timing (startup mid to late April, blowouts early Oct to early Nov, plows at 1-2 inches)", "Fixed"),
            ("Generated-looking service images", "Only their own job photos are used (lawns, night repairs, plow truck, before/afters)", "Fixed"),
            ("Tree trimming, aeration, mowing, pavers have no page", "Not on their site; ask before adding", "Needs client"),
            ("No blog", "A new 1368-word post on watering a Utah lawn (USU Extension, EPA WaterSense, Utah Division of Water Resources)", "Fixed"),
        ],
        "questions": ["The site says 5.0 / 5-star on Google; the listing shows 4.9 from 210. Can we show 4.9?", "Are the five reviews on the site from Google, and may we keep the names?", "Do you offer tree trimming, aeration or pavers? (your job photos show tree removal, retaining walls and stone steps)", "Is a business email available instead of the Gmail address?"],
        "pages": [("Home", "home/index.html"), ("Sprinkler repair", "services/sprinkler-repair/index.html"), ("Sandy", "service-areas/sandy/index.html"), ("Contact", "contact/index.html"), ("New blog post", "utah-lawn-watering-guide/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/iraut.com", "name": "Investment Realty Advisors", "city": "Midvale, UT", "title": "Investment Realty Advisors Review",
        "report": "2026-10-21_iraut.com_report.html", "old": "old_ira", "new": "new_ira",
        "stats": [("48", "pages, same URLs (+1 post)"), ("6", "services on the ecosystem wheel"), ("531", "home page words (was 101)"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Weak rating: 3.2 stars from 227", "A new site won't fix the rating; the rating is not shown anywhere. Flag to Angelo before pitching.", "Needs Angelo"),
            ("Home target \"property management midvale\"; no page names Midvale; 101-word home page", "Home title, H1 and meta name Midvale; full home page built from their own copy (ecosystem, figures, owner/investor/tenant paths, FAQ)", "Fixed"),
            ("No tap-to-call link; no business schema", "Tap-to-call in the header, hero, call bar and contact page; RealEstateAgent schema, breadcrumbs, FAQ and BlogPosting markup", "Fixed"),
            ("Two different assets-under-management figures", "$380M (property management page) used on the home page; the performance page keeps its own $400M+ wording; flagged", "Needs client"),
            ("Template look", "\"Ecosystem\": full-width aerial of one of their properties under the Wasatch with a figures ledger; signature six-service wheel, each panel showing that team's work, a real property photo and its figure", "Fixed"),
            ("28 Wix placeholder, duplicate and form pages", "Kept at the same URLs but noindex, with links to contact and property management", "Fixed"),
            ("8 of 8 report services have no page (HOA management 40)", "Existing service pages rebuilt; HOA management not offered on the site, ask before adding", "Needs client"),
            ("One placeholder blog post", "A new 1366-word post on 1031 exchange rules (IRS sources); the real Joseph Mills post kept", "Fixed"),
        ],
        "questions": ["Assets under management: $380M (PM page) or $400M+ (performance page)?", "Office address: Google says 411 W 7200 S, Midvale; the site lists a mailing address at 869 East 4500 South, PMB 224. Is 411 W 7200 S the public office?", "Do you offer HOA management?", "Should the Wix placeholder pages (team, listings, careers copies) be removed or rewritten?"],
        "pages": [("Home", "home/index.html"), ("Property management", "pm/index.html"), ("Commercial", "commercial-real-estate/index.html"), ("Self storage", "selfstorage/index.html"), ("Contact", "contactus/index.html"), ("New blog post", "post/1031-exchange-rules-for-utah-investors/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/applianceserviceut.com", "name": "ASI Appliance Services", "city": "Salt Lake City, UT", "title": "ASI Appliance Services Review",
        "report": "2026-10-21_applianceserviceut.com_report.html", "old": "old_asi", "new": "new_asi",
        "stats": [("5", "pages, same URLs (+1 post)"), ("14", "brands checked by the ticket"), ("30", "day guarantee, now up front"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"appliance repair salt lake city\"; no page names Salt Lake City; 284-word home page", "Home title, H1 and meta name Salt Lake City; full home page from their own copy (services, brands, areas, hours)", "Fixed"),
            ("Address on site differs from Google", "Google NAP used (2755 S 300 W); the site says 359 W Ironwood Dr; flagged", "Needs client"),
            ("No business schema", "Business schema with hours and payments, breadcrumbs, FAQ, Service and BlogPosting markup", "Fixed"),
            ("Stock photos", "Not used; credited Wikimedia Commons Salt Lake City photos", "Fixed"),
            ("Template look", "\"Service ticket\": skyline banner with a 30-day badge; signature carbon-copy ticket that checks area, appliance and brand and works out the next service day from their real hours and holidays", "Fixed"),
            ("10 of 10 report services have no page (dryer 590)", "Appliance and brand lists rebuilt on the services page; separate pages wait for the client", "Needs client"),
            ("No blog", "A new 1047-word post on clothes dryer fire safety (NFPA and U.S. Fire Administration sources)", "Fixed"),
        ],
        "questions": ["Which address is current: 2755 S 300 W (Google) or 359 W Ironwood Dr (your site)?", "Can we show 4.2 stars from 234 Google reviews?", "'The manufacturers trust us': are you an authorized warranty servicer for any brand?", "Do you have photos of your technicians, vans or shop?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("About", "about-us/index.html"), ("Contact", "contact/index.html"), ("New blog post", "clothes-dryer-fire-safety/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/triplejlandscaping.com", "name": "Triple J Landscaping", "city": "West Valley City, UT", "title": "Triple J Landscaping Review",
        "report": "2026-10-21_triplejlandscaping.com_report.html", "old": "old_tjl", "new": "new_tjl",
        "stats": [("8", "pages, same URLs (+1 post)"), ("7", "yard zones on the plan"), ("344", "words on the old home page; 800+ now"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"landscaping salt lake city\"; no page names Salt Lake City", "Home title, H1 and meta name Salt Lake City; Salt Lake County throughout", "Fixed"),
            ("Thin 7-page site, 344-word home page, no schema", "Full home page from their services and about copy; business, FAQ, Service and BlogPosting schema", "Fixed"),
            ("Gallery mixes AI-looking renders and stock with real jobs", "Only their clearly real job photos used (pavers with the Wasatch, flagstone, sod, xeriscape, concrete, sprinklers)", "Fixed"),
            ("Address on site, none on Google", "Site address shown (client-published); flagged", "Needs client"),
            ("Template look", "\"Grounded\": banner of their own paver job under the Wasatch; signature tap-a-zone yard plan that shows each service with a real job photo", "Fixed"),
            ("Unverified stats and testimonials (15+ years, 500+ projects)", "Left out until confirmed", "Fixed"),
            ("No blog", "A new 1195-word post on how much to water a Utah lawn (USU Extension sources)", "Fixed"),
        ],
        "questions": ["Show the West Valley City address, or stay service-area only like Google?", "Can we show 5.0 stars from 241 Google reviews and quote real ones?", "Your privacy page mentions triplejlandscaping.net: which domain is current?", "Are all gallery photos your own jobs? Some look like renders.", "Confirm '15+ years' and '500+ projects' before we add them back?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("Projects", "projects/index.html"), ("Get a quote", "get-a-quote/index.html"), ("New blog post", "how-much-to-water-your-lawn-in-utah/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/joestreecareutah.com", "name": "Joe's Tree Care", "city": "Salt Lake City, UT", "title": "Joe's Tree Care Review",
        "report": "2026-10-21_joestreecareutah.com_report.html", "old": "old_joe", "new": "new_joe",
        "stats": [("13", "pages, same URLs (+1 post)"), ("12", "of their own job photos used"), ("4", "H1s on the old home page; 1 now"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Google name is Joe's Stump Grinding; site says Joe's Tree Care", "Site brand kept (logo and copy); Google name as alternate name in schema; flagged", "Needs client"),
            ("Home target \"tree service salt lake city\"; no page names Salt Lake City; 4 H1s", "Home title, H1 and meta name Salt Lake City; one H1 per page", "Fixed"),
            ("No meta descriptions, no schema, no sitemap", "Unique titles and metas; business, FAQ, Service and BlogPosting schema; sitemap and robots", "Fixed"),
            ("Leftover lawn-care template text (\"40+ years\", mowing, aeration)", "Removed; only their real tree services, FAQ and 2018 story kept", "Fixed"),
            ("Stock photos mixed with real ones", "Only their own job photos, pulled at original size from their media storage", "Fixed"),
            ("Template look", "\"Heartwood\": full-width banner of their own stump grinder at work; signature before/after slider of their sod job plus a tree-care calendar from their FAQ", "Fixed"),
            ("No blog", "A new 1181-word post on watering trees in Utah (USU Extension sources)", "Fixed"),
        ],
        "questions": ["Which name should the site use: Joe's Tree Care or Joe's Stump Grinding?", "Can we show 5.0 stars from 292 Google reviews? (Your site says 150+.)", "Do you still offer lawn care (mowing, aeration)? Your site had template text for it.", "Any more before/after photos of stump grinding or removals?"],
        "pages": [("Home", "home/index.html"), ("Stump grinding", "stump-grinding/index.html"), ("Small landscaping", "small-landscaping/index.html"), ("Our work", "our-work/index.html"), ("Contact", "contact-us/index.html"), ("New blog post", "watering-trees-in-utah/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/utahbluechipcarpetcleaning.com", "name": "Blue Chip Carpet Cleaning", "city": "Salt Lake City, UT", "title": "Blue Chip Carpet Cleaning Review",
        "report": "2026-10-21_utahbluechipcarpetcleaning.com_report.html", "old": "old_bch", "new": "new_bch",
        "stats": [("17", "pages, same URLs (+1 post)"), ("10", "rooms on the price floor plan"), ("$89.95", "starting room price, now front and center"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet; report said check with Angelo first", "Draft only. The off-topic \"BEST WEBSITE DEALS!\" H1 turned out to be their online price list; it's now a proper prices section", "Needs Angelo"),
            ("Google phone not on the home page", "Google phone 801-785-7385 used everywhere (the site shows 801-645-3501); flagged for the client", "Needs client"),
            ("3 H1s, no tap-to-call, no schema, no sitemap", "One H1 per page; tap-to-call in header, hero, ticket and call bar; business, FAQ, Service and BlogPosting schema; sitemap and robots", "Fixed"),
            ("29 of 33 images without alt text; Wix stock photos", "No stock used; credited Wikimedia Commons Persian carpet photos tied to their rug-restoration story; alt text everywhere", "Fixed"),
            ("No page names Salt Lake City", "Home title, H1 and meta name Salt Lake City", "Fixed"),
            ("Template look", "\"Spotless\": Persian carpet banner; signature floor plan where you tap rooms and see the real online price, plus ducts and pet treatment", "Fixed"),
            ("Duct price differs between pages ($10 vs $15)", "Booking-page price ($15) used; flagged", "Needs client"),
            ("No blog", "A new 1249-word post on drying wet carpet after a leak (EPA sources)", "Fixed"),
        ],
        "questions": ["Which phone should the site use: 801-785-7385 (Google) or 801-645-3501 (site)?", "Air ducts: $10 or $15 per vent and return?", "Can we show 4.7 stars from 292 Google reviews?", "Which counties do you serve: Salt Lake and Utah, or also Summit and Tooele?", "Any photos of your team, van or rug work?"],
        "pages": [("Home", "home/index.html"), ("Prices", "services/index.html"), ("About", "about-us/index.html"), ("New blog post", "wet-carpet-after-a-leak/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/trustyappliancerepairutah.com", "name": "Trusty Appliance Repair", "city": "Sandy, UT", "title": "Trusty Appliance Repair Review",
        "report": "2026-10-21_trustyappliancerepairutah.com_report.html", "old": "old_trs", "new": "new_trs",
        "stats": [("12", "pages, same URLs (+1 post)"), ("7", "appliances on the control-panel dial"), ("90", "day warranty, now up front"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"appliance repair sandy\"; no page names Sandy; 0 H1s", "Home title, H1 and meta name Sandy; one H1 per page; Google NAP in footer, contact page and schema", "Fixed"),
            ("Site address (Midvale) differs from Google (Sandy)", "Google NAP used and copied exactly; flagged for the client", "Needs client"),
            ("No meta descriptions, no schema", "Unique titles and metas; business, breadcrumbs, FAQ, Service and BlogPosting markup; sitemap and robots", "Fixed"),
            ("All photos stock, brand logos as images", "No stock used; credited Wikimedia Commons kitchen and laundry photos; brands listed as text", "Fixed"),
            ("Template look", "\"Control panel\": kitchen banner with a 90-day warranty badge; signature dial that shows what they fix on each appliance and a tip from their own articles", "Fixed"),
            ("10 of 10 report services have no page (refrigerator 590, dryer 590)", "Each appliance now has its own section with an anchor on the services page; separate pages can follow if the client wants", "Needs client"),
            ("Tip articles only", "Six tip posts kept at their URLs; a new 1,200-word post on fridge and freezer temperatures (FDA sources)", "Fixed"),
        ],
        "questions": ["Which address is right: 8223 S 1000 E, Sandy (Google) or 255 W Amanda Lynn Ln, Midvale (your site)?", "Can we show 4.9 stars from 311 Google reviews?", "Do you have photos of your technicians or van?", "Want separate pages for refrigerator and dryer repair (590 searches each)?", "What are your hours?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("About", "about-us/index.html"), ("Tips", "blogs/index.html"), ("Contact", "contact-us/index.html"), ("New blog post", "refrigerator-freezer-temperature-food-safety/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/vogldirect.com", "name": "Vogl Direct", "city": "Eagle Mountain, UT", "title": "Vogl Direct Review",
        "report": "2026-10-21_vogldirect.com_report.html", "old": "old_vgl", "new": "new_vgl",
        "stats": [("23", "pages, same URLs (+1 post)"), ("3", "Comfort Club plans priced live"), ("49", "old mobile speed score"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"hvac company salt lake city\"; no page names Salt Lake City", "Home title, H1 and meta name Salt Lake City and Utah County; schema city Eagle Mountain (no street address: none on Google)", "Fixed"),
            ("No meta descriptions, no business schema", "Unique titles and metas on every page; HVACBusiness, breadcrumbs, FAQ, Service and BlogPosting markup; sitemap and robots", "Fixed"),
            ("Shutterstock photos and a lorem-ipsum page", "No stock used; credited Wikimedia Commons photos of Timpanogos and Utah Lake; the lorem-ipsum, empty and Hello world pages are kept noindex", "Fixed"),
            ("Mobile speed 49/100", "Plain HTML, WebP photos; mobile header fixed and checked", "Fixed"),
            ("Template look", "\"Direct\": Timpanogos banner with a free-second-opinion ticket; signature Comfort Club builder that adds up their real plan and add-on prices", "Fixed"),
            ("10 of 10 report services have no page (AC repair 1,900)", "Their own heating, cooling, installation, duct work, air quality, commercial and reclaim pages rewritten; separate repair pages wait for the client", "Needs client"),
            ("Blog was only WordPress's Hello world!", "A new 1347-word post on R-22 and refrigerant rules (EPA sources)", "Fixed"),
        ],
        "questions": ["Can we show 4.9 stars from 334 Google reviews?", "Which cities should we name? You're in Eagle Mountain; the report target is Salt Lake City.", "Do you have photos of your team, truck or installs?", "Are the Comfort Club prices and the current deals still right?", "Your cooling page says 'CO2 alarm'; we wrote carbon monoxide alarm. OK?"],
        "pages": [("Home", "home/index.html"), ("Heating", "heating/index.html"), ("Cooling", "cooling/index.html"), ("Comfort Club", "comfort-club/index.html"), ("Air quality", "air-quality/index.html"), ("Contact", "contact-us/index.html"), ("New blog post", "r-22-refrigerant-what-homeowners-should-know/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/ahc-utah.com", "name": "Affordable Heating & Cooling", "city": "Salt Lake City, UT", "title": "Affordable Heating & Cooling Review",
        "report": "2026-10-21_ahc-utah.com_report.html", "old": "old_ahc", "new": "new_ahc",
        "stats": [("18", "pages, same URLs (+1 post)"), ("153", "words on the old home page; 800+ now"), ("2", "seasons on the thermostat banner"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"hvac company salt lake city\"; no page names Salt Lake City", "Home title, H1 and first sentence name Salt Lake City; NAP in the header, footer, contact page and HVACBusiness schema", "Fixed"),
            ("Only 153 words on the home page", "Full home page from their own copy: services by season, about, Carrier and Lennox, financing, FAQ", "Fixed"),
            ("2 H1s; no tap-to-call", "One H1 per page; phone tap-to-call in the header, hero, CTA and a sticky call bar on phones", "Fixed"),
            ("No schema, no sitemap; 7 of 10 images without alt text", "HVACBusiness with NAP and hours, breadcrumbs, FAQ, Service and BlogPosting markup; sitemap and robots; alt text everywhere", "Fixed"),
            ("Stock slider photos", "Not used; credited open-license photos of Salt Lake parks near their office (Liberty Park, Sugar House Park) and the valley inversion", "Fixed"),
            ("Template look", "\"Both seasons\": a thermostat card switches the banner between winter and summer, the headline, the dial and the service tab (signature)", "Fixed"),
            ("Mobile speed 63/100", "Plain HTML, WebP photos; mobile header fixed and checked", "Fixed"),
            ("10 of 10 report services have no page (AC repair 1,900, furnace repair 1,300)", "Not invented as separate pages yet; services page lists their real services by group. Repair pages wait for the client", "Needs client"),
            ("No blog", "A new 1472-word post on carbon monoxide safety at home (EPA and NFPA sources)", "Fixed"),
        ],
        "questions": ["Can we build separate AC repair and furnace repair pages? (1,900 and 1,300 searches.)", "Can we show 4.9 stars from 565 Google reviews and quote a few?", "Current promotions: the archived payment amounts are from Feb 2024. What's running now?", "Do you have photos of your team, trucks or installs to replace the park photos?", "Is the Service Finance Company application link still the same?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("About", "About-Affordable/index.html"), ("Carrier furnaces", "Carrier-Furnaces/index.html"), ("Financing", "Financing/index.html"), ("Contact", "Contact/index.html"), ("New blog post", "carbon-monoxide-safety/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/mountainwindowcleaning.com", "name": "Mountain Window Cleaning", "city": "Sandy, UT", "title": "Mountain Window Cleaning Review",
        "report": "2026-10-21_mountainwindowcleaning.com_report.html", "old": "old_mwc", "new": "new_mwc",
        "stats": [("7", "pages, same URLs (+1 post)"), ("6", "real prices in the rate card and estimator"), ("$150", "visit minimum built into the estimator"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"window cleaning sandy\"; no page names Sandy", "Home title, hero label and meta name Sandy; schema city Sandy (street address not shown: not on their site)", "Fixed"),
            ("No business schema, no sitemap", "Business schema with phone, area served and prices; breadcrumbs, FAQ, Service, OfferCatalog and BlogPosting markup; sitemap.xml and robots.txt", "Fixed"),
            ("Stock-looking photos (UK brick house, posed worker, squeegee close-up, gable-roof solar house)", "Not used; only their own Utah job photos and Utah scenery from their site; the solar card uses a drawn panel instead of stock", "Fixed"),
            ("Template look", "\"Pure water\": full-width valley view behind glass fogged with hard-water spots that you squeegee clear (signature); tap vs pure water drop diagram; rate card; working estimator on the quote page", "Fixed"),
            ("Mobile header", "Mobile header fix applied and checked", "Fixed"),
            ("7 of 8 report services have no page (pressure washing 480, gutters 260, Christmas lights 170)", "Not invented. Window and solar pages kept; other pages wait for the client's list", "Needs client"),
            ("No blog", "A new 1,500-word post on why birds hit windows (American Bird Conservancy and Audubon sources)", "Fixed"),
        ],
        "questions": ["Do you offer pressure washing, gutter cleaning or Christmas lights? Those are bigger searches than solar.", "Are the hero home, the stone and modern homes, the log home and the storefront your own jobs?", "Can we show 5.0 stars from 390 Google reviews, and quote a few reviews?", "Show the Sandy address, or keep it service-area only?", "Keep Housecall Pro as the booking link?"],
        "pages": [("Home", "home/index.html"), ("Window cleaning", "window-cleaning.html"), ("Solar panels", "solar-panel-cleaning.html"), ("Pricing", "pricing.html"), ("Instant quote", "quote.html"), ("New blog post", "why-birds-hit-windows.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/rwkconstruction.com", "name": "RWK Construction Co.", "city": "Bluffdale, UT", "title": "RWK Construction Review",
        "report": "2026-10-21_rwkconstruction.com_report.html", "old": "old_rwk", "new": "new_rwk",
        "stats": [("20", "pages, same URLs (+1 post)"), ("22", "real client reviews kept"), ("3", "project rules checked live in the planner"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"general contractor bluffdale\"; no page names Bluffdale", "Home title, hero and lede name Bluffdale and \"general contractor\"; office NAP in the header, footer, contact page and GeneralContractor schema", "Fixed"),
            ("6 H1s on the home page", "One H1 per page", "Fixed"),
            ("Gallery photos broken: most gallery images on the live site return 404", "Galleries rebuilt from the photos that still load (the Adele Lamb architecture shoots, a basement, a theater room, the S Amanda Lane home)", "Fixed"),
            ("No schema, no sitemap", "GeneralContractor with NAP and hours, breadcrumbs, FAQ, Service and BlogPosting markup; sitemap.xml and robots.txt", "Fixed"),
            ("Images without alt text", "Every image has alt text and dimensions", "Fixed"),
            ("Mobile speed 70/100", "Plain HTML instead of the WordPress theme, WebP photos; mobile header fixed and checked", "Fixed"),
            ("Template look", "\"Below grade\": full-bleed photo of their family room cut by a dimensioned grade line; signature \"Plan your basement\" section drawing that checks RWK's own rules (500 sq ft, 1975 or newer, walkouts with a full finish)", "Fixed"),
            ("Unproven claims (\"the best in Utah\", \"Award wining contractor\", \"Five-Star\")", "Left out until confirmed; the reviews speak instead", "Fixed"),
            ("9 of 9 report services have no page (kitchen 880, bathroom 720 searches)", "Not invented. Their own services page (basements, renovations, theaters) kept; kitchen and bathroom pages wait for the client", "Needs client"),
            ("Thin blog", "Six old posts kept at their URLs; a new 1,700-word post on radon testing in Utah homes (EPA sources)", "Fixed"),
        ],
        "questions": ["Do you do kitchen and bathroom remodels as their own jobs? Those are the biggest searches (880 and 720).", "Can you send the basement, theater and remodel gallery photos again? Most files on the live site are gone (404).", "Can we show 4.9 stars from 458 Google reviews?", "Are the Alta condo and Saratoga Springs shoots RWK projects we can caption by city?", "Is the home office address in Bluffdale OK to show publicly?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("Galleries", "galleries/index.html"), ("Process", "process/index.html"), ("Reviews", "testimonials/index.html"), ("Contact", "contact/index.html"), ("New blog post", "radon-testing-utah-homes/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/5starkb.com", "name": "5 Star Kitchen and Bath", "city": "Midvale, UT", "title": "5 Star Kitchen and Bath Review",
        "report": "2026-10-21_5starkb.com_report.html", "old": "old_kb", "new": "new_kb",
        "stats": [("17", "pages, same URLs (+1 post)"), ("1,102", "words in the new blog post"), ("4", "before/after projects in the slider"), ("0", "real QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"bathroom remodeling midvale\"; no page names Midvale", "Home title, H1 and first lines name Midvale; kitchens and bathrooms pages target Midvale too", "Fixed"),
            ("Mobile speed 35/100; 6 H1 headings (some empty); no meta description; no schema", "Plain HTML, resized WebP photos; one H1 per page; unique metas; business schema with hours and the Google NAP", "Fixed"),
            ("29 of 49 images without alt text; Adobe Stock banner and manufacturer renders", "Only their own job photos, every one with alt text; stock and manufacturer images removed", "Fixed"),
            ("Template look", "\"Before / After\": a full-bleed photo banner of their own kitchen; signature draggable before/after slider built from their own composites; photo-led rooms and gallery", "Fixed"),
            ("Testimonials page is unedited template text (\"Click to edit... Customer Name\")", "No testimonials shown; page kept but noindex until real reviews are supplied", "Needs client"),
            ("Claims: 10+ years, A+ BBB, 5-star reviews, best choice, 200-location dealer network", "Left out until confirmed", "Needs client"),
            ("7 of 8 services have no page (countertops, cabinets, replacement windows...)", "Kitchens, bathrooms, walk-in tubs and windows pages rebuilt; ask about dedicated countertop and cabinet pages", "Needs client"),
            ("No blog", "A new 1,102-word post on bathroom moisture and mold (EPA)", "Fixed"),
        ],
        "questions": ["Can we show 10+ years, the A+ BBB rating and 4.7 stars from 527 Google reviews?", "Can you send real customer testimonials for the testimonials page?", "Do you want countertop and cabinet pages (480 and 210 searches)?", "Which email should the site show: sales@, support@ or steve@?"],
        "pages": [("Home", "home/index.html"), ("Before & after", "home/index.html#before-after"), ("Kitchens", "kitchens/index.html"), ("Bathrooms", "bathrooms/index.html"), ("Kitchen gallery", "kitchen_gallery/index.html"), ("New blog post", "blog/bathroom-moisture-mold-guide/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/acs-hoa.com", "name": "Advanced Community Services", "city": "Lehi, UT", "title": "ACS HOA Review",
        "report": "2026-10-21_acs-hoa.com_report.html", "old": "old_acs", "new": "new_acs",
        "stats": [("9", "pages, same URLs (+1 post)"), ("1,113", "words in the new blog post"), ("6", "requests in the action-item board"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet; 3.2-star Google rating", "Draft only. Do not contact this business. Flag the rating to Angelo before any pitch", "Needs Angelo"),
            ("Home target \"property management lehi\"; domain says HOA", "HOA management leads: home title, H1 and first lines name Lehi and HOA management", "Fixed"),
            ("3 H1 headings; no business schema; no sitemap; no canonicals", "One H1 per page; business schema with the Lehi address, FAQ, Service and BlogPosting markup; sitemap and self-canonicals", "Fixed"),
            ("18 of 19 images without alt text; all stock (models, device mockups, houses)", "No stock photos; typographic design around their logo", "Fixed"),
            ("Phone: site 1-877-844-4227 vs Google 801-641-1844", "Both shown: toll-free and Lehi office; confirm the main number", "Needs client"),
            ("2015-era site: office list (Clearfield, Lehi, Eagle Mountain, St. George, Park City x2), \"patented\" software", "Offices shown as listed (confirm they're current); \"patented\", \"premier\" and \"years of experience\" left out", "Needs client"),
            ("Template look", "\"The board's desk\": a meeting agenda hero; signature Community Action Items board where a request moves from reported to closed, naming the ACS service at each step", "Fixed"),
            ("8 of 8 services have no page", "Three service pages rebuilt with every listed service; ask which (condo, community association) deserve their own pages", "Needs client"),
            ("No blog", "A new 1,113-word winter checklist for HOA boards (Ready.gov, Red Cross)", "Fixed"),
        ],
        "questions": ["The 3.2-star rating: does Angelo still want to pitch?", "Which phone is main: 1-877-844-4227 or 801-641-1844?", "Are the listed offices (Clearfield, Eagle Mountain, St. George, Park City) still open?", "Should rental property management or HOA management lead?"],
        "pages": [("Home", "home/index.html"), ("Action items", "home/index.html#action-items"), ("Management", "management-services.html"), ("Professional", "professional-services.html"), ("Testimonials", "testimonials.html"), ("New blog post", "blog/hoa-winter-checklist-utah/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/equitypmusa.com", "name": "Equity Real Estate Property Management", "city": "Sandy, UT", "title": "Equity PM Review",
        "report": "2026-10-21_equitypmusa.com_report.html", "old": "old_eq", "new": "new_eq",
        "stats": [("22", "pages, same URLs (+1 post)"), ("1,047", "words in the new blog post"), ("27", "owner FAQs kept"), ("0", "real QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"property management sandy\"; thin home page (196 words); no page names Sandy", "Home title, H1 and first lines name Sandy; the home page now carries their programs, numbers and FAQs", "Fixed"),
            ("13 /properties pages are Wix template sample listings (fake addresses, \"Brenda Rogers\", built year 2034)", "Same URLs kept but noindex, pointing to tenant and owner pages; remove them on the live site", "Needs client"),
            ("4 of 7 images without alt text; stock and AI interiors", "No stock or AI photos; typographic design around their logo; every image has alt text", "Fixed"),
            ("Programs only in an image (comparison chart)", "Rebuilt as a real, readable table: Tenant placement vs Full service", "Fixed"),
            ("Template look", "\"The owner's ledger\": navy and ruled paper, tabular serif figures; signature Rent math calculator (owner/renter) built only from their published fees and criteria", "Fixed"),
            ("Claims: 1.2% eviction rate, 75% of renters have pets, one of the most established brokerages", "Left out until confirmed", "Needs client"),
            ("8 of 8 services have no page", "Not invented; owners, tenants and agents each have a page. Ask about HOA management (the biggest search term)", "Needs client"),
            ("No blog", "A new 1,047-word post for renters on spotting rental listing scams (FTC)", "Fixed"),
        ],
        "questions": ["Can the Wix sample listing pages be removed (or replaced with real available rentals)?", "Do you manage HOAs? \"hoa management\" is the biggest search term in the report", "Can we show the 1.2% eviction rate and the 4.4-star Google rating?", "Are the fee ranges (50-100% placement, 8-10% monthly) still current?"],
        "pages": [("Home", "home/index.html"), ("Rent math", "home/index.html#rent-math"), ("Owner information", "copy-of-landlords/index.html"), ("FAQs", "copy-of-contact-us/index.html"), ("Application criteria", "copy-of-tenants/index.html"), ("New blog post", "blog/how-to-spot-a-rental-scam/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/abode.cleaning", "name": "Abode House Cleaning", "city": "Draper, UT", "title": "Abode House Cleaning Review",
        "report": "2026-10-21_abode.cleaning_report.html", "old": "old_ab", "new": "new_ab",
        "stats": [("7", "pages, same URLs (+1 post)"), ("1,037", "words in the new blog post"), ("7", "prep steps in the get-ready checklist"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"house cleaning draper\"; no page names Draper", "Home title, H1 and first lines name Draper", "Fixed"),
            ("No phone on the site; no tap-to-call", "Google's number (801) 845-0297 added as tap-to-call everywhere; confirm it", "Needs client"),
            ("2 H1 headings; no business schema; no sitemap; no canonicals", "One H1 per page; business schema with the Google NAP, FAQ and BlogPosting markup; sitemap and self-canonicals", "Fixed"),
            ("Google address \"126 12300 S Suite A\" vs the site's legal pages \"126 W 12300 S\"", "Google version shown (copied exactly); the missing \"W\" needs checking", "Needs client"),
            ("Service area: \"Roy to Spanish Fork\" (home) vs \"Ogden to Payson and St. George\" (services)", "Both kept where they appear; ask which is right", "Needs client"),
            ("Claims: 20,000+ homes, 6+ years, 400+ teams, 4.8 from 400+ reviews, nationwide", "Left out until confirmed; reviews kept word for word", "Needs client"),
            ("Template look", "\"Come home to clean\": stills from their own brand film, Abode violet; signature get-ready checklist from their own prep policy with a readiness meter and their arrival windows", "Fixed"),
            ("7 of 7 services have no page", "Not invented. Their booking app loads the plans; ask which services (office, move-out) to give pages", "Needs client"),
            ("No blog", "A new 1,037-word post on cleaning products and indoor air (EPA Safer Choice and indoor air quality)", "Fixed"),
        ],
        "questions": ["Is (801) 845-0297 the number to show (the site lists none)?", "Which service area is right: Roy to Spanish Fork, or Ogden to Payson plus St. George?", "Can we show the 20,000+ homes, 6+ years and review figures?", "Is the VIP100U offer ($100 off the first recurring cleaning) still running?"],
        "pages": [("Home", "home/index.html"), ("Get ready", "home/index.html#ready"), ("Services", "our-services/index.html"), ("Cancellation policy", "cancellation-policy/index.html"), ("New blog post", "blog/safer-cleaning-products-indoor-air/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/lockthesmithut.com", "name": "Lockthesmith", "city": "West Valley City, UT", "title": "Lockthesmith Review",
        "report": "2026-10-21_lockthesmithut.com_report.html", "old": "old_lk", "new": "new_lk",
        "stats": [("11", "pages, same URLs (+1 post)"), ("1,090", "words in the new blog post"), ("23", "services from their own list"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"locksmith west valley city\"; tab title \"lockthesmithut\"", "Home title, H1 and first lines name West Valley City; a real title and meta description on every page", "Fixed"),
            ("Leftover WordPress pages live (hello-world, new-site 1-3, sample About with coaching-theme filler, 4 logo attachment pages)", "Same URLs kept but noindex, pointing to the real content; About rewritten from their own home-page copy. Remove or redirect them on the live site", "Needs client"),
            ("3 H1 headings; no business schema", "One H1 per page; Locksmith schema with the Google NAP, storefront hours, service catalog, FAQ and BlogPosting markup", "Fixed"),
            ("8 of 8 images without alt text; hero copied from another locksmith's site; stock photos", "No borrowed or stock photos; the site is drawn around their key logo", "Fixed"),
            ("Template look", "\"Brass & steel\": graphite and brass, a stamped-key grotesque; signature pin-tumbler lock: pick a problem, the pins set, the plug turns and the service appears; live open-now status from their real hours", "Fixed"),
            ("Email on a different domain (service@lockthesmith.com)", "Kept as on the site; confirm it's theirs", "Needs client"),
            ("\"Complimentary service call\" offer; \"Expert Experience Guaranteed\"", "The offer is kept as stated (confirm); the guarantee is left out", "Needs client"),
            ("10 of 10 services have no page", "Not invented; all 23 services from their own list are on the home page and in schema. Ask which deserve their own pages", "Needs client"),
            ("No blog", "A new 1,090-word post on hot-car safety: call 911 first (NoHeatStroke.org, NHTSA)", "Fixed"),
        ],
        "questions": ["Is service@lockthesmith.com the right email (the site is lockthesmithut.com)?", "Is the complimentary service call for new customers still offered?", "Which services should get their own pages first (report: car key replacement, key fob programming)?", "OK to remove the leftover WordPress pages on the live site?"],
        "pages": [("Home", "home/index.html"), ("The lock", "home/index.html#lock"), ("Hours", "home/index.html#hours"), ("About", "about/index.html"), ("New blog post", "blog/hot-car-safety-utah/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/rasmussenlandscapes.com", "name": "Rasmussen Landscapes", "city": "South Salt Lake, UT", "title": "Rasmussen Landscapes Review",
        "report": "2026-10-21_rasmussenlandscapes.com_report.html", "old": "old_ras", "new": "new_ras",
        "stats": [("95", "pages, same URLs (+1 post)"), ("1,335", "words in the new blog post"), ("13", "seasonal jobs in the Yard year dial"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"landscaping south salt lake\"; no page names South Salt Lake; 269 words on the home page", "Home title, H1 and first lines name South Salt Lake; the home page now carries 1,000+ words of their own know-how", "Fixed"),
            ("Every page shares one generic title and has no meta description", "A unique title and meta description on all 95 pages", "Fixed"),
            ("No business schema", "Business schema with the Google NAP, plus breadcrumbs, FAQ, Service and BlogPosting markup", "Fixed"),
            ("Address: site says 3446 S West Temple, Salt Lake City; Google says 3446 S W Temple St, South Salt Lake", "Google version shown (copied exactly); confirm with the client", "Needs client"),
            ("19 of 19 images without alt text; stock and template images (tea, mockups, spreader, snowblower)", "Only their own job photos, all with alt text; template images removed", "Fixed"),
            ("Template filler left on some pages (values pages, Projects: \"Write a tagline\", \"Project Name\", 555 555-5555)", "Filler removed; real sentences kept; Portfolio and Projects now show their job photos", "Needs client"),
            ("Mobile speed 53/100", "Plain HTML, resized WebP photos; mobile header checked", "Fixed"),
            ("Template look", "\"Your yard. Our work.\": a garden journal with their photography, Fraunces serif, badge greens; signature Yard year dial showing what they do each month, quoted from their own pages", "Fixed"),
            ("Claims: Utah's premier, best in the business, 50+ years", "Left out of their copy until confirmed (customer reviews kept word for word; History keeps the owner's story)", "Needs client"),
            ("Thin blog", "A new 1,335-word post on when and how much to water a Utah lawn (Utah Division of Water Resources, USU, KSL)", "Fixed"),
        ],
        "questions": ["Which address should the site show: Salt Lake City (site) or South Salt Lake (Google)?", "Can we say \"over 50 years\" / since 1971 on the home page?", "Universal Analytics (UA-162917173-1) stopped collecting in 2023: add a GA4 ID?", "Should the template-filler pages (values subpages, Projects, Media) be rewritten or removed?"],
        "pages": [("Home", "home/index.html"), ("Sprinklers", "sprinklers/index.html"), ("Design & Build", "DesignBuild/index.html"), ("Maintenance", "Services/index.html"), ("Salt Lake City", "salt-lake-city/index.html"), ("Portfolio", "portfolio/index.html"), ("New blog post", "blog/when-to-water-your-lawn-utah/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/ezelectric.com", "name": "EZ Electric", "city": "Salt Lake City, UT", "title": "EZ Electric Review",
        "report": "2026-10-21_ezelectric.com_report.html", "old": "old_ez", "new": "new_ez",
        "stats": [("7", "pages, same URLs (+1 post)"), ("1,076", "words in the new blog post"), ("10", "breakers in the service panel"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"electrician salt lake city\"; no page names Salt Lake City", "Home title, H1 and first lines name Salt Lake City and Utah County; service page titles too", "Fixed"),
            ("0 H1 headings on the home page", "One H1 per page", "Fixed"),
            ("No business schema", "Electrician schema with hours, service area and profiles; breadcrumbs, FAQ, Service and BlogPosting markup", "Fixed"),
            ("Two phone numbers: (385) 284-0394 on the header/contact page, (385) 220-7815 in the footer and on Google", "284-0394 used as the main number; ask which one is primary", "Needs client"),
            ("Stock photos (multimeter, hard hat, pool, Unsplash breakers)", "Not used; only their own three job photos, plus drawn graphics", "Fixed"),
            ("Mobile speed 63/100", "Plain HTML, resized WebP photos; mobile header checked", "Fixed"),
            ("Template look", "\"Flip it on\": dusk palette from their landscape-lighting photo, EZ red and bulb amber; signature breaker panel where each breaker is one of their services and the main lights them all", "Fixed"),
            ("Claims: over 15 years, top-rated, quality guaranteed, certified; a review labelled \"CEO, Acme Industries\" (template text)", "Left out until confirmed; the review is kept with the name only", "Needs client"),
            ("10 of 10 services have no page", "Not invented; their three service pages keep every section, with a contents list. Ask which services deserve their own pages", "Needs client"),
            ("No blog", "A new 1,076-word post on winter electrical safety (NFPA and CPSC sources)", "Fixed"),
        ],
        "questions": ["Which number is main: (385) 284-0394 or (385) 220-7815?", "Can we say \"over 15 years\" and show 4.9 stars from 641 Google reviews?", "Which services should get their own pages first (report: lighting installation, emergency electrician, ceiling fans)?", "Is there an emergency or after-hours service? The site lists Mon-Fri 8-6 only."],
        "pages": [("Home", "home/index.html"), ("Residential", "residential-services/index.html"), ("Commercial", "commercial-services/index.html"), ("Outdoor & specialty", "outdoor-specialty-electrical-services/index.html"), ("Contact", "contact/index.html"), ("New blog post", "blog/winter-electrical-safety-utah/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/therepairpros.com", "name": "The Repair Pros", "city": "Salt Lake City, UT", "title": "The Repair Pros Review",
        "report": "2026-10-21_therepairpros.com_report.html", "old": "old_rp", "new": "new_rp",
        "stats": [("4", "pages, same URLs (+1 post)"), ("1,173", "words in the new blog post"), ("61", "cities in the service-area tool"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("HTTPS is broken (certificate name mismatch / expired); the site only works over http", "Same http URLs and canonicals kept; switch to https once the certificate is fixed", "Needs client"),
            ("Home target \"appliance repair salt lake city\"; no page names Salt Lake City", "Home title, H1 and first lines name Salt Lake City; the four counties and 61 cities in a service-area tool", "Fixed"),
            ("No meta descriptions", "Unique meta description on every page", "Fixed"),
            ("No business schema", "Business, breadcrumb, FAQ and BlogPosting markup; service-area business, no address (as on Google)", "Fixed"),
            ("29 of 37 images without alt text", "Every image has alt text and dimensions; stock (Unsplash stars, electronics bench) removed", "Fixed"),
            ("Template look", "\"The service manual\": numbered sections, figure captions on their own job photos, spec readouts; signature \"Diagnose\": pick product and symptom, a work order prints with the real $125 / $150-$400 / 90-day facts and pre-fills the booking form", "Fixed"),
            ("Claims: hundreds of 5-star reviews, several awards", "Left out; factory-authorized brands and \"only authorized Philips TV center in Utah\" kept as stated", "Needs client"),
            ("10 of 10 services have no page", "Not invented; every service has a symptom set and a deep link on the home page. Service pages wait for the client's word", "Needs client"),
            ("No blog", "A new 1,173-word post: repair or replace, with the NAHB appliance life-expectancy table and ENERGY STAR figures", "Fixed"),
        ],
        "questions": ["Can the HTTPS certificate be fixed so the site can move to https?", "Which services should get their own pages first (report: dryer, washer, refrigerator)?", "Can we show 4.8 stars from 942 Google reviews?", "Confirm: the only authorized Philips TV service center in Utah, Samsung branded engineer, Sharp master service center?"],
        "pages": [("Home", "home/index.html"), ("Diagnose tool", "home/index.html#diagnose"), ("Pricing", "home/index.html#pricing"), ("New blog post", "blog/repair-or-replace-appliance-lifespan/index.html"), ("Privacy policy", "website-privacy-policy/index.html")],
    },
    {
        "key": "New/Weak-Site-Businesses/pestx.org", "name": "Pestx", "city": "Midvale, UT", "title": "Pestx Review",
        "report": "2026-10-21_pestx.org_report.html", "old": "old_px", "new": "new_px",
        "stats": [("19", "pages, same URLs (+1 post)"), ("1,497", "words in the new blog post"), ("7", "zones in the house diagram"), ("0", "QA issues")],
        "fixes": [
            ("Not a client yet", "Draft only. Do not contact this business.", "Needs Angelo"),
            ("Home target \"pest control midvale\"; no page names Midvale", "Home title, H1 and first lines name Midvale; office address from the Google profile in the footer, contact page and schema", "Fixed"),
            ("3 H1s on the home page", "One H1 per page; pest pages keep Identification / Elimination / Prevention as H2s", "Fixed"),
            ("No tap-to-call", "Phone in the header, hero, sidebar, CTA and a sticky call bar on phones", "Fixed"),
            ("No schema", "PestControl business with the Google NAP, breadcrumbs, FAQ, Article and BlogPosting markup", "Fixed"),
            ("57 of 57 images without alt text", "Every image has alt text and dimensions", "Fixed"),
            ("Photos are AI-generated scenes and specimen renders", "Not used; only the brand's own ink-wash drawings, used as illustrations", "Fixed"),
            ("Mobile speed 70/100", "Plain HTML instead of Framer, small WebP drawings; mobile header checked", "Fixed"),
            ("Template look", "\"A field guide to the Utah home\": specimen plates, numbered field notes, their plum and fonts; signature \"Full home coverage\" house where each lettered zone shows its pests", "Fixed"),
            ("10 of 10 services have no page", "Not invented. The ten pest pages stay as they are; service pages wait for the client's list", "Needs client"),
            ("Thin blog", "A new 1,497-word post on ticks in Utah (USU Extension, Utah DHHS, CDC sources)", "Fixed"),
        ],
        "questions": ["Which services does Pestx sell (general pest plans, mosquito, rodent, wasp)? The report shows 10 with no page.", "Show 661 W 7250 S, Midvale as the office address on the site?", "Can we show 4.9 stars from 1,003 Google reviews?", "The old home FAQ answers were hidden: send the wording to add them back?", "OK to keep Google Analytics G-41HFW67EXT as on the live site?"],
        "pages": [("Home", "home/index.html"), ("Field guide", "pests/index.html"), ("Mosquito", "pests/mosquito/index.html"), ("Rodents", "pests/rodents/index.html"), ("Blog", "blogs/index.html"), ("Contact", "contact/index.html"), ("New blog post", "blogs/ticks-in-utah/index.html")],
    },
    {
        "key": "Foundation-Waterproofing-Restoration/foundationrepairogden.com", "name": "Fortified Foundations", "city": "Ogden, UT", "title": "Fortified Foundations Review",
        "report": "2026-10-19_foundationrepairogden.com_report.html", "old": "old_og", "new": "new_og",
        "stats": [("15", "pages, same URLs (+1 post)"), ("1,084", "words in the new blog post"), ("2", "modes in the heave drawing"), ("0", "QA issues")],
        "fixes": [
            ("\"Check first\": no Google profile; lead-generation template (quote funnel, /opt-out, badge reviews)", "Built from the site's own facts only; flagged: confirm the real business before outreach", "Needs Angelo"),
            ("Live site behind a Cloudflare block", "Rebuilt from Internet Archive captures (home Dec 2024, other pages Sep 2020); report counts 23 pages, so some are missing", "Needs Angelo"),
            ("Unverifiable claims: engineers, certified, licensed/insured/bonded, badge ratings, initial-only testimonials, $5,000-$15,000 prices", "Left out", "Needs client"),
            ("No page names Ogden; meta descriptions missing", "Home targets \"foundation repair ogden\"; a unique meta on every page", "Fixed"),
            ("Stock images only", "1870s photographs of Ogden and Ogden Canyon (U.S. National Archives, public domain, credited as atmosphere) in ink duotone, plus drawings", "Fixed"),
            ("Template look, no signature", "v2 \"The same ground\": cinematic archive hero with a line-by-line headline reveal, parallax canyon band, granite header, towns marquee; signature \"Heave or settle?\" from the client's own clay explanation", "Fixed"),
            ("No blog", "A new 1,084-word earthquake readiness post (Ready.gov, Red Cross)", "Fixed"),
        ],
        "questions": ["Angelo: who actually owns this site and answers (385) 213-2324?", "Can the client send the current pages (23 now vs 12 archived) and a street address?", "Is \"Fortified Foundations\" a real registered business? The wordmark here is typographic only.", "Can the claims (insured, bonded, engineers) be backed up?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("Roy", "foundation-repair-roy-weber-county/index.html"), ("About", "about/index.html"), ("Contact", "contact/index.html"), ("New blog post", "blog/earthquake-ready-home-ogden/index.html")],
    },
    {
        "key": "Foundation-Waterproofing-Restoration/rhinofoundationsystems.com", "name": "Rhino Foundation Systems", "city": "American Fork, UT", "title": "Rhino Foundation Systems Review",
        "report": "2026-10-19_rhinofoundationsystems.com_report.html", "old": "old_rh", "new": "new_rh",
        "stats": [("35", "pages, same URLs (+1 post)"), ("1,230", "words in the new blog post"), ("5", "soil layers in the pier drawing"), ("0", "QA issues")],
        "fixes": [
            ("Live site unreachable from our network (connection timed out)", "Rebuilt from the Internet Archive's Jul-Sep 2025 captures of all 30 sitemap and nav pages; the report counts 96 pages now, so newer pages are missing", "Needs Angelo"),
            ("Home target \"foundation repair american fork\"; Google profile in American Fork", "Home title, H1 and first sentence; service pages keep their Salt Lake City titles", "Fixed"),
            ("Phone: site shows 801-509-5344, Google shows 435-660-5182; no address on the site", "Site's own phone and email used; Google address and number flagged", "Needs client"),
            ("Unverified claims: 40+ years, since 1985, thousands of customers, hundreds of 5-star reviews, certified, warranties, case studies", "Left out until confirmed; \"licensed and insured\" kept as stated", "Needs client"),
            ("Stock photos (Depositphotos, Adobe, iStock) and cartoon illustrations", "Not used; only their own photos (truck, piers, installs, measured slabs)", "Fixed"),
            ("Mobile speed 65/100", "Plain HTML, resized WebP photos; mobile header checked", "Fixed"),
            ("Template look, no signature", "\"Down to solid ground\": wide heavy type, Rhino blue, soil strata palette; signature \"Drive the pier\" soil section where the house levels once the pier bears", "Fixed"),
            ("No blog", "A new 1,230-word post on radon and foundation cracks (EPA sources)", "Fixed"),
        ],
        "questions": ["Can the client send the current page list or a site export (96 pages now vs 30 archived)?", "Which phone is main: 801-509-5344 (site) or 435-660-5182 (Google)? Show the American Fork address?", "Can we show 4.7 stars from 290 reviews, and the years in business?", "OK to keep GTM-PKK38W6K as on the live site?"],
        "pages": [("Home", "home/index.html"), ("Foundation repair", "foundation-repair/index.html"), ("Helical & push piers", "helical-piers-push-piers/index.html"), ("Basement waterproofing", "basement-waterproofing/index.html"), ("American Fork", "service-area/foundation-repair/american-fork/index.html"), ("Contact", "contact-us/index.html"), ("New blog post", "blog/radon-foundation-cracks/index.html")],
    },
    {
        "key": "sandsroofingutah.com", "name": "S&S Roofing, Inc.", "city": "West Valley City, UT", "title": "S&S Roofing Review",
        "report": "2026-10-17_sandsroofingutah.com_report.html", "old": "old_ss", "new": "new_ss",
        "stats": [("51", "pages, same URLs (+1 post)"), ("1,154", "words in the new blog post"), ("5", "layers in the roof builder"), ("0", "QA issues")],
        "fixes": [
            ("Home target \"roofing company west valley city\"; only 2 pages name West Valley City", "Home title, H1 and first sentence; West Valley City named across the home page and service pages", "Fixed"),
            ("Address: the site says Salt Lake City, the Google profile says West Valley City (same street and ZIP)", "Site's own wording kept character-for-character; flagged", "Needs Angelo"),
            ("4.6 stars from 149 reviews (Google profile)", "Not shown as a number until the client confirms it", "Needs client"),
            ("Mobile speed 72/100", "Plain HTML, resized WebP photos, lazy-loaded below the fold; mobile header checked", "Fixed"),
            ("5 services to ask about (installation, leak, emergency, inspection, flat roof repair)", "No pages invented; listed as questions", "Needs client"),
            ("Template look: boxed cards, no signature, no motion", "Re-art-directed as \"Above the valley\" (Carhartt, Liquid Death, Ableton references): full-bleed valley hero, 6/12 roof-pitch motif, asymmetric sector collage, and the signature \"Layer by layer\" roof builder paired with real crew photos (reduced motion respected)", "Fixed"),
            ("Blog has no guide on snow load", "A new 1,154-word post on how much snow a roof can hold (FEMA sources)", "Fixed"),
        ],
        "questions": ["Which address should the site show: Salt Lake City or West Valley City (2331 S Redwood Rd, 84119)?", "Can we show 4.6 stars from 149 Google reviews?", "Do they do roof installation, leak repair, emergency repair, inspections and flat roof repair as separate services?", "OK to keep the Google Ads, Amazon pixel and GTM tags exactly as on the live site?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("West Valley City", "roofing-services-in-west-valley-city-utah/index.html"), ("Projects", "projects/index.html"), ("Refugee hub story", "sands-roofing-provides-a-new-roof-for-utah-ukrainian-refugee-hub/index.html"), ("Contact", "contact-us/index.html"), ("New blog post", "how-much-snow-can-a-roof-hold-utah/index.html")],
    },
    {
        "key": "stgeorgeconcreteleveling.com", "name": "St. George Concrete Leveling", "city": "St. George, UT", "title": "St. George Concrete Leveling Review",
        "report": "2026-10-19_stgeorgeconcreteleveling.com_report.html", "old": "old_sgcl", "new": "new_sgcl",
        "stats": [("64", "pages, same URLs (+1 post)"), ("1,054", "words in the new blog post"), ("1/16\"", "steps on the lip gauge"), ("0", "QA issues")],
        "fixes": [
            ("No Google profile; the name and domain read like a lead-generation site (reviewer)", "Built from the site's own contact details only; flagged: confirm who owns it", "Needs Angelo"),
            ("Unverified claims: \"thousands of satisfied customers\", \"family owned\", \"15+ years\", \"certified\", S260, warranty, and customer anecdotes written into pages", "Left out until confirmed; \"licensed and insured\" kept as stated", "Needs client"),
            ("The only photo is a stock foam-lifting composite", "Not used; original drawings (a lip gauge and a drawing per surface) plus one credited Snow Canyon landscape", "Fixed"),
            ("Home target \"concrete leveling st george\"; near-duplicate surface pages (reviewer)", "Home title, H1 and first sentence; surfaces presented as a clear picker so each page has its own job", "Fixed"),
            ("Mobile speed 95/100", "Plain HTML with inline drawings and one small photo; mobile header checked", "Kept"),
            ("No blog", "A new 1,054-word post on irrigation leaks under slabs (EPA WaterSense sources)", "Fixed"),
        ],
        "questions": ["Angelo: who owns this site, and is the phone answered by a local crew?", "Can the client back up the years, customer count, certification and warranty?", "Do they do foundation repair? (the report's biggest gap)", "Any real job photos?"],
        "pages": [("Home", "home/index.html"), ("Driveway leveling", "driveway-leveling/index.html"), ("Trip hazard removal", "trip-hazard-removal/index.html"), ("Foam injection", "polyurethane-foam-injection/index.html"), ("Ivins", "ivins/index.html"), ("Washington County", "washington-county/index.html"), ("Contact", "contact/index.html"), ("New blog post", "blog/irrigation-leaks-sunken-concrete/index.html")],
    },
    {
        "key": "m3industriesconcrete.com", "name": "M3 Industries", "city": "St. George, UT", "title": "M3 Industries Review",
        "report": "2026-10-19_m3industriesconcrete.com_report.html", "old": "old_m3", "new": "new_m3",
        "stats": [("38", "pages, same URLs (+1 post)"), ("1,058", "words in the new blog post"), ("16", "of the client's own job photos"), ("0", "QA issues")],
        "fixes": [
            ("Contact page and footers show the Wix template placeholder (500 Terry Francine St., San Francisco; 123-456-7890; info@mysite.com)", "Replaced everywhere with the client's real details: (435) 701-0081, m3industriesconcrete@gmail.com, 2570 South 3430 East, St. George", "Fixed"),
            ("No Google profile; the site shows a \"5.0 Google\" rating and \"25+ yrs\" vs \"over 20 years\"", "Rating not shown; \"20+ years\" used; flagged", "Needs client"),
            ("Many images look AI-generated (red-rock scenes with workers, logo-stamped cleaning photos, patio renders)", "Not used; only the client's phone-camera job photos", "Fixed"),
            ("Home target \"concrete coatings st george\"; no page names St. George; Wix booking pages show \"1 hr / 1 US dollar\"", "Home title, H1 and first sentence; service pages name St. George; booking junk removed", "Fixed"),
            ("Mobile speed 48/100", "Plain HTML instead of Wix, WebP photos; mobile header checked", "Improved, re-test"),
            ("Blog", "A new 1,058-word post on silica dust from cutting concrete (OSHA sources)", "Fixed"),
        ],
        "questions": ["Which is right: over 20 years or 25+ years?", "Is there a Google Business Profile? (none found; the site shows a 5.0 rating)", "Is Merrill the owner? Can we name him on the site?", "Do you do concrete lifting? (the report's biggest gap)"],
        "pages": [("Home", "home/index.html"), ("Driveways & patios", "concrete-driveway-patio/index.html"), ("Coatings & sealing", "concrete-coatings-st-george/index.html"), ("Foundations", "concrete-foundations/index.html"), ("Retaining walls", "retaining-walls/index.html"), ("FAQs", "faqs/index.html"), ("Contact", "contact-5/index.html"), ("New blog post", "post/concrete-silica-dust-diy/index.html")],
    },
    {
        "key": "thedisasterrepairteam.com", "name": "Disaster Repair Team", "city": "Lehi, UT", "title": "Disaster Repair Team Review",
        "report": "2026-10-19_thedisasterrepairteam.com_report.html", "old": "old_dr", "new": "new_dr",
        "stats": [("128", "pages, same URLs (+1 post)"), ("1,128", "words in the new blog post"), ("4", "damage types, each with its own colour"), ("0", "QA issues")],
        "fixes": [
            ("Home page target \"water damage restoration lehi\"; no page names Lehi (report)", "Home title, H1 and first sentence; every service page names Lehi in title, H1 and opening", "Fixed"),
            ("Most images are AI-generated (several file names end in \"-ai\")", "Not used; only the client's real job photos (fire ceiling, mold, water-bulged ceiling, wet carpet)", "Fixed"),
            ("Phone and address differ: site 385-287-6344 / 45 S 2920 W vs Google +1801-515-2257 / 441 W Main St Ste E", "The site's kept; Google's flagged", "Needs client"),
            ("Mobile speed 68/100; meta descriptions missing", "Plain HTML, small WebP photos; every page has a unique meta description; mobile header checked", "Improved, re-test"),
            ("Report cost/FAQ data is about foundation repair, not water damage (reviewer)", "Foundation-based cost and FAQ parts not applied; no new foundation pages", "Needs Angelo"),
            ("Blog", "A new 1,128-word post on frozen pipes in a Utah winter (Red Cross, EPA sources)", "Fixed"),
        ],
        "questions": ["Which phone and address should Google and the site share?", "Is the truck photo a real vehicle or a wrap mockup?", "Can you send real job photos to replace the AI images (smoke, insulation, foundation, commercial)?", "Angelo: water damage keyword data for the cost and FAQ parts?"],
        "pages": [("Home", "home/index.html"), ("Water damage", "water-damage-cleanup-restoration/index.html"), ("Fire damage", "fire-damage-cleanup-restoration/index.html"), ("Mold", "mold-remediation-restoration/index.html"), ("Fire damage Ogden", "landing-pages/fire-damage-ogden/index.html"), ("Areas", "landing-pages/index.html"), ("Request help", "request-help/index.html"), ("New blog post", "blog/frozen-pipes-utah-winter/index.html")],
    },
    {
        "key": "poly-lift.com", "name": "Poly-Lift", "city": "Logan, UT", "title": "Poly-Lift Review",
        "report": "2026-10-19_poly-lift.com_report.html", "old": "old_pl", "new": "new_pl",
        "stats": [("43", "pages, same URLs (+1 post)"), ("1,036", "words in the new blog post"), ("119", "job photos and pier diagrams"), ("0", "QA issues")],
        "fixes": [
            ("Home page target \"concrete lifting logan\"; foam specialty unclear (reviewer)", "Home title, H1 and first sentence; the polyurethane foam method is the headline and the interactive lift explains it", "Fixed"),
            ("Mobile speed 33/100, the slowest in the group", "Plain HTML, WebP photos at 150 KB or less, lazy-loading, no page builder scripts; mobile header checked", "Improved, re-test"),
            ("Only 2 pages name Logan", "Every service page names Logan in title, H1 and opening; city pages name their own town", "Fixed"),
            ("Address differs: \"715 W 1725 N\" (footer, Google) vs \"715 N 1725 W\" (contact page)", "The footer/Google form used everywhere", "Needs client"),
            ("Copy says \"harsh Pacific Northwest seasons\"; superlatives (\"the best on the market\")", "Changed to \"harsh winters\"; superlatives left out", "Needs client"),
            ("Stock photos (Ukraine, city landmarks, an insurance policy)", "Not used; job photos and the client's pier diagrams only", "Fixed"),
        ],
        "questions": ["Which address is right: 715 W 1725 N or 715 N 1725 W?", "OK to show the Google rating (4.6 from 14)?", "Do you do basement waterproofing? (the report's biggest gap)", "Fold the foundation repair cost article into a single cost page, as the reviewer suggests?"],
        "pages": [("Home", "home/index.html"), ("Concrete lifting", "concrete-leveling-and-lifting/index.html"), ("Push piers", "foundation-repair/push-piering/index.html"), ("Completed projects", "completed-projects/index.html"), ("Logan", "concrete-contractors-logan-ut/index.html"), ("FAQs", "faqs/index.html"), ("Contact", "contact/index.html"), ("New blog post", "uneven-sidewalk-trip-hazard/index.html")],
    },
    {
        "key": "stgeorgehomeservices.com", "name": "St. George Home Services", "city": "St. George, UT", "title": "St. George Home Services Review",
        "report": "2026-10-19_stgeorgehomeservices.com_report.html", "old": "old_sg", "new": "new_sg",
        "stats": [("198", "pages, same URLs (+ blog)"), ("1,171", "words in the new blog post"), ("153", "of the client's own job photos"), ("0", "QA issues")],
        "fixes": [
            ("Home page target \"ac repair st george\" (report; plumbing has more searches)", "Home title, H1 and first sentence name plumbing and AC repair in St. George; service pages name St. George in the H1", "Fixed"),
            ("\"Brand\" hero images (dusk streets, a duct render) and lighting \"illustrations\" look generated", "Not used: every photo on the new site is one of the client's own job photos, captioned like evidence", "Fixed"),
            ("Every fact on the site is footnoted to a document", "All 197 pages kept with their tables, footnotes and source lists; research PDFs, facts.json and llms.txt kept at the same URLs", "Kept"),
            ("Report notes: probably the wrong group (plumber / HVAC, not foundation)", "Foundation-repair cost and FAQ parts of the report not applied", "Needs Angelo"),
            ("Only 1 Google review", "Not shown; the site's own proof (license on request, Plain Terms, the owner on camera) leads instead", "Kept"),
            ("Blog", "A new 1,171-word post on water heater temperature (CPSC, OSHA, WHO sources) at /blog/", "Fixed"),
        ],
        "questions": ["Home keyword: plumbing (more searches) or AC repair (report)? The draft uses both.", "Can we show the Utah license number on the site, or keep 'on request' as now?", "Are the 'brand' street-scene hero images generated? (The draft leaves them out.)", "Is the RO giveaway (/win, closes Oct 27, 2026) still running at go-live?"],
        "pages": [("Home", "home/index.html"), ("Plain Terms", "plain-terms/index.html"), ("AC repair", "services/ac-repair/index.html"), ("Plumbing", "plumbing/index.html"), ("Ivins", "areas/ivins/index.html"), ("Hard water guide", "guides/hard-water-and-water-heaters/index.html"), ("About", "about/index.html"), ("New blog post", "blog/water-heater-temperature-setting/index.html")],
    },
    {
        "key": "cleartopsolutions.shop", "name": "ClearTop Solutions", "city": "St. George, UT", "title": "ClearTop Solutions Review",
        "report": "2026-10-17_cleartopsolutions.shop_report.html", "old": "old_ct", "new": "new_ct",
        "stats": [("32", "pages, same URLs (+ blog)"), ("1,292", "words in the new blog post"), ("6", "rooms in the blueprint house"), ("0", "QA issues")],
        "fixes": [
            ("Home page target \"water damage restoration st george\"; service pages don't name St. George in H1 (report)", "Home title, H1 and first sentence; every service page names St. George in title, H1 and opening", "Fixed"),
            ("Template claims with no evidence: \"98% Client Satisfaction\", \"100+ Projects\", a five-star row with no reviews, \"certified professionals\"", "Left out until the client confirms them", "Needs client"),
            ("The one photo on the site looks AI-generated", "Not used: services shown with an original blueprint drawing of a house; landscape photos openly licensed and credited, for atmosphere only", "Fixed"),
            ("Phone on the site (435) 288-1334 vs Google +1435-220-4296", "The site's number kept; Google's flagged", "Needs client"),
            ("The live home page's canonical points to /st-george/", "Kept as live (same canonicals rule); recommend a self-canonical home once approved", "Needs Angelo"),
            ("No blog", "A blog with a new post on storm-season home prep (Ready.gov, NWS, EPA sources)", "Fixed"),
        ],
        "questions": ["Which phone is the main one: (435) 288-1334 (site) or 435-220-4296 (Google)?", "Can you back up \"98% client satisfaction\" and \"100+ projects\"? Are your technicians certified (e.g. IICRC)?", "Can you send real photos of your own jobs, crew or vehicles?", "Angelo: OK to make the home page self-canonical instead of pointing to /st-george/?"],
        "pages": [("Home", "home/index.html"), ("All services", "services/index.html"), ("Kitchen water damage", "services/kitchen-water-damage-repair/index.html"), ("Basement flood cleanup", "services/basement-flood-cleanup/index.html"), ("St. George", "st-george/index.html"), ("Ivins", "ivins/index.html"), ("Contact", "contact/index.html"), ("New blog post", "blog/monsoon-season-st-george-home-prep/index.html")],
    },
    {
        "key": "jsprofinish.com", "name": "JS ProFinish", "city": "Clearfield, UT", "title": "JS ProFinish Review",
        "report": "2026-10-17_jsprofinish.com_report.html", "old": "old_js", "new": "new_js",
        "stats": [("27", "pages, same URLs (+ blog)"), ("1,150", "words in the new blog post"), ("61", "of the client's own job photos"), ("0", "QA issues")],
        "fixes": [
            ("The report's Google profile is a different business (\"Vista Concrete Construction\", Ogden, +1385-644-6281)", "The draft uses only the site's own facts (JS ProFinish, Clearfield, (385) 626-3514); the mismatch is flagged", "Needs Angelo"),
            ("The client photographs the same rooms at every stage, but the site hides it on one project page", "Signature 'same room' scrubber on the home page: drag a tape measure from drywall hung to finished", "Fixed"),
            ("Only 1 page names Ogden (report)", "Every service page names Ogden in title, H1 and first paragraph", "Fixed"),
            ("Builder markup split text (\"ZIP code s\", stray spaces before commas), bylines broken into headings", "Text re-joined; author and date line rebuilt", "Fixed"),
            ("No blog", "A blog with a new 1,150-word post on basement egress windows (Utah city checklist source)", "Fixed"),
            ("Mobile speed 99/100", "Plain HTML, WebP photos at 150 KB or less, lazy-loading; mobile header checked; keep it above 90", "Keep, re-test"),
        ],
        "questions": ["Angelo: is jsprofinish.com really the site for \"Vista Concrete Construction\"? The site, phone and address all say JS ProFinish in Clearfield.", "OK to show the rating as the site does (4.8 from 18 Google reviews, Sept 2026)?", "OK to put Pablo's name as the author of the new blog post?", "Do you do French drains, foundation repair or water damage? (the report's biggest keywords; only build pages if yes)"],
        "pages": [("Home", "home/index.html"), ("Clinton project", "projects/clinton-basement-finish/index.html"), ("Drywall", "services/drywall/index.html"), ("Services", "services/index.html"), ("Gallery", "gallery/index.html"), ("Cost guide", "basement-finishing-cost/index.html"), ("Ogden", "cities/ogden/index.html"), ("New blog post", "blog/basement-egress-window-requirements-utah/index.html")],
    },
    {
        "key": "armour-crete.com", "name": "Armour Crete", "city": "St. George, UT", "title": "Armour Crete Review",
        "report": "2026-10-17_armour-crete.com_report.html", "old": "old_ac", "new": "new_ac",
        "stats": [("17", "pages, same URLs (+ blog)"), ("1,035", "words in the new blog post"), ("4", "drawn slab states"), ("0", "QA issues")],
        "fixes": [
            ("The site has no photos at all (logo only)", "Original drawings of every finish and of why concrete fails; Snow Canyon landscapes (openly licensed, credited) for atmosphere only", "Fixed"),
            ("Home page target \"concrete sealing st george\" (report)", "Title, H1 and first sentence; every service page names St. George in title, H1 and opening", "Fixed"),
            ("Three phone numbers: Dylan 435-994-5235, Zac 435-224-6987 (site), +1435-938-9271 (Google)", "The site's two numbers kept with names; Google's number flagged", "Needs client"),
            ("Name: \"Armour Crete\" on the site vs \"Armored Concrete Systems\" on Google", "The draft uses the site's name; Google profile should match", "Needs client"),
            ("No blog", "A blog with a new 1,035-word post on efflorescence (NRC source)", "Fixed"),
            ("Mobile speed 77/100", "Plain HTML, small WebP photos, lazy-loading; mobile header checked", "Improved, re-test"),
        ],
        "questions": ["Which name should the business use everywhere: Armour Crete or Armored Concrete Systems?", "Which phone is the main one (Dylan 435-994-5235, Zac 435-224-6987, or Google's 435-938-9271)?", "Can you send photos of your own finished jobs (driveways, pool decks, wet-look)?", "OK to show the Google rating (5.0 from 3)?", "Do you also do concrete lifting? (the report's biggest gap)"],
        "pages": [("Home", "home/index.html"), ("Driveway sealing", "driveway-sealing/index.html"), ("Pool decks", "pool-deck-sealing/index.html"), ("Wet-look", "wet-look-concrete-sealing/index.html"), ("Products", "products/index.html"), ("Hurricane", "concrete-sealing-hurricane-ut/index.html"), ("For contractors", "contractors/index.html"), ("New blog post", "blog/efflorescence-white-stains-concrete-st-george/index.html")],
    },
    {
        "key": "swiftrestoreutah.com", "name": "Swift Restoration and Remodeling", "city": "Ogden, UT", "title": "Swift Restoration and Remodeling Review",
        "report": "2026-10-17_swiftrestoreutah.com_report.html", "old": "old_sw", "new": "new_sw",
        "stats": [("267", "pages, same URLs"), ("1,057", "words in the new blog post"), ("6", "stages in the recovery timeline"), ("0", "QA issues")],
        "fixes": [
            ("Home page target \"water damage restoration ogden\" (report); 28 of 266 pages name Ogden", "Home title, H1 and first sentence; every service page names Ogden in title, H1 and opening paragraph", "Fixed"),
            ("Mobile speed 52/100", "Plain HTML, WebP photos at 150 KB or less, lazy-loading; mobile header checked", "Improved, re-test"),
            ("Links on the live site point to 16 URLs that redirect, and 2 that are 404", "All internal links point straight to the right page; the list is in the notes", "Fixed"),
            ("Builder markup split sentences and headings around links (\"Water Dam / ge\")", "Text re-joined; headings repaired", "Fixed"),
            ("Two phone numbers: (385) 412-8633 (Google, contact page) and (385) 402-8536 (home page button)", "The draft uses (385) 412-8633 everywhere", "Needs client"),
            ("\"BBB accredited\" on city pages; local-guide pages with errors (Waterfall Canyon \"just outside of Park City\")", "BBB claim left out until confirmed; the Park City error removed; the other guide pages kept as written and flagged", "Needs client"),
        ],
        "questions": ["Which phone is right for the website: (385) 412-8633 or (385) 402-8536?", "OK to show the Google rating (4.6 from 179)?", "Is Swift BBB accredited, and IICRC certified (please confirm the certification)?", "Should the free carpet-cleaning gift and consumer report pages stay live?", "Can you send more finished-job photos at full size?"],
        "pages": [("Home", "home/index.html"), ("Water damage restoration", "services/water-damage-restoration/index.html"), ("Flooded basement cleanup", "services/flooded-basement-cleanup/index.html"), ("Bathroom remodeling", "services/bathroom-remodeling/index.html"), ("Case studies", "case-studies/index.html"), ("Layton", "service-areas/water-damage-layton-ut/index.html"), ("Contact", "contact/index.html"), ("New blog post", "restoration-tips/home-fire-safety-checklist-northern-utah-winters/index.html")],
    },
    {
        "key": "exceptional-roofing.com", "name": "Exceptional Roofing", "city": "Salt Lake City, UT", "title": "Exceptional Roofing Review",
        "report": "2026-10-16_exceptional-roofing.com_report.html", "old": "old_er", "new": "new_er",
        "stats": [("44", "pages, same URLs"), ("1,010", "words in the new blog post"), ("5", "drawn material swatches"), ("0", "QA issues")],
        "fixes": [
            ("Only 1 of 47 pages names Salt Lake City (report)", "Home targets \"roofing company salt lake city\" in title, H1 and first sentence; every service page names Salt Lake City in title, H1 and opening paragraph", "Fixed"),
            ("Internal links point to a broken WordPress path (/wb_exceptional-roofing.com/...)", "All links point to the real URLs", "Fixed"),
            ("WordPress leftovers live: \"Hello world!\", \"Sample Page\", empty blog, category and author archives", "Not rebuilt; listed for redirects. The blog now has a real post", "Needs Angelo"),
            ("/commercial/ and /commercial-roofing/ are the same page", "/commercial/ kept, canonical to /commercial-roofing/", "Fixed"),
            ("No address on Google (service-area business)", "No address shown; areas listed in words", "Fixed"),
            ("Mobile speed 97/100 already", "Plain HTML, WebP photos at 150 KB or less, lazy-loading; mobile header checked", "Keep, re-test"),
        ],
        "questions": ["Which phone should be the main one on Google: the estimator line 801-680-6499 (current) or production 801-809-8535?", "OK to show the Google rating (4.8 from 16)?", "OK to mention the Leonardo Museum project by name on the home page?", "Do you want a roof installation page (home page names it, no page yet)?", "More project photos with the town for each?"],
        "pages": [("Home", "home/index.html"), ("Roof repair", "roof-repair/index.html"), ("Metal roofing", "metal-roofing/index.html"), ("Services", "services/index.html"), ("Gallery", "gallery/index.html"), ("Sandy", "sandy/index.html"), ("Contact", "contact/index.html"), ("New blog post", "ice-dams-utah-roofs/index.html")],
    },
    {
        "key": "sfrutah.com", "name": "Superior Foundation Repair Utah", "city": "Salt Lake City & St. George, UT", "title": "Superior Foundation Repair Utah Review",
        "report": "2026-10-17_sfrutah.com_report.html", "old": "old_sf", "new": "new_sf",
        "stats": [("35", "URLs rebuilt (+ new post)"), ("1,057", "words in the new blog post"), ("4", "real Google reviews quoted"), ("0", "QA issues")],
        "fixes": [
            ("The live site is broken today: the home page shows a template \"404 Page Not Found\" and the blog URLs return 404", "Rebuilt from the Wayback captures (Mar–Jul 2026), same URLs; ready to replace the broken site", "Fixed / needs Angelo"),
            ("Home page target \"foundation repair salt lake city\" (report)", "Title, H1 and first sentence on the home page; service pages name Salt Lake City in title, H1 and opening paragraph", "Fixed"),
            ("Office labels swapped on the contact page, a third (Midvale) address, phone numbers swapped on service pages", "One consistent pair: Salt Lake City 801-970-1473, St. George 435-668-0734, as on the home page", "Needs client"),
            ("\"Over 15 years\" vs founded in 2019; \"Utah's premier/best/most trusted\", \"certified\", \"strong guarantee\"", "Left out until confirmed; the draft says founded 2019, Matt has over a decade of experience", "Needs client"),
            ("Unsigned testimonials (\"John and Mary\", \"David\") and stock photos on city pages", "Replaced with 4 real Google reviews (by name) and the client's own job photos; stock photos dropped", "Fixed"),
            ("A blog post meta description advertises \"Quick Quality Plumbing\"; a duplicate post (-2)", "New descriptions; the duplicate canonicals to the original", "Fixed"),
        ],
        "questions": ["Is the site being rebuilt on purpose right now (the live home page is a template 404)?", "Which addresses are current: SLC 774 East 2100 South Ste 448 and St. George 1792 N Serenity Dr? What is 1004 Tuscany View Rd, Midvale?", "How many years in business should the site claim (founded 2019 vs \"15+ years\")?", "OK to show the Google rating (5.0 from 17)?", "Can you send the 7 newer blog posts that have no archive copy, and more job photos?"],
        "pages": [("Home", "home/index.html"), ("Helical piers", "helical_foundation_repair/index.html"), ("Case study", "all_case_studies/index.html"), ("Services", "services/index.html"), ("Coverage areas", "coverage_areas/index.html"), ("St. George", "st_george/index.html"), ("Contact", "contact/index.html"), ("New blog post", "blog/post/expansive-clay-soil-st-george-foundations/index.html")],
    },
    {
        "key": "dryhouse.com", "name": "Rocky Mountain Waterproofing", "city": "West Jordan, UT", "title": "Rocky Mountain Waterproofing Review",
        "report": "2026-10-17_dryhouse.com_report.html", "old": "old_dh", "new": "new_dh",
        "stats": [("47", "live URLs kept (+ new post)"), ("1,297", "words in the new blog post"), ("4", "original technical drawings"), ("0", "QA issues")],
        "fixes": [
            ("Home page target \"basement waterproofing west jordan\" (report); no page named West Jordan", "Title, H1 and first sentence on the home page; every service page names West Jordan in title, H1 and opening paragraph", "Fixed"),
            ("Every page had the same meta description (\"Rocky Mountain Waterproofing\") and no canonical tags", "Unique descriptions on all pages; self canonicals; blog listing duplicates point to /blog", "Fixed"),
            ("Live pages left as template filler: TremProof 250 GC (lorem ipsum), Other Services (menu demo), Horizontal Services (\"Description of...\") and 3 one-line leak pages", "Rebuilt from the client's own text elsewhere on the site; TremProof 250 GC kept short until the client sends product copy", "Fixed / needs client"),
            ("Mobile speed 56/100; the home page scrolls sideways on phones (395 px on a 390 px screen)", "Plain HTML, WebP photos at 152 KB or less, lazy-loading; no sideways scrolling; mobile header checked", "Improved, re-test"),
            ("Analytics tag is UA-138052846-1 (Universal Analytics stopped recording in 2023)", "Kept as is in site/; set up GA4 before go-live", "Needs Angelo"),
            ("Home says \"Licensed Pesticide Company for Termite Pre-Treatment\" but the termite page says the service has ended", "Termite and window well pages say \"no longer offered\"; the licensing claim is left off the home page", "Needs client"),
            ("Unsourced claims: \"85% of building issues\", \"40% of energy loss\", \"200 mph\", \"best warranties\", \"leading brand\", \"one of the first in the nation\"", "Left out until the client confirms them", "Needs client"),
        ],
        "questions": ["Is dryhouse.com the domain you want to keep for Rocky Mountain Waterproofing?", "OK to show the Google rating (4.8 from 50)?", "Is the company still a licensed pesticide company, or should termite references go entirely?", "Can you send product copy for TremProof 250 GC and the horizontal services (suspended slabs, post-tension slabs, decks)?", "Are Chris, Jenn, Tyler and Sam still the owners, and is the team photo set current?", "Can you send more job photos (with the city of each job)?"],
        "pages": [("Home", "home/index.html"), ("Below grade", "services/belowgrade/index.html"), ("Waterproofing", "services/belowgrade/waterproofing/index.html"), ("Damp proofing", "services/belowgrade/damp-proof/index.html"), ("Leak repair", "services/leak-repair/index.html"), ("History", "about/rmwp-history/index.html"), ("Bid request", "estimate/index.html"), ("New blog post", "blog/before-you-backfill-foundation-checklist/index.html")],
    },
    {
        "key": "davenportfoundationrepair.com", "name": "Davenport Foundation Repair", "city": "West Jordan, UT", "title": "Davenport Foundation Repair Review",
        "report": "2026-10-17_davenportfoundationrepair.com_report.html", "old": "old_dv", "new": "new_dv",
        "stats": [("514", "pages, same URLs"), ("1,063", "words in the new blog post"), ("36", "of their own job photos"), ("0", "QA issues")],
        "fixes": [
            ("Home page target \"foundation repair west jordan\" (report); no page named West Jordan", "Title, H1 and first sentence on the home page; every service page names West Jordan in title, H1 and opening paragraph", "Fixed"),
            ("Mobile speed 40/100; the home page scrolls sideways on phones (421 px on a 390 px screen)", "Plain HTML, WebP photos at 160 KB or less, lazy-loading; no sideways scrolling; mobile header checked", "Improved, re-test"),
            ("Big product photos are Basement Systems / Supportworks network library images, not Davenport jobs", "Replaced with 36 of the client's own job photos captioned by town, plus original cross-section drawings of each repair", "Fixed"),
            ("\"100% Customer Satisfaction\", \"best\", \"largest network\", \"lifetime sealant\", \"600 employees\"", "Left out until the client confirms them", "Needs client"),
            ("Two phone numbers (1-801-569-2302 in the header, 1-801-429-9989 on Google and the location block)", "Kept as on the site; client to confirm the main number", "Needs client"),
            ("Hundreds of CMS item pages (single reviews, photos, before/after items) outside the sitemap", "514 pages rebuilt; the rest listed in a redirect CSV for Angelo", "Needs Angelo"),
        ],
        "questions": ["Which phone number should be the main one: 1-801-569-2302 or 1-801-429-9989?", "OK to show the Google rating (4.8 from 1,473)?", "Are the 2017 awards and the team list current?", "Can you send more of your own job photos at full resolution?", "Should the CMS keep serving single review and photo pages, or should they redirect to their listing pages?"],
        "pages": [("Home", "home/index.html"), ("Foundation repair", "foundation-repair.html"), ("Bowing walls", "foundation-repair/foundation-problems/bowing-walls.html"), ("Basement waterproofing", "basement-waterproofing.html"), ("Concrete leveling", "concrete-leveling.html"), ("Service area", "service-area.html"), ("Blog", "about-us/our-blog.html"), ("New blog post", "about-us/our-blog/collapsible-soils-in-utah-why-homes-settle.html")],
    },
    {
        "key": "saltcityroofers.com", "name": "Salt City Roofers", "city": "Salt Lake City, UT", "title": "Salt City Roofers Review",
        "report": "2026-10-17_saltcityroofers.com_report.html", "old": "old_scr", "new": "new_scr",
        "stats": [("36", "pages, same URLs"), ("1,096", "words in the new blog post"), ("23", "real job photos, 0 stock"), ("0", "QA issues")],
        "fixes": [
            ("Design read as a plain template (review, 21 Oct)", "v2 \"The Homeowner's Edition\" (Kinfolk, Dwell, Heath Ceramics): editorial hero with real job photos, a cinematic Avenues panorama, a pinned four-chapter photo story (Educate, Plan, Execute, Wrap it up), magazine case-file spreads, letters, and full-bleed photo heroes on inner pages", "Fixed"),
            ("Home page target \"roofing company salt lake city\" (report); only 2 pages named Salt Lake City; meta descriptions missing", "Title, H1 and first sentence on the home page; service pages name Salt Lake City; a unique meta description on every page", "Fixed"),
            ("Stock photos (Envato \"2UEEZLK\", \"7K3R6FE\", \"NVY3VZW\" files, a mother and baby, a pen on a warranty form) used as if they were jobs", "All stock removed; the site uses the client's own photos from the Avenues, Draper and Park City jobs", "Fixed"),
            ("\"Utah's #1 Roofing Contractor\", \"most complete and trusted\", \"finest\", \"the best roof\", certification and supplier-endorsement claims", "Left out until the client confirms them (certifications date from 2017)", "Needs client"),
            ("2017 Q&A answer: \"the price for an average home in Utah is around $10,000\"", "Removed (old price); the cost question can come back with current numbers", "Needs client"),
            ("21 WordPress archive pages (categories, tags, authors, slider items) with no content of their own", "Not rebuilt; Angelo to redirect them to /roofing-blog/", "Needs Angelo"),
            ("No phone or address on a Google profile; no profile found", "Phone and email from the client's own site; no address shown (service-area business)", "Needs client"),
        ],
        "questions": ["Is Salt City Roofers still taking work? (last blog post April 2022, footer says 2021, no Google profile found)", "Which phone number should the site show, and do you want an address on it?", "Are the CertainTeed ShingleMaster and other certifications still current?", "Do you do roof repair, metal roofing, gutters, inspections and commercial work as services? (report keywords)", "Can you send a high-resolution logo? (the current one is 196 px wide)"],
        "pages": [("Home", "home/index.html"), ("Asphalt shingle systems", "asphalt-shingle-systems/index.html"), ("Services", "services/index.html"), ("Roofing Q&A", "roofing-q-a/index.html"), ("Blog", "roofing-blog/index.html"), ("Draper project post", "blog/2022/02/16/exterior-remodel-draper-utah/index.html"), ("New blog post", "blog/2026/10/18/tear-off-or-roof-over-utah-two-layer-rule/index.html"), ("Contact", "contact/index.html")],
    },
    {
        "key": "utahroofingpros.com", "name": "Utah Roofing Pros", "city": "Cottonwood Heights, UT", "title": "Utah Roofing Pros Review",
        "report": "2026-10-17_utahroofingpros.com_report.html", "old": "old_urp", "new": "new_urp",
        "stats": [("79", "pages, same URLs"), ("1,400", "words in the new blog post"), ("28", "real job photos, 0 AI"), ("0", "QA issues")],
        "fixes": [
            ("Every city page and several service pages used AI-generated photos (the 1376x768 \"{city}_repair / _local / _commercial\" set, plus Higgsfield and mock-up images)", "All AI images removed; the site uses 28 of the client's own job photos and an original map of their 52 service cities", "Fixed"),
            ("Home page target \"roofing company cottonwood heights\" (report); only 1 page named Cottonwood Heights", "Title, H1 and first sentence on the home page; every service page names Cottonwood Heights in its title, H1 and opening paragraph", "Fixed"),
            ("\"GAF Certified\", \"Owens Corning Preferred\", \"Up to 50-Year\" and \"Lifetime\" warranty, \"85+ verified 5-star reviews\", \"24/7\", \"over a decade of combined experience\"", "Left out until the client confirms each one", "Needs client"),
            ("Financing \"12 months no payments, no interest\" and \"no upfront costs\"", "Page kept with \"ask about current options\"; the exact terms come back once confirmed", "Needs client"),
            ("No blog", "New /blog with a 1,400-word guide to attic ventilation (IRC R806 ratios with a worked example, ice dams), linked to inspection, replacement and swamp cooler pages", "Fixed"),
            ("Mobile speed 75/100", "Plain HTML, WebP photos at 150 KB or less, lazy-loaded below the fold; GTM and GA4 tags kept", "Improved, re-test"),
        ],
        "questions": ["Can we show the GAF Certified and Owens Corning Preferred badges? (Need proof of current status.)", "OK to show 4.9 stars from 104 Google reviews?", "What are the current financing terms, and the warranty lengths you offer?", "Do you do roof leak repair as its own service? (report keyword)", "OK to name Saint Ann's School (South Salt Lake, 2021) as a past job?"],
        "pages": [("Home", "home/index.html"), ("Roof repair", "services/residential-roofing/roof-repair/index.html"), ("Service areas map", "service-areas/index.html"), ("Sandy", "service-areas/sandy/index.html"), ("Commercial", "services/commercial-roofing/index.html"), ("Projects", "our-roofing-projects/index.html"), ("New blog post", "blog/attic-ventilation-utah-homes/index.html"), ("Contact", "contact-us/index.html")],
    },
    {
        "key": "xperienceroofing.com", "name": "Xperience Roofing", "city": "Midvale, UT", "title": "Xperience Roofing Review",
        "report": "2026-10-17_xperienceroofing.com_report.html", "old": "old_xperience", "new": "new_xperience",
        "stats": [("37", "pages, same URLs"), ("1,080", "words in the new journal post"), ("0", "stock photos"), ("0", "QA issues")],
        "fixes": [
            ("Design read as type and drawings only (review, 21 Oct)", "v2 \"Built for the Wasatch\": full-height Lone Peak winter hero with a line-by-line headline reveal, a Wasatch panorama band, a photo CTA; openly licensed landscapes credited as atmosphere (not jobs); the Collection selector kept as the signature", "Fixed"),
            ("Every photo on the site is stock (Freepik/Unsplash, including European houses and a Dutch scaffolding sign), captioned as local jobs: \"Standing seam metal - Draper, UT\"", "All stock removed; the design runs on type and original profile drawings of each system until the client sends real job photos", "Fixed, ask for photos"),
            ("Home page target \"roofing company midvale\" (report)", "Title, H1 and first sentence; every service page names Midvale", "Fixed"),
            ("Lifespan and warranty-length figures in the system specs (25-50 years, 50-70 years, lifetime)", "Left out until the client confirms the products", "Needs client"),
            ("\"4.9 average rating\", \"since 2019\", \"licensed & insured\" shown without detail", "Kept as the client states them; rating matches Google (4.9 from 365)", "Needs client OK"),
            ("No blog", "New /blog with a 1,080-word guide to reading a roofing estimate, with Utah license facts", "Fixed"),
            ("Mobile speed 98/100 (good)", "Plain HTML and inline SVG drawings, no photos to load; GA4 tag kept", "Kept fast"),
        ],
        "questions": ["Can you send real job photos, with the city each was in?", "OK to show 4.9 stars from 365 Google reviews near the top?", "Which product lines do you install for each system (for lifespans and warranties)?", "Do you offer roof leak repair, emergency repair, installation, gutters? (report keywords)"],
        "pages": [("Home", "home/index.html"), ("The Collection", "systems/index.html"), ("The Classic", "systems/the-classic/index.html"), ("Roof repair", "services/roof-repair/index.html"), ("Material World", "materials/index.html"), ("Midvale", "locations/midvale-ut/index.html"), ("New journal post", "blog/how-to-read-a-roofing-estimate/index.html"), ("Contact", "contact/index.html")],
    },
    {
        "key": "utahoneroofing.com", "name": "Utah One Roofing", "city": "Salt Lake City, UT", "title": "Utah One Roofing Review",
        "report": "2026-10-17_utahoneroofing.com_report.html", "old": "old_utahone", "new": "new_utahone",
        "stats": [("12", "pages (the 9 real ones plus blog and 404)"), ("1,067", "words in the new blog post"), ("18", "of the client's own photos"), ("0", "QA issues")],
        "fixes": [
            ("No page names Salt Lake City in titles or H1s; no meta descriptions (report)", "Home targets \"roofing company Salt Lake City\"; every service page has Salt Lake City in the title, H1 and opening; every page has a meta description", "Fixed"),
            ("Theme demo content live: lorem ipsum, a fake team (\"Robert C. Simmons, CEO Roof Inc.\"), placeholder testimonials, \"32k partners\"", "Removed", "Fixed"),
            ("9 demo blog posts about Colorado and the Twin Cities, plus category, tag and author archives", "Not rebuilt; 301s or 410s recommended", "Needs Angelo"),
            ("Most images are theme stock (workers in hard hats, headshots)", "Only the client's own 18 job photos used", "Fixed"),
            ("Claims to confirm: \"top-rated\", \"more than 10 years\", \"24/7\" and \"24-hour response\", price ranges, financing terms", "Left out until confirmed", "Needs client"),
            ("Address on the site is 5546 W Heathrow Cir; the Google profile says 5536", "Site's address used; flagged", "Needs client"),
            ("Services page links to /green-roofing/, which returns 404", "Link now goes to a new 1,067-word post on green roofs in Utah", "Fixed"),
            ("Elementor theme with sliders and stock images", "Plain HTML, one CSS file, WebP photos", "Fixed, re-test after go-live"),
        ],
        "questions": ["Which address is right: 5546 or 5536 W Heathrow Cir?", "OK to say \"disabled veteran-owned\" on the site, as the old site did?", "Do you offer 24/7 or 24-hour emergency response?", "Years in business and license number?", "Is financing (12 months same-as-cash) current?", "OK to show 5 stars from 14 Google reviews?", "Do you do roof installation, replacement and inspections as separate services (report keywords)?"],
        "pages": [("Home", "home/index.html"), ("Residential roofing", "residential-roofing/index.html"), ("Commercial roofing", "commercial-roofing/index.html"), ("Roof repair", "roof-repair/index.html"), ("Services", "services/index.html"), ("New blog post", "blog/green-roofs-in-utah/index.html"), ("About", "about-us/index.html"), ("Contact", "contact/index.html")],
    },
    {
        "key": "roofrepairsaltlakecity.com", "name": "Roof Repair Salt Lake City", "city": "Salt Lake City, UT", "title": "Roof Repair SLC Review",
        "report": "2026-10-17_roofrepairsaltlakecity.com_report.html", "old": "old_roofrepairslc", "new": "new_roofrepairslc",
        "stats": [("22", "pages, same URLs"), ("1,040", "words in the new article"), ("0", "stock or AI images"), ("0", "QA issues")],
        "fixes": [
            ("No page names Salt Lake City in its title or H1 (report)", "Home targets \"roof repair Salt Lake City\"; every service page has Salt Lake City in the title, H1 and first paragraph", "Fixed"),
            ("Phone on the site (385) 355-4849 differs from the Google profile (+1385-213-7368); address \"1760 w 2100 s\" vs \"1760 2100 S\"", "The site's own phone and address used, exactly as written; flagged", "Needs client"),
            ("Theme demo pages are live: /clients/wpml/, /clients/jquery/, /clients/envato/, /clients/microlancer/ and a \"John Doe\" testimonial", "Not rebuilt; 301s recommended", "Needs Angelo"),
            ("The only images are theme stock banners and manufacturer logos", "Design built from type and original drawings: a figure of where roofs leak, material swatches and a ballast section", "Fixed, ask for job photos"),
            ("Unsupported claims: \"best\", \"leader\", \"100 percent satisfaction\", a Wall Street Journal statistic, \"62% file complaints\", 24/7, guarantees", "Left out", "Fixed"),
            ("/articles/ page shows \"Nothing Found\"", "Article index with a new 1,040-word post on ballasted roofs, a service the site lists with no page", "Fixed"),
            ("Several near-duplicate pages (commercial roofing / commercial roofing systems; TPO membrane / commercial TPO)", "Each given its own title and opening; merging recommended", "Needs Angelo"),
            ("Mobile speed 61/100 (theme, sliders, jQuery)", "Plain HTML, one CSS file, no image weight beyond one share card", "Fixed, re-test after go-live"),
        ],
        "questions": ["Which phone is right: (385) 355-4849 (site) or 385-213-7368 (Google)?", "Is the address 1760 W 2100 S, Salt Lake City, UT 84119?", "Can you send real job photos, with the city each was in?", "Do you offer 24/7 emergency service?", "Which manufacturer certifications are current?", "OK to show your Google rating? (4 stars from 1 review today)"],
        "pages": [("Home", "home/index.html"), ("Roof repair", "utah-roof-repair/index.html"), ("Metal roofing", "utah-metal-roofing/index.html"), ("Flat roof repair", "flat-roof-repair/index.html"), ("Commercial roofing", "commercial-roofing/index.html"), ("New article", "articles/what-is-a-ballasted-roof/index.html"), ("About", "about-us/index.html"), ("Contact", "contact-us/index.html")],
    },
    {
        "key": "skybridgeroofings.com", "name": "Sky Bridge Roofing", "city": "South Salt Lake, UT", "title": "Sky Bridge Roofing Review",
        "report": "2026-10-17_skybridgeroofings.com_report.html", "old": "old_skybridge", "new": "new_skybridge",
        "stats": [("16", "pages, same Shopify URLs"), ("1,183", "words in the new blog post"), ("3", "of their own videos used"), ("0", "QA issues")],
        "fixes": [
            ("No page names South Salt Lake (report: 0 of 16)", "Home targets \"roofing company South Salt Lake\"; every service page has South Salt Lake in the title, H1 and first paragraph", "Fixed"),
            ("No meta descriptions; titles are just \"ROOF REPAIR – Sky Bridge Roofing\"", "Every page has its own title and meta description", "Fixed"),
            ("Home page reviews (Alex M., Priya K., Diego R.) read like theme placeholders", "Left off; real Google reviews can go in once the client confirms them", "Needs client"),
            ("Unverified numbers and promises: 2-hour emergency response, triple-seal guarantee, 1M+ sq ft, decade+, zero recurrence, lifespans, warranty names, cooling savings up to 30-40%", "Not used; listed in the notes for the client to confirm", "Needs client"),
            ("Banner images have text baked in; several photos are Pinterest-size stock", "Replaced with the client's own photos, drone video and office video", "Fixed"),
            ("Mobile page is 476 px wide on a 390 px phone (sideways scrolling)", "No sideways scrolling at 390 px or 1440 px", "Fixed"),
            ("Spanish template page with placeholder text (/pages/plantilla-servicios) and an empty /collections/frontpage are live", "Not rebuilt; 301s recommended", "Needs Angelo"),
            ("Email on the site uses skybridgeroofing.com but the website is skybridgeroofings.com", "Email copied exactly as the site shows it; flagged", "Needs client"),
            ("Mobile speed 76/100 (Shopify theme, large images and video)", "Plain HTML, one CSS file, WebP photos, compressed video loops (3.6 MB total)", "Fixed, re-test after go-live"),
        ],
        "questions": ["Is the address 3007 S W Temple St, South Salt Lake, UT 84115 correct to show on the site?", "How should the phone show: (435) 659-4915 or +1435-659-4915?",
                      "Which email is right: cesar@skybridgeroofing.com (on the site) or an address at skybridgeroofings.com?", "OK to show 5 stars from 25 Google reviews? Can we use real reviews?",
                      "Do you do roof installation on new builds, storm damage repair and insurance claims?", "Which of the site's warranty and speed claims are real (1-year workmanship, 2-hour emergency response, triple-seal guarantee)?",
                      "Years in business, licenses and certifications?", "More job photos, with the city each job was in? Where was the drone-video metal roof?"],
        "pages": [("Home", "home/index.html"), ("Roof repair", "pages/roof-repair/index.html"), ("Roof replacement", "pages/roof-raplecement/index.html"),
                  ("Metal roofing", "pages/metal-roofing/index.html"), ("TPO", "pages/tpo/index.html"), ("New blog post", "blogs/noticias/do-you-need-a-permit-to-replace-a-roof-in-south-salt-lake/index.html"),
                  ("About", "pages/about-us/index.html"), ("Contact", "pages/contact/index.html")],
    },
    {
        "key": "oakleyroofingslc.com", "name": "Oakley Roofing", "city": "Salt Lake City, UT", "title": "Oakley Roofing Review",
        "report": "2026-10-17_oakleyroofingslc.com_report.html", "old": "old_oakley", "new": "new_oakley",
        "stats": [("16", "pages rebuilt, same URLs"), ("1,252", "words in the new blog post"), ("7", "real job photos (stock dropped)"), ("0", "QA issues")],
        "fixes": [
            ("No page names Salt Lake City; titles are \"Page - Oakley Roofing\" (report)", "Home targets \"roofing company Salt Lake City\"; every service page has Salt Lake City in the title, H1 and first paragraph", "Fixed"),
            ("Most images are Depositphotos stock, Tesla marketing renders and a stock appliance photo", "Removed; only the 7 photos of real Oakley jobs are used", "Fixed, ask for more photos"),
            ("Solar pages show other phone numbers ((801) 949-0929, (801) 683-6085) and sales@oakleysolarlroofing.com (typo in the domain)", "Main office number used everywhere", "Needs client"),
            ("Tesla tile hail rating listed as \"Class 3 ... Best Hail Rating\" (Class 4 is the top FM 4473 class)", "Hail line not reused", "Fixed"),
            ("Service area contradicts itself: \"Northern Utah\" vs \"Utah, Nevada, Colorado & Wyoming\"", "Salt Lake City and Utah only until confirmed", "Needs client"),
            ("Superlatives and promises: \"#1 roofer in Utah\", \"best roofing company\", \"guarantee your roof will withstand any type of weather\", $20,000 solar savings", "Not used", "Fixed"),
            ("Partner logos (GAF Master Select, Owens Corning Preferred, Johns Manville, TAMKO, Versico, NRCA) with no detail", "Left off until each is confirmed", "Needs client"),
            ("WordPress leftovers indexed: hello-world, category/uncategorized, author/supportthemesupport-net", "Kept as noindex pages pointing to the new blog; 301s recommended", "Needs Angelo"),
            ("Solar pages have no meta description; meta descriptions elsewhere are generic", "Every page has its own title and meta description", "Fixed"),
            ("Mobile speed 63/100 (Elementor, GoDaddy, full-size images)", "Plain HTML, one CSS file, WebP photos, lazy-loaded; GA4 tag kept", "Fixed, re-test after go-live"),
        ],
        "questions": ["OK to show 4.6 stars / 14 Google reviews?", "Which phone and email for solar: (801) 651-1000, (801) 949-0929 or (801) 683-6085?",
                      "Where do you work: Northern Utah, or Utah, Nevada, Colorado and Wyoming?", "Which certifications are current: GAF Master Select, Owens Corning Preferred, others?",
                      "Do you install metal roofs and do roof replacements and inspections as separate services? (pages for the report's keywords)",
                      "Are the 7 photos all your jobs? Can you send more?", "Do you still install the Powerwall, and which model?"],
        "pages": [("Home", "home/index.html"), ("Commercial", "commercial/index.html"), ("Commercial installation", "commercial-roofing-installation/index.html"),
                  ("Roof repair", "residential-roofing-repairs/index.html"), ("Solar", "solar/index.html"), ("New blog post", "blog/tpo-vs-epdm-vs-pvc/index.html"),
                  ("About", "about-us/index.html"), ("Contact", "contact-us/index.html")],
    },
    {
        "key": "mandmgutters.com", "name": "M&M Gutters & Exteriors", "city": "Salt Lake City, UT", "title": "M&M Gutters Review",
        "report": "2026-10-17_mandmgutters.com_report.html", "old": "old_mandm", "new": "new_mandm",
        "stats": [("183", "URLs rebuilt, same addresses"), ("1,109", "words in the new blog post"), ("108", "real job photos kept"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned: full-width photo hero, an interactive section drawing of the water's path from roof to ground, material cards, a large project gallery, a winter band, and an editorial blog layout with contents", "Fixed"),
            ("36 of the client's photos have page-builder frames baked in (black borders, orange and blue corner blocks)", "Frames trimmed off so only the photo shows", "Fixed"),
            ("The report's crawler saw 36 pages; the site really has 183 (160 blog posts), blocked to plain crawlers", "All 183 rebuilt on their URLs and canonicals, in a real browser crawl", "Fixed"),
            ("No page names Salt Lake City in the title (report)", "Home targets \"gutter installation Salt Lake City\"; every service page has Salt Lake City in the title, H1 and first paragraph", "Fixed"),
            ("Meta descriptions missing on key pages (18 of 183 have none)", "Hand-written for home, services and company pages; posts use their own or their first paragraph", "Fixed"),
            ("Old internal links (roofing-2/, siding/, windows-2/, posts without /blog/) redirect or 404", "Every one pointed straight at the real page", "Fixed"),
            ("Blog posts use Unsplash hotlinks, Shutterstock files and Bannerbear auto-generated banners", "Removed; only the client's own job photos are used", "Fixed"),
            ("6 images on the live site are broken (404)", "Not carried over", "Fixed"),
            ("5 posts target the competitor brand \"Leaf Guard\" (scam, complaints, support, warranty)", "Kept on their URLs as written; legal/brand review recommended", "Needs Angelo"),
            ("Review count: site says 413, Google profile 427", "No count or stars shown until confirmed", "Needs client"),
            ("Two Universal Analytics IDs still in the code (UA stopped in 2024)", "All tracking kept on the live build (GA4, two GTM, Google Ads, CallRail, Podium); UA can be removed", "Needs Angelo"),
            ("Mobile speed 84/100 (Divi, page builder CSS)", "Plain HTML, one CSS file, WebP photos, lazy-loaded", "Fixed, re-test after go-live"),
        ],
        "questions": ["OK to show 4.8 stars / 427 Google reviews? (site says 413)", "Do you do roof repair and metal roofing? (biggest keywords; no page yet)",
                      "Keep the 5 \"Leaf Guard\" brand posts? (Angelo)", "Are the financing rates (0%/12 mo, 2.99%/12 yr, 7.99%/10 yr) current?",
                      "Remove the two retired Universal Analytics tags?", "BBB A+, GAF Certified, Owens Corning Preferred, HomeAdvisor Elite: all current?"],
        "pages": [("Home", "home/index.html"), ("Rain gutters", "services/rain-gutters-installation/index.html"), ("Heat cable", "services/roof-heat-cable-installation/index.html"),
                  ("New blog post", "blog/5-inch-vs-6-inch-gutters/index.html"), ("Blog index", "blog/index.html"), ("Our work", "our-work/index.html"),
                  ("About", "about-mm-gutters-exteriors/index.html"), ("Request a quote", "request-a-quote/index.html")],
    },
    {
        "key": "roofwiseut.com", "name": "RoofWise", "city": "Salt Lake City, UT", "title": "RoofWise Review",
        "report": "2026-10-17_roofwiseut.com_report.html", "old": "old_roofwise", "new": "new_roofwise",
        "stats": [("10", "pages rebuilt, same URLs"), ("1,138", "words in the new blog post"), ("4", "real photos (from their drone video)"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned as a field report shot from the air: their own drone footage plays behind a camera viewfinder, a marked-up drone frame, a situation picker, and services that swap the drone view", "Fixed"),
            ("robots.txt and sitemap.xml point to roofwise-clear-path.lovable.app, not roofwiseut.com", "New robots.txt and sitemap on the real domain", "Fixed"),
            ("Canonicals are relative (\"/about\"), and the app domain is a duplicate copy of the site", "Absolute canonicals on every page; lovable.app copy should be taken down or redirected", "Needs Angelo"),
            ("12 of the 14 images look AI-generated (job \"photos\" and 3D graphics)", "Removed; photos are now 4 frames from their own drone video of a real re-roof", "Fixed, ask for more photos"),
            ("No page names Salt Lake City (report)", "Home targets \"roofing company Salt Lake City\"; every service page has Salt Lake City in the title, H1 and first paragraph", "Fixed"),
            ("Superlatives: \"Utah's most trusted roofing contractors\", \"one of the best workmanship warranties\"", "Not used", "Fixed"),
            ("Service pages are thin (66-101 words)", "Rewritten from the site's own facts, with FAQs and process steps", "Fixed"),
            ("Mobile speed 75/100 (30 MB autoplay hero video)", "Same real footage cut to a 14-second, 1.6 MB muted loop; plain HTML and WebP frames everywhere else", "Fixed, re-test after go-live"),
            ("No street address on the site; the Google profile has one (5903 S Clear Vista Dr)", "Left off until the client confirms", "Needs client"),
            ("Metal roofing (170 searches) not offered on the site", "No page built; ask the client", "Needs client"),
            ("Schema only on the home page", "RoofingContractor (6 counties), Service, FAQPage, BlogPosting, BreadcrumbList on every page", "Fixed"),
        ],
        "questions": ["Show the street address (5903 S Clear Vista Dr, Salt Lake City 84118)?", "OK to show 5 stars / 25 Google reviews?", "Do you install metal roofs? (170 searches)",
                      "Are 200+ customers, 50+ realtors, 9+ years and 20+ years crew experience current?", "Can you send real job photos (more than the drone video)?",
                      "Brand name: RoofWise or Roof-Wise?", "Phone shown as (435) 655-1246?"],
        "pages": [("Home", "home/index.html"), ("Roof repair", "roof-repair/index.html"), ("Roof replacement", "roof-replacement/index.html"),
                  ("Insurance claims", "insurance-claims/index.html"), ("New blog post", "blog/what-does-hail-damage-look-like-on-a-roof/index.html"),
                  ("Schedule inspection", "schedule-inspection/index.html"), ("Service area", "service-area/index.html"), ("About", "about/index.html")],
    },
    {
        "key": "jordanriverroofing.com", "name": "Jordan River Roofing", "city": "Taylorsville, UT", "title": "Jordan River Roofing Review",
        "report": "2026-10-17_jordanriverroofing.com_report.html", "old": "old_jordanriver", "new": "new_jordanriver",
        "stats": [("92", "URLs rebuilt, same addresses"), ("1,256", "words in the new blog post"), ("7", "real photos kept (24 AI images dropped)"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned around transit signage: a Valley Line route map of the 13 cities, coloured service lines, a departure-board fact strip, a job log of real photos and a moving review wall", "Fixed"),
            ("The wide home-page photo of the crew and truck has garbled lettering and a wrong phone number on the truck, a sign of an AI-generated or AI-altered image", "Removed; only the 7 clearly real job photos are used", "Needs client"),
            ("Single-page app: every URL returns the same empty shell, one title, one meta, and canonical=\"/\" on all 92 pages", "Plain HTML pages, each with its own title, meta description and canonical", "Fixed"),
            ("No real sitemap (sitemap.xml returns the app shell)", "sitemap.xml with the 28 indexable pages; robots.txt points to it", "Fixed"),
            ("65 service x city pages are near-duplicate doorway pages (about 77% identical)", "Kept on their URLs with honest short copy; canonical to the main service page, left out of the sitemap", "Needs Angelo"),
            ("City copy says commercial TPO roofs carry the TAMKO DiamondShield shingle warranty, \"strongest warranty in Utah\"", "Not reused; city pages rewritten from verified facts", "Fixed"),
            ("23 of the 36 images look AI-generated (service and city pages)", "Removed; only the 8 real job photos are used", "Fixed, ask for more photos"),
            ("Numbers contradict: founded 2019 vs \"Since 2003\" / \"20+ years\" / \"over 15 years\"; 4.9 stars vs 4.8 on Google; 5,000+ roofs, 98% satisfaction", "None of the contradictory or unverifiable numbers used", "Needs client"),
            ("Claims not confirmed: 24/7 emergency, BBB accredited (no listing found), GAF / CertainTeed / Owens Corning partner logos", "Left out until the client confirms", "Needs client"),
            ("No page names Taylorsville (report)", "Home targets \"roofing company Taylorsville\"; all 5 service pages have Taylorsville in title, H1 and first paragraph", "Fixed"),
            ("Warranty page details unchecked", "DiamondShield terms checked against TAMKO's own program brochure", "Fixed"),
            ("Hours differ (8-6 header vs 7-6 contact page); reply time differs (1 business hour vs 1 business day)", "Header hours used; no reply-time promise", "Needs client"),
            ("Mobile speed 67/100 (React app, large AI PNGs)", "Plain HTML, one CSS file, WebP images, lazy-loaded", "Fixed, re-test after go-live"),
        ],
        "questions": ["Founded 2019, or in business since 2003? (site says both)", "Is 24/7 emergency service real? Same-day?", "Are you BBB accredited? We couldn't find a listing",
                      "Are you GAF, CertainTeed or Owens Corning certified, or TAMKO only? Which TAMKO Edge tier (DiamondShield needs the top one)?",
                      "OK to show 4.8 stars / 48 Google reviews?", "Office hours: 8am or 7am start?", "Can you send more real job photos, with the city for each? Is the wide crew-and-truck photo on the old home page real?",
                      "Keep the 65 service x city pages, or redirect them to the main service pages? (Angelo)"],
        "pages": [("Home", "home/index.html"), ("Roof replacement", "services/new-roof-replacement/index.html"), ("Service areas", "service-areas/index.html"),
                  ("Sandy (city page)", "service-areas/sandy/index.html"), ("Service x city", "services/commercial-roofing/murray/index.html"),
                  ("New blog post", "blog/ridge-vent-vs-turtle-vents/index.html"), ("Warranty", "warranties/index.html"), ("About", "about/index.html")],
    },
    {
        "key": "jemzaroofing.com", "name": "Jemza Roofing", "city": "Salt Lake City, UT", "title": "Jemza Roofing Review",
        "report": "2026-10-17_jemzaroofing.com_report.html", "old": "old_jemza", "new": "new_jemza",
        "stats": [("15", "pages rebuilt on the same .php URLs"), ("1,560", "words in the new blog post"), ("82", "real job photos, local WebP"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned as a mountain-modern portfolio: full-screen photography, a film strip of projects that moves as you scroll, a services index where the photo follows your pointer, Fraunces display type and copper accents", "Fixed"),
            ("Testimonials page shows template reviews (\"tire service and 24/7 mobile support\", \"Jemza Roofing Corp.\", 4.5 from 2 reviews)", "Removed; the page now shows the 4 real reviews from the home page and links to Google for new ones", "Needs client"),
            ("8 of 14 pages have an empty title tag; one meta description repeated on every page", "Every page has its own title and meta description", "Fixed"),
            ("Service pages are photos and videos with no text", "Each service page now has an answer-first intro, written only from facts on the site, plus captioned photos", "Fixed"),
            ("No page names Salt Lake City (report)", "Home targets \"roofing company Salt Lake City\"; every service page has Salt Lake City in the title, H1 and first paragraph", "Fixed"),
            ("No canonical tags, no sitemap, no robots.txt (both 404)", "Canonicals on every page, sitemap.xml and robots.txt added", "Fixed"),
            ("No schema", "RoofingContractor (bilingual, payment, 50-mile area), Service, FAQPage, Review, BlogPosting, BreadcrumbList", "Fixed"),
            ("Mobile speed 77/100; full-size JPGs (up to 4032 px) and 16 MB videos on every page", "Plain HTML, WebP photos, lazy-loaded; videos load only when played", "Fixed, re-test after go-live"),
            ("Review form posts to insert.php with no real moderation visible", "Form dropped; \"Leave a review on Google\" link instead", "Needs Angelo"),
            ("Contact form relies on a PHP token/captcha (process.php)", "Same field names and action kept; the captcha snippet must be re-added when it goes live", "Needs Angelo"),
            ("Roof repair (biggest keyword) has no page", "Listed under services only; page waits for the client to confirm the service", "Needs client"),
        ],
        "questions": ["Are the testimonials-page reviews (David Clark, Sarah Bell) real? We assumed not", "OK to show 4.9 stars / 29 Google reviews?",
                      "Do you do roof repair, inspections and leak repair? (biggest keywords)", "Roof installation for new builds, and commercial: build pages?",
                      "Phone format: (385) 261-2942 as on the site?", "Which cities do most jobs come from (for city pages)?", "Can you share real prices for a cost page?"],
        "pages": [("Home", "home/index.html"), ("Metal roofing", "metal-roofing/index.html"), ("Caps & shrouds", "ChimneyCap-Shroud/index.html"),
                  ("New blog post", "chimney-cap-vs-chimney-shroud/index.html"), ("Services", "services/index.html"), ("Gutters", "gutter-soffit-fascia/index.html"),
                  ("Reviews", "testimonials/index.html"), ("Contact", "contact/index.html")],
    },
    {
        "key": "jandnroofing.com", "name": "J & N Roofing Maintenance", "city": "West Valley City, UT", "title": "J & N Roofing Review",
        "report": "2026-10-17_jandnroofing.com_report.html", "old": "old_jandn", "new": "new_jandnroofing",
        "stats": [("79", "pages built, same URLs"), ("411", "copied posts left out"), ("1,164", "words in the new blog post"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned as a printed handbook: a magazine-cover home page with an original line drawing of the parts of a roof, services as a table of contents, a letter from the team, guides on a bookshelf, the real offers as tear-off coupons", "Fixed"),
            ("411 of 452 blog posts are copied from goodshomedesign.com (crochet, crafts, cabins; hotlinked images; another site's Amazon affiliate tag)", "Left out of the new site; full list in the copied-posts file for a 410 or noindex decision", "Needs Angelo"),
            ("Home page doesn't target West Valley City", "Home title, H1 and first sentence target \"roofing company West Valley City\"", "Fixed"),
            ("Service pages don't name West Valley City", "All 11 service pages plus services and about now have it in the title, H1 and first paragraph", "Fixed"),
            ("Meta descriptions missing on key pages", "Hand-written for home and service pages; others from each page's own text", "Fixed"),
            ("References page publishes private homeowners' phone numbers", "Names kept; phone numbers held back until the client confirms", "Needs client"),
            ("Years in business contradict (20, over 20, 27, over 27, over 30)", "No year claims used", "Needs client"),
            ("36 of the 41 own posts are near-duplicate \"roofing salt lake city\" pages competing with each other", "Kept on their URLs; merge plan needs Angelo", "Needs Angelo"),
            ("Old links redirect or 404 (services-2/, financing/)", "Pointed at the real pages or removed", "Fixed"),
            ("Most photos look like stock images", "Heroes use house and roof shots only; real job photos requested", "Needs client"),
            ("Thank-you page and search template indexable", "Marked noindex, left out of the sitemap", "Fixed"),
            ("Mobile speed 70/100", "Plain HTML, one CSS file, WebP images under 150 KB, lazy-loaded", "Fixed, re-test after go-live"),
            ("No schema", "RoofingContractor, Service, FAQPage, BlogPosting, DefinedTermSet (glossary), BreadcrumbList", "Fixed"),
        ],
        "questions": ["Remove the 411 copied posts (410) or noindex them? (Angelo)", "How many years in business?", "May individual references' phone numbers be shown?",
                      "Show the street address (3842 S 2200 W) on the site?", "Are the $70/$130/$200 special offers still current?", "Can you send real job photos?",
                      "OK to show 5 stars / 9 reviews?", "Is jandnroofing.com the right site for J & N Roofing Maintenance LLC? (report flag)"],
        "pages": [("Home", "home/index.html"), ("Roof repair WVC", "services/roofing-repairs/index.html"), ("Roof replacement", "services/roof-replacement/index.html"),
                  ("Warranty support", "warranty-support/index.html"), ("Special offers", "special-offers/index.html"),
                  ("New blog post", "how-far-should-shingles-overhang-the-drip-edge/index.html"), ("Glossary", "glossary-of-roofing-terms/index.html"), ("Testimonials", "testimonials/index.html")],
    },
    {
        "key": "gprroofing.com", "name": "Go Pro Roofing", "city": "West Valley City, UT", "title": "Go Pro Roofing Review",
        "report": "2026-10-17_gprroofing.com_report.html", "old": "old_gpr", "new": "new_gprroofing",
        "stats": [("32", "pages built, same URLs"), ("1,248", "words in the new blog post"), ("34", "real photos and badges kept"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned in a pro tool-brand style: heavy italic condensed type, red diagonal slashes, a spec-plate hero, the services as a catalog lineup, an interactive pick-the-right-roof selector and a job-site photo wall cropped to hide the watermarks", "Fixed"),
            ("Mobile speed 26/100; the logo alone is a 40,974 x 7,261 px PNG (1.7 MB)", "Logo scaled to 600 px; plain HTML, no Elementor, WebP images under 150 KB, lazy-loaded", "Fixed, re-test after go-live"),
            ("29 of 30 pages have no meta description", "Hand-written for home, service pages, blog, gallery, reviews; others from each page's own text", "Fixed"),
            ("West Valley City missing from most titles and H1s", "Home and 8 main pages now have West Valley City in the title, H1 and first paragraph", "Fixed"),
            ("Roof repair page's H1 says \"Roof Replacement Experts\"", "H1 is now \"Roof Repair in West Valley City\"", "Fixed"),
            ("87 images look like stock or AI photos", "Only real job photos, crew photos and badges kept", "Fixed, ask for more photos"),
            ("Category pages have no canonical tag", "Self-canonical added to all 4", "Fixed"),
            ("Broken links: a typo URL and a 404 blog link", "Typo pointed to the right page; 404 link removed", "Fixed"),
            ("Privacy policy and terms pages are empty", "Marked noindex with a placeholder", "Needs client"),
            ("Two posts answer the same question (who to call for a roof leak)", "Both kept on their URLs; merge needs a redirect", "Needs Angelo"),
            ("Badges say \"GAF Master Elite\"; text says \"GAF recognized/authorized\"", "Text kept as written; badges shown as on the site", "Needs client"),
            ("Prices and timing claims only in FAQs", "Their FAQ ranges shown in the roof chooser and service intros", "Needs client"),
            ("No schema beyond basics", "RoofingContractor, Service, FAQPage, BlogPosting, BreadcrumbList", "Fixed"),
        ],
        "questions": ["Confirm the price ranges from your FAQs ($8k-15k replacement, $300-1,500 repairs, TPO $5-12/sq ft)", "Is \"24/7 emergency service\" accurate?",
                      "GAF Master Elite or GAF certified: which is current?", "OK to show 5.0 stars / 62 reviews?", "Show the street address (5291 W Ted Wy) on the site?",
                      "Privacy policy and terms text?", "Merge the two roof-leak posts? (Angelo)", "More real job photos, with the city for each?"],
        "pages": [("Home", "home/index.html"), ("Roof repair WVC", "roof-repair-west-valley-city/index.html"), ("Roof replacement", "roof-replacement-services-utah/index.html"),
                  ("Metal roofing", "metal-roofing-contractors-west-valley-city-ut/index.html"), ("Gallery", "gallery/index.html"),
                  ("New blog post", "how-to-do-valleys-on-a-metal-roof/index.html"), ("Reviews", "reviews/index.html"), ("Contact", "contact/index.html")],
    },
    {
        "key": "pioneerroofingutah.com", "name": "Pioneer Roofing", "city": "Salt Lake City, UT", "title": "Pioneer Roofing Review",
        "report": "2026-10-17_pioneerroofingutah.com_report.html", "old": "old_pioneer", "new": "new_pioneerroofingutah",
        "stats": [("52", "pages built, same URLs"), ("1,306", "words in the new blog post"), ("47", "local WebP photos"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned like a heritage workwear brand: a turning Est. 1980 hexagon seal, stitched patches, the roof types as hang tags with the real published prices, a ledger-style price table and a big call-John section", "Fixed"),
            ("Only 1 of 51 pages names Salt Lake City", "Home and the 10 main service pages now have Salt Lake City in the title, H1 and first paragraph", "Fixed"),
            ("Mobile speed 40/100", "Plain HTML, one CSS file, no Elementor, WebP photos under 150 KB, lazy-loaded", "Fixed, re-test after go-live"),
            ("45 of 50 pages have no meta description", "Hand-written for home and service pages; others written from each page's own text", "Fixed"),
            ("Images missing alt text", "Every image has descriptive alt text plus width and height", "Fixed"),
            ("Real prices hidden on one page", "Price ranges shown on the home page and in the service cards; pricing page targets \"roof replacement cost Salt Lake City\"", "Fixed"),
            ("Years in business contradict (nearly 40, over 40, 45, 45+)", "New copy says \"since 1980\", from the logo", "Needs client"),
            ("Two warranty versions (10-20 yr flat / 40 yr shingles vs lifetime materials + 10 yr labor)", "Only the 10-year labor + lifetime materials wording used", "Needs client"),
            ("TPO price line reuses the steep-pitch description", "Description left off the TPO price", "Needs client"),
            ("Two commercial pages compete (commercial-roofing vs your-go-to-solution...)", "Both kept on their URLs; merge needs a redirect", "Needs Angelo"),
            ("Broken link to /careers/ (404) on the About page", "Link removed", "Fixed"),
            ("Thank-you page and home-2 copy indexable", "Marked noindex, left out of the sitemap", "Fixed"),
            ("No schema beyond Yoast basics", "RoofingContractor (2 offices), Service, FAQPage, BlogPosting, BreadcrumbList", "Fixed"),
        ],
        "questions": ["How many years: say \"since 1980\" everywhere?", "Which warranty wording is current?", "OK to show 4.8 stars / 175 reviews?",
                      "Phone format OK as (801) 943-7663?", "OK to name John and Linda Stout under the owner photo?",
                      "Merge the two commercial roofing pages? (Angelo)", "Correct description for the TPO price range?", "Do you work in South Jordan, Sandy and Draper? Recent jobs there?"],
        "pages": [("Home", "home/index.html"), ("Roof repair SLC", "roofing-repairs/index.html"), ("Pricing", "pricing/index.html"),
                  ("Salt Lake City", "salt-lake-city/index.html"), ("TPO membrane", "tpo-membrane/index.html"),
                  ("New blog post", "blog-what-is-the-25-percent-rule-for-roofing/index.html"), ("Estimator", "new-roof-estimator/index.html"), ("Book inspection", "book-inspection/index.html")],
    },
    {
        "key": "ezroofingnow.com", "name": "EZ Roofing", "city": "Salt Lake City, UT & Cabot, AR", "title": "EZ Roofing Review",
        "report": "2026-10-17_ezroofingnow.com_report.html", "old": "old_ezroofing", "new": "new_ezroofingnow",
        "stats": [("253", "pages built, same URLs"), ("1,423", "words in the new blog post"), ("222", "local WebP images"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned around their free property evaluation: a clipboard checklist in the hero that ticks itself off, the seven EZ Shield parts stacking up as you scroll, a drone photo with a live scan line, the real crew photo, and the two offices as photo cards", "Fixed"),
            ("No page names Salt Lake City in the home page title or H1", "Home title, H1 and first sentence target \"roofing company Salt Lake City\"; Utah pages keep Salt Lake City in titles and H1s", "Fixed"),
            ("Utah pages call the company \"EZ Roofing Arkansas\" (titles and copy on 6 Salt Lake City pages)", "Renamed to EZ Roofing on every Utah page", "Fixed"),
            ("35 pages have no meta description", "Written from each page's own text; home and new pages written by hand", "Fixed"),
            ("Two competing pages: commercial roofing + commercial roof", "Both kept on their URLs for now; merge needs a redirect", "Needs Angelo"),
            ("Home page and the Salt Lake City city page say the same thing", "Home targets the keyword; city page kept as the local hub. Consider a merge", "Needs Angelo"),
            ("City pages are near-identical templates (17 Utah, 20 Arkansas)", "Kept on their URLs; each gets nearby-city links. Need real local content", "Needs client"),
            ("Test pages live and indexable (home-test, schedule-a-inspection-test)", "Marked noindex, left out of the sitemap", "Fixed"),
            ("8 empty team-member pages (name only)", "Marked noindex; the full team lives on Meet Our Team", "Fixed"),
            ("Broken link to /arkansas-city/conway/ and 3 missing images (404)", "Link points to the real Conway page; missing images dropped", "Fixed"),
            ("Home claims a \"5 star Google rating\" (Google shows 4.7 from 51)", "Claim left off; rating waits for client OK", "Needs client"),
            ("Stock photos of models shown on posts", "15 stock people photos removed; only EZ crew and job photos used", "Fixed"),
            ("Mobile speed 90/100, right on the line", "Plain HTML, one CSS file, WebP images under 150 KB, lazy-loaded", "Fixed, re-test after go-live"),
        ],
        "questions": ["Business name to show: EZ Roofing, EZ Roofing Utah, or EZ Contracting LLC?", "Keep the toll-free (888) 575-3025 for Utah, or add a local 801 number?",
                      "OK to show 4.7 stars / 51 reviews instead of \"5 star Google rating\"?", "Merge \"commercial roofing\" and \"commercial roof\"? (Angelo)",
                      "What is the pre-cast concrete page for?", "Which state is license #0428111225 for?",
                      "The $25 promo page shows an old Cabot address (2225 Bill Foster Memorial Hwy W): retire it?", "Real local content for the city pages (jobs, photos)?"],
        "pages": [("Home", "home/index.html"), ("Roof repair SLC", "utah/salt-lake-city-roof-repair/index.html"), ("Roof replacement SLC", "utah/salt-lake-city-roof-replacement/index.html"),
                  ("Salt Lake City", "utah-city/salt-lake-city/index.html"), ("Free inspection", "our-free-inspection/index.html"),
                  ("New blog post", "best-time-of-year-to-replace-a-roof-in-utah/index.html"), ("Projects", "projects/index.html"), ("Contact", "contact/index.html")],
    },
    {
        "key": "customroofs.biz", "name": "Custom Roofing LLC", "city": "Lehi, UT", "title": "Custom Roofing Review",
        "report": "2026-10-16_customroofs.biz_report.html", "old": "old_customroofs", "new": "new_customroofs.biz",
        "stats": [("9", "pages built"), ("1,418", "words in the new blog post"), ("19", "local WebP images"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned as a coppersmith's sample book: a copper element tile in the hero that weathers through the five real patina stages as you scroll, the services as copper sample chips on a ring, a standing-seam sheet that ages stage by stage, an arched photo after their curved dormers, and Bodoni serif type", "Fixed"),
            ("Same address as Aluminum Lock Roofing on Google", "No street address on the draft; footer says \"Lehi, Utah\" as the client's site does", "Needs Angelo"),
            ("No page names Salt Lake City", "Home page title, H1 and first sentence target \"roofing company Salt Lake City\", worded truthfully (located in Lehi, serving Salt Lake City)", "Fixed"),
            ("Mobile speed 62/100", "Plain HTML, one CSS file, no Elementor, WebP images under 150 KB, lazy-loaded", "Fixed, re-test after go-live"),
            ("Images missing alt text", "Every image has descriptive alt text plus width and height", "Fixed"),
            ("Home page has no H1; other H1s skip the page keyword", "One H1 per page, each starting with its keyword (e.g. \"Copper Roofing in Utah\")", "Fixed"),
            ("Years in business contradict (75 / 15+ / 20+)", "All year claims left out until the client confirms one number", "Needs client"),
            ("Broken link: \"Gutter\" on the services page goes to a 404", "Link removed; gutters listed without a link until a gutter page exists", "Fixed"),
            ("Internal links that redirect (/home/contact, /lehi-custom-roofing/...)", "Links point straight at the final pages", "Fixed"),
            ("Builder templates in the sitemap (elementor-hf)", "Blocked in robots.txt and left out of the new sitemap", "Fixed"),
            ("No schema beyond Yoast basics", "RoofingContractor, Service, FAQPage, BreadcrumbList, BlogPosting schema", "Fixed"),
            ("No blog", "New blog and first post: \"Why Does Copper Turn Green?\" with 3 cited sources", "Fixed"),
            ("8 of 10 services unconfirmed (roof repair, metal...)", "No new service pages invented; waiting for the client", "Needs client"),
        ],
        "questions": ["How should the shared address with Aluminum Lock Roofing be handled? (Angelo first)", "How many years in business: 75, 15+ or 20+?",
                      "Confirm 700+ projects, 1000+ clients, the 5-year workmanship warranty and the free consultation",
                      "Do you offer 24/7 emergency repairs?", "Which services do you offer besides copper (roof repair, metal, replacement, gutters...)?",
                      "Is \"Sega Nintendo\" a real reviewer? (left off the draft)", "Phone format: 801-889-4220, and keep the secondary line?",
                      "Should the Spanish /es/ pages be rebuilt too?"],
        "pages": [("Home", "home/index.html"), ("Copper roofing", "copper-roofing-utah/index.html"), ("Repair & maintenance", "custom-roofing-maintenance-utah/index.html"),
                  ("Siding", "lehi-custom-siding-home-value/index.html"), ("Services & newest work", "home/roofing-services-lehi-quality-guaranteed/index.html"),
                  ("New blog post", "blog/why-does-copper-turn-green/index.html"), ("Contact / quote", "copper-roofing-lehi/index.html")],
    },
    {
        "key": "aestheticroofing.com", "name": "Aesthetic Roofing", "city": "South Jordan, UT", "title": "Aesthetic Roofing Review",
        "report": "2026-10-16_aestheticroofing.com_report.html", "old": "old_aes", "new": "new_aestheticroofing",
        "stats": [("28", "pages rebuilt"), ("1,771", "words in the new blog post"), ("39", "local WebP images"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned around their real promises: a perforated ticket stub for the On-Time Start Guarantee, a 14-day calendar that fills in day by day, services as expanding drone-photo panels, a process timeline and a sticky FAQ with the blog guide", "Fixed"),
            ("Mobile speed 33/100", "Plain HTML, one CSS file, no Elementor or sliders, small WebP images lazy-loaded below the top", "Fixed, re-test after go-live"),
            ("No page names South Jordan", "South Jordan in the title, H1 and first paragraph of the home page and all 8 service and roof-type pages", "Fixed"),
            ("Images missing alt text", "Every image has descriptive alt text plus width and height", "Fixed"),
            ("Gutter replacement page titled \"Our Services\" with no meta", "New title and meta description naming South Jordan", "Fixed"),
            ("Service areas page had no meta description", "New meta description", "Fixed"),
            ("Broken internal links (3 dead URLs, 14 links)", "Pointed at the real pages: asphalt shingle, metal roofing, storm damage", "Fixed"),
            ("WordPress \"Sample Page\" live and in the sitemap", "Left out of the new site and sitemap; recommend a 301 to the home page", "Needs developer"),
            ("No blog", "New blog and first post: \"What Causes Roof Leaks?\"", "Fixed"),
            ("Roof-type images were 3D renders", "Replaced with the client's drone photos and two real Unsplash photos", "Fixed"),
            ("Three different phone numbers (site, call tracking, Google)", "Kept the site's number and Tag Manager so call tracking still works", "Needs client"),
        ],
        "questions": ["Which phone number is the main one: (801) 810-2276, (801) 516-4053 or 801-997-1500?", "OK to show 4.8 stars / 350+ reviews?",
                      "Is \"495+ roofs installed last year\" still accurate?", "Do you offer roof leak repair as its own service?", "Merge the two gutter pages?",
                      "Real prices for a cost page?", "City pages for Salt Lake City, Sandy and Draper?", "Blog author name and role?"],
        "pages": [("Home", "home/index.html"), ("Roof Repair", "services/roof-repair/index.html"), ("Roof Replacement", "services/roof-replacement/index.html"),
                  ("Storm Damage", "services/storm-damage-roof-repair/index.html"), ("Roof Types", "roof-types/index.html"), ("Projects", "projects/index.html"),
                  ("New blog post", "blog/what-causes-roof-leaks/index.html"), ("Contact", "contact/index.html")],
    },
    {
        "key": "aluminumlockroofing.com", "name": "Aluminum Lock Roofing", "city": "Salt Lake City, UT", "title": "Aluminum Lock Review",
        "report": "2026-10-16_aluminumlockroofing.com_report.html", "old": "old_alr", "new": "new_aluminumlockroofing",
        "stats": [("9", "pages built"), ("1,410", "words in the new blog post"), ("21", "local WebP images"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned around the interlock: four aluminum shingles lock together in the hero, a color picker shows a real Aluminum Lock roof in each finish, the roof system is shown exploded in 3D, and the gallery is a photo wall", "Fixed"),
            ("Same address as Custom Roofing LLC on Google", "Street address left off the draft until Angelo decides", "Needs Angelo"),
            ("Mobile speed 60/100", "Plain HTML, one CSS file, no Elementor, small WebP images lazy-loaded", "Fixed, re-test after go-live"),
            ("No page names Salt Lake City", "Salt Lake City in every page's title or H1, and in the home page's first sentence", "Fixed"),
            ("Images missing alt text", "Every image has descriptive alt text plus width and height", "Fixed"),
            ("Missing meta descriptions on About, Contact, FAQ", "New meta descriptions written", "Fixed"),
            ("Builder pages leaking into Google (header template, form)", "Blocked in robots.txt and left out of the sitemap", "Fixed"),
            ("Privacy policy page has no policy", "Marked noindex, placeholder shown", "Needs client"),
            ("FAQ not marked up", "FAQ turned into an accordion with FAQPage schema", "Fixed"),
            ("No blog", "New blog and first post: \"Can You Put a New Roof Over an Old Roof?\"", "Fixed"),
            ("9 of 10 services unconfirmed", "No service pages invented; waiting for the client", "Needs client"),
        ],
        "questions": ["Is the address shared with Custom Roofing LLC on purpose?", "Exact business name to use?", "Phone format OK as (801) 484-3321?",
                      "Which services do you offer (repair, metal, replacement, gutters...)?", "Where do you install?", "Real prices and warranty terms?",
                      "Privacy policy text?", "Blog author name and role?"],
        "pages": [("Home", "home/index.html"), ("Services", "services/index.html"), ("About", "about-us/index.html"), ("FAQ", "faq/index.html"),
                  ("New blog post", "blog/can-you-put-a-new-roof-over-an-old-roof/index.html"), ("Contact", "contact-us/index.html")],
    },
    {
        "key": "amcoroof.com", "name": "American Roofing Company", "city": "South Salt Lake, UT", "title": "American Roofing Review",
        "report": None, "old": "old_amco", "new": "new_amcoroof",
        "stats": [("107", "pages rebuilt"), ("1,813", "words in the new blog post"), ("243", "local WebP images"), ("0", "QA issues")],
        "audit": [
            ("Typography", "Mulish everywhere with gray headings; low hierarchy", "warn"),
            ("Layout", "Identical white cards in every section; big empty gap in the steps section", "warn"),
            ("Images", "Some sections showed blank image boxes; several iStock photos of models posing as staff", "warn"),
            ("Sitemap", "9 URLs in the sitemap are really 301 redirects (2 of them send people to the home page)", "bad"),
            ("Internal links", "30 links in the content went through old redirecting URLs", "warn"),
            ("Titles", "76 titles outside 50-60 characters; home title is 94 characters", "warn"),
            ("Tracking", "Google Tag Manager, Hotjar and Alivo chat in place", "good"),
        ],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned as American heritage: an enamel Est. 1954 pin in the hero, a 1954 to 2026 year ruler that fills as you scroll beside the real numbers, the Repair-First Promise set like a stamp, and a project wall with their school and commercial jobs", "Fixed"),
            ("Generic look (Mulish, gray headings, identical cards)", "New heritage design from the eagle logo: navy and red, Bitter slab headings, \"Since 1954\" seal, real stat band", "Fixed"),
            ("Blank image boxes and stock \"staff\" photos", "All 243 images local; real project galleries restored; 4 stock team photos removed", "Fixed"),
            ("9 sitemap URLs that are redirects", "Left out of the new sitemap; redirects kept for go-live", "Needs developer"),
            ("30 links through redirecting URLs", "Pointed straight at the final pages", "Fixed"),
            ("No ice dam content (only a lifespan post)", "New post: \"How to Prevent Ice Dams on a Utah Roof\"", "Fixed"),
            ("Over-long, stuffed titles", "Kept as-is (no keyword file); recommend a title pass", "Needs keyword data"),
            ("Tracking and chat", "GTM, Hotjar and Alivo kept in the live build", "Kept"),
        ],
        "questions": ["Blog author name and role?", "Restore /services/low-slope-roof/ and the solar panel post?", "Project names for gallery photos?",
                      "OK to rewrite long titles once we have keyword data?", "OK to reuse the testimonials shown on the site?"],
        "pages": [("Home", "home/index.html"), ("Residential", "residential/index.html"), ("Commercial", "commercial/index.html"),
                  ("Roof Repairs", "services/roof-repairs/index.html"), ("Service Areas", "service-area/index.html"), ("Murray (city page)", "service-area/murray-utah-roofing/index.html"),
                  ("New blog post", "blog/how-to-prevent-ice-dams-on-a-utah-roof/index.html"), ("Request a Quote", "request-free-quote/index.html")],
    },
    {
        "key": "roofamc.com", "name": "Advanced Roofing & Moisture Control", "city": "Salt Lake City, UT", "title": "Advanced Roofing Review",
        "report": "2026-10-16_roofamc.com_report.html", "old": "old_roofamc", "new": "new_roofamc",
        "stats": [("15", "pages rebuilt"), ("1,958", "words in the new blog post"), ("30", "local WebP images"), ("0", "QA issues")],
        "fixes": [
            ("First draft looked templated and plain", "Redesigned around their own line, Built for Winter: a full-bleed skyline hero with falling rain, the emergency leak line in the hero, and a snow stake that measures the valley’s real snowfall averages (University of Utah) as you scroll", "Fixed"),
            ("Home page targeted Park City, not \"roofing company salt lake city\"", "Home title, H1 and first sentence now target Salt Lake City; Park City kept on its own page", "Fixed"),
            ("Only 1 page named Salt Lake City", "Salt Lake City named across the service pages", "Fixed"),
            ("Mobile speed 73/100", "Plain HTML, one CSS file, small WebP images lazy-loaded", "Fixed, re-test after go-live"),
            ("Images missing alt text", "Every image has descriptive alt text plus width and height", "Fixed"),
            ("Thin service pages", "Roof repair, commercial and residential pages now 1,100-1,300 words with FAQs", "Fixed"),
            ("SLC gallery URL competed with home and commercial pages", "Repositioned as a project gallery with its own title", "Needs Angelo"),
            ("No blog", "New blog and first post: \"How Long Do Roofs Last in Utah?\"", "Fixed"),
            ("Phone and address format differ from Google", "Used the site's format; flagged", "Needs client"),
        ],
        "questions": ["Phone format: (801) 326-9708 or +1801-326-9708?", "Address: \"2212 South West Temple #31\" or the Google version?", "Blog author name and role?",
                      "Is \"4th-generation\" true?", "OK to show 5 stars / 23 reviews?", "Do you do metal roofing as a service?"],
        "pages": [("Home", "home/index.html"), ("Roof Repair", "roof-repair/index.html"), ("Commercial", "commercial/index.html"), ("Residential", "residential/index.html"),
                  ("Waterproofing", "waterproofing/index.html"), ("Park City", "park-city-commercial-roofing-and-waterproofing-solutions/index.html"),
                  ("New blog post", "blog/how-long-do-roofs-last-in-utah/index.html"), ("Contact", "contact/index.html")],
    },
]

ARROW = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'


def shot(src, dst, width, crop_h):
    im = Image.open(src).convert("RGB")
    im = im.crop((0, 0, im.width, min(im.height, crop_h)))
    if im.width > width: im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    q = 78
    while True:
        im.save(dst, "WEBP", quality=q, method=6)
        if os.path.getsize(dst) < 180_000 or q < 45: break
        q -= 8
    return im.size


def report_body(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"(?s)<main>(.*)</main>", s)
    body = m.group(1) if m else ""
    body = re.sub(r"(?s)<footer>.*?</footer>", "", body)
    return body


def status_tag(st):
    cls = "ok" if st.startswith(("Fixed", "Kept")) else "wait"
    return f'<span class="tag {cls}">{html.escape(st)}</span>'


def page(c):
    root = os.path.join(OUT, c["key"], "preview")
    rv = os.path.join(root, "review"); os.makedirs(rv, exist_ok=True)
    sizes = {}
    for tag, base in (("old", c["old"]), ("new", c["new"])):
        d = os.path.join(SHOTS, base + "_d.png") if tag == "old" else os.path.join(SHOTS, base, "d_home.png")
        m = os.path.join(SHOTS, base + "_m.png") if tag == "old" else os.path.join(SHOTS, base, "m_home.png")
        sizes[tag + "_d"] = shot(d, os.path.join(rv, f"{tag}-desktop.webp"), 1200, 2300)
        sizes[tag + "_m"] = shot(m, os.path.join(rv, f"{tag}-mobile.webp"), 390, 1900)

    def im(n, alt):
        w, h = sizes[n]
        nm = n.replace("_d", "-desktop").replace("_m", "-mobile")
        return f'<img src="review/{nm}.webp" alt="{html.escape(alt)}" width="{w}" height="{h}" decoding="async">'

    stats = "".join(f'<div class="stat-tile"><b>{v}</b><span>{l}</span></div>' for v, l in c["stats"])
    if c["report"]:
        rep = f'<div class="report">{report_body(os.path.join(OUT, c["key"], c["report"]))}</div>'
        rep_intro = "The website plan report from the 5 Oct 2026 audit. It's the reason behind most of the changes below."
    else:
        rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td><span class="tag {"ok" if t == "good" else ("bad" if t == "bad" else "wait")}">{"OK" if t == "good" else ("Problem" if t == "bad" else "Needs work")}</span></td></tr>' for a, b, t in c["audit"])
        rep = f'<div class="report"><section><h2>Audit of the current site</h2><p class="sub">There was no keyword report for this client, so this is the review of the live site done for the redesign (Oct 2026).</p><div class="table-wrap"><table><thead><tr><th>Area</th><th>What we found</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table></div></section></div>'
        rep_intro = "What we found on the current website before the redesign."
    fixes = "".join(f"<tr><td>{html.escape(i)}</td><td>{html.escape(f)}</td><td>{status_tag(s)}</td></tr>" for i, f, s in c["fixes"])
    n_fixed = sum(1 for _, _, s in c["fixes"] if s.startswith(("Fixed", "Kept")))
    qs = "".join(f"<li>{html.escape(q)}</li>" for q in c["questions"])
    pages = "".join(f'<a class="pagelink" href="{p}"><span>{html.escape(l)}</span>{ARROW}</a>' for l, p in c["pages"])

    return f'''<title>{c["title"]}</title>
<meta name="description" content="Review of the {html.escape(c["name"])} website redesign: audit report, what was fixed, before and after, and a link to open the new site.">
<style>
:root {{
  --bg: #f4f5f7; --card: #ffffff; --text: #16181d; --muted: #5f6672; --line: #e1e4ea; --accent: #1f5f8b; --accent-ink: #ffffff;
  --good: #23784a; --warn: #9a5d00; --bad: #b3261e; --chip: #eef3f7; --shade: rgba(16,24,40,.08);
  --display: "Space Grotesk", "Segoe UI", system-ui, sans-serif; --body: "Inter", "Segoe UI", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #111317; --card: #1a1d23; --text: #eceef2; --muted: #a3a9b5; --line: #2c3039; --accent: #7fb6dd; --accent-ink: #0d1a24;
  --good: #6cc193; --warn: #e0a54a; --bad: #ef7b72; --chip: #232a33; --shade: rgba(0,0,0,.4); color-scheme: dark; }} }}
:root[data-theme="dark"] {{ --bg: #111317; --card: #1a1d23; --text: #eceef2; --muted: #a3a9b5; --line: #2c3039; --accent: #7fb6dd; --accent-ink: #0d1a24;
  --good: #6cc193; --warn: #e0a54a; --bad: #ef7b72; --chip: #232a33; --shade: rgba(0,0,0,.4); color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--text); font: 15px/1.6 var(--body); }}
a {{ color: var(--accent); }}
.wrap {{ width: 100%; max-width: 1120px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.topnav {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 10; background: color-mix(in srgb, var(--card) 92%, transparent); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }}
.topnav .wrap {{ display: flex; align-items: center; gap: 8px 18px; min-height: 60px; flex-wrap: wrap; padding-block: 8px; }}
.topnav .brand {{ font: 700 15px/1.2 var(--display); margin-right: auto; }}
.topnav .brand small {{ display: block; font: 500 11px/1.3 var(--body); color: var(--muted); letter-spacing: .08em; text-transform: uppercase; }}
.topnav nav {{ display: flex; gap: 2px; flex-wrap: wrap; }}
.topnav nav a {{ text-decoration: none; color: var(--text); padding: 8px 10px; border-radius: 8px; font-weight: 500; font-size: 14px; }}
.topnav nav a:hover {{ background: var(--chip); }}
.btn {{ display: inline-flex; align-items: center; gap: 10px; background: var(--accent); color: var(--accent-ink); text-decoration: none; font-weight: 700; padding: 12px 18px; border-radius: 10px; min-height: 46px; }}
.btn:hover {{ filter: brightness(1.08); }}
.btn.big {{ font-size: 17px; padding: 16px 24px; min-height: 56px; }}
.btn.ghost {{ background: transparent; color: var(--accent); border: 2px solid var(--accent); }}
header.intro {{ padding-block: 40px 28px; }}
.eyebrow {{ font: 600 12px/1 var(--body); letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }}
h1 {{ font: 700 clamp(28px, 4.4vw, 44px)/1.1 var(--display); margin: 10px 0 8px; letter-spacing: -.02em; text-wrap: balance; }}
h2.sec {{ font: 700 clamp(22px, 3vw, 30px)/1.15 var(--display); margin: 0 0 6px; letter-spacing: -.01em; }}
.lede {{ color: var(--muted); max-width: 65ch; margin: 0 0 18px; font-size: 16px; }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 24px 0; }}
.stat-tile {{ background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 16px; }}
.stat-tile b {{ display: block; font: 700 28px/1 var(--display); font-variant-numeric: tabular-nums; }}
.stat-tile span {{ color: var(--muted); font-size: 13px; }}
.block {{ padding-block: 34px; border-top: 1px solid var(--line); scroll-margin-top: 70px; }}
.card {{ background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: clamp(16px, 3vw, 28px); }}
.table-wrap {{ overflow-x: auto; }}
table {{ width: 100%; border-collapse: collapse; font-size: 14px; min-width: 560px; }}
th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ color: var(--muted); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: .06em; }}
.tag {{ display: inline-block; padding: 2px 9px; border-radius: 99px; font-size: 12px; font-weight: 600; white-space: nowrap; }}
.tag.ok {{ background: color-mix(in srgb, var(--good) 16%, transparent); color: var(--good); }}
.tag.wait {{ background: color-mix(in srgb, var(--warn) 16%, transparent); color: var(--warn); }}
.tag.bad {{ background: color-mix(in srgb, var(--bad) 16%, transparent); color: var(--bad); }}
/* the embedded audit report (its own markup, scoped here) */
.report section {{ background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; margin-bottom: 14px; }}
.report h1 {{ font-size: 22px; margin: 0 0 4px; }} .report h2 {{ font: 700 18px/1.3 var(--display); margin: 0 0 10px; }} .report h3 {{ font-size: 15px; margin: 14px 0 6px; }}
.report .sub {{ color: var(--muted); margin: 0 0 14px; }}
.report .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; }}
.report .stat {{ border: 1px solid var(--line); border-radius: 8px; padding: 12px; }} .report .stat b {{ display: block; font-size: 20px; }} .report .stat span {{ color: var(--muted); font-size: 13px; }}
.report .t-good {{ background: color-mix(in srgb, var(--good) 16%, transparent); color: var(--good); }}
.report .t-warn {{ background: color-mix(in srgb, var(--warn) 16%, transparent); color: var(--warn); }}
.report .t-bad {{ background: color-mix(in srgb, var(--bad) 16%, transparent); color: var(--bad); }}
.report td.num, .report th.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
.report dl {{ display: grid; grid-template-columns: max-content 1fr; gap: 6px 16px; margin: 0; }} .report dt {{ color: var(--muted); }} .report dd {{ margin: 0; }}
.report code {{ background: var(--chip); padding: 1px 6px; border-radius: 4px; font-size: 13px; }}
.report .note {{ border-left: 3px solid var(--warn); padding: 8px 12px; background: color-mix(in srgb, var(--warn) 8%, transparent); border-radius: 0 6px 6px 0; margin: 10px 0; }}
.report .check li {{ list-style: none; margin-left: -20px; }} .report .check li::before {{ content: "☐ "; color: var(--muted); }}
.report-box {{ max-height: 640px; overflow: auto; border-radius: 14px; border: 1px solid var(--line); padding: 14px; background: var(--bg); }}
.report-box.open {{ max-height: none; }}
.ba {{ display: grid; gap: 18px; }}
.ba figure {{ margin: 0; }}
.ba figcaption {{ font: 600 13px/1.3 var(--body); color: var(--muted); margin: 10px 0 0; text-transform: uppercase; letter-spacing: .08em; }}
.frame {{ border-radius: 12px; overflow: hidden; border: 1px solid var(--line); box-shadow: 0 18px 40px -24px var(--shade); background: var(--card); }}
.frame .bar {{ display: flex; gap: 6px; padding: 9px 12px; border-bottom: 1px solid var(--line); }}
.frame .bar i {{ width: 10px; height: 10px; border-radius: 50%; background: var(--line); }}
.frame img {{ display: block; width: 100%; max-width: 100%; height: auto; max-height: 560px; object-fit: cover; object-position: top; }}
.phones {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; max-width: 520px; }}
.phone {{ border: 8px solid #20232a; border-radius: 26px; overflow: hidden; background: #20232a; }}
.phone img {{ display: block; width: 100%; max-width: 100%; height: auto; max-height: 520px; object-fit: cover; object-position: top; }}
.pages {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 10px; }}
.pagelink {{ display: flex; justify-content: space-between; align-items: center; gap: 10px; padding: 14px 16px; background: var(--card); border: 1px solid var(--line); border-radius: 10px; text-decoration: none; color: var(--text); font-weight: 600; }}
.pagelink:hover {{ border-color: var(--accent); color: var(--accent); }}
.qs li {{ margin: 6px 0; }}
.cta-row {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
footer.foot {{ color: var(--muted); font-size: 13px; padding-block: 30px 50px; border-top: 1px solid var(--line); }}
@media (min-width: 860px) {{ .ba {{ grid-template-columns: 1fr 1fr; }} }}
</style>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap">

<div class="topnav"><div class="wrap">
<div class="brand">{html.escape(c["name"])}<small>Website redesign review &middot; draft</small></div>
<nav aria-label="Sections"><a href="#report">Report</a><a href="#fixes">What we fixed</a><a href="#mockup">Before &amp; after</a><a href="#pages">Pages</a><a href="#questions">Questions</a></nav>
<a class="btn" href="home/index.html">Open website {ARROW}</a>
</div></div>

<header class="wrap intro">
<div class="eyebrow">Draft for review &middot; {html.escape(c["key"].split("/")[-1])} &middot; {html.escape(c["city"])}</div>
<h1>{html.escape(c["name"])}: website redesign</h1>
<p class="lede">Start with the report to see what was wrong, then what we fixed, then the before-and-after. When you're ready, open the new website. Nothing here is live.</p>
<div class="cta-row"><a class="btn big" href="home/index.html">Open the new website {ARROW}</a><a class="btn ghost" href="#mockup">See before &amp; after</a></div>
<div class="stats">{stats}<div class="stat-tile"><b>{n_fixed}/{len(c["fixes"])}</b><span>issues fixed in the draft</span></div></div>
</header>

<section class="block" id="report"><div class="wrap">
<h2 class="sec">1. The report</h2><p class="lede">{rep_intro}</p>
<div class="report-box" id="rbox">{rep}</div>
<p style="margin:12px 0 0"><button class="btn ghost" type="button" id="rtoggle" style="cursor:pointer;font:inherit;font-weight:700">Show the whole report</button></p>
</div></section>

<section class="block" id="fixes"><div class="wrap">
<h2 class="sec">2. What we fixed</h2><p class="lede">Each problem from the report or the site review, and what the new site does about it.</p>
<div class="card table-wrap"><table><thead><tr><th>Problem</th><th>What we did</th><th>Status</th></tr></thead><tbody>{fixes}</tbody></table></div>
</div></section>

<section class="block" id="mockup"><div class="wrap">
<h2 class="sec">3. Before &amp; after</h2><p class="lede">The home page, old site on the left and the new design on the right. Screenshots from 16 to 17 Oct 2026.</p>
<div class="ba">
<figure><div class="frame"><div class="bar"><i></i><i></i><i></i></div>{im("old_d", "Old " + c["name"] + " home page on desktop")}</div><figcaption>Before: current live site</figcaption></figure>
<figure><div class="frame"><div class="bar"><i></i><i></i><i></i></div>{im("new_d", "New " + c["name"] + " home page design on desktop")}</div><figcaption>After: the new design</figcaption></figure>
</div>
<h3 style="font:700 18px/1.3 var(--display);margin:30px 0 12px">On a phone</h3>
<div class="phones"><figure style="margin:0"><div class="phone">{im("old_m", "Old home page on a phone")}</div><figcaption style="font:600 12px var(--body);color:var(--muted);margin-top:8px;text-transform:uppercase;letter-spacing:.08em">Before</figcaption></figure>
<figure style="margin:0"><div class="phone">{im("new_m", "New home page on a phone")}</div><figcaption style="font:600 12px var(--body);color:var(--muted);margin-top:8px;text-transform:uppercase;letter-spacing:.08em">After</figcaption></figure></div>
<p style="margin:26px 0 0"><a class="btn big" href="home/index.html">Open the new website {ARROW}</a></p>
</div></section>

<section class="block" id="pages"><div class="wrap">
<h2 class="sec">4. Pages to look at</h2><p class="lede">Jump straight into key pages of the new site. Use the browser back button to come back here.</p>
<div class="pages">{pages}</div>
</div></section>

<section class="block" id="questions"><div class="wrap">
<h2 class="sec">5. Questions for the client</h2><p class="lede">These need answers before the site goes live. Full details are in the notes file in OUTBOX.</p>
<div class="card"><ol class="qs">{qs}</ol></div>
</div></section>

<footer class="wrap foot">Draft preview made by Novarte AI for review. Not the live site. Forms are switched off in this preview.</footer>
<script>
(function(){{var b=document.getElementById('rtoggle'),x=document.getElementById('rbox');if(!b||!x)return;
b.addEventListener('click',function(){{var o=x.classList.toggle('open');b.textContent=o?'Show less':'Show the whole report';}});}})();
</script>
'''


ONLY = sys.argv[3] if len(sys.argv) > 3 else None  # optional: one client key, e.g. customroofs.biz
for c in CLIENTS:
    if ONLY and c["key"] != ONLY: continue
    out = os.path.join(OUT, c["key"], "preview", "index.html")
    open(out, "w", encoding="utf-8", newline="\n").write(page(c))
    print("wrote", out)
