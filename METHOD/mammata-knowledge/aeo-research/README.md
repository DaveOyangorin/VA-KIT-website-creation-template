> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# AEO/GEO research reference

Distilled 2026-08-19 from **`github.com/discoveredlabs/awesome-aeo-seo`** — a curated AEO/SEO
resource list. Everything here was independently verified; nothing was copied on trust.

| File | Read it for |
|---|---|
| [`measurement-standard.md`](measurement-standard.md) | **How we measure AI visibility from now on.** The single most important file here |
| [`what-actually-drives-citations.md`](what-actually-drives-citations.md) | Evidence-backed citation drivers, taken from paper abstracts not vendor blogs |
| [`papers.md`](papers.md) | All 35 papers, verified real, with citation counts and Novarte relevance flags |
| [`tooling.md`](tooling.md) | 23 repos, live metadata, cross-referenced against our own hunt file |

## Provenance and the caveat

The source list is well made: 35/35 arXiv IDs resolve to real papers, 23/23 repos exist, and
0 of 56 other links were dead when checked. Annotations are specific and carry honest caveats.
That is far above the norm for the genre.

**But it is published by a vendor.** 25 of its 128 links point at Discovered Labs' own blog, free
tools, and paid AI-visibility monitoring service; two of its four "related lists" are their own
repos. One author, nine commits, nothing pushed since 2026-06-27.

So: **the papers are the asset, the framing is marketing.** When a finding in here goes into a
client deliverable, cite the paper, not the vendor's blog post about the paper. Where something
here comes only from the vendor's blog, it is labelled as such and should be treated as a
hypothesis to verify.

Per [`no-agent-names-in-deliverables`], client work ships as "Novarte AI" — and per Golden Rule 1,
nothing here is a measured metric for a specific client until we have measured it for that client.

## Why this matters to MAMMATA

Our AEO method currently comes from a paid course, i.e. practitioner
opinion. This gives us a **peer-reviewed evidence base** underneath it for the first time, and in
one place it contradicts common practice: controlled trials over 252,000 comparisons find
formatting-only edits have little effect on whether a page gets cited
(`what-actually-drives-citations.md`).

It also exposes a real gap in our own tooling: every AI-visibility number we currently produce
comes from a single run, and the research says single-run numbers are frequently noise.
`measurement-standard.md` is the fix, and it is **scoped but not yet implemented**.
