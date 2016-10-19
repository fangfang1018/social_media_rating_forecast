import tweepy
import sys
API_KEY = 'ZFzPvBCcQaLjKcsOrthZ1L5mc'
API_SECRET = 'zAriCp8CF9nrPoeVngFG6Tv6JT78yvfukLYYtSKWEcEJbbNrJ6'
OAUTH_TOKEN = "780463243642937344-hlLqQ0YyR6bVDD9bGexynuddVmqIS3w"
OAUTH_TOKEN_SECRET = "bcqxHJnhZygv7q6unBKlp1axJL9Mk6lAHIiN2MQ8y6P9w"

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

if not api:
    print ("Can't Authenticate")
    sys.exit(-1)

import sys
import jsonpickle
import os

searchQuery = '#TheExorcist'  # this is what we're searching for
maxTweets = 10000000  # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'search_{}_tweets.txt'.format(searchQuery)  # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1L

tweetCount = 0
save_dir = './data/'
print("Downloading max {0} tweets".format(maxTweets))
with open(save_dir + fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if max_id <= 0:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
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

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))