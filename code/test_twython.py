from twython import Twython
from twython import TwythonStreamer


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

APP_KEY = 'ZFzPvBCcQaLjKcsOrthZ1L5mc'
APP_SECRET = 'zAriCp8CF9nrPoeVngFG6Tv6JT78yvfukLYYtSKWEcEJbbNrJ6'
OAUTH_TOKEN = "ZFzPvBCcQaLjKcsOrthZ1L5mc"
OAUTH_TOKEN_SECRET = "zAriCp8CF9nrPoeVngFG6Tv6JT78yvfukLYYtSKWEcEJbbNrJ6"

stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='twitter')



twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()
twitter.search(q='python')