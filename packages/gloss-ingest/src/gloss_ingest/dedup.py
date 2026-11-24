"""Detect the same paper arriving from several sources (or as several versions)."""

import re
import unicodedata
from collections import defaultdict
from collections.abc import Iterable

from gloss_core.models import Paper

_NON_ALNUM = re.compile(r"[^a-z0-9 ]+")
_SPACES = re.compile(r"\s+")
_VERSION = re.compile(r"v\d+$")


def normalize_title(title: str) -> str:
    """Lowercase, strip accents/punctuation and collapse whitespace."""
    decomposed = unicodedata.normalize("NFKD", title)
    text = "".join(c for c in decomposed if not unicodedata.combining(c))
    text = _NON_ALNUM.sub(" ", text.lower())
    return _SPACES.sub(" ", text).strip()


def dedup_keys(paper: Paper) -> list[str]:
    """Keys that, if shared, mean two records are the same paper. Strongest first."""
    keys: list[str] = []
    if paper.doi:
        keys.append(f"doi:{paper.doi.lower()}")
    if paper.arxiv_id:
        keys.append(f"arxiv:{_VERSION.sub('', paper.arxiv_id)}")  # drop "v2" suffix
    keys.append(f"title:{normalize_title(paper.title)}")
    return keys


def group_duplicates(papers: Iterable[Paper]) -> list[list[Paper]]:
    """Group papers sharing any dedup key (union-find over keys)."""
    items = list(papers)
    parent = list(range(len(items)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    first_seen: dict[str, int] = {}
    for idx, paper in enumerate(items):
        for key in dedup_keys(paper):
            if key in first_seen:
                parent[find(idx)] = find(first_seen[key])
            else:
                first_seen[key] = idx

    groups: dict[int, list[Paper]] = defaultdict(list)
    for idx, paper in enumerate(items):
        groups[find(idx)].append(paper)
    return list(groups.values())
