import pytest
from pages.signup import SignUp
from test_data.test_data import *

class TestSignup:

    def test_signup(self, browserSetup):
        email = random_email()
        password = random_password()
        company_name = random_company_name()
        company_owner = random_company_owner()

        signup_page = SignUp(browserSetup)
        signup_page.enter_email(email)
        signup_page.enter_password(password)
        signup_page.enter_company_name(company_name)
        signup_page.enter_company_owner(company_owner)
        signup_page.click_submit()



if __name__ == "__main__":
    pytest.main()