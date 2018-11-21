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
# Explanations = []
# for count in range(10, 15):

#     r = requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
#     data = r.text
#     soup = BeautifulSoup(data, 'html.parser')
#     ExplanationH2Tag = soup.find('span', {'id': "Explanation"}).parent
#     TranscriptH2Tag = soup.find('span', {'id': "Transcript"}).parent
#     TagsAfterExplanation = ExplanationH2Tag.find_all_next('p')
#     TagsBeforeTranscript = TranscriptH2Tag.find_all_previous('p')
#     ptags = [value for value in TagsAfterExplanation if value in TagsBeforeTranscript]
#     s = ""
#     for tag in ptags:
#         s = s + tag.text
#     Explanations.append(s)
#     print(count)

# stop = []
# with open('stopwords.json') as json_file:  
#     stop = json.load(json_file)

# Explanations_Tokenized = []
# for e in Explanations:
#     e = word_tokenize(e)
#     final_tokenized = []
#     for w in e:
#         if w.lower() not in stop:
#             final_tokenized.append(w)
#     Explanations_Tokenized.append(final_tokenized)

# ps = PorterStemmer()
Final_Explanations = []
# for i in Explanations_Tokenized:
#     temp = []
#     for j in i:
#         w = ps.stem(j)
#         temp.append(w)
#     Final_Explanations.append(temp)

with open('Explanations.json') as json_file:  
    Final_Explanations = json.load(json_file)

transcripts = []
with open('Transcripts.json') as json_file:  
    transcripts = json.load(json_file)


Titles = []
with open('Titles.json') as json_file:  
    Titles = json.load(json_file)

Hints = []
with open('Hints.json') as json_file:  
    Hints = json.load(json_file)

Final_Tokens = []
for i in range(0, 5):
    Final_Tokens.append(Final_Explanations[i] + transcripts[i] + Titles[i] + Hints[i])

# Getting All unique tokens
Unique_tokens = []
for documents in Final_Tokens:
    for term in documents:
        Unique_tokens.append(term)
Unique_tokens = list(set(Unique_tokens))

# Calculating TF
TFMatrix = {}
cnt = []
for i in range(0,5):
    cnt.append(Counter(Final_Tokens[i]))
    
for token in Unique_tokens:
    temp = []
    for i in range(0,5):
        temp.append(cnt[i][token])
    TFMatrix[token] = temp

# Calculating IDF
IDFMatrix = {}
for token in Unique_tokens:
    Counter = 0
    for i in range(0,5):
        if token in Final_Tokens[i]:
            Counter = Counter + 1
    IDFMatrix[token] = math.log10(decimal(5)/decimal(Counter))

for i in IDFMatrix.keys():
    print(i + "\t" + IDFMatrix[i] + "\n")




