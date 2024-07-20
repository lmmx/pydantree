from pprint import pprint
from sys import stderr

import black

from ..interface.models import GrammarConfig
from .models import TreeSitterGrammarSpecification

__all__ = ["view_grammar"]


def pprint_model(model):
    s = repr(model)
    pretty = black.format_str(s, mode=black.FileMode(line_length=200))
    print(pretty)


def view_grammar(config: GrammarConfig) -> None:
    try:
        schema_json = config.input_file.read_text()
        grammar = TreeSitterGrammarSpecification.model_validate_json(schema_json)
        # print(f"Grammar generated from file: {config.input_file}")
        rules = [(k, grammar.rules[k]) for k in list(grammar.rules)]
        for idx, (name, rule) in enumerate(rules):
            print(f"Rule {idx}) {name}", end=": ")
            pprint_model(rule)
    except Exception:
        breakpoint()
        print(f"Error: Invalid JSON in grammar file {config.input_file}", file=stderr)
