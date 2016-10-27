import json
import pandas as pd
import pytz
import matplotlib.pyplot as plt
data_dir = '../data/'
# searchQuery = '#60daysin'
# searchQuery = '#duckdynasty'
# searchQuery = '#TheExorcist'
# searchQuery = '@DuckDynastyAE'
searchQuery = '@TheExorcistFOX'
# searchQuery = '@TheMuppetsABC'

data_name = 'search_{}_tweets.txt'.format(searchQuery)

tweets_data = []
tweets_file = open(data_dir+data_name, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)
tweets = pd.DataFrame(tweets_data)
t1 = pd.to_datetime(tweets.created_at[0], format='%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
t2 = pd.datetime.strptime(tweets.created_at[0], '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
tweets.loc[:, 'created_at'] = [pd.to_datetime(i, format='%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
                               for i in tweets.created_at]
tweets['date'] = [i.date() for i in tweets.created_at]
y = tweets.date.value_counts().sort_index()

plt.figure()
plt.plot(y.index, y)
plt.show()