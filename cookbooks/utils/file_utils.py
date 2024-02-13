from pathlib import Path


def read_file(file: Path) -> str:
    """Read a file and return a string."""
    with open(file, "r") as f:
        return f.read()
