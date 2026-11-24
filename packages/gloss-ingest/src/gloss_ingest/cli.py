"""``gloss-ingest`` command line entry point."""

from typing import Annotated

import typer

from gloss_core.config import get_settings
from gloss_core.logging import configure_logging, get_logger
from gloss_core.models import Source
from gloss_ingest.base import SourceAdapter
from gloss_ingest.sources.acl import AclAnthologyAdapter
from gloss_ingest.sources.arxiv import ArxivAdapter

app = typer.Typer(help="Collect papers from academic sources.", no_args_is_help=True)
log = get_logger(__name__)

ADAPTERS: dict[Source, type[SourceAdapter]] = {
    Source.ARXIV: ArxivAdapter,
    Source.ACL_ANTHOLOGY: AclAnthologyAdapter,
}


@app.command()
def run(
    source: Annotated[Source, typer.Option(help="Which source to ingest from.")],
    query: Annotated[str, typer.Option(help="Search query, e.g. 'adaptive learning'.")],
    limit: Annotated[int, typer.Option(help="Maximum number of papers.")] = 50,
) -> None:
    """Fetch metadata (and later PDFs) for papers matching QUERY."""
    settings = get_settings()
    configure_logging(settings.log_level)
    adapter = ADAPTERS[source]()
    for paper in adapter.search(query, limit):
        log.info("fetched %s: %s", paper.id, paper.title)


@app.command()
def sources() -> None:
    """List available sources."""
    for source in ADAPTERS:
        typer.echo(source.value)
