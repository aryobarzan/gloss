from gloss_core.models import Author, Paper, Source


def test_paper_id_is_source_prefixed() -> None:
    paper = Paper(source=Source.ARXIV, source_id="2401.01234", title="A Paper")
    assert paper.id == "arxiv:2401.01234"


def test_paper_round_trips_through_json() -> None:
    paper = Paper(
        source=Source.ACL_ANTHOLOGY,
        source_id="2023.bea-1.1",
        title="Feedback Generation",
        authors=[Author(name="Ada Lovelace", affiliations=["Uni"])],
    )
    assert Paper.model_validate_json(paper.model_dump_json()) == paper
