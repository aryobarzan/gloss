"""Checklists are declared in YAML so they can be versioned and swapped (e.g. for KYC)."""

from importlib import resources
from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class ChecklistItem(BaseModel):
    id: str
    question: str
    description: str = ""
    required: bool = True


class Checklist(BaseModel):
    name: str
    version: str
    items: list[ChecklistItem] = Field(default_factory=list)


class ItemResult(BaseModel):
    item_id: str
    satisfied: bool
    evidence: str | None = None  # quoted span / chunk id supporting the decision


def load_checklist(path: Path | None = None) -> Checklist:
    """Load a checklist; defaults to the bundled reproducibility checklist."""
    if path is None:
        text = (resources.files("gloss_quality") / "checklists" / "reproducibility.yaml").read_text(
            encoding="utf-8"
        )
    else:
        text = path.read_text(encoding="utf-8")
    return Checklist.model_validate(yaml.safe_load(text))


def coverage_score(checklist: Checklist, results: list[ItemResult]) -> float:
    """Share of *required* items that are satisfied (0.0-1.0)."""
    required = {item.id for item in checklist.items if item.required}
    if not required:
        return 1.0
    satisfied = {r.item_id for r in results if r.satisfied}
    return len(required & satisfied) / len(required)
