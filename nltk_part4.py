## introduction to speech tagging
## speech tagging means labelling the words in a sentence  as 
## nouns , adjectives , pronouns , adverbs  , etc

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer , sent_tokenize
from nltk.tokenize import word_tokenize

## loading a existing file from nltk using state_union

#print (state_union.raw("2005-GWBush.txt"))

train_text =  state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

## training the Punkt tokenizer 
training =  PunktSentenceTokenizer(train_text)

## Punkt Sentence Tokenizer  , is an abstract class for default sentence tokenizer i.e sent_tokenize 
## but they actually work in different manner (checked)

## this tokenizer divides a text into a list of sentences by using an unsupervised algorithm 
## to build a model for abbrev. words , collocations , and words that start sentences which need
## to be trained with large amount of data before using 


##  tokenizing the data using tokenize 
tokenized  =  training.tokenize(sample_text)

#print (len(tokenized))
#print (len(sent_tokenize(sample_text)))
#print (tokenized == sent_tokenize(sample_text))

#print (tokenized[1])
#print (sent_tokenize(sample_text)[1])
#print (sent_tokenize(sample_text)[1] == tokenized[1] )

def process_content():
	try :
		for line in tokenized[:5]:
			# using word_token for each line
			words =  word_tokenize(line)
			tagged = nltk.pos_tag(words)
			#print (words)
			print (tagged)
	except Exception as e:
		print (e)


process_content()

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