import requests
from time import sleep
import os
from os.path import join, dirname
from dotenv import load_dotenv, set_key
from utils import oauth

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AL_DATA = {}
if ((os.environ.get("ANILIST_TOKEN") == None) or (os.environ.get("ANILIST_TOKEN") == "")):
    AL_DATA = {
        "ANILIST_CLIENT_ID": os.environ.get("ANILIST_CLIENT_ID"),
        "ANILIST_CLIENT_SECRET": os.environ.get("ANILIST_CLIENT_SECRET"),
        "ANILIST_REDIRECT_URI": os.environ.get("ANILIST_REDIRECT_URI")
    }
    AL_DATA["ANILIST_TOKEN"] = oauth.GET_AL_TOKEN(AL_DATA)['access_token']
    set_key(dotenv_path, "ANILIST_TOKEN",
            AL_DATA["ANILIST_TOKEN"], quote_mode="always")
    print("AL Token has been saved on dotenv file")
else:
    AL_DATA["ANILIST_TOKEN"] = os.environ.get("ANILIST_TOKEN")


def run_query(query, variables):
    response = requests.post(
        "https://graphql.anilist.co",
        json={"query": query, "variables": variables},
        headers={
            'content-type': "application/json",
            'authorization': "Bearer " + AL_DATA["ANILIST_TOKEN"]
        }
    )

    print(response)

    if response.status_code == 200:
        return response.json()["data"]
    else:
        raise Exception("AniList query failed!")


def main():
    ANILIST_USERNAME = input("Input a username!\n> ")

    # Get user Id based on username

    query = '''
        query ($username: String) {
          User (name: $username) {
            id
          }
        }
    '''

    variables = {
        "username": ANILIST_USERNAME
    }

    user_id = run_query(query, variables)["User"]["id"]

    # Get latest AniList activities by user Id.
    npage = 1
    while npage > 0:
      query = '''
      query ($user_id: Int, $page: Int, $perPage: Int) {
              Page (page: $page, perPage: $perPage) {
                pageInfo {
                    hasNextPage
                  }
                activities (userId: $user_id, sort: ID_DESC) {
                    ... on ListActivity {
                      id
                  }
                  ... on TextActivity {
                      id
                      }
                  ... on MessageActivity {
                    id
                  }
                }
              }
            }
      '''

      variables = {
          "user_id": user_id,
          "page": npage,
          "perPage": 30

      }
      page = run_query(query, variables)["Page"]
      activity = page["activities"]
      pageInfo = page["pageInfo"]["hasNextPage"]

      for value in activity:
          query = '''
          mutation ($id: Int) {
            ToggleLikeV2(id: $id, type: ACTIVITY) {
              __typename
            }
          }
        '''
          variables = {
              "id": value["id"]
          }

          # ToggleLikeV2 runs
          run_query(query, variables)
      print(f"End of page, waiting 60 seconds to continue\nPage: {npage}")
      if pageInfo:
        npage = npage + 1
      else:
        npage = 0
      sleep(60)


if __name__ == "__main__":
    main()
