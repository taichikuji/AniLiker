# AniLiker: A python autoliker

<p align="center"><img src="media/logo.webp" width="150px" /><br/>
<a href="https://replit.com/@OkWeeb/AniLiker"><img src="https://repl.it/badge/github/taichikuji/aniliker" /></a>
<img src="https://img.shields.io/github/license/taichikuji/AniLiker?color=FF3351&logo=github" />
<img src="https://img.shields.io/github/commit-activity/w/taichikuji/AniLiker?label=commits&logo=github" />
</p>

# This project is going to be archived following a warning from AL

This means, so far, no more development of this project. I've come to realize it's just not worth it. I will keep the project up, but I don't think I will continue updating / supporting it.

I know a lot of people really liked this project and even offered new ideas, but this project itself is not ToS in regards of AL, and I know that some people used it for nefarious use.

I will continue to learn and develop more using AL's API, but for now, this is going archive. Hope you understand.

## What's the point of this project?

This project was a way to learn GraphQL, and also create a project that I've been interested on using and testing for fun.

## What does it do?

This python project asks for a username from AniList and gives likes to every post available. Finishes with an error if gets capped by the API.

## How do I make it work if I want to run it locally?

1. First of all, you need to remove **.example** from **.env.example**.

2. Then you need to create an API Client on Anilist, and then input the data ( **Client ID**, **Client Secret** and **Redirect URI** ) inside the .env file;

   ```
   ANILIST_TOKEN=""
   ANILIST_CLIENT_ID=""
   ANILIST_CLIENT_SECRET=""
   ANILIST_REDIRECT_URI=""
   ```

   If you already have a token, you can ignore the rest.

   If you don't have anything, and you don't know how to retrieve the API Client from AniList, you can follow our **[Wiki!](https://github.com/taichikuji/AniLiker/wiki)**

3. Now that you have the .env file ready, you just need to run the project! You have two ways;
   1. You can use pipenv. To do this you just need to install it with `pip install pipenv` and then `pipenv update`. This should prepare a virtual env with all the needed packages.
      After this you need to run `pipenv run main.py` and it should work just fine!
   2. You can do it manually without pipenv, this means you'll need to install the next packages: - requests - python-dotenv - requests-oauthlib
