import json
import tkinter as tk
from tkinter import ttk

itemsFile  = open(r"FINISHED\COMMON ITEM-CURRENCY COMPARER\items.json", "r")
itemsDict = json.load(itemsFile)

with open(r"FINISHED\COMMON ITEM-CURRENCY COMPARER\rates.json", "r") as file:
    file = file.read()
    ratesDict = json.loads(file)

def calculateUnits(price, baseValue):

    units = baseValue/float(price)
    return round(units)

def compareCurrency():
    baseValue = float(baseUnits.get()) / int(ratesDict[baseCurrency.get()]) 
    itemUnitDict = {}

    if itemsBox.get() == "All":
        for item, price in itemsDict[comparedCurr.get()][1].items():
            itemUnitDict[item] = calculateUnits(price, baseValue)

    else:
        item = itemsBox.get()
        itemUnitDict[item] = calculateUnits(itemsDict[comparedCurr.get()][1][item], baseValue)     

    printComparedItems(itemUnitDict)

def printComparedItems(Dict):
    
    resultText = f"\nThis is what {baseUnits.get()} {baseCurrency.get()} can buy in {comparedCurr.get()}:\n\n"
    for key, value in Dict.items():
        resultText += f"{key}: {value if value > 0 else '<1'}\n"

    result.config(text = resultText)

def updateItems(*args):
    compared = comparedCurr.get().title()
    
    if compared in itemsDict:
        items = list(itemsDict[compared][1].keys())
        items.insert(0, "All")
        itemsBox['values'] = items
        if items:
            itemsBox.current(0)
    else:
        itemsBox.set('')


root = tk.Tk()
root.title("Currency comparison.")

style = ttk.Style()
style.configure("TLabel", font=("Verdana", 12, "bold"))
style.configure("TButton", font=("Verdana", 12, "bold"))
style.configure("TCombobox", font=("Verdana", 12, "bold"))
style.configure("TEntry", font=("Verdana", 12, "bold"))


ttk.Label(root, text="Base Currency:").grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
baseCurrency = ttk.Combobox(root, values=list(ratesDict.keys()), state="readonly")
baseCurrency.grid(column=1, row=0, padx=10, pady=5)
baseCurrency.current(0)

ttk.Label(root, text="Units:").grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
baseUnitsVar = tk.StringVar(value="1")
baseUnits = ttk.Entry(root, textvariable=baseUnitsVar, font=("Verdana", 10))
baseUnits.grid(column=1, row=1, padx=10, pady=5)


ttk.Label(root, text="Compared Country:").grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
comparedCurr = ttk.Combobox(root, value=list(itemsDict.keys()), state="readonly")
comparedCurr.grid(column=1, row=2, padx=10, pady=5)
comparedCurr.current(0)
comparedCurr.bind("<<ComboboxSelected>>", updateItems)


ttk.Label(root, text="Item:").grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
itemsBox= ttk.Combobox(root, state="readonly")
itemsBox.grid(column=1, row=3, padx=10, pady=5)
updateItems()

compareButton = ttk.Button(root, text= "Compare", command = compareCurrency)
compareButton.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

result = ttk.Label(root, text="", justify=tk.LEFT, font=("Verdana", 10), wraplength=400)
result.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

root.mainloop()








