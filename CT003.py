from start_drive import start_drive
from dotenv import load_dotenv
import os

load_dotenv()


def ct003() -> None:
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

    browser.get(url_page + "perguntar")

    xpath_tittle_question_field = '//*[@id="titulo"]'
    tittle_question_field = browser.find_element("xpath", xpath_tittle_question_field)
    tittle_question_field.send_keys("Selenium")

    xpath_description_question_field = '//*[@id="descricao"]'
    description_question_field = browser.find_element(
        "xpath", xpath_description_question_field
    )
    description_question_field.send_keys(
        "Framework utilizado para criação de testes automatizados"
    )

    xpath_create_question_button = '//*[@id="btnAbrirModal"]'
    create_question_button = browser.find_element("xpath", xpath_create_question_button)
    create_question_button.click()

    xpath_form = '//*[@id="perguntaForm"]'
    form = browser.find_element("xpath", xpath_form)
    form.submit()


ct003()
