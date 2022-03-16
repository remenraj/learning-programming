#!/usr/bin/env python3
# Fitness tracker app using Nutritionix api, Google Sheets and NLP GPT-3
# Natural Language Processing is done using GPT-3 model
import requests, os
from datetime import datetime

GENDER = os.environ["GENDER"]
WEIGHT_KG = os.environ["WEIGHT_KG"]
HEIGHT_CM = os.environ["HEIGHT_CM"]
AGE = os.environ["AGE"]

# Nutritionix app id and key
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_APP_KEY = os.environ["NUTRITIONIX_APP_KEY"]


NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# asking user to enter the workout details
exercise_text = input("What exercise did you do today?: ")

nutritionist_post_request_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutritionist_response = requests.post(
    url=NUTRITIONIX_EXERCISE_ENDPOINT,
    json=nutritionist_post_request_body,
    headers=NUTRITIONIX_HEADERS,
)
nutritionist_response.raise_for_status()

exercise_data = nutritionist_response.json()
# print(exercise_data)

# ---------------------------- sheety api---------------------------------#
# Using headers to authenticates the user
# SHEETY_HEADERS = {
#     "Authorization": os.environ["SHEETY_AUTHORIZATION"],
# }

# # Bearer Token Authentication
# SHEETY_BEARER_HEADERS = {
# "Authorization": os.environ["SHEETY_BEARER_AUTHORIZATION"],
# }

# using username and password to authenticate the user
# Basic Authentication
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
SHEETY_AUTH = (SHEETY_USERNAME, SHEETY_PASSWORD)

SHEETY_ENDPOINT = "https://api.sheety.co/285bc14813fd5609aa824f7e9778ed8c/workoutsTrackingPython/workouts"

# # retrieve rows from sheet
# sheety_get_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
# print(sheety_get_response.json())


# add a row to sheet
# date
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

# looping through all the exercises that the user has done and adding them to the sheet
for exercise in exercise_data["exercises"]:
    sheety_new_row = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_post_response = requests.post(
        url=SHEETY_ENDPOINT, json=sheety_new_row, auth=SHEETY_AUTH
    )
    sheety_post_response.raise_for_status()
# print(sheety_post_response.text)
