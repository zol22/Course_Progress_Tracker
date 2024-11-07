Keep in mind:

### 1) Do we need to install Selenium each time we open and execute a new project using Python? 
 No, Once Selenium is installed in your environment, it will remain available across projects. You only need to install Selenium again if:

1) You start a new project in a new virtual environment that doesn’t yet have Selenium installed.
2) You switch to a different Python environment that lacks Selenium.

### 2) Install Selenium in the New Virtual Environment:
To install Selenium in the new virtual environment, activate the environment and install Selenium using pip:

- Activate the new virtual environment in your terminal:

   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
    
   - On macOS/Linux:
   ```
   source venv/bin/activate
   ```
- Install Selenium in the activated environment:
    ```
  pip install selenium
    ```
  
### 3) Expected Conditions:
Expected Conditions in Selenium WebDriver are predefined conditions that you can use to wait
for a certain state or event on a webpage before proceeding with further actions.
Selenium provides an expected_conditions module with commonly used conditions that you can apply to WebDriver’s WebDriverWait method.

### Why Use Expected Conditions?
It can prevent errors that occur when elements aren’t fully loaded or visible on the page. For example, 
without expected conditions, your script might try to interact with an element before it’s ready, causing a NoSuchElementException or 
ElementNotInteractableException.
### https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html