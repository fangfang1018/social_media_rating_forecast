#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "780463243642937344-hlLqQ0YyR6bVDD9bGexynuddVmqIS3w"
access_token_secret = "bcqxHJnhZygv7q6unBKlp1axJL9Mk6lAHIiN2MQ8y6P9w"
consumer_key = "ZFzPvBCcQaLjKcsOrthZ1L5mc"
consumer_secret = "zAriCp8CF9nrPoeVngFG6Tv6JT78yvfukLYYtSKWEcEJbbNrJ6"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])