"""Common data model shared by all pipeline stages.

Every source adapter converts its raw data into these models, so downstream
stages (parsing, chunking, entity linking, ...) never care where a paper came from.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class Source(StrEnum):
    ARXIV = "arxiv"
    ACL_ANTHOLOGY = "acl_anthology"
    PMC = "pmc"
    OPENREVIEW = "openreview"


class DocType(StrEnum):
    PAPER = "paper"
    THESIS = "thesis"
    POSTER = "poster"
    SLIDES = "slides"
    UNKNOWN = "unknown"


class ChunkKind(StrEnum):
    TEXT = "text"
    TABLE = "table"
    FIGURE_CAPTION = "figure_caption"
    EQUATION = "equation"


class EntityType(StrEnum):
    AUTHOR = "author"
    INSTITUTION = "institution"
    DATASET = "dataset"
    METHOD = "method"
    VENUE = "venue"


class Author(BaseModel):
    name: str
    orcid: str | None = None
    affiliations: list[str] = Field(default_factory=list)


class Paper(BaseModel):
    """A single document as delivered by one source."""

    source: Source
    source_id: str
    title: str
    abstract: str | None = None
    authors: list[Author] = Field(default_factory=list)
    year: int | None = None
    venue: str | None = None
    doi: str | None = None
    arxiv_id: str | None = None
    pdf_url: str | None = None
    latex_url: str | None = None
    doc_type: DocType = DocType.UNKNOWN

    @property
    def id(self) -> str:
        """Stable Gloss identifier, e.g. ``arxiv:2401.01234``."""
        return f"{self.source.value}:{self.source_id}"


class Section(BaseModel):
    id: str
    paper_id: str
    title: str
    level: int = 1
    parent_id: str | None = None
    order: int = 0


class Chunk(BaseModel):
    id: str
    paper_id: str
    text: str
    kind: ChunkKind = ChunkKind.TEXT
    section_id: str | None = None
    parent_chunk_id: str | None = None
    token_count: int | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class Entity(BaseModel):
    """A canonical, resolved real-world thing (one author, one dataset, ...)."""

    id: str
    type: EntityType
    canonical_name: str
    aliases: list[str] = Field(default_factory=list)
    external_ids: dict[str, str] = Field(default_factory=dict)  # e.g. {"orcid": ..., "ror": ...}


class EntityMention(BaseModel):
    """A surface string found in a chunk, optionally linked to an Entity."""

    chunk_id: str
    surface: str
    type: EntityType
    start: int
    end: int
    entity_id: str | None = None
    confidence: float | None = None
