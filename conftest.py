import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browserSetup():
    options = Options()
    if os.getenv('CI'):
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://partner.saauzi.com/")
    driver.maximize_window()
    yield driver
    driver.quit()