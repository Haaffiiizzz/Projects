import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()
url = "https://marketdata.tradermade.com/api/v1/live"
currency = "USDJPY,GBPUSD,UK100"
api_key = "wsm3B5rDX36SE4lbu5rA"
querystring = {"currency":currency,"api_key":api_key}
response = requests.get(url, params=querystring)
pp.pprint(response.json())