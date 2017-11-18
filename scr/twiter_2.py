import sys, json, config
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

def getTwitStream(strSearch):
    auth = OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)
    twitStram = TwitterStream(auth=auth)
    return twitStram.statuses.filter(track=strSearch, language="en")

def main():
    result = getTwitStream("clinikum nord nuremberg")
    for twit in result:
        print twit["text"]

if __name__ == '__main__':
    main()

