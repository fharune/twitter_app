import tweepy
import time


CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#users = ['printemps_317', 'luv_bk_nb', 'hir0ki_0ka']

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print("------------------------------------")
        print("tweet id:", status.id)
        print("screen_name:", status.user.screen_name)
        print("user name:", status.user.name)
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

if __name__ == '__main__':
	stream = tweepy.Stream(auth,MyStreamListener())
	while True :
			stream.filter(follow = ['1257339421440880640'])


