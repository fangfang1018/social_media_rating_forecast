import json
import tweepy
import sys
sys.path.extend(['H:\\rating_forecast\\social_media_rating_forecast\\code'])
from twitter_config import consumer_key, consumer_secret
import jsonpickle
import os
print os.getcwd()
save_dir = '../data/'
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

if not api:
    print ("Can't Authenticate")
    sys.exit(-1)


# searchQuery = '#60daysin'
# searchQuery = '#duckdynasty'
# searchQuery = '#TheExorcist'
# searchQuery = '@DuckDynastyAE'
searchQuery = '@TheExorcistFOX'
# searchQuery = '@TheMuppetsABC'

maxTweets = 10000000  # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'search_{}_tweets.txt'.format(searchQuery)  # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
try:
    tweets_file = open(save_dir + fName, "r")
    print 'recover historical file! '
    for line in tweets_file:
        try:
            latest_tweet = json.loads(line)
            sinceId = latest_tweet['id']
            since_time = latest_tweet['created_at']
            print 'Historical file contain up to {} tweets.'.format(since_time)
        except:
            continue
        break

except IOError:
    sinceId = None

# recover historical file and save info
try:
    tweets_file = open(save_dir + fName, "r")
    print 'recover historical file to save'
    tweets_data = tweets_file.read()
except IOError:
    pass


# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1L

tweetCount = 0

print("Downloading max {0} tweets".format(maxTweets))
f = open(save_dir + fName, 'w')
while tweetCount < maxTweets:
    try:
        if max_id <= 0:
            if not sinceId:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        since_id=sinceId)
        else:
            if not sinceId:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1))
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since_id=sinceId)
        if not new_tweets:
            print("No more tweets found")
            break
        for tweet in new_tweets:
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                    '\n')
        tweetCount += len(new_tweets)
        print("Downloaded {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # Just exit if any error
        print("some error : " + str(e))
        break

f.write(tweets_data)
f.close()

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))