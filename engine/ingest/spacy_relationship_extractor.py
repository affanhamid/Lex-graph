from typing import List
from engine.ingest.types import RelationExtractor
from engine.ingest.types import ParsedSentence
from engine.ontology.types import Entity, Relation
import uuid

from engine.utils.error_handling import safe


def make_spacy_relation_extractor() -> RelationExtractor:
    @safe
    def extract_relations(sentences: List[ParsedSentence], entities: List[Entity]) -> List[Relation]:
        relations: List[Relation] = []

        for sentence in sentences:
            for token in sentence.tokens:
                if token.dep == "ROOT":
                    subject = next((t for t in sentence.tokens if t.dep in ("nsubj", "nsubjpass")), None)
                    obj = next((t for t in sentence.tokens if t.dep in ("dobj", "pobj", "attr")), None)
                    if subject and obj:
                        relations.append(
                            Relation(
                                id=str(uuid.uuid4()),
                                source=subject.text,
                                target=obj.text,
                                relation=token.lemma,
                            )
                        )
        return relations

    return RelationExtractor(extract_relations=extract_relations)
