from random import random
from flask import Flask, redirect, request, render_template
from spotify_api.auth import get_token
from spotify_api.uris import AUTHORIZE_URI
from utils.from_env import REDIRECT_URI, CLIENT_ID
from utils.query_params import query_params


app = Flask(__name__)


# Auto called after user login success
@app.route('/callback', methods=['GET'])
def hello():
    token = get_token(code=request.args["code"])
    response_ok = render_template("callback.html", token=token, default_scope="(only publicly available information)")
    return response_ok if token is not None else "Bad request"


# Loads the Spotify OAuth login page
@app.route('/login', methods=['GET'])
def login():
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "state": int(random() * 16) + 1
    }
    scope = request.args.get("scope", default=None)
    if scope is not None:
        params["scope"] = scope
    return redirect(AUTHORIZE_URI + query_params(params))


if __name__ == '__main__':
    app.run()
