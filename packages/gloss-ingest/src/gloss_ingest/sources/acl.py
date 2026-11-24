"""AclAnthologyAdapter — TODO (1.).

Data source: ACL Anthology metadata, via the acl-anthology Python package
or the anthology's bulk export.
"""

from collections.abc import Iterator
from pathlib import Path

from gloss_core.models import Paper, Source


class AclAnthologyAdapter:
    source = Source.ACL_ANTHOLOGY

    def search(self, query: str, limit: int) -> Iterator[Paper]:
        raise NotImplementedError("1. implement AclAnthologyAdapter.search")

    def download_pdf(self, paper: Paper, dest_dir: Path) -> Path:
        raise NotImplementedError("1. implement AclAnthologyAdapter.download_pdf")
