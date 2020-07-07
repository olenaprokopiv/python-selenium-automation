from behave import given, when, then

@when('Click Amazon Orders link')
def click_orders_button(context):
    context.app.main_page.click_orders_button()


@when('Click on cart icon')
def click_cart_button(context):
    context.app.main_page.click_cart_button()


@when('Click on hamburger menu')
def click_hamburger_menu(context):
    context.app.main_page.click_hamburger_menu()