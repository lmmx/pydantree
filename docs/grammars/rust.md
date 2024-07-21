# Rust

## Rules

### 1) source_file

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="shebang"),
                BlankRule(type="BLANK"),
            ],
        ),
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="_statement"),
        ),
    ],
)
```

### 2) _statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="expression_statement"),
        SymbolRule(type="SYMBOL", name="_declaration_statement"),
    ],
)
```

### 3) empty_statement

```py
StringRule(type="STRING", value=";")
```

### 4) expression_statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="_expression"),
                StringRule(type="STRING", value=";"),
            ],
        ),
        PrecRule(
            type="PREC",
            value=1,
            content=SymbolRule(
                type="SYMBOL", name="_expression_ending_with_block"
            ),
        ),
    ],
)
```

### 5) _declaration_statement

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="const_item"),
        SymbolRule(type="SYMBOL", name="macro_invocation"),
        SymbolRule(type="SYMBOL", name="macro_definition"),
        SymbolRule(type="SYMBOL", name="empty_statement"),
        SymbolRule(type="SYMBOL", name="attribute_item"),
        SymbolRule(type="SYMBOL", name="inner_attribute_item"),
        SymbolRule(type="SYMBOL", name="mod_item"),
        SymbolRule(type="SYMBOL", name="foreign_mod_item"),
        SymbolRule(type="SYMBOL", name="struct_item"),
        SymbolRule(type="SYMBOL", name="union_item"),
        SymbolRule(type="SYMBOL", name="enum_item"),
        SymbolRule(type="SYMBOL", name="type_item"),
        SymbolRule(type="SYMBOL", name="function_item"),
        SymbolRule(type="SYMBOL", name="function_signature_item"),
        SymbolRule(type="SYMBOL", name="impl_item"),
        SymbolRule(type="SYMBOL", name="trait_item"),
        SymbolRule(type="SYMBOL", name="associated_type"),
        SymbolRule(type="SYMBOL", name="let_declaration"),
        SymbolRule(type="SYMBOL", name="use_declaration"),
        SymbolRule(type="SYMBOL", name="extern_crate_declaration"),
        SymbolRule(type="SYMBOL", name="static_item"),
    ],
)
```

### 6) macro_definition

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="macro_rules!"),
        FieldRule(
            name="name",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(
                        type="SYMBOL", name="_reserved_identifier"
                    ),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="("),
                        SeqRule(
                            type="SEQ",
                            members=[
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="macro_rule",
                                            ),
                                            StringRule(
                                                type="STRING",
                                                value=";",
                                            ),
                                        ],
                                    ),
                                ),
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="macro_rule",
                                        ),
                                        BlankRule(type="BLANK"),
                                    ],
                                ),
                            ],
                        ),
                        StringRule(type="STRING", value=")"),
                        StringRule(type="STRING", value=";"),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="["),
                        SeqRule(
                            type="SEQ",
                            members=[
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="macro_rule",
                                            ),
                                            StringRule(
                                                type="STRING",
                                                value=";",
                                            ),
                                        ],
                                    ),
                                ),
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="macro_rule",
                                        ),
                                        BlankRule(type="BLANK"),
                                    ],
                                ),
                            ],
                        ),
                        StringRule(type="STRING", value="]"),
                        StringRule(type="STRING", value=";"),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="{"),
                        SeqRule(
                            type="SEQ",
                            members=[
                                RepeatRule(
                                    type="REPEAT",
                                    content=SeqRule(
                                        type="SEQ",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="macro_rule",
                                            ),
                                            StringRule(
                                                type="STRING",
                                                value=";",
                                            ),
                                        ],
                                    ),
                                ),
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="macro_rule",
                                        ),
                                        BlankRule(type="BLANK"),
                                    ],
                                ),
                            ],
                        ),
                        StringRule(type="STRING", value="}"),
                    ],
                ),
            ],
        ),
    ],
)
```

### 7) macro_rule

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="left",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="token_tree_pattern"
            ),
        ),
        StringRule(type="STRING", value="=>"),
        FieldRule(
            name="right",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="token_tree"),
        ),
    ],
)
```

### 8) _token_pattern

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="token_tree_pattern"),
        SymbolRule(type="SYMBOL", name="token_repetition_pattern"),
        SymbolRule(type="SYMBOL", name="token_binding_pattern"),
        SymbolRule(type="SYMBOL", name="metavariable"),
        SymbolRule(type="SYMBOL", name="_non_special_token"),
    ],
)
```

### 9) token_tree_pattern

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="("),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(
                        type="SYMBOL", name="_token_pattern"
                    ),
                ),
                StringRule(type="STRING", value=")"),
            ],
        ),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="["),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(
                        type="SYMBOL", name="_token_pattern"
                    ),
                ),
                StringRule(type="STRING", value="]"),
            ],
        ),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="{"),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(
                        type="SYMBOL", name="_token_pattern"
                    ),
                ),
                StringRule(type="STRING", value="}"),
            ],
        ),
    ],
)
```

### 10) token_binding_pattern

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="name",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="metavariable"
                ),
            ),
            StringRule(type="STRING", value=":"),
            FieldRule(
                name="type",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="fragment_specifier"
                ),
            ),
        ],
    ),
)
```

### 11) token_repetition_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="$"),
        StringRule(type="STRING", value="("),
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="_token_pattern"),
        ),
        StringRule(type="STRING", value=")"),
        ChoiceRule(
            type="CHOICE",
            members=[
                PatternRule(
                    type="PATTERN", value="[^+*?]+", flags=None
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="+"),
                StringRule(type="STRING", value="*"),
                StringRule(type="STRING", value="?"),
            ],
        ),
    ],
)
```

### 12) fragment_specifier

```py
ChoiceRule(
    type="CHOICE",
    members=[
        StringRule(type="STRING", value="block"),
        StringRule(type="STRING", value="expr"),
        StringRule(type="STRING", value="ident"),
        StringRule(type="STRING", value="item"),
        StringRule(type="STRING", value="lifetime"),
        StringRule(type="STRING", value="literal"),
        StringRule(type="STRING", value="meta"),
        StringRule(type="STRING", value="pat"),
        StringRule(type="STRING", value="path"),
        StringRule(type="STRING", value="stmt"),
        StringRule(type="STRING", value="tt"),
        StringRule(type="STRING", value="ty"),
        StringRule(type="STRING", value="vis"),
    ],
)
```

### 13) _tokens

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="token_tree"),
        SymbolRule(type="SYMBOL", name="token_repetition"),
        SymbolRule(type="SYMBOL", name="metavariable"),
        SymbolRule(type="SYMBOL", name="_non_special_token"),
    ],
)
```

### 14) token_tree

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="("),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(type="SYMBOL", name="_tokens"),
                ),
                StringRule(type="STRING", value=")"),
            ],
        ),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="["),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(type="SYMBOL", name="_tokens"),
                ),
                StringRule(type="STRING", value="]"),
            ],
        ),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="{"),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(type="SYMBOL", name="_tokens"),
                ),
                StringRule(type="STRING", value="}"),
            ],
        ),
    ],
)
```

### 15) token_repetition

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="$"),
        StringRule(type="STRING", value="("),
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="_tokens"),
        ),
        StringRule(type="STRING", value=")"),
        ChoiceRule(
            type="CHOICE",
            members=[
                PatternRule(
                    type="PATTERN", value="[^+*?]+", flags=None
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="+"),
                StringRule(type="STRING", value="*"),
                StringRule(type="STRING", value="?"),
            ],
        ),
    ],
)
```

### 16) _non_special_token

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_literal"),
        SymbolRule(type="SYMBOL", name="identifier"),
        SymbolRule(type="SYMBOL", name="mutable_specifier"),
        SymbolRule(type="SYMBOL", name="self"),
        SymbolRule(type="SYMBOL", name="super"),
        SymbolRule(type="SYMBOL", name="crate"),
        AliasRule(
            type="ALIAS",
            value="primitive_type",
            named=True,
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="u8"),
                    StringRule(type="STRING", value="i8"),
                    StringRule(type="STRING", value="u16"),
                    StringRule(type="STRING", value="i16"),
                    StringRule(type="STRING", value="u32"),
                    StringRule(type="STRING", value="i32"),
                    StringRule(type="STRING", value="u64"),
                    StringRule(type="STRING", value="i64"),
                    StringRule(type="STRING", value="u128"),
                    StringRule(type="STRING", value="i128"),
                    StringRule(type="STRING", value="isize"),
                    StringRule(type="STRING", value="usize"),
                    StringRule(type="STRING", value="f32"),
                    StringRule(type="STRING", value="f64"),
                    StringRule(type="STRING", value="bool"),
                    StringRule(type="STRING", value="str"),
                    StringRule(type="STRING", value="char"),
                ],
            ),
        ),
        PrecRule(
            type="PREC_RIGHT",
            value=0,
            content=Repeat1Rule(
                type="REPEAT1",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        StringRule(type="STRING", value="+"),
                        StringRule(type="STRING", value="-"),
                        StringRule(type="STRING", value="*"),
                        StringRule(type="STRING", value="/"),
                        StringRule(type="STRING", value="%"),
                        StringRule(type="STRING", value="^"),
                        StringRule(type="STRING", value="!"),
                        StringRule(type="STRING", value="&"),
                        StringRule(type="STRING", value="|"),
                        StringRule(type="STRING", value="&&"),
                        StringRule(type="STRING", value="||"),
                        StringRule(type="STRING", value="<<"),
                        StringRule(type="STRING", value=">>"),
                        StringRule(type="STRING", value="+="),
                        StringRule(type="STRING", value="-="),
                        StringRule(type="STRING", value="*="),
                        StringRule(type="STRING", value="/="),
                        StringRule(type="STRING", value="%="),
                        StringRule(type="STRING", value="^="),
                        StringRule(type="STRING", value="&="),
                        StringRule(type="STRING", value="|="),
                        StringRule(type="STRING", value="<<="),
                        StringRule(type="STRING", value=">>="),
                        StringRule(type="STRING", value="="),
                        StringRule(type="STRING", value="=="),
                        StringRule(type="STRING", value="!="),
                        StringRule(type="STRING", value=">"),
                        StringRule(type="STRING", value="<"),
                        StringRule(type="STRING", value=">="),
                        StringRule(type="STRING", value="<="),
                        StringRule(type="STRING", value="@"),
                        StringRule(type="STRING", value="_"),
                        StringRule(type="STRING", value="."),
                        StringRule(type="STRING", value=".."),
                        StringRule(type="STRING", value="..."),
                        StringRule(type="STRING", value="..="),
                        StringRule(type="STRING", value=","),
                        StringRule(type="STRING", value=";"),
                        StringRule(type="STRING", value=":"),
                        StringRule(type="STRING", value="::"),
                        StringRule(type="STRING", value="->"),
                        StringRule(type="STRING", value="=>"),
                        StringRule(type="STRING", value="#"),
                        StringRule(type="STRING", value="?"),
                    ],
                ),
            ),
        ),
        StringRule(type="STRING", value="'"),
        StringRule(type="STRING", value="as"),
        StringRule(type="STRING", value="async"),
        StringRule(type="STRING", value="await"),
        StringRule(type="STRING", value="break"),
        StringRule(type="STRING", value="const"),
        StringRule(type="STRING", value="continue"),
        StringRule(type="STRING", value="default"),
        StringRule(type="STRING", value="enum"),
        StringRule(type="STRING", value="fn"),
        StringRule(type="STRING", value="for"),
        StringRule(type="STRING", value="if"),
        StringRule(type="STRING", value="impl"),
        StringRule(type="STRING", value="let"),
        StringRule(type="STRING", value="loop"),
        StringRule(type="STRING", value="match"),
        StringRule(type="STRING", value="mod"),
        StringRule(type="STRING", value="pub"),
        StringRule(type="STRING", value="return"),
        StringRule(type="STRING", value="static"),
        StringRule(type="STRING", value="struct"),
        StringRule(type="STRING", value="trait"),
        StringRule(type="STRING", value="type"),
        StringRule(type="STRING", value="union"),
        StringRule(type="STRING", value="unsafe"),
        StringRule(type="STRING", value="use"),
        StringRule(type="STRING", value="where"),
        StringRule(type="STRING", value="while"),
    ],
)
```

### 17) attribute_item

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="#"),
        StringRule(type="STRING", value="["),
        SymbolRule(type="SYMBOL", name="attribute"),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 18) inner_attribute_item

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="#"),
        StringRule(type="STRING", value="!"),
        StringRule(type="STRING", value="["),
        SymbolRule(type="SYMBOL", name="attribute"),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 19) attribute

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="_path"),
        ChoiceRule(
            type="CHOICE",
            members=[
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                StringRule(type="STRING", value="="),
                                FieldRule(
                                    name="value",
                                    type="FIELD",
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="_expression",
                                    ),
                                ),
                            ],
                        ),
                        FieldRule(
                            name="arguments",
                            type="FIELD",
                            content=AliasRule(
                                type="ALIAS",
                                value="token_tree",
                                named=True,
                                content=SymbolRule(
                                    type="SYMBOL",
                                    name="delim_token_tree",
                                ),
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

### 20) mod_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="mod"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=";"),
                FieldRule(
                    name="body",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="declaration_list"
                    ),
                ),
            ],
        ),
    ],
)
```

### 21) foreign_mod_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        SymbolRule(type="SYMBOL", name="extern_modifier"),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value=";"),
                FieldRule(
                    name="body",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="declaration_list"
                    ),
                ),
            ],
        ),
    ],
)
```

### 22) declaration_list

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="{"),
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(
                type="SYMBOL", name="_declaration_statement"
            ),
        ),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 23) struct_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="struct"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
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
                                    type="SYMBOL", name="where_clause"
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                        FieldRule(
                            name="body",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL",
                                name="field_declaration_list",
                            ),
                        ),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        FieldRule(
                            name="body",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL",
                                name="ordered_field_declaration_list",
                            ),
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="where_clause"
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                        StringRule(type="STRING", value=";"),
                    ],
                ),
                StringRule(type="STRING", value=";"),
            ],
        ),
    ],
)
```

### 24) union_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="union"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="field_declaration_list"
            ),
        ),
    ],
)
```

### 25) enum_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="enum"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="enum_variant_list"
            ),
        ),
    ],
)
```

### 26) enum_variant_list

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
                                RepeatRule(
                                    type="REPEAT",
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="attribute_item",
                                    ),
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="enum_variant"
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
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            RepeatRule(
                                                type="REPEAT",
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="attribute_item",
                                                ),
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="enum_variant",
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

### 27) enum_variant

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            SymbolRule(
                                type="SYMBOL",
                                name="field_declaration_list",
                            ),
                            SymbolRule(
                                type="SYMBOL",
                                name="ordered_field_declaration_list",
                            ),
                        ],
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="="),
                        FieldRule(
                            name="value",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_expression"
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

### 28) field_declaration_list

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
                                RepeatRule(
                                    type="REPEAT",
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="attribute_item",
                                    ),
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="field_declaration",
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
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            RepeatRule(
                                                type="REPEAT",
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="attribute_item",
                                                ),
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="field_declaration",
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

### 29) field_declaration

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_field_identifier"
            ),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 30) ordered_field_declaration_list

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
                                RepeatRule(
                                    type="REPEAT",
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="attribute_item",
                                    ),
                                ),
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="visibility_modifier",
                                        ),
                                        BlankRule(type="BLANK"),
                                    ],
                                ),
                                FieldRule(
                                    name="type",
                                    type="FIELD",
                                    content=SymbolRule(
                                        type="SYMBOL", name="_type"
                                    ),
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
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            RepeatRule(
                                                type="REPEAT",
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="attribute_item",
                                                ),
                                            ),
                                            ChoiceRule(
                                                type="CHOICE",
                                                members=[
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="visibility_modifier",
                                                    ),
                                                    BlankRule(
                                                        type="BLANK"
                                                    ),
                                                ],
                                            ),
                                            FieldRule(
                                                name="type",
                                                type="FIELD",
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="_type",
                                                ),
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

### 31) extern_crate_declaration

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="extern"),
        SymbolRule(type="SYMBOL", name="crate"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="as"),
                        FieldRule(
                            name="alias",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="identifier"
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 32) const_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="const"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="="),
                        FieldRule(
                            name="value",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_expression"
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 33) static_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="static"),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="ref"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="="),
                        FieldRule(
                            name="value",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_expression"
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 34) type_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="type"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        StringRule(type="STRING", value="="),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 35) function_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="function_modifiers"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="fn"),
        FieldRule(
            name="name",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(type="SYMBOL", name="metavariable"),
                ],
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
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
                                type="SYMBOL", name="_type"
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
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="block"),
        ),
    ],
)
```

### 36) function_signature_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="function_modifiers"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="fn"),
        FieldRule(
            name="name",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(type="SYMBOL", name="metavariable"),
                ],
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
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
                                type="SYMBOL", name="_type"
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
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 37) function_modifiers

```py
Repeat1Rule(
    type="REPEAT1",
    content=ChoiceRule(
        type="CHOICE",
        members=[
            StringRule(type="STRING", value="async"),
            StringRule(type="STRING", value="default"),
            StringRule(type="STRING", value="const"),
            StringRule(type="STRING", value="unsafe"),
            SymbolRule(type="SYMBOL", name="extern_modifier"),
        ],
    ),
)
```

### 38) where_clause

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="where"),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="where_predicate"),
                    RepeatRule(
                        type="REPEAT",
                        content=SeqRule(
                            type="SEQ",
                            members=[
                                StringRule(type="STRING", value=","),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="where_predicate",
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
)
```

### 39) where_predicate

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="left",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="lifetime"),
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="scoped_type_identifier"
                    ),
                    SymbolRule(type="SYMBOL", name="generic_type"),
                    SymbolRule(type="SYMBOL", name="reference_type"),
                    SymbolRule(type="SYMBOL", name="pointer_type"),
                    SymbolRule(type="SYMBOL", name="tuple_type"),
                    SymbolRule(type="SYMBOL", name="array_type"),
                    SymbolRule(
                        type="SYMBOL",
                        name="higher_ranked_trait_bound",
                    ),
                    AliasRule(
                        type="ALIAS",
                        value="primitive_type",
                        named=True,
                        content=ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value="u8"),
                                StringRule(type="STRING", value="i8"),
                                StringRule(
                                    type="STRING", value="u16"
                                ),
                                StringRule(
                                    type="STRING", value="i16"
                                ),
                                StringRule(
                                    type="STRING", value="u32"
                                ),
                                StringRule(
                                    type="STRING", value="i32"
                                ),
                                StringRule(
                                    type="STRING", value="u64"
                                ),
                                StringRule(
                                    type="STRING", value="i64"
                                ),
                                StringRule(
                                    type="STRING", value="u128"
                                ),
                                StringRule(
                                    type="STRING", value="i128"
                                ),
                                StringRule(
                                    type="STRING", value="isize"
                                ),
                                StringRule(
                                    type="STRING", value="usize"
                                ),
                                StringRule(
                                    type="STRING", value="f32"
                                ),
                                StringRule(
                                    type="STRING", value="f64"
                                ),
                                StringRule(
                                    type="STRING", value="bool"
                                ),
                                StringRule(
                                    type="STRING", value="str"
                                ),
                                StringRule(
                                    type="STRING", value="char"
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),
        FieldRule(
            name="bounds",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="trait_bounds"),
        ),
    ],
)
```

### 40) impl_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="unsafe"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="impl"),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value="!"),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                        FieldRule(
                            name="trait",
                            type="FIELD",
                            content=ChoiceRule(
                                type="CHOICE",
                                members=[
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="_type_identifier",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="scoped_type_identifier",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="generic_type",
                                    ),
                                ],
                            ),
                        ),
                        StringRule(type="STRING", value="for"),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                FieldRule(
                    name="body",
                    type="FIELD",
                    content=SymbolRule(
                        type="SYMBOL", name="declaration_list"
                    ),
                ),
                StringRule(type="STRING", value=";"),
            ],
        ),
    ],
)
```

### 41) trait_item

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="unsafe"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="trait"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        FieldRule(
            name="bounds",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="trait_bounds"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="declaration_list"
            ),
        ),
    ],
)
```

### 42) associated_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="type"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_parameters"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        FieldRule(
            name="bounds",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="trait_bounds"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="where_clause"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 43) trait_bounds

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value=":"),
        SeqRule(
            type="SEQ",
            members=[
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(type="SYMBOL", name="_type"),
                        SymbolRule(type="SYMBOL", name="lifetime"),
                        SymbolRule(
                            type="SYMBOL",
                            name="higher_ranked_trait_bound",
                        ),
                    ],
                ),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value="+"),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    SymbolRule(
                                        type="SYMBOL", name="_type"
                                    ),
                                    SymbolRule(
                                        type="SYMBOL", name="lifetime"
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="higher_ranked_trait_bound",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ],
)
```

### 44) higher_ranked_trait_bound

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="for"),
        FieldRule(
            name="type_parameters",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="type_parameters"),
        ),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 45) removed_trait_bound

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="?"),
        SymbolRule(type="SYMBOL", name="_type"),
    ],
)
```

### 46) type_parameters

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="<"),
            SeqRule(
                type="SEQ",
                members=[
                    SeqRule(
                        type="SEQ",
                        members=[
                            RepeatRule(
                                type="REPEAT",
                                content=SymbolRule(
                                    type="SYMBOL",
                                    name="attribute_item",
                                ),
                            ),
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    SymbolRule(
                                        type="SYMBOL", name="lifetime"
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="metavariable",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="_type_identifier",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="constrained_type_parameter",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="optional_type_parameter",
                                    ),
                                    SymbolRule(
                                        type="SYMBOL",
                                        name="const_parameter",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    RepeatRule(
                        type="REPEAT",
                        content=SeqRule(
                            type="SEQ",
                            members=[
                                StringRule(type="STRING", value=","),
                                SeqRule(
                                    type="SEQ",
                                    members=[
                                        RepeatRule(
                                            type="REPEAT",
                                            content=SymbolRule(
                                                type="SYMBOL",
                                                name="attribute_item",
                                            ),
                                        ),
                                        ChoiceRule(
                                            type="CHOICE",
                                            members=[
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="lifetime",
                                                ),
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="metavariable",
                                                ),
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="_type_identifier",
                                                ),
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="constrained_type_parameter",
                                                ),
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="optional_type_parameter",
                                                ),
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="const_parameter",
                                                ),
                                            ],
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
            StringRule(type="STRING", value=">"),
        ],
    ),
)
```

### 47) const_parameter

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="const"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 48) constrained_type_parameter

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="left",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="lifetime"),
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                ],
            ),
        ),
        FieldRule(
            name="bounds",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="trait_bounds"),
        ),
    ],
)
```

### 49) optional_type_parameter

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
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                    SymbolRule(
                        type="SYMBOL",
                        name="constrained_type_parameter",
                    ),
                ],
            ),
        ),
        StringRule(type="STRING", value="="),
        FieldRule(
            name="default_type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 50) let_declaration

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="let"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="pattern",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_pattern"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value=":"),
                        FieldRule(
                            name="type",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_type"
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
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="="),
                        FieldRule(
                            name="value",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_expression"
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
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="else"),
                        FieldRule(
                            name="alternative",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="block"
                            ),
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 51) use_declaration

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="visibility_modifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="use"),
        FieldRule(
            name="argument",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_use_clause"),
        ),
        StringRule(type="STRING", value=";"),
    ],
)
```

### 52) _use_clause

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_path"),
        SymbolRule(type="SYMBOL", name="use_as_clause"),
        SymbolRule(type="SYMBOL", name="use_list"),
        SymbolRule(type="SYMBOL", name="scoped_use_list"),
        SymbolRule(type="SYMBOL", name="use_wildcard"),
    ],
)
```

### 53) scoped_use_list

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="path",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="_path"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        StringRule(type="STRING", value="::"),
        FieldRule(
            name="list",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="use_list"),
        ),
    ],
)
```

### 54) use_list

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
                                    type="SYMBOL", name="_use_clause"
                                )
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
                                                name="_use_clause",
                                            )
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

### 55) use_as_clause

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="path",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_path"),
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

### 56) use_wildcard

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="_path"),
                        StringRule(type="STRING", value="::"),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="*"),
    ],
)
```

### 57) parameters

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
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="attribute_item",
                                        ),
                                        BlankRule(type="BLANK"),
                                    ],
                                ),
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="parameter",
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="self_parameter",
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="variadic_parameter",
                                        ),
                                        StringRule(
                                            type="STRING", value="_"
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="_type",
                                        ),
                                    ],
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
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            ChoiceRule(
                                                type="CHOICE",
                                                members=[
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="attribute_item",
                                                    ),
                                                    BlankRule(
                                                        type="BLANK"
                                                    ),
                                                ],
                                            ),
                                            ChoiceRule(
                                                type="CHOICE",
                                                members=[
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="parameter",
                                                    ),
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="self_parameter",
                                                    ),
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="variadic_parameter",
                                                    ),
                                                    StringRule(
                                                        type="STRING",
                                                        value="_",
                                                    ),
                                                    SymbolRule(
                                                        type="SYMBOL",
                                                        name="_type",
                                                    ),
                                                ],
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

### 58) self_parameter

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="&"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="lifetime"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        SymbolRule(type="SYMBOL", name="self"),
    ],
)
```

### 59) variadic_parameter

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        FieldRule(
                            name="pattern",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_pattern"
                            ),
                        ),
                        StringRule(type="STRING", value=":"),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="..."),
    ],
)
```

### 60) parameter

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="pattern",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="_pattern"),
                    SymbolRule(type="SYMBOL", name="self"),
                ],
            ),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 61) extern_modifier

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="extern"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="string_literal"),
                BlankRule(type="BLANK"),
            ],
        ),
    ],
)
```

### 62) visibility_modifier

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="crate"),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="pub"),
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                StringRule(type="STRING", value="("),
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL", name="self"
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="super",
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="crate",
                                        ),
                                        SeqRule(
                                            type="SEQ",
                                            members=[
                                                StringRule(
                                                    type="STRING",
                                                    value="in",
                                                ),
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="_path",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                StringRule(type="STRING", value=")"),
                            ],
                        ),
                        BlankRule(type="BLANK"),
                    ],
                ),
            ],
        ),
    ],
)
```

### 63) _type

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="abstract_type"),
        SymbolRule(type="SYMBOL", name="reference_type"),
        SymbolRule(type="SYMBOL", name="metavariable"),
        SymbolRule(type="SYMBOL", name="pointer_type"),
        SymbolRule(type="SYMBOL", name="generic_type"),
        SymbolRule(type="SYMBOL", name="scoped_type_identifier"),
        SymbolRule(type="SYMBOL", name="tuple_type"),
        SymbolRule(type="SYMBOL", name="unit_type"),
        SymbolRule(type="SYMBOL", name="array_type"),
        SymbolRule(type="SYMBOL", name="function_type"),
        SymbolRule(type="SYMBOL", name="_type_identifier"),
        SymbolRule(type="SYMBOL", name="macro_invocation"),
        SymbolRule(type="SYMBOL", name="never_type"),
        SymbolRule(type="SYMBOL", name="dynamic_type"),
        SymbolRule(type="SYMBOL", name="bounded_type"),
        SymbolRule(type="SYMBOL", name="removed_trait_bound"),
        AliasRule(
            type="ALIAS",
            value="primitive_type",
            named=True,
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="u8"),
                    StringRule(type="STRING", value="i8"),
                    StringRule(type="STRING", value="u16"),
                    StringRule(type="STRING", value="i16"),
                    StringRule(type="STRING", value="u32"),
                    StringRule(type="STRING", value="i32"),
                    StringRule(type="STRING", value="u64"),
                    StringRule(type="STRING", value="i64"),
                    StringRule(type="STRING", value="u128"),
                    StringRule(type="STRING", value="i128"),
                    StringRule(type="STRING", value="isize"),
                    StringRule(type="STRING", value="usize"),
                    StringRule(type="STRING", value="f32"),
                    StringRule(type="STRING", value="f64"),
                    StringRule(type="STRING", value="bool"),
                    StringRule(type="STRING", value="str"),
                    StringRule(type="STRING", value="char"),
                ],
            ),
        ),
    ],
)
```

### 64) bracketed_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="<"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_type"),
                SymbolRule(type="SYMBOL", name="qualified_type"),
            ],
        ),
        StringRule(type="STRING", value=">"),
    ],
)
```

### 65) qualified_type

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
        StringRule(type="STRING", value="as"),
        FieldRule(
            name="alias",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 66) lifetime

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="'"),
            SymbolRule(type="SYMBOL", name="identifier"),
        ],
    ),
)
```

### 67) array_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="["),
        FieldRule(
            name="element",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value=";"),
                        FieldRule(
                            name="length",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_expression"
                            ),
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

### 68) for_lifetimes

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="for"),
        StringRule(type="STRING", value="<"),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="lifetime"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(
                                type="SYMBOL", name="lifetime"
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
        StringRule(type="STRING", value=">"),
    ],
)
```

### 69) function_type

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="for_lifetimes"),
                BlankRule(type="BLANK"),
            ],
        ),
        PrecRule(
            type="PREC",
            value=15,
            content=SeqRule(
                type="SEQ",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            FieldRule(
                                name="trait",
                                type="FIELD",
                                content=ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="_type_identifier",
                                        ),
                                        SymbolRule(
                                            type="SYMBOL",
                                            name="scoped_type_identifier",
                                        ),
                                    ],
                                ),
                            ),
                            SeqRule(
                                type="SEQ",
                                members=[
                                    ChoiceRule(
                                        type="CHOICE",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="function_modifiers",
                                            ),
                                            BlankRule(type="BLANK"),
                                        ],
                                    ),
                                    StringRule(
                                        type="STRING", value="fn"
                                    ),
                                ],
                            ),
                        ],
                    ),
                    FieldRule(
                        name="parameters",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="parameters"
                        ),
                    ),
                ],
            ),
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
                                type="SYMBOL", name="_type"
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

### 70) tuple_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="_type"),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SymbolRule(type="SYMBOL", name="_type"),
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
)
```

### 71) unit_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 72) generic_function

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="function",
                type="FIELD",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(type="SYMBOL", name="identifier"),
                        SymbolRule(
                            type="SYMBOL", name="scoped_identifier"
                        ),
                        SymbolRule(
                            type="SYMBOL", name="field_expression"
                        ),
                    ],
                ),
            ),
            StringRule(type="STRING", value="::"),
            FieldRule(
                name="type_arguments",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="type_arguments"
                ),
            ),
        ],
    ),
)
```

### 73) generic_type

```py
PrecRule(
    type="PREC",
    value=1,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="type",
                type="FIELD",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(
                            type="SYMBOL", name="_type_identifier"
                        ),
                        SymbolRule(
                            type="SYMBOL", name="_reserved_identifier"
                        ),
                        SymbolRule(
                            type="SYMBOL",
                            name="scoped_type_identifier",
                        ),
                    ],
                ),
            ),
            FieldRule(
                name="type_arguments",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="type_arguments"
                ),
            ),
        ],
    ),
)
```

### 74) generic_type_with_turbofish

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="type",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="scoped_identifier"
                    ),
                ],
            ),
        ),
        StringRule(type="STRING", value="::"),
        FieldRule(
            name="type_arguments",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="type_arguments"),
        ),
    ],
)
```

### 75) bounded_type

```py
PrecRule(
    type="PREC_LEFT",
    value=-1,
    content=ChoiceRule(
        type="CHOICE",
        members=[
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="lifetime"),
                    StringRule(type="STRING", value="+"),
                    SymbolRule(type="SYMBOL", name="_type"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_type"),
                    StringRule(type="STRING", value="+"),
                    SymbolRule(type="SYMBOL", name="_type"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_type"),
                    StringRule(type="STRING", value="+"),
                    SymbolRule(type="SYMBOL", name="lifetime"),
                ],
            ),
        ],
    ),
)
```

### 76) type_arguments

```py
SeqRule(
    type="SEQ",
    members=[
        TokenRule(
            type="TOKEN",
            content=PrecRule(
                type="PREC",
                value=1,
                content=StringRule(type="STRING", value="<"),
            ),
        ),
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
                                    type="SYMBOL", name="_type"
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="type_binding"
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="lifetime"
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="_literal"
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="block"
                                ),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="trait_bounds"
                                ),
                                BlankRule(type="BLANK"),
                            ],
                        ),
                    ],
                ),
                RepeatRule(
                    type="REPEAT",
                    content=SeqRule(
                        type="SEQ",
                        members=[
                            StringRule(type="STRING", value=","),
                            SeqRule(
                                type="SEQ",
                                members=[
                                    ChoiceRule(
                                        type="CHOICE",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="_type",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="type_binding",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="lifetime",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="_literal",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="block",
                                            ),
                                        ],
                                    ),
                                    ChoiceRule(
                                        type="CHOICE",
                                        members=[
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="trait_bounds",
                                            ),
                                            BlankRule(type="BLANK"),
                                        ],
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
        StringRule(type="STRING", value=">"),
    ],
)
```

### 77) type_binding

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
        FieldRule(
            name="type_arguments",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="type_arguments"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        StringRule(type="STRING", value="="),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 78) reference_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="&"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="lifetime"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 79) pointer_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="*"),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="const"),
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
            ],
        ),
        FieldRule(
            name="type",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_type"),
        ),
    ],
)
```

### 80) never_type

```py
StringRule(type="STRING", value="!")
```

### 81) abstract_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="impl"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="for"),
                        SymbolRule(
                            type="SYMBOL", name="type_parameters"
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        FieldRule(
            name="trait",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="scoped_type_identifier"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="removed_trait_bound"
                    ),
                    SymbolRule(type="SYMBOL", name="generic_type"),
                    SymbolRule(type="SYMBOL", name="function_type"),
                    SymbolRule(type="SYMBOL", name="tuple_type"),
                ],
            ),
        ),
    ],
)
```

### 82) dynamic_type

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="dyn"),
        FieldRule(
            name="trait",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL",
                        name="higher_ranked_trait_bound",
                    ),
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="scoped_type_identifier"
                    ),
                    SymbolRule(type="SYMBOL", name="generic_type"),
                    SymbolRule(type="SYMBOL", name="function_type"),
                ],
            ),
        ),
    ],
)
```

### 83) mutable_specifier

```py
StringRule(type="STRING", value="mut")
```

### 84) _expression_except_range

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="unary_expression"),
        SymbolRule(type="SYMBOL", name="reference_expression"),
        SymbolRule(type="SYMBOL", name="try_expression"),
        SymbolRule(type="SYMBOL", name="binary_expression"),
        SymbolRule(type="SYMBOL", name="assignment_expression"),
        SymbolRule(type="SYMBOL", name="compound_assignment_expr"),
        SymbolRule(type="SYMBOL", name="type_cast_expression"),
        SymbolRule(type="SYMBOL", name="call_expression"),
        SymbolRule(type="SYMBOL", name="return_expression"),
        SymbolRule(type="SYMBOL", name="yield_expression"),
        SymbolRule(type="SYMBOL", name="_literal"),
        PrecRule(
            type="PREC_LEFT",
            value=0,
            content=SymbolRule(type="SYMBOL", name="identifier"),
        ),
        AliasRule(
            type="ALIAS",
            value="identifier",
            named=True,
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="u8"),
                    StringRule(type="STRING", value="i8"),
                    StringRule(type="STRING", value="u16"),
                    StringRule(type="STRING", value="i16"),
                    StringRule(type="STRING", value="u32"),
                    StringRule(type="STRING", value="i32"),
                    StringRule(type="STRING", value="u64"),
                    StringRule(type="STRING", value="i64"),
                    StringRule(type="STRING", value="u128"),
                    StringRule(type="STRING", value="i128"),
                    StringRule(type="STRING", value="isize"),
                    StringRule(type="STRING", value="usize"),
                    StringRule(type="STRING", value="f32"),
                    StringRule(type="STRING", value="f64"),
                    StringRule(type="STRING", value="bool"),
                    StringRule(type="STRING", value="str"),
                    StringRule(type="STRING", value="char"),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=0,
            content=SymbolRule(
                type="SYMBOL", name="_reserved_identifier"
            ),
        ),
        SymbolRule(type="SYMBOL", name="self"),
        SymbolRule(type="SYMBOL", name="scoped_identifier"),
        SymbolRule(type="SYMBOL", name="generic_function"),
        SymbolRule(type="SYMBOL", name="await_expression"),
        SymbolRule(type="SYMBOL", name="field_expression"),
        SymbolRule(type="SYMBOL", name="array_expression"),
        SymbolRule(type="SYMBOL", name="tuple_expression"),
        PrecRule(
            type="PREC",
            value=1,
            content=SymbolRule(
                type="SYMBOL", name="macro_invocation"
            ),
        ),
        SymbolRule(type="SYMBOL", name="unit_expression"),
        SymbolRule(type="SYMBOL", name="break_expression"),
        SymbolRule(type="SYMBOL", name="continue_expression"),
        SymbolRule(type="SYMBOL", name="index_expression"),
        SymbolRule(type="SYMBOL", name="metavariable"),
        SymbolRule(type="SYMBOL", name="closure_expression"),
        SymbolRule(type="SYMBOL", name="parenthesized_expression"),
        SymbolRule(type="SYMBOL", name="struct_expression"),
        SymbolRule(
            type="SYMBOL", name="_expression_ending_with_block"
        ),
    ],
)
```

### 85) _expression

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_expression_except_range"),
        SymbolRule(type="SYMBOL", name="range_expression"),
    ],
)
```

### 86) _expression_ending_with_block

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="unsafe_block"),
        SymbolRule(type="SYMBOL", name="async_block"),
        SymbolRule(type="SYMBOL", name="try_block"),
        SymbolRule(type="SYMBOL", name="block"),
        SymbolRule(type="SYMBOL", name="if_expression"),
        SymbolRule(type="SYMBOL", name="match_expression"),
        SymbolRule(type="SYMBOL", name="while_expression"),
        SymbolRule(type="SYMBOL", name="loop_expression"),
        SymbolRule(type="SYMBOL", name="for_expression"),
        SymbolRule(type="SYMBOL", name="const_block"),
    ],
)
```

### 87) macro_invocation

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="macro",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="scoped_identifier"
                    ),
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(
                        type="SYMBOL", name="_reserved_identifier"
                    ),
                ],
            ),
        ),
        StringRule(type="STRING", value="!"),
        AliasRule(
            type="ALIAS",
            value="token_tree",
            named=True,
            content=SymbolRule(
                type="SYMBOL", name="delim_token_tree"
            ),
        ),
    ],
)
```

### 88) delim_token_tree

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="("),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(
                        type="SYMBOL", name="_delim_tokens"
                    ),
                ),
                StringRule(type="STRING", value=")"),
            ],
        ),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="["),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(
                        type="SYMBOL", name="_delim_tokens"
                    ),
                ),
                StringRule(type="STRING", value="]"),
            ],
        ),
        SeqRule(
            type="SEQ",
            members=[
                StringRule(type="STRING", value="{"),
                RepeatRule(
                    type="REPEAT",
                    content=SymbolRule(
                        type="SYMBOL", name="_delim_tokens"
                    ),
                ),
                StringRule(type="STRING", value="}"),
            ],
        ),
    ],
)
```

### 89) _delim_tokens

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_non_delim_token"),
        AliasRule(
            type="ALIAS",
            value="token_tree",
            named=True,
            content=SymbolRule(
                type="SYMBOL", name="delim_token_tree"
            ),
        ),
    ],
)
```

### 90) _non_delim_token

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_non_special_token"),
        StringRule(type="STRING", value="$"),
    ],
)
```

### 91) scoped_identifier

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="path",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            SymbolRule(type="SYMBOL", name="_path"),
                            SymbolRule(
                                type="SYMBOL", name="bracketed_type"
                            ),
                            AliasRule(
                                type="ALIAS",
                                value="generic_type",
                                named=True,
                                content=SymbolRule(
                                    type="SYMBOL",
                                    name="generic_type_with_turbofish",
                                ),
                            ),
                        ],
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        StringRule(type="STRING", value="::"),
        FieldRule(
            name="name",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(type="SYMBOL", name="super"),
                ],
            ),
        ),
    ],
)
```

### 92) scoped_type_identifier_in_expression_position

```py
PrecRule(
    type="PREC",
    value=-2,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="path",
                type="FIELD",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="_path"
                                ),
                                AliasRule(
                                    type="ALIAS",
                                    value="generic_type",
                                    named=True,
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="generic_type_with_turbofish",
                                    ),
                                ),
                            ],
                        ),
                        BlankRule(type="BLANK"),
                    ],
                ),
            ),
            StringRule(type="STRING", value="::"),
            FieldRule(
                name="name",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="_type_identifier"
                ),
            ),
        ],
    ),
)
```

### 93) scoped_type_identifier

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="path",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            SymbolRule(type="SYMBOL", name="_path"),
                            AliasRule(
                                type="ALIAS",
                                value="generic_type",
                                named=True,
                                content=SymbolRule(
                                    type="SYMBOL",
                                    name="generic_type_with_turbofish",
                                ),
                            ),
                            SymbolRule(
                                type="SYMBOL", name="bracketed_type"
                            ),
                            SymbolRule(
                                type="SYMBOL", name="generic_type"
                            ),
                        ],
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
        ),
        StringRule(type="STRING", value="::"),
        FieldRule(
            name="name",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="_type_identifier"
            ),
        ),
    ],
)
```

### 94) range_expression

```py
PrecRule(
    type="PREC_LEFT",
    value=1,
    content=ChoiceRule(
        type="CHOICE",
        members=[
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_expression"),
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            StringRule(type="STRING", value=".."),
                            StringRule(type="STRING", value="..."),
                            StringRule(type="STRING", value="..="),
                        ],
                    ),
                    SymbolRule(type="SYMBOL", name="_expression"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_expression"),
                    StringRule(type="STRING", value=".."),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    StringRule(type="STRING", value=".."),
                    SymbolRule(type="SYMBOL", name="_expression"),
                ],
            ),
            StringRule(type="STRING", value=".."),
        ],
    ),
)
```

### 95) unary_expression

```py
PrecRule(
    type="PREC",
    value=12,
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="-"),
                    StringRule(type="STRING", value="*"),
                    StringRule(type="STRING", value="!"),
                ],
            ),
            SymbolRule(type="SYMBOL", name="_expression"),
        ],
    ),
)
```

### 96) try_expression

```py
PrecRule(
    type="PREC",
    value=13,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="_expression"),
            StringRule(type="STRING", value="?"),
        ],
    ),
)
```

### 97) reference_expression

```py
PrecRule(
    type="PREC",
    value=12,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="&"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="mutable_specifier"
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
            FieldRule(
                name="value",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_expression"),
            ),
        ],
    ),
)
```

### 98) binary_expression

```py
ChoiceRule(
    type="CHOICE",
    members=[
        PrecRule(
            type="PREC_LEFT",
            value=3,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="&&"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=2,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=StringRule(type="STRING", value="||"),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=7,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
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
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=5,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
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
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=6,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
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
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=4,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value="=="),
                                StringRule(type="STRING", value="!="),
                                StringRule(type="STRING", value="<"),
                                StringRule(type="STRING", value="<="),
                                StringRule(type="STRING", value=">"),
                                StringRule(type="STRING", value=">="),
                            ],
                        ),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=8,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value="<<"),
                                StringRule(type="STRING", value=">>"),
                            ],
                        ),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
        PrecRule(
            type="PREC_LEFT",
            value=9,
            content=SeqRule(
                type="SEQ",
                members=[
                    FieldRule(
                        name="left",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value="+"),
                                StringRule(type="STRING", value="-"),
                            ],
                        ),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
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
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                    FieldRule(
                        name="operator",
                        type="FIELD",
                        content=ChoiceRule(
                            type="CHOICE",
                            members=[
                                StringRule(type="STRING", value="*"),
                                StringRule(type="STRING", value="/"),
                                StringRule(type="STRING", value="%"),
                            ],
                        ),
                    ),
                    FieldRule(
                        name="right",
                        type="FIELD",
                        content=SymbolRule(
                            type="SYMBOL", name="_expression"
                        ),
                    ),
                ],
            ),
        ),
    ],
)
```

### 99) assignment_expression

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="left",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_expression"),
            ),
            StringRule(type="STRING", value="="),
            FieldRule(
                name="right",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_expression"),
            ),
        ],
    ),
)
```

### 100) compound_assignment_expr

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="left",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_expression"),
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
                        StringRule(type="STRING", value="%="),
                        StringRule(type="STRING", value="&="),
                        StringRule(type="STRING", value="|="),
                        StringRule(type="STRING", value="^="),
                        StringRule(type="STRING", value="<<="),
                        StringRule(type="STRING", value=">>="),
                    ],
                ),
            ),
            FieldRule(
                name="right",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_expression"),
            ),
        ],
    ),
)
```

### 101) type_cast_expression

```py
PrecRule(
    type="PREC_LEFT",
    value=11,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="value",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_expression"),
            ),
            StringRule(type="STRING", value="as"),
            FieldRule(
                name="type",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_type"),
            ),
        ],
    ),
)
```

### 102) return_expression

```py
ChoiceRule(
    type="CHOICE",
    members=[
        PrecRule(
            type="PREC_LEFT",
            value=0,
            content=SeqRule(
                type="SEQ",
                members=[
                    StringRule(type="STRING", value="return"),
                    SymbolRule(type="SYMBOL", name="_expression"),
                ],
            ),
        ),
        PrecRule(
            type="PREC",
            value=-1,
            content=StringRule(type="STRING", value="return"),
        ),
    ],
)
```

### 103) yield_expression

```py
ChoiceRule(
    type="CHOICE",
    members=[
        PrecRule(
            type="PREC_LEFT",
            value=0,
            content=SeqRule(
                type="SEQ",
                members=[
                    StringRule(type="STRING", value="yield"),
                    SymbolRule(type="SYMBOL", name="_expression"),
                ],
            ),
        ),
        PrecRule(
            type="PREC",
            value=-1,
            content=StringRule(type="STRING", value="yield"),
        ),
    ],
)
```

### 104) call_expression

```py
PrecRule(
    type="PREC",
    value=15,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="function",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="_expression_except_range"
                ),
            ),
            FieldRule(
                name="arguments",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="arguments"),
            ),
        ],
    ),
)
```

### 105) arguments

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
                                RepeatRule(
                                    type="REPEAT",
                                    content=SymbolRule(
                                        type="SYMBOL",
                                        name="attribute_item",
                                    ),
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="_expression"
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
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            RepeatRule(
                                                type="REPEAT",
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="attribute_item",
                                                ),
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="_expression",
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

### 106) array_expression

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="["),
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="attribute_item"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="_expression"),
                        StringRule(type="STRING", value=";"),
                        FieldRule(
                            name="length",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_expression"
                            ),
                        ),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SeqRule(
                                    type="SEQ",
                                    members=[
                                        SeqRule(
                                            type="SEQ",
                                            members=[
                                                RepeatRule(
                                                    type="REPEAT",
                                                    content=SymbolRule(
                                                        type="SYMBOL",
                                                        name="attribute_item",
                                                    ),
                                                ),
                                                SymbolRule(
                                                    type="SYMBOL",
                                                    name="_expression",
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
                                                    SeqRule(
                                                        type="SEQ",
                                                        members=[
                                                            RepeatRule(
                                                                type="REPEAT",
                                                                content=SymbolRule(
                                                                    type="SYMBOL",
                                                                    name="attribute_item",
                                                                ),
                                                            ),
                                                            SymbolRule(
                                                                type="SYMBOL",
                                                                name="_expression",
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
                    ],
                ),
            ],
        ),
        StringRule(type="STRING", value="]"),
    ],
)
```

### 107) parenthesized_expression

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        SymbolRule(type="SYMBOL", name="_expression"),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 108) tuple_expression

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="attribute_item"),
        ),
        SeqRule(
            type="SEQ",
            members=[
                SymbolRule(type="SYMBOL", name="_expression"),
                StringRule(type="STRING", value=","),
            ],
        ),
        RepeatRule(
            type="REPEAT",
            content=SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_expression"),
                    StringRule(type="STRING", value=","),
                ],
            ),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_expression"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 109) unit_expression

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="("),
        StringRule(type="STRING", value=")"),
    ],
)
```

### 110) struct_expression

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
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                    AliasRule(
                        type="ALIAS",
                        value="scoped_type_identifier",
                        named=True,
                        content=SymbolRule(
                            type="SYMBOL",
                            name="scoped_type_identifier_in_expression_position",
                        ),
                    ),
                    SymbolRule(
                        type="SYMBOL",
                        name="generic_type_with_turbofish",
                    ),
                ],
            ),
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(
                type="SYMBOL", name="field_initializer_list"
            ),
        ),
    ],
)
```

### 111) field_initializer_list

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
                                    type="SYMBOL",
                                    name="shorthand_field_initializer",
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="field_initializer",
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="base_field_initializer",
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
                                                name="shorthand_field_initializer",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="field_initializer",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="base_field_initializer",
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

### 112) shorthand_field_initializer

```py
SeqRule(
    type="SEQ",
    members=[
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="attribute_item"),
        ),
        SymbolRule(type="SYMBOL", name="identifier"),
    ],
)
```

### 113) field_initializer

```py
SeqRule(
    type="SEQ",
    members=[
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="attribute_item"),
        ),
        FieldRule(
            name="field",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="_field_identifier"
                    ),
                    SymbolRule(type="SYMBOL", name="integer_literal"),
                ],
            ),
        ),
        StringRule(type="STRING", value=":"),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_expression"),
        ),
    ],
)
```

### 114) base_field_initializer

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value=".."),
        SymbolRule(type="SYMBOL", name="_expression"),
    ],
)
```

### 115) if_expression

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="if"),
            FieldRule(
                name="condition",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_condition"),
            ),
            FieldRule(
                name="consequence",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="block"),
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
    ),
)
```

### 116) let_condition

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="let"),
        FieldRule(
            name="pattern",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_pattern"),
        ),
        StringRule(type="STRING", value="="),
        FieldRule(
            name="value",
            type="FIELD",
            content=PrecRule(
                type="PREC_LEFT",
                value=3,
                content=SymbolRule(type="SYMBOL", name="_expression"),
            ),
        ),
    ],
)
```

### 117) _let_chain

```py
PrecRule(
    type="PREC_LEFT",
    value=3,
    content=ChoiceRule(
        type="CHOICE",
        members=[
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_let_chain"),
                    StringRule(type="STRING", value="&&"),
                    SymbolRule(type="SYMBOL", name="let_condition"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_let_chain"),
                    StringRule(type="STRING", value="&&"),
                    SymbolRule(type="SYMBOL", name="_expression"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="let_condition"),
                    StringRule(type="STRING", value="&&"),
                    SymbolRule(type="SYMBOL", name="_expression"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="let_condition"),
                    StringRule(type="STRING", value="&&"),
                    SymbolRule(type="SYMBOL", name="let_condition"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_expression"),
                    StringRule(type="STRING", value="&&"),
                    SymbolRule(type="SYMBOL", name="let_condition"),
                ],
            ),
        ],
    ),
)
```

### 118) _condition

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_expression"),
        SymbolRule(type="SYMBOL", name="let_condition"),
        AliasRule(
            type="ALIAS",
            value="let_chain",
            named=True,
            content=SymbolRule(type="SYMBOL", name="_let_chain"),
        ),
    ],
)
```

### 119) else_clause

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="else"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="block"),
                SymbolRule(type="SYMBOL", name="if_expression"),
            ],
        ),
    ],
)
```

### 120) match_expression

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="match"),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_expression"),
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="match_block"),
        ),
    ],
)
```

### 121) match_block

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
                        RepeatRule(
                            type="REPEAT",
                            content=SymbolRule(
                                type="SYMBOL", name="match_arm"
                            ),
                        ),
                        AliasRule(
                            type="ALIAS",
                            value="match_arm",
                            named=True,
                            content=SymbolRule(
                                type="SYMBOL", name="last_match_arm"
                            ),
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

### 122) match_arm

```py
PrecRule(
    type="PREC_RIGHT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            RepeatRule(
                type="REPEAT",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(
                            type="SYMBOL", name="attribute_item"
                        ),
                        SymbolRule(
                            type="SYMBOL", name="inner_attribute_item"
                        ),
                    ],
                ),
            ),
            FieldRule(
                name="pattern",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="match_pattern"
                ),
            ),
            StringRule(type="STRING", value="=>"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SeqRule(
                        type="SEQ",
                        members=[
                            FieldRule(
                                name="value",
                                type="FIELD",
                                content=SymbolRule(
                                    type="SYMBOL", name="_expression"
                                ),
                            ),
                            StringRule(type="STRING", value=","),
                        ],
                    ),
                    FieldRule(
                        name="value",
                        type="FIELD",
                        content=PrecRule(
                            type="PREC",
                            value=1,
                            content=SymbolRule(
                                type="SYMBOL",
                                name="_expression_ending_with_block",
                            ),
                        ),
                    ),
                ],
            ),
        ],
    ),
)
```

### 123) last_match_arm

```py
SeqRule(
    type="SEQ",
    members=[
        RepeatRule(
            type="REPEAT",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="attribute_item"),
                    SymbolRule(
                        type="SYMBOL", name="inner_attribute_item"
                    ),
                ],
            ),
        ),
        FieldRule(
            name="pattern",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="match_pattern"),
        ),
        StringRule(type="STRING", value="=>"),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_expression"),
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

### 124) match_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="_pattern"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        StringRule(type="STRING", value="if"),
                        FieldRule(
                            name="condition",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_condition"
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

### 125) while_expression

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="label"),
                        StringRule(type="STRING", value=":"),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="while"),
        FieldRule(
            name="condition",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_condition"),
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="block"),
        ),
    ],
)
```

### 126) loop_expression

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="label"),
                        StringRule(type="STRING", value=":"),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="loop"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="block"),
        ),
    ],
)
```

### 127) for_expression

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="label"),
                        StringRule(type="STRING", value=":"),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="for"),
        FieldRule(
            name="pattern",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_pattern"),
        ),
        StringRule(type="STRING", value="in"),
        FieldRule(
            name="value",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="_expression"),
        ),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="block"),
        ),
    ],
)
```

### 128) const_block

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="const"),
        FieldRule(
            name="body",
            type="FIELD",
            content=SymbolRule(type="SYMBOL", name="block"),
        ),
    ],
)
```

### 129) closure_expression

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
                    StringRule(type="STRING", value="static"),
                    BlankRule(type="BLANK"),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="move"),
                    BlankRule(type="BLANK"),
                ],
            ),
            FieldRule(
                name="parameters",
                type="FIELD",
                content=SymbolRule(
                    type="SYMBOL", name="closure_parameters"
                ),
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SeqRule(
                        type="SEQ",
                        members=[
                            ChoiceRule(
                                type="CHOICE",
                                members=[
                                    SeqRule(
                                        type="SEQ",
                                        members=[
                                            StringRule(
                                                type="STRING",
                                                value="->",
                                            ),
                                            FieldRule(
                                                name="return_type",
                                                type="FIELD",
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="_type",
                                                ),
                                            ),
                                        ],
                                    ),
                                    BlankRule(type="BLANK"),
                                ],
                            ),
                            FieldRule(
                                name="body",
                                type="FIELD",
                                content=SymbolRule(
                                    type="SYMBOL", name="block"
                                ),
                            ),
                        ],
                    ),
                    FieldRule(
                        name="body",
                        type="FIELD",
                        content=ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL", name="_expression"
                                ),
                                StringRule(type="STRING", value="_"),
                            ],
                        ),
                    ),
                ],
            ),
        ],
    ),
)
```

### 130) closure_parameters

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="|"),
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
                                    type="SYMBOL", name="_pattern"
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="parameter"
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
                                                name="_pattern",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="parameter",
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
        StringRule(type="STRING", value="|"),
    ],
)
```

### 131) label

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="'"),
        SymbolRule(type="SYMBOL", name="identifier"),
    ],
)
```

### 132) break_expression

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="break"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="label"),
                    BlankRule(type="BLANK"),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="_expression"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ],
    ),
)
```

### 133) continue_expression

```py
PrecRule(
    type="PREC_LEFT",
    value=0,
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="continue"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="label"),
                    BlankRule(type="BLANK"),
                ],
            ),
        ],
    ),
)
```

### 134) index_expression

```py
PrecRule(
    type="PREC",
    value=15,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="_expression"),
            StringRule(type="STRING", value="["),
            SymbolRule(type="SYMBOL", name="_expression"),
            StringRule(type="STRING", value="]"),
        ],
    ),
)
```

### 135) await_expression

```py
PrecRule(
    type="PREC",
    value=14,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="_expression"),
            StringRule(type="STRING", value="."),
            StringRule(type="STRING", value="await"),
        ],
    ),
)
```

### 136) field_expression

```py
PrecRule(
    type="PREC",
    value=14,
    content=SeqRule(
        type="SEQ",
        members=[
            FieldRule(
                name="value",
                type="FIELD",
                content=SymbolRule(type="SYMBOL", name="_expression"),
            ),
            StringRule(type="STRING", value="."),
            FieldRule(
                name="field",
                type="FIELD",
                content=ChoiceRule(
                    type="CHOICE",
                    members=[
                        SymbolRule(
                            type="SYMBOL", name="_field_identifier"
                        ),
                        SymbolRule(
                            type="SYMBOL", name="integer_literal"
                        ),
                    ],
                ),
            ),
        ],
    ),
)
```

### 137) unsafe_block

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="unsafe"),
        SymbolRule(type="SYMBOL", name="block"),
    ],
)
```

### 138) async_block

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="async"),
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="move"),
                BlankRule(type="BLANK"),
            ],
        ),
        SymbolRule(type="SYMBOL", name="block"),
    ],
)
```

### 139) try_block

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="try"),
        SymbolRule(type="SYMBOL", name="block"),
    ],
)
```

### 140) block

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="label"),
                        StringRule(type="STRING", value=":"),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="{"),
        RepeatRule(
            type="REPEAT",
            content=SymbolRule(type="SYMBOL", name="_statement"),
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_expression"),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="}"),
    ],
)
```

### 141) _pattern

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="_literal_pattern"),
        AliasRule(
            type="ALIAS",
            value="identifier",
            named=True,
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="u8"),
                    StringRule(type="STRING", value="i8"),
                    StringRule(type="STRING", value="u16"),
                    StringRule(type="STRING", value="i16"),
                    StringRule(type="STRING", value="u32"),
                    StringRule(type="STRING", value="i32"),
                    StringRule(type="STRING", value="u64"),
                    StringRule(type="STRING", value="i64"),
                    StringRule(type="STRING", value="u128"),
                    StringRule(type="STRING", value="i128"),
                    StringRule(type="STRING", value="isize"),
                    StringRule(type="STRING", value="usize"),
                    StringRule(type="STRING", value="f32"),
                    StringRule(type="STRING", value="f64"),
                    StringRule(type="STRING", value="bool"),
                    StringRule(type="STRING", value="str"),
                    StringRule(type="STRING", value="char"),
                ],
            ),
        ),
        SymbolRule(type="SYMBOL", name="identifier"),
        SymbolRule(type="SYMBOL", name="scoped_identifier"),
        SymbolRule(type="SYMBOL", name="tuple_pattern"),
        SymbolRule(type="SYMBOL", name="tuple_struct_pattern"),
        SymbolRule(type="SYMBOL", name="struct_pattern"),
        SymbolRule(type="SYMBOL", name="_reserved_identifier"),
        SymbolRule(type="SYMBOL", name="ref_pattern"),
        SymbolRule(type="SYMBOL", name="slice_pattern"),
        SymbolRule(type="SYMBOL", name="captured_pattern"),
        SymbolRule(type="SYMBOL", name="reference_pattern"),
        SymbolRule(type="SYMBOL", name="remaining_field_pattern"),
        SymbolRule(type="SYMBOL", name="mut_pattern"),
        SymbolRule(type="SYMBOL", name="range_pattern"),
        SymbolRule(type="SYMBOL", name="or_pattern"),
        SymbolRule(type="SYMBOL", name="const_block"),
        SymbolRule(type="SYMBOL", name="macro_invocation"),
        StringRule(type="STRING", value="_"),
    ],
)
```

### 142) tuple_pattern

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
                                    type="SYMBOL", name="_pattern"
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="closure_expression",
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
                                                name="_pattern",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="closure_expression",
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

### 143) slice_pattern

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
                        SymbolRule(type="SYMBOL", name="_pattern"),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    SymbolRule(
                                        type="SYMBOL", name="_pattern"
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
        StringRule(type="STRING", value="]"),
    ],
)
```

### 144) tuple_struct_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="type",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="identifier"),
                    SymbolRule(
                        type="SYMBOL", name="scoped_identifier"
                    ),
                    AliasRule(
                        type="ALIAS",
                        value="generic_type",
                        named=True,
                        content=SymbolRule(
                            type="SYMBOL",
                            name="generic_type_with_turbofish",
                        ),
                    ),
                ],
            ),
        ),
        StringRule(type="STRING", value="("),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(type="SYMBOL", name="_pattern"),
                        RepeatRule(
                            type="REPEAT",
                            content=SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value=","
                                    ),
                                    SymbolRule(
                                        type="SYMBOL", name="_pattern"
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

### 145) struct_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        FieldRule(
            name="type",
            type="FIELD",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(
                        type="SYMBOL", name="_type_identifier"
                    ),
                    SymbolRule(
                        type="SYMBOL", name="scoped_type_identifier"
                    ),
                ],
            ),
        ),
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
                                    type="SYMBOL",
                                    name="field_pattern",
                                ),
                                SymbolRule(
                                    type="SYMBOL",
                                    name="remaining_field_pattern",
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
                                                name="field_pattern",
                                            ),
                                            SymbolRule(
                                                type="SYMBOL",
                                                name="remaining_field_pattern",
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

### 146) field_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                StringRule(type="STRING", value="ref"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        ChoiceRule(
            type="CHOICE",
            members=[
                FieldRule(
                    name="name",
                    type="FIELD",
                    content=AliasRule(
                        type="ALIAS",
                        value="shorthand_field_identifier",
                        named=True,
                        content=SymbolRule(
                            type="SYMBOL", name="identifier"
                        ),
                    ),
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        FieldRule(
                            name="name",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL",
                                name="_field_identifier",
                            ),
                        ),
                        StringRule(type="STRING", value=":"),
                        FieldRule(
                            name="pattern",
                            type="FIELD",
                            content=SymbolRule(
                                type="SYMBOL", name="_pattern"
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ],
)
```

### 147) remaining_field_pattern

```py
StringRule(type="STRING", value="..")
```

### 148) mut_pattern

```py
PrecRule(
    type="PREC",
    value=-1,
    content=SeqRule(
        type="SEQ",
        members=[
            SymbolRule(type="SYMBOL", name="mutable_specifier"),
            SymbolRule(type="SYMBOL", name="_pattern"),
        ],
    ),
)
```

### 149) range_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="_literal_pattern"),
                SymbolRule(type="SYMBOL", name="_path"),
            ],
        ),
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
                                    type="STRING", value="..."
                                ),
                                StringRule(
                                    type="STRING", value="..="
                                ),
                                StringRule(type="STRING", value=".."),
                            ],
                        ),
                        ChoiceRule(
                            type="CHOICE",
                            members=[
                                SymbolRule(
                                    type="SYMBOL",
                                    name="_literal_pattern",
                                ),
                                SymbolRule(
                                    type="SYMBOL", name="_path"
                                ),
                            ],
                        ),
                    ],
                ),
                StringRule(type="STRING", value=".."),
            ],
        ),
    ],
)
```

### 150) ref_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="ref"),
        SymbolRule(type="SYMBOL", name="_pattern"),
    ],
)
```

### 151) captured_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="identifier"),
        StringRule(type="STRING", value="@"),
        SymbolRule(type="SYMBOL", name="_pattern"),
    ],
)
```

### 152) reference_pattern

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="&"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="mutable_specifier"),
                BlankRule(type="BLANK"),
            ],
        ),
        SymbolRule(type="SYMBOL", name="_pattern"),
    ],
)
```

### 153) or_pattern

```py
PrecRule(
    type="PREC_LEFT",
    value=-2,
    content=ChoiceRule(
        type="CHOICE",
        members=[
            SeqRule(
                type="SEQ",
                members=[
                    SymbolRule(type="SYMBOL", name="_pattern"),
                    StringRule(type="STRING", value="|"),
                    SymbolRule(type="SYMBOL", name="_pattern"),
                ],
            ),
            SeqRule(
                type="SEQ",
                members=[
                    StringRule(type="STRING", value="|"),
                    SymbolRule(type="SYMBOL", name="_pattern"),
                ],
            ),
        ],
    ),
)
```

### 154) _literal

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="string_literal"),
        SymbolRule(type="SYMBOL", name="raw_string_literal"),
        SymbolRule(type="SYMBOL", name="char_literal"),
        SymbolRule(type="SYMBOL", name="boolean_literal"),
        SymbolRule(type="SYMBOL", name="integer_literal"),
        SymbolRule(type="SYMBOL", name="float_literal"),
    ],
)
```

### 155) _literal_pattern

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="string_literal"),
        SymbolRule(type="SYMBOL", name="raw_string_literal"),
        SymbolRule(type="SYMBOL", name="char_literal"),
        SymbolRule(type="SYMBOL", name="boolean_literal"),
        SymbolRule(type="SYMBOL", name="integer_literal"),
        SymbolRule(type="SYMBOL", name="float_literal"),
        SymbolRule(type="SYMBOL", name="negative_literal"),
    ],
)
```

### 156) negative_literal

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="-"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SymbolRule(type="SYMBOL", name="integer_literal"),
                SymbolRule(type="SYMBOL", name="float_literal"),
            ],
        ),
    ],
)
```

### 157) integer_literal

```py
TokenRule(
    type="TOKEN",
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    PatternRule(
                        type="PATTERN",
                        value="[0-9][0-9_]*",
                        flags=None,
                    ),
                    PatternRule(
                        type="PATTERN",
                        value="0x[0-9a-fA-F_]+",
                        flags=None,
                    ),
                    PatternRule(
                        type="PATTERN", value="0b[01_]+", flags=None
                    ),
                    PatternRule(
                        type="PATTERN", value="0o[0-7_]+", flags=None
                    ),
                ],
            ),
            ChoiceRule(
                type="CHOICE",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            StringRule(type="STRING", value="u8"),
                            StringRule(type="STRING", value="i8"),
                            StringRule(type="STRING", value="u16"),
                            StringRule(type="STRING", value="i16"),
                            StringRule(type="STRING", value="u32"),
                            StringRule(type="STRING", value="i32"),
                            StringRule(type="STRING", value="u64"),
                            StringRule(type="STRING", value="i64"),
                            StringRule(type="STRING", value="u128"),
                            StringRule(type="STRING", value="i128"),
                            StringRule(type="STRING", value="isize"),
                            StringRule(type="STRING", value="usize"),
                            StringRule(type="STRING", value="f32"),
                            StringRule(type="STRING", value="f64"),
                        ],
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
        ],
    ),
)
```

### 158) string_literal

```py
SeqRule(
    type="SEQ",
    members=[
        AliasRule(
            type="ALIAS",
            value='"',
            named=False,
            content=PatternRule(
                type="PATTERN", value='[bc]?"', flags=None
            ),
        ),
        RepeatRule(
            type="REPEAT",
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    SymbolRule(type="SYMBOL", name="escape_sequence"),
                    SymbolRule(type="SYMBOL", name="string_content"),
                ],
            ),
        ),
        TokenRule(
            type="IMMEDIATE_TOKEN",
            content=StringRule(type="STRING", value='"'),
        ),
    ],
)
```

### 159) raw_string_literal

```py
SeqRule(
    type="SEQ",
    members=[
        SymbolRule(type="SYMBOL", name="_raw_string_literal_start"),
        AliasRule(
            type="ALIAS",
            value="string_content",
            named=True,
            content=SymbolRule(
                type="SYMBOL", name="raw_string_literal_content"
            ),
        ),
        SymbolRule(type="SYMBOL", name="_raw_string_literal_end"),
    ],
)
```

### 160) char_literal

```py
TokenRule(
    type="TOKEN",
    content=SeqRule(
        type="SEQ",
        members=[
            ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="b"),
                    BlankRule(type="BLANK"),
                ],
            ),
            StringRule(type="STRING", value="'"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    ChoiceRule(
                        type="CHOICE",
                        members=[
                            SeqRule(
                                type="SEQ",
                                members=[
                                    StringRule(
                                        type="STRING", value="\\"
                                    ),
                                    ChoiceRule(
                                        type="CHOICE",
                                        members=[
                                            PatternRule(
                                                type="PATTERN",
                                                value="[^xu]",
                                                flags=None,
                                            ),
                                            PatternRule(
                                                type="PATTERN",
                                                value="u[0-9a-fA-F]{4}",
                                                flags=None,
                                            ),
                                            PatternRule(
                                                type="PATTERN",
                                                value="u\\{[0-9a-fA-F]+\\}",
                                                flags=None,
                                            ),
                                            PatternRule(
                                                type="PATTERN",
                                                value="x[0-9a-fA-F]{2}",
                                                flags=None,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            PatternRule(
                                type="PATTERN",
                                value="[^\\\\']",
                                flags=None,
                            ),
                        ],
                    ),
                    BlankRule(type="BLANK"),
                ],
            ),
            StringRule(type="STRING", value="'"),
        ],
    ),
)
```

### 161) escape_sequence

```py
TokenRule(
    type="IMMEDIATE_TOKEN",
    content=SeqRule(
        type="SEQ",
        members=[
            StringRule(type="STRING", value="\\"),
            ChoiceRule(
                type="CHOICE",
                members=[
                    PatternRule(
                        type="PATTERN", value="[^xu]", flags=None
                    ),
                    PatternRule(
                        type="PATTERN",
                        value="u[0-9a-fA-F]{4}",
                        flags=None,
                    ),
                    PatternRule(
                        type="PATTERN",
                        value="u\\{[0-9a-fA-F]+\\}",
                        flags=None,
                    ),
                    PatternRule(
                        type="PATTERN",
                        value="x[0-9a-fA-F]{2}",
                        flags=None,
                    ),
                ],
            ),
        ],
    ),
)
```

### 162) boolean_literal

```py
ChoiceRule(
    type="CHOICE",
    members=[
        StringRule(type="STRING", value="true"),
        StringRule(type="STRING", value="false"),
    ],
)
```

### 163) comment

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="line_comment"),
        SymbolRule(type="SYMBOL", name="block_comment"),
    ],
)
```

### 164) line_comment

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="//"),
        ChoiceRule(
            type="CHOICE",
            members=[
                SeqRule(
                    type="SEQ",
                    members=[
                        TokenRule(
                            type="IMMEDIATE_TOKEN",
                            content=PrecRule(
                                type="PREC",
                                value=2,
                                content=PatternRule(
                                    type="PATTERN",
                                    value="\\/\\/",
                                    flags=None,
                                ),
                            ),
                        ),
                        PatternRule(
                            type="PATTERN", value=".*", flags=None
                        ),
                    ],
                ),
                SeqRule(
                    type="SEQ",
                    members=[
                        SymbolRule(
                            type="SYMBOL",
                            name="_line_doc_comment_marker",
                        ),
                        FieldRule(
                            name="doc",
                            type="FIELD",
                            content=AliasRule(
                                type="ALIAS",
                                value="doc_comment",
                                named=True,
                                content=SymbolRule(
                                    type="SYMBOL",
                                    name="_line_doc_content",
                                ),
                            ),
                        ),
                    ],
                ),
                TokenRule(
                    type="IMMEDIATE_TOKEN",
                    content=PrecRule(
                        type="PREC",
                        value=1,
                        content=PatternRule(
                            type="PATTERN", value=".*", flags=None
                        ),
                    ),
                ),
            ],
        ),
    ],
)
```

### 165) _line_doc_comment_marker

```py
ChoiceRule(
    type="CHOICE",
    members=[
        FieldRule(
            name="outer",
            type="FIELD",
            content=AliasRule(
                type="ALIAS",
                value="outer_doc_comment_marker",
                named=True,
                content=SymbolRule(
                    type="SYMBOL",
                    name="_outer_line_doc_comment_marker",
                ),
            ),
        ),
        FieldRule(
            name="inner",
            type="FIELD",
            content=AliasRule(
                type="ALIAS",
                value="inner_doc_comment_marker",
                named=True,
                content=SymbolRule(
                    type="SYMBOL",
                    name="_inner_line_doc_comment_marker",
                ),
            ),
        ),
    ],
)
```

### 166) _inner_line_doc_comment_marker

```py
TokenRule(
    type="IMMEDIATE_TOKEN",
    content=PrecRule(
        type="PREC",
        value=2,
        content=StringRule(type="STRING", value="!"),
    ),
)
```

### 167) _outer_line_doc_comment_marker

```py
TokenRule(
    type="IMMEDIATE_TOKEN",
    content=PrecRule(
        type="PREC",
        value=2,
        content=StringRule(type="STRING", value="/"),
    ),
)
```

### 168) block_comment

```py
SeqRule(
    type="SEQ",
    members=[
        StringRule(type="STRING", value="/*"),
        ChoiceRule(
            type="CHOICE",
            members=[
                ChoiceRule(
                    type="CHOICE",
                    members=[
                        SeqRule(
                            type="SEQ",
                            members=[
                                SymbolRule(
                                    type="SYMBOL",
                                    name="_block_doc_comment_marker",
                                ),
                                ChoiceRule(
                                    type="CHOICE",
                                    members=[
                                        FieldRule(
                                            name="doc",
                                            type="FIELD",
                                            content=AliasRule(
                                                type="ALIAS",
                                                value="doc_comment",
                                                named=True,
                                                content=SymbolRule(
                                                    type="SYMBOL",
                                                    name="_block_comment_content",
                                                ),
                                            ),
                                        ),
                                        BlankRule(type="BLANK"),
                                    ],
                                ),
                            ],
                        ),
                        SymbolRule(
                            type="SYMBOL",
                            name="_block_comment_content",
                        ),
                    ],
                ),
                BlankRule(type="BLANK"),
            ],
        ),
        StringRule(type="STRING", value="*/"),
    ],
)
```

### 169) _block_doc_comment_marker

```py
ChoiceRule(
    type="CHOICE",
    members=[
        FieldRule(
            name="outer",
            type="FIELD",
            content=AliasRule(
                type="ALIAS",
                value="outer_doc_comment_marker",
                named=True,
                content=SymbolRule(
                    type="SYMBOL",
                    name="_outer_block_doc_comment_marker",
                ),
            ),
        ),
        FieldRule(
            name="inner",
            type="FIELD",
            content=AliasRule(
                type="ALIAS",
                value="inner_doc_comment_marker",
                named=True,
                content=SymbolRule(
                    type="SYMBOL",
                    name="_inner_block_doc_comment_marker",
                ),
            ),
        ),
    ],
)
```

### 170) _path

```py
ChoiceRule(
    type="CHOICE",
    members=[
        SymbolRule(type="SYMBOL", name="self"),
        AliasRule(
            type="ALIAS",
            value="identifier",
            named=True,
            content=ChoiceRule(
                type="CHOICE",
                members=[
                    StringRule(type="STRING", value="u8"),
                    StringRule(type="STRING", value="i8"),
                    StringRule(type="STRING", value="u16"),
                    StringRule(type="STRING", value="i16"),
                    StringRule(type="STRING", value="u32"),
                    StringRule(type="STRING", value="i32"),
                    StringRule(type="STRING", value="u64"),
                    StringRule(type="STRING", value="i64"),
                    StringRule(type="STRING", value="u128"),
                    StringRule(type="STRING", value="i128"),
                    StringRule(type="STRING", value="isize"),
                    StringRule(type="STRING", value="usize"),
                    StringRule(type="STRING", value="f32"),
                    StringRule(type="STRING", value="f64"),
                    StringRule(type="STRING", value="bool"),
                    StringRule(type="STRING", value="str"),
                    StringRule(type="STRING", value="char"),
                ],
            ),
        ),
        SymbolRule(type="SYMBOL", name="metavariable"),
        SymbolRule(type="SYMBOL", name="super"),
        SymbolRule(type="SYMBOL", name="crate"),
        SymbolRule(type="SYMBOL", name="identifier"),
        SymbolRule(type="SYMBOL", name="scoped_identifier"),
        SymbolRule(type="SYMBOL", name="_reserved_identifier"),
    ],
)
```

### 171) identifier

```py
PatternRule(
    type="PATTERN",
    value="(r#)?[_\\p{XID_Start}][_\\p{XID_Continue}]*",
    flags=None,
)
```

### 172) shebang

```py
PatternRule(type="PATTERN", value="#![\\s]*[^\\[].+", flags=None)
```

### 173) _reserved_identifier

```py
AliasRule(
    type="ALIAS",
    value="identifier",
    named=True,
    content=ChoiceRule(
        type="CHOICE",
        members=[
            StringRule(type="STRING", value="default"),
            StringRule(type="STRING", value="union"),
        ],
    ),
)
```

### 174) _type_identifier

```py
AliasRule(
    type="ALIAS",
    value="type_identifier",
    named=True,
    content=SymbolRule(type="SYMBOL", name="identifier"),
)
```

### 175) _field_identifier

```py
AliasRule(
    type="ALIAS",
    value="field_identifier",
    named=True,
    content=SymbolRule(type="SYMBOL", name="identifier"),
)
```

### 176) self

```py
StringRule(type="STRING", value="self")
```

### 177) super

```py
StringRule(type="STRING", value="super")
```

### 178) crate

```py
StringRule(type="STRING", value="crate")
```

### 179) metavariable

```py
PatternRule(type="PATTERN", value="\\$[a-zA-Z_]\\w*", flags=None)
```

## Extras

### 1)

```py
PatternRule(type="PATTERN", value="\\s", flags=None)
```

### 2)

```py
SymbolRule(type="SYMBOL", name="line_comment")
```

### 3)

```py
SymbolRule(type="SYMBOL", name="block_comment")
```

## Precedences

## Externals

### 1)

```py
SymbolRule(type="SYMBOL", name="string_content")
```

### 2)

```py
SymbolRule(type="SYMBOL", name="_raw_string_literal_start")
```

### 3)

```py
SymbolRule(type="SYMBOL", name="raw_string_literal_content")
```

### 4)

```py
SymbolRule(type="SYMBOL", name="_raw_string_literal_end")
```

### 5)

```py
SymbolRule(type="SYMBOL", name="float_literal")
```

### 6)

```py
SymbolRule(type="SYMBOL", name="_outer_block_doc_comment_marker")
```

### 7)

```py
SymbolRule(type="SYMBOL", name="_inner_block_doc_comment_marker")
```

### 8)

```py
SymbolRule(type="SYMBOL", name="_block_comment_content")
```

### 9)

```py
SymbolRule(type="SYMBOL", name="_line_doc_content")
```

### 10)

```py
SymbolRule(type="SYMBOL", name="_error_sentinel")
```

## Inline

### 1) _path

### 2) _type_identifier

### 3) _tokens

### 4) _field_identifier

### 5) _non_special_token

### 6) _declaration_statement

### 7) _reserved_identifier

### 8) _expression_ending_with_block

## Conflicts

### 1) ['_type', '_pattern']

### 2) ['unit_type', 'tuple_pattern']

### 3) ['scoped_identifier', 'scoped_type_identifier']

### 4) ['parameters', '_pattern']

### 5) ['parameters', 'tuple_struct_pattern']

### 6) ['type_parameters', 'for_lifetimes']

### 7) ['array_expression']

### 8) ['visibility_modifier']

### 9) ['visibility_modifier', 'scoped_identifier', 'scoped_type_identifier']

## Word

identifier

## supertypes

### 1) _expression

### 2) _type

### 3) _literal

### 4) _literal_pattern

### 5) _declaration_statement

### 6) _pattern
