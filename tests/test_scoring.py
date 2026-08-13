"""Tests for the scoring engine.

Coverage targets the two things that would invalidate a published number:
the validation rules that keep bad data out, and the arithmetic that turns
scores into rankings. Most tests use small hand-built fixtures so the expected
answer is obvious by inspection; one integration test loads the real repository
data and checks known values, guarding against silent regressions in the
published result.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from src.model import (
    Assessment,
    Framework,
    Score,
    load_assessments,
    load_framework,
)
from src.scoring import (
    dimension_means,
    dimension_ranges,
    rank,
    result_for,
    reweight,
    to_percent,
    weighted_total,
)


# --------------------------------------------------------------------------- #
# Fixtures: a tiny two-dimension framework with obvious arithmetic.
# --------------------------------------------------------------------------- #

def make_framework(w1: float = 0.6, w2: float = 0.4) -> Framework:
    return Framework(
        version="test",
        dimensions=[
            {"id": "a", "name": "Alpha", "weight": w1},
            {"id": "b", "name": "Beta", "weight": w2},
        ],
    )


def make_assessment(cid: str, a: int, b: int) -> Assessment:
    return Assessment(
        company_id=cid,
        company_name=cid.title(),
        scores=[
            Score(dimension="a", score=a),
            Score(dimension="b", score=b),
        ],
    )


# --------------------------------------------------------------------------- #
# Framework validation
# --------------------------------------------------------------------------- #

def test_framework_accepts_weights_summing_to_one():
    fw = make_framework(0.6, 0.4)
    assert fw.weight_of("a") == 0.6


def test_framework_rejects_weights_not_summing_to_one():
    with pytest.raises(ValidationError, match="sum to 1.0"):
        make_framework(0.6, 0.5)


def test_framework_rejects_duplicate_dimension_ids():
    with pytest.raises(ValidationError, match="unique"):
        Framework(
            version="test",
            dimensions=[
                {"id": "a", "name": "Alpha", "weight": 0.5},
                {"id": "a", "name": "Alpha again", "weight": 0.5},
            ],
        )


def test_framework_rejects_weight_outside_unit_interval():
    with pytest.raises(ValidationError):
        Framework(
            version="test",
            dimensions=[{"id": "a", "name": "Alpha", "weight": 1.4}],
        )


def test_weight_of_unknown_dimension_raises():
    fw = make_framework()
    with pytest.raises(KeyError):
        fw.weight_of("nonexistent")


# --------------------------------------------------------------------------- #
# Score validation
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("bad", [-1, 6, 100])
def test_score_rejects_out_of_range(bad):
    with pytest.raises(ValidationError, match="score must be in"):
        Score(dimension="a", score=bad)


@pytest.mark.parametrize("good", [0, 1, 2, 3, 4, 5])
def test_score_accepts_full_range(good):
    assert Score(dimension="a", score=good).score == good


# --------------------------------------------------------------------------- #
# Assessment validation against a framework
# --------------------------------------------------------------------------- #

def test_assessment_accepts_complete_scoring():
    fw = make_framework()
    a = make_assessment("acme", 3, 4).validate_against(fw)
    assert a.score_map() == {"a": 3, "b": 4}


def test_assessment_rejects_missing_dimension():
    fw = make_framework()
    a = Assessment(
        company_id="acme",
        company_name="Acme",
        scores=[Score(dimension="a", score=3)],
    )
    with pytest.raises(ValueError, match="missing dimensions"):
        a.validate_against(fw)


def test_assessment_rejects_unknown_dimension():
    fw = make_framework()
    a = Assessment(
        company_id="acme",
        company_name="Acme",
        scores=[
            Score(dimension="a", score=3),
            Score(dimension="b", score=3),
            Score(dimension="c", score=3),
        ],
    )
    with pytest.raises(ValueError, match="unknown dimensions"):
        a.validate_against(fw)


def test_assessment_rejects_duplicate_dimension():
    fw = make_framework()
    a = Assessment(
        company_id="acme",
        company_name="Acme",
        scores=[
            Score(dimension="a", score=3),
            Score(dimension="a", score=4),
        ],
    )
    with pytest.raises(ValueError, match="duplicate dimensions"):
        a.validate_against(fw)


# --------------------------------------------------------------------------- #
# Weighted scoring arithmetic
# --------------------------------------------------------------------------- #

def test_weighted_total_is_weighted_sum():
    fw = make_framework(0.6, 0.4)
    a = make_assessment("acme", 5, 0)
    # 0.6*5 + 0.4*0 = 3.0
    assert weighted_total(a, fw) == pytest.approx(3.0)


def test_weighted_total_maximum_is_score_max():
    fw = make_framework(0.6, 0.4)
    a = make_assessment("acme", 5, 5)
    assert weighted_total(a, fw) == pytest.approx(5.0)


def test_weighted_total_minimum_is_zero():
    fw = make_framework(0.6, 0.4)
    a = make_assessment("acme", 0, 0)
    assert weighted_total(a, fw) == pytest.approx(0.0)


def test_to_percent_scales_by_five():
    assert to_percent(2.5) == pytest.approx(50.0)
    assert to_percent(5.0) == pytest.approx(100.0)
    assert to_percent(0.0) == pytest.approx(0.0)


def test_result_carries_scores_and_percent():
    fw = make_framework(0.6, 0.4)
    r = result_for(make_assessment("acme", 5, 0), fw)
    assert r.scores == {"a": 5, "b": 0}
    assert r.percent == pytest.approx(60.0)


# --------------------------------------------------------------------------- #
# Ranking
# --------------------------------------------------------------------------- #

def test_rank_orders_high_to_low():
    fw = make_framework(0.6, 0.4)
    ranked = rank(
        [
            make_assessment("low", 1, 1),
            make_assessment("high", 5, 5),
            make_assessment("mid", 3, 3),
        ],
        fw,
    )
    assert [r.company_id for r in ranked] == ["high", "mid", "low"]


def test_rank_tie_break_is_deterministic_by_company_id():
    fw = make_framework(0.5, 0.5)
    # zeta and alpha have identical totals; alpha must come first.
    ranked = rank(
        [make_assessment("zeta", 3, 3), make_assessment("alpha", 3, 3)],
        fw,
    )
    assert [r.company_id for r in ranked] == ["alpha", "zeta"]


# --------------------------------------------------------------------------- #
# Dimension summaries
# --------------------------------------------------------------------------- #

def test_dimension_means():
    fw = make_framework()
    means = dimension_means(
        [make_assessment("x", 2, 4), make_assessment("y", 4, 0)], fw
    )
    assert means == {"a": pytest.approx(3.0), "b": pytest.approx(2.0)}


def test_dimension_ranges():
    fw = make_framework()
    ranges = dimension_ranges(
        [make_assessment("x", 1, 5), make_assessment("y", 4, 2)], fw
    )
    assert ranges == {"a": (1, 4), "b": (2, 5)}


# --------------------------------------------------------------------------- #
# Reweighting (sensitivity analysis)
# --------------------------------------------------------------------------- #

def test_reweight_recomputes_under_new_weights():
    a = make_assessment("acme", 4, 2)
    # equal weights: 0.5*4 + 0.5*2 = 3.0
    assert reweight(a, {"a": 0.5, "b": 0.5}) == pytest.approx(3.0)


def test_reweight_rejects_weights_not_summing_to_one():
    a = make_assessment("acme", 4, 2)
    with pytest.raises(ValueError, match="sum to 1.0"):
        reweight(a, {"a": 0.5, "b": 0.4})


def test_reweight_rejects_wrong_dimensions():
    a = make_assessment("acme", 4, 2)
    with pytest.raises(ValueError, match="cover exactly"):
        reweight(a, {"a": 0.5, "c": 0.5})


# --------------------------------------------------------------------------- #
# Integration: the real repository data
# --------------------------------------------------------------------------- #

def test_real_framework_loads_and_validates():
    fw = load_framework()
    assert len(fw.dimensions) == 6
    assert abs(sum(d.weight for d in fw.dimensions) - 1.0) < 1e-9


def test_real_assessments_load_and_validate():
    fw = load_framework()
    assessments = load_assessments(fw)
    assert len(assessments) == 8
    for a in assessments:
        a.validate_against(fw)  # raises if any file is malformed


def test_real_data_headline_finding_holds():
    """No company publishes a quantified result from its own AI use:
    every disclosed_outcomes score is 0 or 1."""
    fw = load_framework()
    assessments = load_assessments(fw)
    outcomes = [a.score_map()["disclosed_outcomes"] for a in assessments]
    assert max(outcomes) <= 1


def test_real_data_every_dimension_discriminates():
    """Sanity check that the rubric is not assigning everyone the same score:
    every dimension spans at least two distinct values."""
    fw = load_framework()
    assessments = load_assessments(fw)
    ranges = dimension_ranges(assessments, fw)
    for dim, (lo, hi) in ranges.items():
        assert hi > lo, f"dimension {dim} does not discriminate"
