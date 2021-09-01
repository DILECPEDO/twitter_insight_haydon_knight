import os
from login import twitter_api_login
from twitter_client import TClient
import time
import datetime

api = twitter_api_login()
tClient = TClient(api)


def if_file_not_exist_create(file):
    if not os.path.exists(file):
        with open(file, 'x'):
            pass


def now():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


while True:

    posts = tClient.get_last_20_posts()

    if_file_not_exist_create("tweets.txt")
    with open("tweets.txt", "r+") as f:
        text_file = f.read()
        for i in posts:
            if str(i["id"]) not in text_file:
                f.write(f"{i}\n")

    print(f"Last post update {now()}")

    mentions = tClient.get_last_20_mentions()

    if_file_not_exist_create("mentions.txt")
    with open("mentions.txt", "r+") as f:
        text_file = f.read()
        for mention in mentions:
            if str(mention["id"]) not in text_file:
                f.write(f"{mention}\n")

    print(f"Last mentions update {now()}")

    time.sleep(60)
