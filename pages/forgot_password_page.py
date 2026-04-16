from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):

    email = (By.ID, "email")
    retrieve_btn = (By.ID, "form_submit")

    def submit_email(self, email_value):
        self.driver.find_element(*self.email).send_keys(email_value)
        self.driver.find_element(*self.retrieve_btn).click()
