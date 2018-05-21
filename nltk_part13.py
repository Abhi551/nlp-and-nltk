## applying Naive Bayes Algorithm to train and test on movie reviews data

import nltk
import random 
import pickle

from nltk.corpus import movie_reviews
from nltk import NaiveBayesClassifier 
from nltk.corpus import stopwords

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


## list of all words 
all_words = []
for word in movie_reviews.words():
	all_words.append(word)

## all_words contains all the words in movie_reviews
print ("\n")
print ("total number of words in the folder are %d "%(len(all_words)))

## calculating the freq of every word in all_words
all_words = nltk.FreqDist(all_words)
##print (all_words.items())


## 1.
## this is our basic model 
## we choose our features as first 3000 words in all_words
word_features = all_words.items()[:3000]
#print (word_features)

## this function works well
## creating our own function for find_features
'''
def find_features(document):
	## creates a set of passed words in the documents
	words = set(document)
	features = {}

	for word in word_features:
		## returns true if word is present in collection of word_features from all words 
		features[word] = word in words

	return features

#print (find_features(movie_reviews.words('neg/cv000_29416.txt')))
present =  find_features(movie_reviews.words('neg/cv000_29416.txt'))
print (present)
for words in present:
	if words[1] == True:
		print (words)

	

## create a function to find the words which will be the features in all_words 
## arguments passed are the words stored in a the file 
## assiging binary values for the words in every document 
'''

## now we have created a function that gives boolean value to each word depending on 
## whether or not it is present in our word_features set

print ("\nchecking the find_features function \n")

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

## to check for one file in the folder 
present = find_features('neg/cv000_29416.txt')

## save all the file names in all_features
## passing all the files present in movie_reviews
## we have already created a shuffled list of fileids named 'docs'

for files in docs:
	print ("file name is %s "%(files))
	break

all_features =[]

## create a feature set 
## a list of tuples with argument (find_features() , category)
## category ,whether a file is pos or neg

for files in docs :
	all_features.append([find_features(files),str(files[:3])])
	

## till now we have created a list of all files in movie_reviews
## while checking which word from word_feature is occuring in present file 

## now we have to train the data using our classifier
training_data = all_features[:1900]
#print (training_data)
testing_data= all_features[1900:]


## training the classifier model
classifier = nltk.NaiveBayesClassifier.train(training_data)

## now check the accuracy of our model
## our accuracy might change due to shuffling of data every time 
## so we get different files in training and test data
print("Classifier accuracy percent on training_data  is :  " , (nltk.classify.accuracy(classifier, training_data))*100)
print("Classifier accuracy percent on testing_data is :  "  , (nltk.classify.accuracy(classifier, testing_data))*100)

## show most infomative features 
print ("\n")
print ("Most occuring words and thier category is \n\n")
print (classifier.show_most_informative_features(15))


## with first 3000 words in word_features which gives false results as the first 3000 words in the all_words might not be
## the most occuring words in the data

## 2.
## so we will change our word_features to most common words , train the model on most occuring words on all_words data
## this is our second value in which we have most freq 3000 words among all words

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

print (len(all_words))

i=0

for word in nltk.FreqDist(all_words).most_common():
	(word_features.append(word))
	i+=1
	if i == 3000:
		break


for files in docs :
	all_features.append([find_features(files),str(files[:3])])

#print (len(all_features))

training_data = all_features[:1900]
testing_data  = all_features[1900:]


## train the data 
clf  = nltk.NaiveBayesClassifier.train(training_data)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_data))*100)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, training_data))*100)

print ("\n")
print ("Most occuring words and thier category is \n\n")
print (classifier.show_most_informative_features(15))


## saving the classifier using the concept of pickling
## this way we have saved the classifier in NaiveBayesClassifier 
save_classifier =  open('NaiveBayesClassifier.pickle' , 'wb')
pickle.dump(classifier , save_classifier)
save_classifier.close()

print ("\n\n")
print ("We have reloaded the classifier here \n")
## load the classifier 
classifier_f =open('NaiveBayesClassifier.pickle' , 'rb')
classifier = pickle.load(classifier_f)
classifier_f.close()
