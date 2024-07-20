from pydantic import BaseModel, FilePath


class GrammarConfig(BaseModel):
    input_file: FilePath | None = None
