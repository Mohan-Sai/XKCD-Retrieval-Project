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
# Explanations = []
# with open('ExplNatural.json') as json_file:  
#     Explanations = json.load(json_file)

# for count in range(2071, 2076):
#     r = requests.get("http://web.archive.org/web/20170828215548/http://www.explainxkcd.com:80/wiki/index.php/"+str(count))
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
# with open('ExplNatural2.json', 'w') as outfile:  
#     json.dump(Explanations, outfile, indent=4)
# for count in range(10,15):
#     r = requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
#     data = r.text
#     soup = BeautifulSoup(data, 'html.parser')
#     tags = soup.find_all('a', {"class" : "extiw"})
#     print(tags)

# print(Explanations)
# stop = []
# with open('stopwords.json') as json_file:  
#     stop = json.load(json_file)

# Explanations_Tokenized = {}
# for e in Explanations:
#     t = word_tokenize(Explanations[e])
#     f = list(set(t))
#     print(str(e) + "\t" + str(len(t)) + "\t" + str(len(f)))
#     final_tokenized = []
#     for w in f:
#         if w.lower() not in stop:
#             final_tokenized.append(w)
#     Explanations_Tokenized[e] = final_tokenized


# ps = PorterStemmer()
# Final_Explanations = {}
# for i in Explanations_Tokenized:
#     temp = []
#     for j in Explanations_Tokenized[i]:
#         w = ps.stem(j)
#         temp.append(w)
#     Final_Explanations[i] = (temp)
# with open('FinalExplanations.json', 'w') as outfile:  
#     json.dump(Final_Explanations, outfile, indent=4)
# with open('Explanations.json') as json_file:  
#     Final_Explanations = json.load(json_file)

# transcripts = []
# with open('Transcripts.json') as json_file:  
#     transcripts = json.load(json_file)


# Titles = []
# with open('Titles.json') as json_file:  
#     Titles = json.load(json_file)

# Hints = []
# with open('Hints.json') as json_file:  
#     Hints = json.load(json_file)

# Final_Tokens = []
# for i in range(0, 5):
#     Final_Tokens.append(Final_Explanations[i] + transcripts[i] + Titles[i] + Hints[i])
FinalExplanations = {}
with open('FinalExplanations.json') as json_file:  
    FinalExplanations = json.load(json_file)

# Getting All unique tokens
Unique_tokens = []
for i in FinalExplanations:
    for term in FinalExplanations[i]:
        Unique_tokens.append(term)
Unique_tokens = list(set(Unique_tokens))

# Calculating TF
TFMatrix = {}
# cnt = {}
# for i in FinalExplanations:
#     cnt[i] = (Counter(FinalExplanations[i]))
    
# for token in Unique_tokens:
#     temp = []
#     for i in FinalExplanations:
#         temp.append(cnt[i][token])
#     TFMatrix[token] = temp
with open('TFMatrix.json') as json_file:  
    TFMatrix = json.load(json_file)
# Calculating IDF
IDFMatrix = {}
# for token in Unique_tokens:
#     Counter = 0
#     for i in FinalExplanations:
#         if token in FinalExplanations[i]:  
#             Counter = Counter + 1
#     IDFMatrix[token] = math.log10(2073/Counter)
#     print(IDFMatrix[token])
with open('IDFMatrix.json') as json_file:  
    IDFMatrix = json.load(json_file)
# Calculating TF-IDF
TFIDFMatrix = {}
for token in Unique_tokens:
    temp = {}
    temp2 = {}
    for i in FinalExplanations:
        temp[int(i)] = (TFMatrix[token][int(i)-1] * IDFMatrix[token])
    for j in temp:
        if(temp[j] != 0):
            temp2[j] = temp[j]
    TFIDFMatrix[token] = temp2

# with open('TFMatrix.json', 'w') as outfile:  
#     json.dump(TFMatrix, outfile, indent=4)

# with open('IDFMatrix.json', 'w') as outfile:  
#     json.dump(IDFMatrix, outfile, indent=4)

with open('TFIDFMatrix1.json', 'w') as outfile:  
    json.dump(TFIDFMatrix, outfile, indent=4)
