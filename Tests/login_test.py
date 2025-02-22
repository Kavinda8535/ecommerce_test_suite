import sys
import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Utils.config import CONFIG
from Pages.login_page import LoginPage

# Ensure Utils folder is accessible for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_valid_login(driver):
    """
    Happy Path Test Case...
    :param driver:
    """

    # if you wanna see whats inside the variable you can check using print.
    # URL = CONFIG['BASE_URL']
    # USERNAME = CONFIG['USERNAME']
    # PASSWORD = CONFIG['PASSWORD']

    # print(f"Variable URL {URL}")
    # print(f"Variable USERNAME {USERNAME}")
    # print(f"Variable PASSWORD {PASSWORD}")


    login_page = LoginPage(driver)
    #login_page.open_page("https://magento.softwaretestingboard.com/customer/account/login/")
    #login_page.open_page(URL)
    login_page.open_page(CONFIG['BASE_URL'])
    time.sleep(1)
    #login_page.enter_unsername("dilii386xp@gmail.com")
    login_page.enter_unsername(CONFIG['USERNAME'])
    time.sleep(1)
    #login_page.enter_password("Kevin@123")
    login_page.enter_password(CONFIG['PASSWORD'])
    time.sleep(1)
    login_page.click_login()

    # Capture new URL after login
    new_url = driver.current_url
    print(f"New URL after login: {new_url}")

    # <editor-fold desc="Description">
    '''
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
    username_txt = driver.find_element(By.ID,"")
    password_txt = driver.find_element(By.ID,"")
    submit_btn = driver.find_element(By.XPATH,"")
    '''
    # </editor-fold>

    #username_txt.send_keys(username)
    #password_txt.send_keys(password)
    #time.sleep(1)
    #submit_btn.click()

    welcomeGreet = driver.find_element(By.CLASS_NAME, "logged-in").text
    #assert "Welcome, Kevin Pat!" in welcomeGreet this also correct...
    #assert welcomeGreet == "Welcome, Kevin Pat!" # we can compare the text like this as well...
    assert welcomeGreet in "Welcome, Kevin Pat!"

    time.sleep(1)


# TODO Write Test Cases for different scenarios like invalid login, empty login required check etc...

# TODO After the Test need to genarate Test report with Successfull and Fail Test Cases. Implement this.

#def test_invalid_login():
