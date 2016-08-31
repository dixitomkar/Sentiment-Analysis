from tweepy import Stream
from tweepy import  OAuthHandler
from tweepy.streaming import StreamListener
import time
import re
from nltk.classify import NaiveBayesClassifier
#from nltk.corpus 
from textblob import TextBlob
import nltk
#nltk.download();
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from textblob.classifiers import NaiveBayesClassifier
import csv
import os
import sys


with open('twit_India_test.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     filtered_sentence =[]
     i=0
     temp_list = []
     for row in spamreader:
          temp_list.append(', '.join(row))
         
     new_class=[]
     p=1
     for i in temp_list:
             char=','
             i=i.replace(char,'')
             char='('
             i=i.replace(char,'')
             char=')'
             i=i.replace(char,'')
             char='['
             i=i.replace(char,'')
             char=']'
             i=i.replace(char,'')
             char=';'
             i=i.replace(char,'')
             char=':'
             i=i.replace(char,'')
             char='|'
             i=i.replace(char,'')
             char='"'
             i=i.replace(char,'')
             char='\''
             i=i.replace(char,'')
             #print i
             abd=TextBlob(i).sentiment.polarity
             if abd>0:
                  p=p+1
                  q=str(p)
                  s1=os.getenv('UserProfile')
                  s2=s1+'\Desktop\\project_python\\Submission\\india\\pos\\'
                  ch=str(s2+q)
                 
                  saveFile = open(ch,'a')
                  saveFile.write(i)             
                  saveFile.write('\n')
                  saveFile.close()
                                    
             else:                  
                  p=p+1
                  q=str(p)
                  s1=os.getenv('UserProfile')
                  s2=s1+'\Desktop\\project_python\\Submission\\india\\neg\\'
                  ch=str(s2+q)
                  
                  saveFile = open(ch,'a')
                  saveFile.write(i)             
                  saveFile.write('\n')
                  saveFile.close()

print "Program Completed. View results in WEKA" 
 

