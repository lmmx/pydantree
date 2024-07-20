from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, RootModel

__all__ = ["Rule", "ConflictList", "External", "Grammar"]


class Rule(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: str
    content: dict | str | None = None
    members: list["Rule"] | None = None
    value: int | str | None = None
    name: str | None = None
    field: str | None = None


class ConflictList(RootModel):
    root: list[list[str]]


class External(BaseModel):
    type: str
    name: str | None = None
    value: str | None = None


class SymbolExternal(BaseModel):
    type: Literal["SYMBOL"]
    name: str


class StringExternal(BaseModel):
    type: Literal["STRING"]
    value: str


External = Union[SymbolExternal, StringExternal]


class Grammar(BaseModel):
    name: str
    word: str
    rules: dict[str, Rule]
    extras: list[Rule | str]
    conflicts: ConflictList
    precedences: list
    externals: list[External]
    inline: list[str]
    supertypes: list[str]
