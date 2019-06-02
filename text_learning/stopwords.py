#!/usr/bin/python

from nltk.corpus import stopwords
from nltk.downloader import download

download('all', halt_on_error=False)
sw = stopwords.words("english")
count = len(sw)
# print(sw)
