from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import urllib
import time
import json
import re

class listener(StreamListener):
    def on_data(self,data):
        try:
            print(data)
            info = json.loads(data)
            tweet = info['text']
            fetched_tweets=' '.join(re.sub("(RT @[A-Za-z0-9.]+)|([^.A-Za-z \t])|(\w+:\/\/\S+)|(https:[\/A-Za-z0-9.]+)", " ",tweet).split())
            

            print(fetched_tweets)
            savefile=open('pradeep.txt','a')
            savefile.write(fetched_tweets)
            savefile.write('\n')
            savefile.close()
            return(True)
        except BaseException as e:
            print('failed ondata',str(e))
            time.sleep(5)
            
    def on_error(self,status):
       print(status)
	   
	   
	   
auth=OAuthHandler("fsO18MwvFupzqDrV4U9dlki8E","1JybhT4V9UvHbtctS73cKKwIVqW37l0bw8IIIRtNLQZe2BfDQV")
auth.set_access_token("911987944608604160-HVrjPRFoIYV6uPHAWmICEFsw6SUo3UB","jXPLUrLmqMvVJxxVz1GzliPVle5BkzyPwpC4QDB3VRQo5")
stream=Stream(auth,listener())
stream.filter(track=["aadhaar"])

