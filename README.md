# BasicSpotifyClient API Reference



## Usage

1. Start the server
2. <b>Log-in into Spotify</b>
3. Enter your Spotify credentials
4. The `access_token` will be shown in the browser
5. Open a REST client, for example: <i>Postman</i>
6. Visit the Spotify API reference docs: https://developer.spotify.com/documentation/web-api
7. Send a request to an Spotify API endpoint with the header `Authorization: Bearer access_token`
<br>
<i> For more info about access tokens, visit https://developer.spotify.com/documentation/web-api/concepts/access-token </i>


<br>
<br>


## Log-in into Spotify

<br>
These endpoints are <span style="text-decoration: underline;">only for accessing from a browser</span>, for example: <i>Google Chrome, Mozilla Firefox, Edge</i>, etc.
<br>
<i>Do not request this URLs using a REST client.</i>
<br>
<br>

### Log-in without scope (access only to publicly available information)
```GET /login``` 

---

### Log-in with [scope](https://developer.spotify.com/documentation/web-api/concepts/scopes) (for example: "user-library-read")
```GET /login?scope=user-library-read```
