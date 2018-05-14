## Using wordnet 
## It is a lexical database for english language , which is used as a part of NLTK corpus , 
## We can use wordnet alongside the NLTK module to find the meaning , synonyms , antonyms , etc
## of a word


from nltk.corpus import wordnet

## for example take word "program"

## synset means set of synonyms

words = "program"
for word in wordnet.synsets(words):
	print (word)

set_words = wordnet.synsets(words)

## acessing a specific word in the synset of a word
print ("\n\nworking with a specific word in the synset ")
print (set_words[1])
print ("set_words[1].name() = %s"%(set_words[1].name()))

print ("\n")
print ("these are the meanings as per wordnet")
print ("set_words[1].lemmas() = %s"%(set_words[1].lemmas()))

## getting just the word
print ("\n")
print ("just getting the  word")
print ("set_words[1].lemmas()[1].name() = %s "%(set_words[1].lemmas()[1].name()))

print ("\n")
print ("these are the defintion of words as per the dictionary of wordnet")
print ("'%s'"%(set_words[1].definition()))


#print (set_words[9].lemmas())
## we have program with 2 versions one is "program" other is "programme"
## a lemma is wordnet's version of a entry in a dictionary 
## for example a "bank" in canonical form have a meaning "bank" but
## there would be separate lemmas for nouns meaning "financial institution" and "side of the river" , etc

## finding a synonym and antonym of a word 
synonym , antonym = [] , []

print ("\n")
## getting the synonym set for the word "good"

"""print (wordnet.synsets("good"))"""
set_words =  wordnet.synsets("good")
print (set_words[1].name())
print (set_words[1].lemmas())
print ("\n\n")
for words in set_words:
	for lemma in words.lemmas():
		## this gives the synonym for good
		synonym.append(lemma.name())
		if lemma.antonyms():
			#print (lemma.antonyms())
			#print (lemma.antonyms()[0])
			#print (lemma.antonyms()[0].name()))
			antonym.append(lemma.antonyms()[0].name())

print (synonym)
print ("\n")
print (antonym)


## Now we need to compare the similarity of two words using Wu and Palmer method

w1 =  wordnet.synset('ship.n.01')
w2 =  wordnet.synset("boat.n.01")
print ("the similarity between two words %s and %s is " % (w1 ,w2))
print (w1.wup_similarity(w2))
print ("\n")

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print ("the similarity between two words %s and %s is " % (w1 ,w2))
print (w1.wup_similarity(w2))
print (w2.wup_similarity(w1))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")
print ("the similarity between two words %s and %s is " % (w1 ,w2))
print (w1.wup_similarity(w2))
