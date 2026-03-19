from selenium.webdriver import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SignUp:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.email = By.ID, "user_email"
        self.password =By.ID, "user_password"
        self.companyName =By.ID, "company_name"
        self.companyOwner =By.ID, "company_owner"
        self.submitButton = By.ID, "login-btn"

    def enter_company_name(self, company_name):
        companyName = self.wait.until(EC.presence_of_element_located(self.companyName))
        companyName.send_keys(companyName)
    def enter_email(self,email):
        emailAddress = self.wait.until(EC.presence_of_element_located(self.email))
        emailAddress.send_keys(email)
    def enter_password(self,password):
        passwordField = self.wait.until(EC.presence_of_element_located(self.password))
        passwordField.send_keys(password)
    def enter_company_owner(self, company_owner):
        companyOwner = self.wait.until(EC.presence_of_element_located(self.companyOwner))
        companyOwner.send_keys(company_owner)
    def click_submit(self):
        submitButton = self.wait.until(EC.element_to_be_clickable(self.submitButton))
        submitButton.click()