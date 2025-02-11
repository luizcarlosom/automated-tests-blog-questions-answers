from selenium.webdriver.common.keys import Keys
from start_drive import start_drive
from dotenv import load_dotenv

import time
import os

load_dotenv()


def ct006() -> None:
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

    xpath_select_button = '//*[@id="filtroTema"]'
    select_button = browser.find_element("xpath", xpath_select_button)

    def slow_arrow_down(times):
        for _ in range(times):
            select_button.send_keys(Keys.ARROW_DOWN)
            time.sleep(1.5)
        select_button.send_keys(Keys.ENTER)
        time.sleep(3)

    select_button.send_keys(Keys.ARROW_DOWN)
    time.sleep(1.5)
    select_button.send_keys(Keys.ENTER)
    time.sleep(3)

    slow_arrow_down(1)
    slow_arrow_down(2)
    slow_arrow_down(3)
    slow_arrow_down(4)


ct006()
