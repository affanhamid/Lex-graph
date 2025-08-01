from logging import Logger

from engine.ingest.types import (
    Ingestion,
    NamedEntityRecognizer,
    OntologyBuilder,
    RelationExtractor,
    TextParser,
)
from engine.ontology.types import KnowledgeGraph
from engine.types import Result


def ingest(
    text: str,
    logger: Logger,
    parser: TextParser,
    ner: NamedEntityRecognizer,
    relation_extractor: RelationExtractor,
    ontology_builder: OntologyBuilder,
) -> Result[KnowledgeGraph]:
    logger.info(f"Ingesting text of length {len(text)}")
    return parser.parse_text(text).bind(
        lambda sents: ner.extract_entities(text).bind(
            lambda ents: relation_extractor.extract_relations(sents, ents).bind(
                lambda rels: ontology_builder.build_ontology(ents, rels).map(
                    lambda onto: KnowledgeGraph(
                        entities=ents, relations=rels, ontology=onto
                    )
                )
            )
        )
    )


def make_ingestion(
    logger: Logger,
    parser: TextParser,
    ner: NamedEntityRecognizer,
    relation_extractor: RelationExtractor,
    ontology_builder: OntologyBuilder,
) -> Ingestion:
    return Ingestion(
        ingest=lambda text: ingest(
            text, logger, parser, ner, relation_extractor, ontology_builder
        )
    )
