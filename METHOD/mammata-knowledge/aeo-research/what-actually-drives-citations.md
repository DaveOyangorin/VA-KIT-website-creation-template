> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# What actually drives AI citations — the evidence

Findings taken from paper abstracts, not from vendor blog summaries. Each is tagged with its
arXiv ID so it can be cited in a client deliverable. See [papers.md](papers.md).

## The strongest controlled result

**`2605.25517` — What Gets Cited: Competitive GEO in AI Answer Engines (2026).**
252,000 trials across six LLMs. Two candidate documents injected into context differing in
exactly one factor at a time, with brand anonymisation and counterbalanced order to strip out
position bias. Which gets cited first?

| Effect | Factor |
|---|---|
| **Biggest drivers** | Topical relevance; list position |
| **Consistent smaller gains** | Explicit price information; a recent timestamp |
| **Smaller still** | Completeness and trust cues |
| **Little effect** | **Formatting-only edits** |

This is the most useful single finding in the whole list, because it contradicts a large amount
of AEO advice being sold right now. **Restructuring a page's formatting without changing its
topical relevance is not an evidence-backed intervention.** Putting a real price on the page and
keeping a genuine recent date is.

## Citation is two stages, not one

**`2604.25707` — From Citation Selection to Citation Absorption (2026).**
602 controlled prompts across ChatGPT, Google AI Overview/Gemini and Perplexity; 21,143
search-layer citations; 18,151 pages fetched; 72 features extracted.

- **Selection** — the engine triggers a search and picks sources.
- **Absorption** — a cited page actually contributes language, evidence or structure to the answer.

Breadth and depth diverge: Perplexity and Google cite *more* sources on average; ChatGPT cites
*fewer* but with substantially higher influence per cited page. High-influence pages are
**longer, more structured, semantically aligned, and richer in extractable evidence**.

Practical read: being listed as a citation is not the win. Being the page the answer is built
from is. Optimise for extractable evidence — concrete facts, figures, named entities — not for
appearing in a list.

## Structure does matter, but at the right level

**`2603.29979` — Structural Feature Engineering for GEO (2026).**
Decomposes structure into macro (document architecture), meso (information chunking) and micro
(visual emphasis), and shows consistent citation improvements across six engines. Read alongside
`2605.25517` above: structure helps when it improves chunking and semantic alignment, not when it
is cosmetic reformatting.

## Authority signals — relevant to our health clients

**`2601.17109` — Authority Signals in AI Cited Health Sources (2026).**
100 questions from Google Research's HealthSearchQA run through ChatGPT 5.2 Pro. Four domains:
*Who wrote it?* (author credentials) · *Who published it?* (institutional affiliation) ·
*How was it vetted?* (quality assurance) · *How does AI find it?* (digital authority).

Applies directly to **a chiropractic client's site**. An unattributed clinical page is a citation problem.

## Expectation setting

**`2606.20065` — GEO at Scale (2026).** 100K+ prompt responses, 100+ brands, March–May 2026.
A three-tier brand-stature ladder: global household names appear in ~73% of relevant AI answers
on the first run; established mid-market and regional brands substantially lower. The paper
explicitly frames the hard case as SMEs, D2C brands and early-stage startups — Novarte's clients.

**`2506.11097` — C-SEO Bench (2025).** Existing AEO evaluations assume one actor adopts the
tactic. Under multi-actor adoption — which is where the market is heading — measured gains erode.

Use both when a client asks "will this get us cited". The honest answer is: it improves the odds
from a low base, and the advantage shrinks as competitors adopt the same tactics.

## Risks worth knowing

- **`2602.16136` — Retrieval Collapses When AI Pollutes the Web** and **`2606.13610` — One
  Polluted Page Is Enough.** Mass-produced AI content degrades generative retrieval, and a single
  polluted page can be enough. An argument against volume-first AI content programmes.
- **`2606.12439` — Position: GEO Creates Underexamined Risks.** Governance and risk framing.
- **`2606.11216` — Great Disappearance Acts: Generative Search and Shadow Banning.**

## The foundation

**`2311.09735` — GEO: Generative Engine Optimization (2023, 82 citations).** The paper that named
the field. Read it before quoting anyone else's framework.
