from start_drive import start_drive
from dotenv import load_dotenv
import os

load_dotenv()


def ct0002() -> None:
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


ct0002()
