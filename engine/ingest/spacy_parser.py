from typing import List
from engine.ingest.types import ParsedSentence, ParsedToken, SpacyModel, TextParser
from engine.types import Result
from engine.utils.error_handling import safe
from engine.utils.load_nlp_model import load_nlp_model


def make_spacy_parser(model: SpacyModel) -> TextParser:
    def parse_text(text: str) -> List[ParsedSentence]:
        return (
            load_nlp_model(model)
            .map(lambda nlp: nlp(text))
            .map(lambda doc: [
                ParsedSentence(
                    tokens=[
                        ParsedToken(
                            text=token.text,
                            lemma=token.lemma_,
                            pos=token.pos_,
                            dep=token.dep_,
                            head=token.head.text,
                            is_entity=token.ent_type_ != "",
                            entity_label=token.ent_type_ or None,
                        )
                        for token in sent
                    ]
                )
                for sent in doc.sents
            ])
        )

    return TextParser(parse_text=parse_text)
