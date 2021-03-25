import requests
from datetime import datetime

APP_ID = "API_ID_HERE"
API_KEY = "API_KEY_HERE"

GENDER = "Male"
WEIGHT_KG = 65
HEIGHT_CM = 170
AGE = 25

exercise_endpoint = "EXERCISE_ENDPOINT_HERE"
sheet_endpoint = "SHEET_ENDPOINT_HERE"

exercise_text = input("What exercises did you do?:")

headers = {
    "x-api-id":APP_ID,
    "x-app-key":API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_kg": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint,json=parameters,headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # No Authentication
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "YOUR USERNAME",
            "YOUR PASSWORD",
        )
    )

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": "Bearer YOUR_TOKEN"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )


    print(sheet_response.text)