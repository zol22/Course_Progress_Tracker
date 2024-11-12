import time
import pytest
from page_objects.login_page import LoginPage
from actions.access_email import  get_email_messages
from actions.code_extractor import extract_verification_code


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

        # Fetch the email messages and extract the verification code
        messages = get_email_messages()
        if messages:
            verification_code = extract_verification_code(messages)
            if verification_code:
                print(f"Verification code retrieved: {verification_code}")
                # Enter verification code in the login process
                # Locate the input to enter 6 digit code and type
            else:
                print("Failed to find verification code in the email messages.")
        else:
            print("Failed to retrieve email messages.")

