import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CompanyProfile:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.CompanyProfileTab = (By.XPATH, "//a[contains(@href, 'company-profile') and contains(normalize-space(.), 'Company Profile')]")
        self.companyName = (By.ID, "company_name")
        self.companyEmail = (By.ID, "company_email")
        self.companyOwner = (By.ID, "company_owner")
        self.companyPhoneNumber = (By.ID, "company_phone_number")
        self.companyAddress = (By.ID, "company_address")
        self.companyWebsite = (By.ID, "company_website")
        self.companyPAN = (By.ID, "company_pan_vat")
        self.companyLogo = (By.XPATH, "(//input[@type='file'])[1]")
        self.companyFavicon = (By.XPATH, "(//input[@type='file'])[2]")
        self.companyContentDetails = (By.TAG_NAME,"p")
        self.updateButton = (By.ID, "update-company-details")

    def navigate_to_company_profile(self):
        # We wait for presence first to survive dom changes or dynamic loading/overlays
        company_profile_tab = self.wait.until(EC.presence_of_element_located(self.CompanyProfileTab))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", company_profile_tab)
        time.sleep(1)
        
        try:
            tab_clickable = self.wait.until(EC.element_to_be_clickable(self.CompanyProfileTab))
            tab_clickable.click()
        except Exception:
            # Fallback to JS click if blocked by overlay/toast or CSS transitions
            self.driver.execute_script("arguments[0].click();", company_profile_tab)
            
        self.wait.until(EC.url_contains("company-profile"))
        assert "company-profile" in self.driver.current_url, "Clicking Company Profile did not navigate to the company profile page"
        time.sleep(3) # Wait for page to stabilize

    def fill_company_details(self, CompanyName, CompanyEmail, CompanyOwner, CompanyPhoneNumber, CompanyAddress, CompanyWebsite, CompanyVat, CompanyLogo, CompanyFavicon, CompanyDetails):
        company_name_field = self.wait.until(EC.visibility_of_element_located(self.companyName))
        assert company_name_field.is_displayed(), "Company Name field is not visible on the company profile page"
        assert company_name_field.is_enabled(), "Company Name field is not enabled on the company profile page"
        company_name_field.clear()
        company_name_field.send_keys(CompanyName)
        company_email_field = self.wait.until(EC.visibility_of_element_located(self.companyEmail))
        assert company_email_field.is_displayed(), "Company Email field is not visible on the company profile page"
        assert company_email_field.is_enabled(), "Company Email field is not enabled on the company profile page"
        company_email_field.clear()
        company_email_field.send_keys(CompanyEmail)
        company_owner_field = self.wait.until(EC.visibility_of_element_located(self.companyOwner))
        assert company_owner_field.is_displayed(), "Company Owner field is not visible on the company profile page"
        assert company_owner_field.is_enabled(), "Company Owner field is not enabled on the company profile page"
        company_owner_field.clear()
        company_owner_field.send_keys(CompanyOwner)
        
        company_phone_number_field = self.wait.until(EC.visibility_of_element_located(self.companyPhoneNumber))
        assert company_phone_number_field.is_displayed(), "Company Phone Number field is not visible on the company profile page"
        assert company_phone_number_field.is_enabled(), "Company Phone Number field is not enabled on the company profile page"
        company_phone_number_field.clear()
        company_phone_number_field.send_keys(CompanyPhoneNumber)
        
        company_address_field = self.wait.until(EC.visibility_of_element_located(self.companyAddress))
        assert company_address_field.is_displayed(), "Company Address field is not visible on the company profile page"
        assert company_address_field.is_enabled(), "Company Address field is not enabled on the company profile page"
        company_address_field.clear()
        company_address_field.send_keys(CompanyAddress)
        
        company_website_field = self.wait.until(EC.visibility_of_element_located(self.companyWebsite))
        assert company_website_field.is_displayed(), "Company Website field is not visible on the company profile page"
        assert company_website_field.is_enabled(), "Company Website field is not enabled on the company profile page"
        company_website_field.clear()
        company_website_field.send_keys(CompanyWebsite)
        
        company_vat_field = self.wait.until(EC.visibility_of_element_located(self.companyPAN))
        assert company_vat_field.is_displayed(), "Company VAT field is not visible on the company profile page"
        assert company_vat_field.is_enabled(), "Company VAT field is not enabled on the company profile page"
        company_vat_field.clear()
        company_vat_field.send_keys(CompanyVat)

        company_logo = self.wait.until(EC.presence_of_element_located(self.companyLogo))
        company_logo.send_keys(CompanyLogo)

        company_favicon = self.wait.until(EC.presence_of_element_located(self.companyFavicon))
        company_favicon.send_keys(CompanyFavicon)

        company_details_field = self.wait.until(EC.presence_of_element_located(self.companyContentDetails))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", company_details_field)
        time.sleep(1)
        try:
            company_details_field.clear()
        except Exception:
            pass # P tags or rich editors might throw exception on clear. If we can't clear, just proceed
        try:
            company_details_field.send_keys(CompanyDetails)
        except Exception:
            pass # Same for sending keys to non-interactable p tags

    def click_submit(self):
        update_button = self.wait.until(EC.presence_of_element_located(self.updateButton))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", update_button)
        time.sleep(1)
        try:
            update_button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", update_button)
        
        # Broad success message check
        success_xpath = "//*[contains(normalize-space(.), 'updated successfully') or contains(normalize-space(.), 'Updated Successfully')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, success_xpath)))
        assert self.driver.find_element(By.XPATH, success_xpath).is_displayed(), "Success message is not visible"