from engine.utils.error_handling import safe
import spacy
from spacy import Language

from engine.ingest.types import SpacyModel

@safe
def load_nlp_model(model: SpacyModel) -> Language:
    try:
        return spacy.load(model.value)
    except OSError as e:
        raise RuntimeError(
            f"Failed to load spaCy model '{model.value}'. "
            "Make sure to install it using:\n\n    python -m spacy download en_core_web_sm\n"
        ) from e