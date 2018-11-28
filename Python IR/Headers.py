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

Titles = []
Hints = []
for count in range(10, 15):

    r = requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    Title = soup.find('h1', {'id': "firstHeading"}).text
    Hint = soup.find('a', {'class': "image"})["title"]
    if Hint is None:
        Hints.append("None")
    else:
        Hints.append(Hint)
    Titles.append(Title)
    
    print(count)
for i in Titles:
    print("\n")
    print(i)

for i in Hints:
    print("\n")
    print(i)

stop = []
with open('stopwords.json') as json_file:  
    stop = json.load(json_file)

Titles_Tokenized = []
for e in Titles:
    e = word_tokenize(e)
    final_tokenized = []
    for w in e:
        if w.lower() not in stop:
            final_tokenized.append(w)
    Titles_Tokenized.append(final_tokenized)
    
Hints_Tokenized = []
for e in Hints:
    e = word_tokenize(e)
    final_tokenized = []
    for w in e:
        if w.lower() not in stop:
            final_tokenized.append(w)
    Hints_Tokenized.append(final_tokenized)
    

ps = PorterStemmer()
Final_Titles = []
for i in Titles_Tokenized:
    temp = []
    for j in i:
        w = ps.stem(j)
        temp.append(w)
    Final_Titles.append(temp)

Final_Hints = []
for i in Hints_Tokenized:
    temp = []
    for j in i:
        w = ps.stem(j)
        temp.append(w)
    Final_Hints.append(temp)

with open('Titles.json', 'w') as outfile:  
    json.dump(Final_Titles, outfile)

with open('Hints.json', 'w') as outfile:  
    json.dump(Final_Hints, outfile)
