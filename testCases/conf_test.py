from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()       
    return driver
