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
    """
    ```
    ['name',
    'inherits',
    'rules',
    'extras',
    'precedences',
    'externals',
    'inline',
    'conflicts',
    'word',
    'supertypes']
    ```
    """
    try:
        schema_json = config.input_file.read_text()
        grammar = TreeSitterGrammarSpecification.model_validate_json(schema_json)

        print(f"# {grammar.name.title()}", end="\n\n")
        # No `inherits` for Python so don't print it

        print("## Rules", end="\n\n")
        rules = [(k, grammar.rules[k]) for k in list(grammar.rules)]
        for idx, (name, rule) in enumerate(rules):
            print(f"### {idx + 1}) {name}", end="\n\n")
            print("```py\n" + pprint_model(rule) + "```\n")

        print("## Extras", end="\n\n")
        for idx, extra in enumerate(grammar.extras):
            print(f"### {idx + 1})", end="\n\n")
            print("```py\n" + pprint_model(extra) + "```\n")

        print("## Precedences", end="\n\n")
        for idx, prec in enumerate(grammar.precedences):
            print(f"### {idx + 1})", end="\n\n")
            print("```py\n" + pprint_model(prec) + "```\n")

        print("## Externals", end="\n\n")
        for idx, external in enumerate(grammar.externals):
            print(f"### {idx + 1})", end="\n\n")
            print("```py\n" + pprint_model(external) + "```\n")

        print("## Inline", end="\n\n")
        for idx, inline in enumerate(grammar.inline):
            print(f"### {idx + 1}) {inline}", end="\n\n")

        print("## Conflicts", end="\n\n")
        for idx, conflict in enumerate(grammar.conflicts):
            conflict_expr = " + ".join(conflict)
            print(f"### {idx + 1}) {conflict}", end="\n\n")

        print("## Word", end="\n\n")
        print(grammar.word, end="\n\n")

        print("## supertypes", end="\n\n")
        for idx, supertype in enumerate(grammar.supertypes):
            print(f"### {idx + 1}) {supertype}", end="\n\n")

    except Exception as exc:
        print(f"Error parsing grammar file {config.input_file}: {exc}", file=stderr)
