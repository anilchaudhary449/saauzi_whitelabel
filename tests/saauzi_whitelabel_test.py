"""
tests/test_saauzi_whitelabel.py
================================
Master test file for the Saauzi White Label partner portal.
All tests for every page of the project live here so the full
suite can be controlled, filtered, and run from a single file.

Project test flow (mirrors saauzi_whitelabel_test.py order):
  1.  Homepage         — navigation links & CTAs
  2.  Signup           — positive & negative cases
  3.  Login            — positive & negative cases
  4.  Dashboard        — element & content verification
  5.  Clients          — create & view client
  6.  Company Subs     — create subscription & make payment
  7.  Client Logs      — navigate & verify table
  8.  Company Profile  — fill & submit update form
  9.  Purchase Plan    — navigate & verify page

Run the full suite:
    pytest tests/test_saauzi_whitelabel.py -v -s

Run only signup tests:
    pytest tests/test_saauzi_whitelabel.py -v -s -k "Signup"

Run only login tests:
    pytest tests/test_saauzi_whitelabel.py -v -s -k "Login"

Run only positive tests:
    pytest tests/test_saauzi_whitelabel.py -v -s -k "positive" (use markers below)

Run only negative tests:
    pytest tests/test_saauzi_whitelabel.py -v -s -k "negative"
"""

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home import Home
from pages.signup import SignUp
from pages.login import Login
from pages.dashboard import Dashboard
from pages.clients import Clients
from pages.company_subscriptions import CompanySubscriptions
from pages.client_logs import ClientLogs
from pages.company_profile import CompanyProfile
from pages.purchase_plan import PurchasePlan

from test_data.data import (
    random_email,
    random_password,
    random_company_name,
    random_company_owner,
    client_data,
    random_number_of_subscriptions,
    random_remarks,
    random_ref_id,
    payment_receipt,
    random_company_details,
    random_paragraph,
    INVALID_EMAIL_FORMAT,
    WHITESPACE_STRING,
    SQL_INJECTION_EMAIL_1,
    XSS_PAYLOAD_SCRIPT,
    INVALID_EMAIL_NO_AT,
    INVALID_EMAIL_NO_DOMAIN,
    WRONG_PASSWORD,
    UNREGISTERED_EMAIL,
    WRONG_ACCOUNT_EMAIL,
    SQL_INJECTION_EMAIL_2,
    SQL_INJECTION_PASSWORD,
    LONG_STRING,
    SPECIAL_CHARS_NAME,
    random_unsupported_tld_email,
    BOOLEAN_BLIND_SQLI,
)


# =============================================================================
# ① HOMEPAGE
# =============================================================================

class TestHomepage:
    """Verify all navigation links and CTAs on the landing page."""

    def test_homepage_login_link(self, browserSetup):
        """TC-HOME-01 — Login link is visible, enabled, navigates to /login."""
        homepage = Home(browserSetup)
        homepage.click_login()

    def test_homepage_signup_link(self, browserSetup):
        """TC-HOME-02 — Sign Up link is visible, enabled, navigates to /register."""
        homepage = Home(browserSetup)
        homepage.click_sign_up()

    def test_homepage_create_agency_free(self, browserSetup):
        """TC-HOME-03 — 'Create My Agency Free' CTA navigates to /register."""
        homepage = Home(browserSetup)
        homepage.create_your_agency_free()

    def test_homepage_claim_your_spot(self, browserSetup):
        """TC-HOME-04 — 'Claim Your Spot' CTA navigates to /register."""
        homepage = Home(browserSetup)
        homepage.claim_your_spot()

    def test_homepage_see_how_it_works(self, browserSetup):
        """TC-HOME-05 — 'See How It Works' scrolls to /#how anchor."""
        homepage = Home(browserSetup)
        homepage.see_how_it_works()


# =============================================================================
# ② SIGNUP PAGE
# =============================================================================

class TestSignup:
    """
    Positive & Negative test cases for /register.

    Shared credentials — generated once at class level.
    valid_email / valid_password are reused by the Login suite below via the
    class-level attributes exposed as TestSignup.registered_email / registered_password
    after test_signup_positive_valid_data completes.
    """

    # generated once — shared across all signup tests and passed to login suite
    valid_email    = random_email()
    valid_password = random_password()

    # ------------------------------------------------------------------
    # POSITIVE
    # ------------------------------------------------------------------

    def test_signup_positive_page_accessible(self, browserSetup):
        """TC-SU-P01 — 'Start for Free' navigates to /register."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        assert "register" in browserSetup.current_url, \
            "Registration page URL check failed"

    def test_signup_positive_email_field_visible(self, browserSetup):
        """TC-SU-P02 — Email field is visible and enabled on /register."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        field = browserSetup.find_element(*signup.email)
        assert field.is_displayed(), "Email field should be visible"
        assert field.is_enabled(),   "Email field should be enabled"

    def test_signup_positive_password_field_masks_input(self, browserSetup):
        """TC-SU-P03 — Password field uses type='password'."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        field = browserSetup.find_element(*signup.password)
        assert field.get_attribute("type") == "password", \
            "Password field should mask input"

    def test_signup_positive_company_name_field_visible(self, browserSetup):
        """TC-SU-P04 — Company Name field is visible and accepts input."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        field = browserSetup.find_element(*signup.companyName)
        assert field.is_displayed(), "Company Name field should be visible"
        assert field.is_enabled(),   "Company Name field should be enabled"

    def test_signup_positive_company_owner_field_visible(self, browserSetup):
        """TC-SU-P05 — Company Owner field is visible and accepts input."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        field = browserSetup.find_element(*signup.companyOwner)
        assert field.is_displayed(), "Company Owner field should be visible"
        assert field.is_enabled(),   "Company Owner field should be enabled"

    def test_signup_positive_submit_button_visible(self, browserSetup):
        """TC-SU-P06 — Submit button is visible and enabled on /register."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        btn = browserSetup.find_element(*signup.submitButton)
        assert btn.is_displayed(), "Submit button should be visible"
        assert btn.is_enabled(),   "Submit button should be enabled"

    def test_signup_positive_email_plus_alias_accepted(self, browserSetup):
        """TC-SU-P07 — Email field accepts RFC-5321 '+' alias format."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        field = browserSetup.find_element(*signup.email)
        field.clear()
        field.send_keys("user+alias@example.com")
        assert field.get_attribute("value") == "user+alias@example.com", \
            "Email field should accept '+' alias format"

    def test_signup_positive_valid_data(self, browserSetup):
        """
        TC-SU-P08 — Successful registration with all valid fields.
        Redirects to /dashboard then logs out.
        NOTE: This test registers valid_email / valid_password which are
        reused by TestLogin positive tests below.
        """
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.enter_email(self.valid_email)
        signup.enter_password(self.valid_password)
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(random_company_owner())
        signup.click_submit()       # asserts dashboard URL
        signup.click_logout()       # asserts login URL

    # ------------------------------------------------------------------
    # NEGATIVE
    # ------------------------------------------------------------------

    def test_signup_negative_empty_form(self, browserSetup):
        """TC-SU-N01 — Submitting a blank form must not redirect to /dashboard."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "Empty form should not navigate to dashboard"

    def test_signup_negative_invalid_email_format(self, browserSetup):
        """TC-SU-N02 — Email without '@' is rejected."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.enter_email(INVALID_EMAIL_FORMAT)
        signup.enter_password(random_password())
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "Invalid email format should not allow registration"

    def test_signup_negative_missing_email(self, browserSetup):
        """TC-SU-N03 — All fields filled except email must block registration."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_password(random_password())
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "Missing email should block registration"

    def test_signup_negative_missing_password(self, browserSetup):
        """TC-SU-N04 — All fields filled except password must block registration."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_email())
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "Missing password should block registration"

    def test_signup_negative_missing_company_name(self, browserSetup):
        """TC-SU-N05 — All fields filled except company name must block registration."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_email())
        signup.enter_password(random_password())
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "Missing company name should block registration"

    def test_signup_negative_missing_company_owner(self, browserSetup):
        """TC-SU-N06 — All fields filled except company owner must block registration."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_email())
        signup.enter_password(random_password())
        signup.enter_company_name(random_company_name())
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "Missing company owner should block registration"

    def test_signup_negative_duplicate_email(self, browserSetup):
        """
        TC-SU-N07 — Re-registering with an already-used email shows error toast.
        Uses valid_email registered in TC-SU-P08.
        """
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.enter_email(self.valid_email)
        signup.enter_password(random_password())
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        toast = WebDriverWait(browserSetup, 10).until(
            EC.visibility_of_element_located(signup.signupToast))
        assert toast.is_displayed(), \
            "Error toast should appear for a duplicate email"
        assert "dashboard" not in browserSetup.current_url, \
            "Duplicate email must not allow registration"

    def test_signup_negative_whitespace_company_name(self, browserSetup):
        """TC-SU-N08 — Company name of only spaces must block registration."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_email())
        signup.enter_password(random_password())
        signup.enter_company_name(WHITESPACE_STRING)
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "Whitespace-only company name should block registration"

    def test_signup_negative_sql_injection_email(self, browserSetup):
        """TC-SU-N09 — SQL injection in email must be safely rejected."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(SQL_INJECTION_EMAIL_1)
        signup.enter_password(random_password())
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        assert "dashboard" not in browserSetup.current_url, \
            "SQL injection in email should be rejected"

    def test_signup_negative_xss_company_name(self, browserSetup):
        """TC-SU-N10 — XSS payload in company name must not execute a browser alert."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_email())
        signup.enter_password(random_password())
        signup.enter_company_name(XSS_PAYLOAD_SCRIPT)
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        try:
            alert = browserSetup.switch_to.alert
            alert.dismiss()
            pytest.fail("XSS vulnerability: alert fired via company name field")
        except Exception:
            pass    # no alert = safe behaviour
            
        # Clean up session if the app safely registered the user with the XSS payload string
        if "dashboard" in browserSetup.current_url:
            signup.click_logout()

    def test_signup_negative_long_company_name(self, browserSetup):
        """TC-SU-N11  Reject overly long company names."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_email())
        signup.enter_password(random_password())
        signup.enter_company_name(LONG_STRING)
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        import time
        time.sleep(2)
        url_after = browserSetup.current_url
        if "dashboard" in url_after:
            signup.click_logout()
        assert "dashboard" not in url_after, \
            "Unreasonably long company name should block registration"

    @pytest.mark.xfail(reason="Bug: Backend currently registers users with special chars in Owner Name")
    def test_signup_negative_special_chars_owner(self, browserSetup):
        """TC-SU-N12  Reject non-alphabetic special characters in owner name."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_email())
        signup.enter_password(random_password())
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(SPECIAL_CHARS_NAME)
        signup.click_signup_btn_only()
        import time
        time.sleep(2)
        url_after = browserSetup.current_url
        if "dashboard" in url_after:
            signup.click_logout()
        assert "dashboard" not in url_after, \
            "Special characters in Owner Name should not be allowed"

    @pytest.mark.xfail(reason="Bug: Backend currently ignores TLD validation and allows fake TLDs")
    def test_signup_negative_unsupported_tld(self, browserSetup):
        """TC-SU-N13  Reject email addresses with invalid or fake TLDs."""
        signup = SignUp(browserSetup)
        signup.navigate_to_register()
        signup.clear_all_fields()
        signup.enter_email(random_unsupported_tld_email())
        signup.enter_password(random_password())
        signup.enter_company_name(random_company_name())
        signup.enter_company_owner(random_company_owner())
        signup.click_signup_btn_only()
        import time
        time.sleep(2)
        url_after = browserSetup.current_url
        if "dashboard" in url_after:
            signup.click_logout()
        assert "dashboard" not in url_after, \
            "Fake TLDs should be gracefully rejected"
# =============================================================================
# ③ LOGIN PAGE
# =============================================================================

class TestLogin:
    """
    Positive & Negative test cases for /login.

    Uses the credentials registered by TestSignup.test_signup_positive_valid_data.
    Class-level valid_email / valid_password must match TestSignup's values.
    Since both classes live in the same file and pytest collects top-to-bottom,
    TestSignup runs before TestLogin so the account is guaranteed to exist.
    """

    # Must match TestSignup.valid_email / valid_password exactly —
    # both are class-level so they evaluate at import time to the same values.
    valid_email    = TestSignup.valid_email
    valid_password = TestSignup.valid_password

    # ------------------------------------------------------------------
    # POSITIVE
    # ------------------------------------------------------------------

    def test_login_positive_page_accessible(self, browserSetup):
        """TC-LG-P01 — /login URL loads correctly."""
        login = Login(browserSetup)
        login.navigate_to_login()
        assert "login" in browserSetup.current_url, \
            "Browser should be on /login"

    def test_login_positive_email_field_visible(self, browserSetup):
        """TC-LG-P02 — Email field is visible and enabled on /login."""
        login = Login(browserSetup)
        login.navigate_to_login()
        field = browserSetup.find_element(*login.email)
        assert field.is_displayed(), "Email field should be visible"
        assert field.is_enabled(),   "Email field should be enabled"

    def test_login_positive_password_field_masks_input(self, browserSetup):
        """TC-LG-P03 — Password field is visible, enabled, type='password'."""
        login = Login(browserSetup)
        login.navigate_to_login()
        field = browserSetup.find_element(*login.password)
        assert field.is_displayed(), "Password field should be visible"
        assert field.is_enabled(),   "Password field should be enabled"
        assert field.get_attribute("type") == "password", \
            "Password field must mask input (type='password')"

    def test_login_positive_submit_button_visible(self, browserSetup):
        """TC-LG-P04 — Submit button is visible and enabled on /login."""
        login = Login(browserSetup)
        login.navigate_to_login()
        btn = browserSetup.find_element(*login.submitButton)
        assert btn.is_displayed(), "Submit button should be visible"
        assert btn.is_enabled(),   "Submit button should be enabled"

    def test_login_positive_email_field_accepts_input(self, browserSetup):
        """TC-LG-P05 — Email field retains typed value."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email("check.input@example.com")
        field = browserSetup.find_element(*login.email)
        assert field.get_attribute("value") == "check.input@example.com", \
            "Email field did not store the typed value"

    def test_login_positive_password_field_accepts_input(self, browserSetup):
        """TC-LG-P06 — Password field retains typed value."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_password("CheckInput@1")
        field = browserSetup.find_element(*login.password)
        assert field.get_attribute("value") == "CheckInput@1", \
            "Password field did not store the typed value"

    def test_login_positive_valid_credentials(self, browserSetup):
        """TC-LG-P07 — Valid credentials log in, show toast, reach dashboard."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(self.valid_password)
        login.click_submit()    # asserts toast + Claim Your Spot visible
        login.click_logout()    # asserts redirect back to /login

    def test_login_positive_success_toast_visible(self, browserSetup):
        """TC-LG-P08 — Success toast appears after a valid login."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(self.valid_password)
        browserSetup.find_element(*login.submitButton).click()
        toast = WebDriverWait(browserSetup, 15).until(
            EC.visibility_of_element_located(login.loginToast))
        assert toast.is_displayed(), "Success toast should appear after valid login"
        login.click_logout()

    def test_login_positive_redirects_to_dashboard(self, browserSetup):
        """TC-LG-P09 — Valid login redirects browser away from /login."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(self.valid_password)
        login.click_submit()
        assert "login" not in browserSetup.current_url, \
            "Browser should leave /login after successful login"
        login.click_logout()

    def test_login_positive_claim_your_spot_visible(self, browserSetup):
        """TC-LG-P10 — 'Claim Your Spot' is visible on dashboard after login."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(self.valid_password)
        login.click_submit()
        spot = WebDriverWait(browserSetup, 15).until(
            EC.visibility_of_element_located(login.ClaimYourSpot))
        assert spot.is_displayed(), \
            "'Claim Your Spot' should be visible after login"
        login.click_logout()

    # ------------------------------------------------------------------
    # NEGATIVE
    # ------------------------------------------------------------------

    def test_login_negative_empty_form(self, browserSetup):
        """TC-LG-N01 — Submitting a blank form must not leave /login."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.clear_all_fields()
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Empty form should keep browser on /login"

    def test_login_negative_invalid_email_no_at(self, browserSetup):
        """TC-LG-N02 — Email without '@' is rejected; browser stays on /login."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(INVALID_EMAIL_NO_AT)
        login.enter_password(self.valid_password)
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Email without '@' should not allow login"

    def test_login_negative_email_missing_domain(self, browserSetup):
        """TC-LG-N03 — Email with '@' but no domain is rejected."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(INVALID_EMAIL_NO_DOMAIN)
        login.enter_password(self.valid_password)
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Email missing domain should not allow login"

    def test_login_negative_missing_email(self, browserSetup):
        """TC-LG-N04 — Password filled, email blank — login must be blocked."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.clear_all_fields()
        login.enter_password(self.valid_password)
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Missing email should keep browser on /login"

    def test_login_negative_missing_password(self, browserSetup):
        """TC-LG-N05 — Email filled, password blank — login must be blocked."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.clear_all_fields()
        login.enter_email(self.valid_email)
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Missing password should keep browser on /login"

    def test_login_negative_wrong_password(self, browserSetup):
        """TC-LG-N06 — Correct email, wrong password — error toast shown."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(WRONG_PASSWORD)
        login.click_login_btn_only()
        toast = WebDriverWait(browserSetup, 10).until(
            EC.visibility_of_element_located(login.loginToast))
        assert toast.is_displayed(), "Error toast should appear for wrong password"
        assert "login" in browserSetup.current_url, \
            "Wrong password should keep browser on /login"

    def test_login_negative_unregistered_email(self, browserSetup):
        """TC-LG-N07 — Unregistered email triggers error toast."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(UNREGISTERED_EMAIL)
        login.enter_password(random_password())
        login.click_login_btn_only()
        toast = WebDriverWait(browserSetup, 10).until(
            EC.visibility_of_element_located(login.loginToast))
        assert toast.is_displayed(), "Error toast should appear for unregistered email"
        assert "login" in browserSetup.current_url, \
            "Unregistered email should keep browser on /login"

    def test_login_negative_wrong_email_valid_password(self, browserSetup):
        """TC-LG-N08 — Wrong email with another account's password must fail."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(WRONG_ACCOUNT_EMAIL)
        login.enter_password(self.valid_password)
        login.click_login_btn_only()
        toast = WebDriverWait(browserSetup, 10).until(
            EC.visibility_of_element_located(login.loginToast))
        assert toast.is_displayed(), "Error toast should appear for mismatched credentials"
        assert "login" in browserSetup.current_url, \
            "Mismatched credentials should keep browser on /login"

    def test_login_negative_sql_injection_email(self, browserSetup):
        """TC-LG-N09 — SQL injection in email must be safely rejected."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(SQL_INJECTION_EMAIL_2)
        login.enter_password(random_password())
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "SQL injection in email should be rejected"

    def test_login_negative_sql_injection_password(self, browserSetup):
        """TC-LG-N10 — SQL injection in password must be safely rejected."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(SQL_INJECTION_PASSWORD)
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "SQL injection in password should be rejected"

    def test_login_negative_xss_in_email(self, browserSetup):
        """TC-LG-N11 — XSS in email must not trigger a browser alert."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(XSS_PAYLOAD_SCRIPT)
        login.enter_password(random_password())
        login.click_login_btn_only()
        try:
            alert = browserSetup.switch_to.alert
            alert.dismiss()
            pytest.fail("XSS vulnerability: alert fired via email field")
        except Exception:
            pass
        assert "login" in browserSetup.current_url, \
            "XSS in email should keep browser on /login"

    def test_login_negative_whitespace_email(self, browserSetup):
        """TC-LG-N12 — Email of only spaces must be rejected."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(WHITESPACE_STRING)
        login.enter_password(self.valid_password)
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Whitespace-only email should keep browser on /login"

    def test_login_negative_whitespace_password(self, browserSetup):
        """TC-LG-N13  Password of only spaces must be rejected."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(WHITESPACE_STRING)
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Whitespace-only password should keep browser on /login"

    def test_login_negative_blind_sqli(self, browserSetup):
        """TC-LG-N14  Advanced boolean-blind SQL injection attempt."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(BOOLEAN_BLIND_SQLI)
        login.enter_password(random_password())
        login.click_login_btn_only()
        assert "login" in browserSetup.current_url, \
            "Boolean-blind SQL Injection should be gracefully handled"

    def test_login_negative_case_sensitive_password(self, browserSetup):
        """TC-LG-N14 — Case-swapped password must be rejected."""
        login = Login(browserSetup)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(self.valid_password.swapcase())
        login.click_login_btn_only()
        toast = WebDriverWait(browserSetup, 10).until(
            EC.visibility_of_element_located(login.loginToast))
        assert toast.is_displayed(), "Error toast should appear for case-swapped password"
        assert "login" in browserSetup.current_url, \
            "Case-swapped password should keep browser on /login"


# =============================================================================
# ④ DASHBOARD  (requires active login — done inside each test)
# =============================================================================

class TestDashboard:
    """Verify dashboard elements after login with registered credentials."""

    valid_email    = TestSignup.valid_email
    valid_password = TestSignup.valid_password

    def _login(self, driver):
        """Helper: log in and land on the dashboard."""
        login = Login(driver)
        login.navigate_to_login()
        login.enter_email(self.valid_email)
        login.enter_password(self.valid_password)
        login.click_submit()

    def test_dashboard_elements_and_content(self, browserSetup):
        """TC-DB-01 — All dashboard cards, client summary, and filter are correct."""
        self._login(browserSetup)
        dashboard = Dashboard(browserSetup)
        dashboard.dashboard()


# =============================================================================
# ⑤ CLIENTS  (stays logged in from Dashboard test)
# =============================================================================

class TestClients:
    """Create a client and verify the clients list page."""

    def test_clients_create_client(self, browserSetup):
        """TC-CL-01 — Create a new client and confirm redirect back to /clients."""
        client_name, client_email, client_phone = client_data()
        client = Clients(browserSetup)
        client.create_client()
        client.fill_form(client_name, client_email, client_phone)
        client.submit_form()


# =============================================================================
# ⑥ COMPANY SUBSCRIPTIONS  (stays logged in)
# =============================================================================

class TestCompanySubscriptions:
    """Create a subscription, view it, and record a payment."""

    def test_company_subscriptions_full_flow(self, browserSetup):
        """TC-CS-01 — Create subscription → view → make payment → assert toast."""
        company_subscription = CompanySubscriptions(browserSetup)
        company_subscription.click_subscription_tab()
        company_subscription.click_create_subscription()
        company_subscription.fill_subscription_form(random_number_of_subscriptions())
        company_subscription.create_subscription()
        company_subscription.view_subscription()
        company_subscription.make_payment()
        company_subscription.fill_payment_details(
            random_remarks(),
            random_ref_id(),
            payment_receipt(),
        )


# =============================================================================
# ⑦ CLIENT LOGS  (stays logged in)
# =============================================================================

class TestClientLogs:
    """Verify the Client Logs page is reachable and shows a table."""

    def test_client_logs_navigation_and_table(self, browserSetup):
        """TC-CL-LOG-01 — Navigate to /client-logs and verify table is visible."""
        client_logs = ClientLogs(browserSetup)
        client_logs.navigate_to_client_logs()


# =============================================================================
# ⑧ COMPANY PROFILE  (stays logged in)
# =============================================================================

class TestCompanyProfile:
    """Update every field on the Company Profile page and assert success toast."""

    def test_company_profile_update(self, browserSetup):
        """TC-CP-01 — Fill all company profile fields and submit successfully."""
        (
            company_name, company_email, company_owner,
            company_phone, company_address,
            company_website, company_vat,
            company_logo, company_favicon,
        ) = random_company_details()

        company_profile = CompanyProfile(browserSetup)
        company_profile.navigate_to_company_profile()
        company_profile.fill_company_details(
            company_name, company_email, company_owner,
            company_phone, company_address,
            company_website, company_vat,
            company_logo, company_favicon,
            random_paragraph(),
        )
        company_profile.click_submit()


# =============================================================================
# ⑨ PURCHASE PLAN  (stays logged in)
# =============================================================================

class TestPurchasePlan:
    """Verify the Purchase Plans page is reachable."""

    def test_purchase_plan_navigation(self, browserSetup):
        """TC-PP-01 — Navigate to /purchase-plans and confirm URL."""
        purchase_plan = PurchasePlan(browserSetup)
        purchase_plan.navigate_to_purchase_plan()