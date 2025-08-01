from logging import Logger
from typing import List

from returns.result import safe
from engine.externals.nlp.types import NamedEntityRecognizer
from engine.ingest.types import Ingestion
from engine.ontology.types import Entity, KnowledgeGraph, Ontology, Relation
from engine.types import Result

@safe
def ingest(text: str, logger: Logger, nlp: NamedEntityRecognizer) -> KnowledgeGraph:
    logger.info(f"Ingesting text of length {len(text)}")
    entities = nlp.extract_entities(text).unwrap()
    relations = extract_relations(text, entities).unwrap()
    ontology = build_ontology(entities, relations).unwrap()
    return KnowledgeGraph(entities, relations, ontology)


@safe
def extract_relations(text: str, entities: List[Entity]) -> List[Relation]:
    return []

@safe
def build_ontology(entities: List[Entity], relations: List[Relation]) -> Ontology:
    return Ontology(entity_types=[], relation_types=[])

def make_ingestion(logger: Logger, nlp: NamedEntityRecognizer) -> Ingestion:

    return Ingestion(ingest=lambda text: ingest(text, logger, nlp))
