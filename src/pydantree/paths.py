from pathlib import Path

__all__ = ["package_dir", "default_grammar_file"]

package_dir = Path(__file__).parent
default_grammar_file = package_dir / "data" / "grammar.json"
