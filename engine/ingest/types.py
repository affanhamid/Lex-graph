
from dataclasses import dataclass
from typing import Callable

from engine.ontology.types import KnowledgeGraph


@dataclass(frozen=True)
class Ingestion:
    ingest: Callable[[str], KnowledgeGraph]