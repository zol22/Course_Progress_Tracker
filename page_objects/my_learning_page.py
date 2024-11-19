from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class MyLearningPage(BasePage):

    __my_learning_button = (By.ID, "u107-popper-trigger--36")
    _url = "https://www.udemy.com/home/my-courses/learning/"


    def navigate_to_my_learning_page(self):
        super()._click(self.__my_learning_button)

    @property
    def expected_url(self) -> str:
        return self._url

