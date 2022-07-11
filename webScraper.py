import time
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# CLuster Database
cluster = MongoClient("mongodb+srv://damond:O76IfcRsXU1YxoPU@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority")

#Setting chrome driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.twitter.com/login")

time.sleep(3)

#account info
email = "daocodedayproject@gmail.com"
password = "Damond900"
username = "codedayproject" #For security check

#login xpaths
email_xpath = "//input[@autocomplete=\"username\"]"
password_xpath = "//input[@autocomplete=\"current-password\"]"
security_xpath = "//input[@autocomplete=\"on\"]"

#filling in username
username_input = driver.find_element(By.XPATH, email_xpath)
username_input.send_keys(email)
username_input.send_keys(Keys.RETURN)
time.sleep(1)

#security check
try:
    security_input = driver.find_element(By.XPATH, security_xpath)
    security_input.send_keys(username)
    security_input.send_keys(Keys.RETURN)
except:
    pass

time.sleep(1)


#filling in password
password_input = driver.find_element(By.XPATH, password_xpath)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

#give enough time for page to load
time.sleep(5)

tweet_xpath = "//article[@data-testid=\"tweet\"]"
tweet = driver.find_elements(By.XPATH, tweet_xpath)

def get_data(tweet):
    username_data = tweet.find_element(By.XPATH, ".//div[@data-testid=\"User-Names\"]//span").text
    handle_data = tweet.find_element(By.XPATH, ".//span[contains(text(), \"@\")]").text
    time_data = tweet.find_element(By.XPATH, ".//time").text
    text_data = tweet.find_element(By.XPATH, ".//div[@data-testid=\"tweetText\"]/span").text
    retweets_data = tweet.find_element(By.XPATH, ".//div[@data-testid=\"retweet\"]").text
    likes_data = tweet.find_element(By.XPATH, ".//div[@data-testid=\"like\"]").text

    #put in dictionary for database
    data = {
        "Username": username_data,
        "Handle": handle_data,
        "Time": time_data,
        "Text": text_data,
        "Number of Retweets": retweets_data,
        "Number of Likes": likes_data
    }
    return data

#adding into database
database = cluster["data"]
collection = database["twitter_data"]

collection.insert_one(get_data(tweet[0]))

driver.quit()
