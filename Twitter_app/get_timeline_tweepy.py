import tweepy
import time
from flask import Flask, render_template, request

app = Flask(__name__)


CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
	if (not status.retweeted) and ("RT @" not in status.text) and ("@" not in status.text):
		print("------------------------------------")
		print("tweet id:", status.id)
		print("screen_name:", status.user.screen_name)
		print("user name:", status.user.name)
		print(status.text)
	
        stream = tweepy.Stream(auth,MyStreamListener())
        stream.filter(follow = ['69889591', '2268227281', '733275531500605441', '1059024253532524544', '1257339421440880640']) 

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)



@app.route('/')
def index():
    header = "Tweet Recommendation"
    stream = myStream
    tweets = api.user_timeline(stream, count = 200)
    return render_template("index.html", header = header, tweets = tweets)   

if __name__ == "__main__":
    app.run(debug=True)
