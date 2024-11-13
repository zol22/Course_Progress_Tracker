import time
import pytest
from page_objects.login_page import LoginPage
from actions.access_email import  get_email_messages
from actions.code_extractor import extract_verification_code
from page_objects.my_learning_page import MyLearningPage



class TestPositiveScenarios:

    #@pytest.mark.login
    @pytest.mark.dependency(name="login")  # Marks this test as the login dependency
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
                login_page.type_verification_code(verification_code)
            else:
                print("Failed to find verification code in the email messages.")
        else:
            print("Failed to retrieve email messages.")

        time.sleep(10)



   #@pytest.mark.navigation
    @pytest.mark.dependency(depends=["login"])  # Specifies dependency on login test
    def test_navigate_to_my_learning(self, driver):

        # Instances
        my_learning_page = MyLearningPage(driver)

        # Navigate to My Learning
        my_learning_page.navigate_to_my_learning_page()

        #Verify new page URL contains https://www.udemy.com/home/my-courses/learning/
        assert my_learning_page.expected_url == my_learning_page.current_url,"Actual URL is not the same as expected"



