from selenium.webdriver.common.by import By
from behave import given, when, then

TEXT_REGULAR = (By.CSS_SELECTOR, "div.a-section ul.s-col-2 li div.a-text-left span.wfm-sales-item-card__regular-price")
PRODUCT_INFO = (By.CSS_SELECTOR, "div.a-section ul.s-col-2 li div.a-text-left")
PRODUCT = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name.a-text-bold")

@given('Open Amazon wholefoodsdesls page')
def open_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then('Verify all product has text Regular')
def product_text(context):
    text_regular = context.driver.find_elements(*TEXT_REGULAR)

    count_found = 0
    count_not_found = 0
    for elem in text_regular:
        if 'Regular' in elem.text:
            count_found += 1
        else:
            count_not_found += 1

    print('Regular text found = ', count_found)
    print('Regular text not found = ', count_not_found)


@then('Verify each product has a Name')
def product_name(context):
    product_info_list = context.driver.find_elements(*PRODUCT_INFO)

    n_not_found = 0
    n_found = 0

    for elem in product_info_list:
        try:
           elem_prod = elem.find_element(*PRODUCT)
           n_found += 1
        except:
            n_not_found += 1
    print('Found product names = ', n_found)
    print('Not found product names = ', n_not_found)
    assert (n_not_found == 0)







