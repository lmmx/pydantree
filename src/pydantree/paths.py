from pathlib import Path

__all__ = ["package_dir", "py_dir", "default_grammar_file", "default_node_types_file"]

package_dir = Path(__file__).parent
py_dir = package_dir / "data" / "languages" / "python"
default_grammar_file = py_dir / "grammar.json"
default_node_types_file = py_dir / "node-types.json"
