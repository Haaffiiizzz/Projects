import openmeteo_requests
import requests_cache
from retry_requests import retry
import json
from twilio.rest import Client

account_sid = "AC07ad148158c8b75259fb7eabb9669039"
auth_token = "f4c771a62202ec17f78f9f53a353a5ff"
client = Client(account_sid, auth_token)

def getWeatherCode(latitude, longitude):
	cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"daily": "weather_code",
		"timezone": "auto",
		"forecast_days": 1
	}
	responses = openmeteo.weather_api(url, params=params)	
	response = responses[0]

	daily = response.Daily()
	daily_weather_code = daily.Variables(0).ValuesAsNumpy()
	
	return response.Timezone(), response.TimezoneAbbreviation(), daily_weather_code

def interpretWeatherCode(code):
	codeFile = open("IN PROGRESS\DAILY WEATHER TEXT\code.json")
	codeDict = json.load(codeFile)
	
	day = codeDict[str(int(code))]["day"]["description"]
	night = codeDict[str(int(code))]["night"]["description"]
	return day, night

def sendText(recepient, messageSend):

	message = client.messages \
					.create(
						body= messageSend,
						from_='+13343264571',
						to= recepient
					)
	
def getMessages():
	print(client.messages.list())

	

timezone, timezoneAbbrev, weather_code = getWeatherCode(53.5501, -113.4687)
day, night= interpretWeatherCode(weather_code[0])

messageText = f"Today in {timezone} the weather is going to be {day}. At night, it will be {night}! Dress for the weather. :)"

sendText("+17803990244", messageText)
getMessages()