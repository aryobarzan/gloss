"""Interface every source adapter implements."""

from collections.abc import Iterator
from pathlib import Path
from typing import Protocol

from gloss_core.models import Paper, Source


class SourceAdapter(Protocol):
    source: Source

    def search(self, query: str, limit: int) -> Iterator[Paper]:
        """Yield papers matching ``query``, already converted to the common model."""
        ...

    def download_pdf(self, paper: Paper, dest_dir: Path) -> Path:
        """Download the paper's PDF and return its local path."""
        ...
