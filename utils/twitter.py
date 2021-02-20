# Library imports
import tweepy

class Twitter:
    """ Class | Twitter

    Controls all things relating to connecting to the Twitter API,
    including querying data.

    Parameters
    ----------
    consumer_key: :class:`str`
        The Twitter API Consumer Key for the app to connect with.
    consumer_secret: :class:`str`
        The Twitter API Consumer Secret for the app to connect with.
    access_token: :class:`str`
        The Twitter API Access Token for the app to connect with.
    access_secret: :class:`str`
        The Twitter API Access Token for the app to connect with.

    Attributes
    ----------
    auth: :class:`tweepy.OAuthHandler`
        The Tweepy OAuth handler for the connection authentication.
    api: :class:`tweepy.API`
        The Tweepy API connection instance, after it has been authenticated.
    """
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        # Checking that all arguments passed have a value.
        if not all((consumer_key, consumer_secret, access_token, access_secret)):
            # Converting the arguments to a dict to report specifically which argument was passed improperly.
            # This is useful for when using `os.getenv()` to get environment variables, which may return None.
            args = dict(
                consumer_key = consumer_key,
                consumer_secret = consumer_secret,
                access_token = access_token,
                access_secret = access_secret
            )

            raise ValueError(f"Argument cannot have null value: {', '.join(arg for arg in args if args[arg] is None)}")

        # Creating the authentication handler with the provided information
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)

        # Creating the API connection instance.
        self.api = tweepy.API(self.auth)

    def get_tweets(self, keyword, num):
        """ Method | Get Tweets

        This method retrieves a list of tweets from the twitter API,
        which include the given keyword and has up the the number of
        results.

        Parameters
        ----------
        keyword: :class:`str`
            A keyword or hashtag to query tweets of.
        num: :class:`int`
            The maximum number of tweets to retrieve.
        """
        tweets = tweepy.Cursor(self.api.search, q=keyword).items(num)
        return tweets
