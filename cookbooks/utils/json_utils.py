import json
from pathlib import Path


def read_json_file(file: Path) -> dict:  # type: ignore
    """Read a json file and return a dictionary."""
    with open(file, "r") as f:
        return json.load(f)


def write_json_file(file: Path, data: dict) -> None:  # type: ignore
    """Write a dictionary to a json file."""
    with open(file, "w") as f:
        json.dump(data, f, indent=2)
