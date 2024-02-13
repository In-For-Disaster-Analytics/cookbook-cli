# type: ignore[attr-defined]
from enum import Enum
from random import choice
from typing import Optional

import typer
from rich.console import Console

from cookbooks import version
from cookbooks.commands.app import app as app_commands
from cookbooks.example import hello


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="cookbooks",
    help="`cookbooks` is a Python cli/package to work with TAPIS to build cookbook",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]cookbooks[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


app.add_typer(
    app_commands,
    name="app",
    help="Create pages of projects and people (students and advisors) from the database (sqlite3) using wowchemy-hugo-academic.",
)

console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]datafest-archive[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


if __name__ == "__main__":
    app()
