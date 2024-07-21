from pydantic import BaseModel, FilePath

from ..paths import default_grammar_file, default_node_types_file


class GrammarConfig(BaseModel):
    input_file: FilePath = default_grammar_file


class NodeTypesConfig(BaseModel):
    input_file: FilePath = default_node_types_file
