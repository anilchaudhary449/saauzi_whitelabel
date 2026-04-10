import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://partner.saauzi.com/"


class SignUp:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        # ── Locators (identical to original pages/signup.py) ──────────────────
        self.signup        = (By.XPATH, "//a[@href='/register' and contains(text(),'Start for Free')]")
        self.email         = (By.ID, "company_email")
        self.password      = (By.ID, "user_password")
        self.companyName   = (By.ID, "company_name")
        self.companyOwner  = (By.ID, "company_owner")
        self.submitButton  = (By.ID, "login-btn")
        self.profileButton = (By.ID, "appbar-user-dropdown")
        self.logoutButton  = (By.XPATH, "//div[@class='dropdown__item my-2']")
        self.signupToast   = (By.XPATH, "//div[@class='alert__message']")

    # ── Navigation ────────────────────────────────────────────────────────────

    def go_to_home(self):
        """Hard-navigate to home — guarantees 'Start for Free' link is in DOM."""
        self.driver.get(BASE_URL)
        time.sleep(1)

    def navigate_to_register(self):
        """
        Always-safe entry to /register regardless of current browser state.
        Goes home first so the 'Start for Free' anchor is always findable.
        """
        self.go_to_home()
        signup_btn = self.wait.until(EC.element_to_be_clickable(self.signup))
        assert signup_btn.is_displayed(), "Sign Up button is not visible on the home page"
        assert signup_btn.is_enabled(),   "Sign Up button is not enabled on the home page"
        signup_btn.click()
        time.sleep(1)
        assert "register" in self.driver.current_url, \
            "Clicking Sign Up did not navigate to the registration page"

    # kept for backward-compat with saauzi_whitelabel_test.py
    def click_signup(self):
        self.navigate_to_register()

    # ── Field helpers ─────────────────────────────────────────────────────────

    def clear_all_fields(self):
        """Clear every form field — ensures no stale input between tests."""
        for locator in (self.email, self.password, self.companyName, self.companyOwner):
            try:
                self.driver.find_element(*locator).clear()
            except Exception:
                pass

    def enter_email(self, email):
        field = self.wait.until(EC.visibility_of_element_located(self.email))
        field.clear()
        field.send_keys(email)
        time.sleep(0.5)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.password))
        field.clear()
        field.send_keys(password)
        time.sleep(0.5)

    def enter_company_name(self, company_name):
        field = self.wait.until(EC.visibility_of_element_located(self.companyName))
        field.clear()
        field.send_keys(company_name)
        time.sleep(0.5)

    def enter_company_owner(self, company_owner):
        field = self.wait.until(EC.visibility_of_element_located(self.companyOwner))
        field.clear()
        field.send_keys(company_owner)
        time.sleep(0.5)

    # ── Submit helpers ────────────────────────────────────────────────────────

    def click_submit(self):
        """Submit and assert successful redirect to /dashboard."""
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.submitButton))
        submit_btn.click()
        time.sleep(1)
        self.wait.until(EC.url_contains("dashboard"))
        assert "dashboard" in self.driver.current_url, \
            "Signup failed or did not redirect to dashboard"

    def click_signup_btn_only(self):
        """
        Click submit WITHOUT asserting a redirect.
        Used by negative tests where the form is expected to stay on /register.
        """
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.submitButton))
        submit_btn.click()
        time.sleep(2)

    # ── Post-signup ───────────────────────────────────────────────────────────

    def click_logout(self):
        self.wait.until(EC.invisibility_of_element_located(self.signupToast))
        profile_btn = self.wait.until(EC.element_to_be_clickable(self.profileButton))
        profile_btn.click()
        time.sleep(1)
        logout_btn = self.wait.until(
            EC.presence_of_element_located(self.logoutButton))
        logout_btn.click()
        time.sleep(1)
        assert "login" in self.driver.current_url, \
            "Logout failed or did not redirect to login page"