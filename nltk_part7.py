## named entitiy recognition 
## In general , named entitiy is a real world object such as persons , locations , products , etc
## that can be denoted with a proper name 
## the basic idea is to pull out "entities" like people , places , thing ,etc
## here are some named entity

"""
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
"""
import nltk 

from nltk import word_tokenize , pos_tag , ne_chunk
from nltk.corpus import state_union 
from nltk.tokenize import PunktSentenceTokenizer
#from nltk import

train_text =  state_union.raw("2005-GWBush.txt")
sample_text =  state_union.raw("2006-GWBush.txt")

## training our own tokenizer based on our training data
custom_tokenizer = PunktSentenceTokenizer(train_text)

## using our custom_tokenizer on sample text 
## custom_tokenizer gives output 'similar'  to sent_tokenize 

tokenized = custom_tokenizer.tokenize(sample_text)

## create a function for finding named entities in our tokenized data

def find_ent():

	try :
		for line in tokenized[:5]:
			words =  word_tokenize(line)
			## finding tags on words for each word in the line
			tagged = pos_tag(words)
			## it gives specific named entity with label on it
			named_entity = ne_chunk(tagged)
			named_entity.draw()

			## tagging the words 
			tagged = pos_tag(words)
			## it only specifies whether or not the word is a named entity 
			named_entity =  ne_chunk(tagged , binary = True)
			named_entity.draw()

	except Exception as e:
		print (e)

find_ent()