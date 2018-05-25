import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
## nltk comes with inbuilt sentiment analyser module that classify
## text under positive , negative and nuetral polarity of sentiments



reviews  = [
			"Great place to be when you are in Bangalore.",
			"The place was being renovated when I visited so the seating was limited.",
			"Loved the ambience, loved the food" , "The food is delicious but not over the top." ,
			"Service - Little slow, probably because too many people." , "The place is not easy to locate",
			"Mushroom fried rice was tasty",
			"I am not happy but very sad " ,
			"I am devasted by his cruelty",
			"I am extremly very delighted by his help",
			"I am so much happy that I am going out to have fun and dance with joy and have fun everyday ",			"I am extremly sorry",
			"I am very happy",
			"I am very very happy"]

analyser =  SentimentIntensityAnalyzer()

for review in reviews:
	print (review)
	result = (analyser.polarity_scores(review))
	print ("negative score = %s , positive score = %s , nuetral score = %s , compound score = %s") %(result['neg'] , result['pos'] , result['neu'] , result['compound'])
	print ("\n")

check = ["wow ! happy delighted amazing loved beloved embrace admire joyful merrily smile laughter alive beautiful and charming celebrate ",
		"Dreadful alas! extremly sad sinister rotten reject revenge rude sick evil cruelty broken cry dead depressed"
		]

print ("just to check how positive words change the compound score\n")
for review in check:
	print ("sentence is :- \n%s"%(review))
	result = analyser.polarity_scores(review)
	print ("negative score = %s , positive score = %s , nuetral score = %s , compound score = %s") %(result['neg'] , result['pos'] , result['neu'] , result['compound'])
	print ("\n")
x = 1;
while (x == 1):
	word = raw_input("Enter the word = ")
	word = TextBlob(word.lower())
	word = word.correct()
	word =str(word)
	print ("The correct word is = %s" %(word))
	print (analyser.polarity_scores(word))
	x = input("x = ")
