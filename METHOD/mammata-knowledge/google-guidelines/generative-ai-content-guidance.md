> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# Google: guidance on using generative AI content (revised 2026-10-01)

Source (checked live 2026-10-05, page says "Last updated 2026-10-01 UTC"):
https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
Changelog: https://developers.google.com/search/updates — Oct 1, 2026 "Updated guidance on using generative AI
content" (brought in material from the Search Quality Rater Guidelines / developer-event talks).
Trigger: Edward Sturm ep. 1187 "Google Just Changed Its AI Content Guidelines (Unreviewed AI Is Now a Liability)",
uploaded 2026-10-04, ~23k views/day on 2026-10-05 (transcript: `SEO-DAILY\transcripts\2026-10-05-wxqf9J2Huu0.txt`).
Also covered in FRAVATA briefs 2026-10-02 and 2026-10-03.

## What the page says now (Google's words)
- Gen AI "can be particularly useful when researching a topic, and to add structure to original content."
- Generating "many pages without adding value for users may violate Google's spam policy on scaled content abuse."
- **NEW (Oct 1):** generative models "don't retrieve facts, but predict a likely sequence of words based on their
  training data", so outputs "may contain inaccuracies (also known as hallucinations)."
- **NEW (Oct 1):** "It is critical to manually factcheck and review all AI-generated content for accuracy and
  trustworthiness before publishing." The review **also covers metadata**: page title, meta description,
  structured data, image alt text — because they can show in search results.
- Give users context: say how content was made where readers would expect it; for automated content, explain how
  automation was used and add image metadata.
- Ecommerce (Merchant Center): AI images must carry IPTC `DigitalSourceType` = `TrainedAlgorithmicMedia`;
  AI-generated product titles/descriptions must be specified separately and labeled AI-generated.

## Same week, related (FRAVATA 2026-10-03 brief)
- Google's people-first content guide (updated Oct 1) calls fabricated creator profiles — AI headshots, made-up
  names, false credentials — **deception**.

## From Google's older AI-content FAQ (2023 blog post; quoted by Sturm, not re-checked today)
- Google does not ban AI content; automation has long made helpful content (sports scores, weather, transcripts).
- AI gives no ranking boost or penalty by itself: useful + original + E-E-A-T → may do well.
- Bylines: add accurate ones where readers would ask "who wrote this?". Listing **"AI" as the author is not
  recommended**. AI/automation disclosures where someone would ask "how was this made?".

## Sturm's reading (opinion, label it as his)
- Unreviewed AI at scale is now an explicit, written reason for Google to drop a site ("you are playing with fire").
  Scaled one-shot AI pages "get away with it for a couple of months", then decline sharply or slowly.
- Quotes John Mueller (to a programmatic-SEO site): "our systems have possibly lost faith in your site" after old
  pages dissatisfied searchers. Recovery covered in his ep. 1166.
- Short AI passages are hard to detect; at length (and across many pages/sites) much easier.
- Use AI as a writing assistant, not one-shot full pages: one-shot pages misread search intent, often above the fold;
  proofreading a one-shot page anchors you to the AI's framing.
- Humanize with real images and video; cut AI fluff — decluttered pages convert better (his examples: 2x–15x).
- Detected AI text may be excluded from AI training data (his ep. 1153).

## What it means for the fleet + clients (action)
1. **Every AI draft gets a named human read before it ships** — body AND title, meta description, schema, alt text.
   (Fleet rule already: drafts first, Angelo approves; now it is also Google's written guidance.)
2. **Real authors only.** No AI headshots, invented names or credentials; never "AI" as byline. Check client sites
   for invented team members/bios (cf. an invented-claim mistake we caught once).
3. **No scaled one-shot pages.** City/service page sets must each carry real, specific local facts, then a human edit.
4. Disclosure where readers would expect it (e.g. AI-made images on a product page; automated data pages).
5. Merchant Center clients: AI product images need IPTC TrainedAlgorithmicMedia metadata.
6. Audit check (MAMMATA): sample 5 pages per site for factual errors in titles/meta/schema/alt; flag fake authors.
