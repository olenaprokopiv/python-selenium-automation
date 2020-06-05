from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.amazon.com/gp/help/customer/display.html")

search = driver.find_element(By.ID, "helpsearch")
search.clear()
search.send_keys('cancel order')

submit_button = driver.find_element(By.XPATH, "//input[@class='a-button-input']")
submit_button.click()

verify_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
assert verify_text == 'Cancel Items or Orders', f'incorect text: {verify_text}.'

driver.quit()