import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')

TO_ADDRESS = os.getenv('TO_ADDRESS')
FROM_ADDRESS = os.getenv('FROM_ADDRESS')


def get_server():
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USER_NAME, PASSWORD)
    return server

# main
def text_alert(rss_feed: str, title: str):
    server = get_server()
    server.sendmail(
        FROM_ADDRESS, 
        [TO_ADDRESS],
        f'Subject: RSS Update - {rss_feed}\n\n{title}'.encode('utf-8')
        )
