from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button.radius")
    logout_button = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

    def logout(self):
        self.driver.find_element(*self.logout_button).click()
