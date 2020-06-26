from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "ul.imageSwatches li")
SELECT_COLOR = (By.CSS_SELECTOR, "div#variation_color_name span.selection")


@given ('Open Amazon product page')
def open_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify select through color')
def verify_select_color(context):
    expcolor =['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    coloptions = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(coloptions)):
        coloptions[i].click()
        select_color_text = context.driver.find_element(*SELECT_COLOR).text
        assert select_color_text == expcolor[i]