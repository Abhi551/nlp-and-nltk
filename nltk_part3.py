## stemming the words such as "going"  stemmed to "go"
##							  "riding" stemmed to "ride"
##							  "stemming" to "stem"					

## we use here stemming algorithm named  PorterStemmer

## Lemmatizing Words Using WordNet
## lemmatizing is similar to stemming but lemmatizing gives better real words 

from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()

examples = ["do" , "doing" , "done" , "hatching" , "hatched" , "catchy" , "catched" , "catching" ]
list_ex = [ps.stem(word) for word in examples]

print (examples)
print (list_ex)

sentence = """It is important to by very pythonly while you are pythoning with python. 
					All pythoners have pythoned poorly at least once."""

## using word token 
token_words  = word_tokenize(sentence)

## removing the stop word
stop_words = stopwords.words("english")
final_words = [word for word in token_words if word not in stop_words ]

## stemming the word from the token and final_words
stemmed_token = [ps.stem(word) for word in token_words]
stemmed_final = [ps.stem(word) for word in final_words]

print "\ntoken words from the sentence \n",token_words
print "\nremoved words from the sentence \n" , final_words
print "\n stemmed words from tokens \n " , stemmed_token
print "\n stemmed words from final words \n " , stemmed_final

## using WordNetLemmatizer
## lemmatizing doesn't magically determine POS tag into account before stemming 
lemmatizer = WordNetLemmatizer()
print (lemmatizer.lemmatize("playing" , "v"))
print (lemmatizer.lemmatize("doing" , "v"))
print (lemmatizer.lemmatize("catched" , "v"))