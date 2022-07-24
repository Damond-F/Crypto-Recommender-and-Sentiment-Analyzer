import time
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests



class ambcrypto:
    def __init__(self, search_term):
        #Setting chrome driver
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        driver = webdriver.Chrome(PATH)

        driver.get('https://ambcrypto.com/')

        time.sleep(4)



    def navigate(self, search_term, driver):
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



    def get_data(self, driver):

        articles = driver.find_elements(By.XPATH, './/li[@class="mvp-blog-story-wrap left relative infinite-post"]')
        print(len(articles))

        article_link = articles[1].find_element(By.XPATH, './/a').get_attribute('href')

        r = requests.get(article_link)
        soup = BeautifulSoup(r.text, 'html.parser')
        paragraphs = soup.find_all('p')

        print(paragraphs)


    def writeData(self, data):
        # CLuster Database
        cluster = MongoClient('mongodb+srv://damond:O76IfcRsXU1YxoPU@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority')
        database = cluster['data']
        collection = database['ambcrypto']

        collection.insert_one(data)



time.sleep(12334)