from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC


BLOG_LINK = (By.XPATH, "//*[contains(text(), 'See daily updates at blog.aboutamazon.com')]")
BLOG_UPDATES = (By.XPATH, "//*[contains(text(), 'daily updates')]")


@when('Click on blog link {updates}')
def blog_link(context, updates):
    context.original_windows = context.driver.window_handles
    print(context.original_windows)
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print("curr window before blog link click = ", context.driver.current_window_handle)
    context.wait.until(EC.element_to_be_clickable(BLOG_LINK))
    context.driver.find_element(*BLOG_LINK).click()
    print("curr window after blog link click = ", context.driver.current_window_handle)


@when('Switch to the new opened window')
def switch_window(context):
    context.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print(current_windows)
    for old_window in context.original_windows:
        current_windows.remove(old_window)
    print(current_windows)
    print("window before switch = ", context.driver.current_window_handle )
    context.driver.switch_to_window(current_windows[0])
    print("window after switch = ", context.driver.current_window_handle)



@then('Amazon Blog {text} is opened')
def verify_blog_open(context, text):
    #context.wait.until(EC.visibility_of_element_located(BLOG_UPDATES))
    context.wait.until(EC.presence_of_all_elements_located(BLOG_UPDATES))
    assert context.driver.find_element(*BLOG_UPDATES), f"Expected to find {text} on the page"


@then('User can close new window and switch back to original')
def close_and_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)




