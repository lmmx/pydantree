from sys import stderr

import black

from ..interface.models import GrammarConfig
from .models import TreeSitterGrammarSpecification

__all__ = ["view_grammar"]


def pprint_model(model) -> str:
    s = repr(model)
    pretty = black.format_str(s, mode=black.FileMode(line_length=70))
    return pretty


def view_grammar(config: GrammarConfig) -> None:
    try:
        schema_json = config.input_file.read_text()
        grammar = TreeSitterGrammarSpecification.model_validate_json(schema_json)
        # print(f"Grammar generated from file: {config.input_file}")
        rules = [(k, grammar.rules[k]) for k in list(grammar.rules)]
        for idx, (name, rule) in enumerate(rules):
            print(f"## {idx + 1}) {name}", end="\n\n")
            print("```py\n" + pprint_model(rule) + "```\n")
    except Exception as exc:
        print(f"Error parsing grammar file {config.input_file}: {exc}", file=stderr)
