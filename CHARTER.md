# Project Charter

**AI Reinvention Benchmark — European Industrial Machinery**

---

## Why this exists

European industrial machinery manufacturers are under pressure to show returns on AI investment. Public discussion of that shift is dominated by vendor claims and announcement-stage pilots, and the gap between what firms say and what they have deployed is difficult to see from the outside.

What is scarce is a **comparable, evidence-based view of where firms in the sector actually stand** — built from public disclosure, scored against a rubric fixed in advance, with every number traceable to its source.

This project produces that view for eight European manufacturers, and then does the thing most benchmarks stop short of: it converts the weakest scoring dimension into a specified redesign of one real operational process, down to the level of what an AI agent decides alone and where a human must approve.

## What this is

A **desk study**. Every input is a public document: annual and sustainability reports, press releases, product announcements, careers pages. There are no interviews, no client data, and no privileged access.

This constraint is stated plainly because it defines what the findings can and cannot support.

## Scope

### In scope

| Component | Output |
|---|---|
| Trend and forces assessment | The forces reshaping European industrial machinery, each sourced and dated |
| Peer benchmark | 8 companies scored across 6 weighted dimensions, every score evidenced |
| Reinvention opportunity map | The weakest dimensions mapped to specific process steps and their economics |
| AX design specification | One process specified in full: autonomy boundaries, confidence thresholds, escalation triggers, human handoff, audit trail |
| Interactive explorer | A published app allowing the reader to reweight dimensions and see rankings change |
| Methodology note | Scope, rubric, limitations, and which steps were AI-accelerated |

### Out of scope

Non-European peers. Financial modelling of the opportunity. Primary research, interviews or surveys. Any claim about internal company capability not visible in public disclosure. Predictive scoring or machine learning models.

Ideas arising during the work that fall outside this list are recorded in `BACKLOG.md` rather than absorbed into v1.

## What the scores mean

**Scores measure evidence of public disclosure, not internal capability.**

A company scoring low may be doing excellent work it has chosen not to publish. A company scoring high has demonstrably communicated its position. These are different things, and this document does not conflate them. Every claim in this repository is a claim about what a company has published.

Scoring uses a 0 to 5 scale with anchored descriptors, defined in `data/dimensions.yaml` and explained in `METHODOLOGY.md`.

## Integrity commitments

Three properties this project holds itself to, each verifiable from the repository itself:

**1. The rubric precedes the data.** Dimensions, weights and anchored descriptors are committed before any company is assessed. The git history shows the order. The rubric was not fitted to the results.

**2. Every score carries its evidence.** Each score is stored alongside a direct quotation or specific reference, a source URL, a publication date, and the document type. A score with no evidence is recorded as 0, never estimated.

**3. Weighting is a judgement, and is exposed as one.** The weights reflect a view about what matters in this sector today. That view is documented and argued in `METHODOLOGY.md`, and the published app lets any reader substitute their own weights and see how the ranking changes.

## Assessment dimensions

| Dimension | Weight |
|---|---|
| Data foundation | 0.20 |
| Process automation depth | 0.15 |
| Agentic and generative AI deployment | 0.25 |
| AI governance readiness | 0.15 |
| Workforce enablement | 0.10 |
| Disclosed measurable outcomes | 0.15 |

Full definitions and the reasoning behind the weighting are in `METHODOLOGY.md`.

## Peer set

Eight European industrial manufacturers, selected for sector relevance and disclosure quality.

| Company | Country | Segment |
|---|---|---|
| Siemens AG | DE | Automation and industrial software |
| TRUMPF SE + Co. KG | DE | Machine tools and laser technology |
| GEA Group AG | DE | Process equipment, food and pharmaceutical |
| Krones AG | DE | Filling and packaging machinery |
| Dürr AG | DE | Paint and final assembly systems |
| KION Group AG | DE | Intralogistics and materials handling |
| Heidelberger Druckmaschinen AG | DE | Printing systems |
| Sandvik AB | SE | Machining and mining equipment |

Where a company's disclosure proves too thin to score honestly, it is replaced and the substitution is recorded in `METHODOLOGY.md` rather than handled silently.

## Delivery phases

| Phase | Output |
|---|---|
| 0 | Charter, scope, repository scaffold |
| 1 | Assessment framework: dimensions, weights, anchored descriptors, methodology |
| 2 | Evidence collection, one company at a time |
| 3 | Scoring engine and tests |
| 4 | Analysis: trends, findings, opportunity map, AX design specification |
| 5 | Published interactive explorer |

## Definition of done

- [ ] Eight companies scored across six dimensions, every score evidenced with source and date
- [ ] Rubric committed before the first assessment, verifiable in history
- [ ] Scoring engine tested, tests passing in CI
- [ ] Four analysis documents complete
- [ ] Interactive explorer published and reachable
- [ ] README carries findings and a static scoring table
- [ ] Methodology states desk-study scope, limitations and AI acceleration honestly

---

*Status: in progress. This charter is fixed at the start of the work and amended only by explicit commit.*
