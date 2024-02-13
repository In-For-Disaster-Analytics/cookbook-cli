from pathlib import Path

import markdown
import requests

from cookbooks.utils.file_utils import read_file


def convert_text_html(content: str) -> str:
    return markdown.markdown(content)


def download_markdown_file(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to download the file from {url}.")
    return response.text


def convert_markdown_remote_file_to_html(src: str) -> str:
    content = download_markdown_file(src)
    return convert_text_html(content)


def convert_markdown_local_file_to_html(path: str) -> str:
    if not Path(path).exists():
        raise FileNotFoundError(f"The file {path} does not exist.")
    content = read_file(Path(path))
    return convert_text_html(content)
