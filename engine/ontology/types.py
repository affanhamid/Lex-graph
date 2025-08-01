from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Entity:
    id: str
    name: str
    kind: str

@dataclass(frozen=True)
class Relation:
    source: str
    target: str
    kind: str
    confidence: float = 1.0

@dataclass(frozen=True)
class Ontology:
    entity_types: List[str]
    relation_types: List[str]

@dataclass(frozen=True)
class KnowledgeGraph:
    entities: List[Entity]
    relations: List[Relation]
    ontology: Ontology
