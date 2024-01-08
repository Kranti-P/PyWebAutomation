from selenium import webdriver
def test_open_login():
    driver = webdriver.Chrome() #Create a fresh session with POST req.
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    print(driver.title)
