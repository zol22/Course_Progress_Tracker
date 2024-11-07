from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)