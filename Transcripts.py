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

#get transcript
#get comics from all major characters
#see the transcript terms manually and see if its accurate
#tf*idf
#TD Matrix
#SVD of Term Document Matrix
#Inverted index of SVD
#Recommendation system

# Getting the text from the website
transcript = []
for count in range(10, 15):
    r = requests.get("https://www.explainxkcd.com/wiki/index.php/"+str(count))
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    ExplanationH2Tag = soup.find('span', {'id': "Transcript"}).parent
    if ExplanationH2Tag is None:
        transcript.append("none")
        continue
    TranscriptH2Tag = soup.find('span', {'id': "Trivia"})
    if TranscriptH2Tag is None:
        TranscriptH2Tag = soup.find('span', {'id': "Discussion"})
    else:
        TranscriptH2Tag = TranscriptH2Tag.parent
    TagsAfterExplanation = ExplanationH2Tag.find_all_next('dd')
    TagsBeforeTranscript = TranscriptH2Tag.find_all_previous('dd')
    ptags = [value for value in TagsAfterExplanation if value in TagsBeforeTranscript]
    s = ""
    for tag in ptags:
        s = s + tag.text
    transcript.append(s)
    print(count)
#If we are taking dd as the reference tag, we are losing some (very low) information. But this is
#resulting in better formatted text.
# for i in transcript:
#     print("\n")
#     print(i)

# Setting the stopwords
stop = []
with open('stopwords.json') as json_file:
    stop = json.load(json_file)

# # tokenize the text and removing the stopwords
transcript_tokenized = []
for j in transcript:
    temp = []
    tokens = nltk.word_tokenize(j)
    for i in tokens:
        if i not in stop:
            temp.append(i)
    transcript_tokenized.append(temp)
# print(transcript_tokenized)
ps = PorterStemmer()
final_transcript = []
for i in transcript_tokenized:
    temp = []
    for j in i:
        w = ps.stem(j)
        temp.append(w)
    final_transcript.append(temp)

with open('Transcripts.json', 'w') as outfile:  
    json.dump(final_transcript, outfile)

# #Calculating the tf
# cnt=Counter()
# for i in transcript_tokenized:
#     for i in transcript:
#         count=len()
#     for a in i:
#         cnt[a]+=1
#         print(cnt[a])
#         for b in i:
#             tf=cnt[b]/count
#             print(a,cnt[a],tf)

#Calculating the idf values
"""
# Trying to create the  inverted index
for i in tokens:
    words= []
    words.append(transcript)
"""
