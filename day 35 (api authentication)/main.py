import requests
from twilio.rest import Client
import os


MY_KEY = "3dbd41d4f4ecdd56a4e41a7b1949201d"
account_sid = 'ACaa02da6a9a5fabe9cb5bc3be0c5184fd'
auth_token = '7056d75362b87b9aa988b1d59b8cf4eb'


parameters = {
    'lat':48.464718,
    'lon':35.046185,
    'appid':MY_KEY,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()['list'][:5]

will_rain = False

for weather_data in data:
    condition_code = weather_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="You should take an umbrella. It's going to rain toda!☔",
        from_='+14422672882',
        to='+380668046628'
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="You should NOT take an umbrella. Sending you love!❤",
        from_='+14422672882',
        to='+380668046628'
    )

print(message.status)
