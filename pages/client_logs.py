import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ClientLogs:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.ClientLogsTab = (By.XPATH,"//a[@href='/client-logs' and contains(normalize-space(.),'Client Logs')]")
        self.ClientLogsTable = (By.TAG_NAME,"table")
    def navigate_to_client_logs(self):
        client_log_tab = self.wait.until(EC.element_to_be_clickable(self.ClientLogsTab))
        assert client_log_tab.is_displayed(), "Client Logs tab is not visible in the navigation bar"
        assert client_log_tab.is_enabled(), "Client Logs tab is not enabled in the navigation bar"
        time.sleep(2)
        client_log_tab.click()
        self.wait.until(EC.url_contains("/client-logs"))
        assert "/client-logs" in self.driver.current_url, "Clicking Client Logs did not navigate to the client logs page"
        assert self.wait.until(EC.visibility_of_element_located(self.ClientLogsTable)).is_displayed(), "Client Logs table is not visible on the client logs page"

