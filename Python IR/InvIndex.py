import string
import json

TFIDFMatrix = {}
with open('TFIDFMatrix1.json') as json_file:  
    TFIDFMatrix = json.load(json_file)
INVIndex = {}
for i in TFIDFMatrix.keys():
    print(i)
    temp = []
    queryVector = []
    for j in TFIDFMatrix[i]:
        temp.append(j)
        queryVector.append(TFIDFMatrix[i][j])
    for a in range(0,len(TFIDFMatrix[i])):
        for b in range(a,len(TFIDFMatrix[i])):
            if(queryVector[a]<queryVector[b]):
                t = queryVector[a]
                queryVector[a] = queryVector[b]
                queryVector[b] = t
                t = temp[a]
                temp[a] = temp[b]
                temp[b] = t
    INVIndex[i] = temp
with open('InvIndex1.json', 'w') as outfile:  
    json.dump(INVIndex, outfile, indent=4)
