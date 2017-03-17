import tweepy

consumer_key="u2ESSV3gR2f1dfF099SkmBRy5"
consumer_secret="kMlyLhkbxVSw9JYBiMbEbM9PkzvBKq6qoOwagimDDKRQ81CJ9B"

access_token="2650637437-rEyx0EYN1kEvQvwwuTm6YqjteODtkBLPmu74e1E"
access_token_secret="Yabu4a45eBJ8VH6R9iB3yohwhkHMjUjMCj0n4b7ODTQ99"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline,id='USATODAY').items(10):
    print(tweet._json)
