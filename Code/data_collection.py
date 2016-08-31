# This program is to collect stream of twitter data using Twitter API.
# It will save oveall data to twits_all.csv file.
# Data is filtered using location and language.
# Feature wise data is stored in twit_camera.csv, twit_price.csv file


from tweepy import Stream
from tweepy import  OAuthHandler
from tweepy.streaming import StreamListener
import time
import re
from nltk.classify import NaiveBayesClassifier

from textblob import TextBlob
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#Twitter API

ckey = 'zh7NemyEV3VBZwKGVXyyEc7KG'						
csecret = 'vAIA5EoTGtiFTEaZbUreNJ11rc7z1dBjFDqIan8eud3jzAR2Ef'
atoken  = '700967991958056960-KHDnblvDjAH3znW6hQwDOraKm4QuXo9'
asecret = 'zJeyiiGsqXdb0yTjyCcANNR9YL2k15LusNDsp3Jt2S1rl'

#For Finding number of tweets collected
cnt=0 
class listener(StreamListener):
    def on_data(self, data):
        try:                    
            tweet = data.split(',"text":"')[1].split('","source')[0]
            English_lan_filter=data.find("lang\":\"en")            # Data filtering
            print "Collecting tweets....."         
            r
            saveFile = open('twits_all.csv','a')       #Save Twits to file
            saveFile.write(data)
            saveFile.write('\n')        
            saveFile.close()
            
            if English_lan_filter != -1:
                
                # Data Preprocessing
                
                #Removing ascii values
                tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
                #tweet = re.sub(r'[^\u \]+',' ', tweet)
                tweet = tweet.encode("utf-8")
                #Convert to lower case
                tweet = tweet.lower()                         
                #Convert @username to AT_USER
                tweet = re.sub('@[^\s]+','', tweet)
                #Remove additional white spaces
                tweet = re.sub('[\s]+', ' ', tweet)
                #Replace #word with word
                tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
                #trim
                tweet = tweet.strip('\'"')                         
                stop_words =  set(stopwords.words("english"))

                words = word_tokenize(tweet)
                filtered_sentence =[]
                for i in words:
                    if i not in stop_words:
                        if(i.startswith("\u") or i.startswith("http") or i.startswith("\\")):                        
                            fg=1
                        else:
                            filtered_sentence.append(i)     
                        
                tweet = " ".join(filtered_sentence)
               
                saveFile = open('twit_over5.csv','a')       #Save Twits to file
                saveFile.write(tweet)
                #saveFile.write(data)
                saveFile.write('\n')        
                saveFile.close()
                        
                Location=data.find("India")                 #Filter Based on India              
                 
                if Location!=-1:                    
                    saveFile = open('twit_India_test.csv','a')
                    sentences = sent_tokenize(tweet)                
                    for i in sentences:
                        saveFile.write(i)
                        #saveFile.write(data)
                        saveFile.write('\n')        
                        saveFile.close()
                        #print "India"
                Location=data.find("New York")          #Filter Based on Location NY
                if Location!=-1:
                    saveFile = open('twit_NY_test.csv','a')
                    sentences = sent_tokenize(tweet)
                
                    for i in sentences:
                        saveFile.write(i)
                        #saveFile.write(tweet)
                        #saveFile.write(data)
                        saveFile.write('\n')        
                        saveFile.close()
                        #print "ny"
                Location=data.find("cali")        #Filter Based on Location California
                if Location!=-1:                    
                    saveFile = open('twit_cali_test.csv','a')
                    sentences = sent_tokenize(tweet)
                
                    for i in sentences:
                        saveFile.write(i)
                        #saveFile.write(tweet)
                        #saveFile.write(data)
                        saveFile.write('\n')        
                        saveFile.close()                          
                Location=data.find("camera")        #Filter Based on Location California
                if Location!=-1:                    
                    saveFile = open('twit_camera.csv','a')
                    sentences = sent_tokenize(tweet)
                
                    for i in sentences:
                        saveFile.write(i)
                        #saveFile.write(tweet)
                        #saveFile.write(data)
                        saveFile.write('\n')        
                        saveFile.close()                          
                Location=data.find("price")        #Filter Based on Location California
                if Location!=-1:                    
                    saveFile = open('twit_price.csv','a')
                    sentences = sent_tokenize(tweet)
                
                    for i in sentences:
                        saveFile.write(i)
                        #saveFile.write(tweet)
                        #saveFile.write(data)
                        saveFile.write('\n')        
                        saveFile.close()                          
                Location=data.find("color")        #Filter Based on Location California
                if Location!=-1:                    
                    saveFile = open('twit_color.csv','a')
                    sentences = sent_tokenize(tweet)
                
                    for i in sentences:
                        saveFile.write(i)
                        #saveFile.write(tweet)
                        #saveFile.write(data)
                        saveFile.write('\n')        
                        saveFile.close()
                Location=data.find("battery")        #Filter Based on Battery
                if Location!=-1:                    
                    saveFile = open('twit_color.csv','a')
                    sentences = sent_tokenize(tweet)
                
                    for i in sentences:
                        saveFile.write(i)
                        #saveFile.write(tweet)
                        #saveFile.write(data)
                        saveFile.write('\n')        
                        saveFile.close()                       
           
            return True
        
        except BaseException, e:            
            time.sleep(1)

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["iphone"])
