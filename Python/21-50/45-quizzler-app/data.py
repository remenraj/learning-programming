# Gets the question data from open trivia database through its api
# api url: https://opentdb.com/api.php?amount=10&type=boolean
# website url: https://opentdb.com/api_config.php


import requests

question_parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
response = requests.get("https://opentdb.com/api.php?", params=question_parameters)
response.raise_for_status()
question_data = response.json()["results"]
