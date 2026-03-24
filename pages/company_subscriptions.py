from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CompanySubscriptions:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.subscriptionTab = (By.LINK_TEXT,"/company-subscriptions")
        self.createSubscriptionsButton = (By.XPATH,"//button[@class='btn btn-pumpkin px-8 py-2']")
        self.activeModal = (By.XPATH,"//div[@class='modal__container max-w-3/4! overflow-auto']")

    def click_subscription_tab(self):
        subscription_tab = self.wait.until(EC.element_to_be_clickable(self.subscriptionTab))
        assert subscription_tab.is_displayed(), "Subscription tab is not visible in the navigation bar"
        assert subscription_tab.is_enabled(), "Subscription tab is not enabled in the navigation bar"
        subscription_tab.click()
        self.wait.until(EC.url_contains("/company-subscriptions"))
        assert "/company-subscriptions" in self.driver.current_url, "Clicking Subscription tab did not navigate to the company subscriptions page"

    def click_create_subscription(self):
        create_subscription_button = self.wait.until(EC.element_to_be_clickable(self.createSubscriptionsButton))
        assert create_subscription_button.is_displayed(), "Create Subscription button is not visible on the company subscriptions page"
        assert create_subscription_button.is_enabled(), "Create Subscription button is not enabled on the company subscriptions page"
        create_subscription_button.click()
        assert self.driver.find_element(self.activeModal).is_displayed(), "Clicking Create Subscription did not open the subscription creation modal"