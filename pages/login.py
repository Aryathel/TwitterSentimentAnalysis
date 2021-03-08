# library imports
from flask import Blueprint, request, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth

class Login:
    """ Flask Blueprint | Login

    This contains all methods necessary for handling Twitter OAuth login to the site.

    Parameters
    ----------
    con_key: :class:`str`
        The Twitter consumer key for the application being used for OAuth.
    con_sec: :class:`str`
        The Twitter consumer secret for the application being used for OAuth.

    Endpoints
    ----------
    /login: GET
        The endpoint where users login through Twitter Oauth.
    """
    # Create a Flask Blueprint instance for the page.
    blueprint = Blueprint('login', __name__, template_folder='templates', static_folder='static')

    def __init__(self, app):
        # Create an instance of the flask oauth handler, and configure it for twitter.
        self.oauth = OAuth(app)
        self.oauth.register('twitter')

        @self.blueprint.route('/login')
        def login():
            """ Redirects the user to log in with Twitter. """

            redirect_uri = url_for('login.authorize', _external=True)
            print(redirect_uri)
            return self.oauth.twitter.authorize_redirect(redirect_uri)

        @self.blueprint.route('/authorize')
        def authorize():
            token = self.oauth.twitter.authorize_access_token()
            #resp = self.oauth.twitter.get('account/verify_credentials.json')
            #profile = resp.json()
            print(token)
            return redirect(url_for('index.index'))
