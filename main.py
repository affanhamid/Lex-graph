from engine.ingest.spacy_ner import make_spacy_ner
from engine.ingest.spacy_ontology_builder import make_spacy_ontology_builder
from engine.ingest.spacy_parser import make_spacy_parser
from engine.ingest.spacy_relationship_extractor import make_spacy_relation_extractor
from engine.ingest.types import SpacyModel
from engine.ingest import make_ingestion
from engine.utils.file_io import make_file_io
from engine.utils.logger import make_logger
from returns.pointfree import bind


def main():
    """Main entry point for the lex-graph engine."""

    logger = make_logger()
    file_io = make_file_io(logger)
    parser = make_spacy_parser(SpacyModel.EN_CORE_WEB_SM)
    ner = make_spacy_ner(SpacyModel.EN_CORE_WEB_SM)
    relation_extractor = make_spacy_relation_extractor()
    ontology_builder = make_spacy_ontology_builder()
    ingestion = make_ingestion(logger, parser, ner, relation_extractor, ontology_builder)

    graph = file_io.read("sample.txt").bind(ingestion.ingest)
    print(graph)

if __name__ == "__main__":
    main()