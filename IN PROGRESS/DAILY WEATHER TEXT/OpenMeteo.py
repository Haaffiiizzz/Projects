import openmeteo_requests

import requests_cache
from retry_requests import retry


cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 53.5501,
	"longitude": -113.4687,
	"daily": "weather_code",
	"timezone": "auto"
}
responses = openmeteo.weather_api(url, params=params)

response = responses[0]
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")


daily = response.Daily()
daily_weather_code = daily.Variables(0).ValuesAsNumpy()

daily_weather_code = list(set(daily_weather_code))

print(daily_weather_code)
