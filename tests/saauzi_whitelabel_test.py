import pytest

from pages.client_logs import ClientLogs
from pages.clients import Clients
from pages.company_subscriptions import CompanySubscriptions
from pages.dashboard import Dashboard
from pages.login import Login
from pages.signup import SignUp
from pages.home import Home
from pages.company_profile import CompanyProfile
from pages.purchase_plan import PurchasePlan
from test_data.test_data import *

class TestSaauziWhitelabel:
    email = random_email()
    password = random_password()

    def test_homepage(self, browserSetup):
        homepage = Home(browserSetup)

        homepage.click_login()
        homepage.click_sign_up()
        homepage.create_your_agency_free()
        homepage.claim_your_spot()
        homepage.see_how_it_works()

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
    def test_company_subscriptions(self, browserSetup):
    
        no_of_subscriptions = random_number_of_subscriptions()
        remarks = random_remarks()
        ref_id = random_ref_id()
        receipt = payment_receipt()

        company_subscription = CompanySubscriptions(browserSetup)
        company_subscription.click_subscription_tab()
        company_subscription.click_create_subscription()
        company_subscription.fill_subscription_form(no_of_subscriptions)
        company_subscription.create_subscription()
        company_subscription.view_subscription()
        company_subscription.make_payment()
        company_subscription.fill_payment_details(remarks, ref_id, receipt)


    def test_clients_logs(self, browserSetup):
        client_logs = ClientLogs(browserSetup)
        client_logs.navigate_to_client_logs()
    
    def test_company_profile_update(self, browserSetup):
        company_name, company_email, company_owner,\
        company_phone, company_address,\
        company_website, company_vat, \
        company_logo, company_favicon = random_company_details()
        company_details = random_paragraph()

        company_profile = CompanyProfile(browserSetup)
        company_profile.navigate_to_company_profile()
        company_profile.fill_company_details(company_name, company_email, company_owner, company_phone, company_address, company_website, company_vat, company_logo, company_favicon, company_details)
        company_profile.click_submit()

    def test_purchase_plan(self, browserSetup):
        purchase_plan = PurchasePlan(browserSetup)
        purchase_plan.navigate_to_purchase_plan()
        

if __name__ == "__main__":
    pytest.main('tests/saauzi_whitelabel_test.py \
    -k "test_signup or test_login \
    or test_client or test_company_subscription \
    " \
    -v -s')