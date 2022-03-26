# import smtplib

# email = "testing@gmail.com"
# password = "testpassword"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # start secure session
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="to_email@gmail.com",
#         msg="Subject:Hello World!\n\nBody of the email",
#     )

# Gmail: smtp.gmail.com

# Hotmail: smtp.live.com

# Outlook: outlook.office365.com

# Yahoo: smtp.mail.yahoo.com

# import datetime as dt

# now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1998, month=12, day=12)    # year: int requires int, hour:int=... means default value
# print(date_of_birth)
