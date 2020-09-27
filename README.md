# AniLiker: A python autoliker

<p align="center"><img src="media/logo.webp" width="150px" /><br/>
<img src="https://img.shields.io/github/license/taichikuji/AniLiker?color=FF3351&logo=github" />
<img src="https://img.shields.io/github/commit-activity/w/taichikuji/AniLiker?label=commits&logo=github" />
</p>

## What's the point of this project?

This project was a way to learn GraphQL, and also create a project that I've been interested on using and testing for fun.

## What does it do?

This python project asks for a username from AniList and gives likes to every post available. Finishes with an error if gets capped by the API.

## How do I make it work?

1. First of all, you need to remove **.example** from **.env.example**.

2. Then you need to create an API Client on Anilist, and then input the data ( **Client ID**, **Client Secret** and **Redirect URI** ) inside the .env file;

   ```
   ANILIST_TOKEN=""
   ANILIST_CLIENT_ID=""
   ANILIST_CLIENT_SECRET=""
   ANILIST_REDIRECT_URI=""
   ```

   If you already have a token, you can ignore the rest.

   If you don't have anything, and you don't know how to retrieve the API Client from AniList

3. Now that you have the .env file ready, you just need to run the project! You have two ways;
   1. You can use pipenv. To do this you just need to install it with `pip install pipenv` and then `pipenv update`. This should prepare a virtual env with all the needed packages.
      After this you need to run `pipenv run main.py` and it should work just fine!
   2. You can do it manually without pipenv, this means you'll need to install the next packages:
      - requests
      - python-dotenv
      - requests-oauthlib
