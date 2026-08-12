# AI Reinvention Benchmark — European Industrial Machinery

An evidence-based benchmark of AI maturity across eight European industrial
machinery manufacturers, scored from public disclosure against a rubric fixed
before any company was assessed.

**Status: in progress.** See [`CHARTER.md`](CHARTER.md) for scope, method and
delivery phases.

---

## What this is

A desk study. Every input is a public document: annual and sustainability
reports, press releases, product announcements, careers pages. No interviews,
no client data, no privileged access.

**Scores measure evidence of public disclosure, not internal capability.** A
company scoring low may be doing excellent work it has chosen not to publish.

## Why it is structured this way

Three properties, each verifiable from the repository itself:

1. **The rubric precedes the data.** Dimensions, weights and anchored
   descriptors were committed before the first company was assessed. The git
   history shows the order.
2. **Every score carries its evidence.** Each score is stored alongside a
   quotation, a source URL, a publication date and the document type.
3. **Weighting is exposed as a judgement.** The published app lets any reader
   substitute their own weights and watch the ranking change.

## Repository map

| Path | Contents |
|---|---|
| `CHARTER.md` | Scope, peer set, integrity commitments, definition of done |
| `METHODOLOGY.md` | Rubric, evidence standard, limitations, AI-acceleration note |
| `data/` | Dimensions, weights, peer set, and per-company assessments |
| `src/` | Data loading, validation and the scoring engine |
| `tests/` | Tests for the scoring mathematics |
| `analysis/` | Trends, findings, opportunity map, AX design specification |
| `app.py` | Interactive benchmark explorer |

## Licence

Code under MIT. Analysis and assessment data under CC BY 4.0. See [`LICENSE`](LICENSE).
