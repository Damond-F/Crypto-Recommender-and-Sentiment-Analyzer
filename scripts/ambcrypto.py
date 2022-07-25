from pkgutil import get_data
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

        time.sleep(3)

        article_elements = self.navigate(search_term, driver)
        
        for article_element in article_elements:
            self.get_data(article_element)




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

        time.sleep(4)

        articles_elements = driver.find_elements(By.XPATH, './/li[@class="mvp-blog-story-wrap left relative infinite-post"]')

        return articles_elements



    def get_data(self, article_element):

        article_link = article_element.find_element(By.XPATH, './/a').get_attribute('href')
        
        r = requests.get(article_link)
        soup = BeautifulSoup(r.text, 'html.parser')

        paragraphs = soup.find_all('span', style='font-weight: 400;')

        

        data = {
            'link': article_link
        }

        print(paragraphs)

        return data




    def writeData(self, data):
        # CLuster Database
        cluster = MongoClient('mongodb+srv://damond:O76IfcRsXU1YxoPU@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority')
        database = cluster['data']
        collection = database['ambcrypto']

        collection.insert_one(data)