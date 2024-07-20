# generated by datamodel-codegen:
#   filename:  grammar-schema.json
#   timestamp: 2024-07-20T17:35:06+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, constr


class BlankRule(BaseModel):
    type: constr(pattern=r'^BLANK$')


class StringRule(BaseModel):
    type: constr(pattern=r'^STRING$')
    value: str


class PatternRule(BaseModel):
    type: constr(pattern=r'^PATTERN$')
    value: str
    flags: Optional[str] = None


class SymbolRule(BaseModel):
    type: constr(pattern=r'^SYMBOL$')
    name: str


class TreeSitterGrammarSpecification(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: constr(pattern=r'^[a-zA-Z_]\w*') = Field(
        ..., description='the name of the grammar'
    )
    inherits: Optional[constr(pattern=r'^[a-zA-Z_]\w*')] = Field(
        None, description='the name of the parent grammar'
    )
    rules: Dict[constr(pattern=r'^[a-zA-Z_]\w*$'), Rule]
    extras: Optional[List[Rule]] = None
    precedences: Optional[List[List[Rule]]] = None
    externals: Optional[List[Rule]] = None
    inline: Optional[List[constr(pattern=r'^[a-zA-Z_]\w*$')]] = None
    conflicts: Optional[List[List[constr(pattern=r'^[a-zA-Z_]\w*$')]]] = None
    word: Optional[constr(pattern=r'^[a-zA-Z_]\w*')] = None
    supertypes: Optional[List[str]] = Field(
        None,
        description='A list of hidden rule names that should be considered supertypes in the generated node types file. See https://tree-sitter.github.io/tree-sitter/using-parsers#static-node-types.',
    )


class SeqRule(BaseModel):
    type: constr(pattern=r'^SEQ$')
    members: List[Rule]


class ChoiceRule(BaseModel):
    type: constr(pattern=r'^CHOICE$')
    members: List[Rule]


class AliasRule(BaseModel):
    type: constr(pattern=r'^ALIAS$')
    value: str
    named: bool
    content: Rule


class RepeatRule(BaseModel):
    type: constr(pattern=r'^REPEAT$')
    content: Rule


class Repeat1Rule(BaseModel):
    type: constr(pattern=r'^REPEAT1$')
    content: Rule


class TokenRule(BaseModel):
    type: constr(pattern=r'^(TOKEN|IMMEDIATE_TOKEN)$')
    content: Rule


class FieldRule(BaseModel):
    name: str
    type: constr(pattern=r'^FIELD$')
    content: Rule


class PrecRule(BaseModel):
    type: constr(pattern=r'^(PREC|PREC_LEFT|PREC_RIGHT|PREC_DYNAMIC)$')
    value: Any
    content: Rule


class Rule(
    RootModel[
        Union[
            AliasRule,
            BlankRule,
            StringRule,
            PatternRule,
            SymbolRule,
            SeqRule,
            ChoiceRule,
            Repeat1Rule,
            RepeatRule,
            TokenRule,
            FieldRule,
            PrecRule,
        ]
    ]
):
    root: Union[
        AliasRule,
        BlankRule,
        StringRule,
        PatternRule,
        SymbolRule,
        SeqRule,
        ChoiceRule,
        Repeat1Rule,
        RepeatRule,
        TokenRule,
        FieldRule,
        PrecRule,
    ]


TreeSitterGrammarSpecification.model_rebuild()
SeqRule.model_rebuild()
ChoiceRule.model_rebuild()
AliasRule.model_rebuild()
RepeatRule.model_rebuild()
Repeat1Rule.model_rebuild()
TokenRule.model_rebuild()
FieldRule.model_rebuild()
PrecRule.model_rebuild()