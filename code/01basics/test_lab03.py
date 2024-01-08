import time
from selenium import webdriver
def test_open_login():

    chrome_option = webdriver.ChromeOptions()
    #GIve some extra arguments or extentions or anything to chrome
    #Chrome with extension, Window size, proxy, JS Disable etc

    extension_path = 'C:/Users/Atul Patil/Downloads/Adblocker.crx'
    chrome_option.add_extension(extension_path)
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(options= chrome_option ) #Create a fresh session with POST req.
    driver.get("https://app.vwo.com/#/login")
    #driver.maximize_window()
    print(driver.title)
    time.sleep(100)
    driver.quit()
