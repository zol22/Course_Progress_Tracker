from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginPage(BasePage):

    __url = "https://www.udemy.com/join/passwordless-auth/?locale=en_US&next=https%3A%2F%2Fwww.udemy.com%2F&response_type=html"
    __email_field = (By.ID, "form-group--1")
    __password_field = (By.NAME, "password")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
