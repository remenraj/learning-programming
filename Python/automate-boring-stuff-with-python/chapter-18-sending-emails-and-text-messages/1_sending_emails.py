# sending emails using smtp: simple mail transfer protocol

import smtplib, os


connection = smtplib.SMTP(host='smtp.gmail.com', port=587)

# start the connection
connection.ehlo()

# start the tls encryption, TLS: Transport Layer Security for encrypting the connection
connection.starttls()

# login
try:
    connection.login(os.environ['EMAIL'], os.environ['EMAIL_PASSWORD'])
except smtplib.SMTPAuthenticationError:
    print("Login failed. Try enabling less secure app access, https://accounts.google.com/b/0/DisplayUnlockCaptcha")

# send the email
connection.sendmail(from_addr=os.environ['EMAIL'], to_addrs=os.environ['EMAIL'], msg="""Subject: Hello.. \n\nWorld!""")

# close the connection
connection.quit()