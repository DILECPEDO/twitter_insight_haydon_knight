import tweepy
import os
from dotenv import load_dotenv, set_key


# used only first time to get the OTP code so we can retrieve (access_token, access_token_secret)
# def twitter_api_auth():
#     load_dotenv()
#     auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
#     print(auth.get_authorization_url())
#     code = input("code: ")
#     access_token = auth.get_access_token(code)
#     print(access_token)
#     set_key(".env", "ACCESS_TOKEN", access_token[0])
#     set_key(".env", "ACCESS_TOKEN_SECRET", access_token[1])


# Instantiation of twitter API client
# To be used every single time
def twitter_api_login():
    load_dotenv()
    auth = tweepy.OAuthHandler(os.getenv("API_KEY"),
                               os.getenv("API_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"),
                          os.getenv("ACCESS_TOKEN_SECRET"))
    return tweepy.API(auth, wait_on_rate_limit=True)
