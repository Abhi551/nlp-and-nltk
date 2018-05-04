from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

sen =  "this is an example showing off stop word filtration ."

## stop words in english
## there are certain words in any language with no meaning that can removed without affecting the sense of 
## the statements and these are pre defined in nltk given by nltk.corpus.stopwords.word("english") for english

stop_words = (stopwords.words("english"))
#print (stop_words)

## tokenizeing by words

token_word = word_tokenize(sen)
print (token_word)

for word in token_word :
	if word not in stop_words:
		print (word)