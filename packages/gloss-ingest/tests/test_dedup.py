from gloss_core.models import Paper, Source
from gloss_ingest.dedup import group_duplicates, normalize_title


def test_normalize_title_ignores_case_accents_and_punctuation() -> None:
    assert normalize_title("  Café: A Study—of Things!  ") == "cafe a study of things"


def test_same_arxiv_paper_in_two_versions_is_grouped() -> None:
    a = Paper(source=Source.ARXIV, source_id="2401.1v1", arxiv_id="2401.1v1", title="X")
    b = Paper(source=Source.ARXIV, source_id="2401.1v2", arxiv_id="2401.1v2", title="X (rev)")
    assert len(group_duplicates([a, b])) == 1


def test_cross_source_match_by_title() -> None:
    a = Paper(source=Source.ARXIV, source_id="1", title="Adaptive Learning, Revisited")
    b = Paper(source=Source.ACL_ANTHOLOGY, source_id="2", title="adaptive learning revisited")
    c = Paper(source=Source.ACL_ANTHOLOGY, source_id="3", title="Something else")
    groups = group_duplicates([a, b, c])
    assert sorted(len(g) for g in groups) == [1, 2]
