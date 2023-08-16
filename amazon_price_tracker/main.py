from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from smtplib import SMTP

load_dotenv()

PRODUCT_URL = os.environ.get('PRODUCT_URL')
USER_AGENT = os.environ.get('USER_AGENT')
ACCEPT_LANGUAGE = os.environ.get('ACCEPT_LANGUAGE')
ACCEPT_ENCODING = os.environ.get('ACCEPT_ENCODING')
ACCEPT = os.environ.get('ACCEPT')
SECCHUAPLATFORM = os.environ.get('SECCHUAPLATFORM')
EMAIL = os.environ.get('EMAIL')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')

headers = {
        'User-Agent': USER_AGENT,
        'Accept-Language': ACCEPT_LANGUAGE,
        'Accept-Encoding': ACCEPT_ENCODING,
        'Accept': ACCEPT,
        'sec-ch-ua-platform': SECCHUAPLATFORM}



######################### SCRAPING AMAZON #########################
# Getting data from the product's page on Amazon and parsing with
# Beautiful Soup to get the price.

product_page = requests.get(url=PRODUCT_URL, headers=headers).text

soup = BeautifulSoup(product_page, 'lxml')

price_span = soup.find('span', class_='aok-offscreen')
price_text = price_span.get_text()
price_without_dollarsign = price_text.split('$')
price_string = price_without_dollarsign[1].split()[0]
price_float = float(price_string)


########################### SENDING EMAIL ##########################
# Sending an email if the product's price is cheaper than a target
# price ; for the sake of the exercize and testing smtplib, it is
# also sending an email if it is above the threshold.

TARGET_PRICE = 50.00
fromaddr = EMAIL
toaddrs = EMAIL
smtp_connection = SMTP('smtp.gmail.com', port=587)

message_headers = f"From: {EMAIL}\nTo: {EMAIL}\nSubject: Instant Cooker Price Alert\n"
                            
if price_float <= TARGET_PRICE:
    with smtp_connection:
        smtp_connection.set_debuglevel(1)
        smtp_connection.starttls()
        smtp_connection.login(user=EMAIL, password=GMAIL_APP_PASSWORD)
        message = message_headers + f"The cooker's price is ${price_float} GO BUY!!!"
        smtp_connection.sendmail(fromaddr, toaddrs, message)
else:
    with smtp_connection:
        smtp_connection.set_debuglevel(1)
        smtp_connection.starttls()
        smtp_connection.login(user=EMAIL, password=GMAIL_APP_PASSWORD)
        message = message_headers + f"The cooker's price is ${price_float} THAT'S TOO EXPENSIVE!!!"
        smtp_connection.sendmail(fromaddr, toaddrs, message)
