from dataclasses import dataclass
import enum
from typing import Callable, List
from engine.ontology.types import Entity, Relation, Ontology
from engine.types import Result

@dataclass(frozen=True)
class SpacyModel(enum.Enum):
    EN_CORE_WEB_SM = "en_core_web_sm"

@dataclass(frozen=True)
class NamedEntityRecognizer:
    extract_entities: Callable[[str], Result[List[Entity]]]

@dataclass(frozen=True)
class RelationExtractor:
    extract_relations: Callable[[str, List[Entity]], Result[List[Relation]]]

@dataclass(frozen=True)
class OntologyBuilder:
    build_ontology: Callable[[List[Entity], List[Relation]], Result[Ontology]]
