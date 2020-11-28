import tweepy
import time


CONSUMER_KEY = "T8h4Fg50DSudKPx47QpHQjgBL"
CONSUMER_SECRET = "2UczH062uFFgYne9yTsGYsrG8NhoohiWNNJs1WqMs0jqaqSHJ4"
ACCESS_TOKEN = "1257339421440880640-fkERYhchbWbFOdODZMPd0DmovtSjBF"
ACCESS_SECRET = "sOekwGYn5k13K4n3l7HPzEV5B2TG2XpRP8l0eTUZZ3Mkj"

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


