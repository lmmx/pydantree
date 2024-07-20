from pydantic import BaseModel, FilePath

from ..paths import default_grammar_file


class GrammarConfig(BaseModel):
    input_file: FilePath = default_grammar_file
