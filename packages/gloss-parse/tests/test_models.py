from gloss_parse.models import Block, BlockKind, ParsedDocument


def test_headings_filter() -> None:
    doc = ParsedDocument(
        paper_id="arxiv:1",
        blocks=[
            Block(kind=BlockKind.HEADING, text="Introduction", page=1, level=1),
            Block(kind=BlockKind.PARAGRAPH, text="Lorem", page=1),
        ],
    )
    assert [b.text for b in doc.headings()] == ["Introduction"]
