import json
import requests

itemsFile  = open(r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\items.json", "r")
itemsDict = json.load(itemsFile)

with open(r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\rates.json", "r") as file:
    file = file.read()
    ratesDict = json.loads(file)


def getCurrencyValues(baseCurr):
    # access how much 1 dollar is in base currency e.g 1000 naira
    return ratesDict[baseCurr]

def calculateComparedUnits(baseCurr, baseUnits, comparedCurr):
    # calculate how much in compared currency a unit of base currency is
    # for example 5 units of dollar * 1000 naira so 5000 naira
    comparedUnits = ((1 / ratesDict[baseCurr]) *  baseUnits) * ratesDict[comparedCurr]
    return comparedUnits

def createDict(comparedCurr, comparedUnit):
    # retrieves the dictionary for the compared country's item and adjusts accordingly, returns
    # a dictionary with items and how many base currency can buy

    comparedDict = itemsDict[comparedCurr]
    for key, value in comparedDict.items():
        units = round(comparedUnit/value)
        comparedDict[key] = units

    return comparedDict

def printComparedItems(baseCurr, baseUnits, comparedCurr, comparedDict):
    # printing out the stuffs

    print(f"\nThis is what {baseUnits} {baseCurr} can buy in {comparedCurr} country:\n")
    for key, value in comparedDict.items():
        print(f"{value} {key.title()}")


def main():
    base = input("\nType in the base currency, leave a space then type in how many units:\n").split(" ")
    baseCurr = base[0].upper()
    baseUnits = int(base[1])

    comparedCurr = input("\nType in the compared country's currency:\n").upper()
    comparedUnits = calculateComparedUnits(baseCurr, baseUnits, comparedCurr)
    comparedDict = createDict(comparedCurr, comparedUnits)
    printComparedItems(baseCurr, baseUnits, comparedCurr, comparedDict)


if __name__ == "__main__":
    main()





