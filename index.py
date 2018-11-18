import requests
from bs4 import BeautifulSoup
from queue import Queue
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import string

# Getting the text from the website
transcript=[]
for count in range(10,15):
    r=requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
    data=r.text
    soup=BeautifulSoup(data,'html.parser')
    transcript.append(soup.find("dd").string)
#If we are taking dd as the reference tag, we are losing some (very low) information. But this is 
# resulting in better formatted text.
#print(transcript)

# Setting the stopwords
stop= set(stopwords.words('english')) | set(string.punctuation)
stop.add('A')

# tokenize the text and removing the stopwords
final_transcript=[]
for j in transcript:
    tokens=nltk.word_tokenize(j)
    for i in tokens:
        if i not in stop:
            final_transcript.append(i)

print(final_transcript)
# #Calculating the tf
# cnt=Counter()
# for i in transcript:
#     count=len(i)
#     for a in i:
#         # how many that word occurs divided by total no of words
#         cnt[a]+=1
#         tf=cnt['a']/count
#         print(tf)
# #Calculating the idf
        

"""
# Trying to create the  inverted index
for i in tokens:
    words= []
    words.append(transcript)
"""