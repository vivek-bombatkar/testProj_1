import sys, json, config
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from tweepy import OAuthHandler
import tweepy

def getTwitStream(strSearch):
    auth = OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)
    twitStram = TwitterStream(auth=auth)
    return twitStram.statuses.filter(track=strSearch, language="en")

def getTwipy():
    auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    api = tweepy.API(auth)
    return tweepy.Cursor(api.home_timeline).items()

def main():
    result = getTwitStream("nuremberg")
    tweet_count = 10
    for twit in result:
        tweet_count -= 1
        print twit["text"]
        if tweet_count <= 0:
            break
    result = getTwipy()
    for s in result:
        print s.text

if __name__ == '__main__':
    main()

