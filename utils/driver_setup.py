from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    service = Service("./drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
