from dataclasses import dataclass
import spacy
import uuid
from engine.ontology.types import Entity
from engine.externals.nlp.types import NamedEntityRecognizer, SpacyModel

def make_spacy_ner(model: SpacyModel) -> NamedEntityRecognizer:
    nlp = spacy.load(model.value)

    def extract_entities(text: str):
        doc = nlp(text)
        return [
            Entity(id=str(uuid.uuid4()), name=ent.text, kind=ent.label_)
            for ent in doc.ents
        ]
    return NamedEntityRecognizer(extract_entities=extract_entities)

"""
OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a Python package or a valid path to a data directory.
In this case, you need to download the model

python -m spacy download en_core_web_sm
"""
