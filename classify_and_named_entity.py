import nltk
import re
from nltk.tokenize import sent_tokenize , word_tokenize , PunktSentenceTokenizer
from nltk import ne_chunk , pos_tag
from nltk.corpus import stopwords 

class classify_and_entity():

    def __init__(self):
        try:
            command = raw_input("Enter your statement = \n")
        except NameError as e :
            command = input("Enter your statement = \n  ")
        ## conversion is 
        command = "Google's office is in California"


        ## training through nltk stored file
        ## need to be replaced later
        ##Enter = raw_input("If trainging data is supplied  , Enter Yes otherwise No \n")

        ## if you want to train the model by your own training set you can provide it here

        ##    if Enter == "Yes":
        ##        train_text = state_union.raw("2005-GWBush.txt")
        ##        training = PunktSentenceTokenizer(train_text)
        ##       tokenized = training.tokenize(command)
        ##        print('You said: ' + command + '\n')
    
        tokenized = sent_tokenize(command)
        self.tokenized = tokenized

    def classify(self):
        ## in classify we classify text (command) in different categories , such as Verb , Noun , etc
        ## 1st function of class is to classifiy the words 
        ## processing the command
        for line in self.tokenized:
            token_words = word_tokenize(line)
            ## tags in the commands
            tagged = pos_tag(token_words)

            ## giving the full names of tagged POS in out program
            try :
                response  = raw_input("Do you want detailed information about the statements you passed , Enter yes \n")
            except Exception as e:
                response = input("Do you want detailed information about the statements you passed \n")
            if response == "yes":
                for i in tagged:
                    if i[1]=="NN":
                        print (i[0])
                        print ("%s = NOUN" % i[1])
                        print ("NUMBER = SINGULAR")
                        print ("\n")
                    elif i[1]=="CC":
                        print (i[0])
                        print ("%s = COORDINATING JUNCTION" % i[1])
                        print ("\n")
                    elif i[1] == "CD":
                        print (i[0])
                        print ("%s = CARDINAL DIGIT" %i[1])
                        print ("\n")
                    elif i[1] == "DT":
                        print (i[0])
                        print ("%s = DETERMINER " %i[1])
                        print ("\n")
                    elif i[1] == "EX":
                        print (i[0])
                        print ("%s = EXISTENTIAL THERE" %i[1])
                        print ("\n")
                    elif i[1] == "FW":
                        print (i[0])
                        print ("%s = FOREIGN WORRD" %i[1])
                        print ("\n")
                    elif i[1] == "IN":
                        print (i[0])
                        print ("%s = PREPOSITION / SUBORDINATING CONJUCTION " %i[1])
                        print ("\n")
                    elif i[1] == "JJ":
                        print (i[0])
                        print ("%s = ADJECTIVE , generally first degree of adjective " %i[1])
                        print ("\n")
                    elif i[1] == "JJR":
                        print (i[0])
                        print ("%s = ADJECTIVE , \nDEGREE = COMPARATIVE" %i[1])
                        print ("\n")
                    elif i[1] == "JJS":
                        print (i[0])
                        print ("%s = ADJECTIVE  , \nDEGREE = SUPERLATIVE" %i[1])
                        print ("\n")
                    elif i[1] == "LS":
                        print (i[0])
                        print ("%s = LIST MARKER" %i[1])
                        print ("\n")
                    elif i[1] == "MD":
                        print (i[0])
                        print ("%s = MODAL " %i[1])
                        print ("\n")
                    elif i[1] == "NNS":
                        print (i[0])
                        print ("%s = NOUN \nNUMBER = PLURAL" %i[1])
                        print ("\n")
                    elif i[1] == "NNP":
                        print (i[0])
                        print ("%s = NOUN \nTYPE = PROPER \nNUMBER = SINGULAR" %i[1])
                        print ("\n")
                    elif i[1] == "NNPS":
                        print (i[0])
                        print ("%s = NOUN \nTYPE = PROPER \nNUMBER = PLURAL " %i[1])
                        print ("\n")
                    elif i[1] == "PDT":
                        print (i[0])
                        print ("%s = PREDETERMINER" %i[1])
                        print ("\n")
                    elif i[1] == "POS":
                        print (i[0])
                        print ("%s = POSSESSIVE ENDING " %i[1])
                        print ("\n")
                    elif i[1] == "PRP":
                        print (i[0])
                        print ("%s = PERSONAL PRONOUN" %i[1])
                        print ("\n")
                    elif i[1] == "PRP$":
                        print ("%s = POSSESSIVE PRONOUN" %i[1])
                        print ("\n")
                    elif i[1] == "RBR":
                        print (i[0])
                        print ("%s = ADVERB \nTYPE = COMPARATIVE" %i[1])
                        print ("\n")
                    elif i[1] == "RBS":
                        print (i[0])
                        print ("%s = ADVERB \nTYPE = SUPERLATIVE" %i[1])
                        print ("\n")
                    elif i[1] == "RB":
                        print (i[0])
                        print ("%s = ADVERB" %i[1])
                        print ("\n")
                    elif i[1] == "RP":
                        print (i[0])
                        print ("%s = PARTICLE " %i[1])
                        print ("\n")
                    elif i[1] == "TO":
                        print (i[0])
                        print ("%s = TO " %i[1])
                        print ("\n")
                    elif i[1] == "UH":
                        print (i[0])
                        print ("%s = INTERJECTION" %i[1])
                        print ("\n")
                    elif i[1] == "VB":
                        print (i[0])
                        print ("%s = VERB \nFORM = BASE" %i[1])
                        print ("\n")
                    elif i[1] == "VBD":
                        print (i[0])
                        print ("%s = VERB \nFORM = PAST TENSE" %i[1])
                        print ("\n")
                    elif i[1] == "VBG":
                        print (i[0])
                        print ("%s = VERB \nFORM = PRESENT PARTICLE" %i[1])
                        print ("\n")
                    elif i[1] == "VBN":
                        print (i[0])
                        print ("%s = VERB \nFORM = PAST PARTICLE" %i[1])
                        print ("\n")
                    elif i[1] == "VBP":
                        print (i[0])
                        print ("%s = VERB \nFORM = PRESENT" %i[1])
                        print ("\n")
                    elif i[1] == "VBZ":
                        print (i[0])
                        print ("%s = VERB , 3rd Person" %i[1])
                        print ("\n")                    
                    elif i[1] == "WDT":
                        print (i[0])
                        print ("%s = wh-DETERMINER " %i[1])
                        print ("\n")
                    elif i[1] == "WP":
                        print (i[0])
                        print ("%s = wh-PRONOUN" %i[1])
                        print ("\n")
                    elif i[1] == "WP$":
                        print (i[0])
                        print ("%s = wh-POSSESSIVE PRONOUN " %i[1])
                        print ("\n")
                    elif i[1] == "WRB":
                        print (i[0])
                        print ("%s = wh-ADVERB " %i[1])
                        print ("\n")
                    elif i[1] == ".":
                        print (i[0])
                        print ("%s = PUNCTUATION " %i[0])
            else :
                print (tagged)


    ## named entity recoginition in text
    ## basic idea is to pull out "entities" like people , places , things , etc

    def entity_recog(self):
        
        try :
            for line in self.tokenized:
                words = word_tokenize(line)
                ## finding tags in the commands
                tagged = pos_tag(words)
                named_entity_false = ne_chunk(tagged , binary = True )                                    
                named_entity_true = ne_chunk(tagged , binary = False)
                ## finding named entity in the tagged words
                label = raw_input("do you want specific names on your entities if yes enter 'yes'\nfor just entity recoginition enter 'no' \nfor both information 'both'\n")
                if label == "yes" or label == "Yes":
                    print (named_entity_true)
                    named_entity_true.draw()
                elif label == 'no':
                    print (named_entity_false)
                    named_entity_false.draw()
                elif re.search(r'[A-Za-z]*both[A-Za-z]*' , label):
                    print ("named_entity_false")
                    print (named_entity_false)
                    named_entity_true.draw()
                    print ("named_entity_true")
                    print (named_entity_true)
                    named_entity_false.draw()

        except Exception as e:
            print (e)
    
obj_classify_and_entity = classify_and_entity()

#obj_classify_and_entity.classify()
obj_classify_and_entity.entity_recog()






## list of short form that are used in Parts Of Speec tagging or pos_tag()
"""
POS tag list:
CC  coordinating conjunction
CD  cardinal digit
DT  determiner
EX  existential there (like: "there is" ... think of it like "there exists")
FW  foreign word
IN  preposition/subordinating conjunction
JJ  adjective   'big'
JJR adjective, comparative  'bigger'
JJS adjective, superlative  'biggest'
LS  list marker 1)
MD  modal   could, will
NN  noun, singular 'desk'
NNS noun plural 'desks'
NNP proper noun, singular   'Harrison'
NNPS    proper noun, plural 'Americans'
PDT predeterminer   'all the kids'
POS possessive ending   parent\'s
PRP personal pronoun    I, he, she
PRP$    possessive pronoun  my, his, hers
RB  adverb  very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP  particle    give up
TO  to  go 'to' the store.
UH  interjection    errrrrrrrm
VB  verb, base form take
VBD verb, past tense    took
VBG verb, gerund/present participle taking
VBN verb, past participle   taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present  takes
WDT wh-determiner   which
WP  wh-pronoun  who, what
WP$ possessive wh-pronoun   whose
WRB wh-abverb   where, when
"""