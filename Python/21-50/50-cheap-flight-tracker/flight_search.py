import requests, os
from flight_data import FlightData


# kiwi.com flight search API endpoint
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_location_code(self, city_name):
        """This function takes a city name as input and returns the location code for that city."""
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        query = {
            "term": city_name,
            "location_types": "city",
        }
        location_response = requests.get(
            url=location_endpoint, headers=headers, params=query
        )
        location_response.raise_for_status()
        code = location_response.json()["locations"][0]["code"]

        return code

    def check_flights(self, departure_city, arrival_city, date_start, date_end):
        """This function takes a departure city, arrival city, start date and end date as input and returns a list of flights."""
        flight_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"

        flight_headers = {
            "apikey": TEQUILA_API_KEY,
        }

        flight_query = {
            "fly_from": departure_city,
            "fly_to": arrival_city,
            "date_from": date_start,
            "date_to": date_end,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        flight_response = requests.get(
            url=flight_endpoint, headers=flight_headers, params=flight_query
        )
        flight_response.raise_for_status()

        # checking for flights
        try:
            data = flight_response.json()["data"][0]
        except IndexError:  # exception occurs when no flights available with step_over = 0

            flight_query["max_stopovers"] = 1

            flight_response = requests.get(
                url=flight_endpoint, headers=flight_headers, params=flight_query
            )
            flight_response.raise_for_status()
            try:
                data = flight_response.json()["data"][0]

            except IndexError:  # no flights found with stepovers 0, 1
                return None
            else:
                # pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )

            # print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
