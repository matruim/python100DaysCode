import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/279e398dc3434f2d9e7d73294c68a4f9/myWorkouts/workouts"

headers = {
    "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
    "Content-Type": "application/json",
}

print(headers)

user_response = {
    "query": input("Tell me which exercises you did: ")
}

res = requests.post(API_URL, headers=headers, json=user_response)
res.raise_for_status()
data = res.json()
for exercise in data['exercises']:
    row = {
        "workout": {
            "date": datetime.datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    response = requests.post(SHEET_URL, json=row, headers={"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"})
    print(response.text)


