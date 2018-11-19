import requests
from bs4 import BeautifulSoup
from queue import Queue
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import string

#get transcript
#get comics from all major characters
#see the transcript terms manually and see if its accurate
#tf*idf
#TD Matrix
#SVD of Term Document Matrix
#Inverted index of SVD
#Recommendation system 


# Getting the text from the website
transcript=[]
for count in range(10,15):
    r=requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
    data=r.text
    soup=BeautifulSoup(data,'html.parser')
    transcript.append(soup.find("dd").string)
#If we are taking dd as the reference tag, we are losing some (very low) information. But this is 
#resulting in better formatted text.
print(transcript)

# Setting the stopwords
stop= set(stopwords.words('english')) | set(string.punctuation)
stop.add('A')
print(stop)
print(len(stop))

# tokenize the text and removing the stopwords
final_transcript=[]
for j in transcript:
    tokens=nltk.word_tokenize(j)
    for i in tokens:
        if i not in stop:
            final_transcript.append(i)
print(final_transcript)

#Calculating the tf
cnt=Counter()
for i in final_transcript:
    for i in transcript:
        count=len()
    for a in i:
        cnt[a]+=1
        print(cnt[a])
        for b in i:
            tf=cnt[b]/count
            print(a,cnt[a],tf)

#Calculating the idf values
"""
# Trying to create the  inverted index
for i in tokens:
    words= []
    words.append(transcript)
"""