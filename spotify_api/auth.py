import base64
from requests import JSONDecodeError, post
from spotify_api.uris import TOKEN_URI
from utils.from_env import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET


def get_token(code: str) -> dict[str, str] | None:
    body = {
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    client_data = base64.b64encode(bytes(f"{CLIENT_ID}:{CLIENT_SECRET}", 'utf-8')).decode('utf-8')
    headers = {
        "Authorization": "Basic " + client_data,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = post(TOKEN_URI, data=body, headers=headers)
    try:
        token = response.json()
    except JSONDecodeError:
        token = None
    return token
