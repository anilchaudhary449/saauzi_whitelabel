import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CompanySubscriptions:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.subscriptionTab = (By.XPATH,"//a[@title='Company Subcriptions']")
        self.createSubscriptionsButton = (By.XPATH,"//button[@class='btn btn-pumpkin px-8 py-2']")
        self.activeModal = (By.XPATH,"//div[@class='modal__container max-w-3/4! overflow-auto']")
        self.numberOfSubscriptions = (By.ID,"no_of_subscriptions")
        self.subscriptionPlan = (By.ID,"subscription_plan")
        self.optionsList = (By.XPATH,"//select[@id='subscription_plan']//option[not(@disabled) and @value!='']")
        self.createButton = (By.XPATH,"//button[normalize-space(.)='Create']")
        self.toastMessage = (By.XPATH,"//div[@class='alert__message']")
        self.viewButton = (By.XPATH,"//a[@title='View Subscription']")
        self.makePaymentButton = (By.XPATH,"//a[@title='Make Payment']")
        self.paymentMethod = (By.ID, "payment_method")
        self.paymentMethodOptions = (By.XPATH,"//select[@id='payment_method']//option[not(@disabled) and @value!='']")
        self.paymentsRemarks = (By.ID, "payment_remarks")
        self.refID = (By.ID,"reference_id")
        self.paymentReceipt = (By.ID,"payment_receipt")
        self.paymentSubmitButton = (By.XPATH,"//button[contains(., 'Confirm Payment')]")

    def click_subscription_tab(self):
        subscription_tab = self.wait.until(EC.visibility_of_element_located(self.subscriptionTab))
        assert subscription_tab.is_displayed(), "Subscription tab is not visible in the navigation bar"
        assert subscription_tab.is_enabled(), "Subscription tab is not enabled in the navigation bar"
        time.sleep(1)
        subscription_tab.click()
        self.wait.until(EC.url_contains("/company-subscriptions"))
        assert "/company-subscriptions" in self.driver.current_url, "Clicking Subscription tab did not navigate to the company subscriptions page"

    def click_create_subscription(self):
        create_subscription_button = self.wait.until(EC.element_to_be_clickable(self.createSubscriptionsButton))
        assert create_subscription_button.is_displayed(), "Create Subscription button is not visible on the company subscriptions page"
        assert create_subscription_button.is_enabled(), "Create Subscription button is not enabled on the company subscriptions page"
        time.sleep(1)
        create_subscription_button.click()
        time.sleep(1)
        activeModal = self.wait.until(EC.visibility_of_element_located(self.activeModal))
        time.sleep(1)
        assert activeModal.is_displayed(), "Clicking Create Subscription did not open the subscription creation modal"

    def fill_subscription_form(self, number_of_subscriptions):
        number_of_subscriptions_field = self.wait.until(EC.visibility_of_element_located(self.numberOfSubscriptions))
        subscription_plan_dropdown = self.wait.until(EC.visibility_of_element_located(self.subscriptionPlan))
        number_of_subscriptions_field.clear()
        number_of_subscriptions_field.send_keys(number_of_subscriptions)
        subscription_plan_dropdown.click()
        expected_plans = ["Monthly (Rs 750 per account)", "Yearly (Rs 6,000 per account)"]

        options = self.wait.until(EC.presence_of_all_elements_located(self.optionsList))
        option_texts = [option.text for option in options]
        for plan in expected_plans:
            assert plan in option_texts, f"Subscription plan '{plan}' is not available in dropdown. Available options: '{option_texts}'"
        
        option = random.choice(options)
        option.click()
    
    def create_subscription(self):
        create_button = self.wait.until(EC.element_to_be_clickable(self.createButton))
        assert create_button.is_displayed(), "Create button is not visible on the subscription creation modal"
        assert create_button.is_enabled(), "Create button is not enabled on the subscription creation modal"
        time.sleep(1)
        create_button.click()
        time.sleep(1)
        toast_message = self.wait.until(EC.visibility_of_element_located(self.toastMessage))
        assert toast_message.is_displayed(), "Toast message is not visible on the company subscriptions page"
        assert toast_message.text == "Subscription created successfully.", f"Unexpected toast text: {toast_message.text}"
    
    def view_subscription(self):
        view_button = self.wait.until(EC.visibility_of_element_located(self.viewButton))
        assert view_button.is_displayed(), "View button is not visible on the company subscriptions page"
        assert view_button.is_enabled(), "View button is not enabled on the company subscriptions page"
        time.sleep(1)
        view_button.click()
        time.sleep(1)
        assert "view" in self.driver.current_url, "Clicking View button did not navigate to the company subscriptions page"
        self.driver.back()

    def make_payment(self):
        make_payment_button = self.wait.until(EC.visibility_of_element_located(self.makePaymentButton))
        assert make_payment_button.is_displayed(), "Make Payment button is not visible on the company subscriptions page"
        assert make_payment_button.is_enabled(), "Make Payment button is not enabled on the company subscriptions page"
        time.sleep(1)
        make_payment_button.click()
        time.sleep(1)
        assert "payment" in self.driver.current_url, "Clicking Make Payment button did not navigate to the company subscriptions page"


    def fill_payment_details(self,remarks, ref_ID, receipt):
        payment_method = self.wait.until(EC.presence_of_element_located(self.paymentMethod))
        payment_method.click()
        payment_method_options = self.wait.until(EC.presence_of_all_elements_located(self.paymentMethodOptions))
        payment_method_option = random.choice(payment_method_options)
        payment_method_option.click()
        time.sleep(1)
        assert payment_method_option.is_selected(), "Payment method option is not selected"
        remarks_field = self.wait.until(EC.visibility_of_element_located(self.paymentsRemarks))
        ref_id_field = self.wait.until(EC.visibility_of_element_located(self.refID))
        remarks_field.clear()
        remarks_field.send_keys(remarks)
        ref_id_field.clear()
        ref_id_field.send_keys(ref_ID)
        payment_receipt = self.wait.until(EC.presence_of_element_located(self.paymentReceipt))
        payment_receipt.send_keys(receipt)
        time.sleep(1)
        payment_submit_button = self.wait.until(EC.element_to_be_clickable(self.paymentSubmitButton))
        assert payment_submit_button.is_displayed(), "Payment submit button is not visible on the company subscriptions page"
        assert payment_submit_button.is_enabled(), "Payment submit button is not enabled on the company subscriptions page"
        time.sleep(1)
        payment_submit_button.click()
        time.sleep(1)
        toast_message = self.wait.until(EC.visibility_of_element_located(self.toastMessage))
        assert toast_message.is_displayed(), "Toast message is not visible on the company subscriptions page"
        assert toast_message.text == "Subscription payment updated successfully.", f"Unexpected toast text: {toast_message.text}"

        self.driver.back()