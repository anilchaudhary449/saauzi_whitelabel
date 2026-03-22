import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browserSetup():
    driver = webdriver.Chrome()
    driver.get("https://partner.saauzi.com/")
    driver.maximize_window()
    yield driver
    driver.quit()