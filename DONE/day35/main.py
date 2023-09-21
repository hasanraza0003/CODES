#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"  #openweather api endpoint
api_key = os.environ.get("OWM_API_KEY")  # openweather api key saved on environment variable
account_sid = "YOUR ACCOUNT SID"        # account sid of twilio saved in environment variable 
auth_token = os.environ.get("AUTH_TOKEN")  #account auth token of twilio saved in environment variable
 
weather_params = {
    "lat": "YOUR LATITUDE",    
    "lon": "YOUR LONGITUDE",
    "appid": api_key,
    "exclude": "current,minutely,daily"    # it can exclude the other data in the owm api json data
}

response = requests.get(OWM_Endpoint, params=weather_params)   
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]     #it can only take next 12 hour data in the whole o w m weather data

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]   #it can take weather id and search in owm server id code for identifying the weather
    if int(condition_code) < 700:       #if id  is less than 700 then weather id gave the output it will rain in this area for next 12 hour
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
