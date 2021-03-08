#!/usr/bin/env python

# Stdlib imports
import sys
import os
import re
import string

# Library imports
from flask import Flask
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

from pages.index import Index
from pages.login import Login

# Make sure that the sentiment analyzer has all of the data downloaded that it needs, and is up to date
nltk.download('vader_lexicon')

# Get the Twitter API connection info from environment variables.
con_key = os.getenv("TWITTER_CONSUMER_KEY")
con_sec = os.getenv("TWITTER_CONSUMER_SECRET")
acc_tok = os.getenv("TWITTER_ACCESS_TOKEN")
acc_sec = os.getenv("TWITTER_ACCESS_SECRET")

# Creating the Flask app.
app = Flask(__name__)

# Create a secret key for the flask sessions.
app.secret_key = os.getenv("APP_SECRET_KEY").encode("utf-8")

app.config.update(
    TWITTER_CLIENT_ID = con_key,
    TWITTER_CLIENT_SECRET = con_sec,
    TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token',
    TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token',
    TWITTER_AUTHORIZE_URL = 'https://api.twitter.com/oauth/authenticate'
)

# Create the twitter handler instance
tw_client = Twitter(con_key, con_sec, acc_tok, acc_sec)

# Creating page instances
index = Index(tw_client)
login = Login(app)

# Registering page blueprints.
app.register_blueprint(index.blueprint, url_prefix='/')
app.register_blueprint(login.blueprint, url_prefix='/')

""" DISABLING THIS FOR NOW WHILE FLASK FRAMEWORK IS GETTING SET UP
# Get a list of tweets with a given keyword
print("Getting tweets...")
tweets = tw_client.get_tweets(keyword = "destinythegame", num = 100)
tweets.drop_duplicates(inplace = True)
tweets = [tweet.text for tweet in tweets]

# Check the sentiments of said tweets
print("Processing Tweet sentiments...")
sentiment = Sentiment(tweets)

# Create and display a Pie Chart of positivity results.
labels = [
    f"Positive [{sentiment.positive_percent}%]",
    f"Neutral [{sentiment.neutral_percent}%]",
    f"Negative [ {sentiment.negative_percent}%]"
]

sizes = [sentiment.positive_percent, sentiment.neutral_percent, sentiment.negative_percent]
colors = ['yellowgreen', 'blue', 'red']
patches, texts = plt.pie(sizes, colors = colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result")
plt.axis("equal")
plt.show()
"""
