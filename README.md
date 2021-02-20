# Twitter Sentiment Analyzer
This is a work in progress project that I am starting to be able to let a user look up the general sentiment of tweets surrounding specific keyword(s) or hashtag(s).

## Setup Instructions
### Prerequisites:
- Python 3.8.2+
- Make sure you have the `pipenv` library installed.
- Have a [Twitter Developer](https://developer.twitter.com/) account created, and have an [application](https://developer.twitter.com/en/portal/dashboard) ready for this project.

1. Clone this repo.
1. Open a command prompt/terminal in the folder where the repo has been cloned, and run `pipenv install`.
1. Create a folder called `nltk_data` anywhere.
1. Create a file in the cloned folder named `.env`, and enter the contents using the following template:
```
NLTK_DATA={path to ntlk_data folder.}
TWITTER_CONSUMER_KEY={your Twitter application's consumer key}
TWITTER_CONSUMER_SECRET={your Twitter application's consumer key}
TWITTER_ACCESS_TOKEN={your Twitter application's access token}
TWITTER_ACCESS_SECRET={your Twitter application's access secret}
```
1. Edit the [main](main.py#39) file, on line 39, and change the `keyword` argument to your search keyword, and change the `num` argument to the maximum number of tweets you want to search.
1. Run `pipenv run python main.py` to start the program.
