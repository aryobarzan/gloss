"""FastAPI app. Run with ``uv run poe api``."""

from fastapi import FastAPI

from gloss_core import __version__

app = FastAPI(title="Gloss", version=__version__)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": __version__}


# TODO (3.): POST /ask        -> RAG answer with citations
# TODO (4.): GET  /entities/{id} and entity-centric search
# TODO (5.): GET  /papers/{id}/checklist
