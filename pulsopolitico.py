#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[5]:


###API ########################
ckey = "5PkdgTA2oaoHz5bkexjSf18aX"
csecret = "S8gYGiVCARMakmKdLlrv5iBw29S8gPJKNn56r5FPgiEgTSelDZ"
atoken = "407397682-RWFLyoDgdA3nF29LEy7UEuFYU2ACsjZnZ9eLt6It"
asecret = "wI0zonTbEnnLxJ5iFy59qiqGq6qug7LQYDWFGywmR6TPL"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:0985985104@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    ###Nombre de la base de datos (provincia)
    db = server.create('guayas')
except:
    db = server['guayas']
    
'''===============LOCATIONS=============='''    
#Filtro por geolocalización
twitterStream.filter(locations=[-80.5634,-3.0643,-79.1019,-0.8367])
#Filtro por palabras
twitterStream.filter(track=['Elecciones Ecuador 2021','Guillermo Lasso','Alfredo Borrero','CREO'])


# In[ ]:




