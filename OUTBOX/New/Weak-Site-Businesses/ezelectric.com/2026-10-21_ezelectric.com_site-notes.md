# ezelectric.com: redesign notes (21 Oct 2026)

**Not a client yet. Do not contact this business.** Draft only; nothing is live.

## Folders
- `site/`: files to put live. Same 6 URLs and canonicals, plus one new post, robots.txt and sitemap.xml.
- `preview/`: the private review copy. `preview/index.html` is the review page; the site is at `preview/home/`.
- `_build/`: build with `python -I build.py ../site ../preview`, then `python -I qa.py ../site`.

## Concept: "Flip it on"
EZ Electric's voice is all switch puns ("amp up", "bring the spark back"), and their best photo is landscape lighting at dusk. So the site uses a dusk palette: navy, EZ red, and warm bulb amber.
- **Hero:** the dusk photo runs to the right edge.
- **Signature, the breaker panel:** ten breakers, each one item from their own "we specialize in" list. Flip a breaker and the bulb lights, showing that job in their words with a link to the right service page. The main switch lights every circuit.
- **Other home sections:** three service "doors" with their own job photos, the free consult in three steps, three Google reviews, and FAQ.
- **Service pages:** every section title and paragraph from their pages is kept, with a contents list added.
- **References** (screenshotted 21 Oct 2026): Flos, Enphase and Rivian. Lutron and Tesla blocked the screenshot.

## Facts used (from their site)
- **Phone and email:** (385) 284-0394 and info@ezelectric.com.
- **Hours:** Monday to Friday, 8 AM to 6 PM.
- **Service area:** Salt Lake County and Utah County.
- **What they offer:**
  - licensed electricians
  - free quotes
  - a free in-person consultation (safety check and load analysis) and a zero-cost evaluation
  - fast responses and upfront pricing
- **Services:** all the services listed on their pages.
- **Reviews:** three Google reviews, quoted word for word.

## Flags
- **Two phone numbers.** The header and contact page show (385) 284-0394. The footer, the accessibility statement and Google show (385) 220-7815. The draft uses 284-0394; ask which number is main.
- **Template placeholder.** The third review was labelled "CEO, Acme Industries", which is template filler. The label is dropped; the name is kept.
- **Claims left out until confirmed:** "over 15 years", "top-rated", "Quality Work, Guaranteed" and "certified". "Licensed" is kept.
- **Not shown:** the Google rating (4.9 from 641) and any address (service-area business).
- **Photos:** only their three job photos are used. The stock photos are dropped.

## New blog post
`blog/winter-electrical-safety-utah` (1,076 words).
- **Sources:**
  - NFPA, *Home Fires Involving Heating Equipment* (2011–2015 data, via OH&S)
  - CPSC holiday decorating release (December 2017)
- **Keyword check:** it doesn't compete with any service keyword.

## QA
- 8 pages, 0 issues.
- Every image has alt text and dimensions.
- No horizontal scroll at 390px.
- Mobile header fix applied; menu checked.
