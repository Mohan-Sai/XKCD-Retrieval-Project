import requests
from bs4 import BeautifulSoup
from queue import Queue
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import string

Explanations=[]
for count in range(10,15):
    r=requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
    data=r.text
    soup=BeautifulSoup(data,'html.parser')
    ExplanationH2Tag = soup.find('span', {'id': "Explanation"}).parent
    TranscriptH2Tag = soup.find('span', {'id': "Transcript"}).parent
    TagsAfterExplanation = ExplanationH2Tag.find_all_next('p')
    TagsBeforeTranscript = TranscriptH2Tag.find_all_previous('p')
    ptags = [value for value in TagsAfterExplanation if value in TagsBeforeTranscript]
    s = ""
    for tag in ptags:
        s = s + tag.text
    Explanations.append(s)
for i in Explanations:
    print("\n\n\n\n")
    print(i)
