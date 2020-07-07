from pages.base_page import Page
from pages.sign_in_page import SignIn
from pages.main_page import Main
from pages.cart_page import Cart
from pages.hamburger_menu_page import HamburgerMenu

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)

        self.main_page = Main(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.cart_page = Cart(self.driver)
        self.hamburger_menu_page = HamburgerMenu(self.driver)
