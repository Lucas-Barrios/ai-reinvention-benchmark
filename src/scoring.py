"""Scoring mathematics.

Deliberately pure and dependency-free. Each function takes validated data and
returns a number or an ordered structure, so that any reader can trace a
published figure back to the arithmetic that produced it. Nothing here reads a
file or holds state.

The composite score is a weighted sum of six 0..5 dimension scores. With
weights summing to 1.0, the composite lies in [0, 5]; dividing by 5 expresses
it as a percentage of the theoretical maximum. The percentage is a
presentation convenience, not a claim that any company could realistically
reach 100%.
"""

from __future__ import annotations

from dataclasses import dataclass

from .model import Assessment, Framework, SCORE_MAX


@dataclass(frozen=True)
class Result:
    """A company's composite result. Ordered high-to-low by callers."""

    company_id: str
    company_name: str
    scores: dict[str, int]
    weighted_total: float  # in [0, SCORE_MAX]
    percent: float         # weighted_total / SCORE_MAX * 100


def weighted_total(assessment: Assessment, framework: Framework) -> float:
    """Weighted sum of dimension scores, in [0, SCORE_MAX].

    Raises via framework.weight_of if the assessment carries a dimension the
    framework does not define; assessments are validated on load, so this is a
    guard rather than an expected path.
    """
    scores = assessment.score_map()
    return sum(framework.weight_of(dim) * value for dim, value in scores.items())


def to_percent(total: float) -> float:
    """Express a composite score as a percentage of the maximum."""
    return total / SCORE_MAX * 100.0


def result_for(assessment: Assessment, framework: Framework) -> Result:
    total = weighted_total(assessment, framework)
    return Result(
        company_id=assessment.company_id,
        company_name=assessment.company_name,
        scores=assessment.score_map(),
        weighted_total=total,
        percent=to_percent(total),
    )


def rank(
    assessments: list[Assessment], framework: Framework
) -> list[Result]:
    """Rank companies by weighted total, highest first.

    Ties are broken by company_id so the ordering is deterministic and
    reproducible rather than dependent on input order.
    """
    results = [result_for(a, framework) for a in assessments]
    return sorted(results, key=lambda r: (-r.weighted_total, r.company_id))


def dimension_means(
    assessments: list[Assessment], framework: Framework
) -> dict[str, float]:
    """Mean raw score per dimension across all companies.

    Used to see where the sector as a whole is strong or weak, independent of
    the weighting. Returned in framework dimension order.
    """
    means: dict[str, float] = {}
    for dim in framework.ids:
        values = [a.score_map()[dim] for a in assessments]
        means[dim] = sum(values) / len(values)
    return means


def dimension_ranges(
    assessments: list[Assessment], framework: Framework
) -> dict[str, tuple[int, int]]:
    """Min and max raw score per dimension.

    A dimension whose range spans most of 0..5 is discriminating; one that
    clusters is not. This is the simplest available check that the rubric is
    doing work rather than assigning everyone the same score.
    """
    ranges: dict[str, tuple[int, int]] = {}
    for dim in framework.ids:
        values = [a.score_map()[dim] for a in assessments]
        ranges[dim] = (min(values), max(values))
    return ranges


def reweight(
    assessment: Assessment, weights: dict[str, float]
) -> float:
    """Recompute a composite under caller-supplied weights.

    Supports the sensitivity analysis the published explorer offers: a reader
    substitutes their own weights and sees whether a ranking survives. Weights
    must cover exactly the assessment's dimensions and sum to 1.0.
    """
    scores = assessment.score_map()
    if set(weights) != set(scores):
        raise ValueError("weights must cover exactly the scored dimensions")
    total = sum(weights[dim] for dim in weights)
    if abs(total - 1.0) > 1e-9:
        raise ValueError(f"weights must sum to 1.0, got {total:.6f}")
    return sum(weights[dim] * value for dim, value in scores.items())
