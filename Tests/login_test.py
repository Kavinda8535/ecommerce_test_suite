import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.login_page import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
    time.sleep(1)
    login_page.enter_unsername("dilii386xp@gmail.com")
    time.sleep(1)
    login_page.enter_password("Kevin@123")
    time.sleep(1)
    login_page.click_login()

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

    welcomeGreet = driver.find_element(By.CLASS_NAME, "logged-in")
    #assert "Welcome, Kevin Pat!" in welcomeGreet #logged-in
    assert "logged-in" in welcomeGreet  # logged-in

    time.sleep(1)

    '''
    login_page = LoginPage(driver)
    login_page.login("dilii386xp@gmail.com", "Kevin@123")
    assert "dashboard" in driver.current_url
    '''
