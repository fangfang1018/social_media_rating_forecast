from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
from twitter_config import access_token, access_token_secret, consumer_key, consumer_secret


# This is a basic listener that just prints received tweets to stdout.
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
    if len(sys.argv) > 1:
        keywords = sys.argv[1:]
    else:
        print 'Using default keywords...'
        keywords = ['@ABCConviction', '@Castle_ABC', '@ESPNCFB', '@ModernFam']
    print keywords
    # stream.filter(track=keywords)
    stream.filter(track=keywords)
