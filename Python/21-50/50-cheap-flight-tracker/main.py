#! usr/bin/env python3
# Program to find the cheapest flight from a given source to a given destination and alerts the user when a cheaper flight is found.

from encodings import utf_8
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from notification_manager import NotificationManager


ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
# getting data from sheet
sheet_data_prices = data_manager.retrieve_data(sheet_name="prices")
# # printing the sheet data
# pprint(sheet_data)

# getting the user list and their emails
sheet_data_users = data_manager.retrieve_data(sheet_name="users")
# pprint(sheet_data_users)

users = sheet_data_users["users"]
# pprint(users)

# creating a flight search object
flight_search = FlightSearch()

# creating a notification manager object
notification_manager = NotificationManager()


# checking if all iata codes are entered, if not then adding them
for location in sheet_data_prices["prices"]:
    if len(location["iataCode"]) == 0:
        location_code = flight_search.get_location_code(location["city"])
        data_manager.add_iata_code(location["id"], location_code)

# start and end dates: tomorrow and six months from now/today
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=180)

# getting the flights
for location in sheet_data_prices["prices"]:
    flight = flight_search.check_flights(
        departure_city=ORIGIN_CITY_IATA,
        arrival_city=location["iataCode"],
        date_start=tomorrow.strftime("%d/%m/%Y"),
        date_end=six_months_from_now.strftime("%d/%m/%Y"),
    )

    # checking if there are no flights
    if flight == None:
        # print(f"No flights found for {location['city']}")
        continue

    # checking for a cheap flight
    if flight.price < location["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        # notification_manager.send_alert(
        #     message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        # )

        if flight.stop_overs > 0:
            message += (
                f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            )
        google_flight_link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(
            message=message, users=users, link=google_flight_link
        )


# # Adding a new user to the Flight Club
# print("Welcome to the Flight Club\nWe find the best flight deals for you.")
# user_first_name = input("What is your first name: ")
# user_last_name = input("What is your last name: ")

# # making sure the user entered correct email
# valid_input = False
# while not valid_input:
#     user_email = input("What is your email: ")
#     user_email_check = input("Enter your email again: ")

#     if user_email == user_email_check:
#         print("Email confirmed")
#         valid_input = True
#     else:
#         print("Emails don't match")


# data_manager.add_user(
#     first_name=user_first_name, last_name=user_last_name, email=user_email
# )


# print("Success! Your email has been added.\nYou're in the club!")
