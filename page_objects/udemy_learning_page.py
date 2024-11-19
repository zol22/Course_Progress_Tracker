from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class UdemyLearningNavigator(BasePage):

    __my_learning_button =(By.XPATH, "//a[@data-testid='my-courses']") # Dynamic My learning button
    _url = "https://www.udemy.com/home/my-courses/learning/"
    __module_selector = (By.XPATH, "//div[starts-with(@id, 'course-card-title-module--title')]//a")




    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def navigate_to_my_learning_page(self):
        super()._click(self.__my_learning_button)

    def get_learning_modules(self):
        # Locate and retrieve course data on the My Learning page
        modules = super()._click(self.__module_selector)
        modules_data = []


    '''
        for module in modules:
            title = module.find_element(By.CLASS_NAME, "course-title").text #course title
            progress = module.find_element(By.CLASS_NAME, "progress-percentage").text
            modules_data.append({"title": title, "progress": progress})
        return modules_data
'''

    @property
    def expected_url(self) -> str:
        return self._url

