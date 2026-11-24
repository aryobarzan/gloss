import pytest

from gloss_eval.metrics import precision_recall_f1, recall_at_k, reciprocal_rank


def test_prf() -> None:
    result = precision_recall_f1({"a", "b", "c"}, {"b", "c", "d", "e"})
    assert result.precision == pytest.approx(2 / 3)
    assert result.recall == pytest.approx(0.5)
    assert result.f1 == pytest.approx(4 / 7)


def test_prf_empty() -> None:
    assert precision_recall_f1(set(), set()).f1 == 0.0


def test_recall_at_k_and_rr() -> None:
    ranked = ["x", "a", "y", "b"]
    assert recall_at_k(ranked, {"a", "b"}, k=2) == 0.5
    assert reciprocal_rank(ranked, {"a", "b"}) == 0.5
    assert reciprocal_rank(ranked, {"z"}) == 0.0
