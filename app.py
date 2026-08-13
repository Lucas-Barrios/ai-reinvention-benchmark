"""AI Reinvention Benchmark: interactive explorer.

A thin presentation layer over the scoring engine in src/. The engine loads and
validates the evidence files and computes every number; this app only displays
them and lets a reader substitute their own dimension weights to see whether a
ranking survives. The reweighting is the honesty feature promised in
METHODOLOGY: the published weights are a judgement, and the reader can overrule
them here.

Run locally:  streamlit run app.py
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.model import load_assessments, load_framework
from src.scoring import SCORE_MAX

st.set_page_config(
    page_title="AI Reinvention Benchmark",
    page_icon="B",
    layout="wide",
)


@st.cache_data
def load():
    framework = load_framework()
    assessments = load_assessments(framework)
    dims = [(d.id, d.name, d.weight) for d in framework.dimensions]
    rows = []
    for a in assessments:
        sm = a.score_map()
        rows.append({"company": a.company_name, "id": a.company_id, **sm})
    # per-company evidence, kept for the drill-down
    evidence = {}
    for a in assessments:
        evidence[a.company_name] = a.scores
    return dims, pd.DataFrame(rows), evidence


DIMS, DF, EVIDENCE = load()
DIM_IDS = [d[0] for d in DIMS]
DIM_NAMES = {d[0]: d[1] for d in DIMS}
DEFAULT_WEIGHTS = {d[0]: d[2] for d in DIMS}


def weighted(df: pd.DataFrame, weights: dict[str, float]) -> pd.DataFrame:
    out = df.copy()
    out["total"] = sum(out[d] * w for d, w in weights.items())
    out["percent"] = out["total"] / SCORE_MAX * 100
    return out.sort_values(["total", "company"], ascending=[False, True])


# --------------------------------------------------------------------------- #
# Header
# --------------------------------------------------------------------------- #

st.title("AI Reinvention Benchmark")
st.caption(
    "AI maturity of eight European industrial machinery manufacturers, scored "
    "from public disclosure against a rubric fixed before assessment. "
    "Scores measure evidence of disclosure of a company's own AI adoption, "
    "not internal capability and not products sold."
)

st.info(
    "**Headline finding.** Across all eight companies, not one publishes a "
    "quantified result from its own AI use. Disclosed measurable outcomes is "
    "the weakest dimension in the set. Every other figure these firms publish "
    "attaches to a product or a customer."
)

# --------------------------------------------------------------------------- #
# Sidebar: reweighting
# --------------------------------------------------------------------------- #

st.sidebar.header("Reweight the dimensions")
st.sidebar.caption(
    "The published weights are a judgement. Move the sliders to apply your own "
    "and see whether the ranking survives. Values are normalised to sum to 1."
)

raw = {}
for did in DIM_IDS:
    raw[did] = st.sidebar.slider(
        DIM_NAMES[did],
        min_value=0.0,
        max_value=1.0,
        value=float(DEFAULT_WEIGHTS[did]),
        step=0.05,
    )
total_raw = sum(raw.values()) or 1.0
weights = {d: v / total_raw for d, v in raw.items()}

if st.sidebar.button("Reset to published weights"):
    st.rerun()

st.sidebar.markdown("**Applied weights (normalised)**")
for did in DIM_IDS:
    st.sidebar.write(f"{DIM_NAMES[did]}: {weights[did]:.2f}")

# --------------------------------------------------------------------------- #
# Leaderboard
# --------------------------------------------------------------------------- #

ranked = weighted(DF, weights)
changed = weights != DEFAULT_WEIGHTS

st.subheader("Ranking" + (" (your weights)" if changed else " (published weights)"))

display = ranked[["company"] + DIM_IDS + ["total", "percent"]].copy()
display = display.rename(columns={d: DIM_NAMES[d][:14] for d in DIM_IDS})
display["total"] = display["total"].round(2)
display["percent"] = display["percent"].round(0).astype(int).astype(str) + "%"
st.dataframe(display, hide_index=True, use_container_width=True)

fig = go.Figure(
    go.Bar(
        x=ranked["percent"],
        y=ranked["company"],
        orientation="h",
        text=ranked["percent"].round(0).astype(int).astype(str) + "%",
        textposition="auto",
    )
)
fig.update_layout(
    height=380,
    xaxis_title="% of theoretical maximum",
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------------------------------- #
# Company drill-down: the evidence trail
# --------------------------------------------------------------------------- #

st.subheader("Evidence trail")
st.caption(
    "Every score traces to a quotation, a source and a date. Pick a company to "
    "see the reasoning and evidence behind each of its six scores."
)

company = st.selectbox("Company", ranked["company"].tolist())
for score in EVIDENCE[company]:
    dim_name = DIM_NAMES.get(score.dimension, score.dimension)
    with st.expander(f"{dim_name}  ·  score {score.score}"):
        data = score.model_dump()
        if data.get("anchor_applied"):
            st.markdown(f"**Anchor applied:** {data['anchor_applied']}")
        if data.get("rationale"):
            st.markdown(f"**Rationale:** {data['rationale']}")
        ev = data.get("evidence") or []
        for e in ev:
            quote = e.get("quote") or e.get("finding") or ""
            src = e.get("source_url", "")
            when = e.get("published") or e.get("retrieved") or ""
            if quote:
                st.markdown(f"> {quote}")
            meta = " · ".join(x for x in [when, src] if x)
            if meta:
                st.caption(meta)

st.divider()
st.caption(
    "Scores measure public disclosure, not internal capability. A low score "
    "may mean a company runs extensive internal AI it has not published. "
    "Full method and limitations in METHODOLOGY.md. Recompute any number with "
    "`python -m src.report`."
)
