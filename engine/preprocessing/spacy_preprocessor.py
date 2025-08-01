from engine.ingest.types import SpacyModel
from engine.preprocessing.types import Preprocessor

from engine.types import Result
from engine.utils.error_handling import safe
from engine.utils.load_nlp_model import load_nlp_model


def make_preprocessor(spacy_model: SpacyModel) -> Preprocessor:
    def preprocess(text: str) -> Result[str]:
        return load_nlp_model(spacy_model).bind(
            safe(
                lambda nlp: " ".join(
                    [
                        token.lemma_.lower()
                        for token in nlp(text)
                        if not token.is_stop
                        and not token.is_punct
                        and not token.is_space
                    ]
                )
            )
        )

    return Preprocessor(preprocess=preprocess)
    return Preprocessor(preprocess=preprocess)
