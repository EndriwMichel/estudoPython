# Primeiro mini-projeto
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
import os

# Consumer Key
consumer_key = os.environ['tweeter_api_key']

# Consumer Secret
consumer_secret = os.environ['tweeter_api_secret']

# Access Token
access_token = os.environ['tweeter_token']

# Token Secret
access_token_secret = os.environ['tweeter_token_secret']

# Criando a autenticação
auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

# Classe para capturar stream de dados do tweeter
class MyListener(StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet['created_at']
        id_str = tweet['id_str']
        text = tweet['text']
        obj = {'created_at':created_at, 'id_str':id_str, 'text':text}
        tweetind = col.insertone(obj).inserted_id
        print(obj)
        return True

# Criando o objeto mylistener
my_listener = MyListener()

my_stream = Stream(auth, listener = MyListener)