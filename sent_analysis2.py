import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
## nltk comes with inbuilt sentiment analyser module that classify
## text under positive , negative and nuetral polarity of sentiments



reviews  = [
			"Great place to be when you are in Bangalore.",
			"The place was being renovated when I visited so the seating was limited.",
			"Loved the ambience, loved the food" , "The food is delicious but not over the top." ,
			"Service - Little slow, probably because too many people." , "The place is not easy to locate",
			"Mushroom fried rice was tasty"]

analyser =  SentimentIntensityAnalyzer()

for review in reviews:
	print (review)
	result = (analyser.polarity_scores(review))
	print ("negative score = %s , positive score = %s , nuetral score = %s , compound score = %s") %(result['neg'] , result['pos'] , result['neu'] , result['compound'])
