#! usr/bin/env python3
# Habit Tracker using Pixela

import requests, os
from datetime import datetime

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = os.environ.get("GRAPH_ID")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

pixela_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # creating a new user account
# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_parameters)
# print(response.text)

# # creating graph
# # headers is one of the kwargs of requests.post, so nobody can see it
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Tracker",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# # created graph url: https://pixe.la/v1/users/r3m3n/graphs/cyclinggraph1.html


#----------------------------- post value to the graph -----------------------------#

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

today = datetime.today()
anyday = datetime(year=2022, month=2, day=21)   # creating a date object

pixel_data = {
    "date": f"{today.strftime('%Y%m%d')}", # YYYYMMDD
    "quantity": "13",
}

# pixel_post_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(pixel_post_response.text)


#---------------------------- editing a pixel on the graph-------------------------------------#

anyday = datetime(year=2022, month=2, day=21)   # creating a date object

pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{anyday.strftime('%Y%m%d')}"


pixel_update_data = {
    "quantity": "14",
}

# pixel_update_respone = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(pixel_update_respone.text)


#---------------------------- deleting a pixel on the graph-------------------------------------#

anyday = datetime(year=2022, month=2, day=21)   # creating a date object

pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{anyday.strftime('%Y%m%d')}"

# pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(pixel_delete_response.text)