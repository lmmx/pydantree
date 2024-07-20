import json
from pathlib import Path
from sys import stderr

from .cli.interfaces import GrammarConfig

__all__ = ["generate_grammar"]


def generate_grammar(config: GrammarConfig) -> None:
    if config.input_file is None:
        # Use the default grammar file shipped with the package
        package_dir = Path(__file__).parent
        default_grammar_file = package_dir / "data" / "grammar.json"
        input_file = default_grammar_file
    else:
        input_file = config.input_file

    try:
        with open(input_file) as f:
            grammar = json.load(f)
        print(f"Grammar generated from file: {input_file}")
        print(json.dumps(grammar, indent=2))
    except FileNotFoundError:
        print(f"Error: Grammar file not found at {input_file}", file=stderr)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in grammar file {input_file}", file=stderr)
