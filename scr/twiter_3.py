from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
import config
import json
import pandas as pd
import matplotlib.pyplot as plt

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status

def getTweetSTream():
    i=StdOutListener()
    auth=OAuthHandler(config.CONSUMER_KEY,config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN,config.ACCESS_SECRET)
    strem=Stream(auth,i)
    return strem



def main():
    stream=getTweetSTream()
    result=stream.filter(track=["python"])
    print result

    '''
    tweets_data = []
    tweets_file = open("logs/te.txt",mode="r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    #print len(tweets_data)
    tweets=pd.DataFrame()
    tweets["text"]=map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

    tweets_by_lang = tweets['lang'].value_counts()
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
    tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
    plt.grid()
    '''

if __name__ == '__main__':
    main()
