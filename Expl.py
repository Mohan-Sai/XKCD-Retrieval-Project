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
Explanations = []
for count in range(10, 15):

    r = requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    ExplanationH2Tag = soup.find('span', {'id': "Explanation"}).parent
    TranscriptH2Tag = soup.find('span', {'id': "Transcript"}).parent
    TagsAfterExplanation = ExplanationH2Tag.find_all_next('p')
    TagsBeforeTranscript = TranscriptH2Tag.find_all_previous('p')
    ptags = [value for value in TagsAfterExplanation if value in TagsBeforeTranscript]
    s = ""
    for tag in ptags:
        s = s + tag.text
    Explanations.append(s)
    print(count)

stop = []
with open('stopwords.json') as json_file:  
    stop = json.load(json_file)

Explanations_Tokenized = []
for e in Explanations:
    e = word_tokenize(e)
    final_tokenized = []
    for w in e:
        if w.lower() not in stop:
            final_tokenized.append(w)
    Explanations_Tokenized.append(final_tokenized)
    print("\n")        
    print(len(e))
    print("    ")
    print(len(final_tokenized))

ps = PorterStemmer()
Final_Explanations = []
for i in Explanations_Tokenized:
    temp = []
    for j in i:
        w = ps.stem(j)
        temp.append(w)
    Final_Explanations.append(temp)

for i in Final_Explanations:
    print("\n\n\n\n")
    print(i)
