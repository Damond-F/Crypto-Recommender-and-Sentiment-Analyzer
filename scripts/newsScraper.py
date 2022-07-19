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

driver.get('https://www.google.com/')

time.sleep(2)

search_term = 'aave coin yahoo'



# clicks next in google search
def click_next():
    ActionChains(driver)
    next_button_click = driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]')
    next_button_click.click()



#searches the term and returns list of article elements
def navigate(search_term):
    search = driver.find_element(By.XPATH, './/div/input[@class="gLFyf gsfi"]')
    search.send_keys(search_term)
    search.send_keys(Keys.RETURN)

    time.sleep(2)
    news_button_click = driver.find_element(By.XPATH, './/div[@class="MUFPAc"]//a').get_attribute('href')
    driver.get(news_button_click)

    time.sleep(2)

    articles = driver.find_elements(By.XPATH, '//*[@id="rso"]/div')

    return articles


# takes in article element and returns title, description, link
def get_data(article):
    article_title = article.find_element(By.XPATH, './/div[@class="mCBkyc y355M ynAwRc MBeuO nDgy9d"]').text
    article_description = article.find_element(By.XPATH, './/div[@class="GI74Re nDgy9d"]').text
    link = article.find_element(By.XPATH, './/a[@class="WlydOe"]').get_attribute('href')
    

    print(article_title)
    print(article_description)
    print(link)

    data = {
        'article title': article_title,
        'article description': article_description,
        'link': link
    }
    return data

coin = '$MANA'

article = get_data(navigate(coin + ' coin yahoo')[0])

url = article['link']


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
paragraphs = soup.find_all('p')

print(paragraphs)

p2 = [paragraph.text for paragraph in paragraphs]

print(p2)

p3 = []

for paragraph in p2:
    if ('$MANA' in paragraph):
        p3.append(paragraph)

print(p3)


time.sleep(11111)

driver.quit()

