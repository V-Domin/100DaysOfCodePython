import requests
from datetime import datetime
import os

GENDER = 'male'
WEIGHT_KG = 60.2
HEIGHT_CM = 175
AGE = 21
exercise_text = input("Which exercises I've done today: ")


AUTH = os.environ["AUTH"]
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
exercises_endpoint = os.environ['exercises_endpoint']
add_row_endpoint = os.environ['add_row_endpoint']

headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
    'Authorization':AUTH,
}
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercises_endpoint, headers=headers, json=params)
result = response.json()
print(result)


today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.time().strftime("%X")

exercise = result['exercises'][0]['name'].title()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

params_publish = {
    "workout": {
        "date":formatted_date,
        "time":formatted_time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories,
    }
}

response_publish = requests.post(url=add_row_endpoint, json=params_publish, headers=headers)
print(response_publish.text)