from behave import given, when, then


@then('Verify {text} page is opened')
def verify_sign_in_text(context, text):
    context.app.sign_in_page.verify_sign_in_text(text)



