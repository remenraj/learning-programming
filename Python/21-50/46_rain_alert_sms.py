# Rain Alert Program: when rain is detected within 12 hrs of the day, sends sms alert
# twilio.com is the service provider for sending text messages
# use https://ventusky.com to find places where it is raining to debug
# use https://latlong.net to find the latitude and longitude of that place

import requests, os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


# user latitude and longitude
USER_LATITUDE = os.environ.get("USER_LATITUDE")
USER_LONGITUDE = os.environ.get("USER_LONGITUDE")

# open weather map endpoint
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api key for openweathermap.org
OWM_API_KEY = os.environ.get("OWM_API_KEY")

# twilio api credentials
twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")

# weather parameters
weather_parameters = {
    "lat": USER_LATITUDE,
    "lon": USER_LONGITUDE,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily",
}
# get weather data
weather_response = requests.get(OWM_endpoint, params=weather_parameters)
# raise exception if response code is not 200
weather_response.raise_for_status()
weather_data = weather_response.json()

hourly_weather_data = weather_data["hourly"]

will_rain = False

# check if it is raining in the next 12 hours, starts with 0 to 11
for item in hourly_weather_data[:12]:
    if item["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    # to make this code work on pythonanywhere's free proxy, we need to use the TwilioHttpClient
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(twilio_account_sid, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    message = client.messages.create(
        body="It is going to rain today. Carry an umbrella.",
        from_=TWILIO_VIRTUAL_NUMBER,
        to=TWILIO_VERIFIED_NUMBER,
    )
    print(message.status)


# creating environment variables
# On the terminal type: env, to list all the current environment variables
# To create new one, type without spaces: export <name>=<value>
# example: export OWM_API_KEY=some_value
# type env to see the updated environment variables
# now update the OWM_API_KEY variable with the new value: OWM_API_KEY = os.environ.get("OWM_API_KEY")

# Windows 10 and Windows 8

#   In Search, search for and then select: System (Control Panel)
#   Click the Advanced system settings link.
#   Click Environment Variables.
#   In the section System Variables find the PATH environment variable and select it. Click Edit.
#   If the PATH environment variable does not exist, click New.
#   In the Edit System Variable (or New System Variable) window, specify the value of the PATH environment variable.
#   Click OK. Close all remaining windows by clicking OK.

# Open pythonanywhere's tasks page and under the command line tab, type:
# export OWM_API_KEY=some_value;export TWILIO_AUTH_TOKEN=some_value python3 rain_alert.py
# ; is used for next line

# In VSCode, edit the launch.json file and add the following:
# {
#   "version": "0.2.0",
#   "configurations": [
#     {
#       "type": "pwa-node",
#       "request": "launch",
#       "name": "Launch Program",
#       "skipFiles": [
#         "<node_internals>/**"
#       ],
#       "program": "${workspaceFolder}/index.js",
#       "env": {
#         "OWM_API_KEY": "some_value",
#         "TWILIO_AUTH_TOKEN": "some_value",
#       }
#     }
#   ]
# }
