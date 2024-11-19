
import pytest
from selenium import webdriver
import undetected_chromedriver as uc

@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Optional: If you want headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode
    chrome_options.add_argument("--no-sandbox")  # Useful for running on CI/CD environments
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("no-startup-window")  # Prevents opening a startup page

    # Ensure that no default URL is loaded upon starting
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")  # Optional: to avoid cache issues
    chrome_options.add_argument("--start-maximized")  # Optional: to maximize the browser window
    chrome_options.add_argument("--disable-automation")  # Disables automated browser features
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection of automation
    #chrome_options.add_argument("--disable-application-cache")  # Clear cache every time
    chrome_options.add_argument("--user-data-dir=/path/to/clean/profile")  # Use a fresh profile

    if browser == "chrome":
        my_driver = uc.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")

    # Clear cookies to prevent unwanted session issues
    my_driver.delete_all_cookies()

    yield my_driver

    print("Closing chrome driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )