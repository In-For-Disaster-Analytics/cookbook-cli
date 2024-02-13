import os
from urllib.parse import urlparse


# enum
class URIS:
    URL = "URL"
    PATH = "Path"
    NEITHER = "Neither URL nor Path"


def check_readme_src(input_string: str):
    # Attempt to parse the input string as a URL
    parsed_url = urlparse(input_string)

    # Check if the input string is a URL
    if parsed_url.scheme in ("http", "https"):
        return URIS.URL

    # Check if the input string is a file path
    elif os.path.exists(input_string):
        return URIS.PATH

    # If neither, return that the input is neither a URL nor a valid path
    else:
        return URIS.NEITHER
