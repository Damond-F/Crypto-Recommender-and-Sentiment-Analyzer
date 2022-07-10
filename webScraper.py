import time
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome


# CLuster Database
cluster = MongoClient("mongodb+srv://damond:O76IfcRsXU1YxoPU@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority")

#Setting chrome driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.twitter.com/login")

time.sleep(1)

#account info
email = "<email>"
password = "<password>"
username = "<username>" #For security check

#login xpaths
email_xpath = "//input[@autocomplete=\"username\"]"
password_xpath = "//input[@autocomplete=\"current-password\"]"
security_xpath = "//input[@autocomplete=\"on\"]"

#filling in username
username_input = driver.find_element(By.XPATH, email_xpath)
username_input.send_keys(email)
username_input.send_keys(Keys.RETURN)
time.sleep(0.5)

#security check

security_input = driver.find_element(By.XPATH, security_xpath)
security_input.send_keys(username)
security_input.send_keys(Keys.RETURN)
time.sleep(0.5)


#filling in password
password_input = driver.find_element(By.XPATH, password_xpath)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
time.sleep(0.5)
