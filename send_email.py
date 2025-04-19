import smtplib, ssl
import os

def email_sender(message):
    host = "smtp.gmail.com"
    port = 465
    username = "korade54321@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "korade54321@gmail.com"

    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

