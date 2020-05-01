import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
import tweepy

# Authenticate to Twitter


app.config["TWITTER_OAUTH_CLIENT_KEY"] = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
app.config["TWITTER_OAUTH_CLIENT_SECRET"] = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")

# OAuth 2 Authentication to consumer key and consumer secret 
auth = tweepy.AppAuthHandler("TWITTER_OAUTH_CLIENT_KEY", "TWITTER_OAUTH_CLIENT_SECRET")
  
# Create API object
# api call limitations
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# ids
whitehouse = 822215673812119553
truongnfrank = 849797017396285440

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
#app.config["TWITTER_OAUTH_CLIENT_KEY"] = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
#app.config["TWITTER_OAUTH_CLIENT_SECRET"] = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")
twitter_bp = make_twitter_blueprint()
app.register_blueprint(twitter_bp, url_prefix="/login")

@app.route("/")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/verify_credentials.json")
    assert resp.ok
    return "You are @{screen_name} on Twitter".format(screen_name=resp.json()["screen_name"] + retweet() + "test")

def retweet():
    for status in tweepy.Cursor(api.user_timeline, screen_name="whitehouse", tweet_mode="extended").items(1):
        #print(status)
        #print(status.user.name)
        print(status.id)
        tweet_id = status.id
        #print(status.created_at)
        print(status.full_text)
        api.retweet(tweet_id)
