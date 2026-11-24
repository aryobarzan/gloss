"""Chunker interface shared by the baseline and the structure-aware chunker."""

from typing import Protocol

from gloss_core.models import Chunk


class Chunker(Protocol):
    def chunk(self, paper_id: str, text: str) -> list[Chunk]: ...
