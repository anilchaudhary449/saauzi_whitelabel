import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.email = (By.ID, "email")
        self.password = (By.ID, "password")
        self.submitButton = (By.ID, "login-btn")

    def enter_email(self,email):
        emailAddress = self.wait.until(EC.visibility_of_element_located(self.email))
        emailAddress.send_keys(email)
        time.sleep(1)
    def enter_password(self,password):
        passwordField = self.wait.until(EC.visibility_of_element_located(self.password))
        passwordField.send_keys(password)
        time.sleep(1)
    def click_submit(self):
        submitButton = self.wait.until(EC.element_to_be_clickable(self.submitButton))
        submitButton.click()
        time.sleep(2)