
import pytest
from selenium import webdriver
import undetected_chromedriver as uc

#@pytest.fixture(param=["chrome", "firefox"])
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = uc.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    # implicit wait
    #my_driver.implicitly_wait(10)
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )