"""Metric implementations used across stages (kept dependency-free on purpose)."""

from collections.abc import Hashable, Sequence, Set
from dataclasses import dataclass


@dataclass(frozen=True)
class PRF:
    precision: float
    recall: float
    f1: float


def precision_recall_f1(predicted: Set[Hashable], gold: Set[Hashable]) -> PRF:
    """Set-based P/R/F1, e.g. for entity extraction or checklist flag detection."""
    tp = len(predicted & gold)
    precision = tp / len(predicted) if predicted else 0.0
    recall = tp / len(gold) if gold else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return PRF(precision, recall, f1)


def recall_at_k(ranked: Sequence[Hashable], relevant: Set[Hashable], k: int) -> float:
    """Fraction of relevant items that appear in the top-k results."""
    if not relevant:
        return 0.0
    return len(set(ranked[:k]) & relevant) / len(relevant)


def reciprocal_rank(ranked: Sequence[Hashable], relevant: Set[Hashable]) -> float:
    """1 / rank of the first relevant result (0 if none). Average over queries for MRR."""
    for i, item in enumerate(ranked, start=1):
        if item in relevant:
            return 1.0 / i
    return 0.0
