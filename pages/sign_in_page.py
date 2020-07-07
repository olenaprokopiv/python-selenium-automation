from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignIn(Page):
    SIGN_IN_TEXT= (By.XPATH, "//h1[@class='a-spacing-small']")

    def open(self):
        self.open_page('https://www.amazon.com/')


    def verify_sign_in_text(self, text):
        self.verify_text(text, *self.SIGN_IN_TEXT)

