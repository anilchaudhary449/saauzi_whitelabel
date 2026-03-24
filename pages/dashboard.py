import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_data.test_data import dashboard_contents, client_summary_contents
from selenium.webdriver.support.wait import WebDriverWait

class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.ToastMessage = (By.XPATH,"//div[@class='alert__message']")
        self.VisitYourWebsite = (By.XPATH,"//a[normalize-space(.)='Visit your website']")
        self.ClaimYourSpot = (By.CSS_SELECTOR, "button.btn.btn-pumpkin--outline")
        self.DashboardElements = (By.XPATH,"//div[@class='card mt-5 grid grid-cols-3 gap-5 p-4']/child::div[@class='card p-6']")
        self.ClientSummary = (By.XPATH,"//div[@class='card mt-7 grid grid-cols-3 gap-5 p-4']/child::div[@class='card p-6']")
        self.DashboardElementsContents = (By.XPATH,"//div[contains(@class,'card mt-5 grid grid-cols-3 gap-5 p-4')]//preceding::h2")
        self.ClientSummaryContents =(By.XPATH,"//div[contains(@class,'card mt-5 grid grid-cols-3 gap-5 p-4')]/following::h2")
        self.WeeklyClientFilter = (By.ID,"dashboard-chart-dropdown")
        self.weekly_client_filter_options = (By.XPATH,"//ul[@class='w-30 py-2']/li")

    def dashboard(self):
        self.wait.until(EC.invisibility_of_element_located(self.ToastMessage))

        visit_your_website = self.wait.until(EC.presence_of_element_located(self.VisitYourWebsite))
        assert visit_your_website.is_displayed(), "Visit Your Website link is not visible on the dashboard"
        assert visit_your_website.is_enabled(), "Visit Your Website link is not enabled on the dashboard"
        assert "Visit your website" in visit_your_website.text, "Visit Your Website link text is incorrect"

        claim_your_spot = self.wait.until(EC.presence_of_element_located(self.ClaimYourSpot))
        assert claim_your_spot.is_displayed(), "Claim Your Spot button is not visible on the dashboard"
        assert claim_your_spot.is_enabled(), "Claim Your Spot button is not enabled on the dashboard"
        assert "Claim Your Spot" in claim_your_spot.text, "Claim Your Spot button text is incorrect"

        dashboard_elements = self.wait.until(EC.presence_of_all_elements_located(self.DashboardElements))
        dashboard__contents = self.wait.until(EC.presence_of_all_elements_located(self.DashboardElementsContents))
        dashboard__contents = [option.text.strip() for option in dashboard__contents]
        assert dashboard__contents == dashboard_contents, "Dashboard elements contents do not match expected values"
        assert len(dashboard_elements) == 6, "Expected 6 dashboard elements, but found {}".format(len(dashboard_elements))

        client_summary = self.wait.until(EC.presence_of_all_elements_located(self.ClientSummary))
        client_summary__contents = self.wait.until(EC.presence_of_all_elements_located(self.ClientSummaryContents))
        client_summary__contents = [option.text.strip() for option in client_summary__contents]
        assert client_summary__contents == client_summary_contents, "Client Summary contents do not match expected values"
        assert len(client_summary) == 3, "Expected 3 client summary elements, but found {}".format(len(client_summary))

        weekly_client_filter = self.wait.until(EC.presence_of_element_located(self.WeeklyClientFilter))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", weekly_client_filter)
        assert weekly_client_filter.is_displayed(), "Weekly Client Filter dropdown is not visible on the dashboard"
        assert weekly_client_filter.is_enabled(), "Weekly Client Filter dropdown is not enabled on the dashboard"
        assert "This Week" in weekly_client_filter.text, "Weekly Client Filter dropdown text is incorrect"

        weekly_client_filter.click()
        time.sleep(1)

        filter_options = self.wait.until(EC.presence_of_all_elements_located(self.weekly_client_filter_options))
        expected_options = ["This Week", "This Month"]
        filter_texts = [option.text.strip() for option in filter_options]
        assert filter_texts == expected_options, f"Expected {expected_options}, got {filter_texts}"
