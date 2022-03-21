
from twilio.rest import Client
import smtplib, os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_alert(self, message) -> None:
        """Sends an alert message"""
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=message, from_=TWILIO_VIRTUAL_NUMBER, to=TWILIO_VERIFIED_NUMBER
        )

        # prints the message sid if successful
        print(message.sid)

    def send_emails(self, message: str, users: list, link: str) -> None:
        """Sends an email to the given users"""
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PASSWORD)

            for user in users:
                message = f"Hello {user['firstName']},\n{message}"
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=user["email"],
                    msg=f"Subject:Flight Deal Alert\n\n{message}\n{link}".encode(
                        "utf-8"
                    ),
                )
