from logging import Logger
from typing import List
from engine.externals.nlp.types import NamedEntityRecognizer
from engine.ingest.types import Ingestion
from engine.ontology.types import Entity, KnowledgeGraph, Ontology, Relation

def ingest(text: str, logger: Logger, nlp: NamedEntityRecognizer) -> KnowledgeGraph:
    logger.info(f"Ingesting text of length {len(text)}")
    entities = nlp.extract_entities(text)
    relations = extract_relations(text, entities)
    ontology = build_ontology(entities, relations)
    return KnowledgeGraph(entities, relations, ontology)

def extract_relations(text: str, entities: List[Entity]) -> List[Relation]:
    return []

def build_ontology(entities: List[Entity], relations: List[Relation]) -> Ontology:
    return Ontology(entity_types=[], relation_types=[])

def make_ingestion(logger: Logger, nlp: NamedEntityRecognizer) -> Ingestion:

    return Ingestion(ingest=lambda text: ingest(text, logger, nlp))
