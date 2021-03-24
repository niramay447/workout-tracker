import requests

APP_ID = "API_ID_HERE"
API_KEY = "API_KEY_HERE"

GENDER = "Male"
WEIGHT_KG = "65"
HEIGHT_CM = "170"
AGE = "25"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(result)