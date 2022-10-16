# Luke Coddington
# 10/16/22
# Assignment - Facial Recognition
# Assumed Time: 2hr
# Actual Time: 2hrs
# Reasoning: It took a bit to get access to the twitter api. After that it was all data modulation. 


from distutils.command.clean import clean
import tweepy
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import traceback
import os
from dotenv import load_dotenv

load_dotenv()

print("")
print("="*50)
print("Sentiment Analysis for Twitter")
print("="*50)
query = input("Enter query :: ")
count = input("Enter number of results :: ")

positive = 0
negative = 0
neutral = 0
id = 0

def log(text, output=False):
    global id
    f = open("Twitter-Analysis.txt", "a")
    f.write("{0}\n==============\n{1}\n\n".format(id,text))
    if(output):
        print(text)
    id+=1
    f.close()

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    global neutral
    global positive
    global negative
    analysis = analyser.polarity_scores(tweet)['compound']
    sentiment = "Neutral"
    if(analysis >= 0.5):
        sentiment = "Positive"
        positive+=1
    elif(analysis <= -0.5):
        sentiment = "Negative"
        negative +=1
    else:
        neutral +=1

    log("Tweet :: {0}\nSentiment :: {1}".format(tweet,sentiment))
    return sentiment


try:
    auth = tweepy.OAuth2BearerHandler(os.getenv("AUTH_TOKEN"))
    api = tweepy.API(auth)
    analyser = SentimentIntensityAnalyzer()
    count = int(count)
    tweets = []
    # call twitter api to fetch tweets
    fetched_tweets = api.search_tweets(q=query, count=count)

    # parsing tweets one by one
    for tweet in fetched_tweets:
        # empty dictionary to store required params of a tweet
        parsed_tweet = {}

        # saving text of tweet
        cleanTweet = clean_tweet(tweet.text)
        parsed_tweet['text'] = cleanTweet
        # saving sentiment of tweet
        parsed_tweet['sentiment'] = get_tweet_sentiment(parsed_tweet)

        # appending parsed tweet to tweets list
        if tweet.retweet_count > 0:
            # if tweet has retweets, ensure that it is appended only once
            if parsed_tweet not in tweets:
                tweets.append(parsed_tweet)
        else:
            tweets.append(parsed_tweet)

    print("\n")
    print("="*50)
    log("General Responses for {0} with {1} results".format(query, count), True)
    print("="*50)
    log("Positive :: {0}/{1}".format(positive, count), True)
    log("Negative :: {0}/{1}".format(negative, count), True)
    log("Neutral :: {0}/{1}".format(neutral, count), True)
    print("")

except:
    traceback.print_exc()