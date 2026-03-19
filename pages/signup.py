import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SignUp:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.email = (By.ID, "company_email")
        self.password = (By.ID, "user_password")
        self.companyName = (By.ID, "company_name")
        self.companyOwner = (By.ID, "company_owner")
        self.submitButton = (By.ID, "login-btn")

    def enter_company_name(self, company_name):
        company_Name = self.wait.until(EC.visibility_of_element_located(self.companyName))
        company_Name.send_keys(company_name)
        time.sleep(1)
    def enter_email(self,email):
        emailAddress = self.wait.until(EC.visibility_of_element_located(self.email))
        emailAddress.send_keys(email)
        time.sleep(1)
    def enter_password(self,password):
        passwordField = self.wait.until(EC.visibility_of_element_located(self.password))
        passwordField.send_keys(password)
        time.sleep(1)
    def enter_company_owner(self, company_owner):
        companyOwner = self.wait.until(EC.visibility_of_element_located(self.companyOwner))
        companyOwner.send_keys(company_owner)
        time.sleep(1)
    def click_submit(self):
        submitButton = self.wait.until(EC.element_to_be_clickable(self.submitButton))
        submitButton.click()
        time.sleep(2)