
from dataclasses import dataclass
import enum
from typing import Callable, List, Optional

from engine.ontology.types import KnowledgeGraph, Entity, Relation, Ontology
from engine.types import Result


@dataclass(frozen=True)
class Ingestion:
    ingest: Callable[[str], Result[KnowledgeGraph]]

@dataclass(frozen=True)
class SpacyModel(enum.Enum):
    EN_CORE_WEB_SM = "en_core_web_sm"

@dataclass(frozen=True)
class ParsedToken:
    text: str
    lemma: str
    pos: str
    dep: str
    head: str
    is_entity: bool
    entity_label: Optional[str]
    entity_id: Optional[str] = None

@dataclass(frozen=True)
class ParsedSentence:
    tokens: List[ParsedToken]

@dataclass(frozen=True)
class TextParser:
    parse_text: Callable[[str], Result[List[ParsedSentence]]]

@dataclass(frozen=True)
class NamedEntityRecognizer:
    extract_entities: Callable[[List[ParsedSentence]], Result[List[Entity]]]

@dataclass(frozen=True)
class RelationExtractor:
    extract_relations: Callable[[List[ParsedSentence], List[Entity]], Result[List[Relation]]]

@dataclass(frozen=True)
class OntologyBuilder:
    build_ontology: Callable[[List[Entity], List[Relation]], Result[Ontology]]