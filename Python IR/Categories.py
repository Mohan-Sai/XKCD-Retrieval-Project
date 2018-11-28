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
import re

# r = requests.get("https://www.explainxkcd.com/wiki/index.php/Category:Comics_by_topic")
# data = r.text
# soup = BeautifulSoup(data, 'html.parser')
# tags = soup.find_all('li',{'id': ""})
# Categories = {}
# for t in tags:
#     a = t.find('a')
#     if(a["title"][0:8] == "Category"):
#         Categories[a.text] = a["href"]
# with open('Categories.json', 'w') as outfile:  
#     json.dump(Categories, outfile, indent=4)

# Links = {}
# with open('Links.json') as json_file:  
#     Links = json.load(json_file)

# for s in Subcategories:
#     temp = {}
#     for a in Subcategories[s]:
#         print(a)
#         if(a=="Comics by topic"):
#             continue
#         temp[a] = Subcategories[s][a]
#     Subcategories[s] = temp
# with open('SubCategories.json', 'w') as outfile:  
#     json.dump(Subcategories, outfile, indent=4)
# for c in Categories:
#     if(c == "Cancer"c == "Dreams"c == "Emoji"Subcategories[]=="Mars rovers"Subcategories[]=="News anchor"Subcategories[]=="Public speaking"Subcategories[]=="Social interactions"Subcategories[]=="Space probes"Subcategories[]=="Spice Girls"Subcategories[]=="Strange powers of Beret Guy"Subcategories[]=="Sport"Subcategories[]=="Substitutions"Subcategories[]=="Tips"Subcategories[]=="Tribute"):
#         continue
#     if(c[0] == "A"c[0] == "B"c[0] == "C"c[0] == "D"c[0] == "E"c[0] == "F"c[0] == "G"c[0] == "H"c[0] == "I"c[0] == "J"c[0] == "K"c[0] == "L"c[0]=="M"c[0]=="N"c[0]=="O"c[0]=="P"c[0]=="Q"c[0]=="R"c[0]=="S"):
#         continue
#     print(c)
#     r = requests.get("https://www.explainxkcd.com"+Categories[c])
#     data = r.text
#     soup = BeautifulSoup(data, 'html.parser')
#     tags = soup.find_all('li',{'id': "", 'class': ""})
#     temp = {}
#     for t in tags:
#         a = t.find('a')
#         print(a)
#         if(a["title"][0:8] == "Category"):
#             temp[a.text] = a["href"]
#     Subcategories[c] = temp
#     print("end")
#     with open('SubCategories.json', 'w') as outfile:  
#         json.dump(Subcategories, outfile, indent=4)

# Links = {}
# for c in Subcategories:
#     print(c)
#     Links[c] = {}
#     for s in Subcategories[c]:
#         r = requests.get("https://www.explainxkcd.com"+Subcategories[c][s])
#         data = r.text
#         soup = BeautifulSoup(data, 'html.parser')
#         div = soup.find('div', {'class':"mw-content-ltr"})
#         tags = div.find_all_next('li',{'id':"", 'class':""})
#         temp=[]
#         for t in tags:
#             a = t.find('a')
#             if a is None:
#                 continue
#             temp.append(a.text[0:4])
#         Links[c][s] = temp
#         with open('SubLinks.json', 'w') as outfile:  
#             json.dump(Links, outfile, indent=4)
# with open('Links.json') as json_file:  
#     Sub = json.load(json_file)

# pattern = re.compile(r"\d{1,4}")
# ExtraWords = {}
# for l in Links:
#     for i in Links[l]:
#         ExtraWords[i] =[]
#         ExtraWords[i].append(l)


# # print(len(list(set(temp))))
# with open('ExtraWords.json', 'w') as outfile:  
#     json.dump(ExtraWords, outfile, indent=4)
# ExtraWords = {}
# with open('ExtraWords.json') as json_file:  
#     ExtraWords = json.load(json_file)
# ExtraWordsSub = {}
# with open('ExtraWordsSub.json') as json_file:  
#     ExtraWordsSub = json.load(json_file)

# EW_Final = {}
# for i in ExtraWords:
#     EW_Final[i] = []
#     for t in ExtraWords[i]:
#         EW_Final[i].append(t)

# for i in ExtraWordsSub:
#     EW_Final[i] = []
#     for t in ExtraWordsSub[i]:
#         EW_Final[i].append(t)

# for i in EW_Final:
#     EW_Final[i] = list(set(EW_Final[i]))

EW_Final = {}
with open('Topics.json') as json_file:  
    EW_Final = json.load(json_file)

Final_Explanations = {}
with open('FinalExplanations.json') as json_file:  
    Final_Explanations = json.load(json_file)
ps = PorterStemmer()
for i in EW_Final:
    if(i == "2074" or i == "2075"):
        continue
    print(i)
    for t in EW_Final[i]:
        Final_Explanations[i].append(ps.stem(t))
    Final_Explanations[i] = list(set(Final_Explanations[i]))

with open('FinalExplanations.json', 'w') as outfile:  
    json.dump(Final_Explanations, outfile, indent=4)