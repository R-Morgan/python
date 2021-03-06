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
        
        
