# only works with less secure apps turned on

import smtplib

sender = "editedmax@gmail.com"
receiver = "joegreenfielduk@hotmail.com"
password = "Tombstone2018"
subject = "Python Email Test"
body = "I wrote this email in Python!"

# header
message = f"""From: Bruno Greenfield{sender}
To: Joe Greenfield{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")