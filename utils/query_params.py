import urllib.parse


def query_params(params: dict[str, str]) -> str:
    return "?" + urllib.parse.urlencode(params)
