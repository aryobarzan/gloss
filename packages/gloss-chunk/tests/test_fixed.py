import pytest

from gloss_chunk.fixed import FixedSizeChunker


def test_windows_overlap_and_cover_all_words() -> None:
    text = " ".join(str(i) for i in range(10))
    chunks = FixedSizeChunker(size=4, overlap=1).chunk("p", text)
    assert [c.text for c in chunks] == ["0 1 2 3", "3 4 5 6", "6 7 8 9"]


def test_empty_text_gives_no_chunks() -> None:
    assert FixedSizeChunker().chunk("p", "") == []


def test_invalid_overlap_rejected() -> None:
    with pytest.raises(ValueError):
        FixedSizeChunker(size=10, overlap=10)
