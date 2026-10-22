"""Blog for jsprofinish.com (the live site has none): a blog index and one new post.

"Basement Bedroom Egress Windows in Utah: The Code in Plain English"
Main phrase: "basement egress window requirements" (informational). No page on the site targets it: the cost page and the city
pages mention egress in a sentence; this post links to them and to bedrooms/remodeling without competing for their keywords.
Facts and sources, checked 20 Oct 2026:
- Murray City, "Basement Finish Permit" checklist, updated 9/16/24 (a Utah city's plan-review list under the statewide code):
  https://www.murray.utah.gov/DocumentCenter/View/15104/Basement-Finish-Checklist-
  egress per R310.2: min 5.7 sq ft opening, height >= 24 in, width >= 20 in; clear opening <= 44 in above the finished floor;
  window well >= 9 sq ft and >= 36 in wide; wells deeper than 44 in need a ladder or steps (R310.4.2); a well under a deck or
  porch needs a path at least 36 in high and wide; smoke/CO alarms per R314.3, interconnected per R314.4; bedrooms at least
  70 sq ft and not less than 7 ft x 10 ft (as written) with a smoke/CO detector and a window; ceilings per R305.1: 7 ft habitable,
  6 ft 8 in hallways/bathrooms/laundry, 6 ft 4 in at beams and ducts; hallways at least 3 ft wide.
- Utah's State Construction Code incorporates the 2021 International Residential Code with state amendments (Utah Code Title 15A;
  le.utah.gov 2025 HB 313 text).
- The client's own text: every city they work in requires a building permit for basement finishing; every legal bedroom needs an
  egress window; an existing opening is a modest line item, cutting a new opening and digging a well costs more; they pull
  permits and attend inspections.
No prices. Author: the business (owner byline used on the client's own guides is Pablo J. Padilla; kept as the organization
until he approves his name on this post)."""
from engine import faq_html, faq_ld, canon, img
from cfg import U, NAME, ST

POST = ("Basement Bedroom Egress Windows in Utah: The Code in Plain English", "blog/basement-egress-window-requirements-utah/")
MUR = "https://www.murray.utah.gov/DocumentCenter/View/15104/Basement-Finish-Checklist-"
FAQ = [("Do I need an egress window if the basement room isn't a bedroom?", "The checklist above ties the window requirement to sleeping rooms, and the code also asks for an escape opening in basements with habitable space. Your city's plan reviewer makes the call on your layout, which is one reason we draw the plan before anything is framed."),
       ("Can an existing basement window count as egress?", "Only if it meets every number: 5.7 square feet of clear opening, at least 24 inches high, at least 20 inches wide, with the opening no more than 44 inches above the floor. Most older hopper and slider windows in basements fall short on one of those."),
       ("Do window wells need a ladder?", "When the well is deeper than 44 inches, yes: a ladder or steps, so someone can actually climb out. The well itself needs at least 9 square feet of area and at least 36 inches of width.")]


def post():
    body = f'''<p class="answer">A basement room only counts as a bedroom in Utah if it has a way out besides the stairs. That&rsquo;s an egress window: an opening big enough to climb out of, low enough to reach, with a window well big enough to stand in. Here are the numbers a Utah plan reviewer checks, in plain English, and what they mean when you&rsquo;re planning a basement finish.</p>
<p>We finish basements across Davis and Weber County, and egress is the item that most often decides whether a room on the plan can be called a bedroom. It&rsquo;s also the one that surprises people most on price, because a window that looks big enough often isn&rsquo;t.</p>
<h2>Where the rules come from</h2>
<p>Utah builds homes to a statewide construction code that adopts the 2021 International Residential Code, with state amendments. Cities enforce it through the building permit. Every city we work in requires a permit to finish a basement, and the plan reviewer checks the escape openings as part of it.</p>
<p>To keep this concrete, the figures below come from a published Utah example: <a href="{MUR}" rel="noopener">Murray City&rsquo;s Basement Finish Permit checklist</a> (updated September 2024), which lists what its reviewers look for under section R310 of the code. Clearfield, Layton, Ogden and the other cities we work in apply the same statewide code, but always confirm with your own city, because local handouts and amendments differ in the details.</p>
<h2>The window: four numbers</h2>
<ol><li><b>Clear opening of at least 5.7 square feet.</b> This is the actual hole you can climb through with the window open, not the glass size and not the rough opening.</li>
<li><b>At least 24 inches high</b> of clear opening.</li>
<li><b>At least 20 inches wide</b> of clear opening.</li>
<li><b>No more than 44 inches from the floor</b> to the bottom of the clear opening, so a child or an adult in smoke can get up and out.</li></ol>
<p>The catch is that the first number is bigger than the other two multiplied together. A window that is exactly 24 by 20 inches only opens to 3.3 square feet, so it fails. To reach 5.7 square feet you need something closer to 24 by 34 inches, or 20 by 41. That&rsquo;s why the common narrow slider in an older basement rarely qualifies as it is.</p>
<h2>The window well: room to stand and climb</h2>
<ul><li><b>At least 9 square feet</b> of floor area in the well.</li>
<li><b>At least 36 inches wide.</b></li>
<li><b>Deeper than 44 inches? Add a ladder or steps</b>, so someone can actually climb out of the well, not just out of the window.</li>
<li><b>Under a deck or porch?</b> There has to be a clear path at least 36 inches high and wide out to the yard.</li></ul>
<p>Grates and covers over a well have to open from inside without tools or special knowledge. A heavy grate bolted down for safety defeats the point of the window.</p>
<h2>What else the reviewer checks on a basement bedroom</h2>
<p>The same checklist shows what comes with the window when a room is labelled &ldquo;bedroom&rdquo; on the plan:</p>
<ul><li><b>Size:</b> at least 70 square feet, and at least 7 feet in any direction.</li>
<li><b>Smoke and carbon monoxide alarms</b> in the bedroom, interconnected with the rest of the house so one sets them all off.</li>
<li><b>Ceiling height:</b> 7 feet in bedrooms and other living space; 6 feet 8 inches is allowed in hallways, bathrooms and laundry; and beams, ducts and similar obstructions can drop to 6 feet 4 inches.</li>
<li><b>Hallways</b> at least 3 feet wide.</li></ul>
<p>Ceiling height is the one to measure early in older homes. Many 1950s to 1970s basements around Ogden and Roy have 7 to 7.5 foot ceilings, which works, but the soffits around ducts and beams have to be planned so they stay above that 6 foot 4 inch line.</p>
<h2>Existing opening or new opening?</h2>
<p>This is where egress shows up in the budget. If your basement already has a window opening of the right size, or one that can be fitted with a larger, code-compliant window, it&rsquo;s a modest line item. If the foundation wall has to be cut for a new opening and a well dug outside, it costs more, and it isn&rsquo;t optional if you want the room to count as a bedroom. Our <a href="@/basement-finishing-cost/">basement finishing cost guide</a> covers how egress fits into the bigger picture.</p>
<p>Newer homes in Davis County often come with a large egress window already in place for a future bedroom. Older homes, particularly in parts of Weber County, are more likely to need a new opening. Sloped lots with a walk-out or daylight side are the easy case: a full-height door or a window at grade often solves egress on that side of the house.</p>
<h2>Why it&rsquo;s worth doing properly</h2>
<p>An egress window is the code&rsquo;s answer to a simple question: if there&rsquo;s a fire at the bottom of the stairs, how does the person sleeping down there get out? Firefighters use the same opening to get in. It also matters later. A basement bedroom without a legal escape opening can cause trouble at inspection and again when you sell, because it shouldn&rsquo;t be listed as a bedroom.</p>
<h2>How we handle it</h2>
<p>On a basement finish, we check the existing windows and wells during the free estimate, mark any that fall short, and put the fix on the plan before framing starts, so nobody discovers it at inspection. We prepare the plans, pull the permit and schedule the inspections as part of the job. If you&rsquo;re planning a guest suite or an apartment-style finish, see our <a href="@/services/basement-remodeling/">basement remodeling</a> page, or the local notes for <a href="@/cities/ogden/">Ogden</a> and <a href="@/cities/layton/">Layton</a>.</p>
<p>Want us to measure yours? Call <a href="tel:{ST["tel"]}">{ST["phone"]}</a> or <a href="@/contact-us/">ask for a free estimate</a>.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Source: <a href="{MUR}" rel="noopener">Murray City, &ldquo;Basement Finish Permit&rdquo; checklist, updated 9/16/2024</a> (requirements under 2021 IRC sections R305, R310 and R314 as adopted in Utah). Code details can change and local amendments apply: check with your city&rsquo;s building department before you build.</p>'''
    return body


def pages(K, img_):
    p = K.page(POST[1], "Egress windows", POST[0], f"By {NAME} &middot; October 20, 2026", "Blog", "Basement Egress Window Requirements in Utah | JS ProFinish",
               "Basement egress window requirements in Utah, in plain English: the 5.7 sq ft opening, 44 in sill, window well size and ladder, and what it means for a bedroom.",
               post(), image="finished-basement-bedroom", alt="Finished basement bedroom with a window, by JS ProFinish", crumbs=[("Blog", "blog/")], ogtype="article")
    p["body"] = p["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    p["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                  "image": U + "assets/img/finished-basement-bedroom.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    idx = K.page("blog/", "Blog", "Basement Finishing Blog", "Plain-English notes on finishing a basement in Northern Utah.", "Blog", "Basement Finishing Blog | JS ProFinish, Clearfield UT",
                 "Notes from JS ProFinish on finishing a basement in Davis and Weber County: code, egress windows, permits, ceilings and passing inspection.",
                 f'<div class="posts one"><a class="post-card" href="@/{POST[1]}">{img_("finished-basement-bedroom", "")}<span class="pc-d">Oct 20, 2026</span><b>{POST[0]}</b><em>Read {K.ARROW}</em></a></div>')
    return [idx, p]
