import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginPage(BasePage):

    __url = "https://www.udemy.com/join/passwordless-auth/"
    __email_field = (By.CSS_SELECTOR, "input[name='email']")
    __continue_with_email_button =(By.XPATH,"//*[@id='udemy']/div[1]/div[2]/div/div/main/div/div/form/button")
    __human = (By.XPATH, "// *[ @ id = 'kGtPC2'] / div / label / input")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, email: str):
        super()._type(self.__email_field, email)
        super()._click(self.__continue_with_email_button)

