import tweepy
import pandas as pd


class TClient:
    def __init__(self, api):
        self.api = api

    def get_last_20_posts(self):
        columns = set()

        accepted_type = [int, str]

        tweets_data = []
        for status in self.api.user_timeline():
            keys = vars(status).keys()

            status_dict = dict(vars(status))
            tweet = {"author": status.user.screen_name,
                     "created": status.created_at.strftime("%m/%d/%Y, %H:%M:%S")}
            allowed = ["author", "text", "created", "id", "source"]
            for k in keys:
                if k not in allowed:
                    continue
                if type(status_dict[k]) in accepted_type:
                    if k == "text":
                        status_dict[k] = status_dict[k].replace("\n", " ")
                    tweet[k] = status_dict[k]
                    columns.add(k)
            tweets_data.append(tweet)

        # header_cols = list(columns)
        # header_cols.append("author")
        # header_cols.append("created")
        return tweets_data
        # return pd.DataFrame(tweets_data, columns=header_cols)

    def get_last_20_mentions(self):
        columns = set()

        accepted_type = [int, str]

        tweets_data = []
        for status in self.api.mentions_timeline():
            keys = vars(status).keys()

            status_dict = dict(vars(status))
            tweet = {"author": status.user.screen_name,
                     "created": status.created_at.strftime("%m/%d/%Y, %H:%M:%S")}
            allowed = ["author", "text", "created", "id", "source"]
            for k in keys:
                if k not in allowed:
                    continue
                if type(status_dict[k]) in accepted_type:
                    if k == "text":
                        status_dict[k] = status_dict[k].replace("\n", " ")
                    tweet[k] = status_dict[k]
                    columns.add(k)
            tweets_data.append(tweet)

        return tweets_data
