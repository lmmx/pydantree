# Python

## Rules

### 1) module

```py
RepeatRule(
    type="REPEAT",
    content=SymbolRule(type="SYMBOL", name="_statement"),
)
```

### 2) _statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_simple_statements"),
        SymbolRule(type="SYMBOL", name="_compound_statement"),
    ],
)
```

### 3) _simple_statements

```py
SeqRule(
    type="SEQ",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="_simple_statement"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=";"),
                            SymbolRule(
                                type="SYMBOL",
                                name="_simple_statement",
                            ),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=";"),
                BlankRule(type="BLANK"),
            ],
        ),
        SymbolRule(type="SYMBOL", name="_newline"),
    ],
)
```

### 4) _simple_statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="future_import_statement"),
        SymbolRule(type="SYMBOL", name="import_statement"),
        SymbolRule(type="SYMBOL", name="import_from_statement"),
        SymbolRule(type="SYMBOL", name="print_statement"),
        SymbolRule(type="SYMBOL", name="assert_statement"),
        SymbolRule(type="SYMBOL", name="expression_statement"),
        SymbolRule(type="SYMBOL", name="return_statement"),
        SymbolRule(type="SYMBOL", name="delete_statement"),
        SymbolRule(type="SYMBOL", name="raise_statement"),
        SymbolRule(type="SYMBOL", name="pass_statement"),
        SymbolRule(type="SYMBOL", name="break_statement"),
        SymbolRule(type="SYMBOL", name="continue_statement"),
        SymbolRule(type="SYMBOL", name="global_statement"),
        SymbolRule(type="SYMBOL", name="nonlocal_statement"),
        SymbolRule(type="SYMBOL", name="exec_statement"),
        SymbolRule(type="SYMBOL", name="type_alias_statement"),
    ],
)
```

### 5) import_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="import"),
        SymbolRule(type="SYMBOL", name="_import_list"),
    ],
)
```

### 6) import_prefix

```py
Repeat1Rule(
    type="REPEAT1", content=StringRule(type="STRING", value=".")
)
```

### 7) relative_import

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="import_prefix"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="dotted_name"),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 8) future_import_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="from"),
        StringRule(type="STRING", value="__future__"),
        StringRule(type="STRING", value="import"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_import_list"),
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="("),
                        SymbolRule(
                            type="SYMBOL", name="_import_list"
                        ),
                        StringRule(type="STRING", value=")"),
                    ],
                ),
            ],
        ),
    ],
)
```

### 9) import_from_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="from"),
        FieldRule(
            name="module_name",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="relative_import"),
                    SymbolRule(type="SYMBOL", name="dotted_name"),
                ],
            ),
        ),
        StringRule(type="STRING", value="import"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="wildcard_import"),
                SymbolRule(type="SYMBOL", name="_import_list"),
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="("),
                        SymbolRule(
                            type="SYMBOL", name="_import_list"
                        ),
                        StringRule(type="STRING", value=")"),
                    ],
                ),
            ],
        ),
    ],
)
```

### 10) _import_list

```py
SeqRule(
    type="SEQ",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                FieldRule(
                    name="name",
                    type="FIELD",
                    content=ChoiceRule(
                        type="CHOICE",
                        members=[
                            SymbolRule(
                                type="SYMBOL", name="dotted_name"
                            ),
                            SymbolRule(
                                type="SYMBOL", name="aliased_import"
                            ),
                        ],
                    ),
                ),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            FieldRule(
                                name="name",
                                type="FIELD",
                                content=ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="dotted_name",
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="aliased_import",
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 11) aliased_import

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="dotted_name"),
        ),
        StringRule(type="STRING", value="as"),
        FieldRule(
            name="alias",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
    ],
)
```

### 12) wildcard_import

```py
StringRule(type="STRING", value="*")
```

### 13) print_statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        PrecRule(
            type="PREC",
            value=1,
            content=SeqRule(
                type="SEQ",
                members=[
                    StringRule(type="STRING", value="print"),
                    SymbolRule(type="SYMBOL", name="chevron"),
                    RepeatRule(
                        type="REPEAT",
                        content=SeqRule(
                            type="SEQ",
                            members=[
                                StringRule(type="STRING", value=","),
                                FieldRule(
                                    name="argument",
                                    type="FIELD",
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="expression",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            StringRule(type="STRING", value=","),
                            BlankRule(type="BLANK"),
                        ],
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC",
            value=-3,
            content=PrecRule(
                type="PREC_DYNAMIC",
                value=-1,
                content=SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="print"),
                        SeqRule(
                            type="SEQ",
                            members=[
                                FieldRule(
                                    name="argument",
                                    type="FIELD",
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="expression",
                                    ),
                                ),
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            StringRule(
                                                type="STRING",
                                                value=",",
                                            ),
                                            FieldRule(
                                                name="argument",
                                                type="FIELD",
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="expression",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value=","),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
            ),
        ),
    ],
)
```

### 14) chevron

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value=">>"),
        SymbolRule(type="SYMBOL", name="expression"),
    ],
)
```

### 15) assert_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="assert"),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="expression"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(
                                type="SYMBOL", name="expression"
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ],
)
```

### 16) expression_statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="expression"),
        SeqRule(
            type="SEQ",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="expression"),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="expression",
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        StringRule(type="STRING", value=","),
                        BlankRule(type="BLANK"),
                    ],
                ),
            ],
        ),
        SymbolRule(type="SYMBOL", name="assignment"),
        SymbolRule(type="SYMBOL", name="augmented_assignment"),
        SymbolRule(type="SYMBOL", name="yield"),
    ],
)
```

### 17) named_expression

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_named_expression_lhs"
            ),
        ),
        StringRule(type="STRING", value=":="),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
    ],
)
```

### 18) _named_expression_lhs

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="identifier"),
        SymbolRule(type="SYMBOL", name="keyword_identifier"),
    ],
)
```

### 19) return_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="return"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_expressions"),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 20) delete_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="del"),
        SymbolRule(type="SYMBOL", name="_expressions"),
    ],
)
```

### 21) _expressions

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="expression"),
        SymbolRule(type="SYMBOL", name="expression_list"),
    ],
)
```

### 22) raise_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="raise"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_expressions"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="from"),
                        FieldRule(
                            name="cause",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="expression"
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 23) pass_statement

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=StringRule(type="STRING", value="pass"),
)
```

### 24) break_statement

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=StringRule(type="STRING", value="break"),
)
```

### 25) continue_statement

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=StringRule(type="STRING", value="continue"),
)
```

### 26) _compound_statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="if_statement"),
        SymbolRule(type="SYMBOL", name="for_statement"),
        SymbolRule(type="SYMBOL", name="while_statement"),
        SymbolRule(type="SYMBOL", name="try_statement"),
        SymbolRule(type="SYMBOL", name="with_statement"),
        SymbolRule(type="SYMBOL", name="function_definition"),
        SymbolRule(type="SYMBOL", name="class_definition"),
        SymbolRule(type="SYMBOL", name="decorated_definition"),
        SymbolRule(type="SYMBOL", name="match_statement"),
    ],
)
```

### 27) if_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="if"),
        FieldRule(
            name="condition",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="consequence",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
        RepeatRule(
            type="REPEAT",
            content=FieldRule(
                name="alternative",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="elif_clause"),
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                FieldRule(
                    name="alternative",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="else_clause"
                    ),
                ),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 28) elif_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="elif"),
        FieldRule(
            name="condition",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="consequence",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
    ],
)
```

### 29) else_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="else"),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
    ],
)
```

### 30) match_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="match"),
        SeqRule(
            type="SEQ",
            members=[
                FieldRule(
                    name="subject",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="expression"
                    ),
                ),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            FieldRule(
                                name="subject",
                                type="FIELD",
                                content=SymbolRule(
                                    type="SYMBOL", name="expression"
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=AliasRule(
                type="ALIAS",
                value="block",
                named=True,
                content=SymbolRule(
                    type="SYMBOL", name="_match_block"
                ),
            ),
        ),
    ],
)
```

### 31) _match_block

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="_indent"),
                RepeatRule(
                    type="REPEAT",
                    content=FieldRule(
                        name="alternative",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="case_clause"
                        ),
                    ),
                ),
                SymbolRule(type="SYMBOL", name="_dedent"),
            ],
        ),
        SymbolRule(type="SYMBOL", name="_newline"),
    ],
)
```

### 32) case_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="case"),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="case_pattern"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(
                                type="SYMBOL", name="case_pattern"
                            ),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                FieldRule(
                    name="guard",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="if_clause"
                    ),
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="consequence",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
    ],
)
```

### 33) for_statement

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="async"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="for"),
        FieldRule(
            name="left",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_left_hand_side"),
        ),
        StringRule(type="STRING", value="in"),
        FieldRule(
            name="right",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_expressions"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
        FieldRule(
            name="alternative",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="else_clause"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
    ],
)
```

### 34) while_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="while"),
        FieldRule(
            name="condition",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                FieldRule(
                    name="alternative",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="else_clause"
                    ),
                ),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 35) try_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="try"),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        Repeat1Rule(
                            type="REPEAT1",
                            content=SymbolRule(
                                type="SYMBOL", name="except_clause"
                            ),
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="else_clause"
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL",
                                    name="finally_clause",
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        Repeat1Rule(
                            type="REPEAT1",
                            content=SymbolRule(
                                type="SYMBOL",
                                name="except_group_clause",
                            ),
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="else_clause"
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL",
                                    name="finally_clause",
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                SymbolRule(type="SYMBOL", name="finally_clause"),
            ],
        ),
    ],
)
```

### 36) except_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="except"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="expression"),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SeqRule(
                                    type="SEQ",
                                    members=[
                                        ChoiceRule(
                                            type="CHOICE",
                                            members=[
                                                StringRule(
                                                    type="STRING",
                                                    value="as",
                                                ),
                                                StringRule(
                                                    type="STRING",
                                                    value=",",
                                                ),
                                            ],
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="expression",
                                        ),
                                    ],
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=":"),
        SymbolRule(type="SYMBOL", name="_suite"),
    ],
)
```

### 37) except_group_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="except*"),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="expression"),
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                StringRule(type="STRING", value="as"),
                                SymbolRule(
                                    type="SYMBOL", name="expression"
                                ),
                            ],
                        ),
                        BlankRule(type="BLANK"),
                    ],
                ),
            ],
        ),
        StringRule(type="STRING", value=":"),
        SymbolRule(type="SYMBOL", name="_suite"),
    ],
)
```

### 38) finally_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="finally"),
        StringRule(type="STRING", value=":"),
        SymbolRule(type="SYMBOL", name="_suite"),
    ],
)
```

### 39) with_statement

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="async"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="with"),
        SymbolRule(type="SYMBOL", name="with_clause"),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
    ],
)
```

### 40) with_clause

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="with_item"),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="with_item",
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        StringRule(type="STRING", value=","),
                        BlankRule(type="BLANK"),
                    ],
                ),
            ],
        ),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="("),
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="with_item"),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="with_item",
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        StringRule(type="STRING", value=","),
                        BlankRule(type="BLANK"),
                    ],
                ),
                StringRule(type="STRING", value=")"),
            ],
        ),
    ],
)
```

### 41) with_item

```py
PrecRule(
    type="PREC_DYNAMIC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="value",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="expression"),
            )
        ],
    ),
)
```

### 42) function_definition

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="async"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="def"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameter"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        FieldRule(
            name="parameters",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="parameters"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="->"),
                        FieldRule(
                            name="return_type",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="type"
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
    ],
)
```

### 43) parameters

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_parameters"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 44) lambda_parameters

```py
SymbolRule(type="SYMBOL", name="_parameters")
```

### 45) list_splat

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="*"),
        SymbolRule(type="SYMBOL", name="expression"),
    ],
)
```

### 46) dictionary_splat

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="**"),
        SymbolRule(type="SYMBOL", name="expression"),
    ],
)
```

### 47) global_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="global"),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="identifier"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(
                                type="SYMBOL", name="identifier"
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ],
)
```

### 48) nonlocal_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="nonlocal"),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="identifier"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(
                                type="SYMBOL", name="identifier"
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ],
)
```

### 49) exec_statement

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="exec"),
        FieldRule(
            name="code",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="string"),
                    SymbolRule(type="SYMBOL", name="identifier"),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="in"),
                        SeqRule(
                            type="SEQ",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="expression"
                                ),
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            StringRule(
                                                type="STRING",
                                                value=",",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="expression",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 50) type_alias_statement

```py
PrecRule(
    type="PREC_DYNAMIC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="type"),
            SymbolRule(type="SYMBOL", name="type"),
            StringRule(type="STRING", value="="),
            SymbolRule(type="SYMBOL", name="type"),
        ],
    ),
)
```

### 51) class_definition

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="class"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameter"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        FieldRule(
            name="superclasses",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="argument_list"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_suite"),
        ),
    ],
)
```

### 52) type_parameter

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="["),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="type"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(type="SYMBOL", name="type"),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 53) parenthesized_list_splat

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="("),
            ChoiceRule(
                type="CHOICE",
                members=[
                    AliasRule(
                        type="ALIAS",
                        value="parenthesized_expression",
                        named=True,
                        content=SymbolRule(
                            type="SYMBOL",
                            name="parenthesized_list_splat",
                        ),
                    ),
                    SymbolRule(type="SYMBOL", name="list_splat"),
                ],
            ),
            StringRule(type="STRING", value=")"),
        ],
    ),
)
```

### 54) argument_list

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="expression"
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="list_splat"
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="dictionary_splat",
                                ),
                                AliasRule(
                                    type="ALIAS",
                                    value="parenthesized_expression",
                                    named=True,
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="parenthesized_list_splat",
                                    ),
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="keyword_argument",
                                ),
                            ],
                        ),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    ChoiceRule(
                                        type="CHOICE",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="expression",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="list_splat",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="dictionary_splat",
                                            ),
                                            AliasRule(
                                                type="ALIAS",
                                                value="parenthesized_expression",
                                                named=True,
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="parenthesized_list_splat",
                                                ),
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="keyword_argument",
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 55) decorated_definition

```py
SeqRule(
    type="SEQ",
    members=[
        Repeat1Rule(
            type="REPEAT1",
            content=SymbolRule(type="SYMBOL", name="decorator"),
        ),
        FieldRule(
            name="definition",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="class_definition"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="function_definition"
                    ),
                ],
            ),
        ),
    ],
)
```

### 56) decorator

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="@"),
        SymbolRule(type="SYMBOL", name="expression"),
        SymbolRule(type="SYMBOL", name="_newline"),
    ],
)
```

### 57) _suite

```py
ChoiceRule(
    type="CHOICE",
    members=[
        AliasRule(
            type="ALIAS",
            value="block",
            named=True,
            content=SymbolRule(
                type="SYMBOL", name="_simple_statements"
            ),
        ),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="_indent"),
                SymbolRule(type="SYMBOL", name="block"),
            ],
        ),
        AliasRule(
            type="ALIAS",
            value="block",
            named=True,
            content=SymbolRule(type="SYMBOL", name="_newline"),
        ),
    ],
)
```

### 58) block

```py
SeqRule(
    type="SEQ",
    members=[
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="_statement"),
        ),
        SymbolRule(type="SYMBOL", name="_dedent"),
    ],
)
```

### 59) expression_list

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="expression"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value=","),
                    SeqRule(
                        type="SEQ",
                        members=[
                            Repeat1Rule(
                                type="REPEAT1",
                                content=SeqRule(
                                    type="SEQ",
                                    members=[
                                        StringRule(
                                            type="STRING", value=","
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="expression",
                                        ),
                                    ],
                                ),
                            ),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ),
)
```

### 60) dotted_name

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="identifier"),
            RepeatRule(
                type="REPEAT",
                content=SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="."),
                        SymbolRule(type="SYMBOL", name="identifier"),
                    ],
                ),
            ),
        ],
    ),
)
```

### 61) case_pattern

```py
PrecRule(
    type="PREC",
    value=1,
    content=ChoiceRule(
        type="CHOICE",
        members=[
            AliasRule(
                type="ALIAS",
                value="as_pattern",
                named=True,
                content=SymbolRule(type="SYMBOL", name="_as_pattern"),
            ),
            SymbolRule(type="SYMBOL", name="keyword_pattern"),
            SymbolRule(type="SYMBOL", name="_simple_pattern"),
        ],
    ),
)
```

### 62) _simple_pattern

```py
PrecRule(
    type="PREC",
    value=1,
    content=ChoiceRule(
        type="CHOICE",
        members=[
            SymbolRule(type="SYMBOL", name="class_pattern"),
            SymbolRule(type="SYMBOL", name="splat_pattern"),
            SymbolRule(type="SYMBOL", name="union_pattern"),
            AliasRule(
                type="ALIAS",
                value="list_pattern",
                named=True,
                content=SymbolRule(
                    type="SYMBOL", name="_list_pattern"
                ),
            ),
            AliasRule(
                type="ALIAS",
                value="tuple_pattern",
                named=True,
                content=SymbolRule(
                    type="SYMBOL", name="_tuple_pattern"
                ),
            ),
            SymbolRule(type="SYMBOL", name="dict_pattern"),
            SymbolRule(type="SYMBOL", name="string"),
            SymbolRule(type="SYMBOL", name="concatenated_string"),
            SymbolRule(type="SYMBOL", name="true"),
            SymbolRule(type="SYMBOL", name="false"),
            SymbolRule(type="SYMBOL", name="none"),
            SeqRule(
                type="SEQ",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            StringRule(type="STRING", value="-"),
                            BlankRule(type="BLANK"),
                        ],
                    ),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            SymbolRule(type="SYMBOL", name="integer"),
                            SymbolRule(type="SYMBOL", name="float"),
                        ],
                    ),
                ],
            ),
            SymbolRule(type="SYMBOL", name="complex_pattern"),
            SymbolRule(type="SYMBOL", name="dotted_name"),
            StringRule(type="STRING", value="_"),
        ],
    ),
)
```

### 63) _as_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="case_pattern"),
        StringRule(type="STRING", value="as"),
        SymbolRule(type="SYMBOL", name="identifier"),
    ],
)
```

### 64) union_pattern

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="_simple_pattern"),
            Repeat1Rule(
                type="REPEAT1",
                content=PrecRule(
                    type="PREC_LEFT",
                    value=0,
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value="|"),
                            SymbolRule(
                                type="SYMBOL", name="_simple_pattern"
                            ),
                        ],
                    ),
                ),
            ),
        ],
    ),
)
```

### 65) _list_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="["),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="case_pattern"
                                ),
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            StringRule(
                                                type="STRING",
                                                value=",",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="case_pattern",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value=","),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 66) _tuple_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="case_pattern"
                                ),
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            StringRule(
                                                type="STRING",
                                                value=",",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="case_pattern",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value=","),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 67) dict_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="{"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="_key_value_pattern",
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="splat_pattern",
                                        ),
                                    ],
                                ),
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            StringRule(
                                                type="STRING",
                                                value=",",
                                            ),
                                            ChoiceRule(
                                                type="CHOICE",
                                                members=[
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="_key_value_pattern",
                                                    ),
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="splat_pattern",
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value=","),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 68) _key_value_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="key",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_simple_pattern"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="case_pattern"),
        ),
    ],
)
```

### 69) keyword_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="identifier"),
        StringRule(type="STRING", value="="),
        SymbolRule(type="SYMBOL", name="_simple_pattern"),
    ],
)
```

### 70) splat_pattern

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="*"),
                    StringRule(type="STRING", value="**"),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    StringRule(type="STRING", value="_"),
                ],
            ),
        ],
    ),
)
```

### 71) class_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="dotted_name"),
        StringRule(type="STRING", value="("),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="case_pattern"
                                ),
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            StringRule(
                                                type="STRING",
                                                value=",",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="case_pattern",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value=","),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 72) complex_pattern

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="-"),
                    BlankRule(type="BLANK"),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="integer"),
                    SymbolRule(type="SYMBOL", name="float"),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="+"),
                    StringRule(type="STRING", value="-"),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="integer"),
                    SymbolRule(type="SYMBOL", name="float"),
                ],
            ),
        ],
    ),
)
```

### 73) _parameters

```py
SeqRule(
    type="SEQ",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="parameter"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(
                                type="SYMBOL", name="parameter"
                            ),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 74) _patterns

```py
SeqRule(
    type="SEQ",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="pattern"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(type="SYMBOL", name="pattern"),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 75) parameter

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="identifier"),
        SymbolRule(type="SYMBOL", name="typed_parameter"),
        SymbolRule(type="SYMBOL", name="default_parameter"),
        SymbolRule(type="SYMBOL", name="typed_default_parameter"),
        SymbolRule(type="SYMBOL", name="list_splat_pattern"),
        SymbolRule(type="SYMBOL", name="tuple_pattern"),
        SymbolRule(type="SYMBOL", name="keyword_separator"),
        SymbolRule(type="SYMBOL", name="positional_separator"),
        SymbolRule(type="SYMBOL", name="dictionary_splat_pattern"),
    ],
)
```

### 76) pattern

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="identifier"),
        SymbolRule(type="SYMBOL", name="keyword_identifier"),
        SymbolRule(type="SYMBOL", name="subscript"),
        SymbolRule(type="SYMBOL", name="attribute"),
        SymbolRule(type="SYMBOL", name="list_splat_pattern"),
        SymbolRule(type="SYMBOL", name="tuple_pattern"),
        SymbolRule(type="SYMBOL", name="list_pattern"),
    ],
)
```

### 77) tuple_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_patterns"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 78) list_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="["),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_patterns"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 79) default_parameter

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="name",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(type="SYMBOL", name="tuple_pattern"),
                ],
            ),
        ),
        StringRule(type="STRING", value="="),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
    ],
)
```

### 80) typed_default_parameter

```py
PrecRule(
    type="PREC",
    value=-1,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="name",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="identifier"),
            ),
            StringRule(type="STRING", value=":"),
            FieldRule(
                name="type",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="type"),
            ),
            StringRule(type="STRING", value="="),
            FieldRule(
                name="value",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="expression"),
            ),
        ],
    ),
)
```

### 81) list_splat_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="*"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="identifier"),
                SymbolRule(type="SYMBOL", name="keyword_identifier"),
                SymbolRule(type="SYMBOL", name="subscript"),
                SymbolRule(type="SYMBOL", name="attribute"),
            ],
        ),
    ],
)
```

### 82) dictionary_splat_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="**"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="identifier"),
                SymbolRule(type="SYMBOL", name="keyword_identifier"),
                SymbolRule(type="SYMBOL", name="subscript"),
                SymbolRule(type="SYMBOL", name="attribute"),
            ],
        ),
    ],
)
```

### 83) as_pattern

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="expression"),
            StringRule(type="STRING", value="as"),
            FieldRule(
                name="alias",
                type="FIELD",
                content=AliasRule(
                    type="ALIAS",
                    value="as_pattern_target",
                    named=True,
                    content=SymbolRule(
                        type="SYMBOL", name="expression"
                    ),
                ),
            ),
        ],
    ),
)
```

### 84) _expression_within_for_in_clause

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="expression"),
        AliasRule(
            type="ALIAS",
            value="lambda",
            named=True,
            content=SymbolRule(
                type="SYMBOL", name="lambda_within_for_in_clause"
            ),
        ),
    ],
)
```

### 85) expression

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="comparison_operator"),
        SymbolRule(type="SYMBOL", name="not_operator"),
        SymbolRule(type="SYMBOL", name="boolean_operator"),
        SymbolRule(type="SYMBOL", name="lambda"),
        SymbolRule(type="SYMBOL", name="primary_expression"),
        SymbolRule(type="SYMBOL", name="conditional_expression"),
        SymbolRule(type="SYMBOL", name="named_expression"),
        SymbolRule(type="SYMBOL", name="as_pattern"),
    ],
)
```

### 86) primary_expression

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="await"),
        SymbolRule(type="SYMBOL", name="binary_operator"),
        SymbolRule(type="SYMBOL", name="identifier"),
        SymbolRule(type="SYMBOL", name="keyword_identifier"),
        SymbolRule(type="SYMBOL", name="string"),
        SymbolRule(type="SYMBOL", name="concatenated_string"),
        SymbolRule(type="SYMBOL", name="integer"),
        SymbolRule(type="SYMBOL", name="float"),
        SymbolRule(type="SYMBOL", name="true"),
        SymbolRule(type="SYMBOL", name="false"),
        SymbolRule(type="SYMBOL", name="none"),
        SymbolRule(type="SYMBOL", name="unary_operator"),
        SymbolRule(type="SYMBOL", name="attribute"),
        SymbolRule(type="SYMBOL", name="subscript"),
        SymbolRule(type="SYMBOL", name="call"),
        SymbolRule(type="SYMBOL", name="list"),
        SymbolRule(type="SYMBOL", name="list_comprehension"),
        SymbolRule(type="SYMBOL", name="dictionary"),
        SymbolRule(type="SYMBOL", name="dictionary_comprehension"),
        SymbolRule(type="SYMBOL", name="set"),
        SymbolRule(type="SYMBOL", name="set_comprehension"),
        SymbolRule(type="SYMBOL", name="tuple"),
        SymbolRule(type="SYMBOL", name="parenthesized_expression"),
        SymbolRule(type="SYMBOL", name="generator_expression"),
        SymbolRule(type="SYMBOL", name="ellipsis"),
        AliasRule(
            type="ALIAS",
            value="list_splat",
            named=True,
            content=SymbolRule(
                type="SYMBOL", name="list_splat_pattern"
            ),
        ),
    ],
)
```

### 87) not_operator

```py
PrecRule(
    type="PREC",
    value=12,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="not"),
            FieldRule(
                name="argument",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="expression"),
            ),
        ],
    ),
)
```

### 88) boolean_operator

```py
ChoiceRule(
    type="CHOICE",
    members=[
        PrecRule(
            type="PREC_LEFT",
            value=11,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(
                            type="STRING", value="and"
                        ),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=10,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="or"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="expression"
                        ),
                    ),
                ],
            ),
        ),
    ],
)
```

### 89) binary_operator

```py
ChoiceRule(
    type="CHOICE",
    members=[
        PrecRule(
            type="PREC_LEFT",
            value=18,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="+"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=18,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="-"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=19,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="*"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=19,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="@"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=19,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="/"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=19,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="%"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=19,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="//"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_RIGHT",
            value=21,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="**"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=14,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="|"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=15,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="&"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=16,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="^"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=17,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="<<"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=17,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value=">>"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ),
                ],
            ),
        ),
    ],
)
```

### 90) unary_operator

```py
PrecRule(
    type="PREC",
    value=20,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="operator",
                type="FIELD",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        StringRule(type="STRING", value="+"),
                        StringRule(type="STRING", value="-"),
                        StringRule(type="STRING", value="~"),
                    ],
                ),
            ),
            FieldRule(
                name="argument",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="primary_expression"
                ),
            ),
        ],
    ),
)
```

### 91) comparison_operator

```py
PrecRule(
    type="PREC_LEFT",
    value=13,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="primary_expression"),
            Repeat1Rule(
                type="REPEAT1",
                content=SeqRule(
                    type="SEQ",
                    members=[
                        FieldRule(
                            name="operators",
                            type="FIELD",
                            content=ChoiceRule(
                                type="CHOICE",
                                members=[
                                    StringRule(
                                        type="STRING", value="<"
                                    ),
                                    StringRule(
                                        type="STRING", value="<="
                                    ),
                                    StringRule(
                                        type="STRING", value="=="
                                    ),
                                    StringRule(
                                        type="STRING", value="!="
                                    ),
                                    StringRule(
                                        type="STRING", value=">="
                                    ),
                                    StringRule(
                                        type="STRING", value=">"
                                    ),
                                    StringRule(
                                        type="STRING", value="<>"
                                    ),
                                    StringRule(
                                        type="STRING", value="in"
                                    ),
                                    AliasRule(
                                        type="ALIAS",
                                        value="not in",
                                        named=False,
                                        content=SeqRule(
                                            type="SEQ",
                                            members=[
                                                StringRule(
                                                    type="STRING",
                                                    value="not",
                                                ),
                                                StringRule(
                                                    type="STRING",
                                                    value="in",
                                                ),
                                            ],
                                        ),
                                    ),
                                    StringRule(
                                        type="STRING", value="is"
                                    ),
                                    AliasRule(
                                        type="ALIAS",
                                        value="is not",
                                        named=False,
                                        content=SeqRule(
                                            type="SEQ",
                                            members=[
                                                StringRule(
                                                    type="STRING",
                                                    value="is",
                                                ),
                                                StringRule(
                                                    type="STRING",
                                                    value="not",
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        SymbolRule(
                            type="SYMBOL", name="primary_expression"
                        ),
                    ],
                ),
            ),
        ],
    ),
)
```

### 92) lambda

```py
PrecRule(
    type="PREC",
    value=-2,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="lambda"),
            FieldRule(
                name="parameters",
                type="FIELD",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(
                            type="SYMBOL", name="lambda_parameters"
                        ),
                        BlankRule(type="BLANK"),
                    ],
                ),
            ),
            StringRule(type="STRING", value=":"),
            FieldRule(
                name="body",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="expression"),
            ),
        ],
    ),
)
```

### 93) lambda_within_for_in_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="lambda"),
        FieldRule(
            name="parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="lambda_parameters"
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_expression_within_for_in_clause"
            ),
        ),
    ],
)
```

### 94) assignment

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="left",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_left_hand_side"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="="),
                        FieldRule(
                            name="right",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_right_hand_side"
                            ),
                        ),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value=":"),
                        FieldRule(
                            name="type",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="type"
                            ),
                        ),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value=":"),
                        FieldRule(
                            name="type",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="type"
                            ),
                        ),
                        StringRule(type="STRING", value="="),
                        FieldRule(
                            name="right",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_right_hand_side"
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ],
)
```

### 95) augmented_assignment

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="left",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_left_hand_side"),
        ),
        FieldRule(
            name="operator",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="+="),
                    StringRule(type="STRING", value="-="),
                    StringRule(type="STRING", value="*="),
                    StringRule(type="STRING", value="/="),
                    StringRule(type="STRING", value="@="),
                    StringRule(type="STRING", value="//="),
                    StringRule(type="STRING", value="%="),
                    StringRule(type="STRING", value="**="),
                    StringRule(type="STRING", value=">>="),
                    StringRule(type="STRING", value="<<="),
                    StringRule(type="STRING", value="&="),
                    StringRule(type="STRING", value="^="),
                    StringRule(type="STRING", value="|="),
                ],
            ),
        ),
        FieldRule(
            name="right",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_right_hand_side"
            ),
        ),
    ],
)
```

### 96) _left_hand_side

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="pattern"),
        SymbolRule(type="SYMBOL", name="pattern_list"),
    ],
)
```

### 97) pattern_list

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="pattern"),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                SeqRule(
                    type="SEQ",
                    members=[
                        Repeat1Rule(
                            type="REPEAT1",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    SymbolRule(
                                        type="SYMBOL", name="pattern"
                                    ),
                                ],
                            ),
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value=","),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
```

### 98) _right_hand_side

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="expression"),
        SymbolRule(type="SYMBOL", name="expression_list"),
        SymbolRule(type="SYMBOL", name="assignment"),
        SymbolRule(type="SYMBOL", name="augmented_assignment"),
        SymbolRule(type="SYMBOL", name="pattern_list"),
        SymbolRule(type="SYMBOL", name="yield"),
    ],
)
```

### 99) yield

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="yield"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value="from"),
                            SymbolRule(
                                type="SYMBOL", name="expression"
                            ),
                        ],
                    ),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            SymbolRule(
                                type="SYMBOL", name="_expressions"
                            ),
                            BlankRule(type="BLANK"),
                        ],
                    ),
                ],
            ),
        ],
    ),
)
```

### 100) attribute

```py
PrecRule(
    type="PREC",
    value=22,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="object",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="primary_expression"
                ),
            ),
            StringRule(type="STRING", value="."),
            FieldRule(
                name="attribute",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="identifier"),
            ),
        ],
    ),
)
```

### 101) subscript

```py
PrecRule(
    type="PREC",
    value=22,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="value",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="primary_expression"
                ),
            ),
            StringRule(type="STRING", value="["),
            SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="subscript",
                        type="FIELD",
                        content=ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="expression"
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="slice"
                                ),
                            ],
                        ),
                    ),
                    RepeatRule(
                        type="REPEAT",
                        content=SeqRule(
                            type="SEQ",
                            members=[
                                StringRule(type="STRING", value=","),
                                FieldRule(
                                    name="subscript",
                                    type="FIELD",
                                    content=ChoiceRule(
                                        type="CHOICE",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="expression",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="slice",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value=","),
                    BlankRule(type="BLANK"),
                ],
            ),
            StringRule(type="STRING", value="]"),
        ],
    ),
)
```

### 102) slice

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="expression"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=":"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="expression"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value=":"),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="expression"
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 103) ellipsis

```py
StringRule(type="STRING", value="...")
```

### 104) call

```py
PrecRule(
    type="PREC",
    value=22,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="function",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="primary_expression"
                ),
            ),
            FieldRule(
                name="arguments",
                type="FIELD",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(
                            type="SYMBOL", name="generator_expression"
                        ),
                        SymbolRule(
                            type="SYMBOL", name="argument_list"
                        ),
                    ],
                ),
            ),
        ],
    ),
)
```

### 105) typed_parameter

```py
PrecRule(
    type="PREC",
    value=-1,
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(
                        type="SYMBOL", name="list_splat_pattern"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="dictionary_splat_pattern"
                    ),
                ],
            ),
            StringRule(type="STRING", value=":"),
            FieldRule(
                name="type",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="type"),
            ),
        ],
    ),
)
```

### 106) type

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="expression"),
        SymbolRule(type="SYMBOL", name="splat_type"),
        SymbolRule(type="SYMBOL", name="generic_type"),
        SymbolRule(type="SYMBOL", name="union_type"),
        SymbolRule(type="SYMBOL", name="constrained_type"),
        SymbolRule(type="SYMBOL", name="member_type"),
    ],
)
```

### 107) splat_type

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="*"),
                    StringRule(type="STRING", value="**"),
                ],
            ),
            SymbolRule(type="SYMBOL", name="identifier"),
        ],
    ),
)
```

### 108) generic_type

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="identifier"),
            SymbolRule(type="SYMBOL", name="type_parameter"),
        ],
    ),
)
```

### 109) union_type

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="type"),
            StringRule(type="STRING", value="|"),
            SymbolRule(type="SYMBOL", name="type"),
        ],
    ),
)
```

### 110) constrained_type

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="type"),
            StringRule(type="STRING", value=":"),
            SymbolRule(type="SYMBOL", name="type"),
        ],
    ),
)
```

### 111) member_type

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="type"),
        StringRule(type="STRING", value="."),
        SymbolRule(type="SYMBOL", name="identifier"),
    ],
)
```

### 112) keyword_argument

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="name",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(
                        type="SYMBOL", name="keyword_identifier"
                    ),
                ],
            ),
        ),
        StringRule(type="STRING", value="="),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
    ],
)
```

### 113) list

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="["),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(
                    type="SYMBOL", name="_collection_elements"
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 114) set

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="{"),
        SymbolRule(type="SYMBOL", name="_collection_elements"),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 115) tuple

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(
                    type="SYMBOL", name="_collection_elements"
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 116) dictionary

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="{"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="pair"
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="dictionary_splat",
                                ),
                            ],
                        ),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    ChoiceRule(
                                        type="CHOICE",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="pair",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="dictionary_splat",
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 117) pair

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="key",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
    ],
)
```

### 118) list_comprehension

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="["),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
        SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 119) dictionary_comprehension

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="{"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="pair"),
        ),
        SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 120) set_comprehension

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="{"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
        SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 121) generator_expression

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="expression"),
        ),
        SymbolRule(type="SYMBOL", name="_comprehension_clauses"),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 122) _comprehension_clauses

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="for_in_clause"),
        RepeatRule(
            type="REPEAT",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="for_in_clause"),
                    SymbolRule(type="SYMBOL", name="if_clause"),
                ],
            ),
        ),
    ],
)
```

### 123) parenthesized_expression

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="("),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="expression"),
                    SymbolRule(type="SYMBOL", name="yield"),
                ],
            ),
            StringRule(type="STRING", value=")"),
        ],
    ),
)
```

### 124) _collection_elements

```py
SeqRule(
    type="SEQ",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(type="SYMBOL", name="expression"),
                        SymbolRule(type="SYMBOL", name="yield"),
                        SymbolRule(type="SYMBOL", name="list_splat"),
                        SymbolRule(
                            type="SYMBOL",
                            name="parenthesized_list_splat",
                        ),
                    ],
                ),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="expression",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL", name="yield"
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="list_splat",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="parenthesized_list_splat",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=","),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 125) for_in_clause

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="async"),
                    BlankRule(type="BLANK"),
                ],
            ),
            StringRule(type="STRING", value="for"),
            FieldRule(
                name="left",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="_left_hand_side"
                ),
            ),
            StringRule(type="STRING", value="in"),
            FieldRule(
                name="right",
                type="FIELD",
                content=SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(
                            type="SYMBOL",
                            name="_expression_within_for_in_clause",
                        ),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="_expression_within_for_in_clause",
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value=","),
                    BlankRule(type="BLANK"),
                ],
            ),
        ],
    ),
)
```

### 126) if_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="if"),
        SymbolRule(type="SYMBOL", name="expression"),
    ],
)
```

### 127) conditional_expression

```py
PrecRule(
    type="PREC_RIGHT",
    value=-1,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="expression"),
            StringRule(type="STRING", value="if"),
            SymbolRule(type="SYMBOL", name="expression"),
            StringRule(type="STRING", value="else"),
            SymbolRule(type="SYMBOL", name="expression"),
        ],
    ),
)
```

### 128) concatenated_string

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="string"),
        Repeat1Rule(
            type="REPEAT1",
            content=SymbolRule(type="SYMBOL", name="string"),
        ),
    ],
)
```

### 129) string

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="string_start"),
        RepeatRule(
            type="REPEAT",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="interpolation"),
                    SymbolRule(type="SYMBOL", name="string_content"),
                ],
            ),
        ),
        SymbolRule(type="SYMBOL", name="string_end"),
    ],
)
```

### 130) string_content

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=Repeat1Rule(
        type="REPEAT1",
        content=ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(
                    type="SYMBOL", name="escape_interpolation"
                ),
                SymbolRule(type="SYMBOL", name="escape_sequence"),
                SymbolRule(
                    type="SYMBOL", name="_not_escape_sequence"
                ),
                SymbolRule(type="SYMBOL", name="_string_content"),
            ],
        ),
    ),
)
```

### 131) interpolation

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="{"),
        FieldRule(
            name="expression",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_f_expression"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="="),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                FieldRule(
                    name="type_conversion",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="type_conversion"
                    ),
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                FieldRule(
                    name="format_specifier",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="format_specifier"
                    ),
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 132) _f_expression

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="expression"),
        SymbolRule(type="SYMBOL", name="expression_list"),
        SymbolRule(type="SYMBOL", name="pattern_list"),
        SymbolRule(type="SYMBOL", name="yield"),
    ],
)
```

### 133) escape_sequence

```py
TokenRule(
    type="IMMEDIATE_TOKEN",
    content=PrecRule(
        type="PREC",
        value=1,
        content=SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="\\"),
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        PatternRule(
                            type="PATTERN",
                            value="u[a-fA-F\\d]{4}",
                            flags=None,
                        ),
                        PatternRule(
                            type="PATTERN",
                            value="U[a-fA-F\\d]{8}",
                            flags=None,
                        ),
                        PatternRule(
                            type="PATTERN",
                            value="x[a-fA-F\\d]{2}",
                            flags=None,
                        ),
                        PatternRule(
                            type="PATTERN",
                            value="\\d{1,3}",
                            flags=None,
                        ),
                        PatternRule(
                            type="PATTERN",
                            value="\\r?\\n",
                            flags=None,
                        ),
                        PatternRule(
                            type="PATTERN",
                            value="['\"abfrntv\\\\]",
                            flags=None,
                        ),
                        PatternRule(
                            type="PATTERN",
                            value="N\\{[^}]+\\}",
                            flags=None,
                        ),
                    ],
                ),
            ],
        ),
    ),
)
```

### 134) _not_escape_sequence

```py
TokenRule(
    type="IMMEDIATE_TOKEN",
    content=StringRule(type="STRING", value="\\"),
)
```

### 135) format_specifier

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value=":"),
        RepeatRule(
            type="REPEAT",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    TokenRule(
                        type="TOKEN",
                        content=PrecRule(
                            type="PREC",
                            value=1,
                            content=PatternRule(
                                type="PATTERN",
                                value="[^{}\\n]+",
                                flags=None,
                            ),
                        ),
                    ),
                    AliasRule(
                        type="ALIAS",
                        value="format_expression",
                        named=True,
                        content=SymbolRule(
                            type="SYMBOL", name="interpolation"
                        ),
                    ),
                ],
            ),
        ),
    ],
)
```

### 136) type_conversion

```py
PatternRule(type="PATTERN", value="![a-z]", flags=None)
```

### 137) integer

```py
TokenRule(
    type="TOKEN",
    content=ChoiceRule(
        type="CHOICE",
        members=[
            SeqRule(
                type="SEQ",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            StringRule(type="STRING", value="0x"),
                            StringRule(type="STRING", value="0X"),
                        ],
                    ),
                    Repeat1Rule(
                        type="REPEAT1",
                        content=PatternRule(
                            type="PATTERN",
                            value="_?[A-Fa-f0-9]+",
                            flags=None,
                        ),
                    ),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            PatternRule(
                                type="PATTERN",
                                value="[Ll]",
                                flags=None,
                            ),
                            BlankRule(type="BLANK"),
                        ],
                    ),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            StringRule(type="STRING", value="0o"),
                            StringRule(type="STRING", value="0O"),
                        ],
                    ),
                    Repeat1Rule(
                        type="REPEAT1",
                        content=PatternRule(
                            type="PATTERN",
                            value="_?[0-7]+",
                            flags=None,
                        ),
                    ),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            PatternRule(
                                type="PATTERN",
                                value="[Ll]",
                                flags=None,
                            ),
                            BlankRule(type="BLANK"),
                        ],
                    ),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            StringRule(type="STRING", value="0b"),
                            StringRule(type="STRING", value="0B"),
                        ],
                    ),
                    Repeat1Rule(
                        type="REPEAT1",
                        content=PatternRule(
                            type="PATTERN",
                            value="_?[0-1]+",
                            flags=None,
                        ),
                    ),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            PatternRule(
                                type="PATTERN",
                                value="[Ll]",
                                flags=None,
                            ),
                            BlankRule(type="BLANK"),
                        ],
                    ),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    Repeat1Rule(
                        type="REPEAT1",
                        content=PatternRule(
                            type="PATTERN",
                            value="[0-9]+_?",
                            flags=None,
                        ),
                    ),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    PatternRule(
                                        type="PATTERN",
                                        value="[Ll]",
                                        flags=None,
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    PatternRule(
                                        type="PATTERN",
                                        value="[jJ]",
                                        flags=None,
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ),
)
```

### 138) float

```py
TokenRule(
    type="TOKEN",
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    SeqRule(
                        type="SEQ",
                        members=[
                            Repeat1Rule(
                                type="REPEAT1",
                                content=PatternRule(
                                    type="PATTERN",
                                    value="[0-9]+_?",
                                    flags=None,
                                ),
                            ),
                            StringRule(type="STRING", value="."),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    Repeat1Rule(
                                        type="REPEAT1",
                                        content=PatternRule(
                                            type="PATTERN",
                                            value="[0-9]+_?",
                                            flags=None,
                                        ),
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            PatternRule(
                                                type="PATTERN",
                                                value="[eE][\\+-]?",
                                                flags=None,
                                            ),
                                            Repeat1Rule(
                                                type="REPEAT1",
                                                content=PatternRule(
                                                    type="PATTERN",
                                                    value="[0-9]+_?",
                                                    flags=None,
                                                ),
                                            ),
                                        ],
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                        ],
                    ),
                    SeqRule(
                        type="SEQ",
                        members=[
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    Repeat1Rule(
                                        type="REPEAT1",
                                        content=PatternRule(
                                            type="PATTERN",
                                            value="[0-9]+_?",
                                            flags=None,
                                        ),
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                            StringRule(type="STRING", value="."),
                            Repeat1Rule(
                                type="REPEAT1",
                                content=PatternRule(
                                    type="PATTERN",
                                    value="[0-9]+_?",
                                    flags=None,
                                ),
                            ),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            PatternRule(
                                                type="PATTERN",
                                                value="[eE][\\+-]?",
                                                flags=None,
                                            ),
                                            Repeat1Rule(
                                                type="REPEAT1",
                                                content=PatternRule(
                                                    type="PATTERN",
                                                    value="[0-9]+_?",
                                                    flags=None,
                                                ),
                                            ),
                                        ],
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                        ],
                    ),
                    SeqRule(
                        type="SEQ",
                        members=[
                            Repeat1Rule(
                                type="REPEAT1",
                                content=PatternRule(
                                    type="PATTERN",
                                    value="[0-9]+_?",
                                    flags=None,
                                ),
                            ),
                            SeqRule(
                                type="SEQ",
                                members=[
                                    PatternRule(
                                        type="PATTERN",
                                        value="[eE][\\+-]?",
                                        flags=None,
                                    ),
                                    Repeat1Rule(
                                        type="REPEAT1",
                                        content=PatternRule(
                                            type="PATTERN",
                                            value="[0-9]+_?",
                                            flags=None,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    PatternRule(
                        type="PATTERN", value="[jJ]", flags=None
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
        ],
    ),
)
```

### 139) identifier

```py
PatternRule(
    type="PATTERN",
    value="[_\\p{XID_Start}][_\\p{XID_Continue}]*",
    flags=None,
)
```

### 140) keyword_identifier

```py
ChoiceRule(
    type="CHOICE",
    members=[
        PrecRule(
            type="PREC",
            value=-3,
            content=AliasRule(
                type="ALIAS",
                value="identifier",
                named=True,
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        StringRule(type="STRING", value="print"),
                        StringRule(type="STRING", value="exec"),
                        StringRule(type="STRING", value="async"),
                        StringRule(type="STRING", value="await"),
                        StringRule(type="STRING", value="match"),
                    ],
                ),
            ),
        ),
        AliasRule(
            type="ALIAS",
            value="identifier",
            named=True,
            content=StringRule(type="STRING", value="type"),
        ),
    ],
)
```

### 141) true

```py
StringRule(type="STRING", value="True")
```

### 142) false

```py
StringRule(type="STRING", value="False")
```

### 143) none

```py
StringRule(type="STRING", value="None")
```

### 144) await

```py
PrecRule(
    type="PREC",
    value=20,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="await"),
            SymbolRule(type="SYMBOL", name="primary_expression"),
        ],
    ),
)
```

### 145) comment

```py
TokenRule(
    type="TOKEN",
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="#"),
            PatternRule(type="PATTERN", value=".*", flags=None),
        ],
    ),
)
```

### 146) line_continuation

```py
TokenRule(
    type="TOKEN",
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="\\"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SeqRule(
                        type="SEQ",
                        members=[
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    StringRule(
                                        type="STRING", value="\r"
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                            StringRule(type="STRING", value="\n"),
                        ],
                    ),
                    StringRule(type="STRING", value="\x00"),
                ],
            ),
        ],
    ),
)
```

### 147) positional_separator

```py
StringRule(type="STRING", value="/")
```

### 148) keyword_separator

```py
StringRule(type="STRING", value="*")
```

## Extras

### 1)

```py
SymbolRule(type="SYMBOL", name="comment")
```

### 2)

```py
PatternRule(
    type="PATTERN",
    value="[\\s\\f\\uFEFF\\u2060\\u200B]|\\r?\\n",
    flags=None,
)
```

### 3)

```py
SymbolRule(type="SYMBOL", name="line_continuation")
```

## Precedences

## Externals

### 1)

```py
SymbolRule(type="SYMBOL", name="_newline")
```

### 2)

```py
SymbolRule(type="SYMBOL", name="_indent")
```

### 3)

```py
SymbolRule(type="SYMBOL", name="_dedent")
```

### 4)

```py
SymbolRule(type="SYMBOL", name="string_start")
```

### 5)

```py
SymbolRule(type="SYMBOL", name="_string_content")
```

### 6)

```py
SymbolRule(type="SYMBOL", name="escape_interpolation")
```

### 7)

```py
SymbolRule(type="SYMBOL", name="string_end")
```

### 8)

```py
SymbolRule(type="SYMBOL", name="comment")
```

### 9)

```py
StringRule(type="STRING", value="]")
```

### 10)

```py
StringRule(type="STRING", value=")")
```

### 11)

```py
StringRule(type="STRING", value="}")
```

### 12)

```py
StringRule(type="STRING", value="except")
```

## Inline

### 1) _simple_statement

### 2) _compound_statement

### 3) _suite

### 4) _expressions

### 5) _left_hand_side

### 6) keyword_identifier

## Conflicts

### 1) primary_expression + pattern

### 2) primary_expression + list_splat_pattern

### 3) tuple + tuple_pattern

### 4) list + list_pattern

### 5) with_item + _collection_elements

### 6) named_expression + as_pattern

### 7) print_statement + primary_expression

### 8) type_alias_statement + primary_expression

## Word

identifier

## supertypes

### 1) _simple_statement

### 2) _compound_statement

### 3) expression

### 4) primary_expression

### 5) pattern

### 6) parameter

