import requests
from bs4 import BeautifulSoup
from queue import Queue
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import string
import json
from nltk.stem import PorterStemmer
from collections import Counter
import math
import decimal

Explanations = []
with open('ExplNatural.json') as json_file:  
    Explanations = json.load(json_file)

stop = []
with open('stopwords.json') as json_file:  
    stop = json.load(json_file)

Words = []
for key in Explanations.keys():
    Words.append(word_tokenize(Explanations[key]))

Tokens = []
for l in Words:
    for w in l:
        Tokens.append(w)
Final_Tokens = []
for w in Tokens:
        if w.lower() not in stop:
            Final_Tokens.append(w)

Cnt = Counter(Final_Tokens)
with open('Counter.json', 'w') as outfile:  
    json.dump(Cnt, outfile, indent=4)
for k in Cnt:
    if Cnt[k] > 300:
        stop.append(k)

with open('stopwords.json', 'w') as outfile:  
    json.dump(stop, outfile)