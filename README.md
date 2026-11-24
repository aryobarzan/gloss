# Gloss

**Entity-centric RAG and document intelligence for research papers.**

Gloss reads large collections of research papers and turns them into something you can query:

1. **Ingest** papers from several sources (arXiv, ACL Anthology, …) into one common model, removing duplicates.
2. **Parse** PDFs with layout awareness (sections, tables, figures, captions), scored against arXiv LaTeX sources.
3. **Chunk** documents along their structure, keeping tables whole and resolving cross-references.
4. **Extract and link entities** (authors, institutions, datasets, methods) to OpenAlex, ORCID and ROR.
5. **Classify and grade** documents: document type plus a reproducibility-checklist coverage score with flags.
6. **Retrieve and answer** questions with cited, entity-aware RAG over a tuned vector index.
7. **Evaluate** every stage with explicit metrics: P/R/F1, recall@k, MRR, faithfulness, citation accuracy.

## Repository layout

```
gloss/
├── packages/
│   ├── gloss-core/        shared Pydantic models, settings, logging, DB helpers
│   ├── gloss-ingest/      1.  source adapters + de-duplication  (CLI: gloss-ingest)
│   ├── gloss-parse/       2.  layout-aware PDF parsing (VRDU), LaTeX ground truth
│   ├── gloss-chunk/       3.  fixed-size baseline + structure-aware chunking
│   ├── gloss-entities/    4.  NER + entity linking
│   ├── gloss-quality/     5.  doc-type classification + checklist completeness
│   ├── gloss-eval/        6.  metrics and evaluation reports
│   └── gloss-retrieval/   3./7. embeddings, vector store, hybrid search, RAG
├── apps/
│   ├── api/               FastAPI service
│   └── ui/                demo UI
├── eval/datasets/         gold annotations and question sets
├── data/                  downloaded corpora (git-ignored)
├── docs/                  architecture and milestones
└── scripts/db/            Postgres init (pgvector, pg_trgm)
```

This is a **uv workspace**: each pipeline stage is its own installable package, all sharing one lockfile and virtual environment.

## Quickstart

Requirements: _Python 3.12+, uv, Docker_.

```bash
uv sync --all-packages          # create .venv and install every package
cp .env.example .env
uv run poe db-up                # Postgres + pgvector on localhost:5432
uv run poe check                # lint + type check + tests
uv run poe api                  # http://localhost:8000/docs
uv run gloss-ingest --help
```

Optional: `uv run pre-commit install` to run ruff on every commit.

### Tasks

| Command                        | What it does            |
| ------------------------------ | ----------------------- |
| `uv run poe fmt`               | Format with ruff        |
| `uv run poe lint`              | Lint with ruff          |
| `uv run poe typecheck`         | mypy (strict)           |
| `uv run poe test`              | pytest                  |
| `uv run poe check`             | All of the above        |
| `uv run poe db-up` / `db-down` | Start / stop Postgres   |
| `uv run poe api`               | Run the API with reload |

## Data and licensing

PDFs and downloaded metadata are **not** committed. The repo ships download scripts, annotations and generators.
