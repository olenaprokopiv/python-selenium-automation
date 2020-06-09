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


#CSS locators for Create Account (Registration) page elements

#Amazon logo
elem_l = driver.find_element(By.CSS_SELECTOR, "i.a-icon-logo")

#Create account
elem_a = driver.find_element(By.CSS_SELECTOR, "h1")

#Your name
elem_n = driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#Email
elem_e = driver.find_element(By.CSS_SELECTOR, "#ap_email")

#Password
elem_p = driver.find_element(By.CSS_SELECTOR, "#ap_password")

# i
elem_i = driver.find_element(By.CSS_SELECTOR, "div.auth-inlined-information-message i")

#Passwords must be at least 6 characters.
elem_c = driver.find_element(By.CSS_SELECTOR, "div.auth-inlined-information-message .a-alert-content")

#Re-enter password
elem_ch = driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#Create your Amazon account
elem_ac = driver.find_element(By.CSS_SELECTOR, "#continue")

#Conditions of Use
elem_con = driver.find_element(By.CSS_SELECTOR, "a[href*='notification_condition']")

#Privacy Notice.
elem_pr = driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy']")

# Sign-In
elem_si = driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")







