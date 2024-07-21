## 0) _declaration_statement


```py
NodeTypeWithSubtypes(
    type="_declaration_statement",
    named=True,
    subtypes=[
        NodeType(named=True, type="associated_type"),
        NodeType(named=True, type="attribute_item"),
        NodeType(named=True, type="const_item"),
        NodeType(named=True, type="empty_statement"),
        NodeType(named=True, type="enum_item"),
        NodeType(named=True, type="extern_crate_declaration"),
        NodeType(named=True, type="foreign_mod_item"),
        NodeType(named=True, type="function_item"),
        NodeType(named=True, type="function_signature_item"),
        NodeType(named=True, type="impl_item"),
        NodeType(named=True, type="inner_attribute_item"),
        NodeType(named=True, type="let_declaration"),
        NodeType(named=True, type="macro_definition"),
        NodeType(named=True, type="macro_invocation"),
        NodeType(named=True, type="mod_item"),
        NodeType(named=True, type="static_item"),
        NodeType(named=True, type="struct_item"),
        NodeType(named=True, type="trait_item"),
        NodeType(named=True, type="type_item"),
        NodeType(named=True, type="union_item"),
        NodeType(named=True, type="use_declaration"),
    ],
)
```
## 1) _expression


```py
NodeTypeWithSubtypes(
    type="_expression",
    named=True,
    subtypes=[
        NodeType(named=True, type="_literal"),
        NodeType(named=True, type="array_expression"),
        NodeType(named=True, type="assignment_expression"),
        NodeType(named=True, type="async_block"),
        NodeType(named=True, type="await_expression"),
        NodeType(named=True, type="binary_expression"),
        NodeType(named=True, type="block"),
        NodeType(named=True, type="break_expression"),
        NodeType(named=True, type="call_expression"),
        NodeType(named=True, type="closure_expression"),
        NodeType(named=True, type="compound_assignment_expr"),
        NodeType(named=True, type="const_block"),
        NodeType(named=True, type="continue_expression"),
        NodeType(named=True, type="field_expression"),
        NodeType(named=True, type="for_expression"),
        NodeType(named=True, type="generic_function"),
        NodeType(named=True, type="identifier"),
        NodeType(named=True, type="if_expression"),
        NodeType(named=True, type="index_expression"),
        NodeType(named=True, type="loop_expression"),
        NodeType(named=True, type="macro_invocation"),
        NodeType(named=True, type="match_expression"),
        NodeType(named=True, type="metavariable"),
        NodeType(named=True, type="parenthesized_expression"),
        NodeType(named=True, type="range_expression"),
        NodeType(named=True, type="reference_expression"),
        NodeType(named=True, type="return_expression"),
        NodeType(named=True, type="scoped_identifier"),
        NodeType(named=True, type="self"),
        NodeType(named=True, type="struct_expression"),
        NodeType(named=True, type="try_block"),
        NodeType(named=True, type="try_expression"),
        NodeType(named=True, type="tuple_expression"),
        NodeType(named=True, type="type_cast_expression"),
        NodeType(named=True, type="unary_expression"),
        NodeType(named=True, type="unit_expression"),
        NodeType(named=True, type="unsafe_block"),
        NodeType(named=True, type="while_expression"),
        NodeType(named=True, type="yield_expression"),
    ],
)
```
## 2) _literal


```py
NodeTypeWithSubtypes(
    type="_literal",
    named=True,
    subtypes=[
        NodeType(named=True, type="boolean_literal"),
        NodeType(named=True, type="char_literal"),
        NodeType(named=True, type="float_literal"),
        NodeType(named=True, type="integer_literal"),
        NodeType(named=True, type="raw_string_literal"),
        NodeType(named=True, type="string_literal"),
    ],
)
```
## 3) _literal_pattern


```py
NodeTypeWithSubtypes(
    type="_literal_pattern",
    named=True,
    subtypes=[
        NodeType(named=True, type="boolean_literal"),
        NodeType(named=True, type="char_literal"),
        NodeType(named=True, type="float_literal"),
        NodeType(named=True, type="integer_literal"),
        NodeType(named=True, type="negative_literal"),
        NodeType(named=True, type="raw_string_literal"),
        NodeType(named=True, type="string_literal"),
    ],
)
```
## 4) _pattern


```py
NodeTypeWithSubtypes(
    type="_pattern",
    named=True,
    subtypes=[
        NodeType(named=False, type="_"),
        NodeType(named=True, type="_literal_pattern"),
        NodeType(named=True, type="captured_pattern"),
        NodeType(named=True, type="const_block"),
        NodeType(named=True, type="identifier"),
        NodeType(named=True, type="macro_invocation"),
        NodeType(named=True, type="mut_pattern"),
        NodeType(named=True, type="or_pattern"),
        NodeType(named=True, type="range_pattern"),
        NodeType(named=True, type="ref_pattern"),
        NodeType(named=True, type="reference_pattern"),
        NodeType(named=True, type="remaining_field_pattern"),
        NodeType(named=True, type="scoped_identifier"),
        NodeType(named=True, type="slice_pattern"),
        NodeType(named=True, type="struct_pattern"),
        NodeType(named=True, type="tuple_pattern"),
        NodeType(named=True, type="tuple_struct_pattern"),
    ],
)
```
## 5) _type


```py
NodeTypeWithSubtypes(
    type="_type",
    named=True,
    subtypes=[
        NodeType(named=True, type="abstract_type"),
        NodeType(named=True, type="array_type"),
        NodeType(named=True, type="bounded_type"),
        NodeType(named=True, type="dynamic_type"),
        NodeType(named=True, type="function_type"),
        NodeType(named=True, type="generic_type"),
        NodeType(named=True, type="macro_invocation"),
        NodeType(named=True, type="metavariable"),
        NodeType(named=True, type="never_type"),
        NodeType(named=True, type="pointer_type"),
        NodeType(named=True, type="primitive_type"),
        NodeType(named=True, type="reference_type"),
        NodeType(named=True, type="removed_trait_bound"),
        NodeType(named=True, type="scoped_type_identifier"),
        NodeType(named=True, type="tuple_type"),
        NodeType(named=True, type="type_identifier"),
        NodeType(named=True, type="unit_type"),
    ],
)
```
## 6) abstract_type


```py
NodeTypeWithFieldsAndChildren(
    type="abstract_type",
    named=True,
    fields={
        "trait": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="function_type"),
                NodeType(named=True, type="generic_type"),
                NodeType(named=True, type="removed_trait_bound"),
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="tuple_type"),
                NodeType(named=True, type="type_identifier"),
            ],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="type_parameters")],
    ),
)
```
## 7) arguments


```py
NodeTypeWithFieldsAndChildren(
    type="arguments",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_expression"),
            NodeType(named=True, type="attribute_item"),
        ],
    ),
)
```
## 8) array_expression


```py
NodeTypeWithFieldsAndChildren(
    type="array_expression",
    named=True,
    fields={
        "length": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_expression")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_expression"),
            NodeType(named=True, type="attribute_item"),
        ],
    ),
)
```
## 9) array_type


```py
NodeTypeWithFields(
    type="array_type",
    named=True,
    fields={
        "element": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "length": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 10) assignment_expression


```py
NodeTypeWithFields(
    type="assignment_expression",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 11) associated_type


```py
NodeTypeWithFieldsAndChildren(
    type="associated_type",
    named=True,
    fields={
        "bounds": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="trait_bounds")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="where_clause")],
    ),
)
```
## 12) async_block


```py
NodeTypeWithFieldsAndChildren(
    type="async_block",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="block")],
    ),
)
```
## 13) attribute


```py
NodeTypeWithFieldsAndChildren(
    type="attribute",
    named=True,
    fields={
        "arguments": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="token_tree")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="scoped_identifier"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
        ],
    ),
)
```
## 14) attribute_item


```py
NodeTypeWithFieldsAndChildren(
    type="attribute_item",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="attribute")],
    ),
)
```
## 15) await_expression


```py
NodeTypeWithFieldsAndChildren(
    type="await_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 16) base_field_initializer


```py
NodeTypeWithFieldsAndChildren(
    type="base_field_initializer",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 17) binary_expression


```py
NodeTypeWithFields(
    type="binary_expression",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
        "operator": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=False, type="!="),
                NodeType(named=False, type="%"),
                NodeType(named=False, type="&"),
                NodeType(named=False, type="&&"),
                NodeType(named=False, type="*"),
                NodeType(named=False, type="+"),
                NodeType(named=False, type="-"),
                NodeType(named=False, type="/"),
                NodeType(named=False, type="<"),
                NodeType(named=False, type="<<"),
                NodeType(named=False, type="<="),
                NodeType(named=False, type="=="),
                NodeType(named=False, type=">"),
                NodeType(named=False, type=">="),
                NodeType(named=False, type=">>"),
                NodeType(named=False, type="^"),
                NodeType(named=False, type="|"),
                NodeType(named=False, type="||"),
            ],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 18) block


```py
NodeTypeWithFieldsAndChildren(
    type="block",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_declaration_statement"),
            NodeType(named=True, type="_expression"),
            NodeType(named=True, type="expression_statement"),
            NodeType(named=True, type="label"),
        ],
    ),
)
```
## 19) block_comment


```py
NodeTypeWithFields(
    type="block_comment",
    named=True,
    fields={
        "doc": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="doc_comment")],
        ),
        "inner": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="inner_doc_comment_marker")
            ],
        ),
        "outer": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="outer_doc_comment_marker")
            ],
        ),
    },
)
```
## 20) boolean_literal


```py
NodeTypeWithFields(type="boolean_literal", named=True, fields={})
```
## 21) bounded_type


```py
NodeTypeWithFieldsAndChildren(
    type="bounded_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_type"),
            NodeType(named=True, type="lifetime"),
        ],
    ),
)
```
## 22) bracketed_type


```py
NodeTypeWithFieldsAndChildren(
    type="bracketed_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="_type"),
            NodeType(named=True, type="qualified_type"),
        ],
    ),
)
```
## 23) break_expression


```py
NodeTypeWithFieldsAndChildren(
    type="break_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_expression"),
            NodeType(named=True, type="label"),
        ],
    ),
)
```
## 24) call_expression


```py
NodeTypeWithFields(
    type="call_expression",
    named=True,
    fields={
        "arguments": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="arguments")],
        ),
        "function": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="_literal"),
                NodeType(named=True, type="array_expression"),
                NodeType(named=True, type="assignment_expression"),
                NodeType(named=True, type="async_block"),
                NodeType(named=True, type="await_expression"),
                NodeType(named=True, type="binary_expression"),
                NodeType(named=True, type="block"),
                NodeType(named=True, type="break_expression"),
                NodeType(named=True, type="call_expression"),
                NodeType(named=True, type="closure_expression"),
                NodeType(named=True, type="compound_assignment_expr"),
                NodeType(named=True, type="const_block"),
                NodeType(named=True, type="continue_expression"),
                NodeType(named=True, type="field_expression"),
                NodeType(named=True, type="for_expression"),
                NodeType(named=True, type="generic_function"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="if_expression"),
                NodeType(named=True, type="index_expression"),
                NodeType(named=True, type="loop_expression"),
                NodeType(named=True, type="macro_invocation"),
                NodeType(named=True, type="match_expression"),
                NodeType(named=True, type="metavariable"),
                NodeType(named=True, type="parenthesized_expression"),
                NodeType(named=True, type="reference_expression"),
                NodeType(named=True, type="return_expression"),
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="self"),
                NodeType(named=True, type="struct_expression"),
                NodeType(named=True, type="try_block"),
                NodeType(named=True, type="try_expression"),
                NodeType(named=True, type="tuple_expression"),
                NodeType(named=True, type="type_cast_expression"),
                NodeType(named=True, type="unary_expression"),
                NodeType(named=True, type="unit_expression"),
                NodeType(named=True, type="unsafe_block"),
                NodeType(named=True, type="while_expression"),
                NodeType(named=True, type="yield_expression"),
            ],
        ),
    },
)
```
## 25) captured_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="captured_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="_pattern")],
    ),
)
```
## 26) closure_expression


```py
NodeTypeWithFields(
    type="closure_expression",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=False, type="_"),
                NodeType(named=True, type="_expression"),
            ],
        ),
        "parameters": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="closure_parameters")],
        ),
        "return_type": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_type")],
        ),
    },
)
```
## 27) closure_parameters


```py
NodeTypeWithFieldsAndChildren(
    type="closure_parameters",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_pattern"),
            NodeType(named=True, type="parameter"),
        ],
    ),
)
```
## 28) compound_assignment_expr


```py
NodeTypeWithFields(
    type="compound_assignment_expr",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
        "operator": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=False, type="%="),
                NodeType(named=False, type="&="),
                NodeType(named=False, type="*="),
                NodeType(named=False, type="+="),
                NodeType(named=False, type="-="),
                NodeType(named=False, type="/="),
                NodeType(named=False, type="<<="),
                NodeType(named=False, type=">>="),
                NodeType(named=False, type="^="),
                NodeType(named=False, type="|="),
            ],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 29) const_block


```py
NodeTypeWithFields(
    type="const_block",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        )
    },
)
```
## 30) const_item


```py
NodeTypeWithFieldsAndChildren(
    type="const_item",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="visibility_modifier")],
    ),
)
```
## 31) const_parameter


```py
NodeTypeWithFields(
    type="const_parameter",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
    },
)
```
## 32) constrained_type_parameter


```py
NodeTypeWithFields(
    type="constrained_type_parameter",
    named=True,
    fields={
        "bounds": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="trait_bounds")],
        ),
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="lifetime"),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
    },
)
```
## 33) continue_expression


```py
NodeTypeWithFieldsAndChildren(
    type="continue_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="label")],
    ),
)
```
## 34) declaration_list


```py
NodeTypeWithFieldsAndChildren(
    type="declaration_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="_declaration_statement")],
    ),
)
```
## 35) dynamic_type


```py
NodeTypeWithFields(
    type="dynamic_type",
    named=True,
    fields={
        "trait": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="function_type"),
                NodeType(named=True, type="generic_type"),
                NodeType(
                    named=True, type="higher_ranked_trait_bound"
                ),
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="type_identifier"),
            ],
        )
    },
)
```
## 36) else_clause


```py
NodeTypeWithFieldsAndChildren(
    type="else_clause",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="block"),
            NodeType(named=True, type="if_expression"),
        ],
    ),
)
```
## 37) empty_statement


```py
NodeTypeWithFields(type="empty_statement", named=True, fields={})
```
## 38) enum_item


```py
NodeTypeWithFieldsAndChildren(
    type="enum_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="enum_variant_list")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="visibility_modifier"),
            NodeType(named=True, type="where_clause"),
        ],
    ),
)
```
## 39) enum_variant


```py
NodeTypeWithFieldsAndChildren(
    type="enum_variant",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="field_declaration_list"),
                NodeType(
                    named=True, type="ordered_field_declaration_list"
                ),
            ],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="visibility_modifier")],
    ),
)
```
## 40) enum_variant_list


```py
NodeTypeWithFieldsAndChildren(
    type="enum_variant_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="attribute_item"),
            NodeType(named=True, type="enum_variant"),
        ],
    ),
)
```
## 41) expression_statement


```py
NodeTypeWithFieldsAndChildren(
    type="expression_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 42) extern_crate_declaration


```py
NodeTypeWithFieldsAndChildren(
    type="extern_crate_declaration",
    named=True,
    fields={
        "alias": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="identifier")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="visibility_modifier"),
        ],
    ),
)
```
## 43) extern_modifier


```py
NodeTypeWithFieldsAndChildren(
    type="extern_modifier",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="string_literal")],
    ),
)
```
## 44) field_declaration


```py
NodeTypeWithFieldsAndChildren(
    type="field_declaration",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="field_identifier")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="visibility_modifier")],
    ),
)
```
## 45) field_declaration_list


```py
NodeTypeWithFieldsAndChildren(
    type="field_declaration_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="attribute_item"),
            NodeType(named=True, type="field_declaration"),
        ],
    ),
)
```
## 46) field_expression


```py
NodeTypeWithFields(
    type="field_expression",
    named=True,
    fields={
        "field": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="field_identifier"),
                NodeType(named=True, type="integer_literal"),
            ],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 47) field_initializer


```py
NodeTypeWithFieldsAndChildren(
    type="field_initializer",
    named=True,
    fields={
        "field": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="field_identifier"),
                NodeType(named=True, type="integer_literal"),
            ],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="attribute_item")],
    ),
)
```
## 48) field_initializer_list


```py
NodeTypeWithFieldsAndChildren(
    type="field_initializer_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="base_field_initializer"),
            NodeType(named=True, type="field_initializer"),
            NodeType(named=True, type="shorthand_field_initializer"),
        ],
    ),
)
```
## 49) field_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="field_pattern",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="field_identifier"),
                NodeType(
                    named=True, type="shorthand_field_identifier"
                ),
            ],
        ),
        "pattern": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_pattern")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="mutable_specifier")],
    ),
)
```
## 50) for_expression


```py
NodeTypeWithFieldsAndChildren(
    type="for_expression",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
        "pattern": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_pattern")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="label")],
    ),
)
```
## 51) for_lifetimes


```py
NodeTypeWithFieldsAndChildren(
    type="for_lifetimes",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="lifetime")],
    ),
)
```
## 52) foreign_mod_item


```py
NodeTypeWithFieldsAndChildren(
    type="foreign_mod_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="declaration_list")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="extern_modifier"),
            NodeType(named=True, type="visibility_modifier"),
        ],
    ),
)
```
## 53) fragment_specifier


```py
NodeTypeWithFields(type="fragment_specifier", named=True, fields={})
```
## 54) function_item


```py
NodeTypeWithFieldsAndChildren(
    type="function_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="metavariable"),
            ],
        ),
        "parameters": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="parameters")],
        ),
        "return_type": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_type")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="function_modifiers"),
            NodeType(named=True, type="visibility_modifier"),
            NodeType(named=True, type="where_clause"),
        ],
    ),
)
```
## 55) function_modifiers


```py
NodeTypeWithFieldsAndChildren(
    type="function_modifiers",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="extern_modifier")],
    ),
)
```
## 56) function_signature_item


```py
NodeTypeWithFieldsAndChildren(
    type="function_signature_item",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="metavariable"),
            ],
        ),
        "parameters": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="parameters")],
        ),
        "return_type": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_type")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="function_modifiers"),
            NodeType(named=True, type="visibility_modifier"),
            NodeType(named=True, type="where_clause"),
        ],
    ),
)
```
## 57) function_type


```py
NodeTypeWithFieldsAndChildren(
    type="function_type",
    named=True,
    fields={
        "parameters": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="parameters")],
        ),
        "return_type": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_type")],
        ),
        "trait": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="for_lifetimes"),
            NodeType(named=True, type="function_modifiers"),
        ],
    ),
)
```
## 58) generic_function


```py
NodeTypeWithFields(
    type="generic_function",
    named=True,
    fields={
        "function": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="field_expression"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="scoped_identifier"),
            ],
        ),
        "type_arguments": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_arguments")],
        ),
    },
)
```
## 59) generic_type


```py
NodeTypeWithFields(
    type="generic_type",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
        "type_arguments": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_arguments")],
        ),
    },
)
```
## 60) generic_type_with_turbofish


```py
NodeTypeWithFields(
    type="generic_type_with_turbofish",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
        "type_arguments": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_arguments")],
        ),
    },
)
```
## 61) higher_ranked_trait_bound


```py
NodeTypeWithFields(
    type="higher_ranked_trait_bound",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
)
```
## 62) if_expression


```py
NodeTypeWithFields(
    type="if_expression",
    named=True,
    fields={
        "alternative": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="else_clause")],
        ),
        "condition": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="_expression"),
                NodeType(named=True, type="let_chain"),
                NodeType(named=True, type="let_condition"),
            ],
        ),
        "consequence": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
    },
)
```
## 63) impl_item


```py
NodeTypeWithFieldsAndChildren(
    type="impl_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="declaration_list")],
        ),
        "trait": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="generic_type"),
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="where_clause")],
    ),
)
```
## 64) index_expression


```py
NodeTypeWithFieldsAndChildren(
    type="index_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 65) inner_attribute_item


```py
NodeTypeWithFieldsAndChildren(
    type="inner_attribute_item",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="attribute")],
    ),
)
```
## 66) label


```py
NodeTypeWithFieldsAndChildren(
    type="label",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="identifier")],
    ),
)
```
## 67) let_chain


```py
NodeTypeWithFieldsAndChildren(
    type="let_chain",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_expression"),
            NodeType(named=True, type="let_condition"),
        ],
    ),
)
```
## 68) let_condition


```py
NodeTypeWithFields(
    type="let_condition",
    named=True,
    fields={
        "pattern": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_pattern")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 69) let_declaration


```py
NodeTypeWithFieldsAndChildren(
    type="let_declaration",
    named=True,
    fields={
        "alternative": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="block")],
        ),
        "pattern": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_pattern")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_type")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="mutable_specifier")],
    ),
)
```
## 70) lifetime


```py
NodeTypeWithFieldsAndChildren(
    type="lifetime",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="identifier")],
    ),
)
```
## 71) line_comment


```py
NodeTypeWithFields(
    type="line_comment",
    named=True,
    fields={
        "doc": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="doc_comment")],
        ),
        "inner": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="inner_doc_comment_marker")
            ],
        ),
        "outer": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="outer_doc_comment_marker")
            ],
        ),
    },
)
```
## 72) loop_expression


```py
NodeTypeWithFieldsAndChildren(
    type="loop_expression",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="label")],
    ),
)
```
## 73) macro_definition


```py
NodeTypeWithFieldsAndChildren(
    type="macro_definition",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="macro_rule")],
    ),
)
```
## 74) macro_invocation


```py
NodeTypeWithFieldsAndChildren(
    type="macro_invocation",
    named=True,
    fields={
        "macro": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="scoped_identifier"),
            ],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="token_tree")],
    ),
)
```
## 75) macro_rule


```py
NodeTypeWithFields(
    type="macro_rule",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="token_tree_pattern")],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="token_tree")],
        ),
    },
)
```
## 76) match_arm


```py
NodeTypeWithFieldsAndChildren(
    type="match_arm",
    named=True,
    fields={
        "pattern": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="match_pattern")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="attribute_item"),
            NodeType(named=True, type="inner_attribute_item"),
        ],
    ),
)
```
## 77) match_block


```py
NodeTypeWithFieldsAndChildren(
    type="match_block",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="match_arm")],
    ),
)
```
## 78) match_expression


```py
NodeTypeWithFields(
    type="match_expression",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="match_block")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 79) match_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="match_pattern",
    named=True,
    fields={
        "condition": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="_expression"),
                NodeType(named=True, type="let_chain"),
                NodeType(named=True, type="let_condition"),
            ],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_pattern")],
    ),
)
```
## 80) mod_item


```py
NodeTypeWithFieldsAndChildren(
    type="mod_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="declaration_list")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="visibility_modifier")],
    ),
)
```
## 81) mut_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="mut_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_pattern"),
            NodeType(named=True, type="mutable_specifier"),
        ],
    ),
)
```
## 82) negative_literal


```py
NodeTypeWithFieldsAndChildren(
    type="negative_literal",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="float_literal"),
            NodeType(named=True, type="integer_literal"),
        ],
    ),
)
```
## 83) never_type


```py
NodeTypeWithFields(type="never_type", named=True, fields={})
```
## 84) optional_type_parameter


```py
NodeTypeWithFields(
    type="optional_type_parameter",
    named=True,
    fields={
        "default_type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(
                    named=True, type="constrained_type_parameter"
                ),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
    },
)
```
## 85) or_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="or_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="_pattern")],
    ),
)
```
## 86) ordered_field_declaration_list


```py
NodeTypeWithFieldsAndChildren(
    type="ordered_field_declaration_list",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=True,
            required=False,
            types=[NodeType(named=True, type="_type")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="attribute_item"),
            NodeType(named=True, type="visibility_modifier"),
        ],
    ),
)
```
## 87) parameter


```py
NodeTypeWithFieldsAndChildren(
    type="parameter",
    named=True,
    fields={
        "pattern": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="_pattern"),
                NodeType(named=True, type="self"),
            ],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="mutable_specifier")],
    ),
)
```
## 88) parameters


```py
NodeTypeWithFieldsAndChildren(
    type="parameters",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_type"),
            NodeType(named=True, type="attribute_item"),
            NodeType(named=True, type="parameter"),
            NodeType(named=True, type="self_parameter"),
            NodeType(named=True, type="variadic_parameter"),
        ],
    ),
)
```
## 89) parenthesized_expression


```py
NodeTypeWithFieldsAndChildren(
    type="parenthesized_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 90) pointer_type


```py
NodeTypeWithFieldsAndChildren(
    type="pointer_type",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="mutable_specifier")],
    ),
)
```
## 91) qualified_type


```py
NodeTypeWithFields(
    type="qualified_type",
    named=True,
    fields={
        "alias": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
    },
)
```
## 92) range_expression


```py
NodeTypeWithFieldsAndChildren(
    type="range_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 93) range_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="range_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_literal_pattern"),
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="scoped_identifier"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
        ],
    ),
)
```
## 94) raw_string_literal


```py
NodeTypeWithFieldsAndChildren(
    type="raw_string_literal",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="string_content")],
    ),
)
```
## 95) ref_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="ref_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_pattern")],
    ),
)
```
## 96) reference_expression


```py
NodeTypeWithFieldsAndChildren(
    type="reference_expression",
    named=True,
    fields={
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="mutable_specifier")],
    ),
)
```
## 97) reference_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="reference_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_pattern"),
            NodeType(named=True, type="mutable_specifier"),
        ],
    ),
)
```
## 98) reference_type


```py
NodeTypeWithFieldsAndChildren(
    type="reference_type",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="lifetime"),
            NodeType(named=True, type="mutable_specifier"),
        ],
    ),
)
```
## 99) remaining_field_pattern


```py
NodeTypeWithFields(
    type="remaining_field_pattern", named=True, fields={}
)
```
## 100) removed_trait_bound


```py
NodeTypeWithFieldsAndChildren(
    type="removed_trait_bound",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_type")],
    ),
)
```
## 101) return_expression


```py
NodeTypeWithFieldsAndChildren(
    type="return_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 102) scoped_identifier


```py
NodeTypeWithFields(
    type="scoped_identifier",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="super"),
            ],
        ),
        "path": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="bracketed_type"),
                NodeType(named=True, type="crate"),
                NodeType(named=True, type="generic_type"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="metavariable"),
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="self"),
                NodeType(named=True, type="super"),
            ],
        ),
    },
)
```
## 103) scoped_type_identifier


```py
NodeTypeWithFields(
    type="scoped_type_identifier",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "path": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="bracketed_type"),
                NodeType(named=True, type="crate"),
                NodeType(named=True, type="generic_type"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="metavariable"),
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="self"),
                NodeType(named=True, type="super"),
            ],
        ),
    },
)
```
## 104) scoped_use_list


```py
NodeTypeWithFields(
    type="scoped_use_list",
    named=True,
    fields={
        "list": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="use_list")],
        ),
        "path": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="crate"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="metavariable"),
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="self"),
                NodeType(named=True, type="super"),
            ],
        ),
    },
)
```
## 105) self_parameter


```py
NodeTypeWithFieldsAndChildren(
    type="self_parameter",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="lifetime"),
            NodeType(named=True, type="mutable_specifier"),
            NodeType(named=True, type="self"),
        ],
    ),
)
```
## 106) shorthand_field_initializer


```py
NodeTypeWithFieldsAndChildren(
    type="shorthand_field_initializer",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="attribute_item"),
            NodeType(named=True, type="identifier"),
        ],
    ),
)
```
## 107) slice_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="slice_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="_pattern")],
    ),
)
```
## 108) source_file


```py
NodeTypeWithFieldsAndChildren(
    type="source_file",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_declaration_statement"),
            NodeType(named=True, type="expression_statement"),
            NodeType(named=True, type="shebang"),
        ],
    ),
)
```
## 109) static_item


```py
NodeTypeWithFieldsAndChildren(
    type="static_item",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="mutable_specifier"),
            NodeType(named=True, type="visibility_modifier"),
        ],
    ),
)
```
## 110) string_literal


```py
NodeTypeWithFieldsAndChildren(
    type="string_literal",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="escape_sequence"),
            NodeType(named=True, type="string_content"),
        ],
    ),
)
```
## 111) struct_expression


```py
NodeTypeWithFields(
    type="struct_expression",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="field_initializer_list")
            ],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(
                    named=True, type="generic_type_with_turbofish"
                ),
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
    },
)
```
## 112) struct_item


```py
NodeTypeWithFieldsAndChildren(
    type="struct_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="field_declaration_list"),
                NodeType(
                    named=True, type="ordered_field_declaration_list"
                ),
            ],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="visibility_modifier"),
            NodeType(named=True, type="where_clause"),
        ],
    ),
)
```
## 113) struct_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="struct_pattern",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="type_identifier"),
            ],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="field_pattern"),
            NodeType(named=True, type="remaining_field_pattern"),
        ],
    ),
)
```
## 114) token_binding_pattern


```py
NodeTypeWithFields(
    type="token_binding_pattern",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="metavariable")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="fragment_specifier")],
        ),
    },
)
```
## 115) token_repetition


```py
NodeTypeWithFieldsAndChildren(
    type="token_repetition",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_literal"),
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="mutable_specifier"),
            NodeType(named=True, type="primitive_type"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
            NodeType(named=True, type="token_repetition"),
            NodeType(named=True, type="token_tree"),
        ],
    ),
)
```
## 116) token_repetition_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="token_repetition_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_literal"),
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="mutable_specifier"),
            NodeType(named=True, type="primitive_type"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
            NodeType(named=True, type="token_binding_pattern"),
            NodeType(named=True, type="token_repetition_pattern"),
            NodeType(named=True, type="token_tree_pattern"),
        ],
    ),
)
```
## 117) token_tree


```py
NodeTypeWithFieldsAndChildren(
    type="token_tree",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_literal"),
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="mutable_specifier"),
            NodeType(named=True, type="primitive_type"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
            NodeType(named=True, type="token_repetition"),
            NodeType(named=True, type="token_tree"),
        ],
    ),
)
```
## 118) token_tree_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="token_tree_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_literal"),
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="mutable_specifier"),
            NodeType(named=True, type="primitive_type"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
            NodeType(named=True, type="token_binding_pattern"),
            NodeType(named=True, type="token_repetition_pattern"),
            NodeType(named=True, type="token_tree_pattern"),
        ],
    ),
)
```
## 119) trait_bounds


```py
NodeTypeWithFieldsAndChildren(
    type="trait_bounds",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_type"),
            NodeType(named=True, type="higher_ranked_trait_bound"),
            NodeType(named=True, type="lifetime"),
        ],
    ),
)
```
## 120) trait_item


```py
NodeTypeWithFieldsAndChildren(
    type="trait_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="declaration_list")],
        ),
        "bounds": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="trait_bounds")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="visibility_modifier"),
            NodeType(named=True, type="where_clause"),
        ],
    ),
)
```
## 121) try_block


```py
NodeTypeWithFieldsAndChildren(
    type="try_block",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="block")],
    ),
)
```
## 122) try_expression


```py
NodeTypeWithFieldsAndChildren(
    type="try_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 123) tuple_expression


```py
NodeTypeWithFieldsAndChildren(
    type="tuple_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_expression"),
            NodeType(named=True, type="attribute_item"),
        ],
    ),
)
```
## 124) tuple_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="tuple_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_pattern"),
            NodeType(named=True, type="closure_expression"),
        ],
    ),
)
```
## 125) tuple_struct_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="tuple_struct_pattern",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="generic_type"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="scoped_identifier"),
            ],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="_pattern")],
    ),
)
```
## 126) tuple_type


```py
NodeTypeWithFieldsAndChildren(
    type="tuple_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="_type")],
    ),
)
```
## 127) type_arguments


```py
NodeTypeWithFieldsAndChildren(
    type="type_arguments",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="_literal"),
            NodeType(named=True, type="_type"),
            NodeType(named=True, type="block"),
            NodeType(named=True, type="lifetime"),
            NodeType(named=True, type="trait_bounds"),
            NodeType(named=True, type="type_binding"),
        ],
    ),
)
```
## 128) type_binding


```py
NodeTypeWithFields(
    type="type_binding",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "type_arguments": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_arguments")],
        ),
    },
)
```
## 129) type_cast_expression


```py
NodeTypeWithFields(
    type="type_cast_expression",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_expression")],
        ),
    },
)
```
## 130) type_item


```py
NodeTypeWithFieldsAndChildren(
    type="type_item",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="_type")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="visibility_modifier"),
            NodeType(named=True, type="where_clause"),
        ],
    ),
)
```
## 131) type_parameters


```py
NodeTypeWithFieldsAndChildren(
    type="type_parameters",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="attribute_item"),
            NodeType(named=True, type="const_parameter"),
            NodeType(named=True, type="constrained_type_parameter"),
            NodeType(named=True, type="lifetime"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="optional_type_parameter"),
            NodeType(named=True, type="type_identifier"),
        ],
    ),
)
```
## 132) unary_expression


```py
NodeTypeWithFieldsAndChildren(
    type="unary_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 133) union_item


```py
NodeTypeWithFieldsAndChildren(
    type="union_item",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="field_declaration_list")
            ],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type_identifier")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameters")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="visibility_modifier"),
            NodeType(named=True, type="where_clause"),
        ],
    ),
)
```
## 134) unit_expression


```py
NodeTypeWithFields(type="unit_expression", named=True, fields={})
```
## 135) unit_type


```py
NodeTypeWithFields(type="unit_type", named=True, fields={})
```
## 136) unsafe_block


```py
NodeTypeWithFieldsAndChildren(
    type="unsafe_block",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="block")],
    ),
)
```
## 137) use_as_clause


```py
NodeTypeWithFields(
    type="use_as_clause",
    named=True,
    fields={
        "alias": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "path": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="crate"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="metavariable"),
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="self"),
                NodeType(named=True, type="super"),
            ],
        ),
    },
)
```
## 138) use_declaration


```py
NodeTypeWithFieldsAndChildren(
    type="use_declaration",
    named=True,
    fields={
        "argument": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="crate"),
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="metavariable"),
                NodeType(named=True, type="scoped_identifier"),
                NodeType(named=True, type="scoped_use_list"),
                NodeType(named=True, type="self"),
                NodeType(named=True, type="super"),
                NodeType(named=True, type="use_as_clause"),
                NodeType(named=True, type="use_list"),
                NodeType(named=True, type="use_wildcard"),
            ],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="visibility_modifier")],
    ),
)
```
## 139) use_list


```py
NodeTypeWithFieldsAndChildren(
    type="use_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="scoped_identifier"),
            NodeType(named=True, type="scoped_use_list"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
            NodeType(named=True, type="use_as_clause"),
            NodeType(named=True, type="use_list"),
            NodeType(named=True, type="use_wildcard"),
        ],
    ),
)
```
## 140) use_wildcard


```py
NodeTypeWithFieldsAndChildren(
    type="use_wildcard",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="scoped_identifier"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
        ],
    ),
)
```
## 141) variadic_parameter


```py
NodeTypeWithFieldsAndChildren(
    type="variadic_parameter",
    named=True,
    fields={
        "pattern": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="_pattern")],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="mutable_specifier")],
    ),
)
```
## 142) visibility_modifier


```py
NodeTypeWithFieldsAndChildren(
    type="visibility_modifier",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[
            NodeType(named=True, type="crate"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="metavariable"),
            NodeType(named=True, type="scoped_identifier"),
            NodeType(named=True, type="self"),
            NodeType(named=True, type="super"),
        ],
    ),
)
```
## 143) where_clause


```py
NodeTypeWithFieldsAndChildren(
    type="where_clause",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="where_predicate")],
    ),
)
```
## 144) where_predicate


```py
NodeTypeWithFields(
    type="where_predicate",
    named=True,
    fields={
        "bounds": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="trait_bounds")],
        ),
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="array_type"),
                NodeType(named=True, type="generic_type"),
                NodeType(
                    named=True, type="higher_ranked_trait_bound"
                ),
                NodeType(named=True, type="lifetime"),
                NodeType(named=True, type="pointer_type"),
                NodeType(named=True, type="primitive_type"),
                NodeType(named=True, type="reference_type"),
                NodeType(named=True, type="scoped_type_identifier"),
                NodeType(named=True, type="tuple_type"),
                NodeType(named=True, type="type_identifier"),
            ],
        ),
    },
)
```
## 145) while_expression


```py
NodeTypeWithFieldsAndChildren(
    type="while_expression",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
        "condition": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="_expression"),
                NodeType(named=True, type="let_chain"),
                NodeType(named=True, type="let_condition"),
            ],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="label")],
    ),
)
```
## 146) yield_expression


```py
NodeTypeWithFieldsAndChildren(
    type="yield_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="_expression")],
    ),
)
```
## 147) !


```py
NodeTypeNamed(type="!", named=False)
```
## 148) !=


```py
NodeTypeNamed(type="!=", named=False)
```
## 149) "


```py
NodeTypeNamed(type='"', named=False)
```
## 150) #


```py
NodeTypeNamed(type="#", named=False)
```
## 151) $


```py
NodeTypeNamed(type="$", named=False)
```
## 152) %


```py
NodeTypeNamed(type="%", named=False)
```
## 153) %=


```py
NodeTypeNamed(type="%=", named=False)
```
## 154) &


```py
NodeTypeNamed(type="&", named=False)
```
## 155) &&


```py
NodeTypeNamed(type="&&", named=False)
```
## 156) &=


```py
NodeTypeNamed(type="&=", named=False)
```
## 157) '


```py
NodeTypeNamed(type="'", named=False)
```
## 158) (


```py
NodeTypeNamed(type="(", named=False)
```
## 159) )


```py
NodeTypeNamed(type=")", named=False)
```
## 160) *


```py
NodeTypeNamed(type="*", named=False)
```
## 161) */


```py
NodeTypeNamed(type="*/", named=False)
```
## 162) *=


```py
NodeTypeNamed(type="*=", named=False)
```
## 163) +


```py
NodeTypeNamed(type="+", named=False)
```
## 164) +=


```py
NodeTypeNamed(type="+=", named=False)
```
## 165) ,


```py
NodeTypeNamed(type=",", named=False)
```
## 166) -


```py
NodeTypeNamed(type="-", named=False)
```
## 167) -=


```py
NodeTypeNamed(type="-=", named=False)
```
## 168) ->


```py
NodeTypeNamed(type="->", named=False)
```
## 169) .


```py
NodeTypeNamed(type=".", named=False)
```
## 170) ..


```py
NodeTypeNamed(type="..", named=False)
```
## 171) ...


```py
NodeTypeNamed(type="...", named=False)
```
## 172) ..=


```py
NodeTypeNamed(type="..=", named=False)
```
## 173) /


```py
NodeTypeNamed(type="/", named=False)
```
## 174) /*


```py
NodeTypeNamed(type="/*", named=False)
```
## 175) //


```py
NodeTypeNamed(type="//", named=False)
```
## 176) /=


```py
NodeTypeNamed(type="/=", named=False)
```
## 177) :


```py
NodeTypeNamed(type=":", named=False)
```
## 178) ::


```py
NodeTypeNamed(type="::", named=False)
```
## 179) ;


```py
NodeTypeNamed(type=";", named=False)
```
## 180) <


```py
NodeTypeNamed(type="<", named=False)
```
## 181) <<


```py
NodeTypeNamed(type="<<", named=False)
```
## 182) <<=


```py
NodeTypeNamed(type="<<=", named=False)
```
## 183) <=


```py
NodeTypeNamed(type="<=", named=False)
```
## 184) =


```py
NodeTypeNamed(type="=", named=False)
```
## 185) ==


```py
NodeTypeNamed(type="==", named=False)
```
## 186) =>


```py
NodeTypeNamed(type="=>", named=False)
```
## 187) >


```py
NodeTypeNamed(type=">", named=False)
```
## 188) >=


```py
NodeTypeNamed(type=">=", named=False)
```
## 189) >>


```py
NodeTypeNamed(type=">>", named=False)
```
## 190) >>=


```py
NodeTypeNamed(type=">>=", named=False)
```
## 191) ?


```py
NodeTypeNamed(type="?", named=False)
```
## 192) @


```py
NodeTypeNamed(type="@", named=False)
```
## 193) [


```py
NodeTypeNamed(type="[", named=False)
```
## 194) ]


```py
NodeTypeNamed(type="]", named=False)
```
## 195) ^


```py
NodeTypeNamed(type="^", named=False)
```
## 196) ^=


```py
NodeTypeNamed(type="^=", named=False)
```
## 197) _


```py
NodeTypeNamed(type="_", named=False)
```
## 198) as


```py
NodeTypeNamed(type="as", named=False)
```
## 199) async


```py
NodeTypeNamed(type="async", named=False)
```
## 200) await


```py
NodeTypeNamed(type="await", named=False)
```
## 201) block


```py
NodeTypeNamed(type="block", named=False)
```
## 202) break


```py
NodeTypeNamed(type="break", named=False)
```
## 203) char_literal


```py
NodeTypeNamed(type="char_literal", named=True)
```
## 204) const


```py
NodeTypeNamed(type="const", named=False)
```
## 205) continue


```py
NodeTypeNamed(type="continue", named=False)
```
## 206) crate


```py
NodeTypeNamed(type="crate", named=True)
```
## 207) default


```py
NodeTypeNamed(type="default", named=False)
```
## 208) doc_comment


```py
NodeTypeNamed(type="doc_comment", named=True)
```
## 209) dyn


```py
NodeTypeNamed(type="dyn", named=False)
```
## 210) else


```py
NodeTypeNamed(type="else", named=False)
```
## 211) enum


```py
NodeTypeNamed(type="enum", named=False)
```
## 212) escape_sequence


```py
NodeTypeNamed(type="escape_sequence", named=True)
```
## 213) expr


```py
NodeTypeNamed(type="expr", named=False)
```
## 214) extern


```py
NodeTypeNamed(type="extern", named=False)
```
## 215) false


```py
NodeTypeNamed(type="false", named=False)
```
## 216) field_identifier


```py
NodeTypeNamed(type="field_identifier", named=True)
```
## 217) float_literal


```py
NodeTypeNamed(type="float_literal", named=True)
```
## 218) fn


```py
NodeTypeNamed(type="fn", named=False)
```
## 219) for


```py
NodeTypeNamed(type="for", named=False)
```
## 220) ident


```py
NodeTypeNamed(type="ident", named=False)
```
## 221) identifier


```py
NodeTypeNamed(type="identifier", named=True)
```
## 222) if


```py
NodeTypeNamed(type="if", named=False)
```
## 223) impl


```py
NodeTypeNamed(type="impl", named=False)
```
## 224) in


```py
NodeTypeNamed(type="in", named=False)
```
## 225) inner_doc_comment_marker


```py
NodeTypeNamed(type="inner_doc_comment_marker", named=True)
```
## 226) integer_literal


```py
NodeTypeNamed(type="integer_literal", named=True)
```
## 227) item


```py
NodeTypeNamed(type="item", named=False)
```
## 228) let


```py
NodeTypeNamed(type="let", named=False)
```
## 229) lifetime


```py
NodeTypeNamed(type="lifetime", named=False)
```
## 230) literal


```py
NodeTypeNamed(type="literal", named=False)
```
## 231) loop


```py
NodeTypeNamed(type="loop", named=False)
```
## 232) macro_rules!


```py
NodeTypeNamed(type="macro_rules!", named=False)
```
## 233) match


```py
NodeTypeNamed(type="match", named=False)
```
## 234) meta


```py
NodeTypeNamed(type="meta", named=False)
```
## 235) metavariable


```py
NodeTypeNamed(type="metavariable", named=True)
```
## 236) mod


```py
NodeTypeNamed(type="mod", named=False)
```
## 237) move


```py
NodeTypeNamed(type="move", named=False)
```
## 238) mutable_specifier


```py
NodeTypeNamed(type="mutable_specifier", named=True)
```
## 239) outer_doc_comment_marker


```py
NodeTypeNamed(type="outer_doc_comment_marker", named=True)
```
## 240) pat


```py
NodeTypeNamed(type="pat", named=False)
```
## 241) path


```py
NodeTypeNamed(type="path", named=False)
```
## 242) primitive_type


```py
NodeTypeNamed(type="primitive_type", named=True)
```
## 243) pub


```py
NodeTypeNamed(type="pub", named=False)
```
## 244) ref


```py
NodeTypeNamed(type="ref", named=False)
```
## 245) return


```py
NodeTypeNamed(type="return", named=False)
```
## 246) self


```py
NodeTypeNamed(type="self", named=True)
```
## 247) shebang


```py
NodeTypeNamed(type="shebang", named=True)
```
## 248) shorthand_field_identifier


```py
NodeTypeNamed(type="shorthand_field_identifier", named=True)
```
## 249) static


```py
NodeTypeNamed(type="static", named=False)
```
## 250) stmt


```py
NodeTypeNamed(type="stmt", named=False)
```
## 251) string_content


```py
NodeTypeNamed(type="string_content", named=True)
```
## 252) struct


```py
NodeTypeNamed(type="struct", named=False)
```
## 253) super


```py
NodeTypeNamed(type="super", named=True)
```
## 254) trait


```py
NodeTypeNamed(type="trait", named=False)
```
## 255) true


```py
NodeTypeNamed(type="true", named=False)
```
## 256) try


```py
NodeTypeNamed(type="try", named=False)
```
## 257) tt


```py
NodeTypeNamed(type="tt", named=False)
```
## 258) ty


```py
NodeTypeNamed(type="ty", named=False)
```
## 259) type


```py
NodeTypeNamed(type="type", named=False)
```
## 260) type_identifier


```py
NodeTypeNamed(type="type_identifier", named=True)
```
## 261) union


```py
NodeTypeNamed(type="union", named=False)
```
## 262) unsafe


```py
NodeTypeNamed(type="unsafe", named=False)
```
## 263) use


```py
NodeTypeNamed(type="use", named=False)
```
## 264) vis


```py
NodeTypeNamed(type="vis", named=False)
```
## 265) where


```py
NodeTypeNamed(type="where", named=False)
```
## 266) while


```py
NodeTypeNamed(type="while", named=False)
```
## 267) yield


```py
NodeTypeNamed(type="yield", named=False)
```
## 268) {


```py
NodeTypeNamed(type="{", named=False)
```
## 269) |


```py
NodeTypeNamed(type="|", named=False)
```
## 270) |=


```py
NodeTypeNamed(type="|=", named=False)
```
## 271) ||


```py
NodeTypeNamed(type="||", named=False)
```
## 272) }


```py
NodeTypeNamed(type="}", named=False)
```
