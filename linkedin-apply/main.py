import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")


service = Service(service_args=["--profile-root", "./temp"])
browser = webdriver.Firefox(service=service)

browser.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
)


def login():
    time.sleep(3)

    login_email = browser.find_element(By.ID, "username")
    login_password = browser.find_element(By.ID, "password")

    login_email.send_keys(LINKEDIN_EMAIL)
    time.sleep(3)
    login_password.send_keys(LINKEDIN_PASSWORD)
    login_password.send_keys(Keys.ENTER)


"""Reject cookies"""
time.sleep(3)

try:
    cookies_reject = browser.find_element(
        By.XPATH, "/html/body/div[1]/div/section/div/div[2]/button[2]"
    )
    cookies_reject.click()
except NoSuchElementException:
    pass

"""Signing in to Linkedin"""
time.sleep(3)
signin_button = browser.find_element(By.LINK_TEXT, "Sign in")
time.sleep(3)
signin_button.click()
login()

"""Save job offer"""
time.sleep(5)
save_offer = browser.find_element(By.CLASS_NAME, 'jobs-save-button')
save_offer.click()

""" browser.close()
browser.quit() """
