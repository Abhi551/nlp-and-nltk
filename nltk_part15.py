## using different learning algorithms from scikit learn on same data and combining them for stable result

## 1. SklearnClassifier , 
## 2. MultinomialNB , 
## 3. BernoulliNB , 
## 4. LogisticRegression 
## 5. SGDClassifier 
## 6. LinearSVC 
## 7. NuSVC

import random 
import nltk 
from nltk.corpus import movie_reviews , stopwords
from nltk import NaiveBayesClassifier
from nltk import classify


## taking fileid and category in docs
docs = []
for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		docs.append(fileid)
## thus there are 2000 file in movie_reviews folder
print ("number of files in the folder are %s" %(len(docs)))
## shuffling as data is already organised
print("first file in the document is %s" %(docs[1]))
random.shuffle(docs)
print("after shuffling the first file is %s"%(docs[1]))


def find_features(loc):
	## checkig that whether a word in feature is present in document or not 
	features_dict = {}
	loc_words = set(movie_reviews.words(loc))
	#print ("number of words in the file %s are %s " % (loc,len(loc_words)))
	

	for word in word_features:
		## checking whether a word present in word_features is also present in our current documents 
		if word[0] in loc_words :
			features_dict[word] = 'True'
		elif word[0] in loc_words :
			features_dict[word] =  'False'

	return features_dict


## create a feature set , called all_features
## a list of tuples with argument (find_features() , category)
## category ,whether a file is pos or neg
	
## till now we have created a list of all files in movie_reviews
## while checking which word from word_feature is occuring in present file 
word_features , all_words ,all_features = []  , [] , [] 

## first step is to remove the stopping words from the set of all words
stop_words = stopwords.words('english')
#print (stop_words)


## create a list of all occuring words in the movie_reviews
for word in movie_reviews.words():
	if word in stop_words:
		pass
	elif word in [u',' , u'.' , u"'" , u'"' , u'-' , u')' , u'(' , u':']:
		pass
	else :
		all_words.append(word)

## after removing illegitimate words
print ("total number of words after removing illegitimate words %s" %(len(all_words)))

i=0
for word in nltk.FreqDist(all_words).most_common():
	(word_features.append(word))
	i+=1
	if i == 3000:
		break


for files in docs :
	all_features.append([find_features(files),str(files[:3])])

#print (len(all_features))

## positive dataset
training_data = all_features[:1900]
testing_data  = all_features[1900:]
## negative dataset
training_data = all_features[:100]
testing_data  = all_features[100:]


## training the classifier model
classifier = nltk.NaiveBayesClassifier.train(training_data)
print("Classifier accuracy percent on training_data : ",(nltk.classify.accuracy(classifier, training_data))*100)
print("Classifier accuracy percent on testing_data  : ",(nltk.classify.accuracy(classifier, testing_data))*100)


## how to use algorithms from scikit learn into nltk
## In nltk to use the scikit learn algorithms import SklearnClassifier 
from nltk.classify.scikitlearn import SklearnClassifier
## use sklearn module to import your classifier or algorithm
from sklearn.naive_bayes import MultinomialNB , BernoulliNB
from sklearn.linear_model import LogisticRegression , SGDClassifier
from sklearn.svm import SVC , LinearSVC , NuSVC

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
 
from nltk.classify import ClassifierI
from statistics import mode 

class VoteClassifier(ClassifierI):

	def __init__(self ,  *classifiers):
		self._classifiers = classifiers

	## function for classification of feature_set that we are passing
	def classify(self , features) :
		votes = []
		for c in self._classifiers:
			## returns the most appropriate label for the given featuere set
			vote = c.classify(features)
			#print (vote)
			votes.append(vote)
		try :
			return(mode(votes))
		except :
			return ("No mode value")

	## calculating the confidence of the feature set 
	def conf(self , features):
		votes = []
		for c in self._classifiers:
			votes.append(c.classify(features))
		try :
			choice_votes = votes.count(mode(votes))
			conf = choice_votes/float(len(votes))
			return (conf*100)
		except:
			return ("No confidence due to mulitple mode value")


votes = VoteClassifier(classifier , MNB_clf , BNB_clf , LR_clf , SGDC_clf , SVC_clf , linearSVC_clf , NuSVC_clf )

## we are providing first 10 files present in the training set to be evaluated whether it is pos or neg
for i in range(10):
	print ("classification  =  %s and confidence = %s " %(votes.classify(testing_data[i][0]) , votes.conf(testing_data[i][0])))

## accuracy using the combined algorithms still need to be calculated 