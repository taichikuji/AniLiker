#!/usr/bin/env python3

import requests
from time import sleep
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ANILIST_TOKEN = os.environ.get("ANILIST_TOKEN")
ANILIST_USERNAME = input("Input a username!\n> ")


def run_query(query, variables):
    response = requests.post(
        "https://graphql.anilist.co",
        json={"query": query, "variables": variables},
        headers={
            'content-type': "application/json",
            'authorization': "Bearer " + ANILIST_TOKEN
        }
    )

    print(response)

    if response.status_code == 200:
        return response.json()["data"]
    else:
        raise Exception("AniList query failed, check the provided username!")


def main():
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

    query = '''
      query ($user_id: Int) {
        Page{
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
        "user_id": user_id
    }

    activity = run_query(query, variables)["Page"]["activities"]

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
        sleep(3)


if __name__ == "__main__":
    main()
