# Reinvention opportunity map

*Part 3 of 4. Builds on the benchmark findings (02) and sets up the AX design
specification (04).*

Benchmarking that stops at scores describes a gap without acting on it. This
section takes the two weakest dimensions in the set and names where, in a
specific operating process, agentic AI would change the economics, and what it
would be worth. It connects the "where the sector stands" of part 2 to the "here
is the concrete redesign" of part 4.

The two lowest-scoring dimensions across the eight companies are **data
foundation** (mean 0.88) and **disclosed measurable outcomes** (mean 0.75).
They are not independent weaknesses; they are the two ends of the same missing
loop. Without a consolidated data foundation there is nothing to measure from,
and without measurement there is no evidence the investment worked. Reinvention
in this sector is, first, closing that loop.

---

## Where the value concentrates

The trends assessment (part 1) found that the sector's most credible internal
AI use is knowledge-access and knowledge-retention, driven by skilled-labour
scarcity, rather than automation for headcount. That points the opportunity at a
specific class of process: **high-volume, judgement-heavy, knowledge-dependent
operating processes where the expert is not always available.**

Three such processes recur across the assessed companies' own disclosures.

### 1. Aftersales spare-parts quoting

The strongest opportunity, and the subject of part 4.

Machinery firms carry vast catalogues of models, variants and components. A
customer request for a spare part, or for a quote to refurbish or extend a
line, requires someone to identify the right parts, check compatibility across
machine generations, price them against current cost and lead-time data, and
produce a quote. Krones discloses exactly this pain in its own quoting process:
"it can take as long as several weeks for a customer to receive a finished
quote", and it is piloting AI to cut that "to mere hours" (Krones magazine,
January 2024).

Why the economics move: the process is high-volume, rules-heavy with genuine
judgement at the edges, and directly revenue-bearing, a slow quote is a lost
aftersales sale. It is also knowledge-dependent in exactly the way the sector's
labour-scarcity problem bites: the person who knows which part fits which
machine generation may have left. This is where an agentic redesign has the
clearest and most defensible payoff, which is why part 4 specifies it in full.

### 2. Service-ticket routing and triage

Heidelberger already runs AI-based routing of roughly 220,000 service tickets a
year to the service staff best matched to each fault (Heidelberg annual report,
2026), and KION applies its MERLIN tool to classifying maintenance reports. The
opportunity here is less about first deployment, some firms have it, and more
about depth: moving from routing and classification to agentic resolution, where
the system drafts the response, proposes the fix, and escalates only the cases
that need a human. The economics are attractive because ticket volume is high
and the marginal cost of a mis-routed or slow ticket is a service-level miss.

### 3. Requirements-to-configuration in complex order handling

Dürr's excluded evidence pointed at automating quotation creation, customer
dialogues and ticket handling; TRUMPF names configuration as an AI target. The
broader opportunity is translating a customer's stated requirements into a
validated machine or line configuration, a process that today consumes
experienced application-engineering time. It is harder to specify than quoting
because the judgement is deeper, which is why quoting, not configuration, is the
right first target for a worked specification.

---

## The two-part prize

For a firm in this sector, the reinvention opportunity has two components, and
the benchmark shows most have addressed neither.

**Close the measurement loop (the disclosed-outcomes gap).** The first firm to
instrument an internal AI process properly, and to publish a credible achieved
figure, gains twice: internally, it learns whether the investment worked and can
direct the next one; externally, it publishes into an empty field, since no peer
yet does. The cost is modest, it is instrumentation of a process the firm
already runs, and the benchmark shows the competitive space is wide open.

**Build the foundation the rest depends on (the data-foundation gap).** The
weakest dimension gates the others. A consolidated view of parts, machine
configurations, service history and current cost and lead-time data is the
precondition for every one of the three processes above. This is unglamorous and
expensive and it is the real constraint; a firm that treats agentic AI as a
layer to add without it will get pilots that do not scale, which is visibly what
several assessed companies have.

---

## From map to specification

Of the three processes, aftersales spare-parts quoting is the one where the
evidence is strongest (a peer discloses the exact pain and a live pilot), the
economics are clearest (high volume, revenue-bearing), and the judgement is
bounded enough to specify precisely. Part 4 does that: it specifies the process
as an agentic redesign, defining what the agent decides alone, the confidence
thresholds at which it acts, what triggers escalation, where a human must
approve before the process continues, and what the audit trail records. That
specification, the level below the opportunity, is where reinvention is either
made real or left as a slogan.
