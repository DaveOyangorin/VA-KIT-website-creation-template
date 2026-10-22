> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# How MAMMATA measures AI visibility — the standard

**This supersedes single-run AI-visibility reporting.** Source:
`arXiv 2603.08924`, *Quantifying Uncertainty in AI Visibility* (Sielinski, 2026), plus
`2606.04362` and `2606.20065`. See [papers.md](papers.md).

## The problem with what we do now

`aio_citation_check.py` and the `_llm_probes` scripts ask each query **once** and record whether
the client was cited. The paper's finding is that this is not a measurement — it is one draw from
a distribution.

The empirical result, across Perplexity, OpenAI SearchGPT and Google Gemini, sampled daily over
nine days and at ten-minute intervals:

- Identical queries at different times return **different answers citing different sources**.
- Citation distributions follow a **power law** with substantial variance across repeated samples.
- **Bootstrap confidence intervals show many apparent differences between domains fall inside
  measurement noise.**

So "the client was cited last month and isn't now" is, on a single run each, very often nothing
at all. Reporting it as a change is inventing a metric — which Golden Rule 1 forbids.

## The standard

1. **Never report an AI-visibility number from a single run.** Not in an audit, not in a
   proof-of-value report, not in a Telegram reply.
2. **Resample.** Run each prompt K times (K=3 minimum; more for a headline claim). Report the
   citation rate across runs, not a yes/no.
3. **Report the interval, not just the point.** "Cited in 2 of 6 runs" is honest. "Cited: yes" is
   not. Where the sample supports it, give a bootstrap interval.
4. **Separate the two variances.** Between-question variance (different prompts genuinely differ
   — 60% vs 20% mention rates) is signal. Within-question variance (the same prompt varying run
   to run) is noise. Never let noise be reported as a trend.
5. **Movement needs three consecutive significant runs** before it counts as a change worth
   telling a client about.
6. **Say the sample size.** Every AI-visibility figure in a deliverable carries how many prompts
   and how many runs produced it. An unqualified percentage is not reportable.
7. **Log the exact prompts.** Different phrasings of "the same" question are different questions
   statistically. Reuse the prompt set across periods or the comparison is meaningless.

## Sample size

The source list's vendor tool suggests: at 95% confidence, ±2% margin, K=3 resamples ≈ **353
unique prompts × 3 = 1,059 API calls**. That is a research-grade budget, not a client-audit
budget. Treat it as the ceiling, not the target.

For Novarte's local clients the practical floor is **10–15 real buyer prompts × 3 runs**. State
plainly in the report that the margin at that size is wide and the result is directional.
Do not dress a 15-prompt sample as a measurement of "AI visibility" in general.

## One measurement trap worth knowing

Testing in a logged-out/incognito session does not reproduce what real users see — logged-in
ChatGPT has web-search tools that incognito sessions lack. Domains showing a 0% citation rate in
incognito testing can show several percent under real conditions. Whatever harness we use, record
which condition it tested, and never compare numbers taken under different conditions.
*(This one comes from the vendor's own blog, not a peer-reviewed paper — treat as a hypothesis to
verify, not established fact.)*

## What this changes in the code

- `aio_citation_check.py` — add a `--runs N` loop and report per-query citation rate with the run
  count, instead of a boolean.
- The `_llm_probes` / `_llm_mentions` pull scripts — same: resample, store every run, aggregate.
- Any audit template section reporting AI visibility — add sample size and run count next to the
  figure.

Not yet implemented. Scoped 2026-08-19.
