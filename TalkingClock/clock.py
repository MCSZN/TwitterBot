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

def get_time():
    my_time = datetime.time(datetime.now())
    my_time = str(my_time)
    my_time = my_time[:5]
    return my_time

schedule = 3600 #type number of seconds between two posts
my_time = get_time()

while True:
    api.update_status(status= "The time is {}.".format(my_time))
    time.sleep(schedule)
    my_time = get_time()
