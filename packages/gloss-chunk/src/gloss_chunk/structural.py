"""Structure-aware chunker — TODO (3.).

Plan:
- split along the section tree from ``gloss_parse`` (never across headings)
- keep each table whole as its own TABLE chunk, with column headers repeated
- store ``parent_chunk_id`` / ``section_id`` for parent-child retrieval
- resolve cross-references ("see Table 3", "Section 4.2") into chunk metadata
"""
