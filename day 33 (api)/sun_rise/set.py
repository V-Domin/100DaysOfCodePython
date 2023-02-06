import requests
from datetime import datetime

MY_LAT = 48.464718
MY_LNG = 35.046185

parameters = {
    "lat":MY_LAT,
    "Lng":MY_LNG,
    "formatted":0,
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
print(time_now.hour)

