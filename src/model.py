"""Data model and loading, with validation that fails loudly.

Every rule the framework depends on is enforced here rather than assumed:
weights sum to 1.0, scores fall in 0..5, every company is scored on every
dimension, and dimension identifiers in an assessment match the framework.
A benchmark whose inputs are silently malformed is worse than no benchmark,
so a bad file raises rather than scoring around the problem.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, field_validator, model_validator

# Repository layout. The engine locates data relative to this file so it runs
# the same from any working directory.
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ASSESSMENTS = DATA / "assessments"

SCORE_MIN = 0
SCORE_MAX = 5
WEIGHT_TOLERANCE = 1e-9


class Dimension(BaseModel):
    """One assessment dimension and its weight in the composite score."""

    model_config = ConfigDict(extra="ignore")

    id: str
    name: str
    weight: float

    @field_validator("weight")
    @classmethod
    def weight_in_unit_interval(cls, v: float) -> float:
        if not 0.0 <= v <= 1.0:
            raise ValueError(f"weight must be in [0, 1], got {v}")
        return v


class Framework(BaseModel):
    """The set of weighted dimensions. Weights must sum to 1.0."""

    model_config = ConfigDict(extra="ignore")

    version: str
    dimensions: list[Dimension]

    @model_validator(mode="after")
    def weights_sum_to_one(self) -> "Framework":
        total = sum(d.weight for d in self.dimensions)
        if abs(total - 1.0) > WEIGHT_TOLERANCE:
            raise ValueError(
                f"dimension weights must sum to 1.0, got {total:.6f}"
            )
        ids = [d.id for d in self.dimensions]
        if len(ids) != len(set(ids)):
            raise ValueError("dimension ids must be unique")
        return self

    @property
    def ids(self) -> list[str]:
        return [d.id for d in self.dimensions]

    def weight_of(self, dimension_id: str) -> float:
        for d in self.dimensions:
            if d.id == dimension_id:
                return d.weight
        raise KeyError(f"unknown dimension: {dimension_id}")


class Score(BaseModel):
    """A single dimension score for a company.

    Only the scoring-critical fields are typed strictly. The descriptive
    fields (rationale, anchor_applied, evidence, various notes) vary between
    files and are permitted but not constrained, so that enriching an
    assessment never breaks the engine.
    """

    model_config = ConfigDict(extra="allow")

    dimension: str
    score: int

    @field_validator("score")
    @classmethod
    def score_in_range(cls, v: int) -> int:
        if not SCORE_MIN <= v <= SCORE_MAX:
            raise ValueError(
                f"score must be in [{SCORE_MIN}, {SCORE_MAX}], got {v}"
            )
        return v


class Assessment(BaseModel):
    """One company's complete assessment against the framework."""

    model_config = ConfigDict(extra="allow")

    company_id: str
    company_name: str
    scores: list[Score]

    def score_map(self) -> dict[str, int]:
        return {s.dimension: s.score for s in self.scores}

    def validate_against(self, framework: Framework) -> "Assessment":
        """Every framework dimension must be scored exactly once, and no
        assessment may score a dimension the framework does not define."""
        scored = [s.dimension for s in self.scores]
        expected = set(framework.ids)
        got = set(scored)

        if len(scored) != len(got):
            dupes = sorted({d for d in scored if scored.count(d) > 1})
            raise ValueError(f"{self.company_id}: duplicate dimensions {dupes}")
        missing = expected - got
        if missing:
            raise ValueError(
                f"{self.company_id}: missing dimensions {sorted(missing)}"
            )
        unknown = got - expected
        if unknown:
            raise ValueError(
                f"{self.company_id}: unknown dimensions {sorted(unknown)}"
            )
        return self


def load_framework(path: Path | None = None) -> Framework:
    """Load and validate the dimensions and weights."""
    path = path or (DATA / "dimensions.yaml")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    return Framework(**raw)


def load_assessments(
    framework: Framework, directory: Path | None = None
) -> list[Assessment]:
    """Load every assessment file and validate each against the framework.

    Returns assessments sorted by company_id for deterministic output.
    """
    directory = directory or ASSESSMENTS
    assessments: list[Assessment] = []
    for path in sorted(directory.glob("*.yaml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        assessment = Assessment(**raw).validate_against(framework)
        assessments.append(assessment)
    if not assessments:
        raise ValueError(f"no assessment files found in {directory}")
    return sorted(assessments, key=lambda a: a.company_id)
