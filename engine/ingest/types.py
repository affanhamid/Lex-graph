
from dataclasses import dataclass
from typing import Callable

from engine.ontology.types import KnowledgeGraph
from engine.types import Result


@dataclass(frozen=True)
class Ingestion:
    ingest: Callable[[str], Result[KnowledgeGraph]]