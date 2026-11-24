"""Output of the layout parser: typed blocks with page positions."""

from enum import StrEnum

from pydantic import BaseModel, Field


class BlockKind(StrEnum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    TABLE = "table"
    FIGURE = "figure"
    CAPTION = "caption"
    EQUATION = "equation"
    FOOTNOTE = "footnote"
    REFERENCE = "reference"


class BoundingBox(BaseModel):
    x0: float
    y0: float
    x1: float
    y1: float


class Block(BaseModel):
    kind: BlockKind
    text: str
    page: int
    bbox: BoundingBox | None = None
    level: int | None = None  # heading depth
    table_rows: list[list[str]] | None = None  # for TABLE blocks


class ParsedDocument(BaseModel):
    paper_id: str
    blocks: list[Block] = Field(default_factory=list)

    def headings(self) -> list[Block]:
        return [b for b in self.blocks if b.kind is BlockKind.HEADING]
