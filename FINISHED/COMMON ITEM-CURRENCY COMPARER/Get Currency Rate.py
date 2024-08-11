import json
import requests

# request for the rates from the api and returns the json file
response = requests.get("https://v6.exchangerate-api.com/v6/b11b7775a7d823efffd22253/latest/USD")
if response.status_code == 200:
    ratesDict = response.json()["conversion_rates"]
else:    
    raise Exception("Not 200 code")

# with open(r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\rates.json", "w") as file:
#     json.dump(ratesDict, file, indent=2)
print(ratesDict)