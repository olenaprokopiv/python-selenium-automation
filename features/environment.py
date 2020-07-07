from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context

    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)
    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStep step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context,feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


