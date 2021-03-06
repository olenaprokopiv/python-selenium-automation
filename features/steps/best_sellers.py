from selenium.webdriver.common.by import By
from behave import given, when, then


BESTSELLER = (By.CSS_SELECTOR, "#nav-xshop a[href*='bestseller']")
ALL_TAB = (By.CSS_SELECTOR, "#zg_tabs li")
BANNER_TEXT = (By.CSS_SELECTOR, "#zg_banner_text_wrapper")


@when('Click BestSellers button')
def click_bestSellers_button(context):
    context.driver.find_element(*BESTSELLER).click()


@then('Click on all tab and verify correct page opens')
def Click_all_tab(context):

    all_tab = context.driver.find_elements(*ALL_TAB)
    print(f'numlinks {len(all_tab)}')

    for li in range(len(all_tab)):

        tab_click = context.driver.find_elements(*ALL_TAB)[li]
        tab_text = tab_click.text

        tab_click.click()

        ban_text = context.driver.find_element(*BANNER_TEXT).text
        print(f'Tab text = {tab_text}, Banner text = {ban_text}')

        assert tab_text in ban_text, f'Expected{tab_text} to be in {ban_text}'

