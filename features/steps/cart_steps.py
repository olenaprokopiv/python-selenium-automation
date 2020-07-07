from behave import given, when, then

@then('Verify {text} text present')
def verify_cart_text(context, text):
    context.app.cart_page.cart_is_empty(text)