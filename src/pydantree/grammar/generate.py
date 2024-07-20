import json
from sys import stderr

from ..interface.models import GrammarConfig

__all__ = ["generate_grammar"]


def generate_grammar(config: GrammarConfig) -> None:
    try:
        with open(config.input_file) as f:
            grammar = json.load(f)
        print(f"Grammar generated from file: {config.input_file}")
        print(json.dumps(grammar, indent=2))
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in grammar file {config.input_file}", file=stderr)
