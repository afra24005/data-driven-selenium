from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("wrong")
driver.find_element(By.ID, "password").send_keys("wrong")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

time.sleep(50)
driver.quit()
