#! /usr/bin/env python3
# Program to send birthday wishes to those in the csv file who have their birthday today
# Body of the email is read from one of the files in the letter_templates folder


from datetime import datetime
import pandas, random, smtplib, os


# file directories
LETTER_TEMPLATE_DIR = (
    r"learning-programming\Python\21-50\42-birthday-wisher-email\letter_templates"
)
BIRTHDAYS_CSV_DIR = (
    r"learning-programming\Python\21-50\42-birthday-wisher-email\birthdays.csv"
)


# email settings
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# importing data from birthdays csv file
try:
    birthdays_df = pandas.read_csv(BIRTHDAYS_CSV_DIR)
except FileNotFoundError:
    print(f"Birthday csv file not found in {BIRTHDAYS_CSV_DIR}")
else:
    # creates a list of dictionary containing each row in csv file
    birthdays_data = {
        (data_row["month"], data_row["day"]): data_row
        for (index, data_row) in birthdays_df.iterrows()
    }

# current day and month
today = datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthdays_data:
    # birthday data for the current day
    birthday_data = birthdays_data[today_tuple]

    # sending email
    try:
        random_letter_file = f"{LETTER_TEMPLATE_DIR}\\letter_{random.randint(1,3)}.txt"
    except FileNotFoundError:
        print(f"Letter not found in directory: {LETTER_TEMPLATE_DIR}")
    else:
        with open(random_letter_file) as letter:
            letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", birthday_data["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # start secure session
            connection.login(user=EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=birthday_data["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_content}",
            )
