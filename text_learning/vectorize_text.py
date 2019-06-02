#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText
from sklearn.feature_extraction.text import TfidfVectorizer

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []
jonesing = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    # print 'from person'
    # print (from_person)
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            # print path
            email = open(path, "r")
            # print 'start'
            # print(email)
            # print 'stop'
            ### use parseOutText to extract the text from the opened email
            parsed_text = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]

            no_signature_words = parsed_text.replace('sara', '').replace('shackleton', '').replace('chris', '').replace('germani', '').replace('  ', '')
            # print 'start'
            # print(no_signature_words)
            # print 'stop'

            ### append the text to word_data
            word_data.append(no_signature_words)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            # print 'name'
            # print(name)
            if (name is 'sara'):
                word_data.append('0')
            elif (name is 'chris'):
                word_data.append('1')
            # else:
            #     word_data.append('')
            # if word_data[temp_counter - 1][:9] == 'tjonesnsf':
            #     print (word_data[temp_counter - 1])
            #     jonesing.append("HEYOOOOOOOOOOOOOOOOOO!" + word_data[temp_counter - 1])
            #     print (temp_counter - 1)
            #     jonesing.append(temp_counter - 1)
            email.close()
            # print word_data

print "emails processed"
# i = 0
# for word_datum in word_data:
#     if word_datum[:46] == 'tjonesnsf stephani and sam need nymex calendar':
#         print word_datum
#         print i
#         # sys.exit(69)
#     i = i + 1

# print (word_data)
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


### in Part 4, do TfIdf vectorization here

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(word_data)
feature_names = vectorizer.get_feature_names()
number_of_words = len(feature_names)
# print feature_names
# print(X.shape)
# print number_of_words
# print feature_names
vocab = vectorizer.vocabulary_
# print vocab
