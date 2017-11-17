import config
try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#1.
oauth = OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)
#2.
twitter_stream = TwitterStream(auth=oauth)
#3.
iterator = twitter_stream.statuses.filter(track="India", language="en")

tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    #print json.dumps(tweet)
    #print json.dumps(tweet, indent=4)
    print json.dumps(tweet["text"])
    if tweet_count <= 0:
        break 