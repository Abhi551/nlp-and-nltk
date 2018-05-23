## both nltk and textblob are part of NLP
## but textblob is design to get more benifits which nltk doesn't provide 
## it is actually built on top of NLTK , i.e. it is a superset of of NLTK.s API

import textblob
from textblob import TextBlob , Word 

text = '''
	The titular threat of The Blob has always struck me as the ultimate movie
	monster: an insatiably hungry, amoeba-like mass able to penetrate
	virtually any safeguard, capable of--as a doomed doctor chillingly
	describes it--"assimilating flesh on contact.
	Snide comparisons to gelatin be damned, it's a concept with the most
	devastating of potential consequences, not unlike the grey goo scenario
	proposed by technological theorists fearful of
	artificial intelligence run rampant.
	'''

## creating a textblob
text = TextBlob(text)

## gives the tags which are also know POS_tags in nltk
tags = text.tags
print ("print all the tags ")
print (tags)

## this will provide noun phrases only from the text
print ("\nonly noun phrases ")
print (text.noun_phrases)

## doing the sentiment anlaysis on text 
## Sentiment returns a namedtuple of form Sentiment(polarity , subjectivity)
## polarity gives score in [-1.0 , 1.0]
## subjectivity gives between [0 , 1.0] , 0 means very objective and 1 is very subjective 
print (text.sentiment)

## tokenization 
## equivalent to nltk.word_tokenize 
print ("\n tokenization by words")
print (text.words)
print ("\n tokenization by sentences")
## equivalent to nltk.sent_tokenize
print (text.sentences)

## word inflection and Lemmatization 

print (text.words[2].pluralize())
print (type(text.words[2]))
print (type(Word('consequences')))
print (Word("consequences").singularize())

## we can apply these operations to complete list of words

sents  = "hell choco pen"
sents  =  TextBlob(sents)
print (sents.words.pluralize())

## lemmatization works as it works in NLTK
print (Word('octopi').lemmatize())
print (Word('went').lemmatize('v'))

## spelling corrections 

print ("The incorrect sentences")
print (text)
text =  TextBlob("I havv pein in back")
print ("after the corrections ")
print (text.correct())

## getting the frequecy of word

monty = TextBlob("""We are no longer the Knights who say Ni . We are now the Knights who say Ekki ekki ekki PTANG.""")
print (monty.words.count('ekki'))
print (monty.words.count('ekki' , case_sensitive = True))

