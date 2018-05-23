import tweepy 
import sys
import re
import textblob

from textblob import TextBlob 
from nltk import sent_tokenize
from tweepy import OAuthHandler , API , Cursor
from datetime import datetime , date , time , timedelta 
from collections import Counter 
from bs4 import BeautifulSoup as soup 

consumer_key =  "XXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXX"

## attempt authentication 
class Twitter():

	def __init__(self):

		self.auth = OAuthHandler(consumer_key , consumer_secret)
		self.auth.set_access_token(access_token , access_token_secret)
		self.api = tweepy.API(self.auth)

		## now loading all the tweets in my page 
		self.public_tweets =  self.api.home_timeline()

	def print_tweets(self):

		for tweets in self.public_tweets:
			print (tweets.text)

		user =  self.api.get_user('twitter')
		## get the detail of user 
		print (user.screen_name)
		print (user.followers_count)

	## to get only text out of the tweets 
	def clean_tweets(self , tweets):
		cleaned_tweets = []
		## using regex for getting only those tweets that have  letters and numbers in it 
		for line in tweets:
			line =  re.findall(r'[A-Za-z0-9.\n]*' , line)
			rev  = TextBlob(" ".join(line))
			lines =  rev.sentences
			cleaned_tweets.append(lines)
		return (cleaned_tweets)		

	def sentiment_tweets(self , text):
		count_pos , count_neg , count_nuetral = 0 , 0 , 0
		text = self.clean_tweets(text)
		for line in text :
			print("\nline is \n ")
			print (line[0])
			print (line[0].sentiment)
			if line[0].sentiment[0] > 0 :
				print ("the following tweet shows Positive text ")
				count_pos += 1
			elif  line[0].sentiment[0] == 0:
				print ("the following tweet shows Nuetral text ")
				count_neg += 1
			else :
				count_nuetral += 1
				print ("the following tweet shows Negative text")

		return (count_pos , count_neg , count_nuetral)

	## getting the tweets 
	def get_tweets(self , query , count = 100):
		## query is the topic on which are going to get the tweets 
		## counts 
		tweets_list = []

		## calling twitter's API to get the tweets 
		try :
			fetched_tweets = self.api.search(q = query , count = count)
			#print (fetched_tweets)

			parsed_tweets = {}
			print ("GETTING TWEETS ON  %s " %(query))
			print ("\n\n")
			## parsing the tweets 
			for tweet in fetched_tweets:
				#print (tweet.text)
				## saving the texts in tweet 
				parsed_tweets['text'] = tweet.text
				tweets_list.append(parsed_tweets['text'])
			return (tweets_list)
		except :
			print ("No tweets")
			return ("No tweets")


def clean_tweets(tweets):
	## using regex for getting only those tweets that have  letters and numbers in it 
	tweets =  re.findall(r'[A-Za-z0-9.\n]*' , tweets)
	rev  = TextBlob(" ".join(tweets))
	## tokeninzing by sentences 
	lines =  rev.sentences
	print (lines)
	
def main ():

	t = Twitter()
	try :
		query = raw_input("Enter the query to be searched in Twitter = ")
		count = input("Enter number of tweets you want to get =  ")
	except NameError:
		query = input("Enter the query to be searched in Twitter")
		count = int(input("Enter number of tweets you want to get "))

	## calling the function get_tweets to get the tweets 
	tweets  = t.get_tweets(query ,count)
	#print (tweets)
	pos, neg , nuetral = t.sentiment_tweets(tweets)

	print ("percent of Positive tweets on %s %%" %(query))
	print (pos/float(count))
	print ("percent of Negative tweets on %s %%" %(query))
	print (neg/float(count))
	print ("percent of Nuetral tweets on %s  %%" %(query))
	print (nuetral/float(count))
	#t.sentiment_tweets(random_text)

if __name__ == "__main__":
	main()