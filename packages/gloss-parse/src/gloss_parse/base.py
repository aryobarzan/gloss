"""Parser interfaces.

TODO (2.):
- ``DoclingParser``: PDF -> ParsedDocument using Docling (add ``docling`` as a dependency).
- ``LatexGroundTruth``: arXiv LaTeX source -> ParsedDocument, used to score the PDF parser.
"""

from pathlib import Path
from typing import Protocol

from gloss_parse.models import ParsedDocument


class LayoutParser(Protocol):
    def parse(self, pdf_path: Path, paper_id: str) -> ParsedDocument: ...
