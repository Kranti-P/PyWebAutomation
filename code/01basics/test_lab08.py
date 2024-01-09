import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_vwo_navigation():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email= driver.find_element(By.XPATH, "//input[@id='login-username']")
    pwd = driver.find_element(By.XPATH, "//li/input[@type='password']")
    sign_in =driver.find_element(By.XPATH, "//li/button[@type='submit' and @id= 'js-login-btn']")
    email.send_keys("contact+atb5x@thetestingacademy.com")
    pwd.send_keys("ATBx@1234")
    sign_in.click()
    time.sleep(5)
    testing= driver.find_element(By.XPATH, "//button[@data-qa='nav-main-test']")
    testing.click()
    time.sleep(5)
    multivar= driver.find_element(By.XPATH, "//a[@href='#/test/multivariate']")
    #multivar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
    # "//a[@href='#/test/multivariate']")))
    multivar.click()
    time.sleep(5)
    driver.maximize_window()
    time.sleep(5)
    create_test_btn = driver.find_element(By.XPATH, "//button[@type='button' and @data-qa='rumuhacelo']")
    create_test_btn.click()
    time.sleep(5)
    driver.quit()

