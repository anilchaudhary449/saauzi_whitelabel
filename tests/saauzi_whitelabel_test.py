import pytest

from pages.login import Login
from pages.signup import SignUp
from test_data.test_data import *

class TestSaauziWhitelabel:
    email = random_email()
    password = random_password()
    def test_signup(self, browserSetup):

        company_name = random_company_name()
        company_owner = random_company_owner()

        signup_page = SignUp(browserSetup)
        signup_page.enter_email(self.email)
        signup_page.enter_password(self.password)
        signup_page.enter_company_name(company_name)
        signup_page.enter_company_owner(company_owner)
        signup_page.click_submit()

    def test_login(self, browserSetup):
        login_page = Login(browserSetup)
        login_page.enter_email(self.email)
        login_page.enter_password(self.password)
        login_page.click_submit()


if __name__ == "__main__":
    pytest.main()