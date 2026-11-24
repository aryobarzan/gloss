"""Retrieval interfaces.

TODO (3.): ``SentenceTransformerEmbedder``, ``PgVectorStore`` and a basic RAG answerer.
TODO (7.): ``QdrantStore``, hybrid BM25 + dense search, HNSW / quantization benchmarks.
"""

from typing import Any, Protocol

from pydantic import BaseModel

from gloss_core.models import Chunk


class SearchHit(BaseModel):
    chunk: Chunk
    score: float


class Embedder(Protocol):
    dim: int

    def embed(self, texts: list[str]) -> list[list[float]]: ...


class VectorStore(Protocol):
    def upsert(self, chunks: list[Chunk], vectors: list[list[float]]) -> None: ...

    def search(
        self, vector: list[float], k: int = 10, filters: dict[str, Any] | None = None
    ) -> list[SearchHit]: ...
