from sys import stderr
from textwrap import indent

import defopt
from pydantic import BaseModel, ValidationError

__all__ = ["run_cli"]


class SimpleConfig(BaseModel):
    hello: str = "world"


def handle_validation_error(ve: ValidationError) -> str:
    error_msgs = "\n".join(str(e["ctx"]["error"]) for e in ve.errors())
    msg = "Invalid command:\n" + indent(error_msgs, prefix="- ")
    print(msg, end="\n\n", file=stderr)
    return


def simple_function(config: SimpleConfig) -> None:
    print("Simple function executed with config:", config)


def run_cli():
    try:
        config = defopt.run(SimpleConfig, no_negated_flags=True)
    except ValidationError as ve:
        handle_validation_error(ve)
        try:
            defopt.run(simple_function, argv=["-h"], no_negated_flags=True)
        except SystemExit as exc:
            exc.code = 1
            raise
    else:
        simple_function(config=config)
