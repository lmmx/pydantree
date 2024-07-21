## 0) _compound_statement


```py
NodeTypeWithSubtypes(
    type="_compound_statement",
    named=True,
    subtypes=[
        NodeType(named=True, type="class_definition"),
        NodeType(named=True, type="decorated_definition"),
        NodeType(named=True, type="for_statement"),
        NodeType(named=True, type="function_definition"),
        NodeType(named=True, type="if_statement"),
        NodeType(named=True, type="match_statement"),
        NodeType(named=True, type="try_statement"),
        NodeType(named=True, type="while_statement"),
        NodeType(named=True, type="with_statement"),
    ],
)
```
## 1) _simple_statement


```py
NodeTypeWithSubtypes(
    type="_simple_statement",
    named=True,
    subtypes=[
        NodeType(named=True, type="assert_statement"),
        NodeType(named=True, type="break_statement"),
        NodeType(named=True, type="continue_statement"),
        NodeType(named=True, type="delete_statement"),
        NodeType(named=True, type="exec_statement"),
        NodeType(named=True, type="expression_statement"),
        NodeType(named=True, type="future_import_statement"),
        NodeType(named=True, type="global_statement"),
        NodeType(named=True, type="import_from_statement"),
        NodeType(named=True, type="import_statement"),
        NodeType(named=True, type="nonlocal_statement"),
        NodeType(named=True, type="pass_statement"),
        NodeType(named=True, type="print_statement"),
        NodeType(named=True, type="raise_statement"),
        NodeType(named=True, type="return_statement"),
        NodeType(named=True, type="type_alias_statement"),
    ],
)
```
## 2) expression


```py
NodeTypeWithSubtypes(
    type="expression",
    named=True,
    subtypes=[
        NodeType(named=True, type="as_pattern"),
        NodeType(named=True, type="boolean_operator"),
        NodeType(named=True, type="comparison_operator"),
        NodeType(named=True, type="conditional_expression"),
        NodeType(named=True, type="lambda"),
        NodeType(named=True, type="named_expression"),
        NodeType(named=True, type="not_operator"),
        NodeType(named=True, type="primary_expression"),
    ],
)
```
## 3) parameter


```py
NodeTypeWithSubtypes(
    type="parameter",
    named=True,
    subtypes=[
        NodeType(named=True, type="default_parameter"),
        NodeType(named=True, type="dictionary_splat_pattern"),
        NodeType(named=True, type="identifier"),
        NodeType(named=True, type="keyword_separator"),
        NodeType(named=True, type="list_splat_pattern"),
        NodeType(named=True, type="positional_separator"),
        NodeType(named=True, type="tuple_pattern"),
        NodeType(named=True, type="typed_default_parameter"),
        NodeType(named=True, type="typed_parameter"),
    ],
)
```
## 4) pattern


```py
NodeTypeWithSubtypes(
    type="pattern",
    named=True,
    subtypes=[
        NodeType(named=True, type="attribute"),
        NodeType(named=True, type="identifier"),
        NodeType(named=True, type="list_pattern"),
        NodeType(named=True, type="list_splat_pattern"),
        NodeType(named=True, type="subscript"),
        NodeType(named=True, type="tuple_pattern"),
    ],
)
```
## 5) primary_expression


```py
NodeTypeWithSubtypes(
    type="primary_expression",
    named=True,
    subtypes=[
        NodeType(named=True, type="attribute"),
        NodeType(named=True, type="await"),
        NodeType(named=True, type="binary_operator"),
        NodeType(named=True, type="call"),
        NodeType(named=True, type="concatenated_string"),
        NodeType(named=True, type="dictionary"),
        NodeType(named=True, type="dictionary_comprehension"),
        NodeType(named=True, type="ellipsis"),
        NodeType(named=True, type="false"),
        NodeType(named=True, type="float"),
        NodeType(named=True, type="generator_expression"),
        NodeType(named=True, type="identifier"),
        NodeType(named=True, type="integer"),
        NodeType(named=True, type="list"),
        NodeType(named=True, type="list_comprehension"),
        NodeType(named=True, type="list_splat"),
        NodeType(named=True, type="none"),
        NodeType(named=True, type="parenthesized_expression"),
        NodeType(named=True, type="set"),
        NodeType(named=True, type="set_comprehension"),
        NodeType(named=True, type="string"),
        NodeType(named=True, type="subscript"),
        NodeType(named=True, type="true"),
        NodeType(named=True, type="tuple"),
        NodeType(named=True, type="unary_operator"),
    ],
)
```
## 6) aliased_import


```py
NodeTypeWithFields(
    type="aliased_import",
    named=True,
    fields={
        "alias": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="dotted_name")],
        ),
    },
)
```
## 7) argument_list


```py
NodeTypeWithFieldsAndChildren(
    type="argument_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="dictionary_splat"),
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="keyword_argument"),
            NodeType(named=True, type="list_splat"),
            NodeType(named=True, type="parenthesized_expression"),
        ],
    ),
)
```
## 8) as_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="as_pattern",
    named=True,
    fields={
        "alias": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="as_pattern_target")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="case_pattern"),
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="identifier"),
        ],
    ),
)
```
## 9) assert_statement


```py
NodeTypeWithFieldsAndChildren(
    type="assert_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 10) assignment


```py
NodeTypeWithFields(
    type="assignment",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="pattern"),
                NodeType(named=True, type="pattern_list"),
            ],
        ),
        "right": NodeSchema(
            multiple=False,
            required=False,
            types=[
                NodeType(named=True, type="assignment"),
                NodeType(named=True, type="augmented_assignment"),
                NodeType(named=True, type="expression"),
                NodeType(named=True, type="expression_list"),
                NodeType(named=True, type="pattern_list"),
                NodeType(named=True, type="yield"),
            ],
        ),
        "type": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type")],
        ),
    },
)
```
## 11) attribute


```py
NodeTypeWithFields(
    type="attribute",
    named=True,
    fields={
        "attribute": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "object": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="primary_expression")],
        ),
    },
)
```
## 12) augmented_assignment


```py
NodeTypeWithFields(
    type="augmented_assignment",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="pattern"),
                NodeType(named=True, type="pattern_list"),
            ],
        ),
        "operator": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=False, type="%="),
                NodeType(named=False, type="&="),
                NodeType(named=False, type="**="),
                NodeType(named=False, type="*="),
                NodeType(named=False, type="+="),
                NodeType(named=False, type="-="),
                NodeType(named=False, type="//="),
                NodeType(named=False, type="/="),
                NodeType(named=False, type="<<="),
                NodeType(named=False, type=">>="),
                NodeType(named=False, type="@="),
                NodeType(named=False, type="^="),
                NodeType(named=False, type="|="),
            ],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="assignment"),
                NodeType(named=True, type="augmented_assignment"),
                NodeType(named=True, type="expression"),
                NodeType(named=True, type="expression_list"),
                NodeType(named=True, type="pattern_list"),
                NodeType(named=True, type="yield"),
            ],
        ),
    },
)
```
## 13) await


```py
NodeTypeWithFieldsAndChildren(
    type="await",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="primary_expression")],
    ),
)
```
## 14) binary_operator


```py
NodeTypeWithFields(
    type="binary_operator",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="primary_expression")],
        ),
        "operator": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=False, type="%"),
                NodeType(named=False, type="&"),
                NodeType(named=False, type="*"),
                NodeType(named=False, type="**"),
                NodeType(named=False, type="+"),
                NodeType(named=False, type="-"),
                NodeType(named=False, type="/"),
                NodeType(named=False, type="//"),
                NodeType(named=False, type="<<"),
                NodeType(named=False, type=">>"),
                NodeType(named=False, type="@"),
                NodeType(named=False, type="^"),
                NodeType(named=False, type="|"),
            ],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="primary_expression")],
        ),
    },
)
```
## 15) block


```py
NodeTypeWithFieldsAndChildren(
    type="block",
    named=True,
    fields={
        "alternative": NodeSchema(
            multiple=True,
            required=False,
            types=[NodeType(named=True, type="case_clause")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_compound_statement"),
            NodeType(named=True, type="_simple_statement"),
        ],
    ),
)
```
## 16) boolean_operator


```py
NodeTypeWithFields(
    type="boolean_operator",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
        "operator": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=False, type="and"),
                NodeType(named=False, type="or"),
            ],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 17) break_statement


```py
NodeTypeWithFields(type="break_statement", named=True, fields={})
```
## 18) call


```py
NodeTypeWithFields(
    type="call",
    named=True,
    fields={
        "arguments": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="argument_list"),
                NodeType(named=True, type="generator_expression"),
            ],
        ),
        "function": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="primary_expression")],
        ),
    },
)
```
## 19) case_clause


```py
NodeTypeWithFieldsAndChildren(
    type="case_clause",
    named=True,
    fields={
        "consequence": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
        "guard": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="if_clause")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="case_pattern")],
    ),
)
```
## 20) case_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="case_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[
            NodeType(named=True, type="as_pattern"),
            NodeType(named=True, type="class_pattern"),
            NodeType(named=True, type="complex_pattern"),
            NodeType(named=True, type="concatenated_string"),
            NodeType(named=True, type="dict_pattern"),
            NodeType(named=True, type="dotted_name"),
            NodeType(named=True, type="false"),
            NodeType(named=True, type="float"),
            NodeType(named=True, type="integer"),
            NodeType(named=True, type="keyword_pattern"),
            NodeType(named=True, type="list_pattern"),
            NodeType(named=True, type="none"),
            NodeType(named=True, type="splat_pattern"),
            NodeType(named=True, type="string"),
            NodeType(named=True, type="true"),
            NodeType(named=True, type="tuple_pattern"),
            NodeType(named=True, type="union_pattern"),
        ],
    ),
)
```
## 21) chevron


```py
NodeTypeWithFieldsAndChildren(
    type="chevron",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 22) class_definition


```py
NodeTypeWithFields(
    type="class_definition",
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
            types=[NodeType(named=True, type="identifier")],
        ),
        "superclasses": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="argument_list")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameter")],
        ),
    },
)
```
## 23) class_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="class_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="case_pattern"),
            NodeType(named=True, type="dotted_name"),
        ],
    ),
)
```
## 24) comparison_operator


```py
NodeTypeWithFieldsAndChildren(
    type="comparison_operator",
    named=True,
    fields={
        "operators": NodeSchema(
            multiple=True,
            required=True,
            types=[
                NodeType(named=False, type="!="),
                NodeType(named=False, type="<"),
                NodeType(named=False, type="<="),
                NodeType(named=False, type="<>"),
                NodeType(named=False, type="=="),
                NodeType(named=False, type=">"),
                NodeType(named=False, type=">="),
                NodeType(named=False, type="in"),
                NodeType(named=False, type="is"),
                NodeType(named=False, type="is not"),
                NodeType(named=False, type="not in"),
            ],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="primary_expression")],
    ),
)
```
## 25) complex_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="complex_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="float"),
            NodeType(named=True, type="integer"),
        ],
    ),
)
```
## 26) concatenated_string


```py
NodeTypeWithFieldsAndChildren(
    type="concatenated_string",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="string")],
    ),
)
```
## 27) conditional_expression


```py
NodeTypeWithFieldsAndChildren(
    type="conditional_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 28) constrained_type


```py
NodeTypeWithFieldsAndChildren(
    type="constrained_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="type")],
    ),
)
```
## 29) continue_statement


```py
NodeTypeWithFields(type="continue_statement", named=True, fields={})
```
## 30) decorated_definition


```py
NodeTypeWithFieldsAndChildren(
    type="decorated_definition",
    named=True,
    fields={
        "definition": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="class_definition"),
                NodeType(named=True, type="function_definition"),
            ],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="decorator")],
    ),
)
```
## 31) decorator


```py
NodeTypeWithFieldsAndChildren(
    type="decorator",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 32) default_parameter


```py
NodeTypeWithFields(
    type="default_parameter",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="tuple_pattern"),
            ],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 33) delete_statement


```py
NodeTypeWithFieldsAndChildren(
    type="delete_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="expression_list"),
        ],
    ),
)
```
## 34) dict_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="dict_pattern",
    named=True,
    fields={
        "key": NodeSchema(
            multiple=True,
            required=False,
            types=[
                NodeType(named=False, type="-"),
                NodeType(named=False, type="_"),
                NodeType(named=True, type="class_pattern"),
                NodeType(named=True, type="complex_pattern"),
                NodeType(named=True, type="concatenated_string"),
                NodeType(named=True, type="dict_pattern"),
                NodeType(named=True, type="dotted_name"),
                NodeType(named=True, type="false"),
                NodeType(named=True, type="float"),
                NodeType(named=True, type="integer"),
                NodeType(named=True, type="list_pattern"),
                NodeType(named=True, type="none"),
                NodeType(named=True, type="splat_pattern"),
                NodeType(named=True, type="string"),
                NodeType(named=True, type="true"),
                NodeType(named=True, type="tuple_pattern"),
                NodeType(named=True, type="union_pattern"),
            ],
        ),
        "value": NodeSchema(
            multiple=True,
            required=False,
            types=[NodeType(named=True, type="case_pattern")],
        ),
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="splat_pattern")],
    ),
)
```
## 35) dictionary


```py
NodeTypeWithFieldsAndChildren(
    type="dictionary",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="dictionary_splat"),
            NodeType(named=True, type="pair"),
        ],
    ),
)
```
## 36) dictionary_comprehension


```py
NodeTypeWithFieldsAndChildren(
    type="dictionary_comprehension",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="pair")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="for_in_clause"),
            NodeType(named=True, type="if_clause"),
        ],
    ),
)
```
## 37) dictionary_splat


```py
NodeTypeWithFieldsAndChildren(
    type="dictionary_splat",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 38) dictionary_splat_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="dictionary_splat_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="attribute"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="subscript"),
        ],
    ),
)
```
## 39) dotted_name


```py
NodeTypeWithFieldsAndChildren(
    type="dotted_name",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="identifier")],
    ),
)
```
## 40) elif_clause


```py
NodeTypeWithFields(
    type="elif_clause",
    named=True,
    fields={
        "condition": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
        "consequence": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
    },
)
```
## 41) else_clause


```py
NodeTypeWithFields(
    type="else_clause",
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
## 42) except_clause


```py
NodeTypeWithFieldsAndChildren(
    type="except_clause",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="block"),
            NodeType(named=True, type="expression"),
        ],
    ),
)
```
## 43) except_group_clause


```py
NodeTypeWithFieldsAndChildren(
    type="except_group_clause",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="block"),
            NodeType(named=True, type="expression"),
        ],
    ),
)
```
## 44) exec_statement


```py
NodeTypeWithFieldsAndChildren(
    type="exec_statement",
    named=True,
    fields={
        "code": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="identifier"),
                NodeType(named=True, type="string"),
            ],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 45) expression_list


```py
NodeTypeWithFieldsAndChildren(
    type="expression_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 46) expression_statement


```py
NodeTypeWithFieldsAndChildren(
    type="expression_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="assignment"),
            NodeType(named=True, type="augmented_assignment"),
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="yield"),
        ],
    ),
)
```
## 47) finally_clause


```py
NodeTypeWithFieldsAndChildren(
    type="finally_clause",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="block")],
    ),
)
```
## 48) for_in_clause


```py
NodeTypeWithFields(
    type="for_in_clause",
    named=True,
    fields={
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="pattern"),
                NodeType(named=True, type="pattern_list"),
            ],
        ),
        "right": NodeSchema(
            multiple=True,
            required=True,
            types=[
                NodeType(named=False, type=","),
                NodeType(named=True, type="expression"),
            ],
        ),
    },
)
```
## 49) for_statement


```py
NodeTypeWithFields(
    type="for_statement",
    named=True,
    fields={
        "alternative": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="else_clause")],
        ),
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
        "left": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="pattern"),
                NodeType(named=True, type="pattern_list"),
            ],
        ),
        "right": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="expression"),
                NodeType(named=True, type="expression_list"),
            ],
        ),
    },
)
```
## 50) format_expression


```py
NodeTypeWithFields(
    type="format_expression",
    named=True,
    fields={
        "expression": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="expression"),
                NodeType(named=True, type="expression_list"),
                NodeType(named=True, type="pattern_list"),
                NodeType(named=True, type="yield"),
            ],
        ),
        "format_specifier": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="format_specifier")],
        ),
        "type_conversion": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_conversion")],
        ),
    },
)
```
## 51) format_specifier


```py
NodeTypeWithFieldsAndChildren(
    type="format_specifier",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="format_expression")],
    ),
)
```
## 52) function_definition


```py
NodeTypeWithFields(
    type="function_definition",
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
            types=[NodeType(named=True, type="identifier")],
        ),
        "parameters": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="parameters")],
        ),
        "return_type": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type")],
        ),
        "type_parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_parameter")],
        ),
    },
)
```
## 53) future_import_statement


```py
NodeTypeWithFields(
    type="future_import_statement",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=True,
            required=True,
            types=[
                NodeType(named=True, type="aliased_import"),
                NodeType(named=True, type="dotted_name"),
            ],
        )
    },
)
```
## 54) generator_expression


```py
NodeTypeWithFieldsAndChildren(
    type="generator_expression",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="for_in_clause"),
            NodeType(named=True, type="if_clause"),
        ],
    ),
)
```
## 55) generic_type


```py
NodeTypeWithFieldsAndChildren(
    type="generic_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="type_parameter"),
        ],
    ),
)
```
## 56) global_statement


```py
NodeTypeWithFieldsAndChildren(
    type="global_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="identifier")],
    ),
)
```
## 57) if_clause


```py
NodeTypeWithFieldsAndChildren(
    type="if_clause",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 58) if_statement


```py
NodeTypeWithFields(
    type="if_statement",
    named=True,
    fields={
        "alternative": NodeSchema(
            multiple=True,
            required=False,
            types=[
                NodeType(named=True, type="elif_clause"),
                NodeType(named=True, type="else_clause"),
            ],
        ),
        "condition": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
        "consequence": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
    },
)
```
## 59) import_from_statement


```py
NodeTypeWithFieldsAndChildren(
    type="import_from_statement",
    named=True,
    fields={
        "module_name": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="dotted_name"),
                NodeType(named=True, type="relative_import"),
            ],
        ),
        "name": NodeSchema(
            multiple=True,
            required=False,
            types=[
                NodeType(named=True, type="aliased_import"),
                NodeType(named=True, type="dotted_name"),
            ],
        ),
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="wildcard_import")],
    ),
)
```
## 60) import_prefix


```py
NodeTypeWithFields(type="import_prefix", named=True, fields={})
```
## 61) import_statement


```py
NodeTypeWithFields(
    type="import_statement",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=True,
            required=True,
            types=[
                NodeType(named=True, type="aliased_import"),
                NodeType(named=True, type="dotted_name"),
            ],
        )
    },
)
```
## 62) interpolation


```py
NodeTypeWithFields(
    type="interpolation",
    named=True,
    fields={
        "expression": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=True, type="expression"),
                NodeType(named=True, type="expression_list"),
                NodeType(named=True, type="pattern_list"),
                NodeType(named=True, type="yield"),
            ],
        ),
        "format_specifier": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="format_specifier")],
        ),
        "type_conversion": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="type_conversion")],
        ),
    },
)
```
## 63) keyword_argument


```py
NodeTypeWithFields(
    type="keyword_argument",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 64) keyword_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="keyword_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="class_pattern"),
            NodeType(named=True, type="complex_pattern"),
            NodeType(named=True, type="concatenated_string"),
            NodeType(named=True, type="dict_pattern"),
            NodeType(named=True, type="dotted_name"),
            NodeType(named=True, type="false"),
            NodeType(named=True, type="float"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="integer"),
            NodeType(named=True, type="list_pattern"),
            NodeType(named=True, type="none"),
            NodeType(named=True, type="splat_pattern"),
            NodeType(named=True, type="string"),
            NodeType(named=True, type="true"),
            NodeType(named=True, type="tuple_pattern"),
            NodeType(named=True, type="union_pattern"),
        ],
    ),
)
```
## 65) keyword_separator


```py
NodeTypeWithFields(type="keyword_separator", named=True, fields={})
```
## 66) lambda


```py
NodeTypeWithFields(
    type="lambda",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
        "parameters": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="lambda_parameters")],
        ),
    },
)
```
## 67) lambda_parameters


```py
NodeTypeWithFieldsAndChildren(
    type="lambda_parameters",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="parameter")],
    ),
)
```
## 68) list


```py
NodeTypeWithFieldsAndChildren(
    type="list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="list_splat"),
            NodeType(named=True, type="parenthesized_list_splat"),
            NodeType(named=True, type="yield"),
        ],
    ),
)
```
## 69) list_comprehension


```py
NodeTypeWithFieldsAndChildren(
    type="list_comprehension",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="for_in_clause"),
            NodeType(named=True, type="if_clause"),
        ],
    ),
)
```
## 70) list_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="list_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="case_pattern"),
            NodeType(named=True, type="pattern"),
        ],
    ),
)
```
## 71) list_splat


```py
NodeTypeWithFieldsAndChildren(
    type="list_splat",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="attribute"),
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="subscript"),
        ],
    ),
)
```
## 72) list_splat_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="list_splat_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="attribute"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="subscript"),
        ],
    ),
)
```
## 73) match_statement


```py
NodeTypeWithFields(
    type="match_statement",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
        "subject": NodeSchema(
            multiple=True,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 74) member_type


```py
NodeTypeWithFieldsAndChildren(
    type="member_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="type"),
        ],
    ),
)
```
## 75) module


```py
NodeTypeWithFieldsAndChildren(
    type="module",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="_compound_statement"),
            NodeType(named=True, type="_simple_statement"),
        ],
    ),
)
```
## 76) named_expression


```py
NodeTypeWithFields(
    type="named_expression",
    named=True,
    fields={
        "name": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="identifier")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 77) nonlocal_statement


```py
NodeTypeWithFieldsAndChildren(
    type="nonlocal_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="identifier")],
    ),
)
```
## 78) not_operator


```py
NodeTypeWithFields(
    type="not_operator",
    named=True,
    fields={
        "argument": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        )
    },
)
```
## 79) pair


```py
NodeTypeWithFields(
    type="pair",
    named=True,
    fields={
        "key": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 80) parameters


```py
NodeTypeWithFieldsAndChildren(
    type="parameters",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="parameter")],
    ),
)
```
## 81) parenthesized_expression


```py
NodeTypeWithFieldsAndChildren(
    type="parenthesized_expression",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="list_splat"),
            NodeType(named=True, type="parenthesized_expression"),
            NodeType(named=True, type="yield"),
        ],
    ),
)
```
## 82) parenthesized_list_splat


```py
NodeTypeWithFieldsAndChildren(
    type="parenthesized_list_splat",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="list_splat"),
            NodeType(named=True, type="parenthesized_expression"),
        ],
    ),
)
```
## 83) pass_statement


```py
NodeTypeWithFields(type="pass_statement", named=True, fields={})
```
## 84) pattern_list


```py
NodeTypeWithFieldsAndChildren(
    type="pattern_list",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="pattern")],
    ),
)
```
## 85) positional_separator


```py
NodeTypeWithFields(type="positional_separator", named=True, fields={})
```
## 86) print_statement


```py
NodeTypeWithFieldsAndChildren(
    type="print_statement",
    named=True,
    fields={
        "argument": NodeSchema(
            multiple=True,
            required=False,
            types=[NodeType(named=True, type="expression")],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="chevron")],
    ),
)
```
## 87) raise_statement


```py
NodeTypeWithFieldsAndChildren(
    type="raise_statement",
    named=True,
    fields={
        "cause": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="expression")],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="expression_list"),
        ],
    ),
)
```
## 88) relative_import


```py
NodeTypeWithFieldsAndChildren(
    type="relative_import",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="dotted_name"),
            NodeType(named=True, type="import_prefix"),
        ],
    ),
)
```
## 89) return_statement


```py
NodeTypeWithFieldsAndChildren(
    type="return_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="expression_list"),
        ],
    ),
)
```
## 90) set


```py
NodeTypeWithFieldsAndChildren(
    type="set",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="list_splat"),
            NodeType(named=True, type="parenthesized_list_splat"),
            NodeType(named=True, type="yield"),
        ],
    ),
)
```
## 91) set_comprehension


```py
NodeTypeWithFieldsAndChildren(
    type="set_comprehension",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="for_in_clause"),
            NodeType(named=True, type="if_clause"),
        ],
    ),
)
```
## 92) slice


```py
NodeTypeWithFieldsAndChildren(
    type="slice",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[NodeType(named=True, type="expression")],
    ),
)
```
## 93) splat_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="splat_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[NodeType(named=True, type="identifier")],
    ),
)
```
## 94) splat_type


```py
NodeTypeWithFieldsAndChildren(
    type="splat_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[NodeType(named=True, type="identifier")],
    ),
)
```
## 95) string


```py
NodeTypeWithFieldsAndChildren(
    type="string",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="interpolation"),
            NodeType(named=True, type="string_content"),
            NodeType(named=True, type="string_end"),
            NodeType(named=True, type="string_start"),
        ],
    ),
)
```
## 96) string_content


```py
NodeTypeWithFieldsAndChildren(
    type="string_content",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="escape_interpolation"),
            NodeType(named=True, type="escape_sequence"),
        ],
    ),
)
```
## 97) subscript


```py
NodeTypeWithFields(
    type="subscript",
    named=True,
    fields={
        "subscript": NodeSchema(
            multiple=True,
            required=True,
            types=[
                NodeType(named=True, type="expression"),
                NodeType(named=True, type="slice"),
            ],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="primary_expression")],
        ),
    },
)
```
## 98) try_statement


```py
NodeTypeWithFieldsAndChildren(
    type="try_statement",
    named=True,
    fields={
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        )
    },
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[
            NodeType(named=True, type="else_clause"),
            NodeType(named=True, type="except_clause"),
            NodeType(named=True, type="except_group_clause"),
            NodeType(named=True, type="finally_clause"),
        ],
    ),
)
```
## 99) tuple


```py
NodeTypeWithFieldsAndChildren(
    type="tuple",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="list_splat"),
            NodeType(named=True, type="parenthesized_list_splat"),
            NodeType(named=True, type="yield"),
        ],
    ),
)
```
## 100) tuple_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="tuple_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="case_pattern"),
            NodeType(named=True, type="pattern"),
        ],
    ),
)
```
## 101) type


```py
NodeTypeWithFieldsAndChildren(
    type="type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="constrained_type"),
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="generic_type"),
            NodeType(named=True, type="member_type"),
            NodeType(named=True, type="splat_type"),
            NodeType(named=True, type="union_type"),
        ],
    ),
)
```
## 102) type_alias_statement


```py
NodeTypeWithFieldsAndChildren(
    type="type_alias_statement",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="type")],
    ),
)
```
## 103) type_parameter


```py
NodeTypeWithFieldsAndChildren(
    type="type_parameter",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="type")],
    ),
)
```
## 104) typed_default_parameter


```py
NodeTypeWithFields(
    type="typed_default_parameter",
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
            types=[NodeType(named=True, type="type")],
        ),
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 105) typed_parameter


```py
NodeTypeWithFieldsAndChildren(
    type="typed_parameter",
    named=True,
    fields={
        "type": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="type")],
        )
    },
    children=NodeSchema(
        multiple=False,
        required=True,
        types=[
            NodeType(named=True, type="dictionary_splat_pattern"),
            NodeType(named=True, type="identifier"),
            NodeType(named=True, type="list_splat_pattern"),
        ],
    ),
)
```
## 106) unary_operator


```py
NodeTypeWithFields(
    type="unary_operator",
    named=True,
    fields={
        "argument": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="primary_expression")],
        ),
        "operator": NodeSchema(
            multiple=False,
            required=True,
            types=[
                NodeType(named=False, type="+"),
                NodeType(named=False, type="-"),
                NodeType(named=False, type="~"),
            ],
        ),
    },
)
```
## 107) union_pattern


```py
NodeTypeWithFieldsAndChildren(
    type="union_pattern",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=False,
        types=[
            NodeType(named=True, type="class_pattern"),
            NodeType(named=True, type="complex_pattern"),
            NodeType(named=True, type="concatenated_string"),
            NodeType(named=True, type="dict_pattern"),
            NodeType(named=True, type="dotted_name"),
            NodeType(named=True, type="false"),
            NodeType(named=True, type="float"),
            NodeType(named=True, type="integer"),
            NodeType(named=True, type="list_pattern"),
            NodeType(named=True, type="none"),
            NodeType(named=True, type="splat_pattern"),
            NodeType(named=True, type="string"),
            NodeType(named=True, type="true"),
            NodeType(named=True, type="tuple_pattern"),
            NodeType(named=True, type="union_pattern"),
        ],
    ),
)
```
## 108) union_type


```py
NodeTypeWithFieldsAndChildren(
    type="union_type",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="type")],
    ),
)
```
## 109) while_statement


```py
NodeTypeWithFields(
    type="while_statement",
    named=True,
    fields={
        "alternative": NodeSchema(
            multiple=False,
            required=False,
            types=[NodeType(named=True, type="else_clause")],
        ),
        "body": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="block")],
        ),
        "condition": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        ),
    },
)
```
## 110) wildcard_import


```py
NodeTypeWithFields(type="wildcard_import", named=True, fields={})
```
## 111) with_clause


```py
NodeTypeWithFieldsAndChildren(
    type="with_clause",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=True,
        required=True,
        types=[NodeType(named=True, type="with_item")],
    ),
)
```
## 112) with_item


```py
NodeTypeWithFields(
    type="with_item",
    named=True,
    fields={
        "value": NodeSchema(
            multiple=False,
            required=True,
            types=[NodeType(named=True, type="expression")],
        )
    },
)
```
## 113) with_statement


```py
NodeTypeWithFieldsAndChildren(
    type="with_statement",
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
        required=True,
        types=[NodeType(named=True, type="with_clause")],
    ),
)
```
## 114) yield


```py
NodeTypeWithFieldsAndChildren(
    type="yield",
    named=True,
    fields={},
    children=NodeSchema(
        multiple=False,
        required=False,
        types=[
            NodeType(named=True, type="expression"),
            NodeType(named=True, type="expression_list"),
        ],
    ),
)
```
## 115) !=


```py
NodeTypeNamed(type="!=", named=False)
```
## 116) %


```py
NodeTypeNamed(type="%", named=False)
```
## 117) %=


```py
NodeTypeNamed(type="%=", named=False)
```
## 118) &


```py
NodeTypeNamed(type="&", named=False)
```
## 119) &=


```py
NodeTypeNamed(type="&=", named=False)
```
## 120) (


```py
NodeTypeNamed(type="(", named=False)
```
## 121) )


```py
NodeTypeNamed(type=")", named=False)
```
## 122) *


```py
NodeTypeNamed(type="*", named=False)
```
## 123) **


```py
NodeTypeNamed(type="**", named=False)
```
## 124) **=


```py
NodeTypeNamed(type="**=", named=False)
```
## 125) *=


```py
NodeTypeNamed(type="*=", named=False)
```
## 126) +


```py
NodeTypeNamed(type="+", named=False)
```
## 127) +=


```py
NodeTypeNamed(type="+=", named=False)
```
## 128) ,


```py
NodeTypeNamed(type=",", named=False)
```
## 129) -


```py
NodeTypeNamed(type="-", named=False)
```
## 130) -=


```py
NodeTypeNamed(type="-=", named=False)
```
## 131) ->


```py
NodeTypeNamed(type="->", named=False)
```
## 132) .


```py
NodeTypeNamed(type=".", named=False)
```
## 133) /


```py
NodeTypeNamed(type="/", named=False)
```
## 134) //


```py
NodeTypeNamed(type="//", named=False)
```
## 135) //=


```py
NodeTypeNamed(type="//=", named=False)
```
## 136) /=


```py
NodeTypeNamed(type="/=", named=False)
```
## 137) :


```py
NodeTypeNamed(type=":", named=False)
```
## 138) :=


```py
NodeTypeNamed(type=":=", named=False)
```
## 139) ;


```py
NodeTypeNamed(type=";", named=False)
```
## 140) <


```py
NodeTypeNamed(type="<", named=False)
```
## 141) <<


```py
NodeTypeNamed(type="<<", named=False)
```
## 142) <<=


```py
NodeTypeNamed(type="<<=", named=False)
```
## 143) <=


```py
NodeTypeNamed(type="<=", named=False)
```
## 144) <>


```py
NodeTypeNamed(type="<>", named=False)
```
## 145) =


```py
NodeTypeNamed(type="=", named=False)
```
## 146) ==


```py
NodeTypeNamed(type="==", named=False)
```
## 147) >


```py
NodeTypeNamed(type=">", named=False)
```
## 148) >=


```py
NodeTypeNamed(type=">=", named=False)
```
## 149) >>


```py
NodeTypeNamed(type=">>", named=False)
```
## 150) >>=


```py
NodeTypeNamed(type=">>=", named=False)
```
## 151) @


```py
NodeTypeNamed(type="@", named=False)
```
## 152) @=


```py
NodeTypeNamed(type="@=", named=False)
```
## 153) [


```py
NodeTypeNamed(type="[", named=False)
```
## 154) \


```py
NodeTypeNamed(type="\\", named=False)
```
## 155) ]


```py
NodeTypeNamed(type="]", named=False)
```
## 156) ^


```py
NodeTypeNamed(type="^", named=False)
```
## 157) ^=


```py
NodeTypeNamed(type="^=", named=False)
```
## 158) _


```py
NodeTypeNamed(type="_", named=False)
```
## 159) __future__


```py
NodeTypeNamed(type="__future__", named=False)
```
## 160) and


```py
NodeTypeNamed(type="and", named=False)
```
## 161) as


```py
NodeTypeNamed(type="as", named=False)
```
## 162) assert


```py
NodeTypeNamed(type="assert", named=False)
```
## 163) async


```py
NodeTypeNamed(type="async", named=False)
```
## 164) await


```py
NodeTypeNamed(type="await", named=False)
```
## 165) break


```py
NodeTypeNamed(type="break", named=False)
```
## 166) case


```py
NodeTypeNamed(type="case", named=False)
```
## 167) class


```py
NodeTypeNamed(type="class", named=False)
```
## 168) comment


```py
NodeTypeNamed(type="comment", named=True)
```
## 169) continue


```py
NodeTypeNamed(type="continue", named=False)
```
## 170) def


```py
NodeTypeNamed(type="def", named=False)
```
## 171) del


```py
NodeTypeNamed(type="del", named=False)
```
## 172) elif


```py
NodeTypeNamed(type="elif", named=False)
```
## 173) ellipsis


```py
NodeTypeNamed(type="ellipsis", named=True)
```
## 174) else


```py
NodeTypeNamed(type="else", named=False)
```
## 175) escape_interpolation


```py
NodeTypeNamed(type="escape_interpolation", named=True)
```
## 176) escape_sequence


```py
NodeTypeNamed(type="escape_sequence", named=True)
```
## 177) except


```py
NodeTypeNamed(type="except", named=False)
```
## 178) except*


```py
NodeTypeNamed(type="except*", named=False)
```
## 179) exec


```py
NodeTypeNamed(type="exec", named=False)
```
## 180) false


```py
NodeTypeNamed(type="false", named=True)
```
## 181) finally


```py
NodeTypeNamed(type="finally", named=False)
```
## 182) float


```py
NodeTypeNamed(type="float", named=True)
```
## 183) for


```py
NodeTypeNamed(type="for", named=False)
```
## 184) from


```py
NodeTypeNamed(type="from", named=False)
```
## 185) global


```py
NodeTypeNamed(type="global", named=False)
```
## 186) identifier


```py
NodeTypeNamed(type="identifier", named=True)
```
## 187) if


```py
NodeTypeNamed(type="if", named=False)
```
## 188) import


```py
NodeTypeNamed(type="import", named=False)
```
## 189) in


```py
NodeTypeNamed(type="in", named=False)
```
## 190) integer


```py
NodeTypeNamed(type="integer", named=True)
```
## 191) is


```py
NodeTypeNamed(type="is", named=False)
```
## 192) is not


```py
NodeTypeNamed(type="is not", named=False)
```
## 193) lambda


```py
NodeTypeNamed(type="lambda", named=False)
```
## 194) line_continuation


```py
NodeTypeNamed(type="line_continuation", named=True)
```
## 195) match


```py
NodeTypeNamed(type="match", named=False)
```
## 196) none


```py
NodeTypeNamed(type="none", named=True)
```
## 197) nonlocal


```py
NodeTypeNamed(type="nonlocal", named=False)
```
## 198) not


```py
NodeTypeNamed(type="not", named=False)
```
## 199) not in


```py
NodeTypeNamed(type="not in", named=False)
```
## 200) or


```py
NodeTypeNamed(type="or", named=False)
```
## 201) pass


```py
NodeTypeNamed(type="pass", named=False)
```
## 202) print


```py
NodeTypeNamed(type="print", named=False)
```
## 203) raise


```py
NodeTypeNamed(type="raise", named=False)
```
## 204) return


```py
NodeTypeNamed(type="return", named=False)
```
## 205) string_end


```py
NodeTypeNamed(type="string_end", named=True)
```
## 206) string_start


```py
NodeTypeNamed(type="string_start", named=True)
```
## 207) true


```py
NodeTypeNamed(type="true", named=True)
```
## 208) try


```py
NodeTypeNamed(type="try", named=False)
```
## 209) type


```py
NodeTypeNamed(type="type", named=False)
```
## 210) type_conversion


```py
NodeTypeNamed(type="type_conversion", named=True)
```
## 211) while


```py
NodeTypeNamed(type="while", named=False)
```
## 212) with


```py
NodeTypeNamed(type="with", named=False)
```
## 213) yield


```py
NodeTypeNamed(type="yield", named=False)
```
## 214) {


```py
NodeTypeNamed(type="{", named=False)
```
## 215) |


```py
NodeTypeNamed(type="|", named=False)
```
## 216) |=


```py
NodeTypeNamed(type="|=", named=False)
```
## 217) }


```py
NodeTypeNamed(type="}", named=False)
```
## 218) ~


```py
NodeTypeNamed(type="~", named=False)
```
