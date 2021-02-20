#!/usr/bin/env python

# Stdlib imports
import sys
import os
import re
import string

# Library imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pycountry
import nltk

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from langdetect import detect
from sklearn.feature_extraction.text import CountVectorizer

# Module imports
from utils.twitter import Twitter
from utils.sentiment import Sentiment

if __name__ == "__main__":
    # Make sure that the sentiment has all of the data downloaded that it needs, and is up to date
    nltk.download('vader_lexicon')

    # Get the Twitter API connection info from environment variables.
    con_key = os.getenv("TWITTER_CONSUMER_KEY")
    con_sec = os.getenv("TWITTER_CONSUMER_SECRET")
    acc_tok = os.getenv("TWITTER_ACCESS_TOKEN")
    acc_sec = os.getenv("TWITTER_ACCESS_SECRET")

    # Create the twitter handler instance
    tw_client = Twitter(con_key, con_sec, acc_tok, acc_sec)

    # Get a list of tweets with a given keyword
    print("Getting tweets...")
    tweets = tw_client.get_tweets(keyword = "destinythegame", num = 1000)
    tweets = [tweet.text for tweet in tweets]

    # Check the sentiments of said tweets
    print("Processing Tweet sentiments...")
    Sentiment(tweets)

    # Saving the tweets to a file just to poke around
    with open('./tweets.txt', 'wb+') as file:
        file.write("\n\n".join(tweets).encode("utf-8"))
