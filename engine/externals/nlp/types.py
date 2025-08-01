from dataclasses import dataclass
import enum
from typing import Callable, List
from engine.ontology.types import Entity, Relation, Ontology

@dataclass(frozen=True)
class SpacyModel(enum.Enum):
    EN_CORE_WEB_SM = "en_core_web_sm"

@dataclass(frozen=True)
class NamedEntityRecognizer:
    extract_entities: Callable[[str], List[Entity]]

@dataclass(frozen=True)
class RelationExtractor:
    extract_relations: Callable[[str, List[Entity]], List[Relation]]

@dataclass(frozen=True)
class OntologyBuilder:
    build_ontology: Callable[[List[Entity], List[Relation]], Ontology]
