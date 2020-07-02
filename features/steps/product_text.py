from selenium.webdriver.common.by import By
from behave import given, when, then


RESULT = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div:last-child li")
TEXT_REGULAR = (By.CSS_SELECTOR, ".wfm-sales-item-card__regular-price")
PRODUCT_NAME = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")


@given('Open Amazon wholefoodsdesls page')
def open_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify all product has text Regular field and name')
def check_item(context):
    all_products = context.driver.find_elements(*RESULT)
    for item in all_products:
        if "Hundreds more in store. Look for the yellow signs." not in item.text:
            assert "Regular" in item.text, f"Expected to have Regular price in the item {item.text}"
            assert item.find_element(*PRODUCT_NAME), f"Expected item to have product name"
            print(item.find_element(*PRODUCT_NAME).text)







