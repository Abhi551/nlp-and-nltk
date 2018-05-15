import nltk
from nltk.book import *

## this import all the text and corpora in the nltk module
print (texts())

## there are 9 corpora in the book
print ("\n")
print (text1)
print ("\n")

## printing the sentences 
print (sents())
print ("\n")

## print a particular sentence
print (sent7)

print ("len of text1 = %d" %(len(text1)))
print ("len of sentence1 in text1 = %d " %(len(sent1)))

## concepts of sets in python is used quite often in nlp and nltk 
## as their feature are quite fitting in text minning

## finding unique words 
## sets in python have same features as in Mathematics
## as sets in Mathematics have no repeated elemnts 

print ("\n set and list of words")
print (sent7)
print ("length of list = %d " %len(sent7))
print (set(sent7))
print ("length of set = %d " %(len(set(sent7))))

## thus using sets reduces repeatedly occuring words in texts
print ("print the number of words in text1")
print (len(text1))
print ("print  the number of unique words in text1")
print (len(set(text1)))

## this prints first distinct 20 letters in the file 
print (list(set(text1))[:20])

## calculate the frequency of a particular words in the text
## FreqDist is similar to dictionaries thus we can see all the data 
## using items ,values and keys as in dicts

dist = FreqDist(text1)
## this gives all the different keys
print (len(dist.keys()))
print (dist.keys())

print (type(dist))
## values of different words
print (dist.values())
 
## items 
print (dist.items())

## defining the repeated words , as per our definition 
## all those words which appear more than 50 and have length more than 5

words =  [word for word in dist if len(word) > 4 and dist[word] > 50]
print (words)


## stemming and lemmatization has already been implemented 

