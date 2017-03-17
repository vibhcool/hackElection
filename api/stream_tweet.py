from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="u2ESSV3gR2f1dfF099SkmBRy5"
consumer_secret="kMlyLhkbxVSw9JYBiMbEbM9PkzvBKq6qoOwagimDDKRQ81CJ9B"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2650637437-rEyx0EYN1kEvQvwwuTm6YqjteODtkBLPmu74e1E"
access_token_secret="Yabu4a45eBJ8VH6R9iB3yohwhkHMjUjMCj0n4b7ODTQ99"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=['bjp'])
