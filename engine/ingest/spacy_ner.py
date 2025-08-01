import uuid
from engine.ontology.types import Entity
from engine.ingest.types import NamedEntityRecognizer, SpacyModel
from engine.utils.load_nlp_model import load_nlp_model
from engine.utils.error_handling import safe
from typing import List


def make_spacy_ner(model: SpacyModel) -> NamedEntityRecognizer:
    def extract_entities(text: str) -> List[Entity]:
        return load_nlp_model(model).map(lambda nlp: nlp(text)).map(lambda doc: [
            Entity(id=str(uuid.uuid4()), name=ent.text, kind=ent.label_)
            for ent in doc.ents
        ])
    return NamedEntityRecognizer(extract_entities=extract_entities)
