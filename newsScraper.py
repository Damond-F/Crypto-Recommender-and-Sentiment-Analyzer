import time
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def click_next():
    ActionChains(driver)
    next_button_click = driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]')
    next_button_click.click()

# CLuster Database
cluster = MongoClient('mongodb+srv://damond:O76IfcRsXU1YxoPU@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority')
database = cluster['data']
collection = database['google_news']

#Setting chrome driver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com/')

time.sleep(2)

search_term = 'aave coin'

search = driver.find_element(By.XPATH, './/div/input')
search.send_keys(search_term)
search.send_keys(Keys.RETURN)

time.sleep(2)
news_button_click = driver.find_element(By.XPATH, './/div[@class="MUFPAc"]//a').get_attribute('href')
driver.get(news_button_click)

time.sleep(2)

articles = driver.find_elements(By.XPATH, '//*[@id="rso"]/div')

def get_data(article):
    article_title = article.find_element(By.XPATH, './/div[@class="mCBkyc y355M ynAwRc MBeuO nDgy9d"]').text
    article_description = article.find_element(By.XPATH, './/div[@class="GI74Re nDgy9d"]').text
    time = article.find_element(By.XPATH, './/div[@class="OSrXXb ZE0LJd"]').text

    print(article_title)
    print(article_description)
    print(time)

    data = {
        'article title': article_title,
        'article description': article_description,
        'time': time
    }
    return data

for article in articles:
    collection.insert_one(get_data(article))

time.sleep(11111)

driver.quit()

