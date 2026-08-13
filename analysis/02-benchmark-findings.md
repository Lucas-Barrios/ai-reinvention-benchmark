# Benchmark findings

*Part 2 of 4. Reads on from the trends and forces assessment (01).*

Eight European industrial machinery manufacturers, scored on six weighted
dimensions from public disclosure, against a rubric fixed before any company
was assessed. Every score traces to a quotation, a source and a date in
`data/assessments/`. This section states what the scored evidence supports and,
as carefully, what it does not.

---

## The result

| Rank | Company | Data | Proc | Agentic | Govern | Workforce | Outcomes | Weighted | % |
|---|---|---|---|---|---|---|---|---|---|
| 1 | GEA Group | 2 | 2 | 3 | 3 | 2 | 1 | 2.25 | 45% |
| 2 | Krones | 1 | 2 | 2 | 4 | 3 | 1 | 2.05 | 41% |
| 3 | TRUMPF | 1 | 1 | 3 | 3 | 3 | 1 | 2.00 | 40% |
| 4 | Siemens | 1 | 2 | 3 | 3 | 1 | 1 | 1.95 | 39% |
| 5 | KION | 1 | 2 | 3 | 0 | 1 | 1 | 1.50 | 30% |
| 6 | Sandvik | 1 | 1 | 1 | 3 | 1 | 0 | 1.15 | 23% |
| 7 | Heidelberger | 0 | 2 | 0 | 0 | 1 | 1 | 0.55 | 11% |
| 8 | Dürr | 0 | 1 | 0 | 2 | 1 | 0 | 0.55 | 11% |

Scores measure evidence of public disclosure of a company's own AI adoption,
not internal capability and not products sold. The percentage is of the
theoretical maximum; no company could realistically reach it, and the figure
is a reading aid, not a target. Recompute any row with `python -m src.report`.

---

## Finding 1: nobody publishes what their internal AI is worth

The single most robust result. Across all eight companies, the mean disclosed-
outcomes score is 0.75, and no company scores above 1. Not one publishes a
quantified result, an achieved figure with scope or baseline, from AI used in
its own operations.

This is not for want of numbers. The assessment excluded roughly forty pieces
of vendor evidence, many carrying precise figures, because every one attached to
a customer outcome or a product's performance rather than to the company's own
adoption. Siemens publishes a 25% reactive-maintenance figure, but for product
pilots. GEA publishes an 8% spray-drying energy gain, but for customers using
GEA machines. The sector measures and publishes constantly; it simply does not
yet do so for itself.

The finding survived the hardest test available to it. The re-run of four
companies actively hunted for internal outcomes, and the strongest thing it
surfaced, Siemens' Erlangen downtime "significantly reduced", was a qualitative
claim with no figure. It held.

## Finding 2: the sector runs on AI more than it discloses, and sells it far more

The scope rule, assessing each firm as an adopter rather than a vendor, is what
makes the benchmark say anything the trade press does not. Four of the eight
companies, Siemens, Dürr, KION and Sandvik, sell industrial AI. Without the
rule, their product portfolios would dominate and the exercise would become a
catalogue of who sells AI.

With the rule applied, a consistent shape appears: rich, dated, quantified
disclosure of product AI, and thin, often undated, rarely quantified disclosure
of internal AI. The clearest single illustration is that the load-bearing
evidence for several companies sits not in annual reports but in a company blog
(Siemens Erlangen), a magazine feature (Krones), or a single executive
interview (TRUMPF). The formal reporting channels carry the product story; the
internal story, where it exists, is told in softer places.

## Finding 3: governance and deployment are decoupled

The most analytically interesting result is that the two capabilities most
associated with "AI maturity" do not move together.

- **Deploy without govern.** KION runs a generative AI tool in production
  (agentic 3) and discloses no AI governance whatsoever (governance 0). Its
  primary sustainability document returns zero matches for any AI-governance
  term.
- **Govern without deploy.** Krones has the strongest governance in the set,
  an Advisory Council on AI Strategy and explicit EU AI Act preparation
  (governance 4), while its flagship internal use case remained a pilot
  (agentic 2). Sandvik has a Chief AI Officer and a dedicated AI centre
  (governance 3) but discloses no named internal deployment (agentic 1).

No company scores highly on both a governed *and* a deployed footing. The
sector is building the two halves of responsible AI adoption in different orders
and at different speeds. This is precisely why a single composite score would
mislead, and why the framework keeps the dimensions visible.

## Finding 4: data foundation is the binding constraint

Across the set, data foundation is the weakest capability (mean 0.88, the lowest
of the six dimensions bar disclosed outcomes). Only GEA scores above 1, and it
does so because it discloses running an internal tool on a named platform. Most
firms name data as a priority and disclose no consolidated internal data estate
to support it. Krones announced an "overarching data platform" in early 2024 and
no later source confirms it exists two and a half years on.

This matters because data foundation is not an independent weakness; it gates
the others. Agentic and generative systems fail quietly on fragmented data. A
sector that is weakest exactly where its other ambitions depend is telling you
where the real work is, and part 3 builds on this.

## Finding 5: a clustered top, then a cliff

The distribution is not a smooth spectrum. Six companies fall in a 23-to-45%
band; two, Dürr and Heidelberger, sit at 11%, less than half the next lowest.
The low pair is genuine, not an artefact: both were assessed under the full
seven-class search protocol, both publish extensively about product AI, and both
disclose almost nothing about internal adoption. Dürr reaches its score through
governance-agenda attention with no internal deployment; Heidelberger through a
real internal deployment (AI service-ticket routing) with no governance. They
arrive at the same total by opposite routes.

The practical reading is that the sector splits into a group that discloses
*something* about internal AI and a group that discloses essentially nothing,
with little in between. A ranking flattens that; the two-tier structure is the
more useful observation.

## Finding 6: disclosure volume is not maturity, and method decides the score

A methodological finding, and the reason the process is documented as heavily as
the results. On the first pass, TRUMPF, a privately held company that publishes
a fraction of what its listed peers do, outscored Siemens, because a single
interview about its own operations outweighed an entire corporate reporting
suite aimed at customers. Volume of disclosure and relevance of disclosure are
different things, and the benchmark measures the second.

The same lesson caught two of the benchmark's own errors. On re-run, Siemens
rose from 31% to 39% once its Erlangen deployment was read in full rather than
from a page summary, and GEA rose from 39% to 45% once a published AI-governance
policy was found in a document the first pass had not searched. Both corrections
are recorded with the superseded findings retained. A benchmark's credibility
does not come from being right first time; it comes from the corrections being
visible.

---

## What these findings do not show

Stated plainly, because the value of the exercise depends on not overclaiming.

**Not internal reality.** Every finding is about disclosure. A company scoring
low may run extensive internal AI it has chosen not to publish. The sell/run
gap in finding 2 makes this likely rather than hypothetical: true internal
adoption is probably ahead of what any outside assessment can see.

**Not a like-for-like capability contest.** The companies differ greatly in
size and structure. TRUMPF is private and discloses less by nature; Siemens is
vast and diversified. The benchmark measures communication posture as much as
maturity, and the two are correlated but not identical.

**Not a verdict on any company.** These are inputs for a reader's own judgement,
not scores to be quoted as fact. The published explorer lets a reader reweight
the dimensions and watch the ranking move; a conclusion that survives only under
one weighting is visible as such.

**A single-author desk study.** No inter-rater check, sources in German and
English only, a point-in-time snapshot of fast-moving disclosure. The full
limitations are in `METHODOLOGY.md` section 7.
