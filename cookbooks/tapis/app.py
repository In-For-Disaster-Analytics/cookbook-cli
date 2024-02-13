from pathlib import Path

from cookbooks.readme.markdown import (
    convert_markdown_local_file_to_html,
    convert_markdown_remote_file_to_html,
)
from cookbooks.utils.json_utils import write_json_file
from cookbooks.utils.uris import URIS, check_readme_src


def add_repository_readme_to_description(
    readme_src: str,
    app_spec_path: Path,
) -> None:
    """Add the repository README.md to the description of an app spec."""
    app_spec: dict = read_json_file(app_spec_path)  # type: ignore

    read_type = check_readme_src(readme_src)
    if read_type == URIS.PATH:
        converted_markdown = convert_markdown_local_file_to_html(readme_src)
    elif read_type == URIS.URL:
        try:
            converted_markdown = convert_markdown_remote_file_to_html(readme_src)
        except:
            print("Unable to download the README.md file.")
            exit(1)
    else:
        raise ValueError("The README.md url is not valid.")
    app_spec["description"] = converted_markdown
    write_json_file(app_spec_path, app_spec)
