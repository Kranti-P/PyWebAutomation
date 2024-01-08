import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_vwo_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    username= driver.find_element(By.ID, "login-username")
    pwd = driver.find_element(By.ID, "login-password")
    sign_in = driver.find_element(By.ID, "js-login-btn")

    username.send_keys("sdasdsad")
    pwd.send_keys("sadad")
    sign_in.click()
    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    time.sleep(5)
    #print("Message is: ", error_msg.text)
    assert(error_msg.text == 'Your email, password, IP address or location did not match', "PASS", "FAIL")
    driver.quit()