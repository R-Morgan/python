#!/usr/bin/env python

""" Before playing with this code, I'd *highly* recommend installing python 3
and bpython, a very slick python interpreter that will make trying out the code
very easy."""

import nltk, re, pprint           # imports several modules for text processing

from nltk import word_tokenize, sent_tokenize
""" The command imports some specific nltk submodules to get the raw text into 
a more useful form  """


from urllib import request
""" These commands are taken from the NLTK book found at 
http://www.nltk.org/book/ch03.html and modified slightly. The URL in the above 
code points to a plaintext version of Doyal's The Adventures of Sherlock
Holmes. This imports a module to retrieve files from the internet. """

url = "http://www.gutenberg.org/files/1661/1661.txt"

""" This assigns the URL string to a variable. """

response = request.urlopen(url)
""" This executes a command to retrieve the file at that URL and stores the 
result in a variable name. """

raw = response.read().decode('utf8')
""" This parses the result into some raw text. The utf8 argument string in the
'decode()' portion refers to the character encoding. """

type(raw)                         # What does this command tell you?

raw[:80]                          # What happens here?  What do  the '\r\n' 
                                  # sequences mean?

len(raw)                          # This tells you the character length of the
                                  # string

##############################################################################

""" Now we need to do something with the this raw text, because it's one long
string which is hard to work with."""

sentences = sent_tokenize(raw)    # Divies raw string into a list of sentences.

sentences[1]                      # What happens with this command?

sentences[3:6]                    # What about this?

sentsdivided = []                 # Instantiates an empty list to store results
                                  # of for loop.

for s in sentences:
    sentsdivided.append(word_tokenize(s))
        
""" This is a basic python for loop. 's' is a variable that represents one unit
in the list sentences. This placeholder variable could be named something else,
like sent.  

What the body of the for loop does is tokenises each s, then appends that to the
list sentsdivided."""        

###############################################################################
""" Now that we've experiemented with for loop iteration, let's definite a
function to calculate the mean sentence length. We will build this up modularly
from smaller functions"""

def normtext (sents):

""" Defines function name and argument structure.  The function takes one
argument called 'sent_tokens', which should a list of sentences."""

    result = []        
""" Initialises an empty list to store the output of the for loop  """

    for s in sents:
        lst = [w.lower() for w in s if w.isalpha()]
        """ List comprehension. w.lower() is executed 
        for each w in s, provided that w.isalph() 
        evaluates to True. """

        result.append(lst)
        """ Appends lst to the the empty vector above"""

   return(result) 
   
def meanlength(normed_sents):

    lengths =  [len(sent) for sent in normed_sents] # Number of words in each
                                                    # sentence

    words = sum(lengths)                            # Sum of all lengths

    sentences = len(normed_sents)                   # Number sentences

    mean = (words / sentences)

    return(mean)
