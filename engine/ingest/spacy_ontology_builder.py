from typing import List
from engine.ingest.types import OntologyBuilder
from engine.ontology.types import Entity, Ontology, Relation
from engine.utils.error_handling import safe


def make_spacy_ontology_builder() -> OntologyBuilder:
    @safe
    def build_ontology(entities: List[Entity], relations: List[Relation]) -> Ontology:
        entity_types = sorted(set(entity.kind for entity in entities))
        relation_types = sorted(set(relation.relation for relation in relations))
        return Ontology(entity_types=entity_types, relation_types=relation_types)

    return OntologyBuilder(build_ontology=build_ontology)
