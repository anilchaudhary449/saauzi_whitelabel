import pytest
from pages.clients import Clients
from pages.dashboard import Dashboard
from pages.login import Login
from pages.signup import SignUp
from pages.home import Home
from test_data.test_data import *

class TestSaauziWhitelabel:
    email = random_email()
    password = random_password()

    def test_homepage(self, browserSetup):
        homepage = Home(browserSetup)

        homepage.create_your_agency_free()
        homepage.see_how_it_works()
        homepage.click_login()
        homepage.click_sign_up()
        homepage.claim_your_spot()

    def test_signup(self, browserSetup):

        company_name = random_company_name()
        company_owner = random_company_owner()

        signup_page = SignUp(browserSetup)
        signup_page.click_signup()
        signup_page.enter_email(self.email)
        signup_page.enter_password(self.password)
        signup_page.enter_company_name(company_name)
        signup_page.enter_company_owner(company_owner)
        signup_page.click_submit()
        signup_page.click_logout()

    def test_login(self, browserSetup):
        login_page = Login(browserSetup)
        login_page.enter_email(self.email)
        login_page.enter_password(self.password)
        login_page.click_submit()
    def test_dashboard(self, browserSetup):
        dashboard_page = Dashboard(browserSetup)
        dashboard_page.dashboard()
        
    def test_client(self, browserSetup):
        client_name, client_email, client_phone = client_data()
        client = Clients(browserSetup)
        client.create_client()
        client.fill_form(client_name, client_email, client_phone)
        client.submit_form()

        # client.view_client()


if __name__ == "__main__":
    pytest.main('tests/saauzi_whitelabel_test.py -k "test_homepage or test_signup or test_login or test_client" -v -s')