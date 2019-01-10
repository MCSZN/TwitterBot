import tweepy, time
from datetime import datetime

consumer_key="YOUR KEY HERE"
consumer_secret="YOUR SECRET KEY HERE"

access_token="YOUR TOKEN HERE"
access_token_secret="YOUR SECRET TOKEN HERE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

"""
You can find such information by creating a titter account and going
in the developper section. Create an APP and use the related credentials
"""

api = tweepy.API(auth)

"""
The following code will unfav and delete all tweets and retweets from your account
"""

for tweets in tweepy.Cursor(api.user_timeline).items():
    api.destroy_status(tweets.id)
    print("Deleted :", tweets.id)

for favorites in tweepy.Cursor(api.favorites).items():
    api.destroy_favorite(favorites.id)
    print("Deleted :", favorites.id)
