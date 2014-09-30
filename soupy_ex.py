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



