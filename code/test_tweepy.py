import tweepy
import sys
sys.path.extend(['H:\\rating_forecast\\social_media_rating_forecast\\code'])
from twitter_config import consumer_key, consumer_secret


auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

if not api:
    print ("Can't Authenticate")
    sys.exit(-1)

query = '#TheExorcist'
max_tweets = 10
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
