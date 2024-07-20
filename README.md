# pydantree

Pydantic parser for tree-sitter

[![PyPI Version](https://img.shields.io/pypi/v/pydantree)](https://pypi.org/project/pydantree/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pydantree.svg)](https://pypi.org/project/pydantree/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-pydantree.vercel.app-blue)](https://pydantree.vercel.app/)
[![CI Status](https://github.com/lmmx/pydantree/actions/workflows/ci.yml/badge.svg)](https://github.com/lmmx/pydantree/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lmmx/pydantree/master.svg)](https://results.pre-commit.ci/latest/github/lmmx/pydantree/master)

## Installation

```bash
pip install pydantree
```

## Grammars

The grammar schema (used to generate `models.py`) comes from
[this version][gs]
and should be updated when that changes.

**Last updated**: 20th July 2024

[gs]: https://github.com/tree-sitter/tree-sitter/blob/800f2c41d0e35e4383172d7a67a16f3933b86039/cli/src/generate/grammar-schema.json

The Python grammar comes from
[this version][gr]
and should be updated when that changes.

**Last updated**: 20th July 2024

[gr]: https://github.com/tree-sitter/tree-sitter-python/blob/0dee05ef958ba2eae88d1e65f24b33cad70d4367/src/grammar.json
