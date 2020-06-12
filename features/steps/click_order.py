from behave import given, when, then
from selenium.webdriver.common.by import By


ORDERS_BUTTON_LOCATOR = (By.XPATH, "//span[@class='nav-line-2' and text()='& Orders']")
EMAIL_FIELD_LOCATOR = (By.ID, "ap_email")


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Orders')
def clic_orders_button(context):
    context.driver.find_element(*ORDERS_BUTTON_LOCATOR).click()


@then('Verify Sign in page opened')
def Verify_page_opened(context):
    context.driver.find_element(*EMAIL_FIELD_LOCATOR)


@then('Verify URL has {expected_url}')
def verify_signin_url(context, expected_url):
    current_url = context.driver.current_url
    assert expected_url in current_url, f'incorrect url, got: {current_url}'
    print(context.driver.current_url)