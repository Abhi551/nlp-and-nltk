import nltk 
import random 
import pandas as pd
import csv
import numpy as np

from nltk.corpus import movie_reviews


## both statements are equivalent

'''
documents = []
documents = [(list (movie_reviews.words(fileid)) , category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]
#print (len(documents))
'''

documents = []
## the statements are eqiuvalent
for category in movie_reviews.categories():			## there are two categories
													## print (category)
	for fileid in movie_reviews.fileids(category):	## every file in the folder movie_reviews is given a fileid or name
													##print (fileid)
		documents.append([movie_reviews.words(fileid) , category])
	
## so we created list of tuple having fileid and category in it 
## shuffling the organised data
random.shuffle(documents)

print (documents[1])

list_file_words = []
all_words  = []

## collecting all the words in all file in the movie_reviews folder

for fileid in movie_reviews.fileids():
	## to get all words in a particular file
	#file_words.append(movie_reviews.words(fileid))
	list_file_words.append(len(movie_reviews.words(fileid)))


list_file_words = np.array(list_file_words)
## checking whether sum calulated after going through all the words is same as
## calculate by other method
print (list_file_words.sum())


## to get all the words in movie_reviews

for word in movie_reviews.words():
	all_words.append(word)

print (len(all_words))

all_words = []

for word in movie_reviews.words():
	all_words.append(word)
print (len(all_words))

## using FreqDist , gives dict type structure in NLTK for words along with their count

all_words = nltk.FreqDist(all_words)
print (all_words.items())
## we can also use different operation as .keys() and .values
## finding the frequency of a particular word stupid in all_words
print (all_words[u'stupid'])




