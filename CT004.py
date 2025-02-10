from start_drive import start_drive
from dotenv import load_dotenv

import os
import time

load_dotenv()


def ct004() -> None:
    browser = start_drive()

    url_page = "http://localhost:3000/"
    browser.get(url_page)

    xpath_email_field = '//*[@id="email"]'
    email_field = browser.find_element("xpath", xpath_email_field)
    email_field.send_keys(os.getenv("emailCT001"))

    xpath_password_field = '//*[@id="senha"]'
    password_field = browser.find_element("xpath", xpath_password_field)
    password_field.send_keys(os.getenv("passwordCT001"))

    xpath_login_button = "/html/body/div/form/button"
    login_button = browser.find_element("xpath", xpath_login_button)
    login_button.click()

    time.sleep(3)

    xpath_next_page_button = "/html/body/div/ul/li[2]/a"
    next_page_button = browser.find_element("xpath", xpath_next_page_button)
    next_page_button.click()

    time.sleep(3)

    xpath_next_page_button = "/html/body/div/ul/li[2]/a"
    next_page_button = browser.find_element("xpath", xpath_next_page_button)
    next_page_button.click()


ct004()
