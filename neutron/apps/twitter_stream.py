# encoding: utf-8
#from tweepy import Stream
#from tweepy import OAuthHandler
import sys
from tweepy.streaming import StreamListener
from img_classifier.classify import ClassifyImg
import json
import score_tweet
import nltk
import numpy as np
class StdOutListener(StreamListener):
    'twitter stream listener'

    def __init__(self):
        self.score_img = ClassifyImg()

    def on_data(self, data):
        stream_data = json.loads(data) #converts to json format
        tweet = stream_data['text'].encode('ascii','ignore').lower()
        name = stream_data['user']
        user = name['screen_name'].encode('ascii','ignore')
        full_name  = name['name'].encode('ascii','ignore')
        tweet_token = nltk.word_tokenize(tweet)    #break the string down into word tokens
        if 'retweeted_status' in stream_data:
            tweet_id = stream_data['retweeted_status']['id_str']
        else:
            tweet_id = stream_data['id_str']
            
        parsed_data = {
            'user': full_name,
            'screen_name': user,
            'tweet': tweet,
            'tweet_token': tweet_token ,
            'raw_data' : stream_data,
            'tweet_id' : tweet_id
        }

          
        if 'retweeted_status' in stream_data:
            try:
                img_score = self.score_img.classify_image(stream_data['retweeted_status']['extended_entities']['media'][0]['media_url_https'])
            except:
                exception_error = sys.exc_info()[0]
                print exception_error
        else:           
            try:
                img_score = self.score_img.classify_image(stream_data['entities']['media'][0]['media_url_https'])
            except:
                exception_error = sys.exc_info()[0]
                print exception_error
                 
        

        try:
            if img_score['tour posters'] > .5:
                parsed_data['img_score'] = img_score['tour posters'] * 10
            else:
                parsed_data['img_score'] = 0
        except UnboundLocalError:
            parsed_data['img_score'] = 0

        #print parsed_data['img_score']
        
        read_tweet_stream = score_tweet.read_tweet()
        read_tweet_stream.process_tweet(parsed_data)
    

            
    def on_error(self, status):
        print status

