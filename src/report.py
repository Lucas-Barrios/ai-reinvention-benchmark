"""Command-line report: the same table the analysis is built on.

Run `python -m src.report` to reproduce the leaderboard, the per-dimension
means and ranges, and the headline finding, directly from the evidence files.
This is the reproducibility path referenced in METHODOLOGY.md: anyone can
recompute the published numbers without trusting a spreadsheet.
"""

from __future__ import annotations

from .model import load_assessments, load_framework
from .scoring import dimension_means, dimension_ranges, rank

BAR = "-" * 72


def _dimension_labels(framework) -> dict[str, str]:
    return {d.id: d.name for d in framework.dimensions}


def leaderboard_lines(assessments, framework) -> list[str]:
    labels = _dimension_labels(framework)
    ids = framework.ids
    header = f"{'company':<30}" + "".join(f"{i[:4]:>5}" for i in ids)
    header += f"{'total':>8}{'%':>6}"
    lines = [header, BAR]
    for r in rank(assessments, framework):
        row = f"{r.company_name:<30}"
        row += "".join(f"{r.scores[i]:>5}" for i in ids)
        row += f"{r.weighted_total:>8.2f}{r.percent:>5.0f}%"
        lines.append(row)
    lines.append(BAR)
    lines.append("dimension key: " + ", ".join(f"{i[:4]}={labels[i]}" for i in ids))
    return lines


def dimension_lines(assessments, framework) -> list[str]:
    labels = _dimension_labels(framework)
    means = dimension_means(assessments, framework)
    ranges = dimension_ranges(assessments, framework)
    lines = ["Per-dimension summary (raw scores, unweighted):"]
    for dim in framework.ids:
        lo, hi = ranges[dim]
        lines.append(
            f"  {labels[dim]:<34} mean {means[dim]:.2f}   range {lo}-{hi}"
        )
    return lines


def headline_lines(assessments, framework) -> list[str]:
    """State the central finding as the data supports it, not as an assertion."""
    means = dimension_means(assessments, framework)
    ranges = dimension_ranges(assessments, framework)
    outcomes_id = "disclosed_outcomes"
    lines = ["Headline check:"]
    if outcomes_id in means:
        lo, hi = ranges[outcomes_id]
        lines.append(
            f"  Disclosed measurable outcomes: mean {means[outcomes_id]:.2f}, "
            f"range {lo}-{hi} across {len(assessments)} companies."
        )
        if hi <= 1:
            lines.append(
                "  No company scores above 1: none publishes a quantified "
                "result from its own AI use."
            )
    return lines


def build_report() -> str:
    framework = load_framework()
    assessments = load_assessments(framework)
    blocks = [
        f"AI Reinvention Benchmark  |  framework {framework.version}  "
        f"|  {len(assessments)} companies",
        "",
        "\n".join(leaderboard_lines(assessments, framework)),
        "",
        "\n".join(dimension_lines(assessments, framework)),
        "",
        "\n".join(headline_lines(assessments, framework)),
    ]
    return "\n".join(blocks)


def main() -> None:
    print(build_report())


if __name__ == "__main__":
    main()
