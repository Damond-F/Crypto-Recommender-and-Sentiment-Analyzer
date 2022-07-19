import time
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

# CLuster Database
cluster = MongoClient('mongodb+srv://damond:O76IfcRsXU1YxoPU@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority')
database = cluster['data']
collection = database['google_news']

#Setting chrome driver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://ambcrypto.com/')

time.sleep(4)

search_term = 'aave'

ActionChains(driver)
try:
    search_button = driver.find_element(By.XPATH, './/span[@class="mvp-nav-search-but fa fa-search fa-2 mvp-search-click"]')
    search_button.click()                                                                                                                                                                                                                                                                                                       
except:
    pass

time.sleep(1)

search = driver.find_element(By.XPATH, './/div[@id="mvp-search-box"]//input')
search.send_keys(search_term)
time.sleep(0.5)
try:
    search.send_keys(Keys.RETURN)
except:
    pass

time.sleep(2)

articles = driver.find_elements(By.XPATH, './/li[@class="mvp-blog-story-wrap left relative infinite-post"]')
print(len(articles))

article_link = articles[1].find_element(By.XPATH, './/a').get_attribute('href')

print(article_link)

r = requests.get(article_link)
soup = BeautifulSoup(r.text, 'html.parser')
paragraphs = soup.find_all('p')

print(paragraphs)



time.sleep(12334)