from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PurchasePlan:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.purchaseTabButton = (By.XPATH, "//a[@href='/purchase-plans' and contains(text(),'Purchase Plans')]")

    def navigate_to_purchase_plan(self):
        purchase_tab = self.wait.until(EC.element_to_be_clickable(self.purchaseTabButton))
        assert purchase_tab.is_displayed(), "Purchase Tab is not visible"
        assert purchase_tab.is_enabled(), "Purchase Tab is not enabled"
        purchase_tab.click()
        self.wait.until(EC.url_contains("/purchase-plans"))
        assert "/purchase-plans" in self.driver.current_url, "Clicking Purchase Plan did not navigate to the purchase plan page"