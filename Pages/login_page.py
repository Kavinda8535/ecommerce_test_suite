from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_txtbx = (By.ID,"email")
        self.password_txtbx = (By.ID, "pass")
        self.login_btn = (By.XPATH, "//button[@id='send2']")
        #self.login_btn = (By.XPATH, " //*[@id='send2'] ") //*[@id="send2"]

    def open_page(self, url):
        self.driver.get(url)

    def enter_unsername(self, username):
        self.driver.find_element(*self.username_txtbx).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txtbx).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
