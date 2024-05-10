import openmeteo_requests

import requests_cache
from retry_requests import retry
import json

def getWeatherCode(latitude, longitude):
	cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)


	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"daily": "weather_code",
		"timezone": "auto"
	}
	responses = openmeteo.weather_api(url, params=params)

	response = responses[0]

	daily = response.Daily()
	daily_weather_code = daily.Variables(0).ValuesAsNumpy()

	daily_weather_code = list(set(daily_weather_code))
	return response.Timezone(), response.TimezoneAbbreviation(), daily_weather_code

def interpretWeatherCode(code):
	codeFile = open("descriptions.json")
	codeDict = json.load(codeFile)
	print(codeDict)

timezone, timezoneAbbrev, weather_code = getWeatherCode(53.5501, -113.4687)
print(f"Timezone {timezone} {timezoneAbbrev}")
print(weather_code)
interpretWeatherCode(weather_code)