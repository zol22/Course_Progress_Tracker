import time
import pytest
from page_objects.login_page import LoginPage
from actions.access_email import EmailHandler
from actions.save_to_cvs import SaveToCVS
from actions.code_extractor import extract_verification_code
from page_objects.udemy_learning_page import UdemyLearningNavigator


class TestPositiveScenarios:

    #@pytest.mark.login
    @pytest.mark.dependency(name="login")  # Marks this test as the login dependency
    def test_positive_login(self,driver):
        # Instances
        login_page = LoginPage(driver)
        login_email = EmailHandler(driver)

        # Open Udemy login page
        login_page.open()
        time.sleep(3)


        # Type email and initiate login
        login_page.execute_login("ssormeno@hotmail.com")  # Email element is present but no visible

        verification_code = None

        # Perform Microsoft authentication and extract the verification code
        messages = login_email.get_email_messages()
        time.sleep(15)
        if messages:
            verification_code = extract_verification_code(messages)
            if verification_code:
                print(f"Verification code retrieved: {verification_code}")
                #login_page.type_verification_code(verification_code) #Enter the verification code
            else:
                print("Failed to find verification code in the email messages.")
        else:
            print("Failed to retrieve email messages.")

        time.sleep(5)

        if verification_code:
            login_page.type_verification_code(verification_code)
        else:
            raise Exception("Verification code not found, login process failed.")

        time.sleep(10)


    @pytest.mark.dependency(depends=["login"])  # Specifies dependency on login test
    def test_navigate_to_my_learning(self, driver):

        # Instances
        my_learning_page_navigator = UdemyLearningNavigator(driver)

        # Navigate to My Learning
        my_learning_page_navigator.navigate_to_my_learning_page()

        #Verify new page URL contains https://www.udemy.com/home/my-courses/learning/
        assert my_learning_page_navigator.expected_url == my_learning_page_navigator.current_url,"Actual URL is not the same as expected"

        # Assert that navigation to "My Learning" was successful
        assert "My Learning" in driver.title, "Navigation to My Learning failed"

        # Retrieve and save course data
        course_data = my_learning_page_navigator.get_learning_modules()

