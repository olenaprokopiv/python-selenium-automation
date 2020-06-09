from behave import given, when, then
from selenium.webdriver.common.by import By

CART_EMPTY_TEXT = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")

@when('Click cart button')
def click_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon").click()

@then('Verify text {text} on the cart page')
def verify_cart_empty_text(context, text):
    verify_text = context.driver.find_element(*CART_EMPTY_TEXT).text
    assert verify_text == 'Your Amazon Cart is empty', f'incorect text: {text}.'
