from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
#from selenium.webdriver.support import expected_conditions as EC


SEARCH_BOX = (By.ID, "twotabsearchtextbox")
SEARCH_BUTTON = (By.CSS_SELECTOR, "div.nav-search-submit input.nav-input")
IMAGE_ITEM = (By.CSS_SELECTOR, "div h2.a-size-mini a")
ADD_CART = (By.ID, 'add-to-cart-button')
POPUP_CART = (By.CSS_SELECTOR, "i.a-icon.a-icon-close")
CART_BUTTON = (By.ID, "hlb-view-cart")
DROPDOWN = (By.CSS_SELECTOR, ".a-dropdown-prompt")

@when('Search item {text}')
def search_item(context, text):
    elem = context.driver.find_element(*SEARCH_BOX)
    elem.clear()
    elem.send_keys("Alexa")


@when('Click search Button')
def click_search_button(context):
    butt = context.driver.find_element(*SEARCH_BUTTON)
    butt.click()


@when('Click image of the first item')
def click_image(context):
    elements = context.driver.find_elements(*IMAGE_ITEM)
    elements[0].click()


@when('Click add to the cart')
def add_to_cart(context):
    but = context.driver.find_element(*ADD_CART).click()


@when('Close popup')
def close_popup(context):
    try:
        sleep(4)
        #context.wait.until(EC.presence_of_element_located(*POPUP_CART))
        #context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "i.a-icon.a-icon-close")))
        #context.wait.until((EC.element_to_be_clickable(*POPUP_CART)))
        popup = context.driver.find_element(*POPUP_CART)
        popup.click()
    except:
        print("popup not found")


@then('Number of items in the cart more than zero')
def more_zero(context):
    cart_button = context.driver.find_element(*CART_BUTTON)
    cart_button.click()

    elem = context.driver.find_element(*DROPDOWN)
    numstr = elem.text
    if int(numstr) > 0:
        print("Number of items in the cart more than zero")