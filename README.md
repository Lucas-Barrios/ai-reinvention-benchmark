# AI Reinvention Benchmark: European Industrial Machinery

**Live explorer:** https://ai-reinvention-benchmark.streamlit.app

An evidence-based benchmark of AI maturity across eight European industrial
machinery manufacturers, scored from public disclosure against a rubric fixed
before any company was assessed.

**Scores measure evidence of public disclosure of a company's own AI adoption,
not internal capability and not products sold.** A company scoring low may run
extensive internal AI it has chosen not to publish.

---

## Headline finding

Across all eight companies, and two full search passes, **not one publishes a
quantified result from its own AI use.** These firms publish precise figures
constantly, but every figure attaches to a product's performance or a customer's
outcome. The sector has begun to run on AI and has not yet begun to measure and
disclose what that is worth to it.

The finding survived a targeted re-run that actively hunted for internal
outcomes. Disclosed measurable outcomes remains the weakest dimension in the set.

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

Dimensions: **Data** foundation, **Proc**ess automation depth, **Agentic** and
generative AI deployment, **Govern**ance readiness, **Workforce** enablement,
disclosed measurable **Outcomes**. Percentage is of the theoretical maximum and
is a reading aid, not a target. The interactive explorer lets you reweight the
dimensions and see whether the ranking survives.

## Why it is structured this way

Three properties, each verifiable from the repository itself:

1. **The rubric precedes the data.** Dimensions, weights and anchored
   descriptors were committed before the first company was assessed. The git
   history shows the order.
2. **Every score carries its evidence.** Each is stored with a quotation, a
   source URL, a publication or retrieval date and the document type, in
   `data/assessments/`.
3. **Weighting is exposed as a judgement.** The published app lets any reader
   substitute their own weights and watch the ranking change.

The framework was amended five times during the work, each time in the open with
the reasoning attached, including two score corrections the process caught in
itself. A benchmark's credibility does not come from being right first time; it
comes from the corrections being visible. See `METHODOLOGY.md` section 9.

## Read the analysis

| Document | Contents |
|---|---|
| [`analysis/01-trends-and-forces.md`](analysis/01-trends-and-forces.md) | Six forces shaping AI adoption in the sector |
| [`analysis/02-benchmark-findings.md`](analysis/02-benchmark-findings.md) | Six findings from the scoring, with a what-this-does-not-show section |
| [`analysis/03-reinvention-opportunities.md`](analysis/03-reinvention-opportunities.md) | The weakest dimensions mapped to concrete process economics |
| [`analysis/04-ax-design-spec.md`](analysis/04-ax-design-spec.md) | One process specified as an agentic redesign, with human oversight under EU AI Act Article 14 |

## Repository map

| Path | Contents |
|---|---|
| `CHARTER.md` | Scope, peer set, integrity commitments |
| `METHODOLOGY.md` | Rubric, evidence standard, search protocol, limitations, amendment log |
| `data/dimensions.yaml` | The six dimensions, weights and anchored 0..5 descriptors |
| `data/assessments/` | One evidence file per company |
| `src/` | Data model, validation and the scoring engine |
| `tests/` | Tests for the scoring mathematics and the real data |
| `analysis/` | The four-part written analysis |
| `app.py` | Interactive explorer |

## Reproduce it

```bash
pip install -e ".[dev]"
pytest                 # 34 tests: validation, arithmetic, ranking, real data
python -m src.report   # recompute the leaderboard from the evidence files
streamlit run app.py   # the interactive explorer, locally
```

Every published number can be recomputed from the evidence with `python -m
src.report`. Disagreement with a specific score is expected and welcome; the
framework is built so that disagreement can be precise.

## Licence

Code under MIT. Analysis and assessment data under CC BY 4.0. See [`LICENSE`](LICENSE).
