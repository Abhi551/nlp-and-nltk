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

## list of short form that are used in Parts Of Speec tagging or pos_tag()
"""
POS tag list:
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent\'s
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
"""