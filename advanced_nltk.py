import nltk


## part of speech tagging in nltk
text = "children should't drink a sugary drink"
tokens = nltk.word_tokenize(text)
print (tokens)
print("\n")
print ("nltk part of speech tagging = %s" %(nltk.pos_tag(tokens)))

## these are the modal auxiliary words provided
print ("\n")
print (nltk.help.upenn_tagset("MD"))

## pos_tagging 

print ("Part of speech tagging ")
print (nltk.pos_tag(tokens))

print ("\n")
print ("creating own Context Free Grammar")

test = "Ali  beats Bob"
test = nltk.word_tokenize(test)
## we can also define our own Context Free Grammar
grammar = nltk.CFG.fromstring("""
S  -> NP VP
VP -> V NP
NP -> 'Ali' | 'Bob'	
V  ->  'beats'		
""")
## parsing the grammar
parser =  nltk.ChartParser(grammar)

trees = parser.parse_all(test)
for tree in trees:
	print (tree)

## we have loaded 1st statement from wall street journal in corpora
 
from nltk.corpus import treebank
text = treebank.parsed_sents('wsj_0001.mrg')
print (text)
