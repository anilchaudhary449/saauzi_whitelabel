import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://partner.saauzi.com/login"


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        # ── Locators (identical to original pages/login.py) ───────────────────
        self.email         = (By.ID, "email")
        self.password      = (By.ID, "password")
        self.submitButton  = (By.ID, "login-btn")
        self.loginToast    = (By.XPATH, "//div[@class='alert__message']")
        self.ClaimYourSpot = (By.CSS_SELECTOR, "button.btn.btn-pumpkin--outline")

        # ── Extra locators used by logout ─────────────────────────────────────
        self.profileButton = (By.ID, "appbar-user-dropdown")
        self.logoutButton  = (By.XPATH, "//div[@class='dropdown__item my-2']")

    # ── Navigation ────────────────────────────────────────────────────────────

    def navigate_to_login(self):
        """
        Hard-navigate to /login via driver.get() — always safe regardless of
        what page the browser is currently on (dashboard, register, anywhere).
        Never relies on clicking a nav link whose presence depends on page state.
        """
        self.driver.get(LOGIN_URL)
        self.wait.until(EC.url_contains("login"))
        time.sleep(1)

    # ── Field helpers ─────────────────────────────────────────────────────────

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

    def clear_all_fields(self):
        """Wipe both fields — prevents stale values leaking between tests."""
        for locator in (self.email, self.password):
            try:
                self.driver.find_element(*locator).clear()
            except Exception:
                pass

    # ── Submit helpers ────────────────────────────────────────────────────────

    def click_submit(self):
        """
        Submit and assert a successful login.
        Kept identical to the original so saauzi_whitelabel_test.py needs
        no changes.
        """
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.submitButton))
        submit_btn.click()
        login_toast = self.wait.until(
            EC.visibility_of_element_located(self.loginToast))
        assert login_toast.is_displayed(), \
            "Login failed or no feedback message displayed"
        claim_your_spot = self.wait.until(
            EC.visibility_of_element_located(self.ClaimYourSpot))
        assert claim_your_spot.is_displayed(), \
            "Login failed or did not redirect to dashboard"
        assert claim_your_spot.is_enabled(), \
            "Claim Your Spot button is not enabled after login"

    def click_login_btn_only(self):
        """
        Click submit WITHOUT waiting for a redirect or asserting success.
        Used by every negative test — the form is expected to stay on /login
        and show a validation error or toast.
        """
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.submitButton))
        submit_btn.click()
        time.sleep(2)   # let HTML5 validation / server error toast render

    # ── Post-login ────────────────────────────────────────────────────────────

    def click_logout(self):
        """Logout from the dashboard and assert the browser returns to /login."""
        self.wait.until(EC.invisibility_of_element_located(self.loginToast))
        profile_btn = self.wait.until(
            EC.element_to_be_clickable(self.profileButton))
        profile_btn.click()
        time.sleep(1)
        logout_btn = self.wait.until(
            EC.presence_of_element_located(self.logoutButton))
        logout_btn.click()
        time.sleep(1)
        assert "login" in self.driver.current_url, \
            "Logout failed or did not redirect to login page"