import json
from pathlib import Path
from sys import stderr
from textwrap import indent

import defopt
from pydantic import BaseModel, ValidationError, FilePath

__all__ = ["run_cli"]


class GrammarConfig(BaseModel):
    input_file: FilePath | None = None


def handle_validation_error(ve: ValidationError) -> None:
    error_msgs = "\n".join(str(e["ctx"]["error"]) for e in ve.errors())
    msg = "Invalid command:\n" + indent(error_msgs, prefix="- ")
    print(msg, end="\n\n", file=stderr)


def generate_grammar(config: GrammarConfig) -> None:
    if config.input_file is None:
        # Use the default grammar file shipped with the package
        package_dir = Path(__file__).parent
        default_grammar_file = package_dir / "grammar.json"
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


def run_cli():
    try:
        config = defopt.run(GrammarConfig, no_negated_flags=True)
    except ValidationError as ve:
        handle_validation_error(ve)
        try:
            defopt.run(generate_grammar, argv=["-h"], no_negated_flags=True)
        except SystemExit as exc:
            exc.code = 1
            raise
    else:
        generate_grammar(config=config)


if __name__ == "__main__":
    run_cli()
