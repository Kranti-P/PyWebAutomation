from selenium import webdriver
import logging

def test_open_login():
    driver = webdriver.Chrome() #Create a fresh session with POST req.
    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    print(driver.title)
    LOGGER.info(driver.title)

