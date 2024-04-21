import requests
import time
start = int(time.time() * 1000) - 60000
end = int(time.time() * 1000) 
print(end)

def fetch_forex_data(symbol):
    url = f'https://api.polygon.io/v2/aggs/ticker/C:EURUSD/range/1/second/{start}/{end}?adjusted=true&sort=asc&limit=120&apiKey=gmu8bQSfD5YcIRg2Vab0KUsOy87p6_rl'
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(data)
        # if 'results' in data:
        #     last_trade = data['results']
        #     print(f"Symbol: {data['ticker']}")
        #     print(f"Price: {last_trade['p']}")
        #     print(f"Timestamp: {last_trade['t']}")
        
fetch_forex_data('EURUSD')
