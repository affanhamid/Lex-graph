import uuid
from engine.ontology.types import Entity
from engine.ingest.types import NamedEntityRecognizer, ParsedSentence
from engine.utils.error_handling import safe
from typing import List


def make_spacy_ner() -> NamedEntityRecognizer:
    @safe
    def extract_entities(sentences: List[ParsedSentence]) -> List[Entity]:
        entities: List[Entity] = []

        for sentence in sentences:
            tokens = sentence.tokens
            current_span = []
            current_label = None

            for token in tokens:
                if token.is_entity:
                    if current_label is None:
                        current_label = token.entity_label
                        current_span = [token.text]
                    elif token.entity_label == current_label:
                        current_span.append(token.text)
                    else:
                        # Finalize the previous entity
                        entity_text = " ".join(current_span)
                        entities.append(Entity(
                            id=str(uuid.uuid4()),
                            name=entity_text,
                            kind=current_label
                        ))
                        # Start new entity
                        current_label = token.entity_label
                        current_span = [token.text]
                else:
                    if current_span:
                        entity_text = " ".join(current_span)
                        entities.append(Entity(
                            id=str(uuid.uuid4()),
                            name=entity_text,
                            kind=current_label
                        ))
                        current_span = []
                        current_label = None

            # Final entity at end of sentence
            if current_span:
                entity_text = " ".join(current_span)
                entities.append(Entity(
                    id=str(uuid.uuid4()),
                    name=entity_text,
                    kind=current_label
                ))

        return entities

    return NamedEntityRecognizer(extract_entities=extract_entities)
