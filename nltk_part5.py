## chunking 
## main goal of chunking is to group into "noun  phrases"
## "noun phrases" are  phrases that contains a  noun with some other descirptive word as verb , adverb , etc

import nltk 
from nltk import word_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer 

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

## train through 2005 year data

trainer = PunktSentenceTokenizer(train_text)

## similar to sentence tokenizer
## but here we train our own model every time

tokenized = trainer.tokenize(sample_text)

##  in order to chunk we use regular expression to give the exact patter to be matched in the text

def process_content():
	try :
		for line in tokenized :
			words = word_tokenize(line)
			tagged = nltk.pos_tag(words)
			## r stands for raw text
			chunk = r""" Chunk :{<RB.?>*<VB.?>*<NNP>+<NN>} """
			## parsing the chunk into regex grammar
			chunkparse = nltk.RegexpParser(chunk)
			chunked = (chunkparse.parse(tagged))
			for subtree in chunked.subtrees(filter = lambda t : t.label() == "Chunk" ):
				subtree.draw()
	except Exception as e :
		print (e)

process_content()







