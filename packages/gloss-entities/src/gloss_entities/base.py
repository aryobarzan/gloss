"""Extraction and linking interfaces.

TODO (4.):
- ``GlinerExtractor``: zero-shot NER for authors, institutions, datasets, methods
- ``OpenAlexLinker`` / ``RorLinker``: resolve mentions against OpenAlex, ORCID and ROR
- dataset/method gazetteer with known aliases
"""

from typing import Protocol

from gloss_core.models import Chunk, Entity, EntityMention


class EntityExtractor(Protocol):
    def extract(self, chunk: Chunk) -> list[EntityMention]: ...


class EntityLinker(Protocol):
    def link(self, mention: EntityMention) -> Entity | None: ...
