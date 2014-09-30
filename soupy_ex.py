# !/usr/bin/env python

# To Do:
# 
# Create a function to BS a user-specified html file.
# 

from bs4 import BeautifulSoup                      #Imports BeautifulSoup


souped = BeautifulSoup(open("reddit.html"))
""" This command creates the html document object. This will be used throughout
the rest of this file. For now, the file is a reddit front page. """

souped.title
""" This command returns the document's title tag and the contents thereof """

title_contents = souped.title.contents
""" Extracts the contents of each title tag and assigns them to a list. """


[tag.name for tag in souped.find_all(True)]

""" This list comprehension finds all the tag names in 'souped' and outputs them
as a list.  I <3 list comprehensions because they can take the place of for
loops to some degree.  Consider the following: """

result = []        # Empty list to collect the results

for tag in souped.find_all(True):
    result.append(tag.name) # Append each tag to result

""" The list comprehension and empty list + for loop have the same result,
but  one takes quite a bit less typing """

def get_tags(souped):
    
    each_tag = [tag.name for tag in souped.find_all(True)]
    tag_set  = list(set(each_tag))

return tag_set



    
    


