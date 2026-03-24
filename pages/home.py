import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Home:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.loginButton = (By.XPATH, "//a[@href='/login']")
        self.signUpButton = (By.XPATH, "//a[@href='/register']")
        self.claimYourSpot = (By.XPATH,"//a[contains(@href,'/register?referral=claim-spot')]")
        self.createYourAgency = (By.XPATH,"//div[@class='lp-hero__ctas']//child::a[contains(normalize-space(.),'Create My Agency Free')]")
        self.seeHowItWorks = (By.XPATH,"//a[normalize-space(.)='See how it works']")
    def click_login(self):
        loginButton = self.wait.until(EC.element_to_be_clickable(self.loginButton))
        time.sleep(2)
        assert loginButton.is_displayed(), "Login button is not visible on the home page"
        assert loginButton.is_enabled(), "Login button is not enabled on the home page"
        time.sleep(2)
        loginButton.click()
        time.sleep(2)
        assert "login" in self.driver.current_url, "Clicking login did not navigate to the login page"
        self.driver.back()

    def click_sign_up(self):
        signUpButton = self.wait.until(EC.element_to_be_clickable(self.signUpButton))
        assert signUpButton.is_displayed(), "Sign Up button is not visible on the home page"
        assert signUpButton.is_enabled(), "Sign Up button is not enabled on the home page"
        signUpButton.click()
        time.sleep(2)
        assert "register" in self.driver.current_url, "Clicking sign up did not navigate to the registration page"
        self.driver.back()

    def claim_your_spot(self):
        claim_your_spot = self.wait.until(EC.element_to_be_clickable(self.claimYourSpot))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",claim_your_spot)
        assert claim_your_spot.is_displayed(), "Claim Your Spot button is not visible on the home page"
        time.sleep(2)
        assert claim_your_spot.is_enabled(), "Claim Your Spot button is not enabled on the home page"
        time.sleep(2)
        claim_your_spot.click()
        time.sleep(2)
        assert "register" in self.driver.current_url, "Clicking Claim Your Spot did not navigate to the registration page"
        self.driver.back()

    def create_your_agency_free(self):
        create_your_agency = self.wait.until(EC.presence_of_element_located(self.createYourAgency))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", create_your_agency)
        assert create_your_agency.is_displayed(), "Create Your Agency button is not visible on the home page"
        assert create_your_agency.is_enabled(), "Create Your Agency button is not enabled on the home page"
        create_your_agency.click()
        time.sleep(2)
        assert "register" in self.driver.current_url, "Clicking Create Your Agency did not navigate to the registration page"
        self.driver.back()

    def see_how_it_works(self):
        see_how_it_works = self.wait.until(EC.element_to_be_clickable(self.seeHowItWorks))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", see_how_it_works)
        assert see_how_it_works.is_displayed(), "See How It Works button is not visible on the home page"
        time.sleep(1)
        assert see_how_it_works.is_enabled(), "See How It Works button is not enabled on the home page"
        see_how_it_works.click()
        time.sleep(2)
        assert "#how" in self.driver.current_url, "Clicking See How It Works did not navigate to the correct page"
        self.driver.back()