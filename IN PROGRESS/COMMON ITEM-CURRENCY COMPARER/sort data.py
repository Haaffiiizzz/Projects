import json
file = open(r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\countries.json", "r").read()
countriesDict = json.loads(file)

fileTwo = open(r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\egg.txt", "r").readlines()


for line in fileTwo:
    line = line.split()
    for key in countriesDict.keys():
        if line[1] == key:
            countriesDict[key]["Apples, 1 KG"] = line[2]
            
with open(r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\countries.json", 'w') as json_file:
    json.dump(countriesDict, json_file, indent=2)