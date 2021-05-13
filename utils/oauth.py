from requests_oauthlib import OAuth2Session


def GET_AL_TOKEN(DATA):
    client_id = DATA["ANILIST_CLIENT_ID"]
    client_secret = DATA["ANILIST_CLIENT_SECRET"]
    authorization_base_url = "https://anilist.co/api/v2/oauth/authorize"
    token_url = "https://anilist.co/api/v2/oauth/token"
    AL = OAuth2Session(client_id, redirect_uri=DATA["ANILIST_REDIRECT_URI"])
    authorization_url, state = AL.authorization_url(authorization_base_url)
    redirect_response = input(
        f"Your Oauth2 url is {authorization_url} .\n Visit the url and login, then paste the full redirect URL here\n==============\nIF YOU GET A INSECURE HTTP ERROR, REPLACE HTTP WITH HTTPS\n==============\n> "
    )

    return AL.fetch_token(
        token_url, client_secret=client_secret, authorization_response=redirect_response
    )
