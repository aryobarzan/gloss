"""Baseline: fixed-size word windows with overlap. Everything else is measured against this."""

from gloss_core.models import Chunk


class FixedSizeChunker:
    def __init__(self, size: int = 200, overlap: int = 40) -> None:
        if not 0 <= overlap < size:
            raise ValueError("overlap must be >= 0 and smaller than size")
        self.size = size
        self.overlap = overlap

    def chunk(self, paper_id: str, text: str) -> list[Chunk]:
        words = text.split()
        step = self.size - self.overlap
        chunks: list[Chunk] = []
        for i, start in enumerate(range(0, max(len(words), 1), step)):
            window = words[start : start + self.size]
            if not window:
                break
            chunks.append(
                Chunk(
                    id=f"{paper_id}#fixed-{i}",
                    paper_id=paper_id,
                    text=" ".join(window),
                    token_count=len(window),
                )
            )
            if start + self.size >= len(words):
                break
        return chunks
