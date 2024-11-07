import pytest

from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    def test_positive_login(self,driver):
        # Instances
        login_page = LoginPage(driver)

        # Open the page
        login_page.open()