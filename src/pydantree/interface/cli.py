from sys import stderr
from textwrap import indent

import defopt
from pydantic import ValidationError

from ..grammar import view_grammar
from ..nodes import view_node_types
from .models import GrammarConfig, NodeTypesConfig

__all__ = ["run"]


def handle_validation_error(ve: ValidationError) -> None:
    error_msgs = "\n".join(str(e["ctx"]["error"]) for e in ve.errors())
    msg = "Invalid command:\n" + indent(error_msgs, prefix="- ")
    print(msg, end="\n\n", file=stderr)


def run():
    try:
        config = defopt.run(
            {"grammar": GrammarConfig, "nodes": NodeTypesConfig},
            no_negated_flags=True,
        )
    except ValidationError as ve:
        handle_validation_error(ve)
        try:
            defopt.run(
                {"grammar": GrammarConfig, "nodes": NodeTypesConfig},
                argv=["-h"],
                no_negated_flags=True,
            )
        except SystemExit as exc:
            exc.code = 1
            raise
    else:
        match config:
            case GrammarConfig():
                view_grammar(config=config)
            case NodeTypesConfig():
                view_node_types(config=config)
