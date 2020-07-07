from selenium.webdriver.common.by import By
from pages.base_page import Page

class HamburgerMenu(Page):
    AMAZON_MUSIC = (By.XPATH, "//div[@id='hmenu-content']//a[@class='hmenu-item']//div[text()='Amazon Music']")
    MAIN_MENU_LOCATOR = (By.XPATH, "//ul[@class='hmenu hmenu-visible hmenu-translateX']//li//a[@class='hmenu-item']")


    def click_amazon_music(self):
        self.wait_for_element_click(*self.AMAZON_MUSIC)

    def get_menu_item_list(self, expected_items):
        elem_links_list = self.driver.find_elements(*self.MAIN_MENU_LOCATOR)
        n_expected_items = int(expected_items)
        print(len(elem_links_list))
        n_elem = len(elem_links_list)
        if n_elem > 0:
            assert n_elem == n_expected_items, f'expected {n_expected_items}, but got {n_elem}'
        else:
            print('Menu elements are not found')
