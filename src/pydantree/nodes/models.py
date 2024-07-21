from typing import Union

from pydantic import BaseModel, Field, RootModel

__all__ = [
    "NodeType",
    "NodeSchema",
    "NodeTypeNamed",
    "NodeTypeWithSubtypes",
    "NodeTypeWithFields",
    "NodeTypeWithFieldsAndChildren",
    "NodeTypesJson",
]


class NodeType(BaseModel):
    named: bool
    type: str


class NodeSchema(BaseModel):
    multiple: bool
    required: bool
    types: list[NodeType]


class NodeTypeNamed(BaseModel):
    type: str
    named: bool


class NodeTypeWithSubtypes(NodeTypeNamed):
    subtypes: list[NodeType]


class NodeTypeWithFields(NodeTypeNamed):
    fields: dict[str, NodeSchema]


class NodeTypeWithFieldsAndChildren(NodeTypeWithFields):
    children: NodeSchema


NodeTypeVariant = Union[
    NodeTypeNamed,
    NodeTypeWithSubtypes,
    NodeTypeWithFields,
    NodeTypeWithFieldsAndChildren,
]


class NodeTypesJson(RootModel):
    root: list[NodeTypeVariant] = Field(..., alias="node-types")
