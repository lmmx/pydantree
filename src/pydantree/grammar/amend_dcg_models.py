import re
import argparse
from pathlib import Path


def replace_patterns_in_file(file_path):
    path = Path(file_path)
    content = path.read_text()

    # Ensure 'Literal' import
    import_pattern = r"from typing import ([\w, ]+)"
    literal_import = "Literal"

    if "from typing import Literal" not in content:
        match = re.search(import_pattern, content)
        if match:
            # If there's an existing import line from typing, add Literal to it
            existing_imports = match.group(1)
            if literal_import not in existing_imports:
                new_imports = existing_imports + ", " + literal_import
                content = re.sub(
                    import_pattern,
                    f"from typing import {new_imports}",
                    content,
                )
        else:
            # Otherwise, add a new import line after the first import
            first_import_pattern = r"(import .+\n)"
            content = re.sub(
                first_import_pattern,
                r"\1from typing import Literal\n",
                content,
                count=1,
            )

    # Define patterns and replacements
    single_value_pattern = r'constr\(pattern=r"\^(\w+)\$"\)'
    single_value_replacement = r'Literal["\1"]'

    multiple_values_pattern = r'constr\(pattern=r"\^\(([\w\|]+)\)\$"\)'

    def multiple_values_replacement(match):
        values = match.group(1).split("|")
        literal_values = ", ".join([f'"{value}"' for value in values])
        return f"Literal[{literal_values}]"

    # Perform the replacements
    content = re.sub(single_value_pattern, single_value_replacement, content)
    content = re.sub(multiple_values_pattern, multiple_values_replacement, content)

    # Find and replace class Rule definition
    rule_class_pattern = re.compile(
        r"class Rule\(\s*RootModel\[\s*Union\[\s*([\w\s,]+)\s*\]\s*\]\s*\):\s*root:\s*Union\[\s*([\w\s,]+)\s*\]",
    )

    def rule_class_replacement(match):
        union_types = match.group(1).replace("\n", "").replace(" ", "").split(",")
        union_variable = "RuleUnion"
        union_definition = (
            f"{union_variable} = Union[\n    " + ",\n    ".join(union_types) + "\n]"
        )
        return (
            f"{union_definition}\n\n"
            "class Rule(RootModel[\n"
            f"    {union_variable}\n"
            "]):\n"
            f"    root: {union_variable}"
        )

    content = re.sub(rule_class_pattern, rule_class_replacement, content)

    path.write_text(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Amend Pydantic models.")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to the input file",
    )

    args = parser.parse_args()

    replace_patterns_in_file(args.input)
