from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ORDERS_BUTTON_LOCATOR = (By.XPATH, "//span[@class='nav-line-2' and text()='& Orders']")
TEXT_SAGN_IN = (By.XPATH, "//div[contains(@class,'a-box-inner')]/h1")

@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')

@when('Click Orders')
def clic_orders_button(context):
    context.driver.find_element(*ORDERS_BUTTON_LOCATOR).click()

@then('Verify Sign in page opened')
def Verify_page_opened(context):
    text = context.driver.find_element(*TEXT_SAGN_IN).text
    assert 'Sign-In' in text, f'incorrect text: {text}'
