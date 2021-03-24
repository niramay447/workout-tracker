import requests

APP_ID = "aa5a07ea"
API_KEY = "a7121f40d7ffb50b124285f49488b1fc"

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

