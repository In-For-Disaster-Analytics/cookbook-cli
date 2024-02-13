import pytest

from cookbooks.readme.markdown import (
    convert_markdown_remote_file_to_html,
    convert_text_html,
    download_markdown_file,
)

markdown_content = """# Sites and Stories Nlp\nCollection of NLP work related to the Sites and Stories efforts\n\n## NNA Alaska\n### Grey Literature: OpenAI Indices\n* Creation of indices using LlamaIndex for the NNA project grey literature\n\n### Planned Cookbook Catalog\n* Data Processing\n* Bertopic Analysis\n* LLM Analysis\n* Intercoder Reliability\n\n"""


def test_download_markdown():
    """Example test with parametrization."""
    url = "https://raw.githubusercontent.com/In-For-Disaster-Analytics/sites-and-stories-nlp/main/README.md"
    content = download_markdown_file(url)
    assert content == markdown_content


def test_convert_text_html():
    """Example test with parametrization."""
    expected = "<h1>Sites and Stories Nlp</h1>\n<p>Collection of NLP work related to the Sites and Stories efforts</p>\n<h2>NNA Alaska</h2>\n<h3>Grey Literature: OpenAI Indices</h3>\n<ul>\n<li>Creation of indices using LlamaIndex for the NNA project grey literature</li>\n</ul>\n<h3>Planned Cookbook Catalog</h3>\n<ul>\n<li>Data Processing</li>\n<li>Bertopic Analysis</li>\n<li>LLM Analysis</li>\n<li>Intercoder Reliability</li>\n</ul>"
    assert convert_text_html(markdown_content) == expected


def test_convert_markdown_file_to_html():
    """Example test with parametrization."""
    url = "https://raw.githubusercontent.com/In-For-Disaster-Analytics/sites-and-stories-nlp/main/README.md"
    expected = "<h1>Sites and Stories Nlp</h1>\n<p>Collection of NLP work related to the Sites and Stories efforts</p>\n<h2>NNA Alaska</h2>\n<h3>Grey Literature: OpenAI Indices</h3>\n<ul>\n<li>Creation of indices using LlamaIndex for the NNA project grey literature</li>\n</ul>\n<h3>Planned Cookbook Catalog</h3>\n<ul>\n<li>Data Processing</li>\n<li>Bertopic Analysis</li>\n<li>LLM Analysis</li>\n<li>Intercoder Reliability</li>\n</ul>"
    assert convert_markdown_remote_file_to_html(url) == expected
