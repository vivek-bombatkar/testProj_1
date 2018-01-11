
from twitter import OAuth, TwitterStream
import config
import time

oauth = OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.filter(track="india", language="en")

#get n tewwts to a file
tweet_count = 10
with open("tweetStream{0}.txt".format(time.strftime('%Y%m%d-%H%M%S')),"a") as myFile:
    for tweet in iterator:
        tweet_count -= 1
        print tweet_count
        myFile.write(tweet["text"].encode('utf-8').strip())
        myFile.write("\n ########################################################## \n")
        if tweet_count <= 0:
            break

