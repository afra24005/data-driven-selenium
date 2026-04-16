from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/forgot_password")

driver.find_element(By.ID, "email").send_keys("test@test.com")
driver.find_element(By.CSS_SELECTOR, "#form_submit").click()

time.sleep(50)
driver.quit()
