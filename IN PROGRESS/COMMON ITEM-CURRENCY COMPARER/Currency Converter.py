import json
import re
import tkinter as tk
from tkinter import ttk, messagebox

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
    comparedCode = itemsDict[comparedCurr][0]
    comparedUnits = ((1 / ratesDict[baseCurr]) *  baseUnits) * ratesDict[comparedCode]
    return comparedUnits

def createDict(comparedCurr, comparedUnit):
    # retrieves the dictionary for the compared country's item and adjusts accordingly, returns
    # a dictionary with items and how many base currency can buy

    comparedDict = itemsDict[comparedCurr][1]
    for key, value in comparedDict.items():
        units = round(comparedUnit/float(value))
        comparedDict[key] = units

    return comparedDict

def printComparedItems(baseCurr, baseUnits, comparedCurr, comparedDict):
    # printing out the stuffs

    print(f"\nThis is what {baseUnits} {baseCurr} can buy in {comparedCurr}:\n")
    for key, value in comparedDict.items():
        print(f"{value} {key.title()}")


def main():
    root = tk.Tk()
    root.title("Currency comparison.")

    ttk.Label(root, text="Base Currency:").grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
    baseCurrency = ttk.Combobox(root, values=list(ratesDict.keys()))
    baseCurrency.grid(column=1, row=0, padx=10, pady=5)
    baseCurrency.current(0)

    ttk.Label(root, text="Units:").grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
    baseUnitsVar = tk.StringVar()
    baseUnits = ttk.Entry(root, textvariable=baseUnitsVar)
    baseUnits.grid(column=1, row=1, padx=10, pady=5)

    ttk.Label(root, text="Compared Country:").grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
    comparedCurr = ttk.Combobox(root, value=list(itemsDict.keys()))
    comparedCurr.grid(column=1, row=2, padx=10, pady=5)
    comparedCurr.current(0)

    ttk.Label(root, text="Item:").grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
    item = ttk.Combobox(root, values=["All"] + list(itemsDict["United States"][1].keys()))
    item.grid(column=1, row=3, padx=10, pady=5)
    item.current(0)


    root.mainloop()

    # baseCurr = input("Type in the base currency:\n").upper()
    # baseUnits = int(input("\nType in how many units:\n")) 

    # comparedCurr = input("Type in the compared country:\n").title()
    # comparedUnits = calculateComparedUnits(baseCurr, baseUnits, comparedCurr)
    # comparedDict = createDict(comparedCurr, comparedUnits)
    # printComparedItems(baseCurr, baseUnits, comparedCurr, comparedDict)


if __name__ == "__main__":
    main()





