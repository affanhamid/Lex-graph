"""
Ingestion modules for the Lex-graph Engine.
"""

from .ingest_impl import make_ingestion
from .spacy_ner import make_spacy_ner


__all__ = [
    "make_ingestion",
    "make_spacy_ner",
] 