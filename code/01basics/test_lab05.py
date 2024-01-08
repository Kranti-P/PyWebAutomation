import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_katalon():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_Appointment_btn = driver.find_element(By.ID, "btn-make-appointment")
    make_Appointment_btn.click()
    time.sleep(10)
    driver.quit()
