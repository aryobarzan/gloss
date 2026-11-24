"""ArxivAdapter — TODO (1.).

Data source: arXiv API (export.arxiv.org/api/query, Atom feed).
Also fetch the LaTeX source (e-print) for 2. ground truth.
Respect the API's rate limit.
"""

from collections.abc import Iterator
from pathlib import Path

from gloss_core.models import Paper, Source


class ArxivAdapter:
    source = Source.ARXIV

    def search(self, query: str, limit: int) -> Iterator[Paper]:
        raise NotImplementedError("1. implement ArxivAdapter.search")

    def download_pdf(self, paper: Paper, dest_dir: Path) -> Path:
        raise NotImplementedError("1. implement ArxivAdapter.download_pdf")
