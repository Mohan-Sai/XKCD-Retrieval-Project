import string
import json

TFIDFMatrix = {}
with open('TFIDFMatrix.json') as json_file:  
    TFIDFMatrix = json.load(json_file)
INVIndex = {}
for i in TFIDFMatrix.keys():
    temp = []
    for j in range(0,5):
        temp.append(j+1)
    queryVector = TFIDFMatrix[i]
    for a in range(0,5):
        for b in range(a,5):
            if(queryVector[a]<queryVector[b]):
                t = queryVector[a]
                queryVector[a] = queryVector[b]
                queryVector[b] = t
                t = temp[a]
                temp[a] = temp[b]
                temp[b] = t
    INVIndex[i] = temp


with open('InvIndex.json', 'w') as outfile:  
    json.dump(INVIndex, outfile, indent=4)
