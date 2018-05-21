## train a new dataset for sentiment analysis
## short positive and negative data of 5300 each is given 

## data should be in specific manner as (line , u'pos')

import nltk 
import random
import pickle

from nltk.tokenize import sent_tokenize , word_tokenize
from nltk.corpus import stopwords , movie_reviews
from unidecode import unidecode
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB , BernoulliNB
from sklearn.linear_model import LogisticRegression , SGDClassifier 
from sklearn.svm import SVC , LinearSVC , NuSVC
from nltk import ClassifierI
from statistics import mode


short_neg = open('neg.txt' , 'r'  ).read()
short_pos = open('pos.txt' , 'r'  ).read()

## converting them to utf-8 format

short_neg = unicode(short_neg , "utf-8")
short_pos = unicode(short_pos , "utf-8")

## earlier in all_features we had a complete data with its label as positive and negative
## we need to create a similar document 

## we will also apply the sent_tokenize method later on

documents = []

for line in short_pos.split('\n'):
	documents.append((line , 'pos'))
	
for line in short_neg.split("\n"):
	documents.append((line , 'neg'))
print (len(documents)/2)

## we have to tokenize all the words 

all_words = []

## tokenizing by word 
short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

## converting all the words to lower case
for words in short_neg_words:
	all_words.append(words.lower())
for words in short_pos_words:
	all_words.append(words.lower())

## gives the freqency distribution of all words in the documents
all_words = nltk.FreqDist(all_words)

## taking word features as most occuring 5000 words after removing symbols 
## which will detemerine the feature of the documents

word_features , i = [] , 0
for word in all_words.most_common():

	if word[0] in [u',' , u'.' , u"'" , u'"' , u'-' , u')' , u'(' , u':']:
		pass
	else :
		word_features.append(word)
		i = i+1
		if i == 5000:
			break

def find_features(document):
	words = word_tokenize(document)
	features = {}
	words = set(words)

	for word in word_features:
		if word[0] in words:
			features[word] = 'True'
		else :
			features[word] = 'False'
	return (features)

'''
print documents[0][0]
x = find_features(documents[0][0])

for a,b in x.items():
	if b == "True":
		print (a)
'''

featuresets = []
for rev , category in documents:
	featuresets.append([find_features(rev) , category])

print (featuresets)
random.shuffle(featuresets)
training_data = featuresets[:10000]
testing_data = featuresets[10000:]

## Voting and confidence  

class VoteClass(ClassifierI):

	def __init__ (self ,  *classifiers):
		self._classifiers = classifiers

	def classify(self ,  features):
		votes = []

		for c in self._c lassifiers:
			vote = c.classify(features)
			votes.append(vote)
		try :
			return (mode(votes))
		except :
			return (" No mode in this case ")

	def confidence(self ,  features) :
		votes = []

		for c in self._classifiers:
			vote = c.classify(features)
			votes.append(vote)

		## counts the votes for maximum occuring votes 
		choice_votes = votes.count(mode(votes))
		conf =  choice_votes/len(votes) 
		try :
			return (conf)
		except :
			return ("No mode in this case")


## training the classifier model
classifier = nltk.NaiveBayesClassifier.train(training_data)
print("Classifier accuracy percent on training_data : ",(nltk.classify.accuracy(classifier, training_data))*100)
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(classifier, testing_data))*100)

MNB_clf =  SklearnClassifier(MultinomialNB())
MNB_clf.train(training_data)
print ("\n\n")
print ("MNB Classifier ")
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(MNB_clf , testing_data))*100)


BNB_clf = SklearnClassifier(BernoulliNB())
BNB_clf.train(training_data)
print ("\n\n")
print ("BNB Classifier")
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(BNB_clf , testing_data))*100)

#for value in [1,10,15,50,335]:
LR_clf = SklearnClassifier(LogisticRegression())
LR_clf.train(training_data)
print ("\n\n")
print ("LogisticRegression")
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(LR_clf, testing_data))*100)

SGDC_clf =  SklearnClassifier(SGDClassifier())
SGDC_clf.train(training_data)
print ("\n\n")
print ("SGDC classifier")
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(SGDC_clf , testing_data))*100)

	
SVC_clf = SklearnClassifier(SVC(kernel = "linear"))
SVC_clf.train(training_data)
print ("\n\n")
print ("SV Classifier")
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(SVC_clf, testing_data))*100)

#for c in [.0001 , 10  ] :
linearSVC_clf = SklearnClassifier(LinearSVC (C = .1))
linearSVC_clf.train(training_data)
print ("\n\n")
print ("Linear SVC classifier")
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(linearSVC_clf, testing_data))*100)


NuSVC_clf = SklearnClassifier(NuSVC())
NuSVC_clf.train(training_data)
print ("\n\n")
print ("Nu SVC classifier")
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(NuSVC_clf, testing_data))*100)
## combining multiple algorithms 

voted_classifier = VoteClass(classifier , BNB_clf , MNB_clf , SVC_clf , SGDC_clf , NuSVC_clf , linearSVC_clf , LR_clf)
print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)