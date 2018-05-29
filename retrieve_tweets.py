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

twitter_name = 'anybody' #chose the person you want to get tweets from
nbTweets = 100 #chose the number of tweets you want to get
file_name = "tweets.txt" #the file name you want

stuff = api.user_timeline(screen_name = twitter_name, count = nbTweets,
                          include_rts = False, tweet_mode = "extended")

my_tweets = []

for status in stuff:
    date = str(status.created_at)
    time = date[10:]
    time = time[:6]
    date = date[:10]
    my_tweets.append(status.full_text)
    print("On", date,"at", time, "{} tweeted:".format(twitter_name) , status.full_text,"\n")
    with open(file_name, "a") as myfile:
        myfile.write(status.full_text + "\n\n")
