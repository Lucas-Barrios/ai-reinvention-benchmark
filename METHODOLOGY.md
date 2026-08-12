# Methodology

**AI Reinvention Benchmark — European Industrial Machinery**

Framework version 1.1, adopted 2026-08-12, before any company was assessed.

---

## 1. Research question

Where do eight European industrial machinery manufacturers stand on AI maturity,
judged strictly on what they have published, and which dimension represents the
largest reinvention opportunity for the sector?

## 2. What a score means

**Scores measure evidence of public disclosure. They do not measure internal
capability.**

This distinction is not a disclaimer, it is the definition of the instrument. A
company scoring 1 on agentic deployment has not demonstrated publicly that it
deploys agents. It may deploy them extensively and say nothing. A company scoring
5 has communicated a position clearly and quantitatively.

Every statement in this repository is a statement about published material.
Nothing here should be read as an assertion about what happens inside any
company.

## 3. The framework

Six dimensions, weighted, each scored 0 to 5 against anchored descriptors. The
full framework with definitions, evidence sources and all thirty-six anchors is
in [`data/dimensions.yaml`](data/dimensions.yaml).

| Dimension | Weight |
|---|---|
| Data foundation | 0.20 |
| Process automation depth | 0.15 |
| Agentic and generative AI deployment | 0.25 |
| AI governance readiness | 0.15 |
| Workforce enablement | 0.10 |
| Disclosed measurable outcomes | 0.15 |

### 3.1 The weighting argument

Weights are a judgement about what separates leaders from followers in this
sector today. The reasoning:

**Agentic and generative AI deployment carries the most weight (0.25)** because
it has the widest gap between announcement and operation. Nearly every firm in
the sector has said something about generative AI. Far fewer have put it into
production with real users. That gap is the most discriminating signal available.

**Data foundation carries 0.20** because it is the binding constraint. Sector
firms hold decades of plant, product and service data across incompatible
systems, and no amount of model sophistication compensates for that. A firm
strong here has optionality; a firm weak here does not, whatever else it claims.

**Governance readiness and disclosed outcomes each carry 0.15.** Governance
because the EU AI Act converts it from reputation into compliance, and because
much of the sector's AI value sits in safety-relevant and regulated processes
where ungoverned deployment is not an option. Disclosed outcomes because
publishing a number with a baseline is the strongest signal an outside observer
can get that a deployment is real and measured.

**Process automation depth carries 0.15.** It matters, but it is partly a
consequence of data foundation rather than an independent capability, so
weighting it equally would double-count.

**Workforce enablement carries the least (0.10).** Not because adoption matters
least, it usually decides success, but because public disclosure on it is the
least comparable across firms. Training figures are reported inconsistently and
often bundled into unrelated sustainability metrics, so the evidence supports
fewer defensible distinctions than the other five dimensions.

**Weights are contestable and exposed as such.** The published explorer lets any
reader substitute their own weights and see the ranking change. If a conclusion
survives only under one weighting, that is visible rather than hidden.

## 4. Evidence standard

Every score requires a recorded evidence entry containing:

| Field | Requirement |
|---|---|
| Quotation or specific reference | Direct text, or a precise pointer to the passage |
| Source URL | Publicly reachable at time of assessment |
| Publication date | As stated by the source |
| Document type | Annual report, press release, product announcement, careers page, interview, conference material |

**A score with no evidence entry is recorded as 0.** It is never estimated,
inferred from company size, or carried across from a related dimension.

### 4.1 Source hierarchy

Where sources conflict, the more accountable document wins:

1. Annual, integrated and sustainability reports
2. Investor and capital markets material
3. Official press releases and published policies
4. Product and platform announcements
5. Named-employee technical material, conference talks, engineering blogs
6. Careers pages and job advertisements

Third-party press coverage is used only to locate primary sources, never as
evidence on its own. Vendor case studies about a company are treated as level 4
at best, since the vendor has an interest in the claim.

### 4.2 Assessment window

Sources published from **January 2024 onward**. Older material is used only for
context, never for scoring, because AI capability disclosure before 2024 is not
comparable with what followed.

## 5. Scoring procedure

For each company, for each dimension:

1. Search the source types listed for that dimension in `dimensions.yaml`
2. Record every relevant piece of evidence with its metadata
3. Compare the strongest evidence against the anchored descriptors
4. Record the score, the deciding evidence, and any ambiguity

**Tie-break rule.** Where evidence sits ambiguously between two levels, the
**lower** level is recorded and the ambiguity is noted in the assessment file.
Unconscious inflation is the standard failure of a self-authored benchmark; this
rule pre-commits against it in public.

**Absence of evidence is scored, and it is scored as absence.** It is not treated
as a reason to skip the dimension or to interpolate from neighbouring scores.

## 6. Peer set

Eight European manufacturers, selected on three criteria: primary business in
industrial machinery or equipment, European headquarters, and sufficient public
disclosure to score honestly.

The set is listed in [`data/companies.yaml`](data/companies.yaml) with the
rationale for each inclusion.

**Substitution policy.** If a company's disclosure proves too thin to score, it
is replaced, and the substitution together with the reason is recorded in section
9 of this document. Substitutions are never made silently.

## 7. Limitations

Stated plainly, because a benchmark that hides its weaknesses invites someone
else to find them.

**Disclosure bias.** Large listed companies disclose more than smaller or
privately held ones. TRUMPF is privately held and discloses less than Siemens as
a matter of structure, not of capability. This benchmark measures communication
practice as much as it measures maturity, and the two are correlated but not
identical.

**Size heterogeneity.** Siemens is far larger and more diversified than Krones.
Comparing their AI maturity on a single scale is informative about disclosure
posture, less informative about like-for-like operational capability.

**Single assessor.** All scores were assigned by one person. There is no
inter-rater reliability check. Anchored descriptors and published evidence
mitigate this, and allow any reader to disagree with a specific score rather than
with the whole instrument, but they do not eliminate it.

**Language coverage.** Sources in German and English only.

**Point in time.** A snapshot. Disclosure in this area changes quickly, and
scores are dated accordingly.

**No verification.** Nothing published by a company has been independently
confirmed. A claim in an annual report is treated as evidence that the claim was
made, not that it is accurate.

**Recency asymmetry.** Recent disclosures are easier to find than older ones,
which may slightly favour firms that have communicated actively in the last
twelve months.

## 8. Use of AI in producing this work

Stated openly, because the honest answer is more interesting than the alternative
and because the distinction between accelerated and generated matters.

**AI-accelerated:**
- Source discovery across annual reports, press releases and technical material
- Extraction of candidate evidence passages from long documents
- Drafting and editing of narrative sections
- Structuring and validating the data files

**Human judgement, not delegated:**
- Selection of dimensions and the weighting argument
- Design of the anchored descriptors and the tie-break rule
- Every scoring decision, including which evidence is decisive
- Peer set selection
- The reinvention opportunity analysis and the AX design specification

The rubric was fixed before any evidence was gathered, which constrains how much
the acceleration can influence the outcome. The git history shows that ordering.

## 9. Framework version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-12 | Six dimensions, weights, definitions and evidence sources defined |
| 1.1 | 2026-08-12 | Anchored descriptors added for all dimensions; generic ladder and tie-break rule introduced |

Substitutions to the peer set and any post-assessment amendment to the framework
are recorded here.

## 10. Independence

This work was produced independently. There is no commercial relationship,
current or past, between the author and any assessed company, and no company was
contacted, consulted or given sight of the assessment before publication.

## 11. Reproducibility

Every input is a public document and every score carries its source. To verify
any score, open the relevant file in `data/assessments/`, follow the URL, and
compare the quoted passage against the anchor in `data/dimensions.yaml`.

To recompute the results:

```bash
pip install -r requirements.txt
pytest
python -m src.report
```

Disagreement with a specific score is expected and welcome. The framework is
built so that disagreement can be precise.
