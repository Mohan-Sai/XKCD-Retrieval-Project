from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import json

# stop = list(set(stopwords.words('english')) | set(string.punctuation))
# file = open("Stopwords/atire_puurula.txt", 'r')
# temp = file.readlines()
# atire_puurula = [line[:-1] for line in temp]

# file.close()
# file = open("Stopwords/onix.txt",'r')
# temp = file.readlines()
# onix = [line[:-1] for line in temp]

# file.close()
# file = open("Stopwords/reuters_wos.txt",'r')
# temp = file.readlines()
# reuters_wos = [line[:-1] for line in temp]

# file.close()
# file = open("Stopwords/scikitlearn.txt",'r')
# temp = file.readlines()
# scikitlearn = [line[:-1] for line in temp]

# file.close()
# file = open("Stopwords/snowball_expanded.txt",'r')
# temp = file.readlines()
# snowball_expanded = [line[:-1] for line in temp]

# file.close()

# merged_list = atire_puurula + onix + scikitlearn + snowball_expanded +stop
# print(len(merged_list))
# set_merged_list = list(set(merged_list))
# print("\n")
# set_merged_list.remove('number')
# set_merged_list.remove('fire')
# set_merged_list.remove('invention')
# set_merged_list.remove('million')
# set_merged_list.remove('zero')
# with open('stopwords.json', 'w') as outfile:  
#     json.dump(set_merged_list, outfile)
data = []
with open('stopwords.json') as json_file:  
    data = json.load(json_file)
newData = []
for word in data:
    print(word)
    word = word.lower()
    newData.append(word)
print(newData)
with open('stopwords.json', 'w') as outfile:  
    json.dump(newData, outfile, indent=4)
# appended_list= ['A','The', 'There','There', 'He', 'Like', 'also', 'really', 'often', 'Similar', 'some', 'This', 'help', 'seemingly', 'eventually']

# stop.extend(appended_list)