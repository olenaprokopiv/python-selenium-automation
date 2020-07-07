from behave import given, when, then


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.app.hamburger_menu_page.click_amazon_music()

@then('{expected_items} menu items are present')
def get_elem_links_list(context, expected_items):
    context.app.hamburger_menu_page.get_menu_item_list(expected_items)