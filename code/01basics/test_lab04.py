from selenium import webdriver

def test_driver_navigation():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print("First Launching Page is: ", driver.title)
    driver.get("https://thetestingacademy.com/")
    print(driver.title)
    driver.back()
    print("Previous Title Was: " , driver.title)
    driver.forward()
    print("Next title is: ", driver.title)
    driver.refresh()
    print("Page is refreshed!")
    driver.quit() #driver.close is different than driver.quit