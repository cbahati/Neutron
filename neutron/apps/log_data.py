# encoding: utf-8
import pprint
import json
from pymongo import MongoClient

class log_data(object):
    'module to store data into a database'

    client = MongoClient()
    
    def __init__(self, data):
        self.data = data
        

    def insert_tweet( self ):
        'insert tweets into tweet table of neutrons database'
        try:
            neutron_db = self.client.test
            tweets = neutron_db.tweets
            tweets.insert_one(self.data)
        except:
            print "Error Inserting Data...."

    def find_tweet( self, name ):
        'find tweet in database'
        try:
            neutron_db = self.client.neutron
            tweets = neutron_db.tweets
            return tweets.find_one({"name": name })
        except:
            print "Error Finding Tweet"
        
            
