import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()
env_pass = os.getenv("db_password")


def email_sender(message):
    host = "smtp.gmail.com"
    port = 465
    username = "korade54321@gmail.com"
    password = env_pass
    receiver = "korade54321@gmail.com"

    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

