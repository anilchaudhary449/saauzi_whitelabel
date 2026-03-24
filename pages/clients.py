import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Clients:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.ClientsTab = (By.XPATH,"//a[@href='/clients' and contains(text(),'Clients')]")
        self.CreateClientButton = (By.XPATH,"//div[contains(@class,'items-center') and normalize-space(.)='Create New Client']")
        self.CreateClient = (By.XPATH,"//div[@class='flex items-center gap-x-2' and contains(normalize-space(.),'Create Client')]")
        self.actionView = (By.XPATH,"//button[@title='View Client']")

    def create_client(self):
        clients_tab = self.wait.until(EC.element_to_be_clickable(self.ClientsTab))
        assert clients_tab.is_displayed(), "Clients tab is not visible in the navigation bar"
        assert clients_tab.is_enabled(), "Clients tab is not enabled in the navigation bar"
        clients_tab.click()

        create_client_button = self.wait.until(EC.presence_of_element_located(self.CreateClientButton))
        assert create_client_button.is_displayed(), "Create Client button is not visible on the Clients page"
        assert create_client_button.is_enabled(), "Create Client button is not enabled on the Clients page"
        time.sleep(2)
        create_client_button.click()
        self.wait.until(EC.url_contains("/clients/create"))
        assert "/clients/create" in self.driver.current_url, "Clicking Create Client did not navigate to the client creation page"

    def fill_form(self, client_name, client_email_address, client_phone):
        client_name_field = self.wait.until(EC.visibility_of_element_located((By.ID,"client_name")))
        client_email_field = self.wait.until(EC.visibility_of_element_located((By.ID,"client_email")))
        client_phone_field = self.wait.until(EC.visibility_of_element_located((By.ID,"client_phone_number")))
        client_name_field.send_keys(client_name)
        client_email_field.send_keys(client_email_address)
        client_phone_field.send_keys(client_phone)

    def submit_form(self):
        create_client_button = self.wait.until(EC.presence_of_element_located(self.CreateClient))
        assert create_client_button.is_displayed(), "Create Client button is not visible on the client creation page"
        assert create_client_button.is_enabled(), "Create Client button is not enabled on the client creation page"
        create_client_button.click()
        WebDriverWait(self.driver, 60).until(EC.url_contains("/clients"))
        assert "/clients" in self.driver.current_url, "Submitting the client creation form did not navigate back to the clients page"

    def view_client(self):
        view_button = self.wait.until(EC.presence_of_element_located(self.actionView))
        assert view_button.is_displayed(), "View Client button is not visible in the clients list"
        assert view_button.is_enabled(), "View Client button is not enabled in the clients list"
        time.sleep(0.5)
        view_button.click()
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element("/clients"))
        assert "/details" in self.driver.current_url, "Clicking View Client did not navigate to the client details page"