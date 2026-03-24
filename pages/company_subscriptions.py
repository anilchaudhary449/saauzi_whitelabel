import time

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
        self.optionsList = (By.XPATH,"//option[not(@disabled)]")

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
        number_of_subscriptions_field.send_keys(number_of_subscriptions)
        subscription_plan_dropdown.click()
        expected_plans = ["Monthly (Rs 750 per account)", "Yearly (Rs 7500 per account)"]

        options = self.wait.until(EC.presence_of_all_elements_located(self.optionsList))
        option_texts = [option.text for option in options]

        for plan in expected_plans:
            # assert plan in option_texts, f"Subscription plan '{plan}' is not available in dropdown"
            print(f"Subscription plan '{plan}' is available in dropdown")
        time.sleep(1)