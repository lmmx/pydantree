from sys import stderr
from textwrap import indent

import defopt
from pydantic import ValidationError

from ..grammar import generate_grammar
from .interfaces import GrammarConfig

__all__ = ["run_cli"]


def handle_validation_error(ve: ValidationError) -> None:
    error_msgs = "\n".join(str(e["ctx"]["error"]) for e in ve.errors())
    msg = "Invalid command:\n" + indent(error_msgs, prefix="- ")
    print(msg, end="\n\n", file=stderr)


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