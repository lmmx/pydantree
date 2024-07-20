import json
from sys import stderr

from ..interface.models import GrammarConfig
from .models import TreeSitterGrammarSpecification

__all__ = ["generate_grammar"]


def generate_grammar(config: GrammarConfig) -> None:
    try:
        schema_json = config.input_file.read_text()
        grammar = TreeSitterGrammarSpecification.model_validate_json(schema_json)
        print(f"Grammar generated from file: {config.input_file}")
        print(grammar.model_dump_json(indent=2))
    except:
        print(f"Error: Invalid JSON in grammar file {config.input_file}", file=stderr)
