# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Import libraries
import tweepy
from textblob import TextBlob

#Create your app from apps.twitter.com and fill your keys and tokens
consumer_key = 'v8ZMKENZ7IsOdtcb8xIN3qpqz'
consumer_secret = 'QXzjWKbUD6U2i6YZKA2v4ogMzZbHgEd4Ka9Bz6szpliLkJAvvt'
access_token = '104183294-2poXRHiCcniV9JKNZIfmFD0SIjva56Iovu0vr5tT'
access_token_secret = 'Xavup77xFaraYIqDoGOp0Mzw8ZxaQvvn73evP360j8zZz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Search tweets
public_tweets = api.search('iphone')
for tweet in public_tweets:
    #Print tweets
    print(tweet.text)
    #use textblob to fecth sentiment of the tweet
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')