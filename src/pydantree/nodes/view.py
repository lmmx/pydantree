from sys import stderr

import black

from ..interface.models import NodeTypesConfig
from .models import NodeTypesJson

__all__ = ["view_node_types"]


def pprint_model(model) -> str:
    s = repr(model)
    pretty = black.format_str(s, mode=black.FileMode(line_length=70))
    return pretty


def view_node_types(config: NodeTypesConfig) -> None:
    try:
        schema_json = config.input_file.read_text()
        node_types = NodeTypesJson.model_validate_json(schema_json).root
        for idx, node_type in enumerate(node_types):
            print(f"## {idx}) {node_type.type}\n\n")
            print("```py\n" + pprint_model(node_type) + "```")
    except Exception as exc:
        print(f"Error parsing node_types file {config.input_file}: {exc}", file=stderr)
