from pathlib import Path
from typing import Annotated

import typer

from cookbooks.tapis.app import add_repository_readme_to_description

app = typer.Typer()


@app.command()
def description(
    readme_src: Annotated[
        str, typer.Argument(help="README.md url to download.", default=None)
    ],
    app_spec_path: Annotated[
        Path,
        typer.Argument(
            help="App spec file to add the README.md to the description.", default=None
        ),
    ],
):
    """
    Create pages of projects and people (students and advisors) from the database (sqlite3) using wowchemy-hugo-academic.
    """
    if app_spec_path and readme_src:
        add_repository_readme_to_description(readme_src, app_spec_path)
    else:
        typer.echo("Please provide the app spec and the README.md url.")
