# encoding: utf-8
import log_data

class read_tweet(object):

        def __init__(self):
                self.score = 0
                self.key_words = { 'surprise': 5, 
                                   'secret': 5,
                                   'secretshow': 5,
                                   'tix' : 5, 
                                   'shows' : 5,
                                   'show' : 5,
                                   'north' : 2,
                                   'american' : 2,
                                   'confirmed' : 3,
                                   'sale' : 5,
                                   'now' : 3,
                                   'at' : 1,
                                   'tour': 3,
                                   'tonight' : 5,
                                   'door' : 2,
                                   'pop' : 3,
                                   'up' : 3,
                                   'live' : 3,
                                   'late' : 2,
                                   'pre-sale' : 8,
                                   'presale' : 8,
                                   'dates' : 3,
                                   'get' : 1,
                                   'today' : 2,
                                   'tickets' : 5,
                                   'ticket' : 5,
                                   'available': 3,
                                   'annouced' : 3,
                                   'concert': 3,
                                   'on' : 2,
                                   'new' : 4
                }  
                        
        
        #class method to log tweets into a txt file
        def log_result(self, processed_tweet):
                result = (
                        "------------------------------------------------------------\n"
                        "------------------------------------------------------------\n"
                        "Importance: {tweet_importance}\n"
                        "Score: {tweet_score}\n"
                        "user_name: {user_name} @{screen_name}\n"
                        "tweet: {tweet_text}\n"
                        ).format(
                                tweet_importance = processed_tweet['status'],
                                tweet_score = processed_tweet['score'],
                                user_name = processed_tweet['user'],
                                screen_name = processed_tweet['screen_name'],
                                tweet_text = processed_tweet['tweet']
                        )

                print result
                #writes to file        
                #with open('data_log.txt', 'ab') as ofstream:
                 #       ofstream.write(result)
                        #print result
                
        
        #class method to read and score tweet
        def process_tweet( self, tweet ):
                self.score = tweet['img_score']
                for word in tweet['tweet_token']:
                        try:
                                self.score += self.key_words[word]
                        except KeyError:
                                pass
                tweet['score'] = self.score
                if tweet['score'] >= 24:
                        tweet['status'] = "VERY IMPORTANT!"
                        
                elif tweet['score'] >= 14 and tweet['score'] < 24:
                        tweet['status'] = "IMPORTANT!"
                                                
                else:
                        tweet['status'] = "IGNORE"
                        
                if tweet['score'] >= 14:
                        data_base = log_data.log_data(tweet)
                        data_base.insert_tweet()

                print tweet['status']
                print tweet['score']
