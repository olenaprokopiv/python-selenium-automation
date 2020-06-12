from behave import given, when, then
from selenium.webdriver.common.by import By


HELP_SEARCH = (By.ID, "helpsearch" )
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".a-button-input")
CANCEL_ORDER_TEXT = (By.CSS_SELECTOR, ".help-content h1")


@given('Open Amazon Help page')
def open_amazon_help_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@when('Search for Cancel order')
def search_for_cancel(context):
    search = context.driver.find_element(*HELP_SEARCH)
    search.clear()
    search.send_keys('cancel order')


@when('Click submit button')
def click_submit_button(context):
    submit_button = context.driver.find_element(*SUBMIT_BUTTON)
    submit_button.click()


@then('Verify text {text} is shown')
def verify_text(context, text):
    verify_text = context.driver.find_element(*CANCEL_ORDER_TEXT).text
    assert verify_text == 'Cancel Items or Orders', f'incorect text: {verify_text}.'