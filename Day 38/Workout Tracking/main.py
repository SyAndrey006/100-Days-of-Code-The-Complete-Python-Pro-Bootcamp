import requests
from datetime import datetime
# import os

# APP_ID = os.environ["ENV_nutritionix_ID"]
# API_KEY = os.environ["ENV_nutritionix_API"]
APP_ID = "497ebb57"
API_KEY = "bda6dd3110d4e1b4baab96e86684ab47"

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 178
AGE = 18

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercises = input("What exercise did you do today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercises,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(f"Nutritionix API call: \n {result} \n")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


# sheet_endpoint = os.environ["ENV_shetty_endpoint"]
sheet_endpoint = "https://api.sheety.co/d60c84605824c2934f2f0b310fd6024f/myWorkouts/workouts"
google_sheet_name = "workout"

headers = {
    "Authorization": f"Bearer {"Andrew"}",
    "Content-Type": "application/json"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        google_sheet_name: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }



    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=headers)

    print(f"Sheety Response: \n {sheet_response.text}")
