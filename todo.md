1. Start with a very simple text (like a few paragraphs)
    - Ingest + extract entities/relations with LLM prompting
2. Build and render the graph
3. Then modularize:
- ontology.py – define schema
- ingest.py – extract triples from text
- graph.py – store and manipulate KGs
- query.py – search and reason
- ui/ – optional editor
