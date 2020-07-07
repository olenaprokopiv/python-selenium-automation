from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Main(Page):
    ORDER_BUTTON_LOCATOR = (By.XPATH, "//a[@id='nav-orders']")
    CART_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".nav-cart-icon")
    HAMBURGER_MENU_LOCATOR = (By.CSS_SELECTOR, '#nav-hamburger-menu')

    def click_orders_button(self):
        self.wait_for_element_click(*self.ORDER_BUTTON_LOCATOR)

    def click_cart_button(self):
        self.wait_for_element_click(*self.CART_BUTTON_LOCATOR)

    def click_hamburger_menu(self):
        self.wait_for_element_click(*self.HAMBURGER_MENU_LOCATOR)

