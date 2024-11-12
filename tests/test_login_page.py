import time

import pytest

from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    def test_positive_login(self,driver):
        # Instances
        login_page = LoginPage(driver)

        # Open the page
        login_page.open()

        time.sleep(3)

        # Type email student into email field , & Push button
        login_page.execute_login("ssormeno@hotmail.com")  # Email element is present but no visible

        time.sleep(10)



