import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from apps.twitter_stream import StdOutListener

#authentication key
consumer_key=
consumer_secret=
access_token=
access_secret=


if __name__ == "__main__":
    
    try:
        '''attempts to connect to twitter'''
        sys.stdout.write('Connecting to twitter........\n')
        twitter_listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        stream = Stream(auth, twitter_listener)
        sys.stdout.write('Connected to Twitter Streaming API!\n')
        sys.stdout.write('Listening....................\n')

    except:
        exception_error = sys.exc_info()[0]
        sys.stderr.write('Error connecting to twitter....\n')
        print exception_error

    #stream.filter( follow = [ '787546598440050688'])
    stream.filter( track = ['show'])
    
    #except KeyError:
     #   pass
        
