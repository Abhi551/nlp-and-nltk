## till now we combined NN (nouns) with other phrases and used regex to do that 
## but in chunking we get some extra results also ,  
## chinking is used to get better results 
## In chinking we chunks from the output we get after chunking

import nltk 
from nltk import word_tokenize  , pos_tag
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text =  state_union.raw("2005-GWBush.txt")
sample_text =  state_union.raw("2006-GWBush.txt")

## tokeninzing word from the train_text

custom_tokenizer = PunktSentenceTokenizer(train_text)

## tokenizing the data of sample_text 
tokeninzed =  custom_tokenizer.tokenize(sample_text)
#print (tokeninzed)

def process_content():
	try :
		for line in tokeninzed[:5]:
			## tokenizing by word each line
			words = word_tokenize(line)
			## giving the tag to each word in list of words 
			tagged = pos_tag(words)

			## chunking 
			## include everything while chunking i.e. {}
			## chinking 
			## excludes every chunk that has either VB , IN , DT , TO in it
			chunk =  r""" Chunk:{<.*>+}
							}<VB.?|IN|DT|TO>+{"""

			## for the graph or drawing the graph
			## parsing 
			chunkParser =  nltk.RegexpParser(chunk)
			chunked  = chunkParser.parse(tagged)

			chunked.draw()
	except  Exception as  e:
		print (e)

process_content()
