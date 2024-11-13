from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):

    __url = "https://www.udemy.com/join/passwordless-auth/"
    __email_field = (By.CSS_SELECTOR, "input[name='email']")
    __continue_with_email_button =(By.XPATH,"//*[@id='udemy']/div[1]/div[2]/div/div/main/div/div/form/button")
    __verification_code_input = (By.ID,"u446-form-group--39")
    __login_button = (By.XPATH, "//*[@id='udemy']/div[1]/div[2]/div/div/main/div/div/div[3]/form/div[2]/button")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, email: str):
        super()._type(self.__email_field, email)
        super()._click(self.__continue_with_email_button)

    def type_verification_code(self, verification_code: int):
        super()._type(self.__verification_code_input, verification_code)
        super()._click(self.__login_button)



