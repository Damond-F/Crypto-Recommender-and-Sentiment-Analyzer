import time
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class googleNews:
    def __init__(self, search_term, coin_symbol):
        print('adfasfd')
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        driver = webdriver.Chrome(PATH)

        driver.get('https://www.google.com/')
        time.sleep(2)

        article_elements = self.navigate(search_term, driver)
        time.sleep(2)

        for article_element in article_elements:
            self.writeData(self.get_data(article_element, coin_symbol))
        
        driver.quit()


    # clicks next in google search
    def click_next(self, driver):
        ActionChains(driver)
        next_button_click = driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]')
        next_button_click.click()



    #searches the term and returns list of article elements
    def navigate(self, search_term, driver):
        search = driver.find_element(By.XPATH, './/div/input[@class="gLFyf gsfi"]')
        search.send_keys(search_term)
        search.send_keys(Keys.RETURN)

        time.sleep(2)
        news_button_click = driver.find_element(By.XPATH, './/div[@class="MUFPAc"]//a').get_attribute('href')
        driver.get(news_button_click)

        time.sleep(2)

        articles_elements = driver.find_elements(By.XPATH, '//*[@id="rso"]/div')

        return articles_elements



    # takes in article element and returns title, description, link
    def get_data(self, article, coin_symbol):
        article_title = article.find_element(By.XPATH, './/div[@class="mCBkyc y355M ynAwRc MBeuO nDgy9d"]').text
        article_description = article.find_element(By.XPATH, './/div[@class="GI74Re nDgy9d"]').text
        link = article.find_element(By.XPATH, './/a[@class="WlydOe"]').get_attribute('href')
        

        print(article_title)
        print(article_description)
        print(link)

        data = {
            'coin symbol': coin_symbol,
            'article title': article_title,
            'article description': article_description,
            'link': link
        }
        return data



    def writeData(self, data):
        # CLuster Database
        cluster = MongoClient('mongodb+srv://damond:O76IfcRsXU1YxoPU@cluster0.qxhzvno.mongodb.net/?retryWrites=true&w=majority')
        database = cluster['data']
        collection = database['google_news']

        collection.insert_one(data)



