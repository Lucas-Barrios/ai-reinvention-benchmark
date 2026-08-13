# AX design specification: aftersales spare-parts quoting

*Part 4 of 4. The process identified in the reinvention opportunity map (03),
specified as an agentic redesign.*

This is the level most AI process work skips. It is straightforward to say "use
AI for quoting"; the design decision that determines whether the redesign
survives contact with the people who run the process is the specification of
**what the agent does autonomously, where it must stop, and how a human stays
accountable**. This document specifies exactly that for one process.

It is a design artefact, not an implementation. It is deliberately independent
of any vendor, model or framework, because the autonomy and oversight decisions
below are the durable part; the tooling underneath is not.

---

## 1. Scope and intent

**Process.** Aftersales spare-parts quoting for installed industrial machinery:
from an inbound customer request to a priced, deliverable quote.

**Why this process.** High volume, revenue-bearing, rules-heavy with genuine
judgement at the edges, and knowledge-dependent in exactly the way the sector's
skilled-labour scarcity bites (parts 1 and 3). A peer, Krones, discloses the
pain directly, quotes taking "as long as several weeks", and a live pilot to
cut it "to mere hours".

**Design goal.** Not to remove the human, but to move the human from *producing*
routine quotes to *approving* consequential ones, so that expert time
concentrates where judgement actually adds value, and every quote that reaches a
customer remains a human-accountable act.

**Regulatory frame.** The specification is built to satisfy EU AI Act Article 14
human-oversight requirements as a design property rather than an afterthought:
the points at which a human can understand, intervene in and override the
system are specified before the automation, not bolted on after.

---

## 2. Process decomposition

The quoting process is decomposed into six steps. Each is classified by how much
autonomy the agent may hold, which is the core of the specification.

| # | Step | Agent autonomy |
|---|---|---|
| 1 | Interpret the request | Assist |
| 2 | Identify parts and check compatibility | Act with threshold |
| 3 | Assemble price, cost and lead time | Act with threshold |
| 4 | Compose the quote | Act |
| 5 | Approve and release to customer | **Human only** |
| 6 | Record and learn | Act |

"Assist" means the agent proposes and a human disposes. "Act with threshold"
means the agent proceeds autonomously only above a defined confidence level and
escalates below it. "Act" means the agent proceeds and logs. "Human only" means
the agent may not perform the step under any confidence.

---

## 3. Per-step specification

### Step 1: Interpret the request (Assist)

**What the agent does alone.** Parses the inbound request (email, portal form,
attached photo of a nameplate or worn part) into structured fields: machine
model and serial, affected component, symptom, urgency, customer identity.

**Confidence threshold.** Not applicable; the agent never acts on its
interpretation without the downstream steps validating it.

**Escalation trigger.** If the machine cannot be identified from the request or
the customer record, the request is routed to a human immediately with the
ambiguity flagged. An unidentifiable machine is the single most common source of
a wrong quote and is never guessed.

**Human checkpoint.** None yet; interpretation errors are caught at step 2.

### Step 2: Identify parts and check compatibility (Act with threshold)

**What the agent does alone.** Maps the interpreted request to specific part
numbers, and checks compatibility across the machine's generation and revision
history, this is the knowledge-retention problem the process exists around.

**Confidence threshold.** The agent proceeds autonomously only where part
identification and compatibility both clear a high confidence bar (for example,
an exact serial-to-bill-of-materials match with a single compatible part). Any
of the following forces escalation regardless of nominal confidence:
- more than one compatible part with materially different price,
- a superseded or discontinued part requiring a substitution judgement,
- a compatibility check that depends on an undocumented field modification.

**Escalation trigger.** Below threshold, the case goes to an aftersales engineer
with the agent's candidate parts, its confidence, and the specific reason it
stopped. The agent presents options; it does not choose among consequential
ambiguous ones.

**Human checkpoint.** Escalated cases only. Above threshold the step is logged
and continues.

### Step 3: Assemble price, cost and lead time (Act with threshold)

**What the agent does alone.** Retrieves current list price, current cost, and
current lead time for the identified parts, and assembles the commercial basis
of the quote.

**Confidence threshold.** The agent proceeds only where all inputs are current
and internally consistent. Escalation is forced where:
- price or cost data is stale beyond a defined age,
- lead time exceeds a threshold that changes the customer's decision,
- the assembled margin falls outside the normal band for the part class,
  which usually signals a data error rather than a real deal.

**Escalation trigger.** An out-of-band margin or a stale-data flag routes to a
human with the specific input at fault highlighted. This is the step where a
silent data error becomes a mispriced quote, so the threshold is deliberately
conservative, consistent with the tie-break discipline used throughout the
benchmark: when unsure, stop.

**Human checkpoint.** Escalated cases only.

### Step 4: Compose the quote (Act)

**What the agent does alone.** Assembles the customer-facing quote document from
the validated parts, pricing and lead time, in the firm's standard format, with
the standard terms.

**Confidence threshold.** Not a judgement step; it assembles validated inputs.

**Escalation trigger.** None specific to this step; it inherits any flags raised
upstream.

**Human checkpoint.** None here; the composed quote goes to step 5.

### Step 5: Approve and release to customer (Human only)

**This is the specified human-accountability point, and it is non-negotiable.**

**What the agent may do.** Present the composed quote to the responsible person,
with a decision-ready summary: the parts and why, the confidence at each prior
step, any substitutions made, the margin, and anything the agent escalated or
resolved. The agent may recommend release.

**What the agent may not do.** Send a quote to a customer. No confidence level
authorises autonomous release. Every quote that reaches a customer is released
by a named human who could have declined.

**Why here and not elsewhere.** This is the point at which the process produces
a consequential, externally-visible, commercially-binding output. Under EU AI
Act Article 14, that is exactly where meaningful human oversight must sit: not
distributed vaguely across the process, but located at the step where a person
can review the machine's work in full and stop it before it has effect. Placing
the checkpoint here is what lets every step above run with real autonomy.

For high-volume, low-value, high-confidence quotes a firm may later choose to
raise the autonomy of this step under a separate, explicitly governed policy.
That is a deliberate future decision with its own risk classification, not a
default, and it would be specified as its own change.

### Step 6: Record and learn (Act)

**What the agent does alone.** Records the complete decision trail (section 4)
and captures the outcome: was the quote accepted, edited before release,
declined, or did it win the order. Feeds the outcome back as training signal for
step 2 and step 3 confidence calibration.

**This step is also the answer to finding 1 of the benchmark.** It is where the
process becomes measurable, and therefore where the firm generates the internal
outcome figure that no company in the sector yet publishes. The measurement loop
is designed into the process, not added later.

---

## 4. The audit trail

For every quote, the system records a trail sufficient for a human to
reconstruct why the quote says what it says:

- the parsed request and the confidence of its interpretation,
- the parts identified, alternatives considered, and any substitution with its
  reason,
- the confidence at steps 2 and 3, and every escalation with its trigger,
- the pricing inputs used and their as-of dates,
- the human who approved release, and any edits they made before approving,
- the eventual commercial outcome.

This trail is what turns Article 14 oversight from a claim into a verifiable
property. It is also, deliberately, the data that makes the process auditable to
a customer, defensible to a regulator, and improvable by the firm.

---

## 5. Failure modes and safeguards

| Failure mode | Safeguard |
|---|---|
| Wrong machine identified | Step 1 escalates any unidentifiable machine rather than guessing |
| Wrong or superseded part | Step 2 forces escalation on any substitution judgement |
| Silent mispricing from stale data | Step 3 escalates on stale inputs and out-of-band margin |
| Confident but wrong autonomous action | No step that produces a customer-facing effect is autonomous; step 5 is human-only |
| Automation bias at approval | Step 5 presents the reasoning and confidences, not just the answer, so the human reviews substance rather than rubber-stamping |
| Drift over time | Step 6 feeds real outcomes back into confidence calibration and surfaces rising escalation rates |

The design principle throughout is the one the benchmark applied to its own
scoring: **where the system is unsure, it stops and asks, and it never takes a
consequential action it cannot justify.**

---

## 6. What this specification demonstrates

Most AI process work names the tool and the goal. The value is in the layer
below: the per-step autonomy decisions, the confidence thresholds, the located
human-accountability point, and the audit trail that makes oversight real. That
layer is what determines whether a redesign is adopted by the people who run the
process or quietly abandoned, and it is the discipline this document exists to
show.

It is specified for one process because a real specification is worth more than
a general one. The same method, decompose, classify autonomy per step, set
thresholds, locate the human-only checkpoint, design the audit trail, transfers
directly to service-ticket resolution and order configuration (part 3), and to
any process where an agent acts and a human must remain accountable.
