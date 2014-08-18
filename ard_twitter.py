#ardunio and Twitter 
#June 29, 2014
#update August 17, 2014

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import serial

#make sure to change these keys according to your keys----------------------------------
ckey =    #ADD YOUR CONSUMER KEY
csecret = #ADD CONSUMER
atoken =  #ADD ACCESS TOKEN
asecret = #ADD ACCESS SECRET

connected = False

#Check serial port, change this is to the port you see on Arduino IDE--------------------
ser = serial.Serial("COM7")   

print ser.name + " is serial name"

#allow Ardunio to setup
time.sleep(2)
ser.write('0')

class listener(StreamListener):
    def on_data(self, data):
        try:
            print "-------------START OF NEW TWEET---------"
            tweet = (data.split(',"text"')[1]).split(',"source"')[0]
            print tweet
            
            print "- - - - - - Before writing to serial - - - - - - -"
            #write to serail 1
            ser.write('1')
            #delay sometime for light to show
            time.sleep(1)
            #write "0" to serial
            ser.write('0')
            #delay some time
            
            time.sleep(2)
        except BaseException, e:
            print 'failed on_data ' , str(e)
            time.sleep(3)
            print 'time after sleep in inner BaseException'

if __name__ == '__main__':
    #AUTHENTICATION
    try: 
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
    except:
        print 'failed to authenticate'
        
        
    try:
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=['fifa']) #Change parameters if needed----------------
        print "after listener"
        time.sleep(2)
    except:
        print "failed to get stream"