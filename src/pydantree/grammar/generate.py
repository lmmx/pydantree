import json
from sys import stderr

from ..interface.models import GrammarConfig
from .models import Grammar

__all__ = ["generate_grammar"]


def generate_grammar(config: GrammarConfig) -> None:
    try:
        grammar = Grammar.model_validate_json(config.input_file.read_text())
        print(f"Grammar generated from file: {config.input_file}")
        print(grammar.model_dump_json(indent=2))
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in grammar file {config.input_file}", file=stderr)
