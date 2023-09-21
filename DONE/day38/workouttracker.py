import requests
from datetime import datetime
import os

APP_ID = "e2ee2af8"
API_KEY = "bc05c4e937216d0b0d1f01476d22b7ec"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ce97b88d96a132611868c3615b46979d/myWorkouts2/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


parameters={
    "query": exercise_text,
    "gender": "male",
    "weight_kg":65.5 , 
    "height_cm": 170.20,
    "age":21
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)

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
    
    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    #Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint, 
    #     json=sheet_inputs, 
    #     auth=(
    #         "hasan03", 
    #         "60221023",
    #     )
    # )

    # #Bearer Token
    # bearer_headers = {
    # "Authorization": "Bearer 41w8d41ew841d6wd1w6d1w6"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint, 
    #     json=sheet_inputs, 
    #     headers=bearer_headers
    # )
    print(sheet_response.text)
