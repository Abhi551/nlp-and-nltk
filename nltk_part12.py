import numpy as np 
import pandas as pd 
import nltk 
import random 
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC

## converting words to features with NLTK 

docs = []

for category in movie_reviews.categories():
	## giving two categories in the movie_reviews , namely pos and neg
	for fileid in movie_reviews.fileids(category):
		docs.append([fileid , category])

## number of files present in the movie_reviews folder are 2000
print (len(docs))

## shuffling the well organised data for analysis
random.shuffle(docs)
print (docs[1])

## listing all words in the movie_reviews folder

list_words = []
for word in movie_reviews.words():
	list_words.append(word)
print (len(list_words))


all_words =  nltk.FreqDist(list_words)
## first 3000 words in the items but this won't give good results
## to get better results we will remove stopping words and after that we will take most occuring words in the texts 

word_features = all_words.items()[:3000]


## marking these words as features 
## i.e. their presence means positive or negative review 

## create a function that accepts list of words 
## in a text file in the movie_reviews folder

def find_features(document):
	## creates a set of passed words in the documents
	words = set(document)
	features = {}

	for word in word_features:
		## returns true if word is present in collection of word_features from all words 
		features[word] = word in words

	return features

print (find_features(movie_reviews.words('neg/cv000_29416.txt')))

## we can do this for all our files present in the movie_reviews folder
feature_set = [(find_features(fileid) , category ) for fileid , category in docs]
print (len(feature_set))
#print (type(feature_set))

## taking better features
## new_features will only inlclude highest occuring non stopping words in the tex


# set that we'll train our classifier with
training_set = feature_set[:1900]

# set that we'll test against.
testing_set = feature_set[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, training_set))*100)



## using different classifiers from nltk modules
