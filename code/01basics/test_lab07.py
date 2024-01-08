import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_vwo_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email = driver.find_element(By.NAME, "username")
    pwd = driver.find_element(By.NAME, "password")
    sign_in = driver.find_element(By.ID, "js-login-btn")
    email.send_keys("contact+atb5x@thetestingacademy.com")
    pwd.send_keys("ATBx@1234")
    sign_in.click()
    time.sleep(5)
    aman = driver.find_element(By.XPATH, "//span[@class='Fw(semi-bold) ng-binding']")
    #print(aman.text)
    assert aman.text == "Aman"
    time.sleep(5)
