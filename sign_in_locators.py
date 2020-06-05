from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.amazon.com/sign-in")

#Amazon
elem = driver.find_element(By.XPATH,"//div[@id='a-page']//a[@class='a-link-nav-icon']")
assert elem.get_attribute("class") == 'a-link-nav-icon'
#Email
elem = driver.find_element(By.XPATH,"//input[@id='ap_email']")
print(elem.get_attribute("name"))
assert elem.get_attribute("name") == 'email'
#Continue
elem = driver.find_element(By.XPATH,"//input[@id='continue']")
print(elem.get_attribute("type"))
assert elem.get_attribute("type") == 'submit'
#Need help?
elem = driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
print(elem.text)
assert elem.text == 'Need help?'
#Fogot your password
elem = driver.find_element(By.XPATH,"//a[@id='auth-fpp-link-bottom']")
print(elem.get_attribute("class"))
assert elem.get_attribute("class") == 'a-link-normal'
#Other issues with sign-in
elem = driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']")
print(elem.get_attribute("class"))
assert elem.get_attribute("class") == 'a-link-normal'
#CreateAccount
elem = driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']")
print(elem.get_attribute("tabindex"))
assert elem.get_attribute("tabindex") == '6'
#Conditions of Use
elem = driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
print(elem.text)
#Privacy Notice
elem = driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
print(elem.text)