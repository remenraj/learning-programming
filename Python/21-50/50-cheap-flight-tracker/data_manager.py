# This file is responsible for talking to the Google Sheet.

import requests, os


SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
SHEETY_ENDPOINT = "https://api.sheety.co/285bc14813fd5609aa824f7e9778ed8c/flightDeals"
SHEETY_ENDPOINT_PRICES = SHEETY_ENDPOINT + "/prices"
SHEETY_ENDPOINT_USERS = SHEETY_ENDPOINT + "/users"

SHEETY_AUTH = (SHEETY_USERNAME, SHEETY_PASSWORD)


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.data = {}

    def retrieve_data(self, sheet_name) -> dict:
        """Retrieves data from sheet and prints it to the console"""

        if sheet_name == "prices":
            sheety_get_response = requests.get(
                url=SHEETY_ENDPOINT_PRICES, auth=SHEETY_AUTH
            )
        elif sheet_name == "users":
            sheety_get_response = requests.get(
                url=SHEETY_ENDPOINT_USERS, auth=SHEETY_AUTH
            )

        sheety_get_response.raise_for_status()

        self.data = sheety_get_response.json()
        return self.data

    def add_iata_code(self, row_id: int, iata_code: str) -> None:
        """Adds an IATA code to the row with the given ID"""

        for row in self.data["prices"]:
            if row["id"] == row_id:
                new_data = {
                    "price": {
                        "iataCode": iata_code,
                    }
                }
                update_response = requests.put(
                    url=f"{SHEETY_ENDPOINT_PRICES}/{row['id']}",
                    json=new_data,
                    auth=SHEETY_AUTH,
                )
                update_response.raise_for_status()
                break

    def add_user(self, first_name: str, last_name: str, email: str) -> None:
        """Adds a new user to the sheet"""
        new_user = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        add_user_response = requests.post(
            url=SHEETY_ENDPOINT_USERS, auth=SHEETY_AUTH, json=new_user
        )
