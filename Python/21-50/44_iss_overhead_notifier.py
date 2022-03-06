# ISS overhead notifier using ISS current location API
# Emails are sent if the ISS is overhead and it is dark

import requests, datetime, smtplib, time, os

USER_LATITUDE = os.getenv("USER_LATITUDE")
USER_LONGITUDE = os.getenv("USER_LONGITUDE")


def is_iss_overhead():
    """Checks if the ISS is near your location and returns true if so"""

    ##### ISS LOCATION #####
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    # print(response)
    # print(response.status_code) # prints the response code
    iss_response.raise_for_status()  # prints the exception error
    # data = response.json()

    iss_latitude = float(iss_response.json()["iss_position"]["latitude"])
    iss_longitude = float(iss_response.json()["iss_position"]["longitude"])
    iss_location = (iss_latitude, iss_longitude)
    # print(f"Location of ISS: {iss_location}")

    if (
        USER_LATITUDE - 5 <= iss_latitude <= USER_LATITUDE + 5
        and USER_LONGITUDE - 5 <= iss_longitude <= USER_LONGITUDE + 5
    ):
        return True
    else:
        return False


def is_night_time():
    """Checks if the current time is after dark and returns True if so"""

    ####### USER LOCATION ########
    location_parameters = {
        "lat": USER_LATITUDE,
        "lng": USER_LONGITUDE,
        "formatted": 0,  # turning formatted off, so datetime module can be used
    }

    # api_url = f"https://api.sunrise-sunset.org/json?lat={MY_LATITUDE}&lng={MY_LONGITUDE}"

    sunrise_response = requests.get(
        url="https://api.sunrise-sunset.org/json?",
        params=location_parameters,
    )
    # raising an exception if the response code is not 200
    sunrise_response.raise_for_status()

    sunrise = sunrise_response.json()["results"][
        "sunrise"
    ]  # can also format it by using the split function here
    sunset = sunrise_response.json()["results"]["sunset"]

    # formatting sunset and sunrise, And getting the hour
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    # current time
    time_now = datetime.datetime.now()
    hour_now = int(time_now.hour)

    # if hour_now not in range(sunrise_hour, sunset_hour):
    if hour_now >= sunset_hour or hour_now <= sunrise_hour:
        return True
    else:
        return False


def send_mail():

    email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    message = "Look up to see ISS"
    
    send_to_email = os.getenv("SEND_TO_EMAIL")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # start secure session
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=send_to_email,
            msg=f"Subject:ISS is here\n\n{message}",
        )


# main function
def iss_overhead_notifier():

    # checking if the iss is currently near the location of user and is currently dark
    if is_iss_overhead() and is_night_time():
        send_mail()


if __name__ == "__main__":
    # running the program every minute
    while True:
        time.sleep(60)
        iss_overhead_notifier()
