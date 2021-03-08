# Library imports
from flask import Blueprint, render_template, session, request
from tweepy.error import TweepError, RateLimitError

# Local imports
from utils.enums import SearchType

class Index:
    """ Flask Blueprint | Index

    The homepage for the Flask application, containing all methods pertaining
    to the primary site index, and navigation.

    Endpoints
    ----------
    /: GET
        The default home page for the site.
    """
    # Create a Flask Blueprint for the page.
    blueprint = Blueprint('index', __name__, template_folder = 'templates', static_folder='static')

    def __init__(self, tw_client):
        self.tw_client = tw_client

        @self.blueprint.route('')
        def index():
            """ This page is the home page that is loaded by default when the website is accessed. """
            # Get information on the session if the user has been logged in previously.
            access_token = session.get('access_token')

            if access_token:
                print(access_token)

            # Render an html file to the user.
            return render_template("index.html")

        @self.blueprint.route('/process', methods = ['GET', 'POST'])
        def process():
            search_type = request.form.get('search_type')
            result_number = request.form.get('result_number')
            search_string = request.form.get('search_string')

            return render_template(
                "processing.html",
                search_type = search_type,
                result_number = result_number,
                serach_string = search_string
            )

        @self.blueprint.route('/sentiment', methods = ['POST'])
        def sentiment():
            search_type = request.form.get('search_type')
            result_number = request.form.get('result_number')
            search_string = request.form.get('search_string')

            search_type = SearchType(search_type)

            if search_type == SearchType.user:
                if not search_string.startswith('@'):
                    search_string = '@' + search_string

                try:
                    tweets = self.tw_client.get_tweets(keyword = search_string, num = int(result_number))
                    tweets = [tweet.text for tweet in tweets]
                except TweepError as e:
                    print(f"Error Status {e.api_code}")

            elif search_type == SearchType.hashtag:
                pass
            elif search_type == SearchType.keyword:
                pass

            return render_template(
                "results.html",
                tweets = tweets
            )
