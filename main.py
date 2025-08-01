from engine.externals.nlp.spacy_impl import make_spacy_ner
from engine.externals.nlp.types import SpacyModel
from engine.ingest.ingest import make_ingestion
from engine.utils.file_io import make_file_io
from engine.utils.logger import make_logger
from returns.pointfree import bind


def main():
    """Main entry point for the lex-graph engine."""

    logger = make_logger()
    file_io = make_file_io(logger)
    nlp = make_spacy_ner(SpacyModel.EN_CORE_WEB_SM)
    ingestion = make_ingestion(logger, nlp)

    graph = file_io.read("sample.txt").bind(ingestion.ingest)
    print(graph)

if __name__ == "__main__":
    main()