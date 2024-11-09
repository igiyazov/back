import random
import string
from urllib.parse import urljoin, parse_qs, urlencode, urlunsplit, urlsplit

from django.conf import settings


def generate_link() -> str:
    random_id = generate_random_id(10)
    link = set_query_parameter(settings.CHECK_URL, "id", random_id)
    return link


def generate_random_id(size: int) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))


def set_query_parameter(url: str, param_name: str, param_value: str | int | float) -> str:
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = parse_qs(query_string)

    query_params[param_name] = [param_value]
    new_query_string = urlencode(query_params, doseq=True)

    return urlunsplit((scheme, netloc, path, new_query_string, fragment))