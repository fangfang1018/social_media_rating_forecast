import tweepy
from tweepy import OAuthHandler

access_token = "780463243642937344-hlLqQ0YyR6bVDD9bGexynuddVmqIS3w"
access_secret = "bcqxHJnhZygv7q6unBKlp1axJL9Mk6lAHIiN2MQ8y6P9w"
consumer_key = "ZFzPvBCcQaLjKcsOrthZ1L5mc"
consumer_secret = "zAriCp8CF9nrPoeVngFG6Tv6JT78yvfukLYYtSKWEcEJbbNrJ6"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)