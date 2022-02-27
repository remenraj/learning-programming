# Program to send motivational quotes to your email on monday

import smtplib, random
import datetime as dt

# file directory
QUOTES_DIR = r"learning-programming\Python\21-50\41-monday-motivational-quotes-email\quotes.txt"

# opening the quotes file and saving the quotes in a list
try:
    
    with open(QUOTES_DIR) as quotes_file:
        quotes_list = quotes_file.readlines()
except FileNotFoundError:
    print("File not found")
# current date and time
now = dt.datetime.now()

# checking if the current day is monday
if now.weekday() == 0:    # day start with 0=monday to 6=sunday
    
    email = "testing@gmail.com"
    password = "testpassword"
    # getting a random quote from the list
    message = random.choice(quotes_list)
    
    # sending the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # start secure session
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email, # sends email to yourself
            msg=f"Subject:Monday Motivational Quote\n\n{message}",
        )
        