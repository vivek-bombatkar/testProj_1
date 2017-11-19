import sys, json, config
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from tweepy import OAuthHandler
import tweepy

def getTwitStream():
    auth = OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)
    return TwitterStream(auth=auth)

def getTwipy():
    auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    return  tweepy.API(auth)

def main():
    twitStream = getTwitStream()
    result = twitStream.statuses.filter(track="papa") #, language="en"
    tweet_count = 10
    for twit in result:
        tweet_count -= 1
        print twit["text"]
        print twit["lang"]
        #print twit["country"]
        if tweet_count <= 0:
            break
    api = getTwipy()
    result = tweepy.Cursor(api.home_timeline).items()
    for s in result:
        print s.text

if __name__ == '__main__':
    main()