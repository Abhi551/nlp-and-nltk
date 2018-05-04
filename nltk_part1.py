import nltk 

## tokenizing - word tokenizers and sentence tokenizers
# word , separates by word
# sentence , separates by sentence

## lexicon and corporas 
 
## corpora - body of text
## lexicon - word and their meanings

from nltk.tokenize import sent_tokenize , word_tokenize 

sentence =  """ Hello Mr. Patel  , how are you  ? Hope you are fine .
			See you seen . """

## same can be done by regex also

## splitting by nltk
print (word_tokenize(sentence))
print (sent_tokenize(sentence))

for word in word_tokenize(sentence):
	print (word)
