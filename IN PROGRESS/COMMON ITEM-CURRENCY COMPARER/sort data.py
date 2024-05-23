import json
import re

# Load the JSON data from a file
json_file_path = r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\items.json"
with open(json_file_path, "r") as file:
    countriesDict = json.load(file)

# Parse the text file to get the currency information
currency_file_path = r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\egg.txt"
currency_dict = {}
with open(currency_file_path, "r") as file:
    for line in file.readlines():
        parts = line.strip().split('\t')
        if len(parts) >= 3:
            country = parts[0].strip()
            currency_code = parts[2].strip()
            currency_dict[country] = currency_code
          
newDict = {}
for country, code in currency_dict.items():
    for key, value in countriesDict.items():
        pattern = r'\(.*?\)'
        # Split the country string at any occurrence of parentheses
        country_name = re.split(pattern, country)[0].strip()
        if key.upper() == country_name:
            print(key, country)
#             newDict[code] = [key, value]

# print(newDict, len(list(newDict.keys())))
# Save the transformed data back to a new JSON file
# new_json_file_path = r"IN PROGRESS\COMMON ITEM-CURRENCY COMPARER\transformed_items.json"
# with open(new_json_file_path, 'w') as json_file:
#     json.dump(new_data, json_file, indent=2)

print("Data has been transformed and saved.")
